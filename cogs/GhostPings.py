import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

class GhostPings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('GhostPing file Loaded')

    @commands.command()
    async def GhostTest(self, ctx, *, question):
        await ctx.send('**LURKING!?** ' + MyID, delete_after=2);
        await ctx.message.delete()

def setup(client):
    client.add_cog(GhostPings(client))
