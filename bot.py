import discord
import random
import time
import os
import asyncio
# import aiohttp

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '=')


client.run(os.environ['token'])
