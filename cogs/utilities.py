import discord
import psutil
import humanize
import sys
from discord.ext import commands
from typing import Union
from utils.clients import PistonClient


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "<:utilities:844292940352192602> Utilities"
        self.process = psutil.Process()
        self.piston = PistonClient(self.bot.session)

    @commands.command(aliases = ["sys"])
    async def system(self, ctx):
        memory_usage = humanize.naturalsize(self.process.memory_full_info().uss / 1024**2)
        cpuUsage = self.process.cpu_percent() / psutil.cpu_count()
        cpuCount = psutil.cpu_count()
        embed = discord.Embed(
            title = "System Information",
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.add_field(name = "Library Version", value = discord.__version__, inline = True)
        embed.add_field(name = "Memory Usage", value = f"{memory_usage}", inline = True)
        embed.add_field(name = "CPU Usage", value = f"{cpuUsage}%", inline = True)
        embed.add_field(name = "CPU Cores", value = f"{cpuCount}", inline = True)
        embed.add_field(name = "OS", value = sys.platform, inline = True)
        embed.add_field(name = "Version Information", value = f"{sys.version}", inline = True)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_guild_permissions(manage_guild = True)
    async def uploademoji(self, ctx, link : str, *, name : str):
        name = name.replace(" ", "_")
        resp = await self.bot.session.get(link)
        botes = await resp.read()
        emoji = await ctx.guild.create_custom_emoji(name = name, image = botes)
        await ctx.send(f"`<:{emoji.name}:{emoji.id}>`")

    @commands.command()
    @commands.is_owner()
    async def blacklist(self, ctx, user : Union[discord.User, discord.Member], *, reason : str = "None given"):
        await ctx.send("Blacklisting some skid....")
        await self.bot.blacklist_user(user, reason)
        await ctx.send(f"Blacklisted {user.mention}")

    @commands.command()
    @commands.is_owner()
    async def whitelist(self, ctx, user : Union[discord.User, discord.Member]):
        await ctx.send("Whitelisting a pog person....")
        await self.bot.whitelist_user(user)
        await ctx.send(f"Whitelisted {user.mention}")


def setup(bot):
    bot.add_cog(Utilities(bot))