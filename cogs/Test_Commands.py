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
        embed.add_field(name='Spam Commands', value='SpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)',inline=False)
        embed.add_field(name='MegaSpam Commands', value='MSVoss\nMSBaldwin\nMSJay\nMSConnor',inline=False)
        embed.add_field(name='Admin Commands', value='Load (cog_name)\nUnload (cog_name)\nReload (cog_name)\n', inline=False)

        await author.send(embed=embed)

def setup(client):
    client.add_cog(Test_Commands(client))
