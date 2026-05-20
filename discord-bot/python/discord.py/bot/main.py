#committed: 27/11/2025

'''
A snapshot of `main.py` from another project
'''

#---

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file into environment
TOKEN = os.getenv("BOT_TOKEN") #get the bot token in the .env file

#-----------------------------------------------------------

#create an Intents object that holds the data of enabled intents for your bot
#Intents are like permissions for how much your bot can do
intents = discord.Intents.default() #allows all basic intents

#special, "privileged" gateway intents
#will work if bot is in less than 100 servers, otherwise require Discord's verification
intents.message_content = True #allows your bot to retrieve a user's message like text, attachments, embeds, and components
intents.members = True #allows your bot to retrieve member-related events, like when they leave or join the server
intents.presences = True #allows your bot to retrieve users' presence data, such as their presences, activities, and custom statuses

#create a Bot object using the `Bot` class from the `commands` package
#use the `command_prefix` parameter to set the prefix of your bot
#set the `intents` object (the one we set above) as the value of the `intents` parameter
bot = commands.Bot(command_prefix="=", intents=intents)

#-----------------------------------------------------------

#a discord bot has a `help` command by default
#but the default `help` command is ugly
#so if you want to add your own `help` command, you must remove the default command first before adding yours to prevent conflict
bot.remove_command("help")

#Import commands from your command files
from .commands import hello, bye
for cmd in [hello, bye]:
    bot.add_command(cmd)

#↑ the example above (`for cmd in [...]`) is an alternative way to write:
'''
bot.add_command(hello)
bot.add_command(bye)
'''
#which is useful if the file has a lot of commands

#-----------------------------------------------------------

@bot.event #a decorator that does something when an event happens
async def on_ready(): #does something when the bot is online
    print(f"{bot.user} has logged in!")

    #Import commands from commands.Cog files
    for ext in ["games.roulette", "src.info", "src.help"]:
        await bot.load_extension(ext)

    #↑ Cogs are a bit different than a regular command file.
    #commands in a Cog file are wrapped in a class that inherits elements from the Cog class.
    #so instead of importing the individual commands and use `add_command()` to add the command to the commands list,
    #they use `load_extension()` on the file path instead.

@bot.event
async def on_disconnect(): #does something when the bot is offline
    print(f'{bot.user} has logged out.')

#catch missing roles / permissions errors
@bot.event
async def on_command_error(ctx, error): #does something when an error occurs when a user sends a command
    if isinstance(error, commands.MissingRole) and error.missing_role == "Level 100":
        await ctx.send("Your level is below 100. You cannot use this command.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("I'm sorry, but you lack moderation permissions.")


#__name__ is a special Python variable where its value becomes "__main__" if the script is being run directly from terminal
#the condition below ensures that the script is being run directly (e.g. `python main.py`), instead of from another script
if __name__ == "__main__":
    bot.run(TOKEN)
