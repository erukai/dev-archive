#committed: 27/11/2025
#---

#function without parameters
def hello():
    print("Hello!")

#---

#function with parameters
def introduction(name, age, city, occupation):
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}.")

#function with positional-only parameters
def intro_pos(name, age, city, occupation, /): #`/` marks the parameters BEFORE it as positional-only. Requires at least 1 parameter before jt.
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}.")

#function with keyword-only parameters
def intro_kw(*, name, age, city, occupation): #`*` marks the parameters AFTER it as keyword-only. Requires at least 1 parameter after jt.
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}.")

#function with parameters that are positional-only, keyword-only, and standard
def intro_pos_kw(name, age, /, city, *, occupation):
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}.")

#explanation for intro_pos_kw:
#`/` looks at the parameters BEFORE it, which are `name` and `age`. Therefore, `name` and `age` only accept positional arguments.
#`*` looks at the parameters AFTER it, which is `occupation`. Therefore, `occupation` only accepts keyword arguments.
#the `city` parameter lies in between `/` and `*`, where neither markers look at its direction. Therefore, `city` can accept both positional and keyword arguments.

#---

#calling a function using positional arguments (args)
intro_pos("John", 23, "Tokyo", "teacher")

#calling a function using keyword arguments (kwargs)
intro_kw(age=23, occupation="teacher", city="Tokyo", name="John")

#---

#calling a function with positional & keyword arguments (*args, **kwargs)

#positional arguments must come BEFORE all keyword arguments; not in between, and not after
#Order: args, kwargs

#example where `city` is passed as a KEYWORD argument.
#in this example, both `city` and `occupation` are keyword arguments.
#therefore, order/position for those two parameters do not matter
intro_pos_kw("John", 23, occupation="teacher", city="Tokyo")

#example where `city` is passed as a POSITIONAL argument.
#in this example, `name`, `age` and `city` are positional arguments.
#therefore, order/position for those three parameters matter
intro_pos_kw("John", 23, "Tokyo", occupation="teacher")

#---

#function with *args parameter (* = a "catch all" or "everything" wildcard)
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