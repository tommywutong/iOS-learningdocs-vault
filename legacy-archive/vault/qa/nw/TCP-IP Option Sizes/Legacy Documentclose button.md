---
title: TCP/IP Option Sizes
apple_id: DTS10001474
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '1999-04-26'
source_url: https://developer.apple.com/library/archive/qa/nw/nw62.html
archived_at: '2026-07-18T02:29:47.625845Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Darwin > Networking](https://developer.apple.com/referencelibrary/Darwin/idxNetworking-date.html)

|  |
| --- |
| Technical Q&A NW62TCP/IP Option Sizes |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I'm confused by the size of various TCP/IP options. For example, the documentation says that `IP_MULTICAST_LOOP` is a 4-byte option, but the `IPMulticastPitch` sample negotiates a size of 1 byte. What's the scoop?  A: In this case, the documentation is wrong. The following table enumerates all the TCP/IP options and their sizes.   |  |  |  |  | | --- | --- | --- | --- | | __XTI Level__ | __XTI Name__ | __Size__ |  | | `INET_IP` | `IP_ADD_MEMBERSHIP` | `sizeof(struct ip_mreq)` |  | | `INET_IP` | `IP_BROADCAST` | `4` |  | | `INET_IP` | `IP_BROADCAST_IFADDR` | `4` |  | | `INET_IP` | `IP_DONTROUTE` | `4` |  | | `INET_IP` | `IP_DROP_MEMBERSHIP` | `sizeof(struct ip_mreq)` |  | | `INET_IP` | `IP_HDRINCL` | `4` |  | | `INET_IP` | `IP_MULTICAST_IF` | `4` |  | | `INET_IP` | `IP_MULTICAST_LOOP` | `1` | \* | | `INET_IP` | `IP_MULTICAST_TTL` | `1` |  | | `INET_IP` | `IP_OPTIONS` | `<= 40` |  | | `INET_IP` | `IP_RECVDSTADDR` | `4` |  | | `INET_IP` | `IP_RECVIFADDR` | `4` |  | | `INET_IP` | `IP_RECVOPTS` | `4` |  | | `INET_IP` | `IP_REUSEADDR` | `4` |  | | `INET_IP` | `IP_REUSEPORT` | `4` |  | | `INET_IP` | `IP_TOS` | `1` |  | | `INET_IP` | `IP_TTL` | `1` |  | |  |  |  |  | | `INET_TCP` | `TCP_ABORT_THRESHOLD` | `4` |  | | `INET_TCP` | `TCP_CONN_ABORT_THRESHOLD` | `4` |  | | `INET_TCP` | `TCP_CONN_NOTIFY_THRESHOLD` | `4` |  | | `INET_TCP` | `TCP_KEEPALIVE` | `sizeof(struct t_kpalive)` | \* | | `INET_TCP` | `TCP_MAXSEG` | `4` |  | | `INET_TCP` | `TCP_NODELAY` | `4` |  | | `INET_TCP` | `TCP_NOTIFY_THRESHOLD` | `4` |  | | `INET_TCP` | `TCP_OOBINLINE` | `4` |  | | `INET_TCP` | `TCP_URGENT_PTR_TYPE` | `4` |  | |  |  |  |  | | `INET_UDP` | `UDP_CHECKSUM` | `4` |  | | `INET_UDP` | `UDP_RX_ICMP` | `1` | \* | |  |  |  |  | | `XTI_GENERIC` | `XTI_DEBUG` | `4` |  | | `XTI_GENERIC` | `XTI_LINGER` | `sizeof(struct t_linger)` |  | | `XTI_GENERIC` | `XTI_PROTOTYPE` | `4` |  | | `XTI_GENERIC` | `XTI_RCVBUF` | `4` |  | | `XTI_GENERIC` | `XTI_RCVLOWAT` | `4` |  | | `XTI_GENERIC` | `XTI_SNDBUF` | `4` |  | | `XTI_GENERIC` | `XTI_SNDLOWAT` | `4` |  |       |  | | --- | | __Warning:__  [Inside Macintosh: Networking with Open Transport](https://developer.apple.com/documentation/mac/NetworkingOT/NetworkingWOT-2.html) gives either incorrect or ambiguous values for the options tagged with an asterisk (\*) in the above table. |       |  | | --- | | __Note:__  The `IP_REUSEPORT` and `IP_BROADCAST_IFADDR` are not currently supported by Open Transport (as of version 2.0.3). They will be available in a future release of Open Transport. | |

#### [Apr 26 1999]

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
