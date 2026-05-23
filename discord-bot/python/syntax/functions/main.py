



#function without parameters
def hello():
    print("Hello!")

#function with parameters
def introduction(name, age, city, occupation):
    print(f"Hello! I am {name} and I am {age} years old. I live in {city} as a {occupation}")

#calling a function using positional arguments (args)
introduction("John", 23, "Texas", "teacher")

#calling a function using keyword arguments (kwargs)
introduction(age=23, occupation="teacher", city="Texas", name="John")

#calling a function with keyword & positional arguments (kwargs args)
#positional arguments must come BEFORE all keyword arguments; not in between, and not after
introduction("John", 23, occupation="teacher", city="Texas")

#---

#function with *args parameter
def greet_args(greet, *names):
  for name in names:
    print(greet, name)

greet_args("Hello", "John", "Jane", "Doe")

#function with **kwargs parameter
def greet_kwargs(**kid):
  print("His last name is " + kid["lname"])

greet_kwargs(fname = "Tobias", lname = "Refsnes")


#---

#function with type hints
def savings(money:int) -> str:
    print(f"I have ${money} in my savings account.")

#---

#lambda function
for i in [1, 2, 3]:
    pass

#---

#function with decorator




#---

#recursive function


#---

#generator function