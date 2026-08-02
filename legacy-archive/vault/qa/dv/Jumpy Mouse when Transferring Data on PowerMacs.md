---
title: Jumpy Mouse when Transferring Data on PowerMacs
apple_id: DTS10001164
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv23.html
archived_at: '2026-07-18T02:29:26.498100Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxUserExperience-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [User Experience > Human Interface Device & Force Feedback](https://developer.apple.com/referencelibrary/UserExperience/idxHumanInterfaceDeviceForceFeedback-date.html)

|  |
| --- |
| Technical Q&A DV23Jumpy Mouse when Transferring Data on PowerMacs |

|  |
| --- |
| ---   Q: We have SCSI routines that transfer 64kB data blocks (to get the highest transfer rates possible with the tape drive we are using). On the PowerPC (8100/80 or 8100/100), if the mouse is moved during a 64k transfer, the mouse is jumpy.  Lowering the cache size to 16k reduces the problem to an acceptable level, but kills the transfer rates. We are using the SCSI manager 4.3.  How do we avoid the jumpy mouse while maintaining maximum throughput?  A: Your jumpy mouse is an indication that you are not properly implementing SCSI DMA. When using the 8100 (and PCI machines) for Direct Memory Access (DMA) transfer efficiency, you want to ensure that:   1. Your data is aligned on 8 byte block boundaries. Since the DMA hardware    can't do odd transfers, it must perform a Programmed IO to handle at least part    of the transfer. 2. Your buffer physical memory is contiguous (a la `LockMemoryContiguous`). Otherwise, the DMA transfer will have to be broken up: this will especially be    a problem if Virtual Memory is turned on.   If you have disconnects enabled in your device or driver, it's possible that the transfer is broken up and some VBL activity is occurring. The bottom line is that you don't want a SCSI disconnect occurring during your transfer. |

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
