---
title: Source code
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/source-code'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:34694d7c6a3a86a9'
translated: false
---

> 原文：[Source code](https://belkadan.com/blog/tags/source-code)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=source-code)

28 December 2023

A few weeks ago I posted this:

[(screen recording)](https://belkadan.com/blog/2023/12/CellLVM/CellLVM.mp4)

Which, if you’re not interested in watching a video right now, is a proof-of-concept LLVM to Excel spreadsheet compiler.

[(Continue reading…)](https://belkadan.com/blog/2023/12/CellLVM/?tag=source-code)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [LLVM](https://belkadan.com/blog/tags/llvm), [Spreadsheets](https://belkadan.com/blog/tags/spreadsheets), [Source code](https://belkadan.com/blog/tags/source-code)

## [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=source-code)

26 November 2023

[A few days ago Julia Evans posted this:](https://social.jvns.ca/@b0rk/111462736760795943)

> has anyone made a read-only FUSE filesystem for a git repository where every commit is a folder and the folder contains all the files in that commit?
> 
> the idea is that you could just run `cd COMMIT_ID` and poke around instead of checking out the commit
> 
> and maybe the branches could be symbolic links to the commit folders?

And I _did_ in fact do something very like that, back when I was [playing with FUSE](https://belkadan.com/blog/2020/07/Suffusion/)! But I never put it up anywhere cause it had an annoying build process, and didn’t seem to add much, and—

[(Continue reading…)](https://belkadan.com/blog/2023/11/GitMounter/?tag=source-code)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Git](https://belkadan.com/blog/tags/git), [Source code](https://belkadan.com/blog/tags/source-code), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=source-code)

07 July 2020

In addition to the personally-long-awaited launch of [Hermit Crab](https://belkadan.com/hermitcrab/), I’ve also spent the last week or so making a limited but easy-to-use Swift wrapper around the [FUSE](https://github.com/libfuse/libfuse/) APIs, which I’ve dubbed [Suffusion](https://belkadan.com/source/Suffusion/). Suffusion is heavily inspired by the [FUSE on macOS project](https://osxfuse.github.io)’s Objective-C APIs, but simplified down to only support read-only filesystems, which is all I really want right now.

[(Continue reading…)](https://belkadan.com/blog/2020/07/Suffusion/?tag=source-code)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Source code](https://belkadan.com/blog/tags/source-code), [Package](https://belkadan.com/blog/tags/package), [Filesystems](https://belkadan.com/blog/tags/filesystems)

## Older Posts

1. 2020-02-04[Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=source-code)
2. 2020-01-28[ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=source-code)
3. 2020-01-13[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=source-code)
4. 2019-12-24[quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/?tag=source-code)
5. 2019-08-01[\> go east](https://belkadan.com/blog/2019/08/go-east/?tag=source-code)
6. 2015-05-09[Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/?tag=source-code)
7. 2011-06-30[Quick Look in TextMate](https://belkadan.com/blog/2011/06/Quick-Look-in-TextMate/?tag=source-code)
8. 2008-03-08[Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/?tag=source-code)

### Possibly Related Tags

- [Assembly](https://belkadan.com/blog/tags/assembly)
- [Cocoa](https://belkadan.com/blog/tags/cocoa)
- [Compilers](https://belkadan.com/blog/tags/compilers)
- [Filesystems](https://belkadan.com/blog/tags/filesystems)
- [Git](https://belkadan.com/blog/tags/git)
- [LLVM](https://belkadan.com/blog/tags/llvm)
- [Mac OS X](https://belkadan.com/blog/tags/mac-os-x)
- [Package](https://belkadan.com/blog/tags/package)
- [ROSE-8](https://belkadan.com/blog/tags/rose-8)
- [Shell](https://belkadan.com/blog/tags/shell)
- [Spreadsheets](https://belkadan.com/blog/tags/spreadsheets)
- [Swift](https://belkadan.com/blog/tags/swift)
- [TextMate](https://belkadan.com/blog/tags/textmate)
