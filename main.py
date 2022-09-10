import discord
import asyncio
import typing
import os
from discord.ext import commands


client = commands.Bot(command_prefix = '!',intents=discord.Intents.all())

@client.command()
async def load(ctx, extension):
    """Loads a Cog"""
    await client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    """Unloads a Cog"""
    client.unload_extension(f'cogs.{extension}')

async def load_extensions(): 
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODAyMDQ3NjIyMTU5NjYzMTM0.YApjDg.RDzgHW6TvTP2JvhmbkUp1HQkUtI')
