import discord
from discord.ext import commands

class Bleh(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def k(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send('**Bahala ka jan**')
    
    @commands.command()
    async def h(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send('**HAHAHA**')

    @commands.command()
    async def r(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send('**tanggal na**')

def setup(client):
    client.add_cog(Bleh(client))
