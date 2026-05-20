#committed: 27/11/2025
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