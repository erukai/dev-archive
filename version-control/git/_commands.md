> _committed: 27/11/2025_

---

`git init`
- initializes the working directory as a local git repository
- version control files will be installed in a hidden `.git` folder
- the `.git` folder is what makes a working directory a valid repository
- without `.git`, using other git commands like `git commit` and `git push` will throw an error
- `git init` is one of the few git commands that can be run outside a git repository

`git remote add`
- connects a local repository to a remote repository
- local repository must be connected to a remote repository first before using synchronization commands like `git push` and `git pull`

---

`git clone`
- make a local copy of a remote repository to the working directory for the first time
- will throw an error if the command is used on an existing local repository *(i.e. a directory with a `.git` folder)*
- to make a local copy of a remote repository to an existing local repository, use `git pull` instead
- using `git clone` automatically connects the remote repository to the recently-initialized-and-copied local repository
- `git clone` is one of the few git commands that can be run outside a git repository

`git pull`
- make a local copy of a remote repository to the connected local repository and working directory
- will throw an error if the command is used outside of a local repository *(i.e. a directory without a `.git` folder)*
- to make a local copy of a remote repository to the working directory for the first time, use `git clone` instead
- `git pull` is essentially a combination of `git fetch` and `git merge`

---

`git add`
- "stage" the changes made to the files in a working directory (project) since the last commit
- staged files are sent to the "staging area" which lies between the working directory and the local repository
- can choose which files to stage

`git commit`
- captures a "snapshot" of the project's staged changes and records to local repository
- use `git commit -m "{message}"` to add a short description
- the changes must be staged using `git add` first

`git push`
- uploads the commits (snapshots/versions) on the local repository to a connected remote repository of the selected branch.
- full command is `git push [remote] [branch]`
- if remote and branch are not given, remote `origin` and branch `main` / `master` (or whatever the default branch was set to)

---

> _learned: 16/5/2026_

`git fetch`
- make a local copy of a remote repository to the connected local repository BUT NOT working directory
- used to view the changes that other developers have made to the remote repository before copying it to the working directory