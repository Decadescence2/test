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

    def ListCheck():
        async def IsInList(ctx):
            member = message.author.id
            return ctx.message.author.id in modlist
        return commands.check(IsInList)



    @commands.command()
    async def addperm(self, ctx, *, question):
        modlist.append(question)
        await ctx.send('User ids that have free reign:')
        for i in range(0, len(modlist)):
            await ctx.send(modlist[i])

    @commands.command()
    async def ViewModlist(self, ctx):
        await ctx.send('User ids that have free reign:')
        for i in range(0, len(modlist)):
            await ctx.send(modlist[i])

    @commands.command()
    async def clearModlist(self, ctx):
        modlist.clear()
        modlist.append(339508544409829376)
        # for i in range(0, len(modlist)):
        #     print(modlist[i])
        await ctx.send('Modlist cleared, Fuck you all')

    @commands.command()
    @ListCheck()
    async def permtest(self, ctx):
        print ('success')



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
