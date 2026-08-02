---
title: 'Closing the Connection: OpenTransport'
apple_id: DTS10001432
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-03-04'
source_url: https://developer.apple.com/library/archive/qa/nw/nw20.html
archived_at: '2026-07-18T02:29:44.937340Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW20Closing the Connection: OpenTransport |

|  |
| --- |
| ---   Q: I am writing an OpenTransport client program, and I'm confused as to how to perform an orderly release when I receive the `T_ORDREL` message.  When I get the `T_ORDREL` message I'm supposed to call `RcvOrderlyDisconnect`. The docs for `RcvOrderlyDisconnect` say that I can then continue to send data, but I cannot read data without getting an `outState` error.  Is this correct?  A: Yes, it is. Your confusion is due more to the dynamics and subtleties of XTI programming than to OpenTransport.  In an orderly disconnect situation, assume that two nodes have an established TCP connection__.__ Endpoint A has finished sending data and indicates closure by invoking a `SndOrderlyDisconnect` call (this translates into sending a end-of-file signal (FIN) over the wire).  Endpoint B receives a `T_ORDREL` message. If, however, B has not finished receiving the data, then B must continue calling into `Rcv` until it gets back `kOTNoDataErr`. At this point, B initiates a `RcvOrderlyDisconnect` (which acknowledges A's FIN).  This is known as a "half-close." B can still call `Snd` to send data to A (which will still receive `T_DATA` events); but if A attempts to send, it will receive an out-of-state Error.  Once B has finished receiving the data, it must initiate a `SndOrderlyDisconnect` -- resulting in sending A a FIN. A should also continue accepting data until receiving `kOTNoDataError`. A should then call `RcvOrderlyDisconnect`, thereby completing the link teardown. Both sides can then unbind.  If, however, either endpoint's network code is written such that `T_ORDREL` and `T_DATA` events are handled at different priorities, (for instance, the `T_ORDREL` is handled at the notifier, but the `T_DATA` is deferred to `systemTask` time) then a race condition can occur. Your program __must__ establish that all data has been read before calling `RcvOrderlyDisconnect`.  There is also a subtlety of XTI programming that you should be aware of. It is possible that `SndOrderlyDisconnect` or `RcvOrderlyDisconnect` will return with a `TLOOK` error. This means that there is another event pending; your program must call OTLook to gather that event.  According to the XTI spec ("Section 4.6 Events and TLOOK Error indication"), the `SndOrderlyDisconnect` and `RcvOrderlyDisconnect` calls can fail because of a pending `T_DISCONNECT` event. This is XTI trying to tell you that the a connection on that endpoint broke. This can happen in this asynchronous wacky world of networks and your program will have to call a `RcvDisconnect` to acknowledge that your endpoint dropped.  You might want to check out the OTI spec, which, although it is not always written in the most lucid fashion, does contain valuable information for those involved in OpenTransport programming. Further Information:Title: X/OPEN TRANSPORT INTERFACE (XTI) VER 2 [ 1.0 ed]  Author: X/OPEN   ISBN #: 0133534596 |

#### [Mar 04 1996]

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
