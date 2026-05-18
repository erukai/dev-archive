> _learned: 18/05/2026_

_(all examples can be found in the files in this directory.)_

---

venv
- venv is a built-in module used to create isolated "virtual environments"
- a virtual environment is a self-contained directory tree that contains its own python interpreter and dependencies.
- take node.js for example. By default, packages are installed inside a folder called `node-modules` located inside the working directory
- but for python, no matter what directory you install the packages in, the packages will always be installed in `Python\Lib\site-packages` or similar _(depending on your operating system and whether the installation is per user or computer)_ instead of your working directory
- global packages can cause conflicts between different python projects that rely on different versions of packages
- so it is always a good practice to use venv for Python projects, even if it's small

using venv
- to create a venv folder, type `python -m venv <relative_path>` in the terminal of your working directory
- if you want to use venv, you must activate it by running `.venv\Scripts\activate` in the terminal
- you can also point your IDE's default interpreter to the `.venv` folder if you want it to automatically activate venv whenever you open a Python project
- to deactivate venv, just run `deactivate` in the terminal, or simply close the IDE
- when venv is active, the packages you install will be located inside the `.venv` folder