---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/libkern.html
archived_at: '2026-07-18T02:51:42.021856Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# libkern Changes for Swift

### libkern

Modified OSBacktrace(_: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UInt32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func OSBacktrace(_ bt: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ maxAddrs: UInt32) -> UInt32 ``` |
| To | ``` func OSBacktrace(_ bt: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ maxAddrs: UInt32) -> UInt32 ``` |

Modified sys_cache_control(_: Int32, _: UnsafeMutableRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sys_cache_control(_ function: Int32, _ start: UnsafeMutablePointer<Void>, _ len: Int) -> Int32 ``` |
| To | ``` func sys_cache_control(_ function: Int32, _ start: UnsafeMutableRawPointer!, _ len: Int) -> Int32 ``` |

Modified sys_dcache_flush(_: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func sys_dcache_flush(_ start: UnsafeMutablePointer<Void>, _ len: Int) ``` |
| To | ``` func sys_dcache_flush(_ start: UnsafeMutableRawPointer!, _ len: Int) ``` |

Modified sys_icache_invalidate(_: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func sys_icache_invalidate(_ start: UnsafeMutablePointer<Void>, _ len: Int) ``` |
| To | ``` func sys_icache_invalidate(_ start: UnsafeMutableRawPointer!, _ len: Int) ``` |

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
