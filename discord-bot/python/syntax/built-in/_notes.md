> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

`any({iterable})` -> `bool`
- returns `True` if ANY item in the iterable is truthy _(even if it's just one)_
- this function expects an iterable _(like sqeuences, sets, dictionaries)_ or any object with the method `_iter_`

`all({iterable})` -> `bool`
- returns `True` if ALL items in the iterable are truthy
- this function expects an iterable _(like sqeuences, sets, dictionaries)_ or any object with the method `_iter_`

`len({collection})`
- returns the number of items in a sequence
- for strings, a single character is an item, so `len()` will return the number of characters in a string
- this function expects a collection _(like sqeuences, sets, dictionaries)_ or any object with the method `__len__`

`type({object})`
- returns the type of an object

`isinstance({object}, {class})` -> `bool`
- returns `True` if the specified object is an instance of a specific class _(meaning, if an object was created from a particular class)_
- for example, `isinstance("hello", str)` checks whether the object `"hello"` is from the `str` class. And since we know it's true, the function will return `True`
- `isinstance(56, dict)`, on the other hand, checks whether the object `560=` is from the `dict` class. However, `56` is not from the `dict` class, but rather from `int`. So the function will return `False`

---

> _learned: 21/5/2026_

`map()`