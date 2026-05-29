> _learned: 27/11/2025_
_(all examples can be found in the files in this directory.)_

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


**parameter**
- a parameter is a function's placeholder variable
- parameters can be used inside the function only _(local scope)_, but the data it receives is from outside the function _(i.e. when calling the function)_
- example of a function with parameters and when calling it:
```python
def addition(x, y):
    return x + y

z = addition(2, 3)
#the arguments `2` and `3` become the value of the parameters `x` and `y` respectively for this specific function call
```
- a function expects all of its parameters to receive an argument when calling it, no more or less.
- when not enough arguments are given when calling a function, a `TypeError: missing x required positional arguments` error will be raised
- however, there are exceptions:
    1. A parameter can have 1 **default** value. When the parameter have a default value, then not giving an argument for that parameter will not raise an error; rather, the default value will be used for that function call
    2. 1 parameter usually expects 1 argument, and collections like `list`, `tuple` and `set` are counted as 1 argument. But a parameter can also expect more than 1 argument, using `*args` and `**kwargs`. When those two types of arguments are expected, the parameters pack the excess arguments into a single tuple
- there are 2 main categories of parameters, and 2 sub-categories of parameters:
    - positional-only parameters
        - when you want a function to only accept positional-only arguments
        - if any keyword arguments are given, a `TypeError: got some positional-only arguments passed as keyword arguments` error will be raised
        - `/` must be added as the **last** parameter of a function
        ```python
        def func(x, y, /):
            return x + y

        func(2, 3)
        ```
    - keyword-only parameters
        - when you want a function to only accept keyword-only arguments
        - if any positional arguments are given, a `TypeError: takes 0 positional arguments but x were given` error will be raised
        - `*` must be added as the **first** parameter of a function
        ```python
        def func(*, name, city="Tokyo"):
            print(f"My name is {name} and I live in {city}.")

        func(name="John", city="Tokyo")
        ```
    - variable positional parameters _(*args)_
        - 
    - variable keyword parameters _(**kwargs)_

- the above are the categories of parameters. In practice, a normal function can take all positional, keyword, `*args` and *`*kwargs` parameters
- But if you deliberately set a function to be positional-only, then only positional parameters can be used
- Likewise, if you deliberately set a function to be keyword-only, then only keyword and `*kwargs` parameters can be used
- Notice how I didn't mention `*args` two points above? That's because, if you set a function to be positional-only _(`func(..., /)`)_, you cannot have variable positional parameters _(`*args`)_. A `**kwargs` parameter packs the excess arguments into a dictionary, but a `**args` parameter packs the excess arguments into a tuple.... ?

argument: args, kwargs, *args, **kwargs
- an argument is the value you pass into a function's parameter
- if you give less arguments than the number of required parameters, a `TypeError: missing x required positional arguments` error will be raised
- if you give more arguments than the number of parameters, a `TypeError: take x arguments but y were given` error will be raised
- there are 2 categories of arguments:
    - positional arguments
        - 
    - keyword arguments


**type hint**
- type hints are a kind of annotations (like comments) where the function tells you the expected type(s) of a variable, a function argument, or a a return value
- syntax:
    - variable: `myNum : int = 23` _(expects the variable `myNum` to be of type `int`)_
    - function argument: `def myFunc(num : int)` _(expects the argument of the parameter `myNum` to be of type `int`)_
    - return value: `def myFunc(num) -> int` _(expects the function `myFunc` to return of type `int`)_
- a variable / argument / return value can have more than one type hint _(e.g. `myNum : int | float = 23`)_
- **NOTE**: type hints are just annotations; even if the type is different than expected when running, no error will be raised _(unless you use type checkers like mypy and Pyright, which catch type inconsistencies)_

---

> _learned: 21/5/2026_

**lambda**

**decorator**

**recursion**

**generator**