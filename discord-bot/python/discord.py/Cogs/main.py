#from: commit 01

# A snapshot of `userprofile.py` from another project
# Some lines have been turned into a string due to their reliance on `saveload.py`; a python module that is not in this project
# They are turned into a double-quote string (and marked with `--` at the end of the line) to prevent warnings from VS Code

import discord #imports the library `discord`
from discord.ext import commands #imports the module `commands` which is from the subpackage `ext` of the package/library `discord`

"from .saveload import save_stats, load_stats --"

#this class inherits from the parent class `Cog`
class UserStats(commands.Cog):

    #initializes an object. `self` is a reference to the instance (object) of a class,
    #meaning when an object is created, all variables declared inside __init__ are automatically given to the object
    def __init__(self, bot):
        self.bot = bot
        "self.user_stats = load_stats() --"

    @commands.command(aliases=["reg"])
    async def register(self, ctx):
        user_id = str(ctx.author.id)
        stats = self.user_stats.get(user_id)

        if stats:
            await ctx.send("You have already registered! Use `stats` to check your profile.")
            return

        self.user_stats[user_id] = {
            "name": ctx.author.name,
            "level": 1,
            "coins": 100,
            "HP": 100,
            "ATK": 10,
            "DEF": 10,
            "FAME": 1,
            "SP": 10,
            "MP": 10
        }

        "save_stats(self.user_stats) --"
        await ctx.send(f"✅ Registered {ctx.author.name} with default stats.")

    @commands.command(aliases=["stats"])
    async def statistics(self, ctx):
        user_id = str(ctx.author.id)
        stats = self.user_stats.get(user_id)

        if not stats:
            await ctx.send("❌ No stats found for you. Try registering first using `register`.")
            return

        chardata = {
            "Name": stats["name"],
            "Level": stats["level"],
            "Coins": f'¢{stats["coins"]}',
            "HP": stats["HP"],
            "ATK": stats["ATK"],
            "DEF": stats["DEF"],
            "FAME": stats["FAME"],
            "SP": stats["SP"],
            "MP": stats["MP"]
        }

        embed = discord.Embed(title="📊 Character Profile", color=discord.Colour.orange())
        embed.set_thumbnail(url=ctx.author.avatar.url)

        for label, value in chardata.items():
            embed.add_field(name=label, value=value, inline=True)

        await ctx.send(embed=embed)

#Use this to connect the bot to the commands inside the classes in this file
async def setup(bot):
    await bot.add_cog(UserStats(bot))