#committed: 27/11/2025
#---

from discord.ext import commands #imports the module `commands` which is from the subpackage `ext` of the package/library `discord`

#this class inherits from the parent class `Cog` from the `commands` module
class Greet(commands.Cog):

    #initializes an object. `self` is a reference to the instance (object) of a class,
    #meaning when an object is created, all variables declared inside __init__ are automatically given to the object
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hi"])
    async def hello(ctx):
        await ctx.send("hello!")

    @commands.command()
    async def bye(ctx):
        await ctx.send("bye!")


#Use this to connect the Discord bot to the commands inside the classes in this file
async def setup(bot):
    await bot.add_cog(Greet(bot)) #the `add_cog` method binds the Cog class to the bot