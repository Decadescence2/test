import discord
import time
import os
import random
from itertools import cycle
from discord.ext import commands
from random import randrange


class Starboard(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Starboard File Loaded')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == '⭐':
            echo = (message.author.name, 'said', message.content)
            print (echo)







def setup(client):
    client.add_cog(Starboard(client))
