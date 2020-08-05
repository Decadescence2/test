import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands, tasks

from bot import AshWeek, VossWeek, BaldwinWeek, JayWeek, AaronWeek, PeteWeek, ConnorWeek, NiallWeek

class donutweekly(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Donut Weekly leaderboard Loaded')

    @tasks.loop(seconds=30)
    async def WeeklyReset(self):
        global NiallWeek
        global VossWeek
        global ConnorWeek
        global BaldwinWeek
        global AshWeek
        global PeteWeek
        global JayWeek
        global AaronWeek
        NiallWeek = 0
        VossWeek = 0
        ConnorWeek = 0
        BaldwinWeek = 0
        JayWeek = 0
        AshWeek = 0
        PeteWeek = 0
        AaronWeek = 0
        channel = self.client.get_channel(523703758564360197)
        await channel.send('test')



def setup(client):
    client.add_cog(donutweekly(client))
