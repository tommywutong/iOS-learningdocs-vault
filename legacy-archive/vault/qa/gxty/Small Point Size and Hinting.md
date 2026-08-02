---
title: Small Point Size and Hinting
apple_id: DTS10001268
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty09.html
archived_at: '2026-07-18T02:29:34.879451Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXTY09Small Point Size and Hinting |

|  |
| --- |
| ---   Q: I am having a problem, apparent at very small font sizes (6 points and below), with the output quality of some fonts that emerge from a GX vector driver.  My application uses `gxLayouts` for text display and editing. If I create my output using `GXDrawShape` to render the layout shapes, the small characters begin to look very crude: character height varies by about 30% between some letters and curved letterforms degenerate to rough polygons.  A: Layouts (like all typographic shapes) have hints turned on by default. If the font you're using isn't hinted at small point sizes, using hints messes up the appearance of the text, rather than helping it (as they should). Try using the layout shape and setting the `gxNoMetricsGridText` and `gxNoContourGridText` bits on in the `textAttributes`. The results at small sizes should be better. |

#### [Apr 08 1996]

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
