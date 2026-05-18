> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_
_(note that the value of the variable in the .env file is gibberish.)_

---

`.gitignore`
- a file that contains a list of file names that you want git to "ignore" when staging and committing files in the working directory
- it is useful when you have important files which contain sensitive personal data, like API keys and tokens for example.
- you don't have to write a `.gitignore` file yourself. Just use whatever `.gitignore` templates related to your project
- when creating a repository in GitHub, there is a dropdown to choose the programming language for your `.gitignore` template
- you can also visit the [repository github/gitignore](https://github.com/github/gitignore), which, as you can see, is owned by GitHub itself

`.env`
- a plain text file used to store important credentials like passwords and API keys and tokens
- the way it works is that instead of hard-coding credentials in your source code, you store the variables inside the `.env` file
- in the source code, you get the variable by loading the `.env` file and use functions, like Python's `os.getenv("API_KEY")` function
- that way, when you push your local commits to a remote, other developers will only see the name of that variable, not the value
- this makes your source code cleaner and your credentials much safer