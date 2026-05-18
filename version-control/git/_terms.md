> _learned: 16/5/2026_

---

version control
- a system that records the changes of files in a working directory, such as the files you create, the lines you remove, or the folders you relocate
- it is primarily used to track the different versions of files in history
- There are two types of version control:

  1. Centralized Version Control System (CVCS)
      - a single repository on the server
      - developers "check out" the files they need to work on from the repository, then commit back to the server when work is done
      - must require an active internet connection to the server

  2. Distributed Version Control System (DVCS)
      - a **remote** repository on the server + a **local** repository on the client
      - with a local copy, the developer can work while offline and make local commits

- Distributed Version Control System is the modern type of version control used, as it is more beneficial
- In DVCS, the repository on the server is called a *"remote repository"*, while the repository on a developer's computer is called a *"local repository"* 

- Git is an open-source software that uses Distributed VCS
- while other DVCS softwares like Mercurial and Bitkeeper exist, Git is the undisputed industry standard for version control
- GitHub is a platform that allows developers to manage and share repositories and is used by the majority

---

remote 
- "remote" refers to the remote repository that a local repository is connected to
- a remote is given an alias by a local repository during `git init` or `git clone`
- the default alias is `origin`
- an alias is given to a remote repository to differentiate it with other remote repositories that a local repository may be connected to _(yes that is valid; a local repo can connect to more than one remote)_

branch

fork

merge

rebase

upstream

tag
- tags are like actual versions of the project
- they are reference points to important commits
- tags are commonly labeled with `v` followed by two or three sets of numbers, like `v1.0` or `v1.0.0`, depending on the developer's preference
- if the version is not finalized, the tag may be followed by terms like `alpha`, `beta`, or `preview`.