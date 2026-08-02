---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DirectoryService.html
archived_at: '2026-07-18T02:53:31.336280Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DirectoryService Changes for Swift

### DirectoryService

Removed tDirPatternMatch.valueRemoved tDirStatus.valueAdded tDirPatternMatch.init(rawValue: UInt32)Added tDirPatternMatch.rawValueAdded tDirStatus.init(rawValue: Int32)Added tDirStatus.rawValueModified tDirPatternMatch [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct tDirPatternMatch {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct tDirPatternMatch : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified tDirStatus [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct tDirStatus {     init(_ value: Int32)     var value: Int32 } ``` | -- |
| To | ``` struct tDirStatus : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |

Modified fpCustomAllocate

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomAllocate = CFunctionPointer<((tDirReference, tClientData, UInt32, UnsafeMutablePointer<tBuffer>) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomAllocate = (tDirReference, tClientData, UInt32, UnsafeMutablePointer<tBuffer>) -> tDirStatus ``` |

Modified fpCustomDeAllocate

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomDeAllocate = CFunctionPointer<((tDirReference, tClientData, tBuffer) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomDeAllocate = (tDirReference, tClientData, tBuffer) -> tDirStatus ``` |

Modified fpCustomThreadBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadBlock = CFunctionPointer<((tDirReference, tClientData) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomThreadBlock = (tDirReference, tClientData) -> tDirStatus ``` |

Modified fpCustomThreadUnBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadUnBlock = CFunctionPointer<((tDirReference, tClientData) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomThreadUnBlock = (tDirReference, tClientData) -> tDirStatus ``` |

Modified fpCustomThreadYield

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomThreadYield = CFunctionPointer<((tDirReference, tClientData) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomThreadYield = (tDirReference, tClientData) -> tDirStatus ``` |

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
