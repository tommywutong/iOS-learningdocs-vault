---
title: GitMounter
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/11/GitMounter/'
original_language: en
published: 2023-11-26
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1e7ca39b8079936a'
translated: false
---

> 原文：[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Type Erasure in Rust](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/)

[Daylight Saving Is Temporal Time Zones](https://belkadan.com/blog/2023/12/Daylight-Saving-Is-Temporal-Time-Zones/) »

« [There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=swift)

« [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/?tag=git)

« [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=source-code)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=source-code) »

« [Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=filesystems)

## [GitMounter](#)

[A few days ago Julia Evans posted this:](https://social.jvns.ca/@b0rk/111462736760795943)

> has anyone made a read-only FUSE filesystem for a git repository where every commit is a folder and the folder contains all the files in that commit?
> 
> the idea is that you could just run `cd COMMIT_ID` and poke around instead of checking out the commit
> 
> and maybe the branches could be symbolic links to the commit folders?

And I _did_ in fact do something very like that, back when I was [playing with FUSE](https://belkadan.com/blog/2020/07/Suffusion/)! But I never put it up anywhere cause it had an annoying build process, and didn’t seem to add much, and—

Well, in any case, Evans asked to see it, so [here it is](https://belkadan.com/source/GitMounter/), cleaned up to be a plain old SwiftPM package. It should work on macOS and on Linux as long as you have FUSE ([macFUSE](https://osxfuse.github.io) or `libfuse-dev`), libgit2, pkg-config, and Swift installed; on Linux you’ll have to create the mount directory first. (If you run the command and it fails it’ll tell you what path it tried to use.)

```
% swift run mount-git /path/to/checkout
```

---

By the way, if you don’t know who Julia Evans is, they make [blog posts](https://jvns.ca) and [zines](https://wizardzines.com) exploring all sorts of software in a way accessible to newbies and veterans alike, all with a lovely sense of discovery and enjoyment. This follow-up post to the original prompt really underscores their approach:

> guys this is such a fun idea I cannot believe people are in the replies trying to explain to me why they think it is impractical
> 
> the whole point of computers is to do impractical things and see what happens

You should definitely follow them and/or subscribe to their newsfeed. :-)

This entry was posted on [November](https://belkadan.com/blog/2023/11) 26, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Git](https://belkadan.com/blog/tags/git), [Source code](https://belkadan.com/blog/tags/source-code), [Filesystems](https://belkadan.com/blog/tags/filesystems)
