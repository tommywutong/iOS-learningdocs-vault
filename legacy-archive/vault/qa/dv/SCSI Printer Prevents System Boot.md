---
title: SCSI Printer Prevents System Boot
apple_id: DTS10001153
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-10-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv12.html
archived_at: '2026-07-18T02:29:25.946355Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV12SCSI Printer Prevents System Boot |

|  |
| --- |
| ---   Q: Our printer uses SCSI as one of its interfaces and operates normally with all interfaces except SCSI. When the printer is connected to a PowerMac 7100 using the SCSI interface, the computer won't boot. If we turn the printer off, the Happy Mac shows up on the screen, and the Power Mac boots normally. How do we troubleshoot this problem?  A: The most likely causes are termination and bus-ID conflicts. If your device is using the same bus ID as some other SCSI device on the chain, it can prevent the boot sequence from preceding. This problem could also occur if your device has a permanent hard-wired terminator and there is another terminator on the bus.  There is one other possibility that relates to the Macintosh boot sequence. When the Mac bootstrap sees a device, it tries to read block zero. If your printer has a long warm-up period before it can fully respond to a read request, it may be stalling the bootstrap. You can check this by booting the Macintosh and waiting to see if the problem clears itself when the printer is fully initialized.  The best way to troubleshoot the problem is to use a SCSI-bus analyzer, so you can see the actual bootstrap sequence. |

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
