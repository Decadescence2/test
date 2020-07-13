import discord
import time
import os
import random
import asyncio

from discord.ext import commands
from discord.utils import get

MyID2 = '<@339508544409829376>'
VossID2 = '<@215985007326527488>'
BaldwinID2 = '<@248950488731484161>'
JayID2 = '<@380887572970340362>'
ConnorID2  = '<@151063490168094721>'
AaronID2 = '<@176810214257852416>'
NiallID2 = '<@246568122457391105>'
PeteID2 = '<@400336685084311552>'
SimonID2 = '<@374657763269410836>'

class MegaSpam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('MegaSpam file Loaded')
    def IDCheck2(ctx):
        return ctx.message.author.id == 339508544409829376

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Response Recieved in {round(self.client.latency *1000)}ms')

def setup(client):
    client.add_cog(MegaSpam(client))
