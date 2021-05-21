import discord
from datetime import datetime

class EmbedParsers():
    @staticmethod
    async def parseforsearch(data : dict, colour : discord.Colour, manga : bool = False):
        data = data.get("data")
        
        embeds = []
        if manga is False:
            for x in data:
                attrs = x.get("attributes")
                trailer_video_id = attrs.get("youtubeVideoId")
                trailer_link = "https://www.youtube.com/watch?v={}".format(trailer_video_id)
                rating = attrs.get("averageRating")
                subtype = attrs.get("subtype")
                status = attrs.get("status")
                popularity = attrs.get("popularityRank")
                episodes = attrs.get("episodeCount")
                episode_length = attrs.get("episodeLength")
                description = attrs.get("description")
                en_title = attrs.get("titles").get("en") or attrs.get("titles").get("en_us") or attrs.get("titles").get("en_jp")
                jp_title = attrs.get("titles").get("ja_jp")
                image = attrs.get("posterImage").get("original")
                age_rating = attrs.get("ageRating")
                nsfw = str(attrs.get("nsfw"))
                description = description[:350]
                description = description + "..."
                embed = discord.Embed(
                    title = f"{en_title}\n*{jp_title}*",
                    colour = colour,
                    description = description,
                    timestamp = datetime.utcnow()
                )
                embed.add_field(name = "Stats:", value = f"**Rating:** `{rating}/100`\n**Popularity:** `{popularity}`\n**Episode Count:** `{episodes}`\n**Episode Length:** `{episode_length}min`", inline = True)
                embed.add_field(name = "Resources:", value = f"**Trailer:** [`Click`]({trailer_link})\n**Age Rating:** `{age_rating}`\n**NSFW:** `{nsfw}`\n**Platform:** `{subtype} | {status}`", inline = True)
                embed.set_thumbnail(url = image)
                embeds.append(embed)

            return embeds
        else:
            for x in data:
                attrs = x.get("attributes")
                trailer_video_id = attrs.get("youtubeVideoId")
                trailer_link = "https://www.youtube.com/watch?v={}".format(trailer_video_id)
                rating = attrs.get("averageRating")
                subtype = attrs.get("subtype")
                status = attrs.get("status")
                popularity = attrs.get("popularityRank")
                episodes = attrs.get("episodeCount")
                episode_length = attrs.get("episodeLength")
                description = attrs.get("description")
                en_title = attrs.get("titles").get("en") or attrs.get("titles").get("en_us") or attrs.get("titles").get("en_jp")
                jp_title = attrs.get("titles").get("ja_jp")
                image = attrs.get("posterImage").get("original")
                age_rating = attrs.get("ageRating")
                nsfw = str(attrs.get("nsfw"))
                description = description[:350]
                description = description + "..."
                embed = discord.Embed(
                    title = f"{en_title}\n*{jp_title}*",
                    colour = colour,
                    description = description,
                    timestamp = datetime.utcnow()
                )
                embed.add_field(name = "Stats:", value = f"**Rating:** `{rating}/100`\n**Popularity:** `{popularity}`", inline = True)
                embed.add_field(name = "Resources:", value = f"**Trailer:** [`Click`]({trailer_link})\n**Age Rating:** `{age_rating}`\n**Platform:** `{subtype} | {status}`", inline = True)
                embed.set_thumbnail(url = image)
                embeds.append(embed)

            return embeds

