---
title: AppleTalk Limitations
apple_id: DTS10001414
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw02.html
archived_at: '2026-07-18T02:29:43.996060Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW02AppleTalk Limitations |

|  |  |
| --- | --- |
| ---   Q: _Inside Macintosh, Volume V_, lists ATP limitations for the Macintosh Plus, RAM-based, Macintosh SE, and Macintosh II AppleTalk implementations. Where can I find the same information for other recent AppleTalk versions? By the way, what's the difference between the `tooManyReqs` and the `noDataArea` errors returned by `PSendRequest` and `PNSendRequest`?  A: ATP in AppleTalk version 58.x has several hard-coded limitations. They are:   - the maximum number of concurrent `SendRequests` is 12 - the maximum number of ATP sockets that can be opened is 126 - the maximum number of concurrent XO `SendResponses` is 32 - the number of ATP data areas (parameter blocks for ATP's MPP calls) to - allocate is 8.   `PGetAppleTalkInfo` returns some information about MPP's limits, but not those for ATP.  If you use `PNSendRequest` instead of `PSendRequest`, your calls will be faster (because ATP doesn't have to open a socket each time it sends a request) and you won't be limited to 12 concurrent SendRequests. The maximum number of `PNSendRequests` is currently calculated based on the value of the `TimeDBRA` low memory global (a word value). We cannot guarantee this formula will always be used but this is what's currently used:   |  | | --- | | ```    max number of PNSendRequests = ((((TimeDBRA / 100) * 120) - 142) / 48) ``` |   For example, `TimeDBRA` on the Macintosh II is 2620, so ((((2620 / 100) \* 120) - 142) / 48) = 62 (That's the same number in the chart on page V-520 in Inside Macintosh, Volume V).  You can get a `tooManyReqs` error from either PSendRequest or PNSendRequest if you attempt too many concurrent requests; 12 for `PSendRequest`; the number from the formula above for `PNSendRequest`.  A `noDataArea` error is not the same (although your application may want to treat it the same). When ATP calls the MPP driver to send out a packet (with `PWriteDDP`), it has to use a parameter block. As noted above, the number of parameter blocks available for this purpose is 8. Since DDP write operations normally complete rather quickly, the chances of 8 calls backing up should be rare. However, if the limit is hit, a `noDataArea` is returned and the packet is not sent.  In most cases, when you get either the `tooManyReqs` or the `noDataArea` error, retrying the request after a short delay should work.  The reason ATP limits concurrent XO `SendResponses` is that ATP has to keep the responses it receives until it receives a release packet, or until the transaction times out.  Remember, your program shares the ATP driver's limited resources with other network programs running (for example, mail servers, mail clients, the AppleShare client, the File Sharing or AppleShare server), so you should only use a reasonable amount of the shared resource. |

#### [May 01 1995]

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
