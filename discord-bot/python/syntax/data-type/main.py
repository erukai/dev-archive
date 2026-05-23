#committed: 27/11/2025
#---

#numeric
num = 3 #int
pi = 3.14 #float
z2 = 3 + 4j #complex

#sequence
hello = "Hello World!" #str
fruits = ["apple", "banana", "grape"] #list
languages = ("english", "japanese", "arabic") #tuple
num_range = range(3) #range

#set
random_num = {1, 20, 56, 760, 5, 3} #set
countries = frozenset(["United Kingdom", "China", "Japan"])

#mapping
user = {
    "username" : "john_doe",
    "password" : "abc123"
} #dict

bot = True #bool
age = None #NoneType

#---

for data in [num, pi, z2, hello, fruits, languages, num_range, random_num, countries, user, bot, age]:
    print(f"value: {data}, type: {type(data)}")