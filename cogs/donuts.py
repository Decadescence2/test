import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

#donuts
Baldwin = int(0)
Ash = int(0)
Voss = int(0)
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
        Voss + 1
        await ctx.send('https://imgur.com/Z7T1Gh5')

    @commands.command(pass_context = True)
    async def Leaderboard(self, ctx):
        await ctx.send('Baldwin: ')
        await ctx.send(f'Baldwin: ' + (Voss))
        # await ctx.send('Voss: ' + Voss);
        # await ctx.send('Ash: ' + Ash);
        # await ctx.send('Jay: ' + Jay);
        # await ctx.send('Aaron: ' + Aaron);
        # await ctx.send('Connor: ' + Connor);
        # await ctx.send('Pete: ' + Pete);
        # await ctx.send('Niall: ' + Niall);





def setup(client):
    client.add_cog(donuts(client))
