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
        await ctx.send('Voss: {}'.format(Voss))
        # await ctx.send('Voss: ' + Voss);
        # await ctx.send('Ash: ' + Ash);
        # await ctx.send('Jay: ' + Jay);
        # await ctx.send('Aaron: ' + Aaron);
        # await ctx.send('Connor: ' + Connor);
        # await ctx.send('Pete: ' + Pete);
        # await ctx.send('Niall: ' + Niall);

        @commands.command(pass_context = True)
        async def Test2(self, ctx):

            embed = discord.Embed(
                colour = discord.Colour.blue()
            )

            embed.set_author(name='Donut Leaderboard')
            embed.add_field(name='Voss:', value=Voss,inline=False)
            embed.add_field(name='MegaSpam Commands', value='MSVoss\nMSBaldwin\nMSJay\nMSConnor\nMS(Message)',inline=False)
            embed.add_field(name='Ghost Ping Commands', value='GhostVoss\nGhostBaldwin\nGhostJay\nGhostConnor\nGhostSimon\nGhostPete\nGhostAaron\nGhostNiall',inline=False)
            embed.add_field(name='Random Commands', value='8Ball\nDonut',inline=False)
            embed.add_field(name='Admin Commands', value='Load (cog_name)\nUnload (cog_name)\nReload (cog_name)\n', inline=False)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(donuts(client))
