---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/libkern.html
archived_at: '2026-07-18T02:52:46.413685Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# libkern Changes

## libkern

Modified OSBacktrace(UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func OSBacktrace(_ bt: UnsafePointer<UnsafePointer<()>>, _ maxAddrs: UInt32) -> UInt32 ``` |
| To | ``` func OSBacktrace(_ bt: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ maxAddrs: UInt32) -> UInt32 ``` |

Modified sys_cache_control(Int32, UnsafeMutablePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sys_cache_control(_ function: Int32, _ start: UnsafePointer<()>, _ len: UInt) -> Int32 ``` | OS X 10.10 |
| To | ``` func sys_cache_control(_ function: Int32, _ start: UnsafeMutablePointer<Void>, _ len: Int) -> Int32 ``` | OS X 10.10.3 |

Modified sys_dcache_flush(UnsafeMutablePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sys_dcache_flush(_ start: UnsafePointer<()>, _ len: UInt) ``` | OS X 10.10 |
| To | ``` func sys_dcache_flush(_ start: UnsafeMutablePointer<Void>, _ len: Int) ``` | OS X 10.5 |

Modified sys_icache_invalidate(UnsafeMutablePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sys_icache_invalidate(_ start: UnsafePointer<()>, _ len: UInt) ``` | OS X 10.10 |
| To | ``` func sys_icache_invalidate(_ start: UnsafeMutablePointer<Void>, _ len: Int) ``` | OS X 10.10.3 |

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
