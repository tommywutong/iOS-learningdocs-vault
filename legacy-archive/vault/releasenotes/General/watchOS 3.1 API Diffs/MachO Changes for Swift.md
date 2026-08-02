---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/MachO.html
archived_at: '2026-07-18T02:58:38.672168Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# MachO Changes for Swift

### MachO

Modified NSLinkEditErrorHandlers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLinkEditErrorHandlers {     var undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!     var multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!     var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!     init()     init(undefined undefined: (@escaping (UnsafePointer<Int8>?) -> Swift.Void)!, multiple multiple: (@escaping (NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit linkEdit: (@escaping (NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!) } ``` |
| To | ``` struct NSLinkEditErrorHandlers {     var undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!     var multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!     var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!     init()     init(undefined undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!, multiple multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!) } ``` |

Modified NSLinkEditErrorHandlers.init(undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!, multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(undefined undefined: (@escaping (UnsafePointer<Int8>?) -> Swift.Void)!, multiple multiple: (@escaping (NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit linkEdit: (@escaping (NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!) ``` |
| To | ``` init(undefined undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!, multiple multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!) ``` |

Modified tlv_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tlv_descriptor {     var thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!     var key: UInt     var offset: UInt     init()     init(thunk thunk: (@escaping (UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key key: UInt, offset offset: UInt) } ``` |
| To | ``` struct tlv_descriptor {     var thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!     var key: UInt     var offset: UInt     init()     init(thunk thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key key: UInt, offset offset: UInt) } ``` |

Modified tlv_descriptor.init(thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key: UInt, offset: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(thunk thunk: (@escaping (UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key key: UInt, offset offset: UInt) ``` |
| To | ``` init(thunk thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key key: UInt, offset offset: UInt) ``` |

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
