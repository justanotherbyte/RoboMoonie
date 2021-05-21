import discord
from io import BytesIO
from utils.clients import KawaiiRedClient
from discord.ext import commands



class Weeb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.name = "<:weebmin:844316832419545090> Weeb"
        self.kawaiired = KawaiiRedClient(self.bot.session, self.bot.config.KAWAII_RED_TOKEN)

    @commands.command()
    async def waifu(self, ctx):
        resp = await self.bot.session.get("https://api.waifu.pics/sfw/waifu")
        data = await resp.json()
        resp = await self.bot.session.get(data.get("url"))
        botes = await resp.read()
        buffer = BytesIO(botes)
        f = discord.File(buffer, filename = "waifu.png")
        await ctx.send(file = f)

    @commands.command()
    async def quote(self, ctx):
        resp = await self.bot.session.get("https://animechan.vercel.app/api/random")
        data = await resp.json()
        anime = data.get("anime")
        character = data.get("character")
        quote = data.get("quote")
        embed = discord.Embed(
            description = quote,
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_footer(text = f"Character: {character} | Anime: {anime}")
        await ctx.send(embed = embed)

    @commands.command()
    async def kiss(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Nice try kissing yourself. Maybe get a gf? or if you're komodo, get a bf?")
        
        data = await self.kawaiired.request("/gif/kiss/")
        embed = discord.Embed(
            description = "pog. **{}** kissed **{}**".format(ctx.author.display_name, member.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)
    @commands.command()
    async def hug(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Nice try hugging yourself. Maybe get a gf? or if you're komodo, get a bf?")
        
        data = await self.kawaiired.request("/gif/hug/")
        embed = discord.Embed(
            description = "pog. **{}** hugged **{}**".format(ctx.author.display_name, member.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)
    
    @commands.command()
    async def cry(self, ctx):
        
        data = await self.kawaiired.request("/gif/hug/")
        embed = discord.Embed(
            description = "**{}** cries lol".format(ctx.author.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def fbi(self, ctx):
        
        data = await self.kawaiired.request("/gif/fbi/")
        embed = discord.Embed(
            description = "**{}** - idk wtf to put here".format(ctx.author.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def lick(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Nice try licking yourself. Maybe get a gf? or if you're komodo, get a bf?")
        
        data = await self.kawaiired.request("/gif/lick/")
        embed = discord.Embed(
            description = "pog. **{}** licked **{}**".format(ctx.author.display_name, member.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def shoot(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Nice try shooting yourself. Maybe get a gf? or if you're komodo, get a bf?")
        
        data = await self.kawaiired.request("/gif/shoot/")
        embed = discord.Embed(
            description = "pog. **{}** shot **{}**".format(ctx.author.display_name, member.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def uwu(self, ctx):
        data = await self.kawaiired.request("/gif/uwu/")
        embed = discord.Embed(
            description = "uwu. wtf do u expect",
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def wiggle(self, ctx):
        data = await self.kawaiired.request("/gif/wiggle/")
        embed = discord.Embed(
            description = "what am i making",
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def brr(self, ctx):
        data = await self.kawaiired.request("/gif/brr/")
        embed = discord.Embed(
            description = "**{}** go brrrrrr".format(ctx.author.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)

    @commands.command()
    async def protect(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Nice try protecting yourself. Maybe get a gf? or if you're komodo, get a bf?")

        data = await self.kawaiired.request("/gif/protect/")
        embed = discord.Embed(
            description = "**{}** simps for **{}**".format(ctx.author.display_name, member.display_name),
            colour = self.bot.config.EMBED_COLOUR
        )
        embed.set_image(url = data["response"])
        await ctx.send(embed = embed)




   


def setup(bot):
    bot.add_cog(Weeb(bot))