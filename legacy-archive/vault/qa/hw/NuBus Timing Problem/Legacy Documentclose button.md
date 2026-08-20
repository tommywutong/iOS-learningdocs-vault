---
title: NuBus Timing Problem
apple_id: DTS10001273
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/hw/hw03.html
archived_at: '2026-07-18T02:29:35.302622Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A HW03NuBus Timing Problem |

|  |
| --- |
| ---   Q: We developed a NuBus card using the Texas Instruments chip set (74ACT2440 and 74BBCT2420) that performs DMA-in and DMA-out. With the card installed in a Quadra 840AV, the Macintosh gets stuck in a DMA-out and needs to be rebooted after several DMAs. We used a logic analyzer to try to determine what is going wrong, but we could not find out what is causing this problem, as the bus is idle at the time the problem occurs.  Since the same card works properly, and has for approximately three years, in other Macintosh models (e.g., Quadra 900, Macintosh II, PowerMac 8100, Macintosh IIfx), is there anything different about the NuBus in the Quadra 840AV?  A: Your problem may be caused by a NuBus timing error that was uncovered by the MUNI chip. The MUNI chip was designed to perform much faster than the older NuBus controllers, and therefore is not as tolerant of timing errors.  While the Quadra 800, and Centris 650 have the KIWI NuBUS ASIC in them, the 840AV has the MUNI NuBUS ASIC. Both of these ASICs have much tighter timing margins to support NuBUS 90 and higher-speed burst transfers. The clock duty cycle of these ASICs is tighter (it is now very close to the 75/25 specification), and some developers have reported problems as a result.  Be sure to sample the correct edge of the NuBUS clock, per the NuBUS '90 specification. Even if your product works properly on the KIWI chip, there may be subtle timing and/or electrical changes in the MUNI chip that are causing your problem.  A similar problem was reported on the Macintosh Quadra 900/950 with the YANC chip and very fast transfers. The timing is such that the YANC (Yet Another NuBus Controller) chip, which came before KIWI and MUNI, gets lost on the Quadra. One developer was trying to transfer four longs by holding REQ\* asserted and was not using attention cycles. Because YANC lost the last arbitration, it looked for start, but it was one clock cycle too late (after the start cycle). As a result, it got lost, and the system hung. Although this problem doesn't exhibit exactly the same symptoms as the problem you are experiencing, there are enough similarities to indicate that both problems are probably caused by the timing differences.  The solution provided to that developer was to use attention-lock, transfer the four long words, and then do an attention-null to re-sync the YANC. This does add some overhead, but it is better than putting a dead cycle after every ACK\*, which would make transfers three cycles long instead of two. This approach might solve your problem, as well.  Here's another possible cause: The Muni chip generates a NuBus timeout error if the entire NuBus transaction takes more than 256 cycles (25.6 µsec) after Start occurs. For Block Transfers, the entire block must complete within 25.6 µsec. Muni generates a timeout error after 25.6 µsec, whether it initiated the NuBus transaction or not (e.g., if the transaction is between two NuBus cards). |

#### [May 01 1995]

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
