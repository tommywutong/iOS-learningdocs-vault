---
title: Open Transport T_DATA Event Queuing
apple_id: DTS10001442
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw30.html
archived_at: '2026-07-18T02:29:45.789143Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW30Open Transport T_DATA Event Queuing |

|  |
| --- |
| ---   Q: I have a question regarding `T_DATA` event handling for multiple active endpoints.  Let's say I have two endpoints open, ep1 and ep2. Data arrives for ep1, which then receives a `T_DATA` event.  If data arrives on ep2 before the data for ep1 is read, it is my understanding that ep2 will not get a `T_DATA` event until the data for ep1 is read. Is that correct? When the data for ep1 is finally read will ep2 then get a `T_DATA` event?  In other words, does Open Transport queue multiple `T_DATA` events corresponding to multiple endpoints?  A: XTI or Open Transport endpoints are handled independently of each other. Whatever events are pending on one endpoint have (for the most part) no effect on any other endpoints.  Assume that ep1 gets notified of a `T_DATA` event. Following this, a separate `T_DATA` event is queued up for ep2. As soon as the notifier for ep1 completes and returns to OpenTransport, the notifier for ep2 will be invoked. This behavior is not contingent upon whether ep1 processed the event or not.  Consequently, ep1 will not receive any more `T_DATA` events until its current T_DATA event is cleared. (In this case, by invoking `OTRcv` until its status returns a `kOTNoDataErr`.)  Keep in mind that waiting too long to process ep1's `T_DATA` event will result in the exhaustion of buffers in the lower protocol layers. |

#### [May 14 1996]

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
