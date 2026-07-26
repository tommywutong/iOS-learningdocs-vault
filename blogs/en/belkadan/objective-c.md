---
title: Objective-C
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/objective-c'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a5bd7cfad743ba5e'
translated: false
---

> 原文：[Objective-C](https://belkadan.com/blog/tags/objective-c)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=objective-c)

14 May 2022

POV: You are a compiler targeting arm64[1](#fn:arm64), and you want some code to reference this global variable from the same library. The classic way to do this is to emit an instruction that loads “the address of X”, which will be [determined at run time by the dynamic loader](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/). But that’s not super efficient! For one thing, addresses are 64 bits long, and instructions are only 32 bits, so you can either break it up into multiple instructions, or load the address from some _other_ location. But more importantly, the global variable is _in the same library._ The dynamic loader isn’t going to break it up from this code[2](#fn:ios), and if we knew _how far away it was_ we could reference it that way.

That’s what the `adrp` instruction’s for.

[(Continue reading…)](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=objective-c)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Debugging](https://belkadan.com/blog/tags/debugging), [Objective-C](https://belkadan.com/blog/tags/objective-c)

## [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

26 August 2020

This is going to be another one of those posts where I did something ridiculous and then show you how I got there, so let’s just get right to it.

[(Continue reading…)](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Objective-C](https://belkadan.com/blog/tags/objective-c), [Rust](https://belkadan.com/blog/tags/rust), [Swift](https://belkadan.com/blog/tags/swift)

## [Presentation on PrintAsObjC](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/?tag=objective-c)

13 September 2019

Makin’ an internal presentation on a fairly friendly bit of the Swift compiler, PrintAsObjC, and

!["We have...imports (Pier 1)! Classes (in a classroom)! Protocols (via C-3PO)! Categories (from math)! Enums (wait that's just an eMac)! And, functions (coming soon)!"](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/slide.jpg)

[(Continue reading…)](https://belkadan.com/blog/2019/09/Presentation-on-PrintAsObjC/?tag=objective-c)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Objective-C](https://belkadan.com/blog/tags/objective-c), [Humor](https://belkadan.com/blog/tags/humor), [Social media import](https://belkadan.com/blog/tags/social-media-import)

## Older Posts

1. 2011-06-20

  Automatic Reference Counting
2. 2009-04-16

  Safer Plugin Categories
3. 2009-03-19

  Categories and +load
4. 2008-09-04

  Objective-J and Objective-C

### Possibly Related Tags

- Assembly
- Cocoa
- Compilers
- Debugging
- Humor
- LLVM
- Programming languages
- Rust
- Social media import
- Swift
