---
title: Blocks Programming Topics
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html
archived_at: '2026-07-15T07:11:18.878804Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Getting%20Started%20with%20Blocks.md)

# Introduction

Block objects are a C-level syntactic and runtime feature. They are similar to standard C functions, but in addition to executable code they may also contain variable bindings to automatic (stack) or managed (heap) memory. A block can therefore maintain a set of state (data) that it can use to impact behavior when executed.

You can use blocks to compose function expressions that can be passed to API, optionally stored, and used by multiple threads. Blocks are particularly useful as a callback because the block carries both the code to be executed on callback and the data needed during that execution.

Blocks are available in GCC and [Clang](http://clang.llvm.org/) as shipped with the OS X v10.6 Xcode developer tools. You can use blocks with OS X v10.6 and later, and iOS 4.0 and later. The blocks runtime is open source and can be found in [LLVM’s compiler-rt subproject repository](http://llvm.org/svn/llvm-project/compiler-rt/trunk/). Blocks have also been presented to the C standards working group as [N1370: Apple’s Extensions to C](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1370.pdf). As Objective-C and C++ are both derived from C, blocks are designed to work with all three languages (as well as Objective-C++). The syntax reflects this goal.

You should read this document to learn what block objects are and how you can use them from C, C++, or Objective-C.

This document contains the following chapters:

- [Getting Started with Blocks](Getting%20Started%20with%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnznknltc) provides a quick, practical, introduction to blocks.
- [Conceptual Overview](Conceptual%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqmznknltc) provides a conceptual introduction to blocks.
- [Declaring and Creating Blocks](Declaring%20and%20Creating%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnbnknltc) shows you how to declare block variables and how to implement blocks.
- [Blocks and Variables](Blocks%20and%20Variables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltc) describes the interaction between blocks and variables, and defines the `__block` storage type modifier.
- [Using Blocks](Using%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnjnknltc) illustrates various usage patterns.

[Next](Getting%20Started%20with%20Blocks.md)

