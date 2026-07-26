---
title: git add
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/git-add/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f1951dd3ae508b2b'
translated: false
---

> 原文：[git add](https://belkadan.com/blog/2011/06/git-add/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/)

[Priorities](https://belkadan.com/blog/2011/07/Priorities/) »

[Git Tricks](https://belkadan.com/blog/2012/10/Git-Tricks/?tag=git) »

## [git add](#)

Yesterday, I was trying to explain `git add` and `git commit` to someone, and hit upon these very clear ways (IMHO) of explaining them:

- adds changes to the next commit
- saves any

  ed changes to the (local) repository

Why is this particularly clear? It eliminates any notion of “tracked files”.[1](#fn:hunks) You use `add` whenever you want to record changes in your version history, whether files are new or not.more

For people who prefer the classical workflow of “commit every modification to a tracked file”, there’s `git commit -a`. I used to think of `-a` as “all”, but now I think of it as “add”. I’ve shot myself in the foot a couple of times with this classic style (committing a file that’s not part of the current logical change), so I’ve mostly given it up when working in a Git/Mercurial repo. (Not that I haven’t left a file out of a change using the two-stage commit.)

Of course, my usual Git workflow now is [through TextMate](https://github.com/jcf/git-tmbundle), which shows you all modified and untracked files in the current directory and allows you to check them off when you say “Commit”.

1. For that matter, it eliminates any notion of “files” at all, since git allows staging _parts_ of a file (“hunks”) for a commit. [↩︎](#fnref:hunks)

This entry was posted on [June](https://belkadan.com/blog/2011/06) 27, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Git](https://belkadan.com/blog/tags/git)
