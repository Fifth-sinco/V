import discord
from discord.ext import commands

class Calc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, left : int, right : int):
        """Adds two numbers together."""
        await ctx.send(left + right)
    
    @commands.command()
    async def sub(self, ctx, left : int, right : int):
        """Subtract two numbers together."""
        await ctx.send(left - right)

    @commands.command()
    async def x(self, ctx, left : int, right : int):
        """Multiply two numbers together."""
        await ctx.send(left * right)

    @commands.command()
    async def div(self, ctx, left : int, right : int):
        """Divide two numbers together."""
        await ctx.send(left / right)

def setup(client):
    client.add_cog(Calc(client))
