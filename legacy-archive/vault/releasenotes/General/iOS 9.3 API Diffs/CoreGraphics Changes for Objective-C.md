---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Objective-C/CoreGraphics.html
archived_at: '2026-07-18T02:57:13.292543Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# CoreGraphics Changes for Objective-C

### CoreGraphics

#### CGColorConverter.h (Added)

Added CGColorConverterCreate()Added CGColorConverterCreateSimple()Added CGColorConverterGetTypeID()Added CGColorConverterRefAdded CGColorConverterRelease()Added CGColorConverterTransformTypeAdded kCGColorConverterTransformApplySpaceAdded kCGColorConverterTransformFromSpaceAdded kCGColorConverterTransformToSpace

#### CGColorSpace.h

Added [kCGColorSpaceDCIP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedcip3)Added [kCGColorSpaceDisplayP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedisplayp3)Modified [kCGColorSpaceAdobeRGB1998](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408865-adobergb1998)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceGenericCMYK](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408904-genericcmyk)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceGenericGrayGamma2_2](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgraygamma2_2)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceSRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408871-srgb)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

#### CGFont.h

Removed CGGlypDeprecatedEnumAdded [CGGlyphDeprecatedEnum](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum)

#### CGImage.h

Added [kCGBitmapFloatInfoMask](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapfloatinfomask)

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
