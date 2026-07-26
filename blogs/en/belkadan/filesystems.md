---
title: Filesystems
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/filesystems'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35e7080cdbf79d80'
translated: false
---

> 原文：[Filesystems](https://belkadan.com/blog/tags/filesystems)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=filesystems)

26 November 2023

[A few days ago Julia Evans posted this:](https://social.jvns.ca/@b0rk/111462736760795943)

> has anyone made a read-only FUSE filesystem for a git repository where every commit is a folder and the folder contains all the files in that commit?
> 
> the idea is that you could just run `cd COMMIT_ID` and poke around instead of checking out the commit
> 
> and maybe the branches could be symbolic links to the commit folders?

And I _did_ in fact do something very like that, back when I was [playing with FUSE](https://belkadan.com/blog/2020/07/Suffusion/)! But I never put it up anywhere cause it had an annoying build process, and didn’t seem to add much, and—

[(Continue reading…)](https://belkadan.com/blog/2023/11/GitMounter/?tag=filesystems)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Git](https://belkadan.com/blog/tags/git), [Source code](https://belkadan.com/blog/tags/source-code), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## [Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=filesystems)

22 January 2023

My winter break project was getting the files off an old PowerBook from the 90s (my dad’s old work computer) that I’ve had lying around for a while. (There’s _probably_ not anything of interest there to anyone but our family, but who knows?) I’ve looked at this before, but it’s hard to get a [25-year-old computer](https://en.wikipedia.org/wiki/PowerBook_3400c) to talk to a modern OS.

[(Continue reading…)](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=filesystems)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Swift](https://belkadan.com/blog/tags/swift), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=filesystems)

07 July 2020

In addition to the personally-long-awaited launch of [Hermit Crab](https://belkadan.com/hermitcrab/), I’ve also spent the last week or so making a limited but easy-to-use Swift wrapper around the [FUSE](https://github.com/libfuse/libfuse/) APIs, which I’ve dubbed [Suffusion](https://belkadan.com/source/Suffusion/). Suffusion is heavily inspired by the [FUSE on macOS project](https://osxfuse.github.io)’s Objective-C APIs, but simplified down to only support read-only filesystems, which is all I really want right now.

[(Continue reading…)](https://belkadan.com/blog/2020/07/Suffusion/?tag=filesystems)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Source code](https://belkadan.com/blog/tags/source-code), [Package](https://belkadan.com/blog/tags/package), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## Older Posts

1. 2011-07-22[rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=filesystems)

### Possibly Related Tags

- [Git](https://belkadan.com/blog/tags/git)
- [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic)
- [Mac OS X](https://belkadan.com/blog/tags/mac-os-x)
- [Package](https://belkadan.com/blog/tags/package)
- [Source code](https://belkadan.com/blog/tags/source-code)
- [Swift](https://belkadan.com/blog/tags/swift)
- [Time Machine](https://belkadan.com/blog/tags/time-machine)
- [Unix](https://belkadan.com/blog/tags/unix)
