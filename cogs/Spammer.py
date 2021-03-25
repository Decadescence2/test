import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

# status = 'Global'
# users = []

MyID = '<@339508544409829376>'
VossID = '<@215985007326527488>'
BaldwinID = '<@248950488731484161>'
JayID = '<@380887572970340362>'
ConnorID  = '<@151063490168094721>'
AaronID = '<@176810214257852416>'
NiallID = '<@246568122457391105>'
PeteID = '<@400336685084311552>'
SimonID = '<@374657763269410836>'
modlist = [339508544409829376]

class Spammers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Spammer Code Loaded')

    def IDCheck(ctx):
        return ctx.message.author.id == 339508544409829376

    @commands.command()
    async def addperm(self, ctx, *, question):
        modlist.append(question)
        for i in range(0, len(modlist)):
            await ctx.send('users in the mod list: ' + modlist[i]))

    @commands.command()
    async def modlist(self, ctx):
        for i in range(0, len(modlist)):
            await ctx.send('users in the mod list: ' + (modlist[i]))


    @commands.command()
    async def SpamSimon(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + SimonID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + SimonID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    async def SpamPete(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + PeteID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + PeteID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    async def SpamNiall(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + NiallID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + NiallID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    async def SpamAaron(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + AaronID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + AaronID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


    @commands.command()
    async def SpamConnor(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + ConnorID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + ConnorID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    async def SpamJay(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + JayID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + JayID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    async def SpamBaldwin(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + BaldwinID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + BaldwinID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})

    @commands.command()
    async def SpamVoss(self, ctx, *, question):
        spamnumber = 0
        limit = 5
        if int(question) > 5:
            await ctx.send('**Command has a limit of 5 pings**', delete_after=5)
            while spamnumber < 5:
                await ctx.send('**LURKING!?** ' + VossID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
        else:
            while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + VossID);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})


def setup(client):
    client.add_cog(Spammers(client))
