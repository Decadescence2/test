import discord
import random
import time
import os
import asyncio
# import aiohttp

from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '=')

##################################################################

Messages = ['With My 2 Balls', 'With Baldwins Sister', '7 Days Until This Game Dies',
            'With My Amazing Headset', 'UNO.', 'With My Fallout Strap On Mod', 'Speaking Over Niall'
            , 'Dont Starve IRL', '~']

##################################################################



#Events
@client.event
async def on_ready():
    print('Bot is Online, Loading Files...')


@client.event
async def on_message(message):
    member = message.author.id

    if message.author.id == 151063490168094721:
        if "gif" in message.content:
            responses = ['https://imgur.com/SFY00cc','https://imgur.com/l1isdSZ','https://imgur.com/XiST5sG','https://imgur.com/Q0c3E8c','https://imgur.com/YFwZgbl','https://imgur.com/vlkOGaf','https://imgur.com/aWyR7iX', 'https://imgur.com/8DjzVc5', 'https://imgur.com/ovOGXf8','https://imgur.com/8HMehnO','https://imgur.com/jvlfhzn','https://imgur.com/8KMJ6sr']
            await message.channel.send(random.choice(responses))

@client.command()
async def Commands(ctx):
    await ctx.send('__**Commands: **__ ' + '```(x = Amount Of Pings)\nSpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)```')

@client.command()
# @commands.check(IDCheck)
async def Test(ctx):
    await ctx.send('working')


client.run(os.environ['token'])
