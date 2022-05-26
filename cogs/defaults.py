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
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Ping = {round(self.client.latency * 1000)}ms')
        
    @commands.command()
    async def clear(self, ctx, amount=5):
        """Clears a set amount of messeges in a channel. Default is 5."""
        await ctx.channel.purge(limit=1+amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        """Kicks a tagged user."""
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        """Bans a tagged user."""
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for {reason}.')

    @commands.command()
    async def unban(self, ctx, *, member):
        """"Unban a previously banned user."""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} has been unbanned.')
                return

def setup(client):
    client.add_cog(Defaults(client))
