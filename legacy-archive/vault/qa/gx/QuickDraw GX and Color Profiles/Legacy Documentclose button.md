---
title: QuickDraw GX and Color Profiles
apple_id: DTS10001208
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gx/gx03.html
archived_at: '2026-07-18T02:29:30.845290Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX03QuickDraw GX and Color Profiles |

|  |
| --- |
| ---   Q: Do I need to call `GXCloneColorProfile` before calling `GXConvertColor`? Since the color passed into `GXConvertColor` by ColorSync is destroyed, should the color profile passed in as part of the color be disposed? If not, isn't that a memory leak?  A: Calling `GXCloneColorProfile` is not necessary, and it would require additional work that does not need to be done. `gxColor` is a public data structure, not an object. The application, not GX, handles adding/maintaining references to objects with respect to `gxColor`'s (and `gxBitmaps`). GX maintains owner counts when the profile is attached to another GX object (using `GXNewBitmap`, `GXSetInkColor`, etc.). This is not a memory leak.  For example, consider this scenario:  When an application gets a shape's color, the ink's profile has two owners -- the shape and the application. Therefore, the application can reference the profile in `gxColor` structures, even if the shape is disposed. Once the application calls `GXDisposeColorProfile`, the reference is no longer valid. Cloning the color profile does nothing except to require that `GXDisposeColorProfile` be called afterward. As a result, all that happens is that time is wasted as the owner count goes from a positive number to that number plus 1, and then back down. |

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
