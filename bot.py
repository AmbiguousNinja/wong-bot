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
    msg_clean = message.content.lower()
    msg_raw   = message.content
    if "wong" in msg_clean:
        await message.channel.send("nice")
    elif msg_raw == "HASHIRIDASHITA":
        await message.channel.send("https://external-preview.redd.it/ztDm-Hvs6h1pbqYSFF3wRore5-cpi7-jM1Odpu_N9_I.jpg?auto=webp&s=4f07f33f33fd7af89c3774a737939bd5ba0ed754")
    elif "umaru" in msg_clean:
        await message.channel.send("I'm sorry I didn't understand that. Did you mean: https://abbeypartyrentals.com/images/stories/virtuemart/product/trash_with_liner.jpg")
@client.event
async def on_member_join(member):
    await member.edit(nick="wong")
    await member.channel.send("welcome to wong, wong")

client.run(TOKEN)
