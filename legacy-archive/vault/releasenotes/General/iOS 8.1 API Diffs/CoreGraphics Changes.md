---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreGraphics.html
archived_at: '2026-07-18T02:56:09.073310Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreGraphics Changes

## CoreGraphics

Removed CGBitmapInfo.valueRemoved CGFloat.convertFromFloatLiteral(NativeType) -> CGFloat [static]Removed CGFloat.convertFromIntegerLiteral(Int) -> CGFloat [static]Removed CGVector.init(_: CGFloat, _: CGFloat)Removed CGVector.init(_: Double, _: Double)Removed CGVector.init(_: Int, _: Int)Added CGBitmapInfo.init(rawValue: UInt32)Added CGFloat.init(floatLiteral: NativeType)Added CGFloat.init(integerLiteral: Int)Added Double.init(_: CGFloat)Added Float.init(_: CGFloat)Added Int.init(_: CGFloat)Added Int16.init(_: CGFloat)Added Int32.init(_: CGFloat)Added Int64.init(_: CGFloat)Added Int8.init(_: CGFloat)Added UInt.init(_: CGFloat)Added UInt16.init(_: CGFloat)Added UInt32.init(_: CGFloat)Added UInt64.init(_: CGFloat)Added UInt8.init(_: CGFloat)Modified CGBitmapInfo [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct CGBitmapInfo : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | iOS 8.0 |
| To | ``` struct CGBitmapInfo : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | iOS 2.0 |

Modified CGBitmapInfo.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformEqualToTransform(CGAffineTransform, CGAffineTransform) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformIdentity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformIsIdentity(CGAffineTransform) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextCreate(UnsafeMutablePointer<Void>, UInt, UInt, UInt, UInt, CGColorSpace!, CGBitmapInfo) -> CGContext!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextCreateImage(CGContext!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextCreateWithData(UnsafeMutablePointer<Void>, UInt, UInt, UInt, UInt, CGColorSpace!, CGBitmapInfo, CGBitmapContextReleaseDataCallback, UnsafeMutablePointer<Void>) -> CGContext!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGBitmapContextGetAlphaInfo(CGContext!) -> CGImageAlphaInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetBitmapInfo(CGContext!) -> CGBitmapInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetBitsPerComponent(CGContext!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetBitsPerPixel(CGContext!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetBytesPerRow(CGContext!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetColorSpace(CGContext!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetData(CGContext!) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetHeight(CGContext!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGBitmapContextGetWidth(CGContext!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorCreate(CGColorSpace!, UnsafePointer<CGFloat>) -> CGColor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorCreateCopy(CGColor!) -> CGColor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorCreateCopyWithAlpha(CGColor!, CGFloat) -> CGColor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorCreateWithPattern(CGColorSpace!, CGPattern!, UnsafePointer<CGFloat>) -> CGColor!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorEqualToColor(CGColor!, CGColor!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetAlpha(CGColor!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetColorSpace(CGColor!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetComponents(CGColor!) -> UnsafePointer<CGFloat>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetNumberOfComponents(CGColor!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetPattern(CGColor!) -> CGPattern!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCopyICCProfile(CGColorSpace!) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CGColorSpaceCreateCalibratedGray(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, CGFloat) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateCalibratedRGB(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateDeviceCMYK() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateDeviceGray() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateDeviceRGB() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateICCBased(UInt, UnsafePointer<CGFloat>, CGDataProvider!, CGColorSpace!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateIndexed(CGColorSpace!, UInt, UnsafePointer<UInt8>) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateLab(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreatePattern(CGColorSpace!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateWithICCProfile(CFData!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceCreateWithName(CFString!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetBaseColorSpace(CGColorSpace!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetColorTable(CGColorSpace!, UnsafeMutablePointer<UInt8>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetColorTableCount(CGColorSpace!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetModel(CGColorSpace!) -> CGColorSpaceModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetNumberOfComponents(CGColorSpace!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGColorSpaceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddArc(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddArcToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddCurveToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddLineToPoint(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddLines(CGContext!, UnsafePointer<CGPoint>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddPath(CGContext!, CGPath!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddQuadCurveToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextAddRects(CGContext!, UnsafePointer<CGRect>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextBeginPage(CGContext!, UnsafePointer<CGRect>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextBeginPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextBeginTransparencyLayer(CGContext!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextBeginTransparencyLayerWithRect(CGContext!, CGRect, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClearRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClip(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClipToMask(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClipToRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClipToRects(CGContext!, UnsafePointer<CGRect>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextClosePath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConcatCTM(CGContext!, CGAffineTransform)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertPointToDeviceSpace(CGContext!, CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertPointToUserSpace(CGContext!, CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertRectToDeviceSpace(CGContext!, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertRectToUserSpace(CGContext!, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertSizeToDeviceSpace(CGContext!, CGSize) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextConvertSizeToUserSpace(CGContext!, CGSize) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextCopyPath(CGContext!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawImage(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawLayerAtPoint(CGContext!, CGPoint, CGLayer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawLayerInRect(CGContext!, CGRect, CGLayer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawLinearGradient(CGContext!, CGGradient!, CGPoint, CGPoint, CGGradientDrawingOptions)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawPDFPage(CGContext!, CGPDFPage!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawPath(CGContext!, CGPathDrawingMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawRadialGradient(CGContext!, CGGradient!, CGPoint, CGFloat, CGPoint, CGFloat, CGGradientDrawingOptions)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawShading(CGContext!, CGShading!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextDrawTiledImage(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextEOClip(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextEOFillPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextEndPage(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextEndTransparencyLayer(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextFillEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextFillPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextFillRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextFillRects(CGContext!, UnsafePointer<CGRect>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextFlush(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetCTM(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetClipBoundingBox(CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetInterpolationQuality(CGContext!) -> CGInterpolationQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetPathBoundingBox(CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetPathCurrentPoint(CGContext!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetTextMatrix(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetTextPosition(CGContext!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextGetUserSpaceToDeviceSpaceTransform(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextIsPathEmpty(CGContext!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextMoveToPoint(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextPathContainsPoint(CGContext!, CGPoint, CGPathDrawingMode) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextReplacePathWithStrokedPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextRestoreGState(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextRotateCTM(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSaveGState(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextScaleCTM(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetAllowsAntialiasing(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetAllowsFontSmoothing(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetAllowsFontSubpixelPositioning(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetAllowsFontSubpixelQuantization(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetAlpha(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetBlendMode(CGContext!, CGBlendMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetCMYKFillColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetCMYKStrokeColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetCharacterSpacing(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFillColor(CGContext!, UnsafePointer<CGFloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFillColorSpace(CGContext!, CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFillColorWithColor(CGContext!, CGColor!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFillPattern(CGContext!, CGPattern!, UnsafePointer<CGFloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFlatness(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFont(CGContext!, CGFont!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetFontSize(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetGrayFillColor(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetGrayStrokeColor(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetInterpolationQuality(CGContext!, CGInterpolationQuality)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetLineCap(CGContext!, CGLineCap)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetLineDash(CGContext!, CGFloat, UnsafePointer<CGFloat>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetLineJoin(CGContext!, CGLineJoin)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetLineWidth(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetMiterLimit(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetPatternPhase(CGContext!, CGSize)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetRGBFillColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetRGBStrokeColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetRenderingIntent(CGContext!, CGColorRenderingIntent)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShadow(CGContext!, CGSize, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShadowWithColor(CGContext!, CGSize, CGFloat, CGColor!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShouldAntialias(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShouldSmoothFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShouldSubpixelPositionFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetShouldSubpixelQuantizeFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetStrokeColor(CGContext!, UnsafePointer<CGFloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetStrokeColorSpace(CGContext!, CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetStrokeColorWithColor(CGContext!, CGColor!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetStrokePattern(CGContext!, CGPattern!, UnsafePointer<CGFloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetTextDrawingMode(CGContext!, CGTextDrawingMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetTextMatrix(CGContext!, CGAffineTransform)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSetTextPosition(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextShowGlyphsAtPositions(CGContext!, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextStrokeEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextStrokeLineSegments(CGContext!, UnsafePointer<CGPoint>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextStrokePath(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextStrokeRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextStrokeRectWithWidth(CGContext!, CGRect, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextSynchronize(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGContextTranslateCTM(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataConsumerCreate(UnsafeMutablePointer<Void>, UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataConsumerCreateWithCFData(CFMutableData!) -> CGDataConsumer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataConsumerCreateWithURL(CFURL!) -> CGDataConsumer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataConsumerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCopyData(CGDataProvider!) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateDirect(UnsafeMutablePointer<Void>, off_t, UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateSequential(UnsafeMutablePointer<Void>, UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateWithCFData(CFData!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateWithData(UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt, CGDataProviderReleaseDataCallback) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateWithFilename(UnsafePointer<Int8>) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderCreateWithURL(CFURL!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGDataProviderGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCanCreatePostScriptSubset(CGFont!, CGFontPostScriptFormat) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyFullName(CGFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyGlyphNameForGlyph(CGFont!, CGGlyph) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyPostScriptName(CGFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyTableForTag(CGFont!, UInt32) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyTableTags(CGFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyVariationAxes(CGFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCopyVariations(CGFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCreateCopyWithVariations(CGFont!, CFDictionary!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCreatePostScriptEncoding(CGFont!, UnsafePointer<CGGlyph>) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCreatePostScriptSubset(CGFont!, CFString!, CGFontPostScriptFormat, UnsafePointer<CGGlyph>, UInt, UnsafePointer<CGGlyph>) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCreateWithDataProvider(CGDataProvider!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontCreateWithFontName(CFString!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetAscent(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetCapHeight(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetDescent(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetFontBBox(CGFont!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetGlyphAdvances(CGFont!, UnsafePointer<CGGlyph>, UInt, UnsafeMutablePointer<Int32>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetGlyphBBoxes(CGFont!, UnsafePointer<CGGlyph>, UInt, UnsafeMutablePointer<CGRect>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetGlyphWithGlyphName(CGFont!, CFString!) -> CGGlyph

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetItalicAngle(CGFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetLeading(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetNumberOfGlyphs(CGFont!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetStemV(CGFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetUnitsPerEm(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFontGetXHeight(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFunctionCreate(UnsafeMutablePointer<Void>, UInt, UnsafePointer<CGFloat>, UInt, UnsafePointer<CGFloat>, UnsafePointer<CGFunctionCallbacks>) -> CGFunction!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGFunctionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGGradientCreateWithColorComponents(CGColorSpace!, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UInt) -> CGGradient!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGGradientCreateWithColors(CGColorSpace!, CFArray!, UnsafePointer<CGFloat>) -> CGGradient!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGGradientGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreate(UInt, UInt, UInt, UInt, UInt, CGColorSpace!, CGBitmapInfo, CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateCopy(CGImage!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateCopyWithColorSpace(CGImage!, CGColorSpace!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateWithImageInRect(CGImage!, CGRect) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateWithJPEGDataProvider(CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateWithMask(CGImage!, CGImage!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateWithMaskingColors(CGImage!, UnsafePointer<CGFloat>) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageCreateWithPNGDataProvider(CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetAlphaInfo(CGImage!) -> CGImageAlphaInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetBitmapInfo(CGImage!) -> CGBitmapInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetBitsPerComponent(CGImage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetBitsPerPixel(CGImage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetBytesPerRow(CGImage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetColorSpace(CGImage!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetDataProvider(CGImage!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetDecode(CGImage!) -> UnsafePointer<CGFloat>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetHeight(CGImage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetRenderingIntent(CGImage!) -> CGColorRenderingIntent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetShouldInterpolate(CGImage!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageGetWidth(CGImage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageIsMask(CGImage!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGImageMaskCreate(UInt, UInt, UInt, UInt, UInt, CGDataProvider!, UnsafePointer<CGFloat>, Bool) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGLayerCreateWithContext(CGContext!, CGSize, CFDictionary!) -> CGLayer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGLayerGetContext(CGLayer!) -> CGContext!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGLayerGetSize(CGLayer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGLayerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFArrayGetArray(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetArray(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetBoolean(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetCount(CGPDFArrayRef) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetCount(_ array: CGPDFArray!) -> UInt ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetCount(_ array: CGPDFArrayRef) -> UInt ``` | iOS 2.0 |

Modified CGPDFArrayGetDictionary(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetInteger(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetInteger(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetName(CGPDFArrayRef, UInt, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetName(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetNull(CGPDFArrayRef, UInt) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetNull(_ array: CGPDFArray!, _ index: UInt) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetNull(_ array: CGPDFArrayRef, _ index: UInt) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetNumber(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetNumber(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetObject(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetObject(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetStream(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetStream(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayGetString(CGPDFArrayRef, UInt, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetString(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafeMutablePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFArrayRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFArrayRef = CGPDFArray ``` |
| To | ``` typealias CGPDFArrayRef = COpaquePointer ``` |

Modified CGPDFContentStreamCreateWithPage(CGPDFPage!) -> CGPDFContentStream!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStream!) -> CGPDFContentStream!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStream!, _ streamResources: CGPDFDictionary!, _ parent: CGPDFContentStream!) -> CGPDFContentStream! ``` | iOS 8.0 |
| To | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStream!) -> CGPDFContentStream! ``` | iOS 2.0 |

Modified CGPDFContentStreamGetResource(CGPDFContentStream!, UnsafePointer<Int8>, UnsafePointer<Int8>) -> CGPDFObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStream!, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObject! ``` | iOS 8.0 |
| To | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStream!, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef ``` | iOS 2.0 |

Modified CGPDFContentStreamGetStreams(CGPDFContentStream!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextAddDestinationAtPoint(CGContext!, CFString!, CGPoint)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextAddDocumentMetadata(CGContext!, CFData!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGPDFContextBeginPage(CGContext!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextClose(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextCreate(CGDataConsumer!, UnsafePointer<CGRect>, CFDictionary!) -> CGContext!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextCreateWithURL(CFURL!, UnsafePointer<CGRect>, CFDictionary!) -> CGContext!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextEndPage(CGContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextSetDestinationForRect(CGContext!, CFString!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFContextSetURLForRect(CGContext!, CFURL!, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDictionaryApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Int8>, CGPDFObject!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPDFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPDFDictionaryApplyFunction(CGPDFDictionaryRef, CGPDFDictionaryApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionary!, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafeMutablePointer<Void>) ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafeMutablePointer<Void>) ``` | iOS 2.0 |

Modified CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionary!) -> UInt ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionaryRef) -> UInt ``` | iOS 2.0 |

Modified CGPDFDictionaryGetDictionary(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetInteger(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetName(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetNumber(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetObject(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetStream(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionary!, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFDictionaryRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryRef = CGPDFDictionary ``` |
| To | ``` typealias CGPDFDictionaryRef = COpaquePointer ``` |

Modified CGPDFDocumentAllowsCopying(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentAllowsPrinting(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentCreateWithProvider(CGDataProvider!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentCreateWithURL(CFURL!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentGetCatalog(CGPDFDocument!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument!) -> CGPDFDictionary! ``` | iOS 8.0 |
| To | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` | iOS 2.0 |

Modified CGPDFDocumentGetID(CGPDFDocument!) -> CGPDFArrayRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument!) -> CGPDFArray! ``` | iOS 8.0 |
| To | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument!) -> CGPDFArrayRef ``` | iOS 2.0 |

Modified CGPDFDocumentGetInfo(CGPDFDocument!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument!) -> CGPDFDictionary! ``` | iOS 8.0 |
| To | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` | iOS 2.0 |

Modified CGPDFDocumentGetNumberOfPages(CGPDFDocument!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentGetPage(CGPDFDocument!, UInt) -> CGPDFPage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentGetVersion(CGPDFDocument!, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentIsEncrypted(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentIsUnlocked(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFDocumentUnlockWithPassword(CGPDFDocument!, UnsafePointer<Int8>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFObjectGetType(CGPDFObjectRef) -> CGPDFObjectType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFObjectGetType(_ object: CGPDFObject!) -> CGPDFObjectType ``` | iOS 8.0 |
| To | ``` func CGPDFObjectGetType(_ object: CGPDFObjectRef) -> CGPDFObjectType ``` | iOS 2.0 |

Modified CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutablePointer<Void>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFObjectGetValue(_ object: CGPDFObject!, _ type: CGPDFObjectType, _ value: UnsafeMutablePointer<Void>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutablePointer<Void>) -> Bool ``` | iOS 2.0 |

Modified CGPDFObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFObjectRef = CGPDFObject ``` |
| To | ``` typealias CGPDFObjectRef = COpaquePointer ``` |

Modified CGPDFOperatorTableCreate() -> CGPDFOperatorTable!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFOperatorTableSetCallback(CGPDFOperatorTable!, UnsafePointer<Int8>, CGPDFOperatorCallback)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetBoxRect(CGPDFPage!, CGPDFBox) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetDictionary(CGPDFPage!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage!) -> CGPDFDictionary! ``` | iOS 8.0 |
| To | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage!) -> CGPDFDictionaryRef ``` | iOS 2.0 |

Modified CGPDFPageGetDocument(CGPDFPage!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetDrawingTransform(CGPDFPage!, CGPDFBox, CGRect, Int32, Bool) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetPageNumber(CGPDFPage!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetRotationAngle(CGPDFPage!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFPageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerCreate(CGPDFContentStream!, CGPDFOperatorTable!, UnsafeMutablePointer<Void>) -> CGPDFScanner!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerGetContentStream(CGPDFScanner!) -> CGPDFContentStream!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerPopArray(CGPDFScanner!, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFScannerPopBoolean(CGPDFScanner!, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerPopDictionary(CGPDFScanner!, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFScannerPopInteger(CGPDFScanner!, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerPopName(CGPDFScanner!, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerPopNumber(CGPDFScanner!, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFScannerPopObject(CGPDFScanner!, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFScannerPopStream(CGPDFScanner!, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFScannerPopString(CGPDFScanner!, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopString(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | iOS 8.0 |
| To | ``` func CGPDFScannerPopString(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | iOS 2.0 |

Modified CGPDFScannerScan(CGPDFScanner!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPDFStreamCopyData(CGPDFStreamRef, UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStreamCopyData(_ stream: CGPDFStream!, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>! ``` | iOS 8.0 |
| To | ``` func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>! ``` | iOS 2.0 |

Modified CGPDFStreamGetDictionary(CGPDFStreamRef) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStream!) -> Unmanaged<CGPDFDictionary>! ``` | iOS 8.0 |
| To | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef ``` | iOS 2.0 |

Modified CGPDFStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStreamRef = CGPDFStream ``` |
| To | ``` typealias CGPDFStreamRef = COpaquePointer ``` |

Modified CGPDFStringCopyDate(CGPDFStringRef) -> Unmanaged<CFDate>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringCopyDate(_ string: CGPDFString!) -> Unmanaged<CFDate>! ``` | iOS 8.0 |
| To | ``` func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> Unmanaged<CFDate>! ``` | iOS 2.0 |

Modified CGPDFStringCopyTextString(CGPDFStringRef) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringCopyTextString(_ string: CGPDFString!) -> Unmanaged<CFString>! ``` | iOS 8.0 |
| To | ``` func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> Unmanaged<CFString>! ``` | iOS 2.0 |

Modified CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringGetBytePtr(_ string: CGPDFString!) -> UnsafePointer<UInt8> ``` | iOS 8.0 |
| To | ``` func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8> ``` | iOS 2.0 |

Modified CGPDFStringGetLength(CGPDFStringRef) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringGetLength(_ string: CGPDFString!) -> UInt ``` | iOS 8.0 |
| To | ``` func CGPDFStringGetLength(_ string: CGPDFStringRef) -> UInt ``` | iOS 2.0 |

Modified CGPDFStringRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStringRef = CGPDFString ``` |
| To | ``` typealias CGPDFStringRef = COpaquePointer ``` |

Modified CGPathAddArc(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddArcToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddCurveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddEllipseInRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddLineToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddLines(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGPoint>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddPath(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGPath!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddQuadCurveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddRects(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGRect>, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathAddRelativeArc(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathAddRoundedRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGPathApply(CGPath!, UnsafeMutablePointer<Void>, CGPathApplierFunction)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathCloseSubpath(CGMutablePath!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathContainsPoint(CGPath!, UnsafePointer<CGAffineTransform>, CGPoint, Bool) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathCreateCopy(CGPath!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathCreateCopyByDashingPath(CGPath!, UnsafePointer<CGAffineTransform>, CGFloat, UnsafePointer<CGFloat>, UInt) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathCreateCopyByStrokingPath(CGPath!, UnsafePointer<CGAffineTransform>, CGFloat, CGLineCap, CGLineJoin, CGFloat) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathCreateCopyByTransformingPath(CGPath!, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathCreateMutable() -> CGMutablePath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathCreateMutableCopy(CGPath!) -> CGMutablePath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathCreateMutableCopyByTransformingPath(CGPath!, UnsafePointer<CGAffineTransform>) -> CGMutablePath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathCreateWithEllipseInRect(CGRect, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CGPathCreateWithRect(CGRect, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGPathCreateWithRoundedRect(CGRect, CGFloat, CGFloat, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGPathEqualToPath(CGPath!, CGPath!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathGetBoundingBox(CGPath!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathGetCurrentPoint(CGPath!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathGetPathBoundingBox(CGPath!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGPathGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathIsEmpty(CGPath!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathIsRect(CGPath!, UnsafeMutablePointer<CGRect>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPathMoveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPatternCreate(UnsafeMutablePointer<Void>, CGRect, CGAffineTransform, CGFloat, CGFloat, CGPatternTiling, Bool, UnsafePointer<CGPatternCallbacks>) -> CGPattern!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPatternGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPointApplyAffineTransform(CGPoint, CGAffineTransform) -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPointCreateDictionaryRepresentation(CGPoint) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPointEqualToPoint(CGPoint, CGPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPointMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGPoint>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGPointZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectApplyAffineTransform(CGRect, CGAffineTransform) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectContainsPoint(CGRect, CGPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectContainsRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectCreateDictionaryRepresentation() -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectDivide(CGRect, UnsafeMutablePointer<CGRect>, UnsafeMutablePointer<CGRect>, CGFloat, CGRectEdge)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectEqualToRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetHeight(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMaxX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMaxY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMidX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMidY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMinX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetMinY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectGetWidth(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectInfinite

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIntegral(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIntersection(CGRect, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIntersectsRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIsEmpty(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIsInfinite(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectIsNull(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGRect>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectNull

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectStandardize(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectUnion(CGRect, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGRectZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGShadingCreateAxial(CGColorSpace!, CGPoint, CGPoint, CGFunction!, Bool, Bool) -> CGShading!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGShadingCreateRadial(CGColorSpace!, CGPoint, CGFloat, CGPoint, CGFloat, CGFunction!, Bool, Bool) -> CGShading!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGShadingGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGSizeApplyAffineTransform(CGSize, CGAffineTransform) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGSizeCreateDictionaryRepresentation(CGSize) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGSizeEqualToSize(CGSize, CGSize) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGSizeMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGSize>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CGSizeZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGFontVariationAxisDefaultValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGFontVariationAxisMaxValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGFontVariationAxisMinValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGFontVariationAxisName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextAllowsCopying

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextAllowsPrinting

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextArtBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextBleedBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextCreator

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextCropBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextEncryptionKeyLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextKeywords

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextMediaBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextOwnerPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextSubject

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextTrimBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCGPDFContextUserPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

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
