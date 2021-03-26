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

    def GetMessage(self):
        async def (getmsgContent):
            await client.send_message(message.channel, message.content)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == '⭐':
            GetMessage()








def setup(client):
    client.add_cog(Starboard(client))
