---
title: Determining Whether a Device Supports Asynchronous I/O
apple_id: DTS10001146
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv05.html
archived_at: '2026-07-18T02:29:25.521196Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV05Determining Whether a Device Supports Asynchronous I/O |

|  |  |
| --- | --- |
| ---   Q: How can we determine whether a device supports asynchronous I/O?  A: The best way to determine if a SCSI device supports asynchronous I/O is to use `Gestalt`. Check the `gestaltSCSI` selector to see if the `gestaltAsyncSCSI` bit is set, as shown below:   |  | | --- | | ``` #include <Gestalt.h> Boolean CanDoAsyncSCSI(void) {   long response;   OSErr err;   err = Gestalt(gestaltSCSI, &response);   if (err) return false;   return (response & (1 << gestaltAsyncSCSI) ); } ``` |    There is no Gestalt test currently available for non-SCSI devices. You can assume that asynchronous calls to a driver will be handled correctly. If the driver is actually asynchronous, your completion routine is called when the I/O is finished. If the driver is not asynchronous, the driver returns and calls your completion routine when the I/O is finished.  For more information, see the __SCSI Manager 4.3 chapter of _Inside Macintosh:Devices___ and __"Asynchronous routines on the Macintosh" in issue 13 of Develop__. |

#### [Jul 01 1995]

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

---
