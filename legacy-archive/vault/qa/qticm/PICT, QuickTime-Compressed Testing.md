---
title: PICT, QuickTime-Compressed Testing
apple_id: DTS10001928
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm09.html
archived_at: '2026-07-18T02:38:45.899798Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM09PICT, QuickTime-Compressed Testing |

|  |
| --- |
| If the picture contains any QuickTime-compressed images, the images will need to pass through the StdPix bottleneck. This is a new graphics routine introduced by QuickTime. Unlike standard QuickDraw images, which only call StdBits, QuickTime-compressed images need to be decompressed first in the StdPix routine. QuickDraw uses StdBits to render the decompressed image. Swap out the QuickDraw bottlenecks and place code in the StdPix routine. If this code is called when you call DrawPicture, you know you have a compressed picture. To determine the type of compression, you can access the image description using GetCompressedPixMapInfo. The cType field of the ImageDescription record will give you the codec type. See the CollectPictColors snippet and "Inside QuickTime and Component-Based Managers" in _develop_ Issue 13, specifically pages 46 and 47, for more information on swapping out the bottlenecks. [May 01 1995] |

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
