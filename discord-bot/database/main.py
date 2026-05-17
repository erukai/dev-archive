#from: commit 01

import json
import os

my_dict = {
    "user1": {
        "username": "john_doe",
        "password": "abc123"
    }
}

#creating path using `os.join` so that it won't break when on other operating systems
path = os.path.join("discord-bot", "database", "password.json")

#writing data to a json file
with open(path, "w") as f: # "w" means "write"
    json.dump(my_dict, f, indent=4)

#reading data from a json file
with open(path, "r") as f: # "r" means "read"
    file = json.load(f)

print(file)