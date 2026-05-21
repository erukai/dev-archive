> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

_(If I'm not that lazy, I could try to explain even the basic syntax. But teaching something so basic is mentally tiring for me, so I'll just cover the things that I find or used to find challenging.)_

conditional
- controls the flow of a program by executing specific blocks of code only when certain conditions are met
- there are two main sets of conditional keywords:
    - `if-elif-else`
    - `match-case`
- examples are shown in `main.py` in this directory

comprehension
- a short, one-line syntax used to create new collections _(e.g. lists, dictionaries, sets)_ from existing iterables
- `[{expression} for {item} in {iterable} if {condition}]`
- the `condition` is optional; you can have a simple `[{expression} for {item} in {iterable}]` comprehension

data type
- Python data types are divided into multiple categories:
    - Numeric _(number value)_: `int`, `float`, `complex`
    - Sequence _(ordered collection of items)_: `str`, `list`, `tuple`, `range`
    - Set _(unordered collection of unique items)_: `set`, `frozenset`
    - Mapping _(unordered collection of key-value items)_: `dict`
    - Boolean _(truth value)_: `bool`
    - None _(absence of value)_: `NoneType`
    - Binary _(binary value)_: `bytes`, `bytearray`, `memoryview`
- you can access the data type of an object using `type(object)`

sequence
- a sequence is a collection of ordered items
- a string (text) is considered a sequence, because it is a collection of ordered characters and symbols
- examples:
    - `str`: `"Hello World!"` _(an ordered and immutable collection of `H`, `e`, `l`, `l`, `o`, ` `, `W`, `o`, `r`, `l`, `d`, `!`)_
    - `list`: `["Hello", 5, True]` _(an ordered and mutable collection of `"Hello"` [`str`], `5` [`int`], `True` [`bool`])_
    - `tuple`: `(True, False, None)` _(and ordered an immutable collection of `True`, [`bool`] `False` [`bool`], `None` [`NoneType`])_
    - `range`: `for i in range(3)` _(an ordered and immutable range of numbers)_
- "ordered" means the sequence of items inside the collection is preserved, and can be accessed by the item's index number (starting with `0`)
- "mutable" means the collection can be changed, such as adding _(`.append()`)_ and removing items _(`.pop()`)_
- besides `range`, you can declare empty sequences like `x = ""`, `y = []` and `z = ()`
- Special note: if a tuple has only one item, the tuple must end with a comma (`,`), as in `z = ("apple",)` so that Python does not mistake the tuple for a parenthesized expression like in logic (`if ("male" or "female") and >= 18:`) or math (`2 * (3 + 4)`)

set
- set is not a sequence since it is unordered _(items don't have indexes, and therefore cannot be accessed by index number)_
- meaning you must access the item by name, or convert it into a sequence like `list` or `tuple`
- however, it is still a collection of items, and therefore is an iterable
- all items must be unique in an **unordered collection** like `set`
- however, for set especially, duplicated items are automatically removed during runtime and won't raise an error 
- example:
    - `set`: `{15, 68, 50}` or `set([15, 68, 50])`
    - `frozenset`: `frozenset([13, 256, 89])`
- a `set` can be declared by surrounding items with curly brackets (`{}`)  or using the `set()` method on an existing collection
- to create an empty set however, you must use the `set()` method without imputing any value
- you cannot create an empty set by declaring an empty curly bracket `{}` because that is reserved for an empty dictionary _(type({}) would return `<class 'dict'>`)_
- `frozenset` on the other hand can only be declared using the `frozenset()` method on an existing collection

mapping
- an object that stores items in key-value pairs _(`{key : value}`)_
- a mapping data type is **unordered**, and each key are unique
- unlike a set where Python will automatically remove the duplicated items, for a mapping data type like `dict`, the last key will **overwrite** the previous key with the same name
- while it matters not for other data types, it is extremely critical for a mapping data type since the values of the keys may be different
- for example, if you have an `"apple"` item in a set and you accidentally created another `"apple"` item, all duplicates of `"apple"` will be removed, leaving the set a single `"apple"` item
- but if you have an item `"fruit" : "apple"` in a mapping type and you accidentally created an item `"fruit" : "banana"`, because they have the same key `"fruit"`, the earlier key with the value `"apple"` will be overwritten to `"banana"`
- keys in a mapping type act like indexes
- to access the value of a key of a mapping type, you can write the key name where you would write the index number of sequence item
- example: `value = dict_name['key_name']` _(`apple = food['fruits']`)_ as opposed to `value = sequence[index]` _(`apple = fruits[0] `)_

boolean
- a boolean is a data that represents `true` or `false`
- `true` or `false`, `yes` or `no`, `1` or `0`
- these two simple yet contradictory values are one of the most vital aspects of programming and logic
- besides booleans, almost all expressions can be expressed with `true` or `false` using the function `bool()`
- when using `bool()`:
    - an expression that returns `True` is called "truthy"
    - elaborately, truthy expressions are:
        - any number that is not exactly `0` _(e.g. `1`, `9000`, `-550`, `0.1`, `-0.7`)_
        - any string with content _(e.g. `"hello"`, `"123"`, `" "`)_
        - any list, tuple, set and dictionary with content _(e.g. `["cat", "dog"]`, `("en", "jp")`, `{"banana", "apple"}`, `{"password" : "abc123"}`)_
        - the boolean `True` itself
    - an expression that returns `False` is called "falsy"
    - elaborately, falsy expressions are:
        - the number `0` _(NOT including fractions and decimals)_ (e.g. `0`, `0.0`)
        - an empty string _(e.g. `""`)_
        - any empty list, tuple, set and dictionary _(e.g. `[]`, `()`, `{}`)_
        - the NoneType value `None`
        - the boolean `False` itself

iterable
- an object that can be iterated; i.e. collections (sequence, set, mapping)


---

> _learned: 21/5/2025_

lambda