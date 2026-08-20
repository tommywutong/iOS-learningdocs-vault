---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/DirectoryService.html
archived_at: '2026-07-18T02:51:16.138342Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DirectoryService Changes for Swift

### DirectoryService

Removed tDataList.init(fDataNodeCount: UInt32, fDataListHead: tDataNodePtr)Added tDataList.init(fDataNodeCount: UInt32, fDataListHead: tDataNodePtr!)Modified tDataList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tDataList {     var fDataNodeCount: UInt32     var fDataListHead: tDataNodePtr     init()     init(fDataNodeCount fDataNodeCount: UInt32, fDataListHead fDataListHead: tDataNodePtr) } ``` |
| To | ``` struct tDataList {     var fDataNodeCount: UInt32     var fDataListHead: tDataNodePtr!     init()     init(fDataNodeCount fDataNodeCount: UInt32, fDataListHead fDataListHead: tDataNodePtr!) } ``` |

Modified tDataList.fDataListHead

|  | Declaration |
| --- | --- |
| From | ``` var fDataListHead: tDataNodePtr ``` |
| To | ``` var fDataListHead: tDataNodePtr! ``` |

Modified dsGetDataLength(_: UnsafePointer<tDataList>!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func dsGetDataLength(_ inDataList: UnsafePointer<tDataList>) -> UInt32 ``` |
| To | ``` func dsGetDataLength(_ inDataList: UnsafePointer<tDataList>!) -> UInt32 ``` |

Modified fpCustomAllocate

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomAllocate = (tDirReference, tClientData, UInt32, UnsafeMutablePointer<tBuffer>) -> tDirStatus ``` |
| To | ``` typealias fpCustomAllocate = (tDirReference, tClientData?, UInt32, UnsafeMutablePointer<tBuffer?>?) -> tDirStatus ``` |

Modified fpCustomDeAllocate

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomDeAllocate = (tDirReference, tClientData, tBuffer) -> tDirStatus ``` |
| To | ``` typealias fpCustomDeAllocate = (tDirReference, tClientData?, tBuffer?) -> tDirStatus ``` |

Modified fpCustomThreadBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadBlock = (tDirReference, tClientData) -> tDirStatus ``` |
| To | ``` typealias fpCustomThreadBlock = (tDirReference, tClientData?) -> tDirStatus ``` |

Modified fpCustomThreadUnBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadUnBlock = (tDirReference, tClientData) -> tDirStatus ``` |
| To | ``` typealias fpCustomThreadUnBlock = (tDirReference, tClientData?) -> tDirStatus ``` |

Modified fpCustomThreadYield

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadYield = (tDirReference, tClientData) -> tDirStatus ``` |
| To | ``` typealias fpCustomThreadYield = (tDirReference, tClientData?) -> tDirStatus ``` |

Modified tBuffer

|  | Declaration |
| --- | --- |
| From | ``` typealias tBuffer = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias tBuffer = UnsafeMutableRawPointer ``` |

Modified tClientData

|  | Declaration |
| --- | --- |
| From | ``` typealias tClientData = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias tClientData = UnsafeMutableRawPointer ``` |

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
