import discord
from discord.ext import commands

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bi(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'***{text}***')
    
    @commands.command()
    async def i(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'*{text}*')

    @commands.command()
    async def b(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**{text}**')
    
    @commands.command()
    async def s(self, ctx, *, text):
        await ctx.channel.purge(limit=1)
        await ctx.send('~~{text}~~')

def setup(client):
    client.add_cog(Text(client))
 
