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

    @commands.command(aliases = ['8Ball', '8ball'])
    async def _8Ball(self, ctx, *, question):
        responses = ['As I see it, yes',
                     'Ask again later',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    @commands.command(pass_context = True)
    async def Help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name='Commands')
        embed.add_field(name='Spam Commands - Limit is 5 pings', value='SpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)',inline=False)
        embed.add_field(name='MegaSpam Commands', value='MSVoss\nMSBaldwin\nMSJay\nMSConnor',inline=False)
        embed.add_field(name='Ghost Ping Commands', value='GhostVoss\nGhostBaldwin\nGhostJay\nGhostConnor\nGhostSimon\nGhostPete\nGhostAaron\nGhostNiall',inline=False)
        embed.add_field(name='Random Commands', value='8Ball',inline=False)
        embed.add_field(name='Admin Commands', value='Load (cog_name)\nUnload (cog_name)\nReload (cog_name)\n', inline=False)

        await author.send(embed=embed)

def setup(client):
    client.add_cog(Test_Commands(client))
