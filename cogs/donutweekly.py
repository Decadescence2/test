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




def setup(client):
    client.add_cog(donutweekly(client))
