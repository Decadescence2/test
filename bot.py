import discord
import time
import os
import asyncio

from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '=')

Messages = ['1', '2', '3']

@client.event
async def on_ready():
    print('Bot is Online, Loading Files...')

async def change_status():
    await client.wait_until_ready()
    status = cycle(Messages)

    while not client.is_closed():
        current_status = next(status)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(60)
        print ('Status Changed')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('You do not have permission to use this command')        
        
@client.command()
async def Commands(ctx):
    await ctx.send('__**Commands: **__ ' + '```(x = Amount Of Pings)\nSpamVoss(x)\nSpamBaldwin(x)\nSpamJay(x)\nSpamSimon(X)\nSpamConnor(x)\nSpamAaron(x)\nSpamNiall(x)\nSpamPete(x)```')
            
@client.command()
async def Test(ctx):
    await ctx.send('working')

client.loop.create_task(change_status())
client.run(os.environ['token'])
