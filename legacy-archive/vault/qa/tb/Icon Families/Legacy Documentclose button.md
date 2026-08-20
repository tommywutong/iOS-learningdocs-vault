---
title: Icon Families
apple_id: DTS10002194
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb08.html
archived_at: '2026-07-18T02:38:55.389617Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB08Icon Families |

|  |
| --- |
| Q We've been doing some conversion between CICNs and icon families, and we've identified some areas where we need some help: 1. Since we created mini icons (12x16), any icons we try to plot that are smaller (10x10, for example) appear compressed horizontally unless we specify a size of 10x13. Is there any way to avoid this?  2. Is it possible to create icons of other sizes (such as 10x10 or 24x24) and make them part of the icon family, or is scaling down larger icons our only choice?  3. When we used CICNs, we were able to use non-standard icon colors and still see a visible effect when we tried to show labeling or selection. The icon families don't seem to support this unless we use the standard icon colors. Is there a way around this? A Your icons must occupy a 32x32-bit rectangle, or if you're using families, a 16x16-bit rectangle. This doesn't mean that you can't have smaller icons, since you can have a 24x24-bit icon that occupies a 32x32-bit rectangle or a 10x10-bit icon that occupies a 16x16-bit rectangle. The Apple standard icon colors were chosen for fast highlighting. There are icon-dimming code examples on the Developer CDs, but these are slower than the system routines. As you've discovered, the system routines are limited to the standard set of colors. You can use any colors you like, but if you use colors other than the standard colors, the highlighting won't look the way you expect it to.  There is additional information relating to the Icon Utilities in Chapter 5 of Inside Macintosh: More Macintosh Toolbox. In addition to being available in printed form, this publication can be found on the Developer CD Series: Reference Library edition. [May 01 1995] |

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
