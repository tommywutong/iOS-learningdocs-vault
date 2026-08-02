---
title: Using Deferred Tasks
apple_id: DTS10001425
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw13.html
archived_at: '2026-07-18T02:29:44.558979Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW13Using Deferred Tasks |

|  |  |
| --- | --- |
| ---   Q: I have a DDP socket listener in a driver, and I'd like to process some of the packets that it receives immediately. I know to be careful to avoid having more than one instance of my deferred task. I don't need to allocate memory, but I might have to open and close forks, read and write to and from those forks, and send a few packets. Can I do these things in a deferred task, or is there a better way to do this? Are there limitations on deferred tasks when they are performed due to a slot-manager interrupt (i.e., an incoming packet)?  A: The deferred-task-manager interrupt occurs when the interrupt handler winds down. The only difference between this interrupt and another interrupt is that the level is low enough for Nubus (or other) interrupts to occur while it's taking place. The rules are more or less the same for both types of interrupts -- you can't move memory, and the file manager might be busy when it occurs.  However, you can post an Async File Manager call at the time of the interrupt, which would allow you to close or write, assuming you pre-allocated your memory. If the file manager is busy, it will handle your call later, and your completion routine can chain to the next operation.  There aren't any time limits, but it helps to avoid delaying the system tasks for long periods. Since deferred tasks run at level 0, other interrupts can take priority over them.  Be sure to set up a semaphore system to handle those times when your task is placed in a queue during an interrupt that occurs while it's working.  As an alternative, you can make use of the Notification Manager by queuing a notification task that has no icon, string, etc. to run at the next systemtask time. This gives you a good A5 space where you can work with files, dialogs, memory, or whatever else you need. The following sample code should help you determine how to do this:   |  | | --- | | ```     NMRec                NM;    /* Notification Mgr Block */  NM.qType          = nmType;  NM.Icon = nil;  NM.Sound = nil;  NM.Mark = nil;  NM.Str = nil     NM.nmResp      = &YourHandler;  NM.nmRefCon    = your globals;  NMInstall(&NM); ....  YourHandler(NMRec * nmP) {   globals = nmP->nmRefCon; ... do whatever ...   NMRemove(nmP); } ``` | |

#### [Jun 01 1995]

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
