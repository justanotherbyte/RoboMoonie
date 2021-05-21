import discord
import re
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from utils.clients import PistonClient
# rust: 1.50.0

class Piston(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.piston = PistonClient(self.bot.session)
        self.cb_regex = re.compile(r"`{3}([a-z]+)((?:\n[^`]+)+)`{3}`")
        self.name = "<:websocket:845037081007751209> Piston"

    @commands.command(aliases = ["py"])
    @commands.cooldown(1, 5, BucketType.user)
    async def python(self, ctx, *, code : str):
        code = code.strip("```").strip("python")
        result = await self.piston.request("/piston/execute/", code, "python", "3.9.4")
        output = result.get("run").get("output")
        status = int(result.get("run").get("code"))
        works = True
        if status != 0:
            works = False
        embed = await self.format_embed(code, "python", works, output)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["rs"])
    @commands.cooldown(1, 5, BucketType.user)
    async def rust(self, ctx, *, code : str):
        code = code.strip("```").strip("rust")
        if "fn main" not in code:
            await ctx.send(r"No `main` function found in `rust` code. Wrapping with boostrap `fn main() {}`")
            code = """
            fn main() {
            """
            code += "\n\t" + code
            code += "\n}"
        result = await self.piston.request("/piston/execute/", code, "rust", "1.50.0")
        output = result.get("run").get("output")
        status = int(result.get("run").get("code"))
        works = True
        if status != 0:
            works = False
        embed = await self.format_embed(code, "rust", works, output)
        await ctx.send(embed = embed)


    async def format_embed(self, code : str, lang : str, works : bool, output : str) -> discord.Embed:
        colour = discord.Colour.red()
        if works:
            colour = discord.Colour.green()

        embed = discord.Embed(
            title = "Code Executed",
            colour = colour
        )
        embed.add_field(name = "Code", value = f"```{lang}\n{code}\n```", inline = False)
        embed.add_field(name = "Output", value = f"```sh\n{output}\n```", inline = False)
        embed.set_footer(text = f"Language: {lang}")
        return embed


def setup(bot):
    bot.add_cog(Piston(bot))