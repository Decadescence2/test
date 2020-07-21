import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

FFA = False

MyID = '<@339508544409829376>'
VossID = '<@215985007326527488>'
BaldwinID = '<@248950488731484161>'
JayID = '<@380887572970340362>'
ConnorID  = '<@151063490168094721>'
AaronID = '<@176810214257852416>'
NiallID = '<@246568122457391105>'
PeteID = '<@400336685084311552>'
SimonID = '<@374657763269410836>'

class Spammers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Spammer Code Loaded')
    def IDCheck(ctx):
        return ctx.message.author.id == 339508544409829376

    @commands.command()
    async def ToggleFFA(ctx):
        if FFA == False:
            FFA = True
            print (FFA)
            await message.channel.send('Free For All mode: Enabled')
        if FFA == True:
            FFA = False
            print (FFA)
            await message.channel.send('Free For All mode: Disabled')

    @commands.command()
    async def SpamTest(self, ctx, *, question):
        if FFA == False:
            @commands.check(IDCheck)
            spamnumber = 0
            while spamnumber < int(question):
                    await ctx.send('**LURKING!?** ' + MyID);
                    await asyncio.sleep(1)
                    spamnumber += 1
                    print ({spamnumber})
        if FFA == True:
            spamnumber = 0
            while spamnumber < int(question):
                    await ctx.send('**LURKING!?** ' + MyID);
                    await asyncio.sleep(1)
                    spamnumber += 1
                    print ({spamnumber})


    @commands.command()
    @commands.check(IDCheck)
    async def SpamSimon(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + SimonID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck)
    async def SpamPete(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + PeteID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    @commands.check(IDCheck)
    async def SpamNiall(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + NiallID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    @commands.check(IDCheck)
    async def SpamAaron(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + AaronID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    @commands.check(IDCheck)
    async def SpamConnor(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + ConnorID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck)
    async def SpamJay(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + JayID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck)
    async def SpamBaldwin(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + BaldwinID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck)
    async def SpamVoss(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + VossID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


def setup(client):
    client.add_cog(Spammers(client))
