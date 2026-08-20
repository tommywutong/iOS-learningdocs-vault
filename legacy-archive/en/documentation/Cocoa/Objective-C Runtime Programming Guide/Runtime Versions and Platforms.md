---
title: Objective-C Runtime Programming Guide
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html
archived_at: '2026-07-15T07:17:29.408042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Objective-C Runtime Programming Guide](Introduction.md)


[Next](Interacting%20with%20the%20Runtime.md)[Previous](Introduction.md)

# Runtime Versions and Platforms

There are different versions of the Objective-C runtime on different platforms.

There are two versions of the Objective-C runtime—“modern” and “legacy”. The modern version was introduced with Objective-C 2.0 and includes a number of new features. The programming interface for the legacy version of the runtime is described in _Objective-C 1 Runtime Reference_; the programming interface for the modern version of the runtime is described in _[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_.

The most notable new feature is that instance variables in the modern runtime are “non-fragile”:

- In the legacy runtime, if you change the layout of instance variables in a class, you must recompile classes that inherit from it.
- In the modern runtime, if you change the layout of instance variables in a class, you do not have to recompile classes that inherit from it.

In addition, the modern runtime supports instance variable synthesis for declared properties (see [Declared Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17) in _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_).

iPhone applications and 64-bit programs on OS X v10.5 and later use the modern version of the runtime.

Other programs (32-bit programs on OS X desktop) use the legacy version of the runtime.

[Next](Interacting%20with%20the%20Runtime.md)[Previous](Introduction.md)

