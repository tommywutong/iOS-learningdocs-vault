---
title: “Skip the FFI”
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2015/01/Skip-the-FFI/'
original_language: en
published: 2015-01-24
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f77590b2656309a2'
translated: false
---

> 原文：[“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [SIGWINCH](https://belkadan.com/blog/2014/12/SIGWINCH/)

[AlterConf SF/Oakland](https://belkadan.com/blog/2015/02/AlterConf/) »

« [How to Write a Checker in 24 Hours](https://belkadan.com/blog/2012/12/How-to-Write-a-Checker/?tag=llvm)

["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/?tag=llvm) »

« [Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/?tag=compilers)

[Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/?tag=compilers) »

## [“Skip the FFI”](#)

I spoke again at last year’s [LLVM Developers’ Meeting](http://llvm.org/devmtg/2014-10/) with my coworker John McCall. Our talk, “Skip the FFI: Embedding Clang for C Interoperability”, was about using the [Clang](http://clang.llvm.org) compiler, in library form, to augment another language to work with C. This lets you present C declarations as if they were just special declarations in your own language rather than forcing your users to go through an external FFI. This is, of course, [relevant to what I currently work on](http://developer.apple.com/swift/).

The video of the talk is [now online](http://llvm.org/devmtg/2014-10/#talk18), along with slides and of course all the other talks.

This entry was posted on [January](https://belkadan.com/blog/2015/01) 24, [2015](https://belkadan.com/blog/2015) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [LLVM](https://belkadan.com/blog/tags/llvm), [Compilers](https://belkadan.com/blog/tags/compilers)
