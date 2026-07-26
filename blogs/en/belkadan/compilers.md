---
title: Compilers
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/compilers'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8f6d847557ed5788'
translated: false
---

> 原文：[Compilers](https://belkadan.com/blog/tags/compilers)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=compilers)

28 December 2023

A few weeks ago I posted this:

[(screen recording)](https://belkadan.com/blog/2023/12/CellLVM/CellLVM.mp4)

Which, if you’re not interested in watching a video right now, is a proof-of-concept LLVM to Excel spreadsheet compiler.

[(Continue reading…)](https://belkadan.com/blog/2023/12/CellLVM/?tag=compilers)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [LLVM](https://belkadan.com/blog/tags/llvm), [Spreadsheets](https://belkadan.com/blog/tags/spreadsheets), [Source code](https://belkadan.com/blog/tags/source-code)

## [There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=compilers)

04 October 2023

> If I have an aligned machine-word-sized variable (Int) and I store to it from Thread A, then I know Thread B might see the old value instead of the new value (because of per-processor caching, or the compiler “hoisting” a load to earlier in the function). But there’s no way, on a modern processor, that Thread B sees a mix of the old and new value, right? That can only happen with wider values, or unaligned values, that the code may update non-atomically, right?

_This question is paraphrased from the Swift forums, though I’m not linking to it cause it’s in the middle of a larger thread and it’s something people might reasonably ask anyway. My response, lightly edited, is below; it is Swift-oriented but also applies to C, C++, and Rust._

[(Continue reading…)](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=compilers)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Compilers](https://belkadan.com/blog/tags/compilers)

## [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=compilers)

01 April 2020

It’s April 1, and that means it’s both [April Fools’ Day](https://en.wikipedia.org/wiki/April_Fools'_Day) and [the anniversary of the founding of Apple Inc.](https://en.wikipedia.org/wiki/History_of_Apple_Inc.) While this year is a sober one due to [current events](https://staythefuckhome.com), I think a lot of people still appreciate what people are creating and sharing to keep spirits up, whether that be music or art or…impractical programming projects. And while _pranks_ on April Fools’ seem less and less fun^[1](#fn:harder), obvious jokes and whimsy, not at anyone’s expense, are still something I believe in…and even better if they actually work.

Last year I implemented [the world’s best code visualizer](https://forums.swift.org/t/new-code-visualizer-for-swift-source-is-view/22454). This year I decided to seriously attempt something that I’d thought about in the past: getting a [Swift](https://swift.org) program to run on Mac OS 9.

[(Continue reading…)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=compilers)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Compilers](https://belkadan.com/blog/tags/compilers), [April Fools](https://belkadan.com/blog/tags/april-fools)

## Older Posts

1. 2016-05-23[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=compilers)
2. 2015-11-18[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=compilers)
3. 2015-05-09[Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/?tag=compilers)
4. 2015-01-24[“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=compilers)
5. 2011-07-29[Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/?tag=compilers)
6. 2011-06-20[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=compilers)

### Possibly Related Tags

- [April Fools](https://belkadan.com/blog/tags/april-fools)
- [Assembly](https://belkadan.com/blog/tags/assembly)
- [Book](https://belkadan.com/blog/tags/book)
- [Cocoa](https://belkadan.com/blog/tags/cocoa)
- [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)
- [Linking](https://belkadan.com/blog/tags/linking)
- [LLVM](https://belkadan.com/blog/tags/llvm)
- [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic)
- [Objective-C](https://belkadan.com/blog/tags/objective-c)
- [Open source](https://belkadan.com/blog/tags/open-source)
- [Programming languages](https://belkadan.com/blog/tags/programming-languages)
- [Source code](https://belkadan.com/blog/tags/source-code)
- [Spreadsheets](https://belkadan.com/blog/tags/spreadsheets)
- [Swift](https://belkadan.com/blog/tags/swift)
