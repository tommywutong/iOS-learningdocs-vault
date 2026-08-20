---
title: Objective-C Runtime Programming Guide
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:17:29.414322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Runtime%20Versions%20and%20Platforms.md)

# Introduction

The Objective-C language defers as many decisions as it can from compile time and link time to runtime. Whenever possible, it does things dynamically. This means that the language requires not just a compiler, but also a runtime system to execute the compiled code. The runtime system acts as a kind of operating system for the Objective-C language; it’s what makes the language work.

This document looks at the `NSObject` class and how Objective-C programs interact with the runtime system. In particular, it examines the paradigms for dynamically loading new classes at runtime, and forwarding messages to other objects. It also provides information about how you can find information about objects while your program is running.

You should read this document to gain an understanding of how the Objective-C runtime system works and how you can take advantage of it. Typically, though, there should be little reason for you to need to know and understand this material to write a Cocoa application.

This document has the following chapters:

- [Runtime Versions and Platforms](Runtime%20Versions%20and%20Platforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgywvgvzr)
- [Interacting with the Runtime](Interacting%20with%20the%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgmwvgvzr)
- [Messaging](Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgqwvgvzr)
- [Dynamic Method Resolution](Dynamic%20Method%20Resolution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgiwvgvzr)
- [Message Forwarding](Message%20Forwarding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwvgvzr)
- [Type Encodings](Type%20Encodings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgawvgvzr)
- [Declared Properties](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqgewvgvzr)

_[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ describes the data structures and functions of the Objective-C runtime support library. Your programs can use these interfaces to interact with the Objective-C runtime system. For example, you can add classes or methods, or obtain a list of all class definitions for loaded classes.

_[Programming with Objective-C](../Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_ describes the Objective-C language.

_[Objective-C Release Notes](https://developer.apple.com/library/archive/releasenotes/Cocoa/RN-ObjectiveC/index.html#//apple_ref/doc/uid/TP40004309)_ describes some of the changes in the Objective-C runtime in recent releases of OS X.

[Next](Runtime%20Versions%20and%20Platforms.md)

