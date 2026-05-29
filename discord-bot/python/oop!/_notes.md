> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---


**instance (object), class, self (this), init (constructor)**


**dunder**

**Object**
- 

---

# Personal Thoughts

One ironic thing for me is that I started my discord project as my very first programming project.
But I couldn't, for the love of me, understand how OOP actually worked, and what the terms like `class`, `instance`, or `method` even meant.
It wasn't until like 8 months later when I started a web development project that I finally understood what an `object` actually is when learning JavaScript.

But because I understood OOP from JavaScript, I can't stop calling it _(by "it" I mean the object of a class)_ `object` even though Python calls it `instance`. So now even when developing Python, I call it an `object`.

Don't get me wrong though. It is also called an `instance` in most OOP languages including JavaScript, but it is more common to call it an object, which in my opinion was easier to understand.

But Python's terminology is slightly different. Because in Python, **EVERYTHING** is an object. Integers, strings, functions, even classes are objects in Python. And `instance`, which is an object of a class, is just one of the many types of objects in Python.

So when referring to the instance of a class in particular, "instance" is more commonly used in Python, while "object" can be used more loosely to refer to the same thing in JavaScript.

Well, it's not that strict anyway. It's just a terminology. But it can be crucial to understand the difference so that you won't stuck at misusing a particular term forever.

---
## Regarding Objects

In 3rd party libraries, there are classes like `datetime` and `ndarray`.
In discord.py, there are classes like `Embed`, `Bot` and `Intents`.
And as mentioned before, almost every element in Python is an object. `int`, `NoneType`, `list`, `funcion`, these are all classes for your objects.

An early misunderstanding I had when learning OOP in Python is that the mentioned terms above _(`int`, `Embed`, `ndarray`, etc.)_ are "instances" / "objects".
Kind of a stupid misunderstanding thinking about it again.
Those _(`int`, `Embed`, `ndarray`)_ are not instances. Those are classes.

I have to keep in mind regarding the term _"instance"_.
Whenever I see or think of the word _"instance"_, I must always remember the phrase _"instance of a class"_.
Because an instance is **ALWAYS** a **CREATION** of a class.
An instance is a creation. An object. An _"instantiation"_.
It is created. And when creating an instance from a class, you do `variable = Class()`.
See how that variable inherits values from the class? That variable IS the instance. The variable IS the object.

An instance is created. An object is created. They are created from a class.
When you use `type()` on a variable _(i.e. that is, an instance/object)_, it returns `<class 'class_name'>`.
If you do `print(type(10))`, it returns `<class 'int'>`.
Thus, `int` is the class. `10` IS the object. The variable IS the object.
The types _(`int`, `list`, `set`, `function`, `bool`, `NoneType`, `Embed`, `datetime`, `ndarray`)_, those are simply classes. Not objects.
That's a reminder for myself.

---