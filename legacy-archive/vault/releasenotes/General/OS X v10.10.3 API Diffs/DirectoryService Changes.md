---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DirectoryService.html
archived_at: '2026-07-18T02:52:22.485453Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DirectoryService Changes

## DirectoryService

Added tAccessControlEntry.init()Added tAccessControlEntry.init(fGuestAccessFlags: UInt32, fDirMemberFlags: UInt32, fDirNodeMemberFlags: UInt32, fOwnerFlags: UInt32, fAdministratorFlags: UInt32)Added tAttributeEntry.init()Added tAttributeEntry.init(fReserved1: UInt32, fReserved2: tAccessControlEntry, fAttributeValueCount: UInt32, fAttributeDataSize: UInt32, fAttributeValueMaxSize: UInt32, fAttributeSignature: tDataNode)Added tAttributeValueEntry.init()Added tAttributeValueEntry.init(fAttributeValueID: UInt32, fAttributeValueData: tDataNode)Added tDataBuffer.init()Added tDataBuffer.init(fBufferSize: UInt32, fBufferLength: UInt32, fBufferData:(Int8))Added tDataList.init()Added tDataList.init(fDataNodeCount: UInt32, fDataListHead: tDataNodePtr)Added tRecordEntry.init()Added tRecordEntry.init(fReserved1: UInt32, fReserved2: tAccessControlEntry, fRecordAttributeCount: UInt32, fRecordNameAndType: tDataNode)Modified tAccessControlEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tAccessControlEntry {     var fGuestAccessFlags: UInt32     var fDirMemberFlags: UInt32     var fDirNodeMemberFlags: UInt32     var fOwnerFlags: UInt32     var fAdministratorFlags: UInt32 } ``` |
| To | ``` struct tAccessControlEntry {     var fGuestAccessFlags: UInt32     var fDirMemberFlags: UInt32     var fDirNodeMemberFlags: UInt32     var fOwnerFlags: UInt32     var fAdministratorFlags: UInt32     init()     init(fGuestAccessFlags fGuestAccessFlags: UInt32, fDirMemberFlags fDirMemberFlags: UInt32, fDirNodeMemberFlags fDirNodeMemberFlags: UInt32, fOwnerFlags fOwnerFlags: UInt32, fAdministratorFlags fAdministratorFlags: UInt32) } ``` |

Modified tAttributeEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tAttributeEntry {     var fReserved1: UInt32     var fReserved2: tAccessControlEntry     var fAttributeValueCount: UInt32     var fAttributeDataSize: UInt32     var fAttributeValueMaxSize: UInt32     var fAttributeSignature: tDataNode } ``` |
| To | ``` struct tAttributeEntry {     var fReserved1: UInt32     var fReserved2: tAccessControlEntry     var fAttributeValueCount: UInt32     var fAttributeDataSize: UInt32     var fAttributeValueMaxSize: UInt32     var fAttributeSignature: tDataNode     init()     init(fReserved1 fReserved1: UInt32, fReserved2 fReserved2: tAccessControlEntry, fAttributeValueCount fAttributeValueCount: UInt32, fAttributeDataSize fAttributeDataSize: UInt32, fAttributeValueMaxSize fAttributeValueMaxSize: UInt32, fAttributeSignature fAttributeSignature: tDataNode) } ``` |

Modified tAttributeValueEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tAttributeValueEntry {     var fAttributeValueID: UInt32     var fAttributeValueData: tDataNode } ``` |
| To | ``` struct tAttributeValueEntry {     var fAttributeValueID: UInt32     var fAttributeValueData: tDataNode     init()     init(fAttributeValueID fAttributeValueID: UInt32, fAttributeValueData fAttributeValueData: tDataNode) } ``` |

Modified tDataBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tDataBuffer {     var fBufferSize: UInt32     var fBufferLength: UInt32     var fBufferData: (Int8) } ``` |
| To | ``` struct tDataBuffer {     var fBufferSize: UInt32     var fBufferLength: UInt32     var fBufferData: (Int8)     init()     init(fBufferSize fBufferSize: UInt32, fBufferLength fBufferLength: UInt32, fBufferData fBufferData: (Int8)) } ``` |

