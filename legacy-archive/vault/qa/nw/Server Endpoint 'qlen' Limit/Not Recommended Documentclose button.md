---
title: Server Endpoint 'qlen' Limit
apple_id: DTS10001450
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/nw/nw38.html
archived_at: '2026-07-18T02:29:46.250839Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW38Server Endpoint 'qlen' Limit |

|  |
| --- |
| ---   Q: I'm writing an Open Transport server product and will be implementing handoff endpoints. What is the maximum '`qlen`' value that limits the number of handoff endpoints that can be implemented?  A: There is a maximum '`qlen`' value for each protocol, but maximum values which are true today for Open Transport may change in the future, so I recommend that you set the '`qlen`' value to a desired value. If the desired value is greater than the number of handoff endpoints that the underlying protocol can support, the protocol can specify its own maximum '`qlen`' value for the server endpoint. After making the `OTBind` call, take a look at the '`qlen`' field of the `TBind` structure, `retAddr`, to see whether the protocol imposed a limit on the '`qlen`' value. |

#### [Aug 21 1996]

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
