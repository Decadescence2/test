import discord
import asyncio
import os
import random
from itertools import cycle
from discord.ext import commands

class SiegeCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Siege File Loaded')

    @commands.command()
    async def RandomMap(self, ctx):
        maps = ['**Bank**','**Bartlett University**','**Chalet**','**Clubhouse**','**Consulate**','**Hereford Base**',
        '**House**','**Kafe Dostoyevsky**','**Kanal**','**Oregon**','**Outback**','**Presidential Plane**',
        '**Yacht**','**Border**','**Favela**','**Fortress**','**Skyscraper**','**Coastline**','**Villa**','**Theme Park**']
        await ctx.send(f'You are playing: {random.choice(maps)}')


def setup(client):
    client.add_cog(SiegeCommands(client))
