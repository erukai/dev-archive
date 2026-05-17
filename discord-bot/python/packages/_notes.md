> _from: commit 01_

_(all examples can be found in the files in this directory.)_

---

`requirements.txt`
- a file used to install listed python dependencies
- can be run with `pip install -r requirements.txt` in the terminal

`pip`
- the standard package installer for python
- used to install, uninstall, and manage packages for python
- example: `pip install numpy`

---

library, package and module
- all of them refer to a group of python files containing variables, functions & classes that can be used in other Python files
- the umbrella term for these three is "dependency"
- In other programming languages, "library", "package" and "module" may have a slightly dfferent meaning than in Python, but the general term "dependency" remains consistent

module
- a single Python file that may contain variables, functions and classes to be used by other Python files
- any Python file can use the variables, functions and classes of a module by importing it
- any Python file can be a module. Even a normal python file is considered a module if it is imported to another file
- an example of a module is Python's built-in module `math`

package
- a folder _(directory)_ that contains one or more modules
- must contain a file named `__init__.py` for Python to register the folder as a package
- an example of a Python package is `numPy`

library
- a collection of modules and packages
- sometimes used with package interchangeably
- an example of a Python library is `Matplotlib`