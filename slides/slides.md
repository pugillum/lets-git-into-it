---
marp: true
theme: gaia
title: bla
backgroundColor: white
style: |
    .columns {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }

    

    h1,h2 {
        color: black;
    }

    img[alt~="center"] {
        display: block;
        margin: 0 auto;
    }

---

![center w:300](./images/Git-Icon-1788C.svg)
<br>
# Branching Out
Exploring the Wonders of Git <!-- fit -->

---

<style scoped>
h1 {
  color: black;
  font-size: 100px;
}
</style>

<!-- _class: lead -->
# git history

![bg w:300px right](linux-icon.svg)

<!--
Linus Torvalds - 2005 - when creating Linux
Current tooling was insufficient
-->

---

<style scoped>
h1 {
  color: black;
  font-size: 100px;
}
</style>

<!-- _class: lead -->
# why git?

---

# Distributed

![h:500px center](./images/git-distributed.svg)

<!--
own local copy
faster
don't get blocked
multiple copies is safer
-->

---

# Branching

![h:500px center](./images/branching.svg)

<!-- 
work isolated
can map your way of work, e.g. story to branch

-->

---

# Merging (via Pull Requests)

![h:500px center](./images/merging.svg)

<!--
prevent destruction
facilitate communication
-->

---

# Community

![h:500px center](./images/friday.png)

<!--
Git underpins most open source projects
It allows working everywhere
-->

---

# Some tools

- The terminal ⌨️
- PyCharm / IntelliJ
- VS Code with extensions
  - Git Graph
  - Git Blame
- lazygit
- SourceTree
- Find what works for you ✨

---

<style scoped>
h1 {
  color: black;
  font-size: 100px;
}
</style>

<!-- _class: lead -->
# let's use it

---

![bg fit](git_workflow.png)

---

![bg fit](branch_and_merge.png)

---

# Good practices

- continuous integration
- branch naming
- pull before push 
- `pre-commit`
- no secrets 🤫

![bg right](ohbehave.jpg)

---

# Good practices - PRs

- test before creation
- smaller is nicer 😊
- positive feedback 👍
- not approving one's own 😬

![bg right](ohbehave.jpg)




---

<col1>

```sh
git remote add origin git@github.com:pugillum/blabla.git
git branch -M main
git push -u origin main
```