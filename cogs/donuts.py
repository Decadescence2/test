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
    async def Leaderboard(self, ctx):
        await ctx.send('Voss: {}\nAsh: {}\nJay: {}\nAaron: {}\nConnor: {}\nPete: {}\nNiall: {}\nBaldwin: {}'.format(Voss, Ash, Jay, Aaron, Connor, Pete, Niall, Baldwin))

    @commands.command(pass_context = True)
    async def embedtest(self, ctx):

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Donut Leaderboard')
        embed.add_field(name='Voss: ', value=('{}'.format(Voss)),inline=True)
        embed.add_field(name='Ash: ', value=('{}'.format(Ash)),inline=True)
        embed.add_field(name='Jay: ', value=('{}'.format(Jay)),inline=True)
        embed.add_field(name='Baldwin: ', value=('{}'.format(Baldwin)),inline=True)
        embed.add_field(name='Pete: ', value=('{}'.format(Aaron)),inline=True)
        embed.add_field(name='Niall: ', value=('{}'.format(Niall)),inline=True)
        embed.add_field(name='Aaron: ', value=('{}'.format(Aaron)),inline=True)
        embed.set_footer(*, text=Embed.empty, icon_url=Embed.https://www.theflavorbender.com/wp-content/uploads/2014/09/Simpsons-Doughnuts-4238-Copy-1.jpg)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(donuts(client))
