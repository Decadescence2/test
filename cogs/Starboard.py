import discord
import time
import os
import random
import embedify
import database as dbman
from itertools import cycle
from discord.ext import commands
from random import randrange


class Starboard(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print ('Starboard File Loaded')
    #
    # def GetMessage(self):
    #     async def (getmsgContent):
    #         await client.send_message(message.channel, message.content)
    #
    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self, payload):
    #     if payload.emoji.name == '⭐':
    #         GetMessage()


    emojis = ["⭐"]

    channel_id = 824828633356435497


    # Only used when the reaction emoji is completely missing
    class FalseReaction:
        def __init__(self, emoji, message):
            self.count = 0
            self.me = False
            self.emoji = emoji
            self.custom_emoji = emoji.is_custom_emoji()
            self.message = message

    # Get the reaction and the user from the payload
    async def from_rct_payload(payload):
        chn = await bot.fetch_channel(payload.channel_id)
        msg = await chn.fetch_message(payload.message_id)
        for reaction in msg.reactions:
            if str(reaction.emoji) == str(payload.emoji):
                return reaction, chn.guild.get_member(payload.user_id)
        reaction = FalseReaction(payload.emoji, msg)
        return reaction, chn.guild.get_member(payload.user_id)

    # Updates the starboard
    async def plug_starboard(msg, emojis):
        global channel_id
        stars = msg.guild.get_channel(channel_id)
        starred = []

        # Count emojis
        for reaction in msg.reactions:
            if str(reaction.emoji) in emojis:
                starred.append(str(reaction.count) + "x" + str(reaction.emoji))

        embed = embedify.embedify(
            title = 'STARBOARD ;]',
            desc = msg.content,
            fields = [
                ['AUTHOR', f'<@{msg.author.id}> `{str(msg.author)}`', True],
                ['CHANNEL', f'<#{msg.channel.id}>', True],
                [
                    'LINK',
                    f'[JUMP](https://discord.com/channels/{msg.guild.id}/{msg.channel.id}/{msg.id})',
                    True
                ],
                ['STARS', '\n'.join(starred), True]
            ],
            thumb = str(msg.author.avatar_url)
        )

        # Get the attachments
        attachments = [att.url for att in msg.attachments]
        if len(attachments):
            embed.add_field(
                name = 'ATTACHMENTS',
                value = '\n'.join(attachments),
                inline = False
            )
            try:
                msg.attachments[0].height
                embed.set_image(url = attachments[0])
            except:
                pass

        # Either post a new star or update the existing one
        stars_id = dbman.get('starboard', 'starboard_id', message_id = msg.id)
        try:
            if not stars_id:
                raise TypeError("stars_id isn't available yet")
            stars_msg = await stars.fetch_message(stars_id)
            await stars_msg.edit(embed = embed)
        except:
            stars_msg = await stars.send(embed = embed)
            dbman.insert('starboard', starboard_id = stars_msg.id, message_id = msg.id)


    # Reaction remove only...
    async def handle_reaction_remove(reaction, user):
        global emojis, count
        chn = reaction.message.channel
        try:
            if user.id == bot.user.id:
                return
            msg = reaction.message
            if str(reaction.emoji) in emojis:
                # Count all stars
                cc = 0
                for r in msg.reactions:
                    cc += r.count if str(r.emoji) in emojis else 0
                # Check if above threshold
                if count <= cc and count > 0:
                    await plug_starboard(msg, emojis)
                # Check if below threshold
                elif count > 0 and count > cc:
                    stars = msg.guild.get_channel(channel_id)
                    stars_id = dbman.get('starboard', 'starboard_id', message_id = msg.id)
                    if stars_id:
                        stars_msg = await stars.fetch_message(stars_id)
                        await stars_msg.delete()
                        dbman.remove('starboard', starboard_id = stars_id, message_id = msg.id)
        except IndexError:
            pass
        except Exception as ex:
            await chn.send(f"`{ex}` line {ex.__traceback__.tb_lineno}")


    # Reaction add only...
    async def handle_reaction_add(reaction, user):
        global emojis, count
        chn = reaction.message.channel
        try:
            if user.id == bot.user.id:
                return
            msg = reaction.message
            mng = False
            try:
                # Check if it's a starboard message
                if msg.embeds[0].title == "STARBOARD ;]":
                    await chn.send(
                        f"<@{user.id}>```diff\n-] YOU CAN'T STAR THE STARBOARD```",
                        delete_after = 10.0
                    )
                    await reaction.remove(user)
                    mng = True
            except IndexError:
                mng = False
            if str(reaction.emoji) in emojis and not mng:
                # Check if the user is starring their own message
                if user.id == msg.author.id:
                    await chn.send(
                        f"<@{user.id}>```diff\n-] YOU CAN'T STAR YOUR OWN MESSAGES```",
                        delete_after = 10.0
                    )
                    await reaction.remove(user)
                else:
                    # Count all stars
                    cc = 0
                    for r in msg.reactions:
                        cc += r.count if str(r.emoji) in emojis else 0
                    if count <= cc and count > 0:
                        await plug_starboard(msg, emojis)
        except IndexError:
            pass
        except Exception as ex:
            await chn.send(f"`{ex}` line {ex.__traceback__.tb_lineno}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(payload):
        reaction, user = await from_rct_payload(payload)
        return await handle_reaction_add(reaction, user)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(payload):
        reaction, user = await from_rct_payload(payload)
        return await handle_reaction_remove(reaction, user)

    @commands.Cog.listener()
    async def on_raw_message_delete(payload):
        # Clean out the starboard database in case it gets unstarred
        stars_id = dbman.get('starboard', 'starboard_id', message_id = payload.message_id)
        if stars_id:
            dbman.remove('starboard', starboard_id = stars_id, message_id = payload.message_id)
            return
        msg_id = dbman.get('starboard', 'message_id', starboard_id = payload.message_id)
        if msg_id:
            dbman.remove('starboard', starboard_id = payload.message_id, message_id = msg_id)
            return








def setup(client):
    client.add_cog(Starboard(client))
