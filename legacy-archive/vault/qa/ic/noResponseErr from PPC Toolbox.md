---
title: noResponseErr from PPC Toolbox
apple_id: DTS10001373
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ic/ic02.html
archived_at: '2026-07-18T02:29:40.407974Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Interapplication Communication](https://developer.apple.com/referencelibrary/Carbon/idxInterapplicationCommunication-date.html)

|  |
| --- |
| Technical Q&A IC02noResponseErr from PPC Toolbox |

|  |
| --- |
| ---   Q: Sometimes we receive a `noResponseErr` (-915) from `IPCListPorts`, `PPCStart`, and `StartSecureSession` for no apparent reason. We know we have Program Linking enabled on both systems and that in the case of `PPCStart` and `StartSecureSession`, we have outstanding `PPCInform` requests pending. What does `noResponseErr` mean and what should we do when we receive it?  A: A `noResponseErr` means that the `PLookupName` request that `IPCListPorts`, `PPCStart` or `StartSecureSession` issued failed to get a match. `PLookupName` is being called by the PPC Toolbox with a retry interval of 1 (8-ticks) and a retry count of 12. That means that `PPCStart` tries to find the location for about one and a half seconds. If the server doesn't get a response back to the client in that time, then `PPCStart` will fail with `noResponseErr`.  Usually, that means that the system the PPC Toolbox is trying to contact is very busy (and cannot reply to NBP requests), or that your network is overloaded and the NBP replies are being lost. In either case, you may want to simply retry the PPC call a couple of times before assuming that the other system cannot be reached. |

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