Modified tDataList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tDataList {     var fDataNodeCount: UInt32     var fDataListHead: tDataNodePtr } ``` |
| To | ``` struct tDataList {     var fDataNodeCount: UInt32     var fDataListHead: tDataNodePtr     init()     init(fDataNodeCount fDataNodeCount: UInt32, fDataListHead fDataListHead: tDataNodePtr) } ``` |

Modified tRecordEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tRecordEntry {     var fReserved1: UInt32     var fReserved2: tAccessControlEntry     var fRecordAttributeCount: UInt32     var fRecordNameAndType: tDataNode } ``` |
| To | ``` struct tRecordEntry {     var fReserved1: UInt32     var fReserved2: tAccessControlEntry     var fRecordAttributeCount: UInt32     var fRecordNameAndType: tDataNode     init()     init(fReserved1 fReserved1: UInt32, fReserved2 fReserved2: tAccessControlEntry, fRecordAttributeCount fRecordAttributeCount: UInt32, fRecordNameAndType fRecordNameAndType: tDataNode) } ``` |

Modified dsGetDataLength(UnsafePointer<tDataList>) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func dsGetDataLength(_ inDataList: ConstUnsafePointer<tDataList>) -> UInt32 ``` |
| To | ``` func dsGetDataLength(_ inDataList: UnsafePointer<tDataList>) -> UInt32 ``` |

Modified fpCustomAllocate

|  | Declaration |
| --- | --- |
| From | ``` typealias fpCustomAllocate = CFunctionPointer<((tDirReference, tClientData, UInt32, UnsafePointer<tBuffer>) -> tDirStatus)> ``` |
| To | ``` typealias fpCustomAllocate = CFunctionPointer<((tDirReference, tClientData, UInt32, UnsafeMutablePointer<tBuffer>) -> tDirStatus)> ``` |

Modified tAccessControlEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tAccessControlEntryPtr = UnsafePointer<tAccessControlEntry> ``` |
| To | ``` typealias tAccessControlEntryPtr = UnsafeMutablePointer<tAccessControlEntry> ``` |

Modified tAttributeEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tAttributeEntryPtr = UnsafePointer<tAttributeEntry> ``` |
| To | ``` typealias tAttributeEntryPtr = UnsafeMutablePointer<tAttributeEntry> ``` |

Modified tAttributeValueEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tAttributeValueEntryPtr = UnsafePointer<tAttributeValueEntry> ``` |
| To | ``` typealias tAttributeValueEntryPtr = UnsafeMutablePointer<tAttributeValueEntry> ``` |

Modified tBuffer

|  | Declaration |
| --- | --- |
| From | ``` typealias tBuffer = UnsafePointer<()> ``` |
| To | ``` typealias tBuffer = UnsafeMutablePointer<Void> ``` |

Modified tClientData

|  | Declaration |
| --- | --- |
| From | ``` typealias tClientData = UnsafePointer<()> ``` |
| To | ``` typealias tClientData = UnsafeMutablePointer<Void> ``` |

Modified tDataBufferPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tDataBufferPtr = UnsafePointer<tDataBuffer> ``` |
| To | ``` typealias tDataBufferPtr = UnsafeMutablePointer<tDataBuffer> ``` |

Modified tDataListPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tDataListPtr = UnsafePointer<tDataList> ``` |
| To | ``` typealias tDataListPtr = UnsafeMutablePointer<tDataList> ``` |

Modified tDataNodePtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tDataNodePtr = UnsafePointer<tDataNode> ``` |
| To | ``` typealias tDataNodePtr = UnsafeMutablePointer<tDataNode> ``` |

Modified tRecordEntryPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias tRecordEntryPtr = UnsafePointer<tRecordEntry> ``` |
| To | ``` typealias tRecordEntryPtr = UnsafeMutablePointer<tRecordEntry> ``` |

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
