# All of the imports, the main libraries the Bot functions with.
# You will need to install the libraries in the terminal with `pip install <library name>` before running the bot.
# The library list you need to install is in the `libraries.txt` file.

import discord
from discord.ext import commands
from discord import app_commands, utils
import huggingface_hub
import aiohttp
import asyncio
import json
import datetime
from datetime import timedelta, timezone, date, time
import os
from dotenv import load_dotenv


# All of the environment variables(information that is hidden from others) are loaded from `.env` file. 
# If you want this bot to run and work. You need to create a `.env` file and add the variables shown in the `varaibles.txt` file.

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD_ID = os.getenv('GUILD_ID') # -> The ID of your discord server. You need to have Developer Mode enabled in discord to get this ID.
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API') # -> The API key for Hugging Face. You can get this by creating an account on Hugging Face and generating an API key in your settings.


#The bot's settings.

intents = discord.Intents.all() # -> The intents of the bot. The intents are basically the permissions that the bot has. I made it `all` so that the bot can do everything, but you can change it to only the intents you need for your bot to work.
BOT_PREFIX = "!" # -> The prefix of the Prefix Commands. You can change this to whatever you want. I recommmend using `!` because it is the most commonly used prfix.
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents) # -> Used to create events and commands for the bot.
bot.remove_command('help') # -> This is used to remove the default help command, so that I can create our own custom help command.


# The `on_ready` event, it is used to make you know whenever the bot is online!

@bot.event
async def on_ready():
    print(f"{bot.user} has successfully connected to Discord's API! It is now online. The bot is developed by: `justpixel.code`.")
    channel = bot.get_channel("CHANNEL_ID") # Replace the "CHANNEL_ID" with the ID of the channel you want the bot to send the Online message in.
    embed = discord.Embed(
        title=f"{bot.user} is Online!",
        description=f"The bot is online now!\nIt's username is: `{bot.user.name}`",
        color=discord.Color.green()
    )
    embed.set_footer(text="The bot was developed by: justpixel.code.")

    await channel.send("The bot is online!", embed=embed)


# This is the `on_message` event, it used to respond to messages people send!

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content in ["Hello", "Hi", "Hey", "hello", "hi", "hey"]: # -> You can add more words to this list. Just make sure to keep the same format( "", )
        await message.channel.send(f"Hello {message.author.mention}! How are you doing today?")

    await bot.process_commands(message) # -> This is used to make sure that the bot can still process commands even with the `on_message` event.


# These are ALL of the commands for the bot. I made sure to section every one!

# ---Ping Command---
@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f"Pong! 🏓\nThe bot's ping is {latency:.2f}ms")


# ---Help Command---
@bot.command(aliases=["h", "helpme"])
async def help(ctx, *, reason=None):
    if reason is None:
        reason = "No reason provided"

    embed = discord.Embed(
        title="Help System",
        description=f"The user: {ctx.author.mention} needs help.\nHis reason is: `{reason}`\nConnected to a voice channel: `{ctx.author.voice.channel if ctx.author.voice else 'No'}`",
        color = discord.Color.blue()
    )
    embed.set_footer(text="The bot was developed by: justpixel.code.")
    support = "Insert Id" # -> Replace "Insert Id" with the ID of your support team role.
    await ctx.send(f"<@&{support}>", embed=embed)

# ---Kick Command---
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = "No reason provided"

    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked from the server! Reason: `{reason}`", delete_after=5)
        embed = discord.Embed(
            title="User Kicked",
            description=f"{member.mention} was kicked from the server.\nReason: `{reason}`",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Kicked by: {ctx.author}\nThe bot was developed by: justpixel.code.")
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick this user.", delete_after=5)
    except Exception as e:
        await ctx.send(f"An error occurred while trying to kick the user: {str(e)}", delete_after=5)

# ---Ban Command---
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        reason = "No reason provided"

    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned from the server! Reason: `{reason}`", delete_after=5)
        embed = discord.Embed(
            title="User Banned",
            description=f"{member.mention} was banned from the server.\nReason: `{reason}`",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text=f"Banned by: {ctx.author}\nThe bot was developed by: justpixel.code.")
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban this user.", delete_after=5)
    except Exception as e:
        await ctx.send(f"An error occurred while trying to ban the user: {str(e)}", delete_after=5)


# Finally, this is the function that runs the bot.

bot.run(TOKEN)
