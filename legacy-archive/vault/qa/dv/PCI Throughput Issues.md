---
title: PCI Throughput Issues
apple_id: DTS10001161
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/dv/dv20.html
archived_at: '2026-07-18T02:29:26.323276Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A DV20PCI Throughput Issues |

|  |
| --- |
| ---   Q: We want to maximize our throughput across the PCI bus between Mac memory and a block of static RAM on our card. This static RAM is also accessible from an on-card DSP, which constantly reads/modifies RAM. The DSP is not directly on the PCI bus, so it cannot easily participate in cache coherency schemes.  What's the best way to get data across PCI to and from this memory?  A: PPC can only burst to and from a CACHEABLE memory space. Your best option is to use `BlockMoveDataUncached`. This does not use burst transfers, but rather, it utilizes floating point loads and stores.  You may want to design your own algorithms, using the double declaration in C to get compilers to translate `BlockMoveDataUncached` into floating point loads and stores. See _Designing PCI Cards and Drivers for PowerMac Computers_, Chapter 9. |

#### [Sep 15 1995]

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
