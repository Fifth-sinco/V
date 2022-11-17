#headers 
import discord
import asyncio
import os
from discord.ext import commands
from os import environ
from dotenv import load_dotenv

#loads token file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#declaration of prefix
client = commands.Bot(command_prefix = '!',intents=discord.Intents.all())

#load and unload a COG commands
@client.command()
async def load(ctx, extension):
    """Loads a Cog"""
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    """Unloads a Cog"""
    client.unload_extension(f'cogs.{extension}')

#scans Cogs Folder for Files
async def load_extensions(): 
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

#logs in the bot after loading all cogs
async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)
        
asyncio.run(main())