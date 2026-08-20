---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreGraphics.html
archived_at: '2026-07-18T02:56:22.499096Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreGraphics Changes

## CoreGraphics

Added CGAffineTransform.init()Added CGAffineTransform.init(a: CGFloat, b: CGFloat, c: CGFloat, d: CGFloat, tx: CGFloat, ty: CGFloat)Added CGDataConsumerCallbacks.init()Added CGDataConsumerCallbacks.init(putBytes: CGDataConsumerPutBytesCallback, releaseConsumer: CGDataConsumerReleaseInfoCallback)Added CGDataProviderDirectCallbacks.init()Added CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback, releaseBytePointer: CGDataProviderReleaseBytePointerCallback, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Added CGDataProviderSequentialCallbacks.init()Added CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CGDataProviderGetBytesCallback, skipForward: CGDataProviderSkipForwardCallback, rewind: CGDataProviderRewindCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Added CGFloat.encode() -> [Word]Added CGFunctionCallbacks.init()Added CGFunctionCallbacks.init(version: UInt32, evaluate: CGFunctionEvaluateCallback, releaseInfo: CGFunctionReleaseInfoCallback)Added CGPathElement.init()Added CGPathElement.init(type: CGPathElementType, points: UnsafeMutablePointer<CGPoint>)Added CGPatternCallbacks.init()Added CGPatternCallbacks.init(version: UInt32, drawPattern: CGPatternDrawPatternCallback, releaseInfo: CGPatternReleaseInfoCallback)Added CGPoint.init(x: CGFloat, y: CGFloat)Added CGRect.init(origin: CGPoint, size: CGSize)Added CGSize.init(width: CGFloat, height: CGFloat)Added CGVector.init()Added CGVector.init(dx: CGFloat, dy: CGFloat)Added CGPDFContentStreamRelease(CGPDFContentStreamRef)Added CGPDFContentStreamRetain(CGPDFContentStreamRef) -> CGPDFContentStreamRefAdded CGPDFOperatorTableRelease(CGPDFOperatorTableRef)Added CGPDFOperatorTableRetain(CGPDFOperatorTableRef) -> CGPDFOperatorTableRefAdded CGPDFScannerRelease(CGPDFScannerRef)Added CGPDFScannerRetain(CGPDFScannerRef) -> CGPDFScannerRefModified CGAffineTransform [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat } ``` |
| To | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat     init()     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat) } ``` |

Modified CGDataConsumerCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataConsumerCallbacks {     var putBytes: CGDataConsumerPutBytesCallback     var releaseConsumer: CGDataConsumerReleaseInfoCallback } ``` |
| To | ``` struct CGDataConsumerCallbacks {     var putBytes: CGDataConsumerPutBytesCallback     var releaseConsumer: CGDataConsumerReleaseInfoCallback     init()     init(putBytes putBytes: CGDataConsumerPutBytesCallback, releaseConsumer releaseConsumer: CGDataConsumerReleaseInfoCallback) } ``` |

Modified CGDataProviderDirectCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CGDataProviderGetBytePointerCallback     var releaseBytePointer: CGDataProviderReleaseBytePointerCallback     var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback     var releaseInfo: CGDataProviderReleaseInfoCallback } ``` |
| To | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CGDataProviderGetBytePointerCallback     var releaseBytePointer: CGDataProviderReleaseBytePointerCallback     var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback     var releaseInfo: CGDataProviderReleaseInfoCallback     init()     init(version version: UInt32, getBytePointer getBytePointer: CGDataProviderGetBytePointerCallback, releaseBytePointer releaseBytePointer: CGDataProviderReleaseBytePointerCallback, getBytesAtPosition getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback) } ``` |

Modified CGDataProviderSequentialCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CGDataProviderGetBytesCallback     var skipForward: CGDataProviderSkipForwardCallback     var rewind: CGDataProviderRewindCallback     var releaseInfo: CGDataProviderReleaseInfoCallback } ``` |
| To | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CGDataProviderGetBytesCallback     var skipForward: CGDataProviderSkipForwardCallback     var rewind: CGDataProviderRewindCallback     var releaseInfo: CGDataProviderReleaseInfoCallback     init()     init(version version: UInt32, getBytes getBytes: CGDataProviderGetBytesCallback, skipForward skipForward: CGDataProviderSkipForwardCallback, rewind rewind: CGDataProviderRewindCallback, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback) } ``` |

Modified CGFunctionCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback     var releaseInfo: CGFunctionReleaseInfoCallback } ``` |
| To | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback     var releaseInfo: CGFunctionReleaseInfoCallback     init()     init(version version: UInt32, evaluate evaluate: CGFunctionEvaluateCallback, releaseInfo releaseInfo: CGFunctionReleaseInfoCallback) } ``` |

Modified CGPathElement [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafeMutablePointer<CGPoint> } ``` |
| To | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafeMutablePointer<CGPoint>     init()     init(type type: CGPathElementType, points points: UnsafeMutablePointer<CGPoint>) } ``` |

Modified CGPatternCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CGPatternDrawPatternCallback     var releaseInfo: CGPatternReleaseInfoCallback } ``` |
| To | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CGPatternDrawPatternCallback     var releaseInfo: CGPatternReleaseInfoCallback     init()     init(version version: UInt32, drawPattern drawPattern: CGPatternDrawPatternCallback, releaseInfo releaseInfo: CGPatternReleaseInfoCallback) } ``` |

Modified CGPoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat } ``` |
| To | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } ``` |

Modified CGRect [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGRect {     var origin: CGPoint     var size: CGSize } ``` |
| To | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } ``` |

Modified CGSize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGSize {     var width: CGFloat     var height: CGFloat } ``` |
| To | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } ``` |

Modified CGVector [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat } ``` |
| To | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } ``` |

Modified CGBitmapContextCreate(UnsafeMutablePointer<Void>, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo) -> CGContext!

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo) -> CGContext! ``` |
| To | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo) -> CGContext! ``` |

Modified CGBitmapContextCreateWithData(UnsafeMutablePointer<Void>, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo, CGBitmapContextReleaseDataCallback, UnsafeMutablePointer<Void>) -> CGContext!

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ releaseCallback: CGBitmapContextReleaseDataCallback, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext! ``` |
| To | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ releaseCallback: CGBitmapContextReleaseDataCallback, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext! ``` |

Modified CGBitmapContextGetBitsPerComponent(CGContext!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext!) -> UInt ``` |
| To | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext!) -> Int ``` |

Modified CGBitmapContextGetBitsPerPixel(CGContext!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext!) -> UInt ``` |
| To | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext!) -> Int ``` |

Modified CGBitmapContextGetBytesPerRow(CGContext!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext!) -> UInt ``` |
| To | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext!) -> Int ``` |

Modified CGBitmapContextGetHeight(CGContext!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetHeight(_ context: CGContext!) -> UInt ``` |
| To | ``` func CGBitmapContextGetHeight(_ context: CGContext!) -> Int ``` |

Modified CGBitmapContextGetWidth(CGContext!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGBitmapContextGetWidth(_ context: CGContext!) -> UInt ``` |
| To | ``` func CGBitmapContextGetWidth(_ context: CGContext!) -> Int ``` |

Modified CGColorGetNumberOfComponents(CGColor!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGColorGetNumberOfComponents(_ color: CGColor!) -> UInt ``` |
| To | ``` func CGColorGetNumberOfComponents(_ color: CGColor!) -> Int ``` |

Modified CGColorSpaceCreateICCBased(Int, UnsafePointer<CGFloat>, CGDataProvider!, CGColorSpace!) -> CGColorSpace!

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateICCBased(_ nComponents: UInt, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider!, _ alternate: CGColorSpace!) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateICCBased(_ nComponents: Int, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider!, _ alternate: CGColorSpace!) -> CGColorSpace! ``` |

Modified CGColorSpaceCreateIndexed(CGColorSpace!, Int, UnsafePointer<UInt8>) -> CGColorSpace!

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace!, _ lastIndex: UInt, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace! ``` |
| To | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace!, _ lastIndex: Int, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace! ``` |

Modified CGColorSpaceGetColorTableCount(CGColorSpace!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace!) -> UInt ``` |
| To | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace!) -> Int ``` |

Modified CGColorSpaceGetNumberOfComponents(CGColorSpace!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace!) -> UInt ``` |
| To | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace!) -> Int ``` |

Modified CGContextAddLines(CGContext!, UnsafePointer<CGPoint>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddLines(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: UInt) ``` |
| To | ``` func CGContextAddLines(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified CGContextAddRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextAddRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: UInt) ``` |
| To | ``` func CGContextAddRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified CGContextClipToRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextClipToRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: UInt) ``` |
| To | ``` func CGContextClipToRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified CGContextFillRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextFillRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: UInt) ``` |
| To | ``` func CGContextFillRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified CGContextSetLineDash(CGContext!, CGFloat, UnsafePointer<CGFloat>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextSetLineDash(_ c: CGContext!, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: UInt) ``` |
| To | ``` func CGContextSetLineDash(_ c: CGContext!, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) ``` |

Modified CGContextShowGlyphsAtPositions(CGContext!, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextShowGlyphsAtPositions(_ context: CGContext!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: UInt) ``` |
| To | ``` func CGContextShowGlyphsAtPositions(_ context: CGContext!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified CGContextStrokeLineSegments(CGContext!, UnsafePointer<CGPoint>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGContextStrokeLineSegments(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: UInt) ``` |
| To | ``` func CGContextStrokeLineSegments(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified CGDataConsumerPutBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerPutBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataConsumerPutBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Int)> ``` |

Modified CGDataProviderCreateWithData(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, CGDataProviderReleaseDataCallback) -> CGDataProvider!

|  | Declaration |
| --- | --- |
| From | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: UInt, _ releaseData: CGDataProviderReleaseDataCallback) -> CGDataProvider! ``` |
| To | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: Int, _ releaseData: CGDataProviderReleaseDataCallback) -> CGDataProvider! ``` |

Modified CGDataProviderGetBytesAtPositionCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesAtPositionCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataProviderGetBytesAtPositionCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, Int) -> Int)> ``` |

Modified CGDataProviderGetBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataProviderGetBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Int)> ``` |

Modified CGDataProviderReleaseDataCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Void)> ``` |

Modified CGFontCreatePostScriptSubset(CGFont!, CFString!, CGFontPostScriptFormat, UnsafePointer<CGGlyph>, Int, UnsafePointer<CGGlyph>) -> CFData!

|  | Declaration |
| --- | --- |
| From | ``` func CGFontCreatePostScriptSubset(_ font: CGFont!, _ subsetName: CFString!, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: UInt, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` |
| To | ``` func CGFontCreatePostScriptSubset(_ font: CGFont!, _ subsetName: CFString!, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` |

Modified CGFontGetGlyphAdvances(CGFont!, UnsafePointer<CGGlyph>, Int, UnsafeMutablePointer<Int32>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetGlyphAdvances(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: UInt, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | ``` func CGFontGetGlyphAdvances(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` |

Modified CGFontGetGlyphBBoxes(CGFont!, UnsafePointer<CGGlyph>, Int, UnsafeMutablePointer<CGRect>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetGlyphBBoxes(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: UInt, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | ``` func CGFontGetGlyphBBoxes(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |

Modified CGFontGetNumberOfGlyphs(CGFont!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont!) -> UInt ``` |
| To | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont!) -> Int ``` |

Modified CGFunctionCreate(UnsafeMutablePointer<Void>, Int, UnsafePointer<CGFloat>, Int, UnsafePointer<CGFloat>, UnsafePointer<CGFunctionCallbacks>) -> CGFunction!

|  | Declaration |
| --- | --- |
| From | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: UInt, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: UInt, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction! ``` |
| To | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: Int, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: Int, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction! ``` |

Modified CGGradientCreateWithColorComponents(CGColorSpace!, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, Int) -> CGGradient!

|  | Declaration |
| --- | --- |
| From | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: UInt) -> CGGradient! ``` |
| To | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: Int) -> CGGradient! ``` |

Modified CGImageCreate(Int, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo, CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageCreate(_ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bitsPerPixel: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` |
| To | ``` func CGImageCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` |

Modified CGImageGetBitsPerComponent(CGImage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBitsPerComponent(_ image: CGImage!) -> UInt ``` |
| To | ``` func CGImageGetBitsPerComponent(_ image: CGImage!) -> Int ``` |

Modified CGImageGetBitsPerPixel(CGImage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBitsPerPixel(_ image: CGImage!) -> UInt ``` |
| To | ``` func CGImageGetBitsPerPixel(_ image: CGImage!) -> Int ``` |

Modified CGImageGetBytesPerRow(CGImage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetBytesPerRow(_ image: CGImage!) -> UInt ``` |
| To | ``` func CGImageGetBytesPerRow(_ image: CGImage!) -> Int ``` |

Modified CGImageGetHeight(CGImage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetHeight(_ image: CGImage!) -> UInt ``` |
| To | ``` func CGImageGetHeight(_ image: CGImage!) -> Int ``` |

Modified CGImageGetWidth(CGImage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGImageGetWidth(_ image: CGImage!) -> UInt ``` |
| To | ``` func CGImageGetWidth(_ image: CGImage!) -> Int ``` |

Modified CGImageMaskCreate(Int, Int, Int, Int, Int, CGDataProvider!, UnsafePointer<CGFloat>, Bool) -> CGImage!

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMaskCreate(_ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bitsPerPixel: UInt, _ bytesPerRow: UInt, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage! ``` |
| To | ``` func CGImageMaskCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage! ``` |

Modified CGPDFArrayGetArray(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |

Modified CGPDFArrayGetBoolean(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |
| To | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |

Modified CGPDFArrayGetCount(CGPDFArrayRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetCount(_ array: CGPDFArrayRef) -> UInt ``` |
| To | ``` func CGPDFArrayGetCount(_ array: CGPDFArrayRef) -> Int ``` |

Modified CGPDFArrayGetDictionary(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |

Modified CGPDFArrayGetInteger(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |
| To | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |

Modified CGPDFArrayGetName(CGPDFArrayRef, Int, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |
| To | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |

Modified CGPDFArrayGetNull(CGPDFArrayRef, Int) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetNull(_ array: CGPDFArrayRef, _ index: UInt) -> Bool ``` |
| To | ``` func CGPDFArrayGetNull(_ array: CGPDFArrayRef, _ index: Int) -> Bool ``` |

Modified CGPDFArrayGetNumber(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |
| To | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |

Modified CGPDFArrayGetObject(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |

Modified CGPDFArrayGetStream(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |

Modified CGPDFArrayGetString(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: UInt, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |

Modified CGPDFContentStreamCreateWithPage(CGPDFPage!) -> CGPDFContentStreamRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage!) -> CGPDFContentStream! ``` |
| To | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage!) -> CGPDFContentStreamRef ``` |

Modified CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStreamRef) -> CGPDFContentStreamRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStream!) -> CGPDFContentStream! ``` |
| To | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStreamRef) -> CGPDFContentStreamRef ``` |

Modified CGPDFContentStreamGetResource(CGPDFContentStreamRef, UnsafePointer<Int8>, UnsafePointer<Int8>) -> CGPDFObjectRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStream!, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef ``` |
| To | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef ``` |

Modified CGPDFContentStreamGetStreams(CGPDFContentStreamRef) -> CFArray!

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStream!) -> CFArray! ``` |
| To | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray! ``` |

Modified CGPDFContentStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFContentStreamRef = CGPDFContentStream ``` |
| To | ``` typealias CGPDFContentStreamRef = COpaquePointer ``` |

Modified CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionaryRef) -> UInt ``` |
| To | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionaryRef) -> Int ``` |

Modified CGPDFDocumentGetNumberOfPages(CGPDFDocument!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument!) -> UInt ``` |
| To | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument!) -> Int ``` |

Modified CGPDFDocumentGetPage(CGPDFDocument!, Int) -> CGPDFPage!

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument!, _ pageNumber: UInt) -> CGPDFPage! ``` |
| To | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument!, _ pageNumber: Int) -> CGPDFPage! ``` |

Modified CGPDFOperatorCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorCallback = CFunctionPointer<((CGPDFScanner!, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias CGPDFOperatorCallback = CFunctionPointer<((CGPDFScannerRef, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTable! ``` |
| To | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef ``` |

Modified CGPDFOperatorTableRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorTableRef = CGPDFOperatorTable ``` |
| To | ``` typealias CGPDFOperatorTableRef = COpaquePointer ``` |

Modified CGPDFOperatorTableSetCallback(CGPDFOperatorTableRef, UnsafePointer<Int8>, CGPDFOperatorCallback)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTable!, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback) ``` |
| To | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback) ``` |

Modified CGPDFPageGetPageNumber(CGPDFPage!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage!) -> UInt ``` |
| To | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage!) -> Int ``` |

Modified CGPDFScannerCreate(CGPDFContentStreamRef, CGPDFOperatorTableRef, UnsafeMutablePointer<Void>) -> CGPDFScannerRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStream!, _ table: CGPDFOperatorTable!, _ info: UnsafeMutablePointer<Void>) -> CGPDFScanner! ``` |
| To | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef, _ info: UnsafeMutablePointer<Void>) -> CGPDFScannerRef ``` |

Modified CGPDFScannerGetContentStream(CGPDFScannerRef) -> CGPDFContentStreamRef

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerGetContentStream(_ scanner: CGPDFScanner!) -> CGPDFContentStream! ``` |
| To | ``` func CGPDFScannerGetContentStream(_ scanner: CGPDFScannerRef) -> CGPDFContentStreamRef ``` |

Modified CGPDFScannerPopArray(CGPDFScannerRef, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |

Modified CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |
| To | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |

Modified CGPDFScannerPopDictionary(CGPDFScannerRef, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |

Modified CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |
| To | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |

Modified CGPDFScannerPopName(CGPDFScannerRef, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopName(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |
| To | ``` func CGPDFScannerPopName(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |

Modified CGPDFScannerPopNumber(CGPDFScannerRef, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |
| To | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |

Modified CGPDFScannerPopObject(CGPDFScannerRef, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |

Modified CGPDFScannerPopStream(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |

Modified CGPDFScannerPopString(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopString(_ scanner: CGPDFScanner!, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopString(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |

Modified CGPDFScannerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFScannerRef = CGPDFScanner ``` |
| To | ``` typealias CGPDFScannerRef = COpaquePointer ``` |

Modified CGPDFScannerScan(CGPDFScannerRef) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerScan(_ scanner: CGPDFScanner!) -> Bool ``` |
| To | ``` func CGPDFScannerScan(_ scanner: CGPDFScannerRef) -> Bool ``` |

Modified CGPDFStringGetLength(CGPDFStringRef) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStringGetLength(_ string: CGPDFStringRef) -> UInt ``` |
| To | ``` func CGPDFStringGetLength(_ string: CGPDFStringRef) -> Int ``` |

Modified CGPathAddLines(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGPoint>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddLines(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ points: UnsafePointer<CGPoint>, _ count: UInt) ``` |
| To | ``` func CGPathAddLines(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` |

Modified CGPathAddRects(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGRect>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func CGPathAddRects(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rects: UnsafePointer<CGRect>, _ count: UInt) ``` |
| To | ``` func CGPathAddRects(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` |

Modified CGPathCreateCopyByDashingPath(CGPath!, UnsafePointer<CGAffineTransform>, CGFloat, UnsafePointer<CGFloat>, Int) -> CGPath!

|  | Declaration |
| --- | --- |
| From | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: UInt) -> CGPath! ``` |
| To | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) -> CGPath! ``` |

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
