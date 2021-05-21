from discord.ext import commands
from utils.parsers import EmbedParsers



class Kitsu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = self.bot.session
        self.base = "https://kitsu.io/api/edge"
        self.category = "Anime"
        self.name = "<:kitsu:844288205149962261> Kitsu"

    @commands.command(usage = "<query>", help = "Searches for Anime")
    async def anime(self, ctx, *, query : str):
        query = query.replace(" ", r"%20")
        url = f"{self.base}/anime?filter[text]={query}"
        async with ctx.channel.typing():
            async with self.session.get(url) as response:
                data = await response.json()
                embeds = await EmbedParsers.parseforsearch(data, self.bot.config.EMBED_COLOUR)
                paginator = await self.bot.create_paginator(ctx, embeds)
                
        await paginator.run()
        await ctx.message.add_reaction("✅")


    @commands.command(usage = "<query>", help = "Searches for Manga")
    async def manga(self, ctx, *, query : str):
        query = query.replace(" ", r"%20")
        url = f"{self.base}/manga?filter[text]={query}"
        async with ctx.channel.typing():
            async with self.session.get(url) as response:
                data = await response.json()
                embeds = await EmbedParsers.parseforsearch(data, self.bot.config.EMBED_COLOUR, manga = True)
                paginator = await self.bot.create_paginator(ctx, embeds)
                
        await paginator.run()
        await ctx.message.add_reaction("✅")


    
            

    
    


def setup(client):
    client.add_cog(Kitsu(client))