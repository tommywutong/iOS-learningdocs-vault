---
title: Unbinding from a TCP Port
apple_id: DTS10001429
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw17.html
archived_at: '2026-07-18T02:29:44.801335Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW17Unbinding from a TCP Port |

|  |
| --- |
| ---   Q: After unbinding from a TCP port, I am sometimes unable to do anything with that port until I reboot. This happens in both native OpenTransport API and MacTCP emulation. What gives?  A: OpenTranport TCP makes that port busy for a period of time long enough (about 2 minutes) for any remote connections to time out before you can bind to it again. This is done to prevent any stale connections from corrupting new ones.  You will notice that even though your next `OTBind` to that port was successful, the address returned wasn't what you asked for, because of the lag. The X/Open spec states that you have to explicitly check the address returned.  Although a MacTCP emulation should return a `duplicateSocket` error, on some older version of OT it doesn't; you should check the address returned when using MacTCP, too.  The bottom line is: always check your returned address.  If you are using the native Open Transport API, there is a way around the two-minute delay. You can issue an option management call before you do the bind to enable the `IP_REUSEADDR` option.  Be aware, though, that with the `IP_REUSEADDR` option, at most only one endpoint in an unconnected state (i.e., listening) may be bound to a port. There may be more endpoints, however, _already_ connected or closing, which are bound to the same port.  See _X/OpenTransport Interface_ for further documentation. |

#### [Nov 01 1995]

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
