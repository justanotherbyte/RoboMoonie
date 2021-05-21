import discord
from discord.ext import commands

class RMHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        channel = self.get_destination()
        bot = self.context.bot
        embed = discord.Embed(
            title = "Help Panel",
            description = f"```diff\n- [] = optional argument\n- <> = required argument\n- Do NOT type these when using commands!\n+ Type {self.context.prefix}help [command | module] for more help on a command or module!\n```\n[Server](https://discord.gg/QJSEmAQ) | [Developer](https://discord.com/users/691406006277898302)\n\nRemember, to be able to add RoboMoonie, you must DM the developer for permission!",
            colour = bot.config.EMBED_COLOUR
        )
        embed.set_image(url = "https://secure-asset-delivery.gameforge.com/partnersite_live_product/4aba1528-9c08-46cd-ad57-2d324191d312/2cc57e9d-b1f6-4cfd-bfa2-fa131d950f102020-05-07_SW_TNT_Library_Title_Banner_1920x620.png")
        cog_names = []
        for cog, _ in mapping.items():
            cog_name = getattr(cog, "name", None)
            if cog_name is None:
                continue
            cog_names.append("•" + f"**{cog_name}**")
        

        embed.add_field(name = "Modules:", value = "\n".join(cog_names), inline = True)
        embed.add_field(name = "News - 18/05/2021", value = "Some news, oh ik. Komodo is gay", inline = True)
        await channel.send(embed = embed)

    async def send_cog_help(self, cog):
        channel = self.get_destination()
        bot = self.context.bot
        embed = discord.Embed(
            colour = bot.config.EMBED_COLOUR,
            title = cog.name
        )
        for command in cog.get_commands():
            embed.add_field(name = command.name, value = "`" + self.get_command_signature(command) + "`", inline = True)

        await channel.send(embed = embed)


    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        channel = self.get_destination()
        bot = self.context.bot
        embed = discord.Embed(
            title = "Command Help",
            description = f"Command: `{command.name}`",
            colour = bot.config.EMBED_COLOUR
        )
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/816760746087546951/845337689036554250/022cf00f-d55b-4ec4-afc6-22c8896bd842.png")
        aliases = "`No Aliases`"
        if len(command.aliases) != 0:
            aliases = ", ".join([f"`{alias}`" for alias in command.aliases])
        embed.add_field(name = "Aliases", value = aliases, inline = True)
        embed.add_field(name = "Signature", value = f"`{self.get_command_signature(command)}`", inline = True)
        return await channel.send(embed = embed)