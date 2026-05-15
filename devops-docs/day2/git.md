# Git Internals

When you initialize a Git repository using `git init`, a hidden `.git` directory is created within your project's root directory. This `.git` directory is the core of your Git repository, containing all the metadata and version control information.  Let's explore its key components:

## Key Components of `.git` Directory:

**HEAD:**  This file acts as a pointer, referencing the current branch you're working on.  It essentially tells Git which branch's commits should be reflected in your working directory.

**config:** This file stores the repository-specific configuration settings.  These settings override any global Git configurations you might have set in your home directory (`~/.gitconfig`).  If no local configuration is provided for a particular setting, Git defaults to the global configuration.

**description:** This file is used by the Gitweb program (a web-based Git repository browser) and is generally not directly manipulated by users.

**hooks:**  This directory contains scripts that can be triggered automatically at various points in the Git workflow, such as before or after a commit, push, or receive.  Hooks are useful for enforcing coding standards, running tests, or performing other automated tasks.

**info:** This directory contains repository-specific exclusion rules.  The `exclude` file within this directory works similarly to `.gitignore`, but it's not tracked by Git itself, making it suitable for personal ignore patterns that you don't want to share with others.

**objects:** This directory is the heart of Git's version control system. It stores all the content and metadata of your repository as compressed objects. Each object has a unique SHA-1 hash as its identifier.  The first two characters of the hash are used as a directory name, and the remaining characters form the file name within that directory. This structure optimizes storage and retrieval.

There are four main types of objects:

* **Commit objects:** Store metadata about a commit, including the author and committer details, timestamp, commit message, and a reference to the associated tree object.

* **Tree objects:** Represent directories. They contain a list of file names and their corresponding blob or tree objects (for subdirectories), along with file mode information.

* **Blob objects:** Store the actual content of files.  Each file version is stored as a separate blob object.

* **Tag objects:**  (Not mentioned in the original notes, but important) are used to mark specific commits with a user-friendly name, often for releases.

**refs:** This directory stores references to branches and tags.  Branches are stored under `refs/heads`, and tags are stored under `refs/tags`.  Each file in these directories contains the commit hash that the branch or tag currently points to.


# Branching

Branches in Git are essentially pointers to commits. They allow you to work on different features or bug fixes in parallel without affecting the main codebase. A branch is represented by a file within the `.git/refs/heads` directory. The file's name is the branch name, and its content is the commit hash that the branch currently points to.

## Main Branch:

The `main` branch (formerly known as `master` in older Git versions) is created by default when you make your first commit.  It usually represents the stable, production-ready version of your code.

## Branching Commands:

* `git branch`: Lists all existing branches in your local repository.

* `git branch <branch_name>`: Creates a new branch.

* `git checkout -b <new_branch_name>`: Creates a new branch and immediately switches to it.

* `git checkout <branch_name>`: Switches to the specified branch.

* `git merge <new_branch_name>`:  Merges the specified branch into the currently checked-out branch.

* `git branch -d <branch_name>`: Deletes the specified branch.

* `git log --oneline --graph --color`:  Visualizes the commit history with a graph and colors, providing a clear overview of branch structure and merges.  The `--oneline` flag shows each commit on a single line.


# Remote Repositories

Remote repositories are hosted on servers (like GitHub, GitLab, or Bitbucket) and act as a central hub for sharing code and collaborating with others.

## Remote vs. Local:

A local repository is the one on your machine, where you make changes and commit them.  A remote repository serves as a shared copy of the project.

## Remote Commands:

* `git remote -v`: Lists all remote repositories associated with your local repository, along with their URLs.  The `-v` flag stands for "verbose".

* `git remote add <alias> <remote_repo_url>`: Adds a new remote repository with a specified alias (usually `origin`) and URL.

* `git remote remove <alias>`: Removes a remote repository association.


This expanded explanation provides a more detailed understanding of the concepts presented in the original notes, clarifying Git's internal workings, branching mechanisms, and interaction with remote repositories.

# Undoing Changes in the Staging Area

You can Unstage the files (remove the file from the index while keeping the changes intact in the working directory):

```
git restore --staged <file-name>
```

The command will only affect the index, while you changes in the working directory are still the same. 

# Navigating Git History

### Viewing commit history

```
git log --online
```

The command will give the list of commits performed in history with thier abbreviated SHA-1 and commit message. Use it to identify the commit you want to inspect.

### Inspecting a specific commit

To inspect the past state of the directory, use: 

```
git checkout <commit-id>
```

You will enter a **detached HEAD** state where you can explore the directory using `git show` or `git tree-ls` but you should not create new commits unless you want to make the changes. To return the normal: 

```
git checkout main
```

### Exploring git's internal objects (optional)

Every commit, tree, and file content is stored as an object in .git/objects/. You can inspect them directly:

```
# Show the commit object
git cat-file -p <commit-sha>

# Example output
tree df796557d61dcf236c4931156b4ae068777fb753
author Kartikey <kartikey@example.com> 1234567890 +0530
committer Kartikey <kartikey@example.com> 1234567890 +0530

Initial commit message

# Show the tree object
git cat-file -p <tree-sha>

# Example output
100644 blob 07af81380248d433126ef464e286bc4abc3e57ca    file1.md
100644 blob 5bdf9a1bc46f2a2fe053b333014552755f9aaac9    gitfile.md

# Show the content of a blob (file)
git cat-file -p <blob-sha>
```

The blob content is exactly what the file contained at the time it was commited. 

# Git's Snapshot Model

Git does not store individual file changes as diffs. Instead, every commit records a complete snapshot of your working tree at that moment.

### What happens during a commit

When you run git commit, Git performs these steps:

1. It creates a blob object for every file whose content has changed (or is new). A blob is simply the raw file content plus a header.

2. It creates a tree object for every directory whose contents have changed (including the root directory). A tree is a sorted list of entries, each pointing to either a blob (file) or another tree (subdirectory) by its object ID (SHA-1).

3. Because unchanged files and directories already exist as objects in the database, Git simply reuses their existing object IDs. No new blobs or trees are written for them.

4. Finally, Git creates a commit object that points to the new root tree, stores your commit message, author information, and the parent commit(s).

Result: every commit object gives you the exact state of the entire project at that point in time, yet Git stores only the differences in the object graph.


### Visualizing the object graph

```
Commit → Root Tree
             ├── file1.txt → Blob (content)
             ├── docs/ → Sub-tree
             │     └── readme.md → Blob
             └── src/ → Sub-tree (unchanged → reused)
```

### How to inspect what you actually committed

Use these two commands together:

```
# See commit history with short hashes and messages
git log --oneline

# Examine exactly what changed in a specific commit
git show <commit-id>
```

`git show` displays:

- The commit metadata
- The diff between this commit’s tree and its parent’s tree

To see only the list of paths that changed, add `--name-only` or `--name-status`.
