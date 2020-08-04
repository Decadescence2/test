import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

#donuts
Baldwin = 0
Ash = 0
Voss = 0
Jay = 0
Connor = 0
Aaron = 0
Pete = 0
Niall = 0


class donuts(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('donut leaderboard Loaded')

    @commands.command(pass_context = True)
    async def AddDonutVoss(self, ctx):
        Voss += 1
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def DonutLeaderboard(self, ctx):
        await ctx.send('Baldwin: ' + Baldwin)
        await ctx.send('Voss: ' + Voss)
        await ctx.send('Ash: ' + Ash)
        await ctx.send('Jay: ' + Jay)
        await ctx.send('Aaron: ' + Aaron)
        await ctx.send('Connor: ' + Connor)
        await ctx.send('Pete: ' + Pete)
        await ctx.send('Niall: ' + Niall)





def setup(client):
    client.add_cog(donuts(client))
