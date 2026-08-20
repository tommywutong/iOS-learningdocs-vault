---
title: GDHasScale
apple_id: DTS10001922
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm03.html
archived_at: '2026-07-18T02:38:45.623865Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Compression & Decompression](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxCompressionDecompression-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM03GDHasScale |

|  |
| --- |
| GDHasScale returns the closest possible scaling that a particular screen device can be set to in a given pixel depth. It returns scaling information for a particular GDevice for a requested depth. It allows you to query a GDevice without actually changing it. For example, if you specify 0x20000, but the GDevice does not support it, GDHasScale will return with noErr, and a scale of 0x10000. Remember, it checks for a supported depth, so your requested depth must be supported by the GDevice. GDHasScale references the video driver through the graphics device structure.  For multiple screens, see "Multiple Screens Revealed" in _develop_ #10 to find out how to walk the GDeviceList.  pascal OSErr GDHasScale(GDHandle gdh,short depth,Fixed \*scale)  gdh A handle to a screen graphics device.  depth Pixel depth of screen device. Use this field to specify which pixel depth scaling information should be returned for.  scale A pointer to a fixed point scale value. On input, this field should be set to the desired scale value. On output, this field will contain the closest scale available for the given depth. A scale of 0x10000 indicates normal size, 0x20000 indicates double size, and so on.  __Errors__:  cDepthErr The requested depth is not supported.  cDevErr Not a screen device.  controlErr Video driver can not respond to this call.  See also: [QuickTime Technote QT4.](https://developer.apple.com/library/archive/technotes/qt/qt_04.html) [May 01 1995] |

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
