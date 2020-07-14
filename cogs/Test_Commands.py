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

    @commands.command(pass_context = True)
    async def Help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='Commands')
        embed.add_field(name='SpamCommands', value='SpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)',inline=False)

        await author.send(embed=embed)

def setup(client):
    client.add_cog(Test_Commands(client))
