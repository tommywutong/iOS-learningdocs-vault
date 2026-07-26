---
title: Cocoa
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/cocoa'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:450b17e222fa8ce6'
translated: false
---

> 原文：[Cocoa](https://belkadan.com/blog/tags/cocoa)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=cocoa)

20 June 2011

In the Cocoa world, the big news from WWDC is the advent of Automatic Reference Counting, or ARC. The only real documentation for the system is an [unlinked reference page](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) on the Clang website, but as Clang is open source and the implementation’s in the latest builds now, that counts as public information.

The Cocoa frameworks have long used a reference-count-based system, but as of Mac OS X v10.5, Apple added optional garbage collection. As with most GC systems, you can mark certain references as `__weak` (which automatically become `nil` when their target is collected), and the actual collection of…

[(Continue reading…)](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=cocoa)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa), [Objective-C](https://belkadan.com/blog/tags/objective-c), [LLVM](https://belkadan.com/blog/tags/llvm), [Compilers](https://belkadan.com/blog/tags/compilers)

## [Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/?tag=cocoa)

21 July 2009

Recently I had occasion to deal with the Finder, beyond what NSFileManager or NSWorkspace could handle. Now, the easy way to do this is through AppleScript, and Cocoa does provide a way to run AppleScripts (NSAppleScript). The trouble is, (a) NSAppleScript is slow and only runs on the main thread, and (b) you can’t pass input easily.

AppleScript is built on Apple events, a mid-to-high-level form of interprocess communication that’s been around since System 7. Apple events can be constructed and sent off using either pure C code (what’s now part of the CoreServices framework) or the Objective-C wrapper, NSAppleEventDescriptor,…

[(Continue reading…)](https://belkadan.com/blog/2009/07/Scripting-Bridge/?tag=cocoa)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa)

## [Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=cocoa)

16 April 2009

Why did I miss last week’s post? To test this!

A few posts back I [suggested](http://belkadan.com/blog/2009/03/Categories-and-load/) the use of a category’s `+load` method as a way to safely swizzle methods in a plugin. What do you do, though, if the _same_ category is going to be loaded twice?

The established behavior of categories, of course is that the last one loaded “wins”.

The behavior of _classes_, however, is that the _first_ one loaded wins.

That is, if a bundle defines a class with the same name as an existing class, it is not loaded. `[bundle principalClass]` returns the existing…

[(Continue reading…)](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=cocoa)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Objective-C](https://belkadan.com/blog/tags/objective-c), [Cocoa](https://belkadan.com/blog/tags/cocoa)

## Older Posts

1. 2009-03-19

  Categories and +load
2. 2008-03-08

  Alerts Without Apps (or nibs)
3. 2008-01-14

  NSNumber, CFNumber, and CFBoolean
4. 2007-10-27

  Performance Optimization: Why We Can't Use valueForKeyPath:

### Possibly Related Tags

- Compilers
- LLVM
- Objective-C
- Source code
