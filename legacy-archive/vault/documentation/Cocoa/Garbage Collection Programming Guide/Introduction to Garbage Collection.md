---
title: Garbage Collection Programming Guide
apple_id: TP40002431
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/GarbageCollection/Introduction.html
archived_at: '2026-07-15T07:16:01.018836Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Garbage%20Collection%20for%20Cocoa%20Essentials.md)

# Introduction to Garbage Collection

In OS X, you can write programs that make use of an automatic memory management system commonly known as “garbage collection.” (Garbage collection is not available in iOS.) Garbage collection coexists with the traditional system of memory management (that uses manual reference counting using `retain`, `release`, and autorelease pools)—herein referred to as “manually reference counted”—and is hence an opt-in system.

These documents describe the complete garbage collection system provided for Cocoa, the functionality provided, and some of the issues that arise if you adopt this technology.

If you are developing applications using Cocoa, you should read at least [Garbage Collection for Cocoa Essentials](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvomi) to gain an understanding of the garbage collection system. It is strongly recommended that you also read [Adopting Garbage Collection](Adopting%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjxfvjvomi) and [Implementing a finalize Method](Implementing%20a%20finalize%20Method.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjtfvjvomi). You are expected to already understand the Objective-C language (see _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_) and to have some familiarity with Cocoa.

The following articles explain the problems the garbage collection system addresses, the solutions it provides, its basic functionality, and common tasks you might perform:

- [Garbage Collection for Cocoa Essentials](Garbage%20Collection%20for%20Cocoa%20Essentials.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjsfvjvomi) describes the essential details of the garbage collection system for Cocoa. At a minimum, you should read this article.
- [Adopting Garbage Collection](Adopting%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjxfvjvomi) describes issues related to adopting garbage collection.
- [Architecture](Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjrfvjvomi) describes the design goals and architecture of the technology, and the benefits you get from using it.
- [Using Garbage Collection](Using%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dambwfvjvomi) describes some of the features you can take advantage of when you use garbage collection, and some of subtleties you need to be aware of.
- [Implementing a finalize Method](Implementing%20a%20finalize%20Method.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinjtfvjvomi) describes how to correctly implement a `finalize` method.
- [Inapplicable Patterns](Inapplicable%20Patterns.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3donrsfvjvomi) describes Cocoa programming patterns that are not applicable to garbage collection.
- [Using Core Foundation with Garbage Collection](Using%20Core%20Foundation%20with%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmobxfvjvomi) describes how to use Core Foundation objects with garbage collection.
- [Garbage Collection API](Garbage%20Collection%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinrxfvjvomi) provides a summary of API used in garbage collection.

The following documents provide information about related aspects of Cocoa and the Objective-C language.

- _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ describes object-oriented programming and describes the Objective-C programming language.
- _[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ describes the data structures and functions of the Objective-C runtime support library.
- _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_ provides information adopting Automatic Reference Counting.
[Next](Garbage%20Collection%20for%20Cocoa%20Essentials.md)

