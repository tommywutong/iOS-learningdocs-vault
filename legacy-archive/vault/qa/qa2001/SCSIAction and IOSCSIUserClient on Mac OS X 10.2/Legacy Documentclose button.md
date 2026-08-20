---
title: SCSIAction and IOSCSIUserClient on Mac OS X 10.2
apple_id: DTS10001726
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-09-13'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1201.html
archived_at: '2026-07-18T02:38:17.829311Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A QA1201SCSIAction and IOSCSIUserClient on Mac OS X 10.2 |

|  |
| --- |
| ---   Q: My application communicates with SCSI Parallel devices like scanners or printers using the `SCSIAction` or `IOSCSIUserClient` APIs. This worked on all versions of Mac OS X prior to 10.2. On Mac OS X 10.2, when I call `SCSIAction` I get an `opWrErr` (-49). Or, if I call `IOSCSIDeviceInterface->open` I get a `kIOReturnExclusiveAccess` error (0xE00002C5 or -536870203). Why does this no longer work?  A: `IOSCSIUserClient` and `SCSIAction` are deprecated APIs in Mac OS X 10.2. The intention was for these APIs to continue functioning as on earlier releases until users installed SCSI HBA drivers written to the new `IOSCSIParallelFamily` that shipped in Mac OS X 10.2. These APIs were inadvertently disabled and have been restored in Mac OS X 10.2.1 (rr. 3006423, 3026125). Until then, calling `open` on an `IOSCSIDeviceInterface` will return `kIOReturnExclusiveAccess`. `SCSIAction` internally calls that same function and maps the I/O Kit error `kIOReturnExclusiveAccess` to the `OSErr opWrErr`.  `SCSITaskUserClient` is the API that replaces `IOSCSIUserClient` and `SCSIAction`. Apple recommends that developers wishing the greatest backward compatibility use both `SCSITaskUserClient` and `SCSIAction/IOSCSIUserClient` to discover their device, then use the API which found the device to communicate with it.   ---  [Sep 13 2002] |

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
