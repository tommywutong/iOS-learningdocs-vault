---
title: Problems with DiffRgn
apple_id: DTS10001784
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd25.html
archived_at: '2026-07-18T02:38:36.703887Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD25Problems with DiffRgn |

|  |
| --- |
| ---   Q: I'm having a bit of a problem with `DiffRgn`. I start out with a "wide open" rectangular region (-32767, -32767, 32767, 32767) and then use `DiffRgn` to subtract a group of smaller rectangles from it. When I'm done, the bounding box of the region isn't what it should be. Any idea what's happening?  A: What you need to do is create your clipping region so that it's not quite wide open (bottom and right coordinates of 32766 will work). If you do this, all your `DiffRgn` calculations will work fine.  While this isn't explicitly documented anywhere, it does seem to be a quirk in the way regions work. Due to the internal storage format of regions, the number `0x7FFF` (32767) causes problems if it appears as a point inside a region. `0x7FFF` is used as a flag in the internal region data structure to signify a "barrier." When this flag is used as a data point in a nonrectangular region, region parsing becomes completely screwed up.  QuickDraw tries to catch the creation of regions that will be poorly formed and turn them into properly formed (but slightly incorrect) regions, but it isn't 100% successful. |

#### [Sep 15 1995]

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
