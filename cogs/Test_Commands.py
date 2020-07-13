import discord
import time
import os
import random
from itertools import cycle
from discord.ext import commands

class Test_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print ('Test Command File Loaded')

    @commands.command()
    async def gilbert(self, ctx):
        gilbertN = 0
        while gilbertN < 3:
            await ctx.send('https://imgur.com/8DjzVc5')
            gilbertN += 1
            print ({gilbertN})

def setup(client):
    client.add_cog(Test_Commands(client))
