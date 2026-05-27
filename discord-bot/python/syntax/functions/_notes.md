> _learned: 27/11/2025_
_(all examples can be found in the files in this directory.)_

function

parameter

argument: args, kwargs, *args, **kwargs


type hint
- type hints are a kind of annotations (like comments) where the function tells you the expected type(s) of a variable, a function argument, or a a return value
- syntax:
    - variable: `myNum : int = 23` _(expects the variable `myNum` to be of type `int`)_
    - function argument: `def myFunc(num : int)` _(expects the argument of the parameter `myNum` to be of type `int`)_
    - return value: `def myFunc(num) -> int` _(expects the function `myFunc` to return of type `int`)_
- a variable / argument / return value can have more than one type hint _(e.g. `myNum : int | float = 23`)_

- type hints are just annotations; even if the type is different than expected when running, no error will be raised _(unless you use type checkers like mypy and Pyright, which catch type inconsistencies)_

---

> _learned: 21/5/2026_

lambda

decorator

recursion

generator