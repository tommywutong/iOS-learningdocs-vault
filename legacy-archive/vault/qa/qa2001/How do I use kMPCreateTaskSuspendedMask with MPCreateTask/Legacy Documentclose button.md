---
title: How do I use kMPCreateTaskSuspendedMask with MPCreateTask?
apple_id: DTS10001607
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2001-07-02'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1055.html
archived_at: '2026-07-18T02:38:06.048991Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A QA1055How do I use kMPCreateTaskSuspendedMask with MPCreateTask? |

|  |
| --- |
| ---   Q: When I call the `MPCreateTask` API with the `kMPCreateTaskSuspendedMask` option my task is suspended at startup but I then can't figure out how to resume it. Is there an API that can resume my task?  A: The `kMPCreateTaskSuspendedMask` was originally intended to allow debuggers to start tasks in the suspended state. But because of how exception handlers work the ability to resume a task that wasn't suspended by an actual exception was never possible. If you want to suspend a task when it starts and be able to resume it later you have to use the `MPThrowException` API in your task at the point where you want to suspend it. You exception handler can then resume that task at a later time. Optionally, if all you want is to be able stop/start the task you may consider using one of the synchronization / signaling API's (semaphores, queue, event groups, critical regions, etc.).   ---  [Jul 02 2001] |

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
