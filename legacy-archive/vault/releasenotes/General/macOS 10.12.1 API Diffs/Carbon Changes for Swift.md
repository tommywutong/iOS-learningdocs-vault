---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/Carbon.html
archived_at: '2026-07-18T02:51:44.704115Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# Carbon Changes for Swift

### Carbon

Modified ContextualMenuInterfaceStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ContextualMenuInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!     var AddRef: ((UnsafeMutableRawPointer?) -> UInt32)!     var Release: ((UnsafeMutableRawPointer?) -> UInt32)!     var ExamineContext: ((UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!     var HandleSelection: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!     var PostMenuCleanup: ((UnsafeMutableRawPointer?) -> Swift.Void)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> UInt32)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> UInt32)!, ExamineContext ExamineContext: (@escaping (UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!, HandleSelection HandleSelection: (@escaping (UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!, PostMenuCleanup PostMenuCleanup: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!) } ``` |
| To | ``` struct ContextualMenuInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!     var AddRef: ((UnsafeMutableRawPointer?) -> UInt32)!     var Release: ((UnsafeMutableRawPointer?) -> UInt32)!     var ExamineContext: ((UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!     var HandleSelection: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!     var PostMenuCleanup: ((UnsafeMutableRawPointer?) -> Swift.Void)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> UInt32)!, Release Release: ((UnsafeMutableRawPointer?) -> UInt32)!, ExamineContext ExamineContext: ((UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!, HandleSelection HandleSelection: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!, PostMenuCleanup PostMenuCleanup: ((UnsafeMutableRawPointer?) -> Swift.Void)!) } ``` |

Modified ContextualMenuInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ((UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!, AddRef: ((UnsafeMutableRawPointer?) -> UInt32)!, Release: ((UnsafeMutableRawPointer?) -> UInt32)!, ExamineContext: ((UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!, HandleSelection: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!, PostMenuCleanup: ((UnsafeMutableRawPointer?) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> UInt32)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> UInt32)!, ExamineContext ExamineContext: (@escaping (UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!, HandleSelection HandleSelection: (@escaping (UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!, PostMenuCleanup PostMenuCleanup: (@escaping (UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |
| To | ``` init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: ((UnsafeMutableRawPointer?, CFUUIDBytes, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32)!, AddRef AddRef: ((UnsafeMutableRawPointer?) -> UInt32)!, Release Release: ((UnsafeMutableRawPointer?) -> UInt32)!, ExamineContext ExamineContext: ((UnsafeMutableRawPointer?, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDescList>?) -> OSStatus)!, HandleSelection HandleSelection: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<AEDesc>?, Int32) -> OSStatus)!, PostMenuCleanup PostMenuCleanup: ((UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
