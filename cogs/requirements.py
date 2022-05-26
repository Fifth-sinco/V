import discord
from discord.ext import commands

class Requirement(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prc(self, ctx):
        embed = discord.Embed(title= "**PRC Application Requirements**", description = "Step after online registration (LERIS)")
        embed.add_field(name = "**1. Birth Certificate (PSA, NSO)**" , value = "- can be acquired thru psahelpline.ph or psaserbilis.com.ph \n- can be processed thru SM or SaveMore", inline = False)
        embed.add_field(name = "**2. PSA Marriage Certificate**", value= "- for married female applicants", inline = False)
        embed.add_field(name = "**3. Transcript of Records (*TOR*)**", value = "-    school: for board exam purposes, picture, school logo, date of graduation \n- *PRC does not accept TOR without Remarks*", inline = False)
        embed.add_field(name = "**4. PAYMENT**", value = "- REE Exam: 900php \n- RME - 600php \n- prepare 50 php for metered stamp when filing for NOA (*Notice of Admission*) \n- payment can be done thru GCash or Paymaya", inline = False)
        embed.add_field(name = "**5. 4 Passport Size Pictures**", value = "- White Background \n- Collared (formal) \n- Name at the bottom", inline = False)
        embed.add_field(name = "**6. Metered Documentary Stamps**", value = "- PRC Office (forms, Payment, passing of requirements, purchase of stamps, mailing envelop) \n- can be bought to room watchers on exam day  \n-    *Price: 35php*", inline = False)
        embed.add_field(name = "**7. Community Tax Certificate (CEDULA)**", value = "- Municipal office \n- LTO or any valid ID will suffice", inline = False)
        embed.set_footer(text = "Prepare 3-4 photocopies of each document, Original copies are for verification only. \nInformation above are based on PRC Application requirements for April 2022 Exams")
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.command()
    async def oath(self, ctx):
        embed = discord.Embed(title= "**Oath Taking Requirements**", description = "For Exam Passers")
        embed.add_field(name = "**1. Notice of Admission (NOA)**" , value = "- for identification and verification purposes", inline = False)
        embed.add_field(name = "**2. Duly Accomplised Oath Form or Panunumpa ng Propesyonal**", value = "- can be acquired on PRC Website",  inline = False)
        embed.add_field(name = "**3. Two (2) pieces of passport-sized ID**", value = "- photo in white background and with complete name tag", inline = False)
        embed.add_field(name = "**4. Two (2) sets of documentary stamp**", value = "- can be acquired directly on PRC offices", inline = False)
        embed.add_field(name = "**5. One (1) piece short brown envelope**", value = "- for filing", inline = False)
        embed.add_field(name = "**6. IIEE Membership Reciept**", value = "- can be processed online or directly at IIEE Main Office. ", inline = False)
        embed.set_footer(text = "Information above are based on PRC Requirement for April 2022")
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(Requirement(client))