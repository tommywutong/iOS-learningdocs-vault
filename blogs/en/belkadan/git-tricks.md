---
title: Git Tricks
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2012/10/Git-Tricks/'
original_language: en
published: 2012-10-02
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2c85189edef44caa'
translated: false
---

> 原文：[Git Tricks](https://belkadan.com/blog/2012/10/Git-Tricks/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Keyboard Adventures](https://belkadan.com/blog/2012/04/Keyboard-Adventures/)

[How to Write a Checker in 24 Hours](https://belkadan.com/blog/2012/12/How-to-Write-a-Checker/) »

« [git add](https://belkadan.com/blog/2011/06/git-add/?tag=git)

[Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/?tag=git) »

## [Git Tricks](#)

[Git](http://git-scm.com/) is one of the most useful tools in my programming toolbox besides the compiler itself. Sure, there are holy wars over which version control system is best ([Mercurial](http://mercurial.selenic.com), anyone?), but if you’re coming from CVS or Subversion, Git is a huge improvement. Or will be, once you get over the learning curve. I highly recommend _[Pro Git](http://git-scm.com/book)_ as a way to become fluent in Git.

If you already use Git, however, you might be wondering how to make it _more_ useful…perhaps by adding these commands to the `[alias]` section of your `.gitconfig` file! Okay, there are tons of these pages on the internet already, but here are the aliases I use, most of them on a close-to-daily basis:

---

```
st = status
```

The first alias is the simplest. There are a number of Git commands that start with “st”, so Git can’t just guess what you mean, but 95% of the time I just want to see what’s going on in my working copy. “`st`” is simply shorter to type than “`status`”.

---

```
stq = status -uno
```

“`stq`” is supposed to stand for “status quiet”. It simply filters out untracked files from the status listing, which can be useful if you have a lot of random files lying around for some reason. I’ve mostly stopped using this, though…a well-configured `.gitignore` or `exclude` file is a more discriminatory (and more lasting) way to deal with these. But I’ve listed it here because knowing about the `-u` option can be useful.

---

```
amend = commit --amend -C HEAD
```

Careful with this one! `git commit --amend` allows you to edit the _previous_ commit—the same as if you’d made a new commit, then merged it into the previous one with `git rebase -i`. But it stops to ask you if you want to change the commit message, which usually I don’t. This `git amend` just uses the previous commit message, always.

It’s not easy to undo this, but the original commit will be `HEAD@{1}`, which you should read as “whatever `HEAD` was one change before the current value”. Since every commit (and checkout, and more) resets `HEAD`, this lets you refer to whatever your state was before your last commit (or checkout, or whatever). You can straight-up reset the current branch by using `git checkout -B <branch> HEAD@{1}`.

(Remember, `HEAD` means “the commit my working copy is based on”, and almost always matches the latest commit in your current branch.)

If I ever _do_ want to edit the commit message, I can do that with `git commit --amend`, even if I have no files to change.

---

```
log1 = log --oneline
```

`git log` has some useful custom formats; the simplest is the compact “oneline” format. This is useful enough that I added this alias. One way I use this: add `--author=rose` to see at a glance everything I’ve done recently.

---

```
graph = log --graph --branches --format=format:'%h%C(bold)%d%C(reset) %s'
```

Yikes! You can tell it’s the same sort of thing going on as `log1`, because it still starts with `log`. But it’s a lot more complicated! Let’s break it down.

You’ve probably seen nice pictures of git branches emerging from and rejoining the main repository. `git log --graph` does the same thing, only with ASCII art, starting from the commits you specify…

…which in this case is `--branches`, meaning all branches (plus `HEAD`, I believe?) Since I usually only have a few branches active at once, it shows me what my repository looks like without being unmanageable. Even if I have only one branch, it’s still useful to see how far I’ve gotten from the upstream repository, thanks to…

…the complicated custom `--format`, which basically reads “abbreviated hash, list of names in bold (like `HEAD`, or `origin/master`), commit message”. Being able to see where my branches are relative to the upstream repository can be _really_ helpful.

Just try it, and tweak it if something bugs you. Trust me.

---

```
rebranch = ! "zsh -c \"if git branch \| grep -q $1; then if git st -bs \| grep -q $1; then echo 'Already on branch' $1; else git checkout -B $1 && git cherry-pick ^HEAD $1@{1}; fi; else echo 'No such branch:' $1; fi\" - "
```

Uh-oh.

No, I don’t expect you to read that. Here it is properly formatted. Git aliases just prefer to be on one line:

```
if git branch | grep -q $1; then
    if git st -bs | grep -q $1; then
        echo 'Already on branch' $1
    else
        # This is the important line!
        git checkout -B $1 && git cherry-pick ^HEAD $1@{1}
    fi
else
    echo 'No such branch:' $1
fi
```

Is that better? …Hm. Let me tell you the use case.

[Clang](http://clang.llvm.org/) is backed by a central SVN repository, but it has a nice Git mirror for fetching from trunk. (To avoid complications, it’s read-only…commits still need to be made through SVN.) An SVN repository doesn’t support merges—the history is _always_ linear. So the appropriate way to re-sync any local work with what’s coming in from upstream is to `rebase` your work onto the upstream master branch (conventionally `origin/master`).

The trouble is, what if I’ve been working on an up-to-date branch, but I want to go back to a branch I was working on a week ago? You’d think I could just do `git rebase origin/master feature-branch`, and indeed that will work (if you remember which order to put the two branches in). But the algorithm Git uses for this is awful: it first switches to `feature-branch` (basically using `checkout`), then resets that branch to match `origin/master`, and finally replays the commits on `feature-branch` to give you a merged tree. Essentially, I’ve now touched every file that was modified in _either_ branch, and probably have to do a full rebuild of my project.

`git rebranch` skips the `checkout` step. The line labeled “this is the important line” does three things:

1. Move the branch you selected to the current `HEAD`.
2. Switch to that branch.
3. Cherry-pick everything that’s not in `HEAD`’s history.

It’s more dangerous because if anything fails, it’s harder to get back to the way things were before; `git cherry-pick --abort` will leave `feature-branch` pointing at `origin/master` without any of its own commits. If you find yourself in this situation, **the old `HEAD` of `feature-branch` is still accessible**—for now—**as `feature-branch@{1}`**.

An additional caveat: the commit on a Git mirror of an SVN repo may not match your commit into that repo! At the very least, this will happen because SVN usernames don’t have an associated name and e-mail, so the upstream Git mirror has to pull them from some central table when it grabs the commit. That means my local branches may be based on commits that technically don’t exist in the master branch, and `cherry-pick` will complain about this.

I haven’t found a perfect solution for this yet.

TLDR: this is an unsafe optimization for rebasing a given branch onto the current branch, just so I don’t have to recompile everything.

---

```
svn-up = ! cd ${1-.} && git fetch && git svn rebase -l
```

Like I said, Clang and LLVM are backed by a Subversion repository, not a Git repository. Fetching from the Git mirror is usually faster than fetching from the SVN repo, though, so I use `git fetch && git svn rebase -l` instead of just `git svn rebase`. The `-l` means “only use local commits when rebasing”.

I didn’t come up with this (it’s recommended by the LLVM “Getting Started” guide), but I did add the `cd` at the beginning, which (unlike most git commands) allows me to update a repo that is not my current working directory. Combining this with custom directory shell aliases makes this very convenient: `git svn-up ~llvm`.

---

```
svn-show = ! "zsh -c 'git show ${$(git svn find-rev r${1#r}):-r${1#r}} --' - "
```

To translate from SVN revision numbers, use `git svn find-rev <revision>`. However, it’s very common for me to just want to _look_ at a particular SVN revision. This command wraps `find-rev` so that it immediately calls `show` with the result. If `find-rev` comes back empty, the alias uses a bit of shell trickery to substitute the SVN revision right back in, so that `show` will come back with a nice error message saying the revision doesn’t exist. (If you call `show` with no revision argument, it shows `HEAD`, and it’s not immediately obvious that `find-rev` failed.)

You might notice that this command and `rebranch` both wrap the command in a call to `zsh`. Doesn’t Git already use a shell to run aliases that start with “!”? Well, Git’s not so happy with some of the shell tricks I’m pulling here. (In particular, ‘#’ usually starts a comment.) Rather than try to figure out what sort of escaping I need, I just stuck the whole thing in another shell.^[1](#fn:arguments)

---

That’s my current collection of Git aliases. Got any cool ones you want to share?

**Bonus**: Set your `log.date` config option to `local` to show commit timestamps in local time by default.

1. There’s actually a better reason for this: although you can access arguments in a shell alias using the usual `$1`, `$2` notation that shell programmers are familiar with, Git _also_ appends them to the end of the command. This makes certain kinds of aliases easier (non-shell aliases almost always depend on this), but can very much confuse something like `git show`, which can _already_ take multiple arguments. By wrapping the call to `git show` in a shell invocation, we make sure that the arguments are only included when referenced with a variable. [↩︎](#fnref:arguments)

This entry was posted on [October](https://belkadan.com/blog/2012/10) 02, [2012](https://belkadan.com/blog/2012) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git)
