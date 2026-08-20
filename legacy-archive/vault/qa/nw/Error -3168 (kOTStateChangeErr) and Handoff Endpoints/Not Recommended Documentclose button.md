---
title: Error -3168 (kOTStateChangeErr) and Handoff Endpoints
apple_id: DTS10001434
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/nw/nw22.html
archived_at: '2026-07-18T02:29:45.029389Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW22Error -3168 (kOTStateChangeErr) and Handoff Endpoints |

|  |
| --- |
| ---   Q: I've implemented a server endpoint which hands the connection off to a handoff endpoint. After the server processes a connect request using the `OTAccept` call, the asynchronous handler for the handoff endpoint is passed a `T_DATA` event. When the handler makes the `OTRcv` call, however, it returns error -3168, (`kOTStateChangeErr`). Can you explain this?  A: This problem only occurs when there is a handoff (secondary) endpoint involved. The implementation of Open Transport makes it possible for an asynchronous handoff endpoint to receive a `T_DATA` event before the connect mechanism is completed. After accepting a connection, an asynchronous listener endpoint can expect to receive a `T_ACCEPTCOMPLETE` call. The "accepting" or handoff endpoint can expect to receive the `T_PASSCON` event.  It is possible for the handoff endpoint to receive the `T_DATA` event before receiving the `T_PASSCON` event. If this happens, set a flag to defer receiving the data until later. When the `T_PASSCON` event is received, check the flag and issue the `OTRcv` call if the flag is set. (Note that after deferring the handling of the `T_DATA` event, your handler will not be notified with this event, until you process (read) all of the data presently available.) |

#### [Apr 08 1996]

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
