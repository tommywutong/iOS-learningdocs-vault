---
title: QD3D Windows Pixel Format Support
apple_id: DTS10001881
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d83.html
archived_at: '2026-07-18T02:38:44.672372Z'
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
| Technical Q&A QD3D83QD3D Windows Pixel Format Support |

|  |
| --- |
| ---   Q: I get the `kQ3ErrorUnimplemented` result code after a call to the `Q3PixmapTexture_New` function under Windows 95. I have tried two pixels formats for Windows: `kQ3PixelTypeRGB16_565` and `kQ3PixelTypeRGB24`. Are these not supported under QuickDraw 3D 1.5?  A: QD3D only supports texture maps and mipmaps in 5-5-5 16-bit formats (`kQ3PixelTypeARGB16` and `kQ3PixelTypeRGB16`) and 32-bit formats (`kQ3PixelTypeARGB32` and `kQ3PixelTypeRGB32`). This true for both the Mac OS and Windows versions. Texture maps must be cross-platform to be supported by 3DMF. So the same types have to be supported on all platforms.  The `kQ3PixelTypeRGB16_565` and `kQ3PixelTypeRGB24` pixel types are only valid for Pixmap Draw Contexts on Windows and are not supported for Pixmap Draw Contexts on Mac OS.  Additionally, dynamically created pixmaps for Draw Context, Textures, Markers or Mipmaps must be created with the byte-endianness appropriate for the current platform (`kQ3EndianLittle` for Windows and `kQ3EndianBig` for Mac OS). The byte-endianness of Pixmaps, Mipmaps, and Markers in 3DMF files gets translated automatically by the library when loading a 3DMF created on a different endian platform. [Jul 11 1997] |

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
