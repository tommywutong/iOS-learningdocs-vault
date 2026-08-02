---
title: Ethernet Driver Interface
apple_id: DTS10001416
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw04.html
archived_at: '2026-07-18T02:29:44.119763Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW04Ethernet Driver Interface |

|  |
| --- |
| ---   Q: Is there an Ethernet-driver-interface `PBControl` spec that allows the Ethernet interface to receive all multicast packets on the locally connected Ethernet? In other words, I need the ability to directly access the Ethernet-hardware logical-address filter, so that all multicast packets are received.  I can use the `EAddMulti()` function to add a multicast address to the node on which the Ethernet driver is running only six times in succession. On the seventh call, the function returns result code `eMultiErr (-91)`, indicating that the table is full. I am attempting to add 64 unique, sequential addresses to the table to allow reception of all multicast groups. My understanding of the underlying hardware is that, with a 64-bit logical-address filter, with all bits set, the hardware receives all multicast addresses on the interface. Can this apparently arbitrary maximum number of six multicast entries be modified (to 64), so I can "fill out" the hardware-multicast logical-address filter?  A: The number of addresses you can set up for multicast _is_ limited. The size of the limit depends on the driver you are dealing with (i.e., Apple, Asante, etc). This limit is a function of the number of CAM locations the Ethernet controller supports. Controllers with a SONIC chip support six CAM locations, so with these controllers, the limit on multicast addresses is six.  Q: I need the ability to set the interface to "promiscuous" mode, where all (multicast and unicast) addresses are received.  A: Our Ethernet driver does _not_ support promiscuous mode. The only way to enable promiscuous mode is to write your own Ethernet driver to support promiscuous mode only. This is no easy task, in that you need to know about every network interface card that exists if you need to support them all.  There is also a performance issue with promiscuous mode, as it is very interrupt-intensive. If you are on a busy network, promiscuous-mode operation would require a very fast Macintosh. |

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
