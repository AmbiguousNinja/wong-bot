import os
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('WONG_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    # skip bot messages
    if message.author.bot:
        return

    msg_clean = message.content.lower()
    msg_raw   = message.content

    if "wong" in msg_clean:
        await message.channel.send("wong!")
    elif msg_raw == "HASHIRIDASHITA":
        await message.channel.send("https://external-preview.redd.it/ztDm-Hvs6h1pbqYSFF3wRore5-cpi7-jM1Odpu_N9_I.jpg?auto=webp&s=4f07f33f33fd7af89c3774a737939bd5ba0ed754")
    elif "umaru" in msg_clean:
        await message.channel.send("I'm sorry I didn't understand that. Did you mean: https://abbeypartyrentals.com/images/stories/virtuemart/product/trash_with_liner.jpg")
    elif "nico" in msg_clean.split(" "):
        await message.channel.send("How about nico nico no?")
    elif "nana" in msg_clean.split(" "):
        await message.channel.send("https://64.media.tumblr.com/ff27fbde60837edb3596ff31424b4ee4/afbb96a6f0cb6227-5f/s1280x1920/86051a9723f25e9d2d42f2d301bd67a39d45975a.png")

@client.event
async def on_member_join(member):
    await member.edit(nick="wong")

client.run(TOKEN)
