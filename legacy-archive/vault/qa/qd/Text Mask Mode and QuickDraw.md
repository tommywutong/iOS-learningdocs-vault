---
title: Text Mask Mode and QuickDraw
apple_id: DTS10001911
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-07'
source_url: https://developer.apple.com/library/archive/qa/qd/qd58.html
archived_at: '2026-07-18T02:38:38.570049Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD58Text Mask Mode and QuickDraw |

|  |
| --- |
| ---   Q: The "Text Mask Mode" section on p. 3-26 of [_Inside Macintosh: Text_](https://developer.apple.com/documentation/mac/Text/Text-137.html#HEADING137-30) describes a constant "mask" which is supposed to allow one to apply only the glyph portion of the font to the destination. This constant seems to be missing from Universal Interfaces 3.1. Why?  A: The value for the "mask" constant can be found in the Macintosh Toolbox Assistant. Unfortunately, it is defined as 64, which collides with the value for `ditherCopy`. After some investigations, it has been determined that the "mask" constant has limited support in recent versions of the Mac OS. Therefore, with the release of Mac OS 8.5, Apple will no longer support the "mask" mode. We recommend that any developer who requires the "mask" mode functionality use an offscreen with `BitmapToRegion()` and `CopyBits()` instead. |

#### [Sep 07 1998]

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
