---
title: NuBus Declaration ROM
apple_id: DTS10001272
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/hw/hw02.html
archived_at: '2026-07-18T02:29:35.268526Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > Hardware & Drivers](https://developer.apple.com/referencelibrary/GraphicsImaging/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A HW02NuBus Declaration ROM |

|  |
| --- |
| ---   Q: I am building a data-acquisition card that requires one driver in the system folder. Compared to a video card, this card is very simple, but it has to identify itself to the Slot Manager.  Should I put the driver into a system extension which would scan for the card at startup, or would it be better to have the code in the declaration ROM on the card tell the startup manager to load and execute the driver from the System folder?  A: The Slot Manager needs to see the declaration ROM in order to recognize your card and your driver. A video device is a special case, because the video driver is loaded before the file system becomes available. That's why video cards must have the driver in the declaration ROM.  There is sample code for a NuBus declaration ROM on the March 95 Developer CD. There is also quite a bit of detailed information regarding NuBus declaration-ROM code in _Designing Cards and Drivers for the Macintosh Family_, Third Edition. |

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
