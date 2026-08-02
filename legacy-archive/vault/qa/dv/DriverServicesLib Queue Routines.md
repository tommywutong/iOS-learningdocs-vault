---
title: DriverServicesLib Queue Routines
apple_id: DTS10001181
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-01-18'
source_url: https://developer.apple.com/library/archive/qa/dv/dv40.html
archived_at: '2026-07-18T02:29:27.976562Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV40DriverServicesLib Queue Routines |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I've noticed that when I use the DriverServicesLib queue routines (for example, `PBEnqueue`), the `qTail` field of the `QHdr` is always nil. Is this expected? Are there other differences between the DriverServicesLib queue routines and those provided in "OSUtils.h"?  A: Other than initializing it to zero, the DriverServicesLib queue routines never use the `qTail` field of the `QHdr`, so yes, that is expected. Furthermore, it means that you can't mix and match queue routines on the same queue. When you create a queue, you should choose which set of routines you intend to use, and use those routines on that queue exclusively.  The most obvious differences between the DriverServicesLib queue routines and the "OSUtils.h" queue routines is that DriverServicesLib provides a larger set of routines. For example, you can use `PBEnqueue` and `PBEnqueueLast` to place an element at either the beginning or the end of a queue.  In addition, the DriverServicesLib queue routines are implemented in PowerPC code and have been optimized to avoid Mixed Mode switches in some cases.   | Routine | Mixed Mode Switches? | | --- | --- | | `PBEnqueue` | never | | `PBEnqueueLast` | adding to a non-empty queue | | `PBDequeue` | dequeuing elements other than the first | | `PBDequeueFirst` | never | | `PBDequeueLast` | always |   The implementation of these queue routines (and their relative performance) is subject to change. |

#### [Jan 18 2000]

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
