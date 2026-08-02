---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/CoreGraphics.html
archived_at: '2026-07-18T02:57:15.288801Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# CoreGraphics Changes for Swift

### CoreGraphics

Removed CGGlypDeprecatedEnum [enum]Removed [CGGlypDeprecatedEnum.GlyphMax](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmax)Removed [CGGlypDeprecatedEnum.GlyphMin](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmin)Added [CGBitmapInfo.FloatInfoMask](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapfloatinfomask)Added CGColorConverterTransformType [enum]Added CGColorConverterTransformType.ApplySpaceAdded CGColorConverterTransformType.FromSpaceAdded CGColorConverterTransformType.ToSpaceAdded [CGGlyphDeprecatedEnum [enum]](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum)Added [CGGlyphDeprecatedEnum.Max](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmax)Added [CGGlyphDeprecatedEnum.Min](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmin)Added CGColorConverterCreateSimple(_: CGColorSpace?, _: CGColorSpace?) -> CGColorConverterRefAdded CGColorConverterGetTypeID() -> CFTypeIDAdded CGColorConverterRefAdded CGColorConverterRelease(_: CGColorConverterRef)Added [kCGColorSpaceDCIP3](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408859-dcip3)Added [kCGColorSpaceDisplayP3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedisplayp3)Modified [CGBitmapInfo [struct]](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct CGBitmapInfo : OptionSetType {     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` |
| To | ``` struct CGBitmapInfo : OptionSetType {     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` |

Modified [CGColor](https://developer.apple.com/documentation/coregraphics/cgcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorRef | ``` typealias CGColorRef = CGColor ``` |
| To | CGColor | ``` class CGColor { } ``` |

Modified [CGColorSpace](https://developer.apple.com/documentation/coregraphics/cgcolorspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceRef | ``` typealias CGColorSpaceRef = CGColorSpace ``` |
| To | CGColorSpace | ``` class CGColorSpace { } ``` |

Modified [CGContext](https://developer.apple.com/documentation/coregraphics/cgcontextref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextRef | ``` typealias CGContextRef = CGContext ``` |
| To | CGContext | ``` class CGContext { } ``` |

Modified [CGDataConsumer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataConsumerRef | ``` typealias CGDataConsumerRef = CGDataConsumer ``` |
| To | CGDataConsumer | ``` class CGDataConsumer { } ``` |

Modified [CGDataProvider](https://developer.apple.com/documentation/coregraphics/cgdataprovider)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderRef | ``` typealias CGDataProviderRef = CGDataProvider ``` |
| To | CGDataProvider | ``` class CGDataProvider { } ``` |

Modified [CGFont](https://developer.apple.com/documentation/coregraphics/cgfontref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontRef | ``` typealias CGFontRef = CGFont ``` |
| To | CGFont | ``` class CGFont { } ``` |

Modified [CGFunction](https://developer.apple.com/documentation/coregraphics/cgfunction)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFunctionRef | ``` typealias CGFunctionRef = CGFunction ``` |
| To | CGFunction | ``` class CGFunction { } ``` |

Modified [CGGradient](https://developer.apple.com/documentation/coregraphics/cggradient)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGGradientRef | ``` typealias CGGradientRef = CGGradient ``` |
| To | CGGradient | ``` class CGGradient { } ``` |

Modified [CGImage](https://developer.apple.com/documentation/coregraphics/cgimage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageRef | ``` typealias CGImageRef = CGImage ``` |
| To | CGImage | ``` class CGImage { } ``` |

Modified [CGLayer](https://developer.apple.com/documentation/coregraphics/cglayer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGLayerRef | ``` typealias CGLayerRef = CGLayer ``` |
| To | CGLayer | ``` class CGLayer { } ``` |

Modified [CGMutablePath](https://developer.apple.com/documentation/coregraphics/cgmutablepathref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGMutablePathRef | ``` typealias CGMutablePathRef = CGMutablePath ``` |
| To | CGMutablePath | ``` class CGMutablePath { } ``` |

Modified [CGPath](https://developer.apple.com/documentation/coregraphics/cgpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathRef | ``` typealias CGPathRef = CGPath ``` |
| To | CGPath | ``` class CGPath { } ``` |

Modified [CGPattern](https://developer.apple.com/documentation/coregraphics/cgpatternref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPatternRef | ``` typealias CGPatternRef = CGPattern ``` |
| To | CGPattern | ``` class CGPattern { } ``` |

Modified [CGPDFDocument](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentRef | ``` typealias CGPDFDocumentRef = CGPDFDocument ``` |
| To | CGPDFDocument | ``` class CGPDFDocument { } ``` |

Modified [CGPDFPage](https://developer.apple.com/documentation/coregraphics/cgpdfpageref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFPageRef | ``` typealias CGPDFPageRef = CGPDFPage ``` |
| To | CGPDFPage | ``` class CGPDFPage { } ``` |

Modified [CGShading](https://developer.apple.com/documentation/coregraphics/cgshadingref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGShadingRef | ``` typealias CGShadingRef = CGShading ``` |
| To | CGShading | ``` class CGShading { } ``` |

Modified [kCGColorSpaceAdobeRGB1998](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceadobergb1998)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceGenericCMYK](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408904-genericcmyk)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceGenericGrayGamma2_2](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408857-genericgraygamma2_2)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCGColorSpaceSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacesrgb)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

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
