---
title: Printing Finder Icons
apple_id: DTS10001791
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd32.html
archived_at: '2026-07-18T02:38:37.140278Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| Technical Q&A QD32Printing Finder Icons |

|  |  |
| --- | --- |
| ---   Q: In writing a print driver, I've noticed that when I print a window from the Finder, the icons don't show up. What gives?  A: What you've uncovered is an "optimization" in the Icon Utilities. When drawing an icon, rather than going through the standard bottlenecks, the Icon Utilities use `CopyMask`. This is true unless you're saving to a pict or drawing to a port they recognize as a printing port (by the print driver setting a low-memory global, which is underdocumented).  The following two macros tell the Icon Utilities to use `CopyBits` instead of using `CopyMask`. Call `setPrinting` in your `PrOpenPage` function and call `clearPrinting` in your `PrClosePage` function, and all should be well.   |  | | --- | | ``` #define setPrinting {*((short *)0x948) = 0;} #define clearPrinting {*((short *)0x948) = -1;} ``` | |

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
