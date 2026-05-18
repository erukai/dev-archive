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
    "user1": {
        "username": "john_doe",
        "password": "abc123"
    }
}

#writing data to a json file
with open(path, "w") as f: # "w" means "write"
    json.dump(my_dict, f, indent=4)

#reading data from a json file
with open(path, "r") as f: # "r" means "read"
    file = json.load(f)

print(file)