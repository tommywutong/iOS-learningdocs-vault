---
title: LLVM
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/llvm'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:af1b21790c617be2'
translated: false
---

> 原文：[LLVM](https://belkadan.com/blog/tags/llvm)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=llvm)

28 December 2023

A few weeks ago I posted this:

Which, if you’re not interested in watching a video right now, is a proof-of-concept LLVM to Excel spreadsheet compiler.

[(Continue reading…)](https://belkadan.com/blog/2023/12/CellLVM/?tag=llvm)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [LLVM](https://belkadan.com/blog/tags/llvm), [Spreadsheets](https://belkadan.com/blog/tags/spreadsheets), [Source code](https://belkadan.com/blog/tags/source-code)

## ["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/?tag=llvm)

03 April 2018

If you browse through the Swift (or LLVM) codebase for a while, you’ll see a comment like [this](https://github.com/apple/swift/blob/3ffbc41d075b362f160ba685ee192d430551d233/lib/Serialization/SerializedModuleLoader.cpp#L278-L279):

```
// FIXME: Dependencies should be de-duplicated at serialization time,
// not now.
```

[(Continue reading…)](https://belkadan.com/blog/2018/04/FIXME/?tag=llvm)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [LLVM](https://belkadan.com/blog/tags/llvm)

## [“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=llvm)

24 January 2015

I spoke again at last year’s [LLVM Developers’ Meeting](http://llvm.org/devmtg/2014-10/) with my coworker John McCall. Our talk, “Skip the FFI: Embedding Clang for C Interoperability”, was about using the [Clang](http://clang.llvm.org) compiler, in library form, to augment another language to work with C. This lets you present C declarations as if they were just special declarations in your own language rather than forcing your users to go through an external FFI. This is, of course, [relevant to what I currently work on](http://developer.apple.com/swift/).

The video of the talk is [now online](http://llvm.org/devmtg/2014-10/#talk18), along with slides and of course all the other talks.

[(Continue reading…)](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=llvm)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [LLVM](https://belkadan.com/blog/tags/llvm), [Compilers](https://belkadan.com/blog/tags/compilers)

## Older Posts

1. 2012-12-08

  How to Write a Checker in 24 Hours
2. 2012-05-16

  Big News
3. 2011-07-25

  Using Clang from SVN in Xcode
4. 2011-06-20

  Automatic Reference Counting

### Possibly Related Tags

- Apple
- Cocoa
- Compilers
- Meta
- Objective-C
- Source code
- Spreadsheets
- Swift
- Xcode
