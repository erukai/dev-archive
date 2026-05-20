#committed: 27/11/2025
#---

#import the `commands` package from the `ext` subpackage of the `discord` library 
from discord.ext import commands

@commands.command(aliases=["hi"])
async def hello(ctx):
    await ctx.send("hello!")

@commands.command()
async def bye(ctx):
    await ctx.send("bye!")