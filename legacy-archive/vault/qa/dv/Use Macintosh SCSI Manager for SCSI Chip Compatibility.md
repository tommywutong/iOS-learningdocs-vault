---
title: Use Macintosh SCSI Manager for SCSI Chip Compatibility
apple_id: DTS10001156
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv15.html
archived_at: '2026-07-18T02:29:26.065304Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)

|  |
| --- |
| Technical Q&A DV15Use Macintosh SCSI Manager for SCSI Chip Compatibility |

|  |
| --- |
| ---   Q: Our SCSI driver asserts the SCSI bus protocol directly (per the SCSI bus specs), using the low-memory global `SCSIBase` as the SCSI base address. Our code works properly on systems using the NCR 5380, but it hangs with the SCSI NCR 53C96. Should I add a NOP somewhere because the 53C96 is faster?  A: Although `SCSIBase` is exactly where a SCSI device driver should look to find the base address of a SCSI chip in the Macintosh, the NCR 53C96 is physically different from the NCR 5380. In addition to having its registers in different locations of the address map and a slightly different register set, the chip takes on much more of the burden (and control) of accessing the SCSI bus. The major difference is that, with the 5380, the chip controller (`drvr`) needs to actively respond to the phases of the SCSI bus as the target changes them, and it has to be ready to correctly react to any unexpected changes in state. For continued compatibility with the Macintosh product lines, your driver must use the SCSI Manager rather than write directly to the chip. With 5396, the chip controller needs to set up all information for the entire command sequence (Arbitration through Message In) and then tell the chip to execute it. The "controller" is not in direct control of the SCSI bus. With the 5380, the Target is always in control -- not your driver, but the 5380's interaction model gives the _impression_ that your driver is in control.  Your best course of action is to ensure your SCSI driver uses the SCSI Manager so that it automatically works on all Macintosh platforms in case Apple changes chips again in the future. If there is something odd about your SCSI device that cannot be accommodated by the SCSI Manager (this is rare), you should get the documentation for the NCR 5396 from NCR and rewrite your driver to use this new "setup and go" interaction model. |

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
