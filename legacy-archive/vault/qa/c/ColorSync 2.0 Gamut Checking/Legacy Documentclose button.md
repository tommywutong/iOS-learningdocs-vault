---
title: ColorSync 2.0 Gamut Checking
apple_id: DTS10001132
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/c/cs04.html
archived_at: '2026-07-18T02:29:24.541118Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A CS04ColorSync 2.0 Gamut Checking |

|  |
| --- |
| ---   Q: I'm using `CMCheckBitmap()` API to do gamut checking in a plug-in for Photoshop. The result bitmap is not what I expected. Here's the scenario:  The source profile is a typical monitor profile, and the destination profile (for the gamut check) has the data-color space of CMY and the `interchangeSpace` of Lab. The gamut tag was set to have three identity-input channels, a CLUT , and one output channel, which sets everything to be inside the gamut. Since the gamut was set to be "all in gamut," the result image should be all in gamut (0). However, The result image which came from `CMCheckBitmap()` was not all in gamut, and the result image varies each time the gamut check is performed.  Do you have any idea what would cause this problem? Also, does the leftmost bit of byte 0 contain the gamut for the first pixel of the source image? Please elaborate on the format of the result image?  A: `CMCheckBitmap` sets each pixel in the result bitmap to black if the corresponding pixel in the source bitmap is out of the gamut. However, `CMCheckBitmap` does not set each pixel in the result bitmap to white if the pixel in the source bitmap is in the gamut. For this reason, be sure to erase the result bitmap to white before calling `CMCheckBitmap`. (This is also true of `CheckPixMap` and `CheckColors`.)  It could be that you are incorrectly allocating the bitmaps or misinterpreting the result bitmap. You are correct that the high-bit of byte 0 of the bitmap-image data contains the gamut for the first pixel of the source image, because the pixelSize of the result bitmap is 1.  If neither of the above are causing the problem, there may be something strange about your profile's gamut tags. To confirm this, try using the `CSDemo` application on the SDK to test the profile. To do this, open a PICT file, open your profile, select "Make Printer Profile" from the "Profiles" menu, check the "ColorSync" checkbox in the PICT window, and select "Gamut Check" from the "Mode" popup. |

#### [Aug 01 1995]

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
