---
title: CHDataStructures on the iPhone
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2009/12/chdatastructures-on-the-iphone/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fa2876233e07ef88'
translated: false
---

> 原文：[CHDataStructures on the iPhone](https://oleb.net/blog/2009/12/chdatastructures-on-the-iphone/)　·　Ole Begemann

# CHDataStructures on the iPhone

With `NSArray`, `NSDictionary`, `NSSet` and their subclasses, the [Foundation framework](http://developer.apple.com/mac/library/documentation/cocoa/Reference/Foundation/ObjC_classic/Intro/IntroFoundation.html) provides a number of basic collection classes. If you need more specialized or advanced collection data structures, there is a good chance that Quinn Taylor’s [CHDataStructures framework](http://cocoaheads.byu.edu/code/CHDataStructures) already has what you need. CHDataStructures is open source under a very liberal license and well-tested. It includes collection classes for different types of trees, specialized dictionaries and sets, linked lists, and many more.

I recently helped Quinn to make the CHDataStructures project iPhone-compatible. You can now grab the latest version from the repository and either build a static library to include in your iPhone projects or add the entire code to your project. The [readme file](http://dysart.cs.byu.edu/chsvn/CHDataStructures/README.html) includes detailed installation instructions.

Even though CHDataStructures included virtually no OS X-specific code, we had to tweak the build configuration to make it work on the iPhone as seamlessly as possible:

- Unfortunately, Apple does not support [frameworks](http://developer.apple.com/mac/library/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WhatAreFrameworks.html) (so useful!) or dynamic libraries on the iPhone, so we have to build a static libary (or include all the code directly in our iPhone projects). And since we are dealing with two different architectures (ARMv6 on the iPhone and i386 on the iPhone Simulator), we actually need to build different versions of the static library.
- [Unit Testing in Xcode](http://developer.apple.com/mac/library/DOCUMENTATION/DeveloperTools/Conceptual/UnitTesting/0-Introduction/introduction.html) means that the tests are run from a script during the build phase and test results show up in Xcode’s Build Results window. This is great if you are developing for the same platform your development system runs on, which is usually the case (or close enough) if you write OS X apps. If you develop for the iPhone, your build runs on an Intel machine but you want your unit tests run against the ARM architecture. To accomplish this, you need a separate iPhone unit testing app that installs on the device, runs all unit tests upon launch, outputs the results to the console, and quits. Apple has [a good how-to on this](http://developer.apple.com/iphone/library/documentation/Xcode/Conceptual/iphone_development/135-Unit_Testing_Applications/unit_testing_applications.html#//apple_ref/doc/uid/TP40007959-CH20-SW6).

I highly recommend CHDataStructures to anyone who needs more than the standard collection classes.
