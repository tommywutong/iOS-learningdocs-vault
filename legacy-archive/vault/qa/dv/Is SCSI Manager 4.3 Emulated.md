---
title: Is SCSI Manager 4.3 Emulated?
apple_id: DTS10001148
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-04-05'
source_url: https://developer.apple.com/library/archive/qa/dv/dv07.html
archived_at: '2026-07-18T02:29:25.649863Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV07Is SCSI Manager 4.3 Emulated? |

|  |
| --- |
| ---   Q: Is the new SCSI Manager 4.3 emulated?  A: SCSI Manager 4.3 was originally released as 68K code simply because its release vehicle was the ROM in the Macintosh Quadra 840av and 660av, both of which used 68040 processors. It remained in 68K code, emulated when run on PowerPC-based computers, until the release of the first PCI Power Macintosh computers, which had a native version of SCSI Manager 4.3 in ROM. The situation changed again starting with [System 7.5.3](https://developer.apple.com/library/archive/technotes/tn/tn1017.html#RTFToC36), which installs native SCSI Manager 4.3 on all PowerPC-based computers with the appropriate hardware.  In summary, SCSI Manager 4.3 is running native on System 7.5.3 and later. |

#### [Apr 05 1995]

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
