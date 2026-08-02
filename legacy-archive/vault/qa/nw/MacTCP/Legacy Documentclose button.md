---
title: MacTCP
apple_id: DTS10001420
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw08.html
archived_at: '2026-07-18T02:29:44.332249Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW08MacTCP |

|  |
| --- |
| ---   Q: We use two versions of MacTCP in-house: 2.0.4 and 2.0.6. We are experiencing an annoying bug in both versions -- IP Pings do not work properly on a class- C address when the subnet mask is set to 255.255.255.192. All other packets work, and we can also make IP Pings work by changing the subnet mask to 255.255.255.128, but we can't operate with the subnet mask at this setting.  A: The problem you're observing may be caused by a known bug in MacTCP, which incorrectly assumes that certain host addresses are broadcast addresses, based on the address class and the subnet mask. To determine if this is the same bug, monitor the line to see if there's an ICMP redirect being sent. Since ICMP does not respond to a broadcast source address, the absence of redirects would indicate this is being caused by the same bug. |

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
