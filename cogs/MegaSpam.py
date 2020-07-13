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

    @commands.command()
    @commands.check(IDCheck2)
    async def MSConnor(self, ctx):
        spamnumber = 0
        while spamnumber < 20:
            channel = self.client.get_channel(380834959495266304)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(431598672912973836)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(479427858670944276)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(522964547846537226)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(645743473303224351)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(339489387278499841)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(381554304034537472)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(467858221265059860)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(675496261511544848)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(432675920713613313)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(643165392352575498)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(534178060757368842)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(502164029796646914)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(502166581124792330)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(509531143587102720)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(591300587711234175)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(339490396071657472)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(638061970389729311)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(588771820979748874)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(436615704310186006)
            await channel.send(ConnorID2)
            channel = self.client.get_channel(476067400500903957)
            await channel.send(ConnorID2)
            await asyncio.sleep(1)
            spamnumber += 1
            print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck2)
    async def MSVoss(self, ctx):
        spamnumber = 0
        while spamnumber < 20:
            channel = self.client.get_channel(380834959495266304)
            await channel.send(VossID2)
            channel = self.client.get_channel(431598672912973836)
            await channel.send(VossID2)
            channel = self.client.get_channel(479427858670944276)
            await channel.send(VossID2)
            channel = self.client.get_channel(522964547846537226)
            await channel.send(VossID2)
            channel = self.client.get_channel(645743473303224351)
            await channel.send(VossID2)
            channel = self.client.get_channel(339489387278499841)
            await channel.send(VossID2)
            channel = self.client.get_channel(381554304034537472)
            await channel.send(VossID2)
            channel = self.client.get_channel(467858221265059860)
            await channel.send(VossID2)
            channel = self.client.get_channel(675496261511544848)
            await channel.send(VossID2)
            channel = self.client.get_channel(432675920713613313)
            await channel.send(VossID2)
            channel = self.client.get_channel(643165392352575498)
            await channel.send(VossID2)
            channel = self.client.get_channel(534178060757368842)
            await channel.send(VossID2)
            channel = self.client.get_channel(502164029796646914)
            await channel.send(VossID2)
            channel = self.client.get_channel(502166581124792330)
            await channel.send(VossID2)
            channel = self.client.get_channel(509531143587102720)
            await channel.send(VossID2)
            channel = self.client.get_channel(591300587711234175)
            await channel.send(VossID2)
            channel = self.client.get_channel(339490396071657472)
            await channel.send(VossID2)
            channel = self.client.get_channel(638061970389729311)
            await channel.send(VossID2)
            channel = self.client.get_channel(588771820979748874)
            await channel.send(VossID2)
            channel = self.client.get_channel(436615704310186006)
            await channel.send(VossID2)
            channel = self.client.get_channel(476067400500903957)
            await channel.send(VossID2)
            await asyncio.sleep(1)
            spamnumber += 1
            print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck2)
    async def MSJay(self, ctx):
        spamnumber = 0
        while spamnumber < 20:
            channel = self.client.get_channel(380834959495266304)
            await channel.send(JayID2)
            channel = self.client.get_channel(431598672912973836)
            await channel.send(JayID2)
            channel = self.client.get_channel(479427858670944276)
            await channel.send(JayID2)
            channel = self.client.get_channel(522964547846537226)
            await channel.send(JayID2)
            channel = self.client.get_channel(645743473303224351)
            await channel.send(JayID2)
            channel = self.client.get_channel(339489387278499841)
            await channel.send(JayID2)
            channel = self.client.get_channel(381554304034537472)
            await channel.send(JayID2)
            channel = self.client.get_channel(467858221265059860)
            await channel.send(JayID2)
            channel = self.client.get_channel(675496261511544848)
            await channel.send(JayID2)
            channel = self.client.get_channel(432675920713613313)
            await channel.send(JayID2)
            channel = self.client.get_channel(643165392352575498)
            await channel.send(JayID2)
            channel = self.client.get_channel(534178060757368842)
            await channel.send(JayID2)
            channel = self.client.get_channel(502164029796646914)
            await channel.send(JayID2)
            channel = self.client.get_channel(502166581124792330)
            await channel.send(JayID2)
            channel = self.client.get_channel(509531143587102720)
            await channel.send(JayID2)
            channel = self.client.get_channel(591300587711234175)
            await channel.send(JayID2)
            channel = self.client.get_channel(339490396071657472)
            await channel.send(JayID2)
            channel = self.client.get_channel(638061970389729311)
            await channel.send(JayID2)
            channel = self.client.get_channel(588771820979748874)
            await channel.send(JayID2)
            channel = self.client.get_channel(436615704310186006)
            await channel.send(JayID2)
            channel = self.client.get_channel(476067400500903957)
            await channel.send(JayID2)
            await asyncio.sleep(1)
            spamnumber += 1
            print ({spamnumber})

    @commands.command()
    @commands.check(IDCheck2)
    async def MSBaldwin(self, ctx):
        spamnumber = 0
        while spamnumber < 20:
            channel = self.client.get_channel(380834959495266304)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(431598672912973836)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(479427858670944276)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(522964547846537226)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(645743473303224351)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(339489387278499841)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(381554304034537472)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(467858221265059860)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(675496261511544848)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(432675920713613313)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(643165392352575498)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(534178060757368842)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(502164029796646914)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(502166581124792330)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(509531143587102720)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(591300587711234175)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(339490396071657472)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(638061970389729311)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(588771820979748874)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(436615704310186006)
            await channel.send(BaldwinID2)
            channel = self.client.get_channel(476067400500903957)
            await channel.send(BaldwinID2)
            await asyncio.sleep(1)
            spamnumber += 1
            print ({spamnumber})


def setup(client):
    client.add_cog(MegaSpam(client))
