---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/DiskArbitration.html
archived_at: '2026-07-18T02:51:45.759456Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# DiskArbitration Changes for Swift

### DiskArbitration

Modified [DARegisterDiskAppearedCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskAppearedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492707-daregisterdiskappearedcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskAppearedCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskAppearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: @escaping DiskArbitration.DADiskAppearedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskDescriptionChangedCallback(_: DASession, _: CFDictionary?, _: CFArray?, _: DiskArbitration.DADiskDescriptionChangedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492705-daregisterdiskdescriptionchanged)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession, _ match: CFDictionary?, _ watch: CFArray?, _ callback: DiskArbitration.DADiskDescriptionChangedCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskDescriptionChangedCallback(_ session: DASession, _ match: CFDictionary?, _ watch: CFArray?, _ callback: @escaping DiskArbitration.DADiskDescriptionChangedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskDisappearedCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskDisappearedCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492696-daregisterdiskdisappearedcallbac)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskDisappearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskDisappearedCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskDisappearedCallback(_ session: DASession, _ match: CFDictionary?, _ callback: @escaping DiskArbitration.DADiskDisappearedCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskEjectApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskEjectApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskEjectApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskEjectApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: @escaping DiskArbitration.DADiskEjectApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskMountApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskMountApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskMountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskMountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: @escaping DiskArbitration.DADiskMountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskPeekCallback(_: DASession, _: CFDictionary?, _: CFIndex, _: DiskArbitration.DADiskPeekCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492728-daregisterdiskpeekcallback)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: DiskArbitration.DADiskPeekCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskPeekCallback(_ session: DASession, _ match: CFDictionary?, _ order: CFIndex, _ callback: @escaping DiskArbitration.DADiskPeekCallback, _ context: UnsafeMutableRawPointer?) ``` |

Modified [DARegisterDiskUnmountApprovalCallback(_: DASession, _: CFDictionary?, _: DiskArbitration.DADiskUnmountApprovalCallback, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal)

|  | Declaration |
| --- | --- |
| From | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: DiskArbitration.DADiskUnmountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |
| To | ``` func DARegisterDiskUnmountApprovalCallback(_ session: DASession, _ match: CFDictionary?, _ callback: @escaping DiskArbitration.DADiskUnmountApprovalCallback, _ context: UnsafeMutableRawPointer?) ``` |

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
