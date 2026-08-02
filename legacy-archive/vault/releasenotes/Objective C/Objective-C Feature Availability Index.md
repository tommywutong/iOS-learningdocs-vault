---
title: Objective-C Feature Availability Index
apple_id: TP40012243
resource_type: Release Note
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/ObjectiveC/ObjCAvailabilityIndex/index.html
archived_at: '2026-07-18T02:59:01.116867Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Objective-C Feature Availability Index

This article correlates features of the Objective-C language with the versions of Xcode and compiler you need to use them, and the OS versions you can use them with.

For more information about these modern Objective-C features, see _[Programming with Objective-C](../../documentation/Cocoa/Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_.

| Feature | Tools versions | OS X deployment | iOS deployment |
| --- | --- | --- | --- |
| Automatic Reference Counting (ARC) | Xcode 4.2  (LLVM Compiler 3.0) | Using modern runtime: Deploys back to OS X v10.7  Using legacy runtime: Deploys back to OS X v10.12 | Deploys back to iOS 5 |
| Automatic Reference Counting without zeroing weak reference (“ARCLite”) | Xcode 4.2  (LLVM Compiler 3.0) | Requires modern runtime  Deploys back to OS X v10.6 | Deploys back to iOS 4 |
| `@autoreleasepool` blocks | Xcode 4.2  (LLVM Compiler 3.0) | Using ARC: Requires modern runtime and deploys back to OS X v10.6  Using MRR: All releases | Using ARC: Deploys back to iOS 4  Using MRR: All releases |
| Default synthesis of `@property` instance variables and accessor methods | Xcode 4.4  (LLVM Compiler 4.0) | Requires modern runtime | Deploys back to iOS 4 |
| Instance variables in class extensions and `@implementation` block | Xcode 4.2  (LLVM Compiler 3.0) | Requires modern runtime | All iOS releases |
| No forward method prototypes needed in `@implementation` block | Xcode 4.3  (LLVM Compiler 3.1) | All releases | All iOS releases |
| `NSNumber`, `NSDictionary` and `NSArray` literals | Xcode 4.4  (LLVM Compiler 4.0) | All releases | All iOS releases |
| `@YES` and `@NO` literals | Xcode 4.4 and OS X 10.8 or later SDK  Xcode 4.5 and iOS 6.0 or later SDK  (LLVM Compiler 4.0) | All releases | All iOS releases |
| `NSDictionary` and `NSArray` subscripting | Xcode 4.4 and OS X 10.8 or later SDK  Xcode 4.5 and iOS 6.0 or later SDK  (LLVM Compiler 4.0) | Deploys back to OS X v10.6 | Deploys back to iOS 5 |

“Requires modern runtime” implies 64-bit systems.
