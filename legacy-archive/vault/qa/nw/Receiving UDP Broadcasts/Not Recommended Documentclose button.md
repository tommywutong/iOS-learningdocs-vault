---
title: Receiving UDP Broadcasts
apple_id: DTS10001465
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-11-17'
source_url: https://developer.apple.com/library/archive/qa/nw/nw53.html
archived_at: '2026-07-18T02:29:47.117473Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW53Receiving UDP Broadcasts |

|  |
| --- |
| ---   Q: I've created an Open Transport UDP endpoint to listen for UDP broadcasts. However the endpoint never receives any UDP broadcast messages. A packet sniffer shows that the UDP packet is actually arriving at the machine. What's going on?  A: There are two likely causes for this problem:   1. The port you're binding to is already in use, so OT reroutes your    bind request to another port. You can check for the problem programatically    by passing a `retAddr` parameter to `OTBind`, and checking    that the resulting `fPort` field matches the port you requested. One common cause of this is that the port is still in use by your own application    because of the IP reuse address delay. You can eliminate this delay using the code    described in Q&A NW 28 ["TCP Application Acquires Different Port Address After Relaunch"](Not%20Recommended%20Documentclose%20button-2.md).    That Q&A is specific to TCP endpoints, but the technique works for both TCP and UDP endpoints. 2. You are passing a specific IP address to `OTBind`. General purpose    programs that want to listen for connections/datagrams should always bind to `kOTAnyInetAddress`    (ie 0), not to a specific IP address. On a multi-homed machine, if you bind to a    specific address, you will only receive connections/datagrams addressed to that IP    number. This is useful if you're writing a server that reacts differently depending    on which IP address it receives a connection on, but most general purpose code should    not care which IP address the connection/datagram was sent to.    In this specific case, if you bind a UDP endpoint to a specific IP address, you will    not receive broadcast packets on that endpoint because they were not sent to the    specific IP address you bound to. |

#### [Nov 17 1997]

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
