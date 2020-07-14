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

    @client.command(pass_context = True)
    async def Help(self, ctx):
        author = ctx.message.author

        embed = discord.embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Commands')
        embed.add_field(name='SpamCommands', value='SpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)')
        
        await author.send(embed=embed)

def setup(client):
    client.add_cog(Test_Commands(client))
