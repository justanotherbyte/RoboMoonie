import discord
from discord.ext import commands
from typing import Union
from utils.clients import DagpiClient


                

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dagpi = DagpiClient(self.bot.session, self.bot.config.DAGPI_TOKEN)
        self.name = "<:dagpi:844289057503707209> Images"

    
    @commands.command()
    async def pixel(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/pixel/", url = url)
        file = discord.File(fp = buffer, filename = "processed.png")
        await ctx.send(file = file)

    @commands.command(aliases = ["colors"])
    async def colours(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/colors/", url = url)
        file = discord.File(fp = buffer, filename = "processed.png")
        await ctx.send(file = file)

    @commands.command()
    async def wag(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(ctx.author.avatar_url_as(format = "png"))
        url2 = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/whyareyougay/", url = url, url2 = url2)
        file = discord.File(fp = buffer, filename = "processed.gif")
        await ctx.send(file = file)

    """@commands.command(name = "5g1g")
    async def _5g1g(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(ctx.author.avatar_url_as(format = "png"))
        url2 = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/5g1g/", url = url, url2 = url2)
        file = discord.File(fp = buffer, filename = "processed.png")
        await ctx.send(file = file)"""


    @commands.command()
    async def trigger(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/triggered/", url = url)
        file = discord.File(fp = buffer, filename = "processed.gif")
        await ctx.send(file = file)

    @commands.command()
    async def magik(self, ctx, member : Union[discord.User, discord.Member] = None):
        member = member or ctx.author
        url = str(member.avatar_url_as(format = "png"))
        buffer = await self.dagpi.request("/image/magik/", url = url)
        file = discord.File(fp = buffer, filename = "processed.gif")
        await ctx.send(file = file)

    

    




def setup(bot):
    bot.add_cog(Images(bot))