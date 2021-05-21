import discord
import aiohttp
import asyncio
import config
import wavelink
import itertools
import subprocess
import sys
import asyncpg
from discord.ext import commands, menus
from typing import List, Iterable, Union
from utils.classes import EmbedPaginator, PaginatorPageSource
from utils.help import RMHelp


class NodeLogColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




class RoboMoonie(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.bl_pg = kwargs.pop("bl_pg_conn")
        super().__init__(*args, **kwargs)
        self._BotBase__cogs = commands.core._CaseInsensitiveDict()
        self.session = aiohttp.ClientSession()
        self.wavelink = wavelink.Client(bot=self)
        self.wavelink_nodes = []
        self.loop = asyncio.get_event_loop()
        self.config = config
        self.bl_cache = {}
        for ext in self.config.EXTENSIONS:
            self.load_extension(ext)
            print(f"[{ext}] Loaded")

        if "cogs.music" in self.config.EXTENSIONS:
            self.loop.create_task(self.boot_lavalink())
            self.loop.create_task(self.connect_nodes(nodes = 10))

    async def on_ready(self):
        print(f"Ready: {self.user} (ID: {self.user.id})")

    async def create_paginator(self, ctx : commands.Context, embeds : List[discord.Embed], *, start = False) -> EmbedPaginator:
        base_menu = menus.MenuPages(PaginatorPageSource(embeds, per_page = 1))
        paginator = EmbedPaginator(ctx, base_menu)
        if start:
            await paginator.run()
            return paginator
        return paginator


    def chunk(self, iterable : Iterable, n : int) -> list:
        it = iter(iterable)
        while True:
            chunk = tuple(itertools.islice(it, n))
            if not chunk:
                return
            yield chunk

    async def process_commands(self, message):
        user = self.bl_cache.get(message.author.id)
        if user is None:
            return await super().process_commands(message)


    async def blacklist_user(self, user : Union[discord.Member, discord.User], reason : str):
        await self.bl_pg.execute("INSERT INTO blacklists VALUES($1, $2)", user.id, reason)
        self.bl_cache.update({
            user.id : reason
        })

    async def whitelist_user(self, user : Union[discord.Member, discord.User]):
        await self.bl_pg.execute("DELETE FROM blacklists WHERE user_id = $1", user.id)
        self.bl_cache.pop(user.id, None)



    
    async def connect_nodes(self, *, nodes : int = 1, required_node_count : int = 1, max_retries : int = 10):
        await self.wait_until_ready()
        can_connect = asyncio.Event()
        while not can_connect.is_set():
            try:
                resp = await self.session.get("http://127.0.0.1:8000", headers = {"Authorization" : "youshallnotpass"})
                print(NodeLogColours.WARNING + f"Connection Test: {resp.status}" + NodeLogColours.ENDC)
                can_connect.set()
            except Exception as e:
                print(e)
                await asyncio.sleep(1)
        for i in range(nodes):
            retries = 0
            node_name = f"WavelinkNode:{i}"
            node_ev = asyncio.Event()
            while not node_ev.is_set():
                print(NodeLogColours.WARNING + f"Trying to connect to node: {node_name}" + NodeLogColours.ENDC)
                try:
                    node = await self.wavelink.initiate_node(host='127.0.0.1',
                                              port=8000,
                                              rest_uri='http://127.0.0.1:8000',
                                              password='youshallnotpass',
                                              identifier=node_name,
                                              region='us_central')

                    self.wavelink_nodes.append(node)
                    node_ev.set()
                    print(NodeLogColours.OKGREEN + f"Node Created: {node_name}" + NodeLogColours.ENDC)

                except Exception as exc:
                    print(NodeLogColours.FAIL + "ERROR OCCURED" + NodeLogColours.ENDC)
                    print(NodeLogColours.FAIL + exc + NodeLogColours.ENDC)
                    await asyncio.sleep(1)
                    retries += 1
                    if retries == max_retries:
                        if len(nodes) < required_node_count:
                            print(NodeLogColours.FAIL + "Node Connection Failure" + NodeLogColours.ENDC)
                            await self.close()
                        else:
                            print(NodeLogColours.WARNING + "Node Connection Failure: Required Node Count Reached" + NodeLogColours.ENDC)

                

    
    async def boot_lavalink(self):
        command = "java -jar {}".format(self.config.LAVALINK_JAR_PATH)
        command = command.split(" ")
        subprocess.Popen(command + sys.argv[1:])
    
        

    
    async def logout(self):
        return await self.close()

    async def close(self):
        await self.session.close()
        for node in self.wavelink_nodes:
            await self.wavelink.destroy_node(identifier = node.identifier)
            print(NodeLogColours.OKGREEN + f"Node Destroyed: {node.identifier}" + NodeLogColours.ENDC)
        await super().close()
        


    




async def launch():
    bl_pg_conn = await asyncpg.connect(config.BLACKLIST_PG_URI)
    results = await bl_pg_conn.fetch("SELECT * FROM blacklists")
    bot = RoboMoonie(command_prefix = ["hey mon ", "hey moan ", "hey cum "], case_insensitive = True, intents = config.PRIVILEGED_INTENTS, help_command = RMHelp(), bl_pg_conn = bl_pg_conn)
    for user in results:
        bot.bl_cache.update({
            user["user_id"] : user["reason"]
        })
    await bot.start(bot.config.TOKEN)

asyncio.get_event_loop().run_until_complete(launch())