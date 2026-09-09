import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


def run_cmd(cmd, array_of_arguments):
    print(cmd, array_of_arguments)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    parts = message.content.split()
    if not parts:
        return

    cmd = parts[0]
    array_of_arguments = parts[1:]

    run_cmd(cmd, array_of_arguments)


async def main():
    async with client:
        await client.start(TOKEN)


asyncio.run(main())