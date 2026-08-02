---
title: SCSI Calls Translated for IDE Devices
apple_id: DTS10001143
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv02.html
archived_at: '2026-07-18T02:29:25.420896Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Storage](https://developer.apple.com/referencelibrary/HardwareDrivers/idxMassStorageDevices-date.html)

|  |
| --- |
| Technical Q&A DV02SCSI Calls Translated for IDE Devices |

|  |
| --- |
| ---   Q: My application makes various SCSI calls to obtain information about devices attached to the SCSI bus. Since I also need to support the new IDE drives that are in some Macintosh models, I need to know if SCSI calls are automatically translated for IDE devices or if there is a new API for these drives. Where can I get more information about Apple's use of IDE drives?  A: IDE is an industry standard. For information on the standard and a full description of the ATA Manager, see ANSI specification number X3T9/0948D, revision 2, which can be ordered from Global Engineering at:  Phone: 800-854-7179  Fax: 303-792-2192  Although it is not documented, the ATA Manager does support the 'Identify Drive Command', which returns the IDE drive model and serial numbers (if the drive manufacturer supports this).  Developer CD, March 95 (Reference Library)   Technical Documentation  Developer Notes  Mac LC 630 & Quadra 630  (Chapter 6) Software for the IDE Hard Disk |

#### [May 01 1999]

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
