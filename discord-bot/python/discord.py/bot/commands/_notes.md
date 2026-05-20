> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

commands
- an async function that runs when a user invoke it
- a command function must be asynchronous, and also includes the `@commands` decorator from `discord.ext.commands`
- when a user invokes a command, the invocation message is passed into the function as a `Context` object
- a Context object contains information of the message and the user that invoked the command, such as `guild`, `channel`, and `author`
- you can also use `@bot.commands` instead of `@commands.commands` if you're inside the main file where you instantiated the Bot object

alias
- an alias is an alternative name for a command
- for example, if the bot's prefix is `=`, and you have a command called `hello` with an alias `hi`, then invoking `=hi` would be the same as invoking `=hello`
- a command can have more than one aliases
- to set an alias for a command, use the `aliases` parameter inside the `@commands()` decorator