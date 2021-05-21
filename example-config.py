import discord

TOKEN = "ODE2MDcyMDg1MzY1MTk0Nzky.YD1oWw.X3zVo1-A5j3NPemQ_0wENgbQdqI"

EXTENSIONS = (
    "jishaku",
    "cogs.images",
    "cogs.utilities",
    "cogs.kitsu",
    "cogs.anime",
    "cogs.piston",
    "cogs.errors",
)

BASE_INTENTS = discord.Intents.default()
BASE_INTENTS.presences = True
BASE_INTENTS.members = True

PRIVILEGED_INTENTS = BASE_INTENTS
LAVALINK_JAR_PATH = "Lavalink.jar"
EMBED_COLOUR = 0xebb145

DAGPI_TOKEN = "W107VMmlIMH1u4vA9sTk90fg83vo6TdqzEj2jd5sMvKU4vXm6yrhfMLtdPvdOM26"
KAWAII_RED_TOKEN = "691406006277898302.AGyHLQFkscYDUFKOywzd"
BLACKLIST_PG_URI = "postgres://lcizdlei:rer8vPuXFPyUO450VkQy93ja1suUeeOc@tai.db.elephantsql.com/lcizdlei"