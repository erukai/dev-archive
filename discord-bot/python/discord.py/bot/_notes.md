> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

**bot**
- a `Bot` object used to represent your Discord bot
- this object is used very often in a Discord project environment, especially for commands and or events
- to instantiate a Bot object, use `discord.ext.commands.Bot`, where `Bot` is the class
- there can only be **ONE** Bot object in the entire working directory
- if more than one Bot object is instantiated, conflict will arise and for each command invocation, the command will run as many times as there are Bot objects in the working directory

**intent**
- intents are permission-based parameters that let developers choose which WebSocket events their bot receives from Discord
- being able to choose intents are useful to filter unnecessary events and increase bot performance by reducing memory usage
- there are regular intents and privileged intents
- the privileged intents are:
    - `message_content`
    - `members`
    - `presences`
- the three privileged intents have been explained in `main.py` in this directory

**token**
- when you create a bot application in (Discord Developer Portal - Applications)[https://discord.com/developers/applications], you are given a token for your discord bot
- the token is required to run your discord bot
- however, it is dangerous to hard-code the token into your bot's source code
- instead, it is better to use a system like `.env` that reads the key-value pairs inside it
- that way, your source code can remain clean from any sensitive personal data

**event**
- an event is something that happens inside discord
- things like user joining a guild, leaving a guild, sending a message, deleting a message, are all events
- you can make an event handler to make your bot do something when a specific event is triggered
- to mark a function as an event handler, use the `@event` decorator
- the `@event` decorator is from `discord.Client`
- but instead of using `@discord.Client.event`, you want to use `@discord.ext.commands.Bot.event`, or simply `@bot.event`
- the reason why it works is because `bot` (or `discord.ext.commands.Bot`) is a **subclass** of `discord.Client`
- so as a subclass of `discord.Client`, the Bot object can also use methods and decorators from its parent class, one of them being `@event`