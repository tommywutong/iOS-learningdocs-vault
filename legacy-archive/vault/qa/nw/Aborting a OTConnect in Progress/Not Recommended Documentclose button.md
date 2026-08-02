---
title: Aborting a OTConnect in Progress
apple_id: DTS10001441
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw29.html
archived_at: '2026-07-18T02:29:45.735910Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW29Aborting a OTConnect in Progress |

|  |
| --- |
| ---   Q: I'd like my network client software to be able to abort an asynchronous `OTConnect` in progress -- to allow a user, for example, to recover from an attempted connection to a nonexistent IP address.  I've been calling `OTSndDisconnect` to abort it, but when I check the return code, I get a `kOTOutStateErr`. What gives?  A: Using a `OTSndDisconnect` is the proper way to abort an `OTConnect` in progress. After successfully calling `OTConnect`, the endpoint state will transition from `T_IDLE` to `T_OUTCON`. Calling `SndDisconnect` returns the endpoint state to `T_IDLE`. You may be getting a `kOTOutStateErr` for the following reasons:   1. The original `OTConnect` failed. Determine this by checking the `OTConnect`    result. 2. The connection broke and was asynchronously handled by your notifier. In    this case, your endpoint would no longer be in the `T_OUTCON` state when you do    the disconnect.   A good rule of thumb is to always confirm the endpoint state before doing the `OTSndDisconnect` to insure that the endpoint isn't already disconnected. |

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
