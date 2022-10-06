import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):

    await member.create_dm()
    await member.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

    channel = client.get_channel(476753911819141120) # put your server's channel ID here
    print(channel)
    await channel.send(f"{member} has arrived!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(os.environ.get("TOKEN"))