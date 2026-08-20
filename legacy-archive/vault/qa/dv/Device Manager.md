---
title: Device Manager
apple_id: DTS10001142
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/dv/dv01.html
archived_at: '2026-07-18T02:29:25.360485Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A DV01Device Manager |

|  |
| --- |
| ---   Q: I'd like to port some of my `'DRVR'` code to the PowerPC, but I'm worried about the 68K-specific design of the Device Manager. What should I do?  A: In general, we advise against writing PowerPC-native device driver code, with the current emulated Device Manager architecture. Each driver call incurs a Mixed Mode context switch (75-125 microseconds) just to enter the code. The same reasoning applies to interrupt routines.  Depending on how much your driver routines do, it may even happen that the driver with the native code runs slower than the original emulated code. These routines would have to be loaded and called using the Code Fragment Manager and Mixed Mode.  There are a few things that low-level device driver programmers should know: The 68K instructions that produce indivisible read-modify-write bus cycles do not produce indivisible bus cycles on the PowerPC. This is because there is no read-modify-write cycle in the PowerPC ARBus architecture. If you're using TAS or CAS to do semaphore operations, you should look into software semaphore solutions. They can also use the PowerPC instructions `lwarx` (Load Word and Reserve Indexed) and `stwcx`. (Store Word Conditional Indexed). These instructions can be used to provide a base for building semaphores. Keep in mind that the memory location locked must be in main memory on the PowerPC computer.  Another problem you may run into is bus reordering. The 601 can choose to reorder bus operations to be more efficient. This means a load from a specific address followed by a store to a second location could happen in reverse order. Accesses to the same location are always serialized and will occur in instruction order. Where this becomes a problem is working with config registers on hardware devices. Say you have a control register and a data register on a NuBus(TM) card. Normally, you would write a value to the control register; this value would then produce a result in the data register which you would then read with the next instruction. If the 601 reorders the bus transactions, the read will occur first and you will be provided with bad data. To prevent this problem, you need to execute a PowerPC `eieio` (Enforce In-Order Execution of I/O) instruction between the write and read. The emulator will execute an eieio when a 68K NOP is dispatched. So you should insert NOP or eieio instructions between any order critical reads and writes.  Another change that may affect NuBus developers is Bart. Bart is the code name for the NuBus controller on the 601 systems. Bart has very similar features to MUNI (the controller in the 840av and 660av). One new feature is "dump and run." This means Bart will absorb a ARBus burst write, release the ARBus and then transfer the data to NuBus with a burst or locked multi-beat write. This increases the overall throughput to NuBus and also frees the ARBus for other processing. NuBus and the ARBus therefore work asynchronously with Bart. |

#### [May 05 1999]

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
