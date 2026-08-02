---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CoreGraphics.html
archived_at: '2026-07-18T02:54:54.653755Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreGraphics Changes for Objective-C

### CoreGraphics

#### CGBase.h

Added #def cg_nullableAdded [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref)

#### CGColorConversionInfo.h (Added)

Added [CGColorConversionInfoCreate()](https://developer.apple.com/documentation/coregraphics/2113677-cgcolorconversioninfocreate)Added [CGColorConversionInfoCreateFromList()](https://developer.apple.com/documentation/coregraphics/2118077-cgcolorconversioninfocreatefroml)Added [CGColorConversionInfoGetTypeID()](https://developer.apple.com/documentation/coregraphics/2113681-cgcolorconversioninfogettypeid)Added [CGColorConversionInfoRef](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninforef)Added [CGColorConversionInfoTransformType](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype)Added [kCGColorConversionBlackPointCompensation](https://developer.apple.com/documentation/coregraphics/kcgcolorconversionblackpointcompensation)Added [kCGColorConversionTransformApplySpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/kcgcolorconversiontransformapplyspace)Added [kCGColorConversionTransformFromSpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/kcgcolorconversiontransformfromspace)Added [kCGColorConversionTransformToSpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/kcgcolorconversiontransformtospace)

#### CGColorConverter.h (Removed)

Removed CGColorConverterCreate()Removed CGColorConverterCreateSimple()Removed CGColorConverterGetTypeID()Removed CGColorConverterRefRemoved CGColorConverterRelease()Removed CGColorConverterTransformTypeRemoved kCGColorConverterTransformApplySpaceRemoved kCGColorConverterTransformFromSpaceRemoved kCGColorConverterTransformToSpace

#### CGColorSpace.h

Added [CGColorSpaceCopyICCData()](https://developer.apple.com/documentation/coregraphics/1644732-cgcolorspacecopyiccdata)Added [CGColorSpaceCopyName()](https://developer.apple.com/documentation/coregraphics/1408903-cgcolorspacecopyname)Added [CGColorSpaceIsWideGamutRGB()](https://developer.apple.com/documentation/coregraphics/1644737-cgcolorspaceiswidegamutrgb)Added [CGColorSpaceSupportsOutput()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1690958-supportsoutput)Added [kCGColorSpaceExtendedGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceextendedgray)Added [kCGColorSpaceExtendedLinearGray](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1690959-extendedlineargray)Added [kCGColorSpaceExtendedLinearSRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1690961-extendedlinearsrgb)Added [kCGColorSpaceExtendedSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceextendedsrgb)Added [kCGColorSpaceLinearGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspacelineargray)Added [kCGColorSpaceLinearSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacelinearsrgb)Modified [kCGColorSpaceDisplayP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedisplayp3)

|  | Introduction |
| --- | --- |
| From | iOS 9.0 |
| To | iOS 9.3 |

#### CGImage.h

Added [CGImageByteOrderInfo](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo)Added [kCGImageByteOrder16Big](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteorder16big)Added [kCGImageByteOrder16Little](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteorder16little)Added [kCGImageByteOrder32Big](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteorder32big)Added [kCGImageByteOrder32Little](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/order32little)Added [kCGImageByteOrderMask](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteordermask)

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
