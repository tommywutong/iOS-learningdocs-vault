---
title: Fixed Math Rounding
apple_id: DTS10001501
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/ops/ops20.html
archived_at: '2026-07-18T02:29:50.074285Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS20Fixed Math Rounding |

|  |
| --- |
| ---   Q: When I call `FixMul` (3, 1 << 15) (3\*0.5), the result is 2, but `FixMul` (-3, 1 << 15) yields a result of -1. Furthermore, on 68K Macs `FixMul` (-3, 1 << 15) yields a result of -2. What's going on?  A: This has to do with the rounding needed to make QuickDraw work correctly on PowerPC-based Macintoshes. The Fixed math routines round up, which in the case of negative numbers is towards zero, so -1.5 rounds to -1, and 1.5 rounds to 2.  This behavior is not going to change, and if this causes problems, you will either need to write your own Fixed math routines or wrap the Apple ones to account for the different rounding direction. Updated: 17-May-1999 |

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
