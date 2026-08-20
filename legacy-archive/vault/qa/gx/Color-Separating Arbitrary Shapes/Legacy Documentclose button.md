---
title: Color-Separating Arbitrary Shapes
apple_id: DTS10001214
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/gx/gx09.html
archived_at: '2026-07-18T02:29:32.005332Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX09Color-Separating Arbitrary Shapes |

|  |  |
| --- | --- |
| ---   Q: I'm trying to color-separate arbitrary shapes. For example, to make the cyan plate, I want to take the shape's color, convert it to `gxCMYKspace`, then replace the black component with the cyan one, and zero out the others.  This is fairly easy to do for simple shapes, but bitmaps are going to give me problems. I need to find a way to convert a bitmap from one color space to another without changing its visual appearance (in other words, the pixel values have to change to reflect a `GXConvertColor` on them).  Is there a way to do this without traversing the whole bitmap "by hand"?  A: Using a transfer mode will do the trick for bitmaps, but it probably won't be all that speedy (it also probably won't be any worse than your slow alternative of traversing the bitmap by hand).  Transfer modes allow you to specify 5x4 matrices that specify which color component of the source gets mapped to which color component of the destination.  The easiest way to set up a transfer mode is to get the existing mode and then modify it as follows:  In the `gxTransferMode` struct:   1. Set space to `gxCMYKSpace`. 2. Then to copy cyan to black, set the `sourceMatrix` to     |  |    | --- |    | ``` [       0       0       0       1         0       0       0       0         0       0       0       0         0       0       0       0         0       0       0       0       ] ``` |   See Also:  - Pages 5-33 and 34 in _Inside Macintosh: QuickDraw GX Objects_ has further   details on Transfer Mode matrices. |

#### [Jun 11 1996]

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
