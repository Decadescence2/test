import discord
import asyncio
import os
from itertools import cycle
from discord.ext import commands

MyID3 = '<@339508544409829376>'
VossID3 = '<@215985007326527488>'
BaldwinID3 = '<@248950488731484161>'
JayID3 = '<@380887572970340362>'
ConnorID3  = '<@151063490168094721>'
AaronID3 = '<@176810214257852416>'
NiallID3 = '<@246568122457391105>'
PeteID3 = '<@400336685084311552>'
SimonID3 = '<@374657763269410836>'

class GhostPings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('GhostPing file Loaded')

    @commands.command()
    async def GhostTest(self, ctx):
        await ctx.send(MyID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostVoss(self, ctx):
        await ctx.send(VossID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostJay(self, ctx):
        await ctx.send(JayID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostConnor(self, ctx):
        await ctx.send(ConnorID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostAaron(self, ctx):
        await ctx.send(AaronID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostNiall(self, ctx):
        await ctx.send(NiallID3, delete_after=2);
        await ctx.message.delete()

    @commands.command()
    async def GhostPete(self, ctx):
        await ctx.send(PeteID3, delete_after=2);
        await ctx.message.delete()

    async def GhostSimon(self, ctx):
        await ctx.send(SimonID3, delete_after=2);
        await ctx.message.delete()

def setup(client):
    client.add_cog(GhostPings(client))
