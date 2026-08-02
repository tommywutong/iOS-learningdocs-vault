---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreGraphics.html
archived_at: '2026-07-18T02:56:31.644939Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreGraphics Changes for Objective-C

### CoreGraphics

#### CGBitmapContext.h

Modified [CGBitmapContextCreate()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGBitmapContextCreate (     void *data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo ); ``` |
| To | ``` CGContextRef _Nullable CGBitmapContextCreate (     void * _Nullable data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     uint32_t bitmapInfo ); ``` |

Modified [CGBitmapContextCreateWithData()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454984-init)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGBitmapContextCreateWithData (     void *data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo,     CGBitmapContextReleaseDataCallback releaseCallback,     void *releaseInfo ); ``` |
| To | ``` CGContextRef _Nullable CGBitmapContextCreateWithData (     void * _Nullable data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     uint32_t bitmapInfo,     CGBitmapContextReleaseDataCallback _Nullable releaseCallback,     void * _Nullable releaseInfo ); ``` |

#### CGColor.h

Added [CGColorCreateCopyByMatchingToColorSpace()](https://developer.apple.com/documentation/coregraphics/1455493-cgcolorcreatecopybymatchingtocol)Modified [CGColorCreate()](https://developer.apple.com/documentation/coregraphics/1455927-cgcolorcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreate (     CGColorSpaceRef space,     const CGFloat components[] ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreate (     CGColorSpaceRef _Nullable space,     const CGFloat * _Nullable components ); ``` |

Modified [CGColorCreateWithPattern()](https://developer.apple.com/documentation/coregraphics/cgcolor/1455687-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateWithPattern (     CGColorSpaceRef space,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreateWithPattern (     CGColorSpaceRef _Nullable space,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

#### CGColorSpace.h

Added [CGColorSpaceCreateWithPlatformColorSpace()](https://developer.apple.com/documentation/coregraphics/1408850-cgcolorspacecreatewithplatformco)Added [kCGColorSpaceACESCGLinear](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408841-acescglinear)Added [kCGColorSpaceAdobeRGB1998](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408865-adobergb1998)Added [kCGColorSpaceGenericCMYK](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408904-genericcmyk)Added [kCGColorSpaceGenericGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgray)Added [kCGColorSpaceGenericGrayGamma2_2](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgraygamma2_2)Added [kCGColorSpaceGenericRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgb)Added [kCGColorSpaceGenericRGBLinear](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408893-genericrgblinear)Added [kCGColorSpaceGenericXYZ](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408844-genericxyz)Added [kCGColorSpaceITUR_2020](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408901-itur_2020)Added [kCGColorSpaceITUR_709](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408906-itur_709)Added [kCGColorSpaceROMMRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacerommrgb)Added [kCGColorSpaceSRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408871-srgb)

#### CGContext.h

Modified [CGContextAddEllipseInRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456420-addellipse)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextAddEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextAddLines()](https://developer.apple.com/documentation/coregraphics/1455461-cgcontextaddlines)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddLines (     CGContextRef c,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGContextAddLines (     CGContextRef _Nullable c,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGContextAddPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456628-addpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddPath (     CGContextRef context,     CGPathRef path ); ``` |
| To | ``` void CGContextAddPath (     CGContextRef _Nullable c,     CGPathRef _Nullable path ); ``` |

Modified [CGContextAddRects()](https://developer.apple.com/documentation/coregraphics/1454734-cgcontextaddrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextAddRects (     CGContextRef _Nullable c,     const CGRect * _Nullable rects,     size_t count ); ``` |

Modified [CGContextBeginTransparencyLayer()](https://developer.apple.com/documentation/coregraphics/1456011-cgcontextbegintransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginTransparencyLayer (     CGContextRef context,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` void CGContextBeginTransparencyLayer (     CGContextRef _Nullable c,     CFDictionaryRef _Nullable auxiliaryInfo ); ``` |

Modified [CGContextBeginTransparencyLayerWithRect()](https://developer.apple.com/documentation/coregraphics/1454368-cgcontextbegintransparencylayerw)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginTransparencyLayerWithRect (     CGContextRef context,     CGRect rect,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` void CGContextBeginTransparencyLayerWithRect (     CGContextRef _Nullable c,     CGRect rect,     CFDictionaryRef _Nullable auxInfo ); ``` |

Modified [CGContextClipToRects()](https://developer.apple.com/documentation/coregraphics/1454626-cgcontextcliptorects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClipToRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextClipToRects (     CGContextRef _Nullable c,     const CGRect * _Nonnull rects,     size_t count ); ``` |

Modified [CGContextConvertPointToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455916-converttodevicespace)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextConvertPointToDeviceSpace (     CGContextRef context,     CGPoint point ); ``` |
| To | ``` CGPoint CGContextConvertPointToDeviceSpace (     CGContextRef _Nullable c,     CGPoint point ); ``` |

Modified [CGContextConvertPointToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456451-converttouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextConvertPointToUserSpace (     CGContextRef context,     CGPoint point ); ``` |
| To | ``` CGPoint CGContextConvertPointToUserSpace (     CGContextRef _Nullable c,     CGPoint point ); ``` |

Modified [CGContextConvertRectToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextConvertRectToDeviceSpace (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` CGRect CGContextConvertRectToDeviceSpace (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextConvertRectToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454165-converttouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextConvertRectToUserSpace (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` CGRect CGContextConvertRectToUserSpace (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextConvertSizeToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CGContextConvertSizeToDeviceSpace (     CGContextRef context,     CGSize size ); ``` |
| To | ``` CGSize CGContextConvertSizeToDeviceSpace (     CGContextRef _Nullable c,     CGSize size ); ``` |

Modified [CGContextConvertSizeToUserSpace()](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CGContextConvertSizeToUserSpace (     CGContextRef context,     CGSize size ); ``` |
| To | ``` CGSize CGContextConvertSizeToUserSpace (     CGContextRef _Nullable c,     CGSize size ); ``` |

Modified [CGContextCopyPath()](https://developer.apple.com/documentation/coregraphics/1455397-cgcontextcopypath)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGContextCopyPath (     CGContextRef context ); ``` |
| To | ``` CGPathRef _Nullable CGContextCopyPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextDrawLinearGradient()](https://developer.apple.com/documentation/coregraphics/1454782-cgcontextdrawlineargradient)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawLinearGradient (     CGContextRef context,     CGGradientRef gradient,     CGPoint startPoint,     CGPoint endPoint,     CGGradientDrawingOptions options ); ``` |
| To | ``` void CGContextDrawLinearGradient (     CGContextRef _Nullable c,     CGGradientRef _Nullable gradient,     CGPoint startPoint,     CGPoint endPoint,     CGGradientDrawingOptions options ); ``` |

Modified [CGContextDrawRadialGradient()](https://developer.apple.com/documentation/coregraphics/1455923-cgcontextdrawradialgradient)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawRadialGradient (     CGContextRef context,     CGGradientRef gradient,     CGPoint startCenter,     CGFloat startRadius,     CGPoint endCenter,     CGFloat endRadius,     CGGradientDrawingOptions options ); ``` |
| To | ``` void CGContextDrawRadialGradient (     CGContextRef _Nullable c,     CGGradientRef _Nullable gradient,     CGPoint startCenter,     CGFloat startRadius,     CGPoint endCenter,     CGFloat endRadius,     CGGradientDrawingOptions options ); ``` |

Modified [CGContextDrawShading()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456643-drawshading)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawShading (     CGContextRef context,     CGShadingRef shading ); ``` |
| To | ``` void CGContextDrawShading (     CGContextRef _Nullable c,     CGShadingRef _Nullable shading ); ``` |

Modified [CGContextEndTransparencyLayer()](https://developer.apple.com/documentation/coregraphics/1456554-cgcontextendtransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextEndTransparencyLayer (     CGContextRef context ); ``` |
| To | ``` void CGContextEndTransparencyLayer (     CGContextRef _Nullable c ); ``` |

Modified [CGContextFillEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1454371-cgcontextfillellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextFillEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextFillRects()](https://developer.apple.com/documentation/coregraphics/1454132-cgcontextfillrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextFillRects (     CGContextRef _Nullable c,     const CGRect * _Nullable rects,     size_t count ); ``` |

Modified [CGContextGetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1454940-cgcontextgetinterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` CGInterpolationQuality CGContextGetInterpolationQuality (     CGContextRef context ); ``` |
| To | ``` CGInterpolationQuality CGContextGetInterpolationQuality (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetPathBoundingBox()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454577-boundingboxofpath)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextGetPathBoundingBox (     CGContextRef context ); ``` |
| To | ``` CGRect CGContextGetPathBoundingBox (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetPathCurrentPoint()](https://developer.apple.com/documentation/coregraphics/1454788-cgcontextgetpathcurrentpoint)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextGetPathCurrentPoint (     CGContextRef context ); ``` |
| To | ``` CGPoint CGContextGetPathCurrentPoint (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetTextPosition()](https://developer.apple.com/documentation/coregraphics/1454687-cgcontextgettextposition)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextGetTextPosition (     CGContextRef context ); ``` |
| To | ``` CGPoint CGContextGetTextPosition (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetUserSpaceToDeviceSpaceTransform()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455677-userspacetodevicespacetransform)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform (     CGContextRef context ); ``` |
| To | ``` CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform (     CGContextRef _Nullable c ); ``` |

Modified [CGContextIsPathEmpty()](https://developer.apple.com/documentation/coregraphics/1455772-cgcontextispathempty)

|  | Declaration |
| --- | --- |
| From | ``` bool CGContextIsPathEmpty (     CGContextRef context ); ``` |
| To | ``` bool CGContextIsPathEmpty (     CGContextRef _Nullable c ); ``` |

Modified [CGContextPathContainsPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454778-pathcontains)

|  | Declaration |
| --- | --- |
| From | ``` bool CGContextPathContainsPoint (     CGContextRef context,     CGPoint point,     CGPathDrawingMode mode ); ``` |
| To | ``` bool CGContextPathContainsPoint (     CGContextRef _Nullable c,     CGPoint point,     CGPathDrawingMode mode ); ``` |

Modified [CGContextSetAllowsAntialiasing()](https://developer.apple.com/documentation/coregraphics/1456310-cgcontextsetallowsantialiasing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsAntialiasing (     CGContextRef context,     bool allowsAntialiasing ); ``` |
| To | ``` void CGContextSetAllowsAntialiasing (     CGContextRef _Nullable c,     bool allowsAntialiasing ); ``` |

Modified [CGContextSetAllowsFontSmoothing()](https://developer.apple.com/documentation/coregraphics/1454767-cgcontextsetallowsfontsmoothing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSmoothing (     CGContextRef context,     bool allowsFontSmoothing ); ``` |
| To | ``` void CGContextSetAllowsFontSmoothing (     CGContextRef _Nullable c,     bool allowsFontSmoothing ); ``` |

Modified [CGContextSetAllowsFontSubpixelPositioning()](https://developer.apple.com/documentation/coregraphics/1454942-cgcontextsetallowsfontsubpixelpo)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSubpixelPositioning (     CGContextRef context,     bool allowsFontSubpixelPositioning ); ``` |
| To | ``` void CGContextSetAllowsFontSubpixelPositioning (     CGContextRef _Nullable c,     bool allowsFontSubpixelPositioning ); ``` |

Modified [CGContextSetAllowsFontSubpixelQuantization()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456263-setallowsfontsubpixelquantizatio)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSubpixelQuantization (     CGContextRef context,     bool allowsFontSubpixelQuantization ); ``` |
| To | ``` void CGContextSetAllowsFontSubpixelQuantization (     CGContextRef _Nullable c,     bool allowsFontSubpixelQuantization ); ``` |

Modified [CGContextSetBlendMode()](https://developer.apple.com/documentation/coregraphics/1455994-cgcontextsetblendmode)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetBlendMode (     CGContextRef context,     CGBlendMode mode ); ``` |
| To | ``` void CGContextSetBlendMode (     CGContextRef _Nullable c,     CGBlendMode mode ); ``` |

Modified [CGContextSetCharacterSpacing()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454786-setcharacterspacing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCharacterSpacing (     CGContextRef context,     CGFloat spacing ); ``` |
| To | ``` void CGContextSetCharacterSpacing (     CGContextRef _Nullable c,     CGFloat spacing ); ``` |

Modified [CGContextSetCMYKFillColor()](https://developer.apple.com/documentation/coregraphics/1454214-cgcontextsetcmykfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCMYKFillColor (     CGContextRef context,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetCMYKFillColor (     CGContextRef _Nullable c,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |

Modified [CGContextSetCMYKStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455358-cgcontextsetcmykstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCMYKStrokeColor (     CGContextRef context,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetCMYKStrokeColor (     CGContextRef _Nullable c,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |

Modified [CGContextSetFillColor()](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillColor (     CGContextRef context,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetFillColor (     CGContextRef _Nullable c,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetFillColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455151-setfillcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillColorSpace (     CGContextRef context,     CGColorSpaceRef space ); ``` |
| To | ``` void CGContextSetFillColorSpace (     CGContextRef _Nullable c,     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGContextSetFillPattern()](https://developer.apple.com/documentation/coregraphics/1456334-cgcontextsetfillpattern)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillPattern (     CGContextRef context,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetFillPattern (     CGContextRef _Nullable c,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetGrayFillColor()](https://developer.apple.com/documentation/coregraphics/1454255-cgcontextsetgrayfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetGrayFillColor (     CGContextRef context,     CGFloat gray,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetGrayFillColor (     CGContextRef _Nullable c,     CGFloat gray,     CGFloat alpha ); ``` |

Modified [CGContextSetGrayStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455209-cgcontextsetgraystrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetGrayStrokeColor (     CGContextRef context,     CGFloat gray,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetGrayStrokeColor (     CGContextRef _Nullable c,     CGFloat gray,     CGFloat alpha ); ``` |

Modified [CGContextSetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetInterpolationQuality (     CGContextRef context,     CGInterpolationQuality quality ); ``` |
| To | ``` void CGContextSetInterpolationQuality (     CGContextRef _Nullable c,     CGInterpolationQuality quality ); ``` |

Modified [CGContextSetLineDash()](https://developer.apple.com/documentation/coregraphics/1455911-cgcontextsetlinedash)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetLineDash (     CGContextRef c,     CGFloat phase,     const CGFloat lengths[],     size_t count ); ``` |
| To | ``` void CGContextSetLineDash (     CGContextRef _Nullable c,     CGFloat phase,     const CGFloat * _Nullable lengths,     size_t count ); ``` |

Modified [CGContextSetPatternPhase()](https://developer.apple.com/documentation/coregraphics/1455334-cgcontextsetpatternphase)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetPatternPhase (     CGContextRef context,     CGSize phase ); ``` |
| To | ``` void CGContextSetPatternPhase (     CGContextRef _Nullable c,     CGSize phase ); ``` |

Modified [CGContextSetRenderingIntent()](https://developer.apple.com/documentation/coregraphics/1455544-cgcontextsetrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRenderingIntent (     CGContextRef context,     CGColorRenderingIntent intent ); ``` |
| To | ``` void CGContextSetRenderingIntent (     CGContextRef _Nullable c,     CGColorRenderingIntent intent ); ``` |

Modified [CGContextSetRGBFillColor()](https://developer.apple.com/documentation/coregraphics/1455624-cgcontextsetrgbfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRGBFillColor (     CGContextRef context,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetRGBFillColor (     CGContextRef _Nullable c,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |

Modified [CGContextSetRGBStrokeColor()](https://developer.apple.com/documentation/coregraphics/1456378-cgcontextsetrgbstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRGBStrokeColor (     CGContextRef context,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetRGBStrokeColor (     CGContextRef _Nullable c,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |

Modified [CGContextSetShadow()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456082-setshadow)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShadow (     CGContextRef context,     CGSize offset,     CGFloat blur ); ``` |
| To | ``` void CGContextSetShadow (     CGContextRef _Nullable c,     CGSize offset,     CGFloat blur ); ``` |

Modified [CGContextSetShadowWithColor()](https://developer.apple.com/documentation/coregraphics/1455205-cgcontextsetshadowwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShadowWithColor (     CGContextRef context,     CGSize offset,     CGFloat blur,     CGColorRef color ); ``` |
| To | ``` void CGContextSetShadowWithColor (     CGContextRef _Nullable c,     CGSize offset,     CGFloat blur,     CGColorRef _Nullable color ); ``` |

Modified [CGContextSetShouldAntialias()](https://developer.apple.com/documentation/coregraphics/1455178-cgcontextsetshouldantialias)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldAntialias (     CGContextRef context,     bool shouldAntialias ); ``` |
| To | ``` void CGContextSetShouldAntialias (     CGContextRef _Nullable c,     bool shouldAntialias ); ``` |

Modified [CGContextSetShouldSmoothFonts()](https://developer.apple.com/documentation/coregraphics/1455816-cgcontextsetshouldsmoothfonts)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSmoothFonts (     CGContextRef context,     bool shouldSmoothFonts ); ``` |
| To | ``` void CGContextSetShouldSmoothFonts (     CGContextRef _Nullable c,     bool shouldSmoothFonts ); ``` |

Modified [CGContextSetShouldSubpixelPositionFonts()](https://developer.apple.com/documentation/coregraphics/1455671-cgcontextsetshouldsubpixelpositi)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSubpixelPositionFonts (     CGContextRef context,     bool shouldSubpixelPositionFonts ); ``` |
| To | ``` void CGContextSetShouldSubpixelPositionFonts (     CGContextRef _Nullable c,     bool shouldSubpixelPositionFonts ); ``` |

Modified [CGContextSetShouldSubpixelQuantizeFonts()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455766-setshouldsubpixelquantizefonts)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSubpixelQuantizeFonts (     CGContextRef context,     bool shouldSubpixelQuantizeFonts ); ``` |
| To | ``` void CGContextSetShouldSubpixelQuantizeFonts (     CGContextRef _Nullable c,     bool shouldSubpixelQuantizeFonts ); ``` |

Modified [CGContextSetStrokeColor()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456283-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokeColor (     CGContextRef context,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetStrokeColor (     CGContextRef _Nullable c,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetStrokeColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454396-setstrokecolorspace)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokeColorSpace (     CGContextRef context,     CGColorSpaceRef space ); ``` |
| To | ``` void CGContextSetStrokeColorSpace (     CGContextRef _Nullable c,     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGContextSetStrokePattern()](https://developer.apple.com/documentation/coregraphics/1454796-cgcontextsetstrokepattern)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokePattern (     CGContextRef context,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetStrokePattern (     CGContextRef _Nullable c,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextShowGlyphs()](https://developer.apple.com/documentation/coregraphics/1586500-cgcontextshowglyphs)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphs (     CGContextRef c,     const CGGlyph g[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphs (     CGContextRef _Nullable c,     const CGGlyph * _Nullable g,     size_t count ); ``` |

Modified [CGContextShowGlyphsAtPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsAtPoint (     CGContextRef context,     CGFloat x,     CGFloat y,     const CGGlyph glyphs[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsAtPoint (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y,     const CGGlyph * _Nullable glyphs,     size_t count ); ``` |

Modified [CGContextShowGlyphsAtPositions()](https://developer.apple.com/documentation/coregraphics/1456200-cgcontextshowglyphsatpositions)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsAtPositions (     CGContextRef context,     const CGGlyph glyphs[],     const CGPoint positions[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsAtPositions (     CGContextRef _Nullable c,     const CGGlyph * _Nullable glyphs,     const CGPoint * _Nullable Lpositions,     size_t count ); ``` |

Modified [CGContextShowGlyphsWithAdvances()](https://developer.apple.com/documentation/coregraphics/1586503-cgcontextshowglyphswithadvances)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsWithAdvances (     CGContextRef context,     const CGGlyph glyphs[],     const CGSize advances[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsWithAdvances (     CGContextRef _Nullable c,     const CGGlyph * _Nullable glyphs,     const CGSize * _Nullable advances,     size_t count ); ``` |

Modified [CGContextStrokeEllipseInRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455774-strokeellipse)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextStrokeEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextStrokeLineSegments()](https://developer.apple.com/documentation/coregraphics/1454389-cgcontextstrokelinesegments)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeLineSegments (     CGContextRef c,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGContextStrokeLineSegments (     CGContextRef _Nullable c,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGTextEncoding](https://developer.apple.com/documentation/coregraphics/cgtextencoding)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [kCGEncodingFontSpecific](https://developer.apple.com/documentation/coregraphics/cgtextencoding/encodingfontspecific)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [kCGEncodingMacRoman](https://developer.apple.com/documentation/coregraphics/cgtextencoding/encodingmacroman)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

#### CGDataConsumer.h

Modified [CGDataConsumerCreate()](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/1456428-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDataConsumerRef CGDataConsumerCreate (     void *info,     const CGDataConsumerCallbacks *callbacks ); ``` |
| To | ``` CGDataConsumerRef _Nullable CGDataConsumerCreate (     void * _Nullable info,     const CGDataConsumerCallbacks * _Nullable cbks ); ``` |

#### CGFont.h

Removed [kCGFontIndexInvalid](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgfontindexinvalid)Removed [kCGFontIndexMax](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgfontindexmax)Removed [kCGGlyphMax](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgglyphmax)Added CGGlypDeprecatedEnumAdded [kCGFontIndexInvalid](https://developer.apple.com/documentation/coregraphics/kcgfontindexinvalid)Added [kCGFontIndexMax](https://developer.apple.com/documentation/coregraphics/kcgfontindexmax)Added [kCGGlyphMax](https://developer.apple.com/documentation/coregraphics/kcgglyphmax)Modified [CGFontCreatePostScriptSubset()](https://developer.apple.com/documentation/coregraphics/cgfont/1396324-createpostscriptsubset)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGFontCreatePostScriptSubset (     CGFontRef font,     CFStringRef subsetName,     CGFontPostScriptFormat format,     const CGGlyph glyphs[],     size_t count,     const CGGlyph encoding[256] ); ``` |
| To | ``` CFDataRef _Nullable CGFontCreatePostScriptSubset (     CGFontRef _Nullable font,     CFStringRef _Nullable subsetName,     CGFontPostScriptFormat format,     const CGGlyph * _Nullable glyphs,     size_t count,     const CGGlyph encoding[256] ); ``` |

Modified [CGFontGetGlyphAdvances()](https://developer.apple.com/documentation/coregraphics/1396332-cgfontgetglyphadvances)

|  | Declaration |
| --- | --- |
| From | ``` bool CGFontGetGlyphAdvances (     CGFontRef font,     const CGGlyph glyphs[],     size_t count,     int advances[] ); ``` |
| To | ``` bool CGFontGetGlyphAdvances (     CGFontRef _Nullable font,     const CGGlyph * _Nonnull glyphs,     size_t count,     int * _Nonnull advances ); ``` |

Modified [CGFontGetGlyphBBoxes()](https://developer.apple.com/documentation/coregraphics/1396342-cgfontgetglyphbboxes)

|  | Declaration |
| --- | --- |
| From | ``` bool CGFontGetGlyphBBoxes (     CGFontRef font,     const CGGlyph glyphs[],     size_t count,     CGRect bboxes[] ); ``` |
| To | ``` bool CGFontGetGlyphBBoxes (     CGFontRef _Nullable font,     const CGGlyph * _Nonnull glyphs,     size_t count,     CGRect * _Nonnull bboxes ); ``` |

#### CGGradient.h

Modified [CGGradientCreateWithColorComponents()](https://developer.apple.com/documentation/coregraphics/cggradient/1398454-init)

|  | Declaration |
| --- | --- |
| From | ``` CGGradientRef CGGradientCreateWithColorComponents (     CGColorSpaceRef space,     const CGFloat components[],     const CGFloat locations[],     size_t count ); ``` |
| To | ``` CGGradientRef _Nullable CGGradientCreateWithColorComponents (     CGColorSpaceRef _Nullable space,     const CGFloat * _Nullable components,     const CGFloat * _Nullable locations,     size_t count ); ``` |

Modified [CGGradientCreateWithColors()](https://developer.apple.com/documentation/coregraphics/cggradient/1398458-init)

|  | Declaration |
| --- | --- |
| From | ``` CGGradientRef CGGradientCreateWithColors (     CGColorSpaceRef space,     CFArrayRef colors,     const CGFloat locations[] ); ``` |
| To | ``` CGGradientRef _Nullable CGGradientCreateWithColors (     CGColorSpaceRef _Nullable space,     CFArrayRef _Nullable colors,     const CGFloat * _Nullable locations ); ``` |

#### CGImage.h

Added [CGImageGetUTType()](https://developer.apple.com/documentation/coregraphics/1456067-cgimagegetuttype)Modified [CGImageCreate()](https://developer.apple.com/documentation/coregraphics/cgimage/1455149-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo,     CGDataProviderRef provider,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     CGBitmapInfo bitmapInfo,     CGDataProviderRef _Nullable provider,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageCreateWithJPEGDataProvider()](https://developer.apple.com/documentation/coregraphics/cgimage/1454920-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithJPEGDataProvider (     CGDataProviderRef source,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithJPEGDataProvider (     CGDataProviderRef _Nullable source,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageCreateWithMaskingColors()](https://developer.apple.com/documentation/coregraphics/cgimage/1454358-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithMaskingColors (     CGImageRef image,     const CGFloat components[] ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithMaskingColors (     CGImageRef _Nullable image,     const CGFloat * _Nullable components ); ``` |

Modified [CGImageCreateWithPNGDataProvider()](https://developer.apple.com/documentation/coregraphics/cgimage/1454993-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithPNGDataProvider (     CGDataProviderRef source,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithPNGDataProvider (     CGDataProviderRef _Nullable source,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageMaskCreate()](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageMaskCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGDataProviderRef provider,     const CGFloat decode[],     bool shouldInterpolate ); ``` |
| To | ``` CGImageRef _Nullable CGImageMaskCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGDataProviderRef _Nullable provider,     const CGFloat * _Nullable decode,     bool shouldInterpolate ); ``` |

#### CGPath.h

Modified [CGPathAddLines()](https://developer.apple.com/documentation/coregraphics/1411171-cgpathaddlines)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddLines (     CGMutablePathRef path,     const CGAffineTransform *m,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGPathAddLines (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGPathAddRects()](https://developer.apple.com/documentation/coregraphics/1411153-cgpathaddrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddRects (     CGMutablePathRef path,     const CGAffineTransform *m,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGPathAddRects (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     const CGRect * _Nullable rects,     size_t count ); ``` |

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
