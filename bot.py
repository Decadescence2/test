import discord
import random
import time
import os
import asyncio
# import aiohttp

from discord.ext import commands, tasks
from itertools import cycle


TOKEN = 'NzMyMDIwMzMxMzE2NzcyOTk2.XwuhGQ.4xRE95CJXLcVwd4dQvnyAgHZg_I'

client = commands.Bot(command_prefix = '=')

@client.command()
# @commands.check(IDCheck)
async def Test(ctx):
    await ctx.send('working')


client.run(TOKEN)
