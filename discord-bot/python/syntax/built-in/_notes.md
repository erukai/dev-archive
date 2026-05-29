> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

`any({iterable})` -> `bool`
- returns `True` if ANY item in the iterable is truthy _(even if it's just one)_
- this function expects an iterable _(like sqeuences, sets, dictionaries)_ or any object with the method `_iter_`

`all({iterable})` -> `bool`
- returns `True` if ALL items in the iterable are truthy
- this function expects an iterable _(like sqeuences, sets, dictionaries)_ or any object with the method `_iter_`

`len({collection})` -> `int`
- returns the number of items in a sequence
- for strings, a single character is an item, so `len()` will return the number of characters in a string
- this function expects a collection _(like sqeuences, sets, dictionaries)_ or any object with the method `__len__`

`type({object})` -> `<class 'class_name'>`
- returns the type of an object _(an object's "type" is the object's class)_

`isinstance({object}, {class})` -> `bool`
- returns `True` if the specified object is an instance of a specific class _(meaning, if an object was created from a particular class)_
- for example, `isinstance("hello", str)` checks whether the object `"hello"` is from the `str` class. And since we know it's true, the function will return `True`
- `isinstance(56, dict)`, as another example, checks whether the object `560` is from the `dict` class. However, `56` is not from the `dict` class, but rather from `int`. So the function will return `False`

---

> _learned: 21/5/2026_

`map({function}, {iterable})` -> `<map object>` _(iterator)_
- applies a function to each item in an iterable
- it's like saying _"for each item in this iterable, do this function to it"_
- basically, calling a function in a `for` loop
- or in Python, it's the same as the code below:
```python
for item in ["item1", "item2", "item3"]:
    func_name(item)
```
- but instead of that, we just write:
```python
map(func_name, ["item1", "item2", "item3"]) 
```
- simply put, `map()` is useful if you want to call a function in an iterable
- however, `map()` returns a map object _(`<map object at 0x...>` when using `print()`)_
- to access the value of the _mapped_ iterable, convert the map object into a collection, like `list`, `tuple` or `set`
- so the entire process is basically just you creating a function and an iterable, use `map()` on them both, and then convert the map object back into another iterable/collection
- **IMPORTANT**: the `map` function is not the same as the `mapping` data type. Although the name is similar, the usage is unrelated