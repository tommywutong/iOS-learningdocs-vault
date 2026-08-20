---
title: System Error 119
apple_id: DTS10001507
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/ops/ops26.html
archived_at: '2026-07-18T02:29:50.346226Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS26System Error 119 |

|  |
| --- |
| ---   Q: My customers report that my application is crashing with system error `119`. What does it mean?  A: This error, defined in Errors.h as `dsMustUseFCBAccessors`, was introduced in Mac OS 9.0. In order for Apple to increase the maximum number of open files, we had to change the FCB structure and thus its length.  Software that calls the PowerPC low-memory accessor functions for the FCB table will now halt the system with this `dsMustUseFCBAccessors` (119) system error. Developers needing to access FCB data should do so using the appropriate routines, as described in DTS Technote [TN 1184, “FCBs, Now and Forever.”](https://developer.apple.com/library/archive/technotes/tn/tn1184.html) Updated: 5-October-1999 |

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
