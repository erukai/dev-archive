#committed: 27/11/2025
#---

#function without parameters
def hello():
    print("Hello!")

#function with parameters
def introduction(name, age, city, occupation):
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}.")

#calling a function using positional arguments (args)
introduction("John", 23, "Tokyo", "teacher")

#calling a function using keyword arguments (kwargs)
introduction(age=23, occupation="teacher", city="Tokyo", name="John")

#calling a function with keyword & positional arguments (kwargs args)
#positional arguments must come BEFORE all keyword arguments; not in between, and not after
#Order: args, kwargs
introduction("John", 23, occupation="teacher", city="Tokyo")

#---

#function with *args parameter (* = a "catch all" or "everything" widlcard)
def greet_args(greet, *names):
  for name in names:
    print(greet, name)

greet_args("Hello", "John", "Jane", "Doe")

#function with **kwargs parameter (* = a "catch all" or "everything" widlcard. **kwargs has two * to differentiate from *args)
def greet_kwargs(**names): 
  print("My last name is " + names["lname"])

greet_kwargs(fname = "John", lname = "Doe")

#function with args, *args, kwargs & **kwargs parameters
#Order: args, *args, kwargs,  **kwargs
def greet_all(name, *friends, married:bool=False, **spouse_info):
    fr = ", ".join(friends)

    phrase_name = f"Hello! I am {name}."
    phrase_hobbies = f"My friends are {fr}." if friends else f"I don't have any friends."
    phrase_married = f"I am married." if married else f"I am not married."
    phrase_spouse = f"My spouse's name is {spouse_info['sp_name']} and is {spouse_info['age']} years old." if spouse_info else ""

    print(phrase_name, phrase_hobbies, phrase_married, phrase_spouse)

greet_all("John", "Jane", "Evelyn", "Brad", married=True, sp_name="Tulip", age=23)

#---

#function with type hints
def savings(num:int|float) -> str: #num is expected to be of type `int` or `float`, and the function is expected to return the type `str`
    return str(num)

#---

#lambda function
temp_func = lambda x : x + 1
print(temp_func(5))

#---

#function with decorator




#---

#recursive function


#---

#generator function