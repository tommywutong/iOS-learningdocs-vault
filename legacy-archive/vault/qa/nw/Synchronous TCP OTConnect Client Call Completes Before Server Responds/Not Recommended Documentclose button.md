---
title: Synchronous TCP OTConnect Client Call Completes Before Server Responds
apple_id: DTS10001436
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw24.html
archived_at: '2026-07-18T02:29:45.124834Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW24Synchronous TCP OTConnect Client Call Completes Before Server Responds |

|  |
| --- |
| ---   Q: I make a synchronous `OTConnect` call from a TCP client to a TCP server which is passively awaiting an incoming connection. I find that even before the server responds with the `OTListen` and `OTAccept` calls, the `OTConnect` call complete with no error. At this point, if I examine the client endpoint state, I find that it is in the `T_DATAXFER` state. Can you explain this?  A: As mentioned in the X/Open Transport Interface (XTI) specification, "TCP does not allow the possibility of refusing a connection indication. Each connect indication causes the TCP transport provider to establish the connection. Therefore t_listen() and t_accept() have a symantic which is slightly different from that for ISO providers."  As a result, the server will accept the TCP connection request if the current number of connections is less than the `qlen` for the passive endpoint. As per the XTI specification, "when the transport detects a `T_LISTEN`, TCP has already established the connection." The client, whether in synchronous or asynchronous mode, will receive notice that the connection was established. For synchronous endpoints, TCP completes the 3-way connection handshake. For asynchronous endpoints, the `OTRcvConnect` call must be made to complete the handshake. |

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
