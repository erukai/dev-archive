> _learned: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

**function**
- a function is a **block of code** that only runs when it is _"called"_ _(in other words, "executed" / "run")_
- a function is reusable, meaning it can be called more than once
- to declare a function, do this:
```python
def func_name(params):
    ...
```
- where,
    - `def`: a keyword used to declare a function
    - `func_name`: the name of the function. Name it whatever you want, as long as it does not clash with built-in words or existing objects
    - `()`: parentheses, used to hold parameters. if the function does not expect any arguments, the parentheses are still required, just empty
    - `params`: a placeholder for a function's parameters, which are written inside a function's parentheses and separated by a comma
    - `...`: just a placeholder for *expressions*, which are the blocks of code you put in a function. the expressions in a function are what executed when being called
- a Python file is executed line-by-line, from top to bottom. But if the block of code is inside a function, it will not be executed unless when called.
- to call a function, just write:
```python
func_name(args)
```
- where,
    - `func_name`: name of the function when you declared it with `def`
    - `args`: a placeholder for a function call's arguments, which are written inside a function call's parentheses and separated by a comma
- if the function does not expect any arguments, you call the function with empty parentheses _(`func_name()`)_
- unlike JavaScript, you cannot _hoist_ a function in Python _(to hoist is to call a function / access a variable before it is being created)_
- you must declare a function first before calling it, much like how you must declare a variable before accessing it

**_further elaboration on `function`_**
- everything in Python is an object, and for functions, its object is a `function` type
- and since objects can be stored as values, you can declare a variable to a function
- to do that, just write `var_name = func_name`, where `func_name` does not have parentheses
- then, to call the function through the variable, use parentheses on the variable, including any necessary arguments, like `var_name(args)`
- do not confuse between `var_name = func_name` and `var_name = func_name()`. When declaring a variable to a function without parentheses _(i.e. just the name of the function)_, the variable stores the function object. So printing the variable will simply return `<function func_name at 0x...>`. It's the same as printing the function without parentheses; in other words, the variable simply references the function
- but if you declare a variable to a function with parentheses _(i.e. calling a function, or what I prefer to call it a "function call" as a noun)_, rather than referencing the function, the variable ACTUALLY calls the function, and the return value of the function is stored in the variable
- That is in fact how you store the return value of a function; because if a function returns a value, then you would need something to store the return value of the function




**type hint**
- type hints are a kind of annotations _(like comments)_ where the function tells you the expected type(s) of a variable, a function argument, or a return value
- syntax:
    - variable: `myNum : int = 23` _(expects the variable `myNum` to be of type `int`)_
    - function argument: `def myFunc(num : int)` _(expects the argument of the parameter `myNum` to be of type `int`)_
    - return value: `def myFunc(num) -> int` _(expects the function `myFunc` to return of type `int`)_
- a variable / argument / return value can have more than one type hint _(e.g. `myNum : int | float = 23`)_
- **NOTE**: type hints are just annotations; even if the type is different than expected when running, no error will be raised _(unless you use type checkers like mypy and Pyright, which catch type inconsistencies)_

---

> _learned: 21/5/2026_

**lambda**
- a keyword used to create a single-expression anonymous function _(meaning the function is defined without a name)_
- it is primarily used to create a quick, one-time use function that only has one expression
- a lambda expression creates a function object
- a lot of the times you would use a lambda expression directly inside another method or function call _(that accepts a function object)_
- for example:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]
```
- if you don't want to use the lambda expression immediately, you can store it in a variable. It's no different than storing a regular function in a variable, since both functions create a function object
```python
square_var = lambda x: x ** 2
```
... is the same as:
```python
def square_func(x):
    return x ** 2
```
- both `square_var` and `square_func` creates a function object

**decorator**

**recursion**

**generator**