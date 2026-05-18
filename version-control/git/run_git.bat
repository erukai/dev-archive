:: this is a batch a file used to execute command written in this file into the terminal. 
::---

:: Prevents printing command line
@echo off

:: initializes a git repository in the working directory [git init]
git init

:: adds a remote repository to a local repository [git remote add <remote> <url>]
git remote add origin https://github.com/erukai/dev-archive.git

:: download contents from a remote repository to a non-repository [git clone <url>] 
git clone https://github.com/erukai/dev-archive.git

:: download contents from a remote repository to a local repository [git pull <remote> <branch>]
git pull origin main

:: adds changes into the staging area [git add <pathspec>]
git add .

:: commits staged files [git commit -m <message>]
git commit -m "initial commit"

:: pushes local commits to a remote repository [git push <remote> <branch>]
git push origin main

:: download contents from a remote repository to a local repository without merging to working directory [git fetch <remote> <branch>]
git fetch origin main