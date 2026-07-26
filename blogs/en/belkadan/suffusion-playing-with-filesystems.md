---
title: 'Suffusion: Playing with Filesystems'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/07/Suffusion/'
original_language: en
published: 2020-07-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c91e1b49f599c863'
translated: false
---

> 原文：[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)

[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/) »

« [ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=swift)

[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=swift) »

« [Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=source-code)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=source-code) »

« [rm vs. Time Machine](https://belkadan.com/blog/2011/07/rm-vs-Time-Machine/?tag=filesystems)

[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=filesystems) »

## [Suffusion: Playing with Filesystems](#)

In addition to the personally-long-awaited launch of [Hermit Crab](https://belkadan.com/hermitcrab/), I’ve also spent the last week or so making a limited but easy-to-use Swift wrapper around the [FUSE](https://github.com/libfuse/libfuse/) APIs, which I’ve dubbed [Suffusion](https://belkadan.com/source/Suffusion/). Suffusion is heavily inspired by the [FUSE on macOS project](https://osxfuse.github.io)’s Objective-C APIs, but simplified down to only support read-only filesystems, which is all I really want right now.more

Why FUSE? Because like compilers, filesystems are sometimes seen as mystic-level programming, beyond the abilities of mere mortals. And from my perspective as a former compiler developer, filesystems really are harder in a number of ways: they have to deal with concurrency and mutable state, they have to be fast, they should be secure, and above all else they have to _not corrupt user data._

But like compilers, you don’t have to jump into the deep end to learn about filesystems.[1](#fn:compilers) At its simplest, a filesystem is just a tree structure that you navigate with a shell or a file browser. _Read-only_ filesystems simplify things even further by only requiring you to implement a few operations. And FUSE makes it possible to do that without doing OS-level programming, or even root access.

I’ve used FUSE to explore archive formats, git repositories (with the help of [SwiftGit2](https://github.com/SwiftGit2/SwiftGit2)), and even dumps of Classic Mac resource forks. Porting these projects to Suffusion wasn’t hard and left me with code that was easier to maintain (if not actually shorter).

Suffusion works on macOS and Linux. If you build anything cool with it, let me know!

1. “[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/)” [↩︎](#fnref:compilers)

This entry was posted on [July](https://belkadan.com/blog/2020/07) 07, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Source code](https://belkadan.com/blog/tags/source-code), [Package](https://belkadan.com/blog/tags/package), [Filesystems](https://belkadan.com/blog/tags/filesystems)
