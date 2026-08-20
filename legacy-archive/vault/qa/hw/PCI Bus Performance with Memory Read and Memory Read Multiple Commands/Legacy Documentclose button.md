---
title: PCI Bus Performance with Memory Read and Memory Read Multiple Commands
apple_id: DTS10001275
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw05.html
archived_at: '2026-07-18T02:29:35.393200Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW05PCI Bus Performance with Memory Read and Memory Read Multiple Commands |

|  |
| --- |
| ---   Q: If I attempt to transfer a full cache line using the `MemoryRead` command, will I get lower performance than if I make the same transfer with the `MemoryReadMultiple` command?  A: Yes. If you use `MemoryRead` instead of `MemoryReadLine` or `MemoryReadMultiple`, you will be disconnected at eight-byte boundaries, because, just as with the writes, that is the size of a PowerPC single transaction. In the first implementation, a `MemoryReadLine` and `MemoryReadMultiple` are dealt with in the same way. There is no optimization for `MemoryReadMultiple`. However, you should use the `MemoryReadMultiple` transaction if that is what your PCI Master is doing, i.e., transferring multiple cache lines. Future bridges should take advantage of that. If you are doing a cache line read, or even close to a full cache line, you should do a `MemoryReadLine`.  Follow the PCI Specification's description of the different cycles. The general rule of thumb is:   - If the number of data phases is <= 2, use `MemoryRead`. - If the number of data phases is > 2 and <= the cache line size, use `MemoryReadLine`. - If the number of data phases > one cache line, use `MemoryReadMultiple`.   There are better guidelines than these in Rev. 2.1 of the PCI Specification. Although the PCI SIG hasn't officially released this revision of the specification, it should be available from your company's PCI SIG representative. |

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
