---
title: Explicitly Forcing PCI Burst Transfers
apple_id: DTS10001291
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw19.html
archived_at: '2026-07-18T02:29:36.114618Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW19Explicitly Forcing PCI Burst Transfers |

|  |
| --- |
| ---   Q: I am writing a device driver as well as diagnostic software for our new PCI card, which is capable of receiving PCI burst transfers (it is not a bus master).  How does one explicitly force PCI burst transfers? Is this done automatically when one calls `BlockMove` with a sufficiently large `Size` parameter?  A: Within the System's address space, main memory defaults to write back cache mode while PCI memory space defaults to cache inhibit mode. To enable the PowerPC to burst to areas of PCI memory space, the particular area must be set to a cacheable setting. However, extreme care must be taken to perform appropriate cache flushing when operating on cacheable PCI memory space. Drivers that control PCI masters may wish to experiment with different cache modes for their particular DMA buffer spaces to determine optimal settings. There is a `SetProcessorCacheMode` function in the Drive Services Library (DSL).  BlockCopy in the DSL uses `BlockMoveData` memory management primitive to move the bytes. `BlockMoveData` is optimized for cached data while `BlockMoveDataUncached` is optimized for uncached data.  For more information, refer to _Designing PCI Cards and Drivers_ |

#### [Jul 15 1995]

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
