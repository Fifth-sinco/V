import discord
from discord.ext import commands

class Defaults(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot online')

    @commands.command()
    async def ping(self, ctx):
        """Check for Bot Latency"""
        await ctx.send(f'Ping = {round(self.client.latency * 1000)}ms')
        
    @commands.command()
    async def clear(self, ctx, amount=5):
        """Clears a set amount of messeges in the specified channel. Default is 5."""
        await ctx.channel.purge(limit=1+amount)

def setup(client):
    client.add_cog(Defaults(client))
