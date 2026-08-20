---
title: PrepareMemoryForIO and Execution Levels
apple_id: DTS10001173
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-06-08'
source_url: https://developer.apple.com/library/archive/qa/dv/dv32.html
archived_at: '2026-07-18T02:29:27.104659Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Coordinating Deferred Tasks and Secondary Interrupts](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV32PrepareMemoryForIO and Execution Levels |

|  |  |
| --- | --- |
| ---   Q: I'm writing a native driver (a SCSI SIM) that controls DMA hardware and needs to use partial preparation. How can I do this without breaking the rules described in Table 9-2 of "Designing PCI Cards and Drivers for Power Macintosh Computers"?  A: The short answer is that you can't do this without breaking the rules, but it's OK to break the rules in this case. A native SCSI SIM on the traditional Mac OS must call `PrepareMemoryForIO` at native hardware-interrupt level, and it is safe to do so. This is obviously going to require some explanation. Hold on to your hats!  For background information on the problem, you should read the article [The New Device Drivers: Memory Matters](https://developer.apple.com/dev/techsupport/develop/issue24/minow.html) (_develop_ 24). This article describes the official algorithm for implementing partial preparation mechanism in the native driver model. However, there are two problems with this algorithm:   1. It doesn't work (in practice) because it relies on software    interrupts, which are not implemented on the traditional Mac OS.    See    [Technote    1104: Interrupt Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) for a discussion of this    restriction. 2. It doesn't work (in theory) for devices on the page fault    path. This is because the algorithm requires the use of software    interrupts -- which can cause a page fault -- and a device on the    page fault path is not allowed to cause a page fault. This    restriction is described in the _develop_    [article](https://developer.apple.com/dev/techsupport/develop/issue24/minow.html) itself.   So the algorithm described in [The New Device Drivers: Memory Matters](https://developer.apple.com/dev/techsupport/develop/issue24/minow.html) is not valid for SCSI SIMs on the traditional Mac OS. There is, however, a relatively simple workaround that does work in these circumstances. In the algorithm described after Figure 2 of the _develop_ [article](https://developer.apple.com/dev/techsupport/develop/issue24/minow.html), you can compress steps 2, 3 and 4 into one step, eliminating the use of secondary-interrupt and software-interrupt level execution. As a result, your SIM calls `PrepareMemoryForIO` at native hardware-interrupt time. This is explicitly outlawed in Table 9-2 of "Designing PCI Cards and Drivers for Power Macintosh Computers," but is the only way that works.  The rest of this Q&A is a justification of why this works. To understand this discussion, you may need to reference [Technote 1094: Virtual Memory Application Compatibility](https://developer.apple.com/library/archive/technotes/tn/tn1094.html), which contains a comprehensive explanation of how virtual memory works on the traditional Mac OS.  On the traditional Mac OS, `PrepareMemoryForIO` is actually implemented as a wrapper around standard Virtual Memory Manager routines. The specific routines of interest are `LockMemory` and `GetPhysical`. The implementation of `PrepareMemoryForIO` is, in itself, interrupt-safe; thus, calling `PrepareMemoryForIO` is allowed at any time calling the underlying Virtual Memory Manager routines is allowed.   |  | | --- | | Note: On Mac OS 8.5 or higher, `PrepareMemoryForIO` will call `LockMemory` or `LockMemoryForOutput`, depending on the direction of the request, as specified in the `options` field of the `IOPreparationTable`. However, in this context we can treat `LockMemory` and `LockMemoryForOutput` as synonyms and ignore this complication. |   [Technote 1104: Interrupt Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) describes the interrupt-safe nature of `GetPhysical` and `LockMemory`. To summarize the discussion in that Technote, `GetPhysical` is always interrupt-safe and `LockMemory` is interrupt-safe if either a) paging is safe, or b) you can guarantee that locking the memory will not cause any page faults.  In the case of a SCSI SIM, the traditional Mac OS guarantees that any transfer buffer passed to the SIM is held resident in memory. This guarantee is maintained by two mechanisms:   1. The Virtual Memory Manager holds any transfer buffer passed to    a SCSI device driver. The details of this mechanism are covered in    the    [VM    Implementation Details](https://developer.apple.com/library/archive/technotes/tn/tn1094b.html#Implementation) section of    [Technote    1094](https://developer.apple.com/library/archive/technotes/tn/tn1094b.html). 2. The programming rules for SCSI Manager require that any    program making direct SCSI calls must hold all transfer buffers    passed to SCSI Manager. This requirement is explicitly spelt out    in the    [Direct    SCSI Manager or ATA Manager Calls](https://developer.apple.com/library/archive/technotes/tn/tn1094b.html#Programming1) section of    [Technote    1094](https://developer.apple.com/library/archive/technotes/tn/tn1094b.html).   So, as the author of a SCSI SIM, you are guaranteed that transfer buffers passed to your SIM are held resident. This implies that it's always safe to call `LockMemory` on those transfer buffers, even at hardware-interrupt time. This, in turn, implies that it is always safe to prepare those transfer buffers using `PrepareMemoryForIO`, even at hardware-interrupt time. |

#### [Jun 08 1998]

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
