import discord
import config as cfg
from bot_news_interface import BotNewsInterface

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$news"):

        digest = message.content.split()

        if (len(digest) < 2):
            await message.channel.send("You can select business, science, sports, or technology.\nFormat: $news query\nex. $news science\n")

        else:
            query = digest[1]
            if (query in cfg.NEWS_QUERIES):
                ret_msg = BotNewsInterface.default_query(query)
            else:
                ret_msg = BotNewsInterface.custom_query(query)

            if (not len(ret_msg)):
                await message.channel.send(f"No results found for {query}")
            else:
                for story in ret_msg:
                    await message.channel.send(story)

client.run(cfg.BOT_TOKEN)