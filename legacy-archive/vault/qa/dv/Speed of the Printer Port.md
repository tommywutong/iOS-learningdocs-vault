---
title: Speed of the Printer Port
apple_id: DTS10001172
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/dv/dv31.html
archived_at: '2026-07-18T02:29:27.042544Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Serial](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSerial-date.html)

|  |
| --- |
| Technical Q&A DV31Speed of the Printer Port |

|  |
| --- |
| ---   Q: In [Inside Mac:Devices](https://developer.apple.com/documentation/mac/Devices/Devices-314.html), it says:  Because the serial hardware in some Macintosh computers relies on processor interrupts during I/O operations, overrun errors are possible if interrupts are disabled while data is being received at the serial port. To prevent such errors, the Disk Driver and other system software components are designed to store any data received by the modem port while they have interrupts disabled, and then pass this data to the port's input driver. Because the system software only monitors the modem port, the printer port is not recommended for two-way communication at data rates above 300 baud.  Is this still true for computers which use the Serial DMA driver? Is printer port still slower than modem port?  A: Practically speaking, the printer port is probably no less capable than the modem port of maintaining high baud rates if it has DMA on the receive channel. Note that on the 68K AV Macs, which do use SerialDMA, there is still no DMA on the receive channel, so the printer port is less capable on those machines.  On the other hand, there are internal prioritization algorithms for the SCC which dictate that channel A (modem port) takes priority over channel B (printer port), so if you're trying to do something on both ports simultaneously and channel A is completely saturated (a term which I use loosely because I am at a loss to define it accurately), then port B could theoretically be starved. |

#### [Jul 11 1997]

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
