#committed: 27/11/2025
#---

#if statement
bot = False

if bot is False: #execute if true
    print("You can visit the website!")


#if-else statement
age = 22

if age >= 18: #execute if true
    print("You are an adult!")
else: #execute if `if` is false
    print("You are a kid!")


#if-elif-else statement
day_index = 9

if day_index in range(0, 3): #execute if true
    print("Today is a weekend!")
elif day_index in range(3, 7): #execute if `if` is false
    print("Today is a weekday!")
else: #execute if `if` and all `elif` are false
    print("This is not a valid day.")


#short-hand if statement (if the `if` block only has 1 line to execute)
light = "green"

if light == "green": print("GO!") 


#ternary conditional statement
#(if both `if` and `else` only have 1 line to execute, provided that both blocks execute the same thing, only with different values)

age = 15
print("You are an adult!" if age >= 18 else "You are a kid!")


#match-case statement (if the object has multiple values)
day_index = 5

match day_index:
    case 0:
        print("Today is Sunday!")
    case 1:
        print("Today is Monday!")
    case 2:
        print("Today is Tuesday!")
    case 3:
        print("Today is Wednesday!")
    case 4:
        print("Today is Thursday!")
    case 5:
        print("Today is Friday!")
    case 6:
        print("Today is Saturday!")

    case _: #default "fallback" case if none of the cases above matched, similar to `else`. Must be placed last
        print("This is not a valid day.")

#---

#with list comprehension
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
# Output: [2, 4, 6]


#without list comprehension
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)

'''
As you can see, with a list comprehension, you don't need to declare the list beforehand
because the comprehension itself is done inside a list.
You also don't need to use `apppend()` because the expression in the list comprehension already does that by default.
'''
#[x for x in numbers if ...] == [x.append() for x in numbers if ...]

'''You can also make a simple comprehension without conditions'''

#[x for x in numbers] == [x.append() for x in numbers]

#with list comprehension without condition
numbers = [1, 2, 3, 4, 5, 6]
evens = [x**2 for x in numbers]
# Output: [1, 4, 9, 16, 25, 36]


#without list comprehension without condition
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for x in numbers:
    evens.append(x**2)

#---

#DATA TYPES

#numeric
num = 3 #int
pi = 3.14 #float
z2 = 3 + 4j #complex

#sequence
hello = "Hello World!" #str
fruits = ["apple", "banana", "grape"] #list
languages = ("english", "japanese", "arabic") #tuple
for i in range(3): pass #range

#set
random_numbers = {1, 20, 56, 760, 5, 3} #set
countries = frozenset(["United Kingdom", "China", "Japan"])

#mapping
user = {
    "username" : "john_doe",
    "password" : "abc123"
} #dict

bot = True #bool
age = None #NoneType

#---

#iteration
for char in "Hello World!":
    print(char) #will go through (iterate) every single character in the string, and print the letter in the current iteration

#---

#lambda