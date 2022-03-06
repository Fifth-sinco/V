import asyncio
from http import client
import discord
from discord.ext import commands
from discord.utils import get

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

songs = asyncio.Queue()
play_next_song = asyncio.Event()

async def audio_player_task():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()

def toggle_next():
    client.loop.call_soon_threadsafe(play_next_song.set)

@commands.command(pass_context=True)
async def play(ctx, url):
    if not client.voice_clients(ctx.message.guild):
        voice = await client.join_voice_channel(ctx.message.author.voice_channel)
    else:
       voice = client.voice_client_in(ctx.message.guild)

    player = await voice.create_ytdl_player(url, after=toggle_next)
    await songs.put(player)


def setup(client):
    client.add_cog(Music(client))