> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_\
_(example of a main bot file can be found in the `bot` folder in the parent directory `/bot/` above `/Cogs/`.)_

---

Cogs
- a modular class that lets you organize your bot's commands, event listeners, and state into separate, reusable components
- your bot's commands become the methods of the Cog class
- to make a Cog class, make a class with inheritance from `commands.Cog`
- then, just insert your commands into the class
- at the end of the Cog file, declare an async function named `setup()` and add `await bot.add_cog({class_name}(bot))`
- at your main python file _(your startup file that activates the bot)_, do this:
```py
@bot.event #a decorator that does something when an event happens
async def on_ready(): #does something when the bot is online
    print(f"{bot.user} has logged in!")

    for ext in ["relpath_to_cogfile"]:
        await bot.load_extension(ext)
```
- the `load_extension()` method of your `Bot` object will search for a global function named `setup()` in your Cog files
- then, the commands inside the Cog files will be registered to your bot's commands list