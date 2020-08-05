import discord
import time
import os
import asyncio
import random

from discord.ext import commands, tasks
from itertools import cycle


Baldwin = int(0)
Ash = int(0)
Voss = 0
Jay = int(0)
Connor = int(0)
Aaron = int(0)
Pete = int(0)
Niall = int(0)
AshWeek = int(0)
VossWeek = int(0)
JayWeek = int(0)
BaldwinWeek = int(0)
ConnorWeek = int(0)
PeteWeek = int(0)
AaronWeek = int(0)
NiallWeek = int(0)

# target_channel_id = 523703758564360197

client = commands.Bot(command_prefix = '~', case_insensitive=True)
client.remove_command('help')

Messages = ['With My 2 Balls', 'With Baldwins Sister', '7 Days Until This Game Dies',
            'With My Amazing Headset', 'UNO.', 'With My Fallout Strap On Mod', 'Speaking Over Niall'
            , 'Dont Starve IRL', '~']


@client.command()
async def Load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def Unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def Reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

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

@client.command(pass_context = True)
async def Resetdonuts(ctx):
    global Niall
    global Voss
    global Connor
    global Baldwin
    global Ash
    global Pete
    global Jay
    global Aaron
    Niall = 0
    Voss = 0
    Connor = 0
    Baldwin = 0
    Jay = 0
    Ash = 0
    Pete = 0
    Aaron = 0

@client.event
async def on_message(message):
    await client.process_commands(message)
    member = message.author.id
    if message.author.id == 151063490168094721:
        if "gif" in message.content:
            responses = ['https://imgur.com/SnGm07p', 'https://imgur.com/xUcha8d''https://imgur.com/SFY00cc','https://imgur.com/l1isdSZ','https://imgur.com/XiST5sG','https://imgur.com/Q0c3E8c','https://imgur.com/YFwZgbl','https://imgur.com/vlkOGaf','https://imgur.com/aWyR7iX', 'https://imgur.com/8DjzVc5', 'https://imgur.com/ovOGXf8','https://imgur.com/8HMehnO','https://imgur.com/jvlfhzn','https://imgur.com/8KMJ6sr']
            await message.channel.send(random.choice(responses))


@client.command()
async def Test(ctx):
    await ctx.send('working')

# called_once_a_week.start()
client.loop.create_task(change_status())
client.run(os.environ['token'])
