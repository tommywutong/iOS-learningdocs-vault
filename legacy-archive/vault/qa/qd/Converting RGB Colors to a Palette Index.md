---
title: Converting RGB Colors to a Palette Index
apple_id: DTS10001780
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd21.html
archived_at: '2026-07-18T02:38:36.502513Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD21Converting RGB Colors to a Palette Index |

|  |
| --- |
| ---   Q: How can I convert an RGB color into an index to a palette created by my application? `Color2Index` converts the RGB color to an index to the current device's color table, but that's not what I want.  A: There's no single call that will give you a palette match to an RGB color. You'll have to do this: call `Color2Index` to get the closest match to your RGB request; call `Index2Color` to get the device's indexed color from your match; search the palette yourself to find the color match (according to RGB value); and call `Color2Index` to verify that you have the color you're looking for.  Alternatively, you can create an off-screen `GWorld`, call `Palette2CTab` to convert your palette to a color table, and call `UpdateGWorld` to insert your new color table in your off-screen `GWorld`. Then, to find the index of an RGB color, make your `GWorld` the active device and call `Color2Index`. |

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
