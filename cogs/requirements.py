import discord
from discord.ext import commands

class Requirement(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reg(self, ctx):
      
        embed = discord.Embed(title= "PRC Online Application Registration", description = "1st step before passing the required documents")
        embed.add_field(name = "1. LERIS Registration" , value = "- https://online.prc.gov.ph/ ", inline = False)
        embed.add_field(name = "2. 2x2 Soft Copy", value= "- Formal attire \n - White background \n- No eyeglasses \n- Not more than 6 months from the date of submission", inline = False)
        embed.add_field(name = "3. Payment", value = "- REE Exam: 900php \n- RME - 600php \n- payment can be done thru GCash or Paymaya", inline = False)
        embed.set_footer(text = "Information above are based on PRC Application requirements for April 2022 Exams")
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
            
    @commands.command()
    async def prc(self, ctx):
 
        embed = discord.Embed(title= "PRC Application Requirements", description = "Step after online registration (LERIS)")
        embed.add_field(name = "1. Birth Certificate (PSA, NSO)" , value = "- can be acquired thru psahelpline.ph or psaserbilis.com.ph \n- can be processed thru SM or SaveMore", inline = False)
        embed.add_field(name = "2. PSA Marriage Certificate", value= "- for married female applicants", inline = False)
        embed.add_field(name = "3. Transcript of Records (*TOR*)", value = "- school: for board exam purposes, picture, school logo, date of graduation \n- *PRC does not accept TOR without Remarks*", inline = False)
        embed.add_field(name = "4. Payment", value = "- Electronic Official Receipt (EOR, can be acquired on LERIS)  \n- prepare 50 php for metered stamp when filing for NOA (*Notice of Admission*)", inline = False)
        embed.add_field(name = "5. 4 Passport Size Pictures", value = "- White Background \n- Collared (formal) \n- Name at the bottom", inline = False)
        embed.add_field(name = "6. Metered Documentary Stamps", value = "- PRC Office (forms, Payment, passing of requirements, purchase of stamps, mailing envelop) \n- can be bought to room watchers on exam day  \n-    *Price: 35php*", inline = False)
        embed.add_field(name = "7. Community Tax Certificate (CEDULA)", value = "- Municipal office \n- LTO or any valid ID will suffice", inline = False)
        embed.add_field(name = "8. NC-2", value = "- for RME takers")
        embed.add_field(name = "9. Certificate of Apprenticeship", value = "- for RME takers")
        embed.set_footer(text = "Prepare 3-4 photocopies of each document, Original copies are for verification only. \nInformation above are based on PRC Application requirements for April 2022 Exams and IIEE Midyear Convention of 2022")
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.command()
    async def exam(self, ctx):
        embed = discord.Embed(title= "Exam things to bring", description = "Check the Program Breakdown")
        embed.add_field(name = "1. Notice of Admission" , value = "- acquired thru PRC office or LERIS(For repeat takers)", inline = False)
        embed.add_field(name = "2. Calculator", value = "- Preffered Casio FX-570ES Plus \n- Prohibited calculators : fx-991ES/EX Plus and other programmable calculators")
        embed.add_field(name = "3. No.2 Pencils", value= "- 2 to 4 pieces along with a sharpener and eraser", inline = False)
        embed.add_field(name = "4. Health Declaration Forms", value = "- Annex A: https://www.prc.gov.ph/sites/default/files/Annex%20A%20-%20Informed%20ConsentNov2020.docx \n- Annex B : https://www.prc.gov.ph/sites/default/files/Annex%20B%20-%20Health%20Declaration%20FormNov2020.docx \n- Annex C: https://www.prc.gov.ph/sites/default/files/Annex%20C%20-%20Post%20Examination%20Health%20Surveillance%20FormNov2020.docx \n - Annex C is to be Passed 15 days after the examination", inline = False)
        embed.add_field(name = "5. Ballpen", value = "- Black pen only", inline = False)
        embed.add_field(name = "6. Long brown Envelope", value = "- 1 piece for documents", inline = False)
        embed.add_field(name = "7. Plastic Envelope", value = "- serves as bag for thing to bring", inline = False)
        embed.add_field(name = "8. Vaccination Card", value = "- photocopy \n- bring the original for verification.")
        embed.add_field(name = "9. RT-PRC", value = "- 3 days before the exam day. \n- optional if you have a photocopy of Vaccination card ", inline = False)
        embed.add_field(name = "10. OR or EOR", value = "- prepare 2 to 3 copies. ", inline = False)
        embed.add_field(name = "11. Money", value = "- 35php \n- for mailing evelope and metered stamp \n- to be bought from the room watcher", inline = False)
        embed.set_footer(text = "Prepare 3-4 photocopies of each document, Original copies are for verification only. \nInformation above are based on PRC Application requirements for April 2022 Exams and IIEE Midyear Convention of 2022")
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    @commands.command()
    async def oath(self, ctx):
        embed = discord.Embed(title= "Oath Taking Requirements", description = "For Exam Passers")
        embed.add_field(name = "1. Notice of Admission (NOA)" , value = "- for identification and verification purposes", inline = False)
        embed.add_field(name = "2. Duly Accomplised Oath Form or Panunumpa ng Propesyonal", value = "- Panunumpa ng Propesyonal: https://www.prc.gov.ph/uploaded/documents/1.%20Panunumpa%20ng%20Propesyonal.pdf",  inline = False)
        embed.add_field(name = "3. Two (2) pieces of passport-sized ID", value = "- photo in white background and with complete name tag", inline = False)
        embed.add_field(name = "4. Two (2) sets of documentary stamp", value = "- can be acquired directly on PRC offices", inline = False)
        embed.add_field(name = "5. One (1) piece short brown envelope", value = "- for filing", inline = False)
        embed.add_field(name = "6. IIEE Membership Reciept", value = "- can be processed online or directly at IIEE Main Office. \n- Reggistration Link: https://membership.iiee.org.ph/ee/index.php/appform?fbclid=IwAR1OnXO-fifrYEPgo7UF-kbf78WFNyPZO9-6e9tlv9abtCQR_XNSEjrk0Ec \n- Registration Guide: https://iiee.org.ph:89/uploads/files/1109.pdf \n- for questions not detailed on Guide, contact Ma'am Alma Larce, IIEE Membership Department Head: larce_alma@yahoo.com.ph", inline = False)
        embed.add_field(name = "7. Money (100 php) Metered Stamp", value = "- purchased on PRC Office", inline = False)
        embed.add_field(name = "8. Screenshots (for E-Oath, Print out)", value = "- atleast 4 screenshots", inline = False)
        embed.set_footer(text = "Information above are based on PRC Requirement for April 2022")
        
        

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    
async def setup(client):
    await client.add_cog(Requirement(client))
