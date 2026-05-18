> _committed: 27/11/2025_

_(all examples can be found in the files in this directory.)_

---

path
- a path is the address of a file or folder on a computer
- an example of a Windows path is `C:\Users\Documents\file.txt`
- the symbol that separates directories is called a separator, which is `/` or `\` depending on the operating system
- to be specific, Windows is the only operating system that uses `\` while others use `/`

types of path
- there are two types of path:
    - absolute path
    - relative path

---

absolute path
- starts from the very root of the filesystem _(e.g. `C:` on Windows)_
- example: `C:\Users\Username\Desktop\MyProject\my-folder\file.txt`
- it is extremely not recommended to use absolute paths when coding since the path would be utterly useless on other computers

relative path
- locates a file or directory relative to your current working directory
- if your working directory is `\MyProject\`, then the relative path to `file.txt` is: `discord-bot\main.py`
- you can also use `.` and `..` to navigate to other files relative to the directory
- `.` refers to current directory, while `..` refers to the parent directory
- for example, if you have a file in `Desktop`, then the relative path to the file from `\MyProject\` is `..\Desktop\second_file.txt`
- and if you have a file in `Username`, then the relative path to the file from `\MyProject\` is `..\..\Desktop\third_file.txt`

---

writing path in coding
- it is not recommended to hard-code the directory separator since different operating systems use different separators
- for example, Windows uses `\` while Linux and MacOS use `/`
- so if you want your code to work cross-platform, use a function that combines directories