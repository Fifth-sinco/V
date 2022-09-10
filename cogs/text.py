import discord
from discord.ext import commands

class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def BI(self, ctx, *, text):
        """Bold-Italic text"""
        await ctx.channel.purge(limit=1)
        await ctx.send(f'***{text}***')
    
    @commands.command()
    async def I(self, ctx, *, text):
        """Italic text"""
        await ctx.channel.purge(limit=1)
        await ctx.send(f'*{text}*')

    @commands.command()
    async def B(self, ctx, *, text):
        """Bold text"""
        await ctx.channel.purge(limit=1)
        await ctx.send(f'**{text}**')

    @commands.command()
    async def S(self, ctx, *, text):
        """Strikethrough text"""
        await ctx.channel.purge(limit=1)
        await ctx.send(f'~~{text}~~')

async def setup(client):
    client.add_cog(Text(client))
 
