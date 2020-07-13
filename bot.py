import discord
import random
import time
import os
import asyncio

from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '=')

Messages = ['1', '2', '3']


# #Events
# @client.event
# async def on_ready():
#     print('Bot is Online, Loading Files...')

async def change_status():
    await client.wait_until_ready()
    status = cycle(Messages)

    while not client.is_closed():
        current_status = next(status)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(60)
        print ('Status Changed')
           
@client.command()
# @commands.check(IDCheck)
async def Test(ctx):
    await ctx.send('working')

client.loop.create_task(change_status())
client.run(os.environ['token'])
