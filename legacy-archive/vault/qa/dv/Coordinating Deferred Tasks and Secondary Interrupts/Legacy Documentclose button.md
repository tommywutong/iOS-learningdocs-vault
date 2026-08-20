---
title: Coordinating Deferred Tasks and Secondary Interrupts
apple_id: DTS10001186
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/dv/dv45.html
archived_at: '2026-07-18T02:29:28.419962Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV45Coordinating Deferred Tasks and Secondary Interrupts |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I'm writing a driver for a USB network device. USB callbacks happen at secondary interrupt level. Many Open Transport calls can only be called from deferred task level. How do I get from one to the other?  A: The answer to this question is simple, although the background is very complex and needs some explanation. I will start with the basics and then fill in the details for the relentlessly curious.  Deferred Task to Secondary Interrupt  To get from deferred task level to secondary interrupt level, use the DriverServicesLib call `QueueSecondaryInterruptHandler`.   |  | | --- | | __WARNING:__  Do not use `CallSecondaryInterruptHandler2`. Depending on the system version this call will either do the wrong thing or fail with an error code if you call it from a deferred task. See the detailed explanation later in this document. |   Secondary Interrupt to Deferred Task  To get from secondary interrupt level to deferred task level, use the standard `DTInstall` system call. On some systems (see the explanation below), calling `DTInstall` from a secondary interrupt can result in the deferred task being called immediately (that is, before `DTInstall` returns). If this is a problem for your software, you can force the Deferred Task Manager to always queue your deferred task using the code from Listing 1.   |  |  | | --- | --- | | __Listing 1__. Forcing a deferred task to always be queued.   |  | | --- | | ``` static OSStatus MySecondaryInterruptHandler(void *p1, void *p2) {     OSStatus junk;     UInt16 oldInterruptMask;      oldInterruptMask = SetInterruptMask(7);      junk = DTInstall(&gDeferredTask);     MoreAssertQ(junk == noErr);      (void) SetInterruptMask(oldInterruptMask);      return noErr; } ``` | |   Listing 1 uses the routines from InterruptDisableLib, as described in DTS Technote 1137 [Disabling Interrupts on the Traditional Mac OS](https://developer.apple.com/library/archive/technotes/tn/tn1137.html).  The Full Story  As explained in DTS Q&A DV 43 [InterfaceLib and Native Drivers](Legacy%20Documentclose%20button-2.md), DriverServicesLib defines a model that is somewhat out of sync with the reality of traditional Mac OS. This is not a big problem if your software works entirely within the DriverServicesLib model, but it can cause problems if you write code that operates in both worlds. An example of this is a USB network driver, which must use both deferred tasks (Open Transport) and secondary interrupts (USB).  The biggest problem with calling DriverServicesLib routines from a deferred task is that many of its routines rely internally on the value returned by `CurrentExecutionLevel`. As explained in Technote 1104 [Interrupt-Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html), `CurrentExecutionLevel` does not always yield accurate results when called from non-DriverServicesLib environments (such as deferred tasks). If `CurrentExecutionLevel` returns the wrong result, DriverServicesLib does the wrong thing.   |  | | --- | | __IMPORTANT:__  A specific example of this problem is `CallSecondaryInterruptHandler2`. This routine calls `CurrentExecutionLevel` and uses the result to either:   - return an error (if the execution level is   `kHardwareInterruptLevel`), or - call the secondary interrupt handler   directly   (`kSecondaryInterruptLevel`), or - enter secondary interrupt level and run all   secondary interrupts   (`kTaskLevel`).   It has never been legal to call `CallSecondaryInterruptHandler2` from a deferred task, however the old `CurrentExecutionLevel` algorithm masked this error. This mislead some developers into thinking that it was OK to call `CallSecondaryInterruptHandler2` from a deferred task. When `CurrentExecutionLevel` was updated to return more accurate results, these developers' products broke.  When calling `CallSecondaryInterruptHandler2` from a deferred task there are three cases to consider.   1. On older systems (those with the old    `CurrentExecutionLevel` algorithm),    `CallSecondaryInterruptHandler2`    would treat deferred task level the same as    system task level. Calling    `CallSecondaryInterruptHandler2` from    a deferred task would run the handler (and any    other queued secondary interrupt handlers) and    return `noErr`. 2. On CPUs running Mac OS 9.0.4 with the new    `CurrentExecutionLevel` algorithm    ([Technote    1104](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) explains how to detect the presence of    the new algorithm),    `CallSecondaryInterruptHandler2`    would return an error if called from a deferred    task. 3. Because this caused some compatibility    problems, Mac OS 9.1 was changed    [2529860] to include a special case    'hack' that restores the old behavior of    `CallSecondaryInterruptHandler2`    without undoing the fix to    `CurrentExecutionLevel`.   In summary, your software should not call `CallSecondaryInterruptHandler2` from a deferred task because it defined to be illegal. It might work, but that doesn't make it right! |   Likewise, calling the Deferred Task Manager from a secondary interrupt yields strange results. Because of its heritage, the Deferred Task Manager uses the 68K interrupt mask to detect whether to queue the deferred task or call it immediately. However, the 68K interrupts mask is zero while secondary interrupts execute (this is, after all, the purpose of secondary interrupts), so if you call `DTInstall` from a secondary interrupt the Deferred Task Manager gets confused and typically executes the deferred task immediately. This exact behavior is dependent on the system version and the presence of VM and is shown in Table 1.   |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | __Table 1__. Behavior of `DTInstall` when called from a secondary interrupt.   | Mac OS Version | VM On | VM Off | | --- | --- | --- | | 9.0 and earlier | immediate • | immediate • | | 9.0.1 through 9.0.4 | queued | immediate • | | 9.1 and later | queued | queued |  - The deferred task is only executed immediately if it isn't blocked in some other way, for example, if an another deferred task is already running, or paging is unsafe. |   The behavior of `DTInstall` explains why the code in Listing 1 always forces the deferred task to be queued. By artificially (and temporarily) raising the interrupt mask to 7, it convinces the Deferred Task Manager that it is being called from a hardware interrupt, and hence must queue the deferred task.   |  | | --- | | __IMPORTANT:__  As you can see from this discussion, the 68K interrupt mask is not a good indication of the current execution level. In fact, there is no general way to determine the current execution level. Technote 1104 [Interrupt-Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) has a [section](https://developer.apple.com/library/archive/technotes/tn/tn1104.html#DeterminingExecutionLevel) describing the various common attempts to solve this problem, and their various flaws. |   In summary, problems can arise when you mix native driver model execution levels with older execution levels. You can avoid these problems using the techniques described at the beginning of this Q&A. |

#### [Nov 08 2000]

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
