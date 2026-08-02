---
title: Writing Native SCSI Disk Drivers for PowerMacs
apple_id: DTS10001163
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-03-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv22.html
archived_at: '2026-07-18T02:29:26.450431Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV22Writing Native SCSI Disk Drivers for PowerMacs |

|  |
| --- |
| ---   Q: Is there any information on writing native SCSI disk drivers for the PCI based PowerMacs? Particularly, what's the proper way of installing a native driver on a SCSI disk: is there a special partition type for a native driver, or should there be a standard SCSI disk driver that loads a PowerPC code fragment?  A: Apple doesn't support native SCSI drivers yet (this will be a Copland feature). You _can_ write a native SCSI Interface Module (SIM). Remember that a driver is the software that handles a particular SCSI device, while a SIM is responsible for SCSI controllers (e.g., PCI or NuBus cards).  Normally, SCSI 4.3 drivers are loaded off the Apple_Driver43 partition, and SIMs are typically loaded from the disk controller firmware (PCI card). If you want to load a native SIM off of the disk, you will have to encapsulate the code fragments, and read and link them in from your standard 68K driver.See _Inside Macintosh: Devices_, chapter 4, for more information on loading SCSI drivers. |

#### [Nov 01 1995]

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
