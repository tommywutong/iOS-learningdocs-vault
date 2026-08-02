---
title: Receiving UDP Broadcasts While Sending from a Secondary Address
apple_id: DTS10001479
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-05-08'
source_url: https://developer.apple.com/library/archive/qa/nw/nw67.html
archived_at: '2026-07-18T02:29:48.021420Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW67Receiving UDP Broadcasts While Sending from a Secondary Address |

|  |
| --- |
| ---   Q: I'm writing an application that needs to receive UDP broadcasts. I also want to send unicast replies; however, when running on a single-link multi-homed machine, I want to control the source IP address from which the replies originate. How do I do this?  A: To listen to UDP broadcasts (and multicasts), you must create an endpoint and bind it to `kOTAnyInetAddress` (0.0.0.0). If you send your unicast replies from the same endpoint, the replies will have their source address set to the default IP address of the interface from which the packets were sent. To get around this, you must create an endpoint for each possible source address, bind the endpoint to the corresponding IP address, and then send the packet using the appropriate endpoint.  If you wish to send and receive on the same port number, you must set the [IP_REUSEADDR](https://developer.apple.com/qa/nw/nw28.html) option on each endpoint before binding it. This prevents `OTBind` from returning the `kOTAddressBusyErr` error.  The only gotcha here is that if someone unicasts a packet to one of your IP addresses, the corresponding sending endpoint will receive it. Your sending endpoints must be prepared for this; typically, they either discard the packet or pass it to the logic used for the receiving endpoint. |

#### [May 08 2000]

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
