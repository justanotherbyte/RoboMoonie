import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("no fuck you. you're on a cooldown")

def setup(bot):
    bot.add_cog(Errors(bot))