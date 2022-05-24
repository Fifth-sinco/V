import discord
from discord.ext import commands

class Tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def conv(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'***{text}***')
    
    @commands.command()
    async def cons(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'*{text}*')

    @commands.command()
    async def geom(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send('**{text}**')

def setup(client):
    client.add_cog(Tools(client))
 