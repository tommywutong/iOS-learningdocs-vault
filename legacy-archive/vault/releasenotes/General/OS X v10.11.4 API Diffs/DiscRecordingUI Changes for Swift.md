---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/DiscRecordingUI.html
archived_at: '2026-07-18T02:53:51.311922Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# DiscRecordingUI Changes for Swift

### DiscRecordingUI

Modified DRBurnSession

|  | Name | Declaration |
| --- | --- | --- |
| From | DRBurnSessionRef | ``` typealias DRBurnSessionRef = DRBurnSession ``` |
| To | DRBurnSession | ``` class DRBurnSession { } ``` |

Modified DREraseSession

|  | Name | Declaration |
| --- | --- | --- |
| From | DREraseSessionRef | ``` typealias DREraseSessionRef = DREraseSession ``` |
| To | DREraseSession | ``` class DREraseSession { } ``` |

Modified DRBurnSessionBurnCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionBurnCompleteProcPtr = (DRBurnSession!, DRBurn!) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionBurnCompleteProcPtr = (DRBurnSession!, DRBurnRef!) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceCheckProcPtr = (DRBurnSession!, DRDevice!) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionDeviceCheckProcPtr = (DRBurnSession!, DRDeviceRef!) -> DarwinBoolean ``` |

Modified DRBurnSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = (DRBurnSession!, DRDevice!) -> Void ``` |
| To | ``` typealias DRBurnSessionDeviceSelectionNotificationProcPtr = (DRBurnSession!, DRDeviceRef!) -> Void ``` |

Modified DRBurnSessionGetBurn(_: DRBurnSession!) -> Unmanaged<DRBurnRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnSessionGetBurn(_ burnSession: DRBurnSession!) -> Unmanaged<DRBurn>! ``` |
| To | ``` func DRBurnSessionGetBurn(_ burnSession: DRBurnSession!) -> Unmanaged<DRBurnRef>! ``` |

Modified DRBurnSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DRBurnSessionMediaCheckProcPtr = (DRBurnSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |
| To | ``` typealias DRBurnSessionMediaCheckProcPtr = (DRBurnSession!, DRDeviceRef!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |

Modified DRBurnSessionSetBurn(_: DRBurnSession!, _: DRBurnRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DRBurnSessionSetBurn(_ burnSession: DRBurnSession!, _ burn: DRBurn!) ``` |
| To | ``` func DRBurnSessionSetBurn(_ burnSession: DRBurnSession!, _ burn: DRBurnRef!) ``` |

Modified DREraseSessionDeviceCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceCheckProcPtr = (DREraseSession!, DRDevice!) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionDeviceCheckProcPtr = (DREraseSession!, DRDeviceRef!) -> DarwinBoolean ``` |

Modified DREraseSessionDeviceSelectionNotificationProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = (DREraseSession!, DRDevice!) -> Void ``` |
| To | ``` typealias DREraseSessionDeviceSelectionNotificationProcPtr = (DREraseSession!, DRDeviceRef!) -> Void ``` |

Modified DREraseSessionEraseCompleteProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionEraseCompleteProcPtr = (DREraseSession!, DRErase!) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionEraseCompleteProcPtr = (DREraseSession!, DREraseRef!) -> DarwinBoolean ``` |

Modified DREraseSessionGetErase(_: DREraseSession!) -> Unmanaged<DREraseRef>!

|  | Declaration |
| --- | --- |
| From | ``` func DREraseSessionGetErase(_ eraseSession: DREraseSession!) -> Unmanaged<DRErase>! ``` |
| To | ``` func DREraseSessionGetErase(_ eraseSession: DREraseSession!) -> Unmanaged<DREraseRef>! ``` |

Modified DREraseSessionMediaCheckProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DREraseSessionMediaCheckProcPtr = (DREraseSession!, DRDevice!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |
| To | ``` typealias DREraseSessionMediaCheckProcPtr = (DREraseSession!, DRDeviceRef!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> DarwinBoolean ``` |

Modified DREraseSessionSetErase(_: DREraseSession!, _: DREraseRef!)

|  | Declaration |
| --- | --- |
| From | ``` func DREraseSessionSetErase(_ eraseSession: DREraseSession!, _ erase: DRErase!) ``` |
| To | ``` func DREraseSessionSetErase(_ eraseSession: DREraseSession!, _ erase: DREraseRef!) ``` |

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
