import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands, tasks


class donutweekly(commands.Cog):

    def __init__(self, client):
        self.client = client
# #     #     self.WeeklyReset.start()
# #     #
# #     #     AshWeek = int(0)
# #     #     VossWeek = int(0)
# #     #     JayWeek = int(0)
# #     #     BaldwinWeek = int(0)
# #     #     ConnorWeek = int(0)
# #     #     PeteWeek = int(0)
# #     #     AaronWeek = int(0)
# #     #     NiallWeek = int(0)
# #     #
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Donut Weekly leaderboard Loaded')
# #     #
# #     # @tasks.loop(seconds=30)
# #     # async def WeeklyReset(self):
# #     #     print('reset')
# #     #     global NiallWeek
# #     #     global VossWeek
# #     #     global ConnorWeek
# #     #     global BaldwinWeek
# #     #     global AshWeek
# #     #     global PeteWeek
# #     #     global JayWeek
# #     #     global AaronWeek
# #     #     NiallWeek = 0
# #     #     VossWeek = 0
# #     #     ConnorWeek = 0
# #     #     BaldwinWeek = 0
# #     #     JayWeek = 0
# #     #     AshWeek = 0
# #     #     PeteWeek = 0
# #     #     AaronWeek = 0
# #     #
# #     # @commands.command(pass_context = True)
# #     # async def Weekly(self, ctx):
# #     #
# #     #     embed = discord.Embed(
# #     #         colour = discord.Colour.blue()
# #     #     )
# #     #
# #     #     embed.set_author(name='Donut Leaderboard', icon_url='https://www.theflavorbender.com/wp-content/uploads/2014/09/Simpsons-Doughnuts-4238-Copy-1.jpg')
# #     #     embed.add_field(name='Voss: ', value=('{}'.format(VossWeek)),inline=False)
# #     #     embed.add_field(name='Ash: ', value=('{}'.format(AshWeek)),inline=False)
# #     #     embed.add_field(name='Jay: ', value=('{}'.format(JayWeek)),inline=False)
# #     #     embed.add_field(name='Baldwin: ', value=('{}'.format(BaldwinWeek)),inline=False)
# #     #     embed.add_field(name='Pete: ', value=('{}'.format(AaronWeek)),inline=False)
# #     #     embed.add_field(name='Niall: ', value=('{}'.format(NiallWeek)),inline=False)
# #     #     embed.add_field(name='Aaron: ', value=('{}'.format(AaronWeek)),inline=False)
# #     #     embed.add_field(name='Connor: ', value=('{}'.format(ConnorWeek)),inline=False)
# #     #
# #     #     await ctx.send(embed=embed)
# #
# #
def setup(client):
    client.add_cog(donutweekly(client))
