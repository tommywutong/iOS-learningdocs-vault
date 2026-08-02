---
title: Secondary Interrupts on the Page Fault Path
apple_id: DTS10001175
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-21'
source_url: https://developer.apple.com/library/archive/qa/dv/dv34.html
archived_at: '2026-07-18T02:29:27.647255Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV34Secondary Interrupts on the Page Fault Path |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q: I'd like to use secondary interrupts in my SCSI Interface Module (SIM) but doing so causes strange deadlocks. Is it legal to use secondary interrupts in a SIM?  A: In general, using secondary interrupts on the page fault path is not legal. There are, however, circumstances under which it works. As with most of my Q&A, this takes some explanation.    |  | | --- | | __Note:__  The __page fault path__ is the set system of system software and device drivers that are required to resolve a virtual memory page fault. The page fault path is an interesting concept in operating system design, because most operating systems require that all entities on the page fault path not cause a page fault. Double page faults will commonly cause an operating system to "panic".  On Mac OS, double page faults are always fatal. Mac OS prevents double page faults by disabling "user code" while page fault path entities are executing. In addition, all entities on the page fault path must be capable of performing an I/O request with interrupts disabled.  For more information about the virtual memory implementation on Mac OS, see Technote 1094 [Virtual Memory Application Compatibility](https://developer.apple.com/library/archive/technotes/tn/tn1094.html). |     |  | | --- | | __IMPORTANT:__  While this Q&A is couched in terms of SCSI Manager SIMs, the same logic applies to any entity on the page fault path. Third-party developer opportunities on the page fault path currently include SIMs, AIMs (ATA Interface Modules), and disk drivers. This list will grow as new technologies, like FireWire, evolve to support disk devices. |   The two common reasons for using secondary interrupts in a device driver are:   1. Reducing interrupt latency -- By deferring complex    work to a secondary interrupt, you can reduce the amount    of time your driver spends at hardware interrupt time,    and thereby reduce the overall interrupt latency of the    system. 2. Concurrency guarantee -- Secondary interrupts are    guaranteed to be serialized; only one secondary interrupt    handler can be running at any point in time. This is a    very useful concurrency control mechanism. If you always    access global data structures from your secondary    interrupt handler, you can be assured that only one    thread of execution is reading or writing those global    data structures at a time.   However, secondary interrupts can cause problems for devices on the page fault path. Imagine the following scenario:   1. Your SIM takes a hardware interrupt, schedules a    secondary interrupt (SIH A), and then returns from its    hardware interrupt handler. For your SIM to make forward    progress, its secondary interrupt handler must execute to    completion. 2. The interrupt systems notices that it is returning to    interrupt level 0 and begins processing secondary    interrupts. It enables interrupts and starts running    secondary interrupt handlers. 3. While SIH A is running, a Time Manager interrupt    occurs. The timer task executes, schedules a deferred    task, and then returns. 4. The interrupt system notices that it is returning    from the Time Manager interrupt to interrupt level 0.    There are deferred tasks to run, so it enables interrupts    and starts running deferred tasks. 5. One of the deferred tasks causes a page fault. 6. The Virtual Memory Manager intercepts the page fault,    and makes a synchronous request to the disk device driver    to read the page contents from the backing store. 7. The disk device driver calls SCSI Manager to execute    a SCSI command, which in turn calls your SIM. Your SIM    starts the command and returns, expecting a hardware    interrupt to complete the command. 8. Your SIM's hardware interrupt fires and schedules a    secondary interrupt (SIH B) to complete the command.   The system is now deadlocked. The SIH B cannot run because secondary interrupt handlers must be single-threaded and SIH A is already running. But the SIH A cannot run because it has been interrupted by a page fault, which is sitting in a synchronous wait loop waiting for SIH B to run.  The solution is to not use secondary interrupt handlers in your SIM, or any software entity on the page fault path.  Newer versions of Mac OS provide another workaround for this problem. On such systems, the OS detects these potential deadlock cases (waiting for a synchronous device request with an interrupt mask of 0 and with secondary interrupt handlers queued) and calls your [SIMInterruptPoll](https://developer.apple.com/documentation/mac/Devices/Devices-198.html) routine. Your interrupt poll routine can detect that it has queued a secondary interrupt that has not yet run, and perform the appropriate action directly. Typically this involves calling your secondary interrupt handler routine directly.  This approach has a number of important caveats:   1. It does not work on older systems. You can check for    the presence of secondary interrupt polling using the    code in Listing 1. You should find it available on Mac OS    8.5 and later. 2. Secondary interrupt polling may undermine the    concurrency guarantees provided by secondary interrupts.    In the above example, look carefully at what happens during    the deadlock recovery process. The system calls your    interrupt poll routine and your interrupt poll routine    calls SIH B directly. At this point, you have two threads    of execution inside secondary interrupt handlers, SIH A    and SIH B. This could cause problems if you designed your    SIM to rely on the concurrency guarantees provided by    secondary interrupts. If you want to use secondary    interrupts in your SIM, you must take this potential    reentrancy into account. 3. Secondary interrupt polling is only useful for    devices with an interrupt poll routine, such as SIMs and    AIMs. Other native drivers, such as disk drivers, do not    have an interrupt poll routine and cannot use secondary    interrupts if they are on the page fault path.   Because of these caveats, it may just be easier to do everything in your SIMs hardware interrupt handler. SIMs are mostly I/O bound, so the interrupt latency increase of doing everything in your hardware interrupt handler is minimal.  You can detect whether secondary interrupt polling is implemented using `Gestalt`, as shown in Listing 1.  __Listing 1__. Determining whether secondary interrupt polling is available    |  | | --- | | ``` static Boolean HasSecondaryInterruptPolling(void) {     UInt32 response;      return (Gestalt(gestaltSCSI, (SInt32 *) &response) == noErr) &&             ((response & (1 << gestaltSCSIPollSIH)) != 0); } ``` |   In summary:   - Prior to Mac OS 8.5, you must never use secondary   interrupts on the page fault path. - With Mac OS 8.5 and beyond, SIMs and AIMs may use   secondary interrupts, but they must take special action   in their interrupt poll routine. - Despite the difficulties using secondary interrupts   in a SIM, DTS recommends that SIM developers seriously   consider adopting this technique. The primary advantage,   lower system interrupt latency, is a significant benefit   to real-time applications such as QuickTime.   For more information about this mind-manglingly complex part of the Mac OS I/O subsystem, see:   - [Designing   PCI Cards and Drivers for Power Macintosh Computers](ftp://ftp.apple.com/devworld/Development_Kits/PCI_Driver_SDK.sit.hqx) - [Inside   Macintosh: Devices](https://developer.apple.com/documentation/mac/Devices/Devices-2.html) (especially the   [SCSI   Manager 4.3](https://developer.apple.com/documentation/mac/Devices/Devices-151.html) chapter) - Technote 1094   [Virtual   Memory Application Compatibility](https://developer.apple.com/library/archive/technotes/tn/tn1094.html) - Technote 1104   [Interrupt-Safe   Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) - Technote 1137   [Disabling   Interrupts on the Traditional Mac OS](https://developer.apple.com/library/archive/technotes/tn/tn1137.html) - DTS Q&A DV 32   [PrepareMemoryForIO   and Execution Levels](../Coordinating%20Deferred%20Tasks%20and%20Secondary%20Interrupts/Legacy%20Documentclose%20button-3.md) |

#### [Dec 21 1998]

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
