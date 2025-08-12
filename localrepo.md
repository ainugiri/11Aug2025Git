SCM - to track changes in the project files

Local Directory
    - set of files.
    - changes in the files
    - is it possible to track changes in the files?
    - Saving the doc -> in memory, update the file. 

git 
   - scm tool
   - if i want to track changes in the files, i can use git.
   - create a local repository, git init
   - git appl -> track the changes in the files
   - git add <file>
   - added to staging area -> untracked -> tracked
   - Once you made a set of changes, you can commit the changes, that is called as versioning.
   - git commit -m "message"
   - 7letter hash code -> commit id
   

git init: 
    - create empty repository
    - .git folder is created
    - .git folder contains all the information about the repository
    - .git folder is hidden folder
    - git init, setup the local repository, to track the changes in the files (but which files?)

git add <file>:
    - add the file to staging area (untracked -> tracked / modified -> staged)
    - once you add the file to staging area, it is ready to be committed., after commit, it is tracked.
    - if you make changes to the file after adding it to staging area, it is modified but not staged.
    - what are changes in the file?

git status:
    - check the status of the repository
    - which files are tracked, untracked, staged, modified, etc.
    - git status will show the current state of the repository.

modify a file:
    - if you modify a file after adding it to staging area, it is modified but not staged.
    - you can add the modified file to staging area again using git add <file>.