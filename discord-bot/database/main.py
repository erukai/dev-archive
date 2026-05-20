#committed: 27/11/2025
#---

import json
import os
from pathlib import Path #import the `Path` class from the `pathlib` library

#creating path using [`join()` function of the `path module` from the `os` package] so that it won't break when on other operating systems
path = os.path.join("discord-bot", "database", "password.json")

# Build a path relative to the script (this file) using the Path class
path = Path(__file__).parent / "password.json"

#NOTE: `os.path.join()` is an old method, and nowadays it is better to use `pathlib.Path()` due to its object-oriented approach (it returns a Path object instead of a literal string)

#---

my_dict = {
    "username": "john_doe",
    "password": "abc123"
}

#reading data from a json file
with open(path, "r") as f: # "r" means "read"
    file = json.load(f) #stores the entire data of the json file into a single variable `file` as a dictionary

#navigate the data from the imported file to a specific key
"user = file['user1']" #use `dict['key_name']` to find the value of the key. if key not found, will return a `KeyError` exception
user = file.get("user1") #use the `get()` method to find the key and return the value safely. if not found, will return `None`

if user is not None: #if the `user1` key exists in the file

    #modify the `password` key from the `user1` dictionary
    #to modify the value of a key, you must do `dict[key] = new_value`
    #even though doing so is risky when retrieving data, it is safe when writing
    #because, if the `password` key is not found when you write it, it will automatically create that key with the value you assigned
    #however, if the dictionary itself does not exist (i.e `user1`), then an error will occur
    #which is why I added a guard (`if user is not None:`) before writing it
    user["password"] = "abc123"

else:
    #if `user1` doesn't exist, create it
    file["user1"] = my_dict

#writing data to a json file
with open(path, "w") as f: # "w" means "write"
    json.dump(file, f, indent=4)

print(file)