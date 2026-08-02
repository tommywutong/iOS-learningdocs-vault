---
title: Limitations of the Apple QuickDraw 3D Acceleration Card
apple_id: DTS10001832
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d34.html
archived_at: '2026-07-18T02:38:40.990226Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D34Limitations of the Apple QuickDraw 3D Acceleration Card |

|  |
| --- |
|  Q: What are the limitations of the Apple QuickDraw 3D Acceleration Card?  A: First, note that these limitations only apply the Apple QuickDraw 3D Acceleration Card as of March 1996. Future 3D acceleration technologies, either from Apple or other vendors, may not share these restrictions.   - No more than 12 textures can reside in the card's memory at any one time. - The largest texture size is 256X256 pixels. If the texture is larger than this it will be shrunk and dithered down to 256x256. - Pixel-by-pixel transparency is not supported for textures. - Virtual Memory can adversely affect acceleration. We strongly recommend turning off Virtual Memory when using 3D Acceleration. - Acceleration only works if the monitor is set to display thousands (16 bit pixels) or millions (32 bit pixels) of colors. - The Apple QuickDraw 3D Acceleration Card is a PCI card, thus will only work in Macintoshes with PCI slots. |

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
