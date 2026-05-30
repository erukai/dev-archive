> _learned: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

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
    2. 1 parameter usually expects 1 argument, and collections like `list`, `tuple` and `set` are counted as 1 argument. But a parameter can also expect more than 1 argument, using `*args` and `**kwargs`. When those two types of arguments are expected, the parameters pack the extra arguments into a single tuple
- there are 2 main categories of parameters, and 2 sub-categories of parameters:
    - positional-only parameters
        - when you want a parameter to only accept positional arguments
        - if any keyword arguments are given, a `TypeError: got some positional-only arguments passed as keyword arguments` error will be raised
        - `/` must be added as the **last** parameter of a function
        ```python
        def func(x, y, /):
            return x + y

        func(2, 3)
        ```
    - keyword-only parameters
        - when you want a parameter to only accept keyword arguments
        - if any positional arguments are given, a `TypeError: takes 0 positional arguments but x were given` error will be raised
        - `*` must be added as the **first** parameter of a function
        ```python
        def func(*, name, city="Tokyo"):
            print(f"My name is {name} and I live in {city}.")

        func(name="John", city="Tokyo")
        ```
    - variable positional parameters _(*args)_
        - when you want a positional parameter to receive more than 1 argument
        - a variable positional parameter is marked with an asterisk _(`*`)_ before the parameter name _(hence why it's called `*args`)_
        - the `*args` parameter packs the extra arguments into a single **tuple** _(`(arg1, arg2, arg3)`)_
        - there can only be 1 `*args` parameter in a function, and it must be placed as the last positional parameter
        - example:
        ```python
        def func(name, *friends): #`name` takes the first argument of the function call, while `*friends` takes the rest
            print(name) #output: "John"
            print(friends) #output: ("Diana", "Mark", "Edison")

        func("John", "Diana", "Mark", "Edison")
        ```
        - even if the `*args` parameter receives 1 argument, it will still pack into a tuple _(e.g. `friends = ("Diana",)`)_
    - variable keyword parameters _(**kwargs)_
        - when you want a keyword parameter to receive more than 1 argument
        - a variable keyword parameter is marked with two asterisks _(`**`)_ before the parameter name _(hence why it's called `**kwargs`)_
        - the `**kwargs` parameter packs the extra arguments into a single **dictionary** _(`{key1=val1, key2=val2, key3=val3}`)_
        - there can only be 1 `*kwargs` parameter in a function, and it must be placed as the last keyword parameter
        - example:
        ```python
        def func(name, **friend_data): #`name` takes the first argument of the function call, while `**friend_data` takes the rest of the keyword arguments
            print(name) #output: "John"
            print(friend_data) #output: {"name": "Diana", "age": 24, "city": "Paris"}

        func("John", name="Diana", age=24, city="Paris")
        ```
        - even if the `*kwargs` parameter receives 1 argument, it will still pack into a dictionary _(e.g. `friend_data = {"name":"Diana"}`)_
-  standard parameters
    - when you want a parameter to accept both positional and keyword arguments
    - "standard" is not really a specific type of parameter; rather, it's the default state where a parameter would normally accept any kind of arguments, be it positional or keyword
    - in other words, a standard parameter that accepts both positional and keyword arguments are parameters that are not marked with `/, ...`, `*, ...`, `*...`, and `**...`
    - example of a function with standard parameters: 
    ```python
    def func(x, y, z):
        return x + y

    func(2, z=3, y=4)
    ```
    - **NOTE**: even though standard parameters are flexible, in that they accept any kinds of arguments, the general, "top-layer" structure must still be followed by both parameters and arguments. This particular topic will be addressed in the `structure of parameters & arguments` section below


**argument**
- an argument is the value you pass into a function's parameter
- if you give less arguments than the number of required parameters, a `TypeError: missing x required positional arguments` error will be raised
    - an exception is if the extra **parameters** have a **default value** _(e.g. `def func(param=default_val)`)_
- if you give more arguments than the number of parameters, a `TypeError: take x arguments but y were given` error will be raised
    - an exception is if the extra **arguments** are passed into a **variable parameter** _(`*args` or `**kwargs`)_
- there are 2 categories of arguments:
    - positional arguments
        - passed to a function by following the position of the function's parameters
        - example:
        ```python
        def func(name, age, city): #index 0: name, index 1: age, index 3: city
            pass

        func("John", 23, "Tokyo") #index 0: "John", index 1: 23, index 3: "Tokyo"

        #hence, name: "John", age: 23, city: "Tokyo"
        ```
        - will raise an error if less / more arguments are received
    - keyword arguments
        - passed to a function by using the parameter name as the "key" with the argument as the "value"
        - keyword arguments do not need to care about the position
        - example:
        ```python
        def func(name, age, city):
            pass

        func(city="Tokyo" name="John", age=23)
        ```
        - will raise an error if keyword _(parameter name)_ does not exist


**structure of parameters and arguments**
- a function can have a standard parameter _(not bound to any specific types)_, a positional-only parameter _(`..., /`)_, a keyword-only parameter _(`*, ...`)_, a variable positional parameter _(`*args`)_, and a variable keyword parameter _(`**kwargs`)_
- and in a function call, it can pass a positional argument, and a keyword argument
- each parameter/argument type are flexible in its own way
    - standard parameter: can take both positional & keyword arguments
    - positional argument: can be passed without keyword _(parameter name)_
    - keyword argument: can ignore parameter order
    - variable parameter _(`*args` & `**kwargs`)_: can take more than 1 argument
- however, as flexible as they _(parameters & arguments)_ are, they must still follow a rigid, general structure of positioning
- at its core, the most basic structure for parameters and arguments is:
```python
{positional}, {keyword}
```

1. Standard parameters
    ```python
    func({standard})
    ```
    - if a function contains all standard parameters, then the type of each parameter is decided when calling the function
    - arguments must also follow the `{positional} | {keyword}` order. If you want to call a function with standard parameters but pass both positional and keyword arguments, then your function call must start with positional arguments, and then keyword arguments.
    ```python
    def func(a, b, c, d):
        pass

    func(2, 3, d=10, c=5) # you cannot do `func(d=10, c=5, 2, 3)` because positional arguments must always be at the front
    ```
    - in the example above, the parameters are standard
    - when calling the function with `func(2, 3, d=10, c=5)`, the parameters `a` and `b` become positional, while parameters `c` and `d` become keyword

2. Positional-only & Standard parameters
    - order of parameters:
    ```python
    func({positional}, /, {standard})
    ```
    - example:
    ```python
    def func(a, b, c, /, d):
        pass

    func(2, 3, 5, d=10)
    ```
    - in the example above, the parameters `a`, `b` and `c` are positional-only, while `d` is standard _(flexible)_
    - when calling the function with `func(2, 3, 5, d=10)`, the standard parameter `d` becomes keyword

3. Positional-only, Keyword-only & Standard parameters
    - order of parameters:
    ```python
    func({positional}, /, {standard}, *, {keyword})
    ```
    - example:
    ```python
    def func(a, b, /, c, *, d, e):
        pass

    func(2, 3, 5, d=10, e=7)
    ```
    - in the example above, the parameters `a` and `b` are positional-only, `c` is standard, while `d` and `e` are keyword-only
    - when calling the function with `func(2, 3, 5, d=10, e=7)`, the standard parameter `c` becomes positional

4. Positional-only, Keyword-only, Standard parameters & `*args`
    - order of parameters:
    ```python
    func({positional}, /, {standard}, *{args}, {keyword})
    ```
    - example:
    ```python
    def func(a, b, /, c, *x, d, e):
        pass

    func(2, 3, 5, 25, 80, 71, d=10, e=7) #x = (25, 80, 71)
    ```
    - in the example above:
        - positional-only: `a=2`, `b=3`
        - standard -> positional: `c=5`
        - extra positional: `x = (25, 80, 71)`
        - keyword-only: `d=10`, `e=7`
    - **NOTE**: when a function has both variable positional parameter _(`*args`)_ and keyword parameters, you only need to write `({positional}, *args, {keyword})` instead of `({positional}, *args, *, {keyword})`, because `*args` already acts as a separator between the positional parameters on the left, and the keyword parameters on the right
    - Another important thing to note is that, if you use `/` and `*args` in your function, then the standard parameter before it will be pretty much redundant, since it would automatically become positional as it is trapped by both `{positional}` and `{*args}` _(variable positional)_


5. Positional-only, Keyword-only, Standard parameters, `*args` & `**kwargs`
    - order of parameters:
    ```python
    func({positional}, /, {standard}, *{args}, {keyword}, **{kwargs})
    ```
    - example:
    ```python
    def func(a, b, /, c, *x, d, e, *y):
        pass

    func(2, 3, 5, 25, 80, 71, d=10, e=7, f=15, g=19, h=21) #x = (25, 80, 71); y = {'f'=15, 'g'=19, 'h'=21}
    ```
    - in the example above:
        - positional-only: `a=2`, `b=3`
        - standard -> positional: `c=5`
        - extra positional: `x = (25, 80, 71)`
        - keyword-only: `d=10`, `e=7`
        - extra keyword: `y = {'f'=15, 'g'=19, 'h'=21}`

---

**default argument**
- a fallback value assigned to a function parameter when created
- a parameter with a default argument will not raise an error if it does not receive an argument when the function is called
- syntax is: `def func(param=default_value)`
- example _(no argument)_:
```python
def func(string="Hello World!"):
    print(string)

func() #output: "Hello World!"
```
- however, if an argument is provided during a function call, that argument will be used
- example _(with argument)_:
```python
def func(string="Hello World!"):
    print(string)

func("My name is John.") #output: "My name is John."
```