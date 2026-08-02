---
title: Custom Designing a GX Font
apple_id: DTS10001270
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-07-03'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty11.html
archived_at: '2026-07-18T02:29:34.970716Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXTY11Custom Designing a GX Font |

|  |
| --- |
| ---   Q: I want to turn my font (generated with a third-party product) into a true GX font with a customized features menu, not just GXify it.  How did font developers (Apple, Linotype, ITC, etc.) create their GX fonts? What programs are available for GX font design? Would I be able to add a features menu to my font _after_ generating it with the third-party product?  A: For custom design of GX features in a font you should use TrueEdit, available at[Apple's Font Tools site](http://fonts.apple.com/) and on the Developer CD Series : MacOS SDK Edition in the QuickDraw GX folder.  The general process of designing a GX font starts with building all the glyphs you're interested in and hinting them, just as you would for a non-GX font. Once you have the glyph repertoire, use TrueEdit to add all the GX tables. You should be able to add the tables for the various manu features with TrueEdit just fine after you have built the font with a third-party product. |

#### [Jul 03 1996]

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
