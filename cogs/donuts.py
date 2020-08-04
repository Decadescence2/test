import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands, tasks

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
        self.called_once_a_week.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Donut leaderboard Loaded')

    @commands.command(pass_context = True)
    async def AddDonutVoss(self, ctx):
        global Voss
        Voss += 1
        await ctx.send('Donut Added')
        return Voss

    @commands.command(pass_context = True)
    async def AddDonutJay(self, ctx):
        global Jay
        Jay += 1
        await ctx.send('Donut Added')
        return Jay

    @commands.command(pass_context = True)
    async def AddDonutBaldwin(self, ctx):
        global Baldwin
        Baldwin += 1
        await ctx.send('Donut Added')
        return Baldwin

    @commands.command(pass_context = True)
    async def AddDonutAsh(self, ctx):
        global Ash
        Ash += 1
        await ctx.send('Donut Added')
        return Ash

    @commands.command(pass_context = True)
    async def AddDonutConnor(self, ctx):
        global Connor
        Connor += 1
        await ctx.send('Donut Added')
        return Connor

    @commands.command(pass_context = True)
    async def AddDonutAaron(self, ctx):
        global Aaron
        Aaron += 1
        await ctx.send('Donut Added')
        return Aaron

    @commands.command(pass_context = True)
    async def AddDonutPete(self, ctx):
        global Pete
        Pete += 1
        await ctx.send('Donut Added')
        return Pete

    @commands.command(pass_context = True)
    async def AddDonutNiall(self, ctx):
        global Niall
        Niall += 1
        await ctx.send('Donut Added')
        return Niall

        target_channel_id = 523703758564360197

    @tasks.loop(seconds=30)
    async def called_once_a_week():
        message_channel = client.get_channel(target_channel_id)
        print(f"Got channel {message_channel}")
        await message_channel.send("reset")
        global Niall
        global Voss
        global Connor
        global Baldwin
        global Ash
        global Pete
        global Jay
        global Aaron
        Niall = 0
        Voss = 0
        Connor = 0
        Baldwin = 0
        Jay = 0
        Ash = 0
        Pete = 0
        Aaron = 0

    @called_once_a_week.before_loop
    async def before():
        await client.wait_until_ready()
        print("Finished waiting")

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
