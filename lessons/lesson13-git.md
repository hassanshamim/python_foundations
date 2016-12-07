[TOC]

# Git

What is git?  A distributed version control system

- Distrubuted = exists in many different places
- Version Control System = Allows us to keep a history of our files and work with current and past versions of those files (merge them, find differences, undo updates etc.)

#### Why?

![Why use git?](http://swcarpentry.github.io/git-novice/fig/phd101212s.png)

### Tools used

- Git
- command line
- GitHub
- any text editor

## Vocabulary

**Repository** - A database of history snapshots.  Contains files, folders, the history of those files, and additional git things (i.e. branches).

**Commit** - A snapshot of your files at a certain point in time.  I.e. v0, v1, etc.

**The Index**  AKA **Staging Area**  - A list of confirmed changes that will be included in the next snapshot (commit)

**Working Tree** - Any directory on your computer with a *repository* associated.  Generally this is the folder on your computer that contains all the relavent files to your project.

**Branch** - A name that references a certain *commit* or snapshot.  **ALL** it does is point to a commit.  The convention in which we use branches gives them their power.

**master** - by convention, the *main* branch.  If this is your software project, it's the version that's most up-to-date and stable.  If it's a term paper, it's the version that will end up being submitted.

**HEAD** - also a branch name.  git uses the *HEAD* branch to denote where you are in the timeline of a project

**origin** - by convention, the name of the copy of a repository that lives on GitHub **under your account**

**upstream** - by convention the name of the *source* copy of a repository.  i.e. hackoregon project maintained by hackoregon

**fork** - Create a remote copy of a repository, (i.e. on GitHub)

**clone** - Create a *local* copy of a repository (on your computer)

​	

### About commits

Commits are the snapshots of our working tree.  Each commit only tracks **changed** files, instead of making a whole copy of the entire working tree.  Since a commit only tracks changes, it has to know what the files looked like before the changes were made.  In order to know that, a commit references one or more other commits as its **parent**.  That is, by replaying all of any commits parents, one by one, we can figure out the state of the working tree.



Parts of a commit

- **sha1 hash** - a unique identifier for that commit
- **message** - a human-readable message that describes those changes
- **contents** - the changes to the files included in that commit
- **parents** - one or more parent commits which describes the state of the working tree before the changes described in the contents

**Note**: when a commit has more than one parent, it called a **merge commit**.  Merging is one technique to unify different sets of changes.



Visual Example of 2 commits in succession: ![Series of commits](http://swcarpentry.github.io/git-novice/fig/play-changes.svg)

![Merge](http://swcarpentry.github.io/git-novice/fig/merge.svg)Visual example of a merge commit

Example of a series of commits.  (master is a branch)

![Commit tree](https://git-scm.com/book/en/v2/book/03-git-branching/images/basic-branching-1.png) 



The flow of changes.  Edit File -> add changes to Index/Staging -> Create commit

![Commit-staging-repository](https://swcarpentry.github.io/git-novice/fig/git-committing.svg)



### Branches

Branches are simply a *reference*.  Generally if a branch points at a commit (C1) and a new commit is made with the previous commit as its parent (C2) the branch will now point to that new commit.  They are useful in tracking a series of changes.



When we want to test some changes in isolation, we will create a new branch and *commit* our changes to that branch.  When we are happy with our changes, we update our **master** branch with the work in the branch we just created.



Master and an example branch before merging.  Notice the split?  This reflects the fact that commits **C4** and **C3** contain different changes.

![Branches before merge](https://git-scm.com/book/en/v2/book/03-git-branching/images/basic-branching-6.png)



This is what the branches look like after **merging iss53 into master**.  Master now contains all the changes to the working tree that were made in iss53.

![Branches after merge](https://git-scm.com/book/en/v2/book/03-git-branching/images/basic-merging-2.png)

[This page](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) contains a detailed description of branching and merging, but the images alone will give you a good gist of the idea.

### General Workflow

##### When creating a new project

1. create the project folder
2. Make it a *repository* by typing `git init`
3. Do some work
4. Prep the parts you want to save by using `git add` any the relavent files
5. Create a snapshot with `git commit -m <description of snapshot>`



##### When working on a new feature, i.e. fixing a bug or adding new functionality

1. Create a new branch with `git branch <branchname>`
2. Switch to that branch so your work gets saved there `git checkout <branchname>`
3. Do work,  add files, create commits
4. When you are happy with the feature and want to incorporate it back into *master* branch:
   - `git checkout master`
   - `git merge <branchname>`
5. Now all your work for that feature is in your main branch.



##### Working on an existing project

1. Fork the repository
2. Clone your forked respository
3. Create a new branch
4. Do work in your new branch
5. Update your forked repository (often called origin) with your code - `git push origin`
6. Create a **pull request** in Github.
7. Incorporate feedback and update your feature branch, then push those changes to GitHub again
8. When it's ready, the project maintainers will merge your code into the main project codebase



## When in doubt

Have some changes/edits and unsure of what to do?  Afraid you might break something?  No worries.  Just do the following and then you'll be in a safe place.  This just saves your changes in their own branch without overwriting any of your other branches.  After doing the following, you can continue working until someone more comfortable with git can help you negotiate your changes.

1. Create a new branch - `git branch <branch_name>`
2. Checkout that branch `git checkout <branch_name>`
   1. Does git scold you about untracked changes?
      1. `git stash`
      2. `git checkout <branch_name>`
      3. `git stash pop`
3. Create a new commit with whatever changes you are afraid to make at the moment
4. `git add <file1> <file2>`
5. `git commit -m 'Saving my changes in case I break something later'`
6. `git checkout <original_branch>`

### Additional Tools

- [sourcetree](https://www.sourcetreeapp.com/)
- [git up](http://gitup.co/)

### Not Discussed

- `git rebase` (also see interactive rebasing)
- merge conflicts
- git submodules

### Guides and Resources

- [learn git branching](http://learngitbranching.js.org/) - Git command line practice in the browser
- [git-it](https://github.com/jlord/git-it-electron) - Similar to above but as a standalone app
- [git cheatsheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf) 
- [Atlassian Git Tutorial](https://www.atlassian.com/git/) ( well written IMO )
- [Git From the Bottom up](https://jwiegley.github.io/git-from-the-bottom-up/) -  a deeper dive into what git does under the hood.