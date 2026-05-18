#committed: 27/11/2025
#---

import os
from dotenv import load_dotenv #imports the function `load_dotenv` from the package `dotenv`

#loads .env file
load_dotenv()

#use the function `.getenv` from the module `os`to get the value of the key "WEATHER_API_KEY" file from the .env file
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

print(WEATHER_API_KEY) #returns 65c15wf156wqcc5e5asvsc1