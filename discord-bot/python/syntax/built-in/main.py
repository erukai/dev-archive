#committed: 27/11/2025
#---

if any(["hello", "world", 0]):
    print("The iterable has a truthy item!")
else:
    #"the iterable has a falsy item", and not "the iterable is falsy".
    #Because an iterable / collection  is still truthy as long as it has a truthy item.
    print("The iterable has a falsy item!")