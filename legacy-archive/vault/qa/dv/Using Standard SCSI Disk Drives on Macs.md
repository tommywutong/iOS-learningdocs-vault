---
title: Using Standard SCSI Disk Drives on Macs
apple_id: DTS10001157
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv16.html
archived_at: '2026-07-18T02:29:26.122221Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV16Using Standard SCSI Disk Drives on Macs |

|  |
| --- |
| ---   Q: At one time, we were told the we could not use a standard SCSI drive, because Apple didn't follow the SCSI standard. Since then, we heard that, at some point, Apple conformed to the SCSI standard.  Which Macintosh models can use standard SCSI hard drives, and are there any remaining issues related to using SCSI drives that are not specifically manufactured for use in a Mac?  A: It's not accurate to say Apple didn't follow the SCSI Standard. What actually happened was that the SCSI standard didn't really exist when some of the early operating-system decisions were made.  The only issue related to using standard SCSI drives on Apple machines was that bootstraps on machines earlier than the Mac IIci would not boot if a SCSI device responded to the first I/O request after power up with "Check Condition" (Request Sense returned "Unit Attention"). The bootstrap assumed that the device failed and it issued bus reset and try again (and, of course, fail again).  Drives not specifically manufactured for the Apple market should work, but may not offer optimal performance. The major issue here is "blind" transfers. The SCSI data-transfer phase uses an interlocked REQ/ACK handshake to move bytes between the initiator and target. Many low-cost Mac models had no DMA hardware, so all handshaking was done in software. To improve performance, the Mac SCSI Manager implemented an optional "blind" transfer that performed a full REQ/ACK synchronization at some defined boundary (for example, at every 512-byte block) but then did partial synchronization within blocks. This presumed that the device could move data across the bus with no more than a 16-microsecond latency between bytes. The device driver must specifically select "blind" transfers, and it must provide a transfer vector (TIB) that defines synchronization points. If your device stalls at unpredictable points (many magnetic-optical and DAT devices do this), you cannot specify blind transfers. This is discussed further in ___Inside Macintosh: Devices___.  For more information, see also:[Technote DV 14 on SCSI Bugs](https://developer.apple.com/library/archive/technotes/dv/dv_14.html). |

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
