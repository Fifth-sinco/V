from email import message
from http import client
import discord
import json
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if payload.member.bot:
            pass
        
        else:
            with open('./cogs/roles.json') as x:
                data = json.loads(x)
                for x in data:
                    if x ['emoji'] == payload.emoji.name:
                        role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                        await payload.member.add_role(role)
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        
            with open('./cogs/roles.json') as x:

                data = json.loads(x)
                for x in data:
                    if x ['emoji'] == payload.emoji.name:
                        role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

    @commands.command()
    async def roles(self, ctx, emoji, role: discord.Role, *, text):
        
        emb = discord.Embed(description=text)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)

        with open('./cogs/roles.json') as x:
            data = json.load(x)

            new_react_role ={
                'role_name':role.name,
                'role_id':role.id,
                'emoji':emoji,
                'message_id':msg.id
            }

            data.append(new_react_role)

        with open('./cogs/roles.json','w') as x:
            json.dump(data, x, indent=4)

def setup(client):
    client.add_cog(Roles(client))
 