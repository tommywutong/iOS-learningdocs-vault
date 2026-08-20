---
title: Problem with PaintRgn on 256-color Screens
apple_id: DTS10001782
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd23.html
archived_at: '2026-07-18T02:38:36.608470Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD23Problem with PaintRgn on 256-color Screens |

|  |
| --- |
| ---   Q: In our application, the user can select an area of an image and drag it around. I want to show this visually by inverting the region under the current mouse coordinate as the user moves the mouse around. Inverting the region is nice because I can invert it again to get the unselected pixels back. It's not nice, however, in that a 50% gray color looks the same when it's inverted. To fix this problem, I tried using `PaintRgn` with an `RGBForeColor` of r,g,b = 0x8000 and a transfer mode of `addOver`. This works great on 24-bit screens, but it seems that on 256-color screens, applying this operation twice doesn't quite return to the original color. Am I going to have to use a custom color search procedure?  A: You get the results you want on direct devices but not on indexed ones, and unless you're extremely lucky with your color table, this is how it will always work. The problem is that the mode calculations are done with the actual RGB values used (the ones available in the color table), not the ones you request. On indexed devices there's almost always a difference between the two, so unless your color table happens to have the exact color you request, there will be "errors." This never happens on direct devices because all colors are available - the operations work on direct RGB values and are never mapped through color tables.  The solution is either to set up your color tables or palettes to make sure you get the results you want each time, or to install a custom color search procedure if that's what you'd prefer. |

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
