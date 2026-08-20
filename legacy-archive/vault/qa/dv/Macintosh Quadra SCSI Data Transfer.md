---
title: Macintosh Quadra SCSI Data Transfer
apple_id: DTS10001151
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv10.html
archived_at: '2026-07-18T02:29:25.836119Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV10Macintosh Quadra SCSI Data Transfer |

|  |
| --- |
| ---   Q: My app is having trouble with Macintosh Quadra SCSI data transfers. It appears to be related to the SCSI-chip in the particular machine. Is there a `Gestalt` definition for the SCSI-chip?  A: To determine which SCSI chip is present, examine the 6th, 7th, and 21st bits of the `gestaltHardwareAttr` selector. To investigate hardware-dependent bit values, use the `Gestalt` DA, which is on the Developer CD.  Make sure your software doesn't read or write to the SCSI hardware directly. For example, the Quadra utilizes the 53C96, so it won't correctly interpret or queue a `SCSIstat` call. With the 53C96, you don't have access to the state of the SCSI bus lines. In implementation, the 53C96 is more abstract than the 53C80, and software no longer has access to the physical layers of the chip's instruction set. Your software should allow the SCSI Manager to handle the 53C96 chip/software interaction. |

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
