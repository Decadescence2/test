import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

#donuts
Baldwin = int(0)
Ash = int(0)
Voss = 0
Jay = int(0)
Connor = int(0)
Aaron = int(0)
Pete = int(0)
Niall = int(0)


class donuts(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Donut leaderboard Loaded')

    @commands.command(pass_context = True)
    async def AddDonutVoss(self, ctx):
        global Voss
        Voss += 1
        return Voss
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutJay(self, ctx):
        global Jay
        Jay += 1
        return Jay
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutBaldwin(self, ctx):
        global Baldwin
        Baldwin += 1
        return Badlwin
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutAsh(self, ctx):
        global Ash
        Ash += 1
        return Ash
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutConnor(self, ctx):
        global Connor
        Connor += 1
        return Connor
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutAaron(self, ctx):
        global Aaron
        Aaron += 1
        return Aaron
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutPete(self, ctx):
        global Pete
        Pete += 1
        return Pete
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def AddDonutNiall(self, ctx):
        global Niall
        Niall += 1
        return Niall
        await ctx.send('https://imgur.com/Z7T1Gh5')





    # @commands.command(pass_context = True)
    # async def Leaderboard(self, ctx):
    #     await ctx.send('Voss: {}\nAsh: {}\nJay: {}\nAaron: {}\nConnor: {}\nPete: {}\nNiall: {}\nBaldwin: {}'.format(Voss, Ash, Jay, Aaron, Connor, Pete, Niall, Baldwin))

    @commands.command(pass_context = True)
    async def Leaderboard(self, ctx):

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Donut Leaderboard', icon_url='https://www.theflavorbender.com/wp-content/uploads/2014/09/Simpsons-Doughnuts-4238-Copy-1.jpg')
        embed.add_field(name='Voss: ', value=('{}'.format(Voss)),inline=False)
        embed.add_field(name='Ash: ', value=('{}'.format(Ash)),inline=False)
        embed.add_field(name='Jay: ', value=('{}'.format(Jay)),inline=False)
        embed.add_field(name='Baldwin: ', value=('{}'.format(Baldwin)),inline=False)
        embed.add_field(name='Pete: ', value=('{}'.format(Aaron)),inline=False)
        embed.add_field(name='Niall: ', value=('{}'.format(Niall)),inline=False)
        embed.add_field(name='Aaron: ', value=('{}'.format(Aaron)),inline=False)
        embed.add_field(name='Connor: ', value=('{}'.format(Connor)),inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(donuts(client))
