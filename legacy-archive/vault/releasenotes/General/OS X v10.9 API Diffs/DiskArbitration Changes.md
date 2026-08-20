---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/DiskArbitration.html
archived_at: '2026-07-18T02:54:12.216405Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# DiskArbitration Changes

## DiskArbitration

DiskArbitration.hModified [DARegisterDiskEjectApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492715-daregisterdiskejectapprovalcallb)

|  | Declaration |
| --- | --- |
| From | void DARegisterDiskEjectApprovalCallback ( DAApprovalSessionRef session, CFDictionaryRef match, DADiskEjectApprovalCallback callback, void \*context); |
| To | void DARegisterDiskEjectApprovalCallback ( DASessionRef session, CFDictionaryRef match, DADiskEjectApprovalCallback callback, void \*context); |

Modified [DARegisterDiskMountApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492762-daregisterdiskmountapprovalcallb)

|  | Declaration |
| --- | --- |
| From | void DARegisterDiskMountApprovalCallback ( DAApprovalSessionRef session, CFDictionaryRef match, DADiskMountApprovalCallback callback, void \*context); |
| To | void DARegisterDiskMountApprovalCallback ( DASessionRef session, CFDictionaryRef match, DADiskMountApprovalCallback callback, void \*context); |

Modified [DARegisterDiskUnmountApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492698-daregisterdiskunmountapprovalcal)

|  | Declaration |
| --- | --- |
| From | void DARegisterDiskUnmountApprovalCallback ( DAApprovalSessionRef session, CFDictionaryRef match, DADiskUnmountApprovalCallback callback, void \*context); |
| To | void DARegisterDiskUnmountApprovalCallback ( DASessionRef session, CFDictionaryRef match, DADiskUnmountApprovalCallback callback, void \*context); |

Modified [DAUnregisterApprovalCallback()](https://developer.apple.com/documentation/diskarbitration/1492750-daunregisterapprovalcallback)

|  | Declaration |
| --- | --- |
| From | void DAUnregisterApprovalCallback ( DAApprovalSessionRef session, void \*callback, void \*context); |
| To | void DAUnregisterApprovalCallback ( DASessionRef session, void \*callback, void \*context); |

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
