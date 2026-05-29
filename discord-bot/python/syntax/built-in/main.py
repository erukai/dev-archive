#committed: 27/11/2025
#---
import os
path = os.path.join("discord-bot", "python", "oop")

import sys
sys.path.append(path)

import mymain as myModule
print("---")

#---

rand_list = ["hello", "world", 0]

if any(rand_list):
    #as long as an iterable has at least one truthy item, `any()` will return `True`
    print("The iterable has a truthy item!")
else:
    #if all items in the iterable are falsy, that's when `any()` will return `False`
    print("The iterable is falsy!")


if all(rand_list):
    #if all items in the iterable are truthy, `any()` will return `True`
    print("The iterable has a truthy item!")
else:
    #if even a single item in the least is falsy, `any()` will return `False`
    print("The iterable has a falsy item!")


list_len = len(rand_list)
print(list_len)

#-----------

money = 120.70
print(type(money))

if isinstance(money, str):
    print("Object is an instance of the `str` class. In other words, the object's type is `str`.")
else:
    print("Object is NOT an instance of the `str` class. In other words, the object type is NOT `str`.")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def statistics(self):
        print(f"brand: {self.brand}, model: {self.model}")

#if the type/class is not built-in, will return `<class 'module_name.obj_name'>`
myPlayer = myModule.Player()
print(type(myPlayer))

#but if the class is created in the same file where `type()` is used, will return `<class '__main__.obj_name'>` instead
myCar = Car(brand="Vokswagen", model="Golf")
print(type(myCar))

if isinstance(myPlayer, myModule.Player):
    print("Object is an instance of the `Player` class. In other words, the object type is `Player`.")

#-----------
nums = [1, 2, 3, 4]

# Squares each number. The `map()` function returns a map object.
#`map()` expects the first argument to be a function.
#If you want to use `map()` with a quick and simple function, you can use `lambda`, since it creates an anonymous, single-expression function
squares_map = map(lambda x: x**2, nums)

#To access the values in a map object, convert it into an iterable collection
squares_list = list(squares_map)

print(squares_map) # <map object at 0x...>
print(squares_list) # [1, 4, 9, 16]