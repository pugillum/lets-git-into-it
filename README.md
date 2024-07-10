# What is this?

This is a repo to help people getting started with git.  See in slides for the slides.

# Create a new repository

Create a directory called `tmp_repo` and in the terminal run
```sh
git init
```

Check the contents of the directory, you should see a `.git` folder has been created.

Run `git status` - what is the name of the branch created?

# Clone this repository

In this repo, select the "Clone" button. Select "HTTPS" and copy the URL that has been created.

In the terminal in a directory in which you have your project code run:
```sh
git clone <the url>
```

You will be asked for a password.  To generate it, back in the browser select "Generate Git Credentials".  Copy and paste the password generated (you won't need to keep it anywhere else)

In an IDE (VS Code) open the folder created

# Add a new commit

## Staging

Add a new file: `<your name>.md`

Run

 ```sh
 git status
 ```
You'll notice your file is "untracked"

Track your file by running:

 ```sh
 git add <your new file name>
 ```

Again run `git status` - git should now see your file

Add a bunch more files and then run `git status` again - what do you notice?

To add all the new files in one go, run `git add .`

> You can also unstage files using `git rm --cached <file name>`

## Committing

Okay, your files are staged, let's create a commit. Run

```sh
git commit -m "Adding some files 🗂️"
```

You should be able to see your commit on the branch by running:

```sh
git log main
```

Press `q` to exit

## Pushing your commit 🫸

You've created a wonderful commit, but how to share it with your team? We'll need to push it to the remote repository using `git push`

Run the following command:

```sh
git push
```

🔥 This didn't work! Why? `main` is protected 😷 from direct pushes

Time to branch!

# Working with branches 🪚

Run the following to create a new branch (Replace `<your name>` with your name):

```sh
git checkout -b <your name>/my_branch
```

If you run `git log main` you'll see that this branch also contains your commit 🥳

Let's try that push again:

```sh
git push
```

Oh no, it failed again! But this time you get some advice on what to do:

```sh
git push --set-upstream origin <your name>/my_branch
```

Now go into Azure DevOps and select "Repos" -> "Branches" - what do you see?



# Pull requests 🏊‍♀️

So you now have a remote branch containing a new commit.  How do you get it into the `main` branch? Time to create a Pull Request!

- In Azure DevOps, go to "Repos" -> "Pull requests".
- Select "New Pull Request"
- Press "Select a source branch..." and select your branch
- Tag some reviewers
- For the work item fill in 99084
- Get some approvals and then select "Complete"
- Pat yourself on your back and do a victory spin on your desk chair 💺

## Getting up to date

It's good to keep your local repository up to date with all the new code!

Back in the terminal, run:

```sh
git checkout main
```

You're now on the main branch.  It contains an extra commit which you couldn't push because of branch protection rules.  Let's get rid of that with:

```sh
git reset --hard HEAD~
```

And now let's get it up to date by running:

```sh
git pull
```

You should now see the file you added via your PR.

# Merge conflicts 🫣

When working with multiple people on the same project, you will end up working on code in the same location and this can lead to *merge conflicts*.

Ensure you are on `main` (You can run `git checkout main`)

Run the following commands:

```sh
git branch im_editting_1
git branch im_editting_2
```

Let's do stuff on `im_editting_1`:

```sh
git checkout im_editting_1
```

In this README file under "Let the merge conflict begin 🤼" add the line "Left hook! 🤜"

Stage and commit your change!

Now let's go to `im_editting_2`

```sh
git checkout im_editting_2
```

Again in this README.md add a line under "Let the merge conflict begin 🤼" add a line, but this time "Right hook! 🤛"

Stage and commit the change!

Now what happens if we try to merge `im_editting_1` into `im_editting_2`?  Run
```sh
git merge im_editting_1
```

What happens? See "Resolve Merge Conflicts" further below

## Merge conflicts happening below ☢️☣️⚠️

#######

Let the merge conflict begin! 🤼

#######

## Resolve Merge Conflicts

In README.md you'll notice some additional text has been added that looks something like:
```md
<<<<<<< HEAD
Right hook! 🤛
=======
Left hook! 🤜
>>>>>>> im_editting_1
#######
```

The top change is the last commit added, the bottom one is the commit that's coming in from `im_editting_1`.  It's fairly typical to solve these kinds of merge conflicts in the IDE but we'll do it here with text.

In the README.md, to keep both "hooks", delete the following lines and **save the file**.
```md
<<<<<<< HEAD
=======
>>>>>>> im_editting_1
```

Now stage the file using:

```sh
git add README.md
```

You can then continue with a commit and the merge conflict has been resolved! 😮‍💨

# Some tools to help with git

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [VS Code](https://code.visualstudio.com/) with extensions
  - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
  - [Git Blame](https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame)
  - [Git Lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [lazygit](https://github.com/jesseduffield/lazygit) - a UI in the terminal for keyboard shortcut lovers
- [SourceTree](https://www.sourcetreeapp.com/) - a git GUI for those who don't like the terminal
- Find what works for you! ✨

# What we didn't cover

*But do ask about it*

- `git remote add`
- `git reset`
- `force push`
- cherry picking 🍒
- `git blame`
- `rebase` 🫣
- detached HEAD 🤖
- pipeline triggers 🪠

# Some good references

- https://rogerdudler.github.io/git-guide/
- https://www.atlassian.com/git/tutorials/what-is-version-control
