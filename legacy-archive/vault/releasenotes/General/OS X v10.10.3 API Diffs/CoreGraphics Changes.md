---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreGraphics.html
archived_at: '2026-07-18T02:52:12.113642Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreGraphics Changes

## CoreGraphics

Removed CGBitmapInfo.valueRemoved CGFloat.advancedBy(Int) -> CGFloatRemoved CGFloat.convertFromFloatLiteral(NativeType) -> CGFloat [static]Removed CGFloat.convertFromIntegerLiteral(Int) -> CGFloat [static]Removed CGFloat.distanceTo(CGFloat) -> IntRemoved CGFloat.predecessor() -> CGFloatRemoved CGFloat.successor() -> CGFloatRemoved CGPoint.getMirror() -> MirrorRemoved CGRect.getMirror() -> MirrorRemoved CGSize.getMirror() -> MirrorRemoved CGVector.init(_: CGFloat, _: CGFloat)Removed CGVector.init(_: Int, _: Int)Added CGAffineTransform.init()Added CGAffineTransform.init(a: CGFloat, b: CGFloat, c: CGFloat, d: CGFloat, tx: CGFloat, ty: CGFloat)Added CGBitmapInfo.init(rawValue: UInt32)Added CGDataConsumerCallbacks.init()Added CGDataConsumerCallbacks.init(putBytes: CGDataConsumerPutBytesCallback, releaseConsumer: CGDataConsumerReleaseInfoCallback)Added CGDataProviderDirectCallbacks.init()Added CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback, releaseBytePointer: CGDataProviderReleaseBytePointerCallback, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Added CGDataProviderSequentialCallbacks.init()Added CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CGDataProviderGetBytesCallback, skipForward: CGDataProviderSkipForwardCallback, rewind: CGDataProviderRewindCallback, releaseInfo: CGDataProviderReleaseInfoCallback)Added CGDeviceColor.init()Added CGDeviceColor.init(red: Float, green: Float, blue: Float)Added CGFloat.init(_: Int16)Added CGFloat.init(_: Int32)Added CGFloat.init(_: Int64)Added CGFloat.init(_: Int8)Added CGFloat.init(_: UInt16)Added CGFloat.init(_: UInt32)Added CGFloat.init(_: UInt64)Added CGFloat.init(_: UInt8)Added CGFloat.advancedBy(CGFloat) -> CGFloatAdded CGFloat.distanceTo(CGFloat) -> CGFloatAdded CGFloat.encode() -> [Word]Added CGFloat.init(floatLiteral: NativeType)Added CGFloat.getMirror() -> MirrorTypeAdded CGFloat.init(integerLiteral: Int)Added CGFunctionCallbacks.init()Added CGFunctionCallbacks.init(version: UInt32, evaluate: CGFunctionEvaluateCallback, releaseInfo: CGFunctionReleaseInfoCallback)Added CGPSConverterCallbacks.init()Added CGPSConverterCallbacks.init(version: UInt32, beginDocument: CGPSConverterBeginDocumentCallback, endDocument: CGPSConverterEndDocumentCallback, beginPage: CGPSConverterBeginPageCallback, endPage: CGPSConverterEndPageCallback, noteProgress: CGPSConverterProgressCallback, noteMessage: CGPSConverterMessageCallback, releaseInfo: CGPSConverterReleaseInfoCallback)Added CGPathElement.init()Added CGPathElement.init(type: CGPathElementType, points: UnsafeMutablePointer<CGPoint>)Added CGPatternCallbacks.init()Added CGPatternCallbacks.init(version: UInt32, drawPattern: CGPatternDrawPatternCallback, releaseInfo: CGPatternReleaseInfoCallback)Added CGPoint.getMirror() -> MirrorTypeAdded CGPoint.init(x: CGFloat, y: CGFloat)Added CGPoint.init(x: Double, y: Double)Added CGRect.getMirror() -> MirrorTypeAdded CGRect.init(origin: CGPoint, size: CGSize)Added CGRect.init(x: Double, y: Double, width: Double, height: Double)Added CGScreenUpdateMoveDelta.init()Added CGScreenUpdateMoveDelta.init(dX: Int32, dY: Int32)Added CGSize.getMirror() -> MirrorTypeAdded CGSize.init(width: CGFloat, height: CGFloat)Added CGSize.init(width: Double, height: Double)Added CGVector.init()Added CGVector.init(dx: CGFloat, dy: CGFloat)Added CGVector.init(dx: Double, dy: Double)Added CGVector.init(dx: Int, dy: Int)Added Double.init(_: CGFloat)Added Float.init(_: CGFloat)Added Int.init(_: CGFloat)Added Int16.init(_: CGFloat)Added Int32.init(_: CGFloat)Added Int64.init(_: CGFloat)Added Int8.init(_: CGFloat)Added UInt.init(_: CGFloat)Added UInt16.init(_: CGFloat)Added UInt32.init(_: CGFloat)Added UInt64.init(_: CGFloat)Added UInt8.init(_: CGFloat)Added CGPDFContentStreamRelease(CGPDFContentStreamRef)Added CGPDFContentStreamRetain(CGPDFContentStreamRef) -> CGPDFContentStreamRefAdded CGPDFOperatorTableRelease(CGPDFOperatorTableRef)Added CGPDFOperatorTableRetain(CGPDFOperatorTableRef) -> CGPDFOperatorTableRefAdded CGPDFScannerRelease(CGPDFScannerRef)Added CGPDFScannerRetain(CGPDFScannerRef) -> CGPDFScannerRefAdded kCGDisplayBitsPerPixelAdded kCGDisplayBitsPerSampleAdded kCGDisplayBytesPerRowAdded kCGDisplayHeightAdded kCGDisplayIOFlagsAdded kCGDisplayModeAdded kCGDisplayModeIsInterlacedAdded kCGDisplayModeIsSafeForHardwareAdded kCGDisplayModeIsStretchedAdded kCGDisplayModeIsTelevisionOutputAdded kCGDisplayModeUsableForDesktopGUIAdded kCGDisplayRefreshRateAdded kCGDisplaySamplesPerPixelAdded kCGDisplayWidthAdded kCGIODisplayModeIDAdded kCGSessionConsoleSetKeyAdded kCGSessionLoginDoneKeyAdded kCGSessionOnConsoleKeyAdded kCGSessionUserIDKeyAdded kCGSessionUserNameKeyModified CGAffineTransform [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat } ``` |
| To | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat     init()     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat) } ``` |

Modified CGBitmapInfo [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct CGBitmapInfo : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct CGBitmapInfo : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | RawOptionSetType | OS X 10.4 |

Modified CGBitmapInfo.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

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

Modified CGDeviceColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGDeviceColor {     var red: Float     var green: Float     var blue: Float } ``` |
| To | ``` struct CGDeviceColor {     var red: Float     var green: Float     var blue: Float     init()     init(red red: Float, green green: Float, blue blue: Float) } ``` |

Modified CGFloat [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Int)     init(_ value: UInt)     init(_ value: Float)     init(_ value: Double)     var native: NativeType } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointNumber, Hashable, IntegerLiteralConvertible, Printable, RandomAccessIndex |
| To | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |

Modified CGFunctionCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback     var releaseInfo: CGFunctionReleaseInfoCallback } ``` |
| To | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback     var releaseInfo: CGFunctionReleaseInfoCallback     init()     init(version version: UInt32, evaluate evaluate: CGFunctionEvaluateCallback, releaseInfo releaseInfo: CGFunctionReleaseInfoCallback) } ``` |

Modified CGPSConverterCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGPSConverterCallbacks {     var version: UInt32     var beginDocument: CGPSConverterBeginDocumentCallback     var endDocument: CGPSConverterEndDocumentCallback     var beginPage: CGPSConverterBeginPageCallback     var endPage: CGPSConverterEndPageCallback     var noteProgress: CGPSConverterProgressCallback     var noteMessage: CGPSConverterMessageCallback     var releaseInfo: CGPSConverterReleaseInfoCallback } ``` |
| To | ``` struct CGPSConverterCallbacks {     var version: UInt32     var beginDocument: CGPSConverterBeginDocumentCallback     var endDocument: CGPSConverterEndDocumentCallback     var beginPage: CGPSConverterBeginPageCallback     var endPage: CGPSConverterEndPageCallback     var noteProgress: CGPSConverterProgressCallback     var noteMessage: CGPSConverterMessageCallback     var releaseInfo: CGPSConverterReleaseInfoCallback     init()     init(version version: UInt32, beginDocument beginDocument: CGPSConverterBeginDocumentCallback, endDocument endDocument: CGPSConverterEndDocumentCallback, beginPage beginPage: CGPSConverterBeginPageCallback, endPage endPage: CGPSConverterEndPageCallback, noteProgress noteProgress: CGPSConverterProgressCallback, noteMessage noteMessage: CGPSConverterMessageCallback, releaseInfo releaseInfo: CGPSConverterReleaseInfoCallback) } ``` |

Modified CGPathElement [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafePointer<CGPoint> } ``` |
| To | ``` struct CGPathElement {     var type: CGPathElementType     var points: UnsafeMutablePointer<CGPoint>     init()     init(type type: CGPathElementType, points points: UnsafeMutablePointer<CGPoint>) } ``` |

Modified CGPathElement.points

|  | Declaration |
| --- | --- |
| From | ``` var points: UnsafePointer<CGPoint> ``` |
| To | ``` var points: UnsafeMutablePointer<CGPoint> ``` |

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

Modified CGRect.inset(CGFloat, dy: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func inset(dx dx: CGFloat, dy dy: CGFloat) ``` |
| To | ``` mutating func inset(dx dx: CGFloat, dy dy: CGFloat) ``` |

Modified CGRect.integerize()

|  | Declaration |
| --- | --- |
| From | ``` func integerize() ``` |
| To | ``` mutating func integerize() ``` |

Modified CGRect.intersect(CGRect)

|  | Declaration |
| --- | --- |
| From | ``` func intersect(_ withRect: CGRect) ``` |
| To | ``` mutating func intersect(_ withRect: CGRect) ``` |

Modified CGRect.offset(CGFloat, dy: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func offset(dx dx: CGFloat, dy dy: CGFloat) ``` |
| To | ``` mutating func offset(dx dx: CGFloat, dy dy: CGFloat) ``` |

Modified CGRect.standardize()

|  | Declaration |
| --- | --- |
| From | ``` func standardize() ``` |
| To | ``` mutating func standardize() ``` |

Modified CGRect.union(CGRect)

|  | Declaration |
| --- | --- |
| From | ``` func union(_ withRect: CGRect) ``` |
| To | ``` mutating func union(_ withRect: CGRect) ``` |

Modified CGScreenUpdateMoveDelta [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CGScreenUpdateMoveDelta {     var dX: Int32     var dY: Int32 } ``` |
| To | ``` struct CGScreenUpdateMoveDelta {     var dX: Int32     var dY: Int32     init()     init(dX dX: Int32, dY dY: Int32) } ``` |

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

Modified CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGAcquireDisplayFadeReservation(_ seconds: CGDisplayReservationInterval, _ token: UnsafePointer<CGDisplayFadeReservationToken>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGAcquireDisplayFadeReservation(_ seconds: CGDisplayReservationInterval, _ token: UnsafeMutablePointer<CGDisplayFadeReservationToken>) -> CGError ``` | OS X 10.2 |

Modified CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformEqualToTransform(CGAffineTransform, CGAffineTransform) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGAffineTransformIdentity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformIsIdentity(CGAffineTransform) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBeginDisplayConfiguration(_ config: UnsafePointer<Unmanaged<CGDisplayConfig>?>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGBeginDisplayConfiguration(_ config: UnsafeMutablePointer<CGDisplayConfigRef>) -> CGError ``` | OS X 10.0 |

Modified CGBitmapContextCreate(UnsafeMutablePointer<Void>, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo) -> CGContext!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextCreate(_ data: UnsafePointer<()>, _ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo) -> CGContext! ``` | OS X 10.10 |
| To | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo) -> CGContext! ``` | OS X 10.0 |

Modified CGBitmapContextCreateImage(CGContext!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGBitmapContextCreateWithData(UnsafeMutablePointer<Void>, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo, CGBitmapContextReleaseDataCallback, UnsafeMutablePointer<Void>) -> CGContext!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextCreateWithData(_ data: UnsafePointer<()>, _ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ releaseCallback: CGBitmapContextReleaseDataCallback, _ releaseInfo: UnsafePointer<()>) -> CGContext! ``` | OS X 10.10 |
| To | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ releaseCallback: CGBitmapContextReleaseDataCallback, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext! ``` | OS X 10.6 |

Modified CGBitmapContextGetAlphaInfo(CGContext!) -> CGImageAlphaInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGBitmapContextGetBitmapInfo(CGContext!) -> CGBitmapInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGBitmapContextGetBitsPerComponent(CGContext!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext!) -> Int ``` | OS X 10.2 |

Modified CGBitmapContextGetBitsPerPixel(CGContext!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext!) -> Int ``` | OS X 10.2 |

Modified CGBitmapContextGetBytesPerRow(CGContext!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext!) -> Int ``` | OS X 10.2 |

Modified CGBitmapContextGetColorSpace(CGContext!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGBitmapContextGetData(CGContext!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetData(_ context: CGContext!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetData(_ context: CGContext!) -> UnsafeMutablePointer<Void> ``` | OS X 10.2 |

Modified CGBitmapContextGetHeight(CGContext!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetHeight(_ context: CGContext!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetHeight(_ context: CGContext!) -> Int ``` | OS X 10.2 |

Modified CGBitmapContextGetWidth(CGContext!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGBitmapContextGetWidth(_ context: CGContext!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGBitmapContextGetWidth(_ context: CGContext!) -> Int ``` | OS X 10.2 |

Modified CGBitmapContextReleaseDataCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGBitmapContextReleaseDataCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGBitmapContextReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGCancelDisplayConfiguration(CGDisplayConfigRef) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGCancelDisplayConfiguration(_ config: CGDisplayConfig!) -> CGError ``` | OS X 10.10 |
| To | ``` func CGCancelDisplayConfiguration(_ config: CGDisplayConfigRef) -> CGError ``` | OS X 10.0 |

Modified CGCaptureAllDisplays() -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorCreate(CGColorSpace!, UnsafePointer<CGFloat>) -> CGColor!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorCreate(_ space: CGColorSpace!, _ components: ConstUnsafePointer<CGFloat>) -> CGColor! ``` | OS X 10.10 |
| To | ``` func CGColorCreate(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>) -> CGColor! ``` | OS X 10.3 |

Modified CGColorCreateCopy(CGColor!) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorCreateCopyWithAlpha(CGColor!, CGFloat) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorCreateGenericCMYK(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorCreateGenericGray(CGFloat, CGFloat) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorCreateGenericRGB(CGFloat, CGFloat, CGFloat, CGFloat) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorCreateWithPattern(CGColorSpace!, CGPattern!, UnsafePointer<CGFloat>) -> CGColor!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorCreateWithPattern(_ space: CGColorSpace!, _ pattern: CGPattern!, _ components: ConstUnsafePointer<CGFloat>) -> CGColor! ``` | OS X 10.10 |
| To | ``` func CGColorCreateWithPattern(_ space: CGColorSpace!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) -> CGColor! ``` | OS X 10.3 |

Modified CGColorEqualToColor(CGColor!, CGColor!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorGetAlpha(CGColor!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorGetColorSpace(CGColor!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorGetComponents(CGColor!) -> UnsafePointer<CGFloat>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorGetComponents(_ color: CGColor!) -> ConstUnsafePointer<CGFloat> ``` | OS X 10.10 |
| To | ``` func CGColorGetComponents(_ color: CGColor!) -> UnsafePointer<CGFloat> ``` | OS X 10.3 |

Modified CGColorGetConstantColor(CFString!) -> CGColor!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorGetNumberOfComponents(CGColor!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorGetNumberOfComponents(_ color: CGColor!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGColorGetNumberOfComponents(_ color: CGColor!) -> Int ``` | OS X 10.3 |

Modified CGColorGetPattern(CGColor!) -> CGPattern!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGColorSpaceCopyICCProfile(CGColorSpace!) -> CFData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorSpaceCopyName(CGColorSpace!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGColorSpaceCreateCalibratedGray(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, CGFloat) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateCalibratedGray(_ whitePoint: ConstUnsafePointer<CGFloat>, _ blackPoint: ConstUnsafePointer<CGFloat>, _ gamma: CGFloat) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateCalibratedGray(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: CGFloat) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceCreateCalibratedRGB(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateCalibratedRGB(_ whitePoint: ConstUnsafePointer<CGFloat>, _ blackPoint: ConstUnsafePointer<CGFloat>, _ gamma: ConstUnsafePointer<CGFloat>, _ matrix: ConstUnsafePointer<CGFloat>) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateCalibratedRGB(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: UnsafePointer<CGFloat>, _ matrix: UnsafePointer<CGFloat>) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceCreateDeviceCMYK() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGColorSpaceCreateDeviceGray() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGColorSpaceCreateDeviceRGB() -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGColorSpaceCreateICCBased(Int, UnsafePointer<CGFloat>, CGDataProvider!, CGColorSpace!) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateICCBased(_ nComponents: UInt, _ range: ConstUnsafePointer<CGFloat>, _ profile: CGDataProvider!, _ alternate: CGColorSpace!) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateICCBased(_ nComponents: Int, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider!, _ alternate: CGColorSpace!) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceCreateIndexed(CGColorSpace!, Int, UnsafePointer<UInt8>) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace!, _ lastIndex: UInt, _ colorTable: ConstUnsafePointer<UInt8>) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace!, _ lastIndex: Int, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceCreateLab(UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateLab(_ whitePoint: ConstUnsafePointer<CGFloat>, _ blackPoint: ConstUnsafePointer<CGFloat>, _ range: ConstUnsafePointer<CGFloat>) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateLab(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ range: UnsafePointer<CGFloat>) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceCreatePattern(CGColorSpace!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGColorSpaceCreateWithICCProfile(CFData!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorSpaceCreateWithName(CFString!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGColorSpaceCreateWithPlatformColorSpace(UnsafePointer<Void>) -> CGColorSpace!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceCreateWithPlatformColorSpace(_ ref: ConstUnsafePointer<()>) -> CGColorSpace! ``` | OS X 10.10 |
| To | ``` func CGColorSpaceCreateWithPlatformColorSpace(_ ref: UnsafePointer<Void>) -> CGColorSpace! ``` | OS X 10.0 |

Modified CGColorSpaceGetBaseColorSpace(CGColorSpace!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorSpaceGetColorTable(CGColorSpace!, UnsafeMutablePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceGetColorTable(_ space: CGColorSpace!, _ table: UnsafePointer<UInt8>) ``` | OS X 10.10 |
| To | ``` func CGColorSpaceGetColorTable(_ space: CGColorSpace!, _ table: UnsafeMutablePointer<UInt8>) ``` | OS X 10.5 |

Modified CGColorSpaceGetColorTableCount(CGColorSpace!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGColorSpaceGetColorTableCount(_ space: CGColorSpace!) -> Int ``` | OS X 10.5 |

Modified CGColorSpaceGetModel(CGColorSpace!) -> CGColorSpaceModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGColorSpaceGetNumberOfComponents(CGColorSpace!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace!) -> Int ``` | OS X 10.0 |

Modified CGColorSpaceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGCompleteDisplayConfiguration(CGDisplayConfigRef, CGConfigureOption) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGCompleteDisplayConfiguration(_ config: CGDisplayConfig!, _ option: CGConfigureOption) -> CGError ``` | OS X 10.10 |
| To | ``` func CGCompleteDisplayConfiguration(_ config: CGDisplayConfigRef, _ option: CGConfigureOption) -> CGError ``` | OS X 10.0 |

Modified CGConfigureDisplayFadeEffect(CGDisplayConfigRef, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGConfigureDisplayFadeEffect(_ config: CGDisplayConfig!, _ fadeOutSeconds: CGDisplayFadeInterval, _ fadeInSeconds: CGDisplayFadeInterval, _ fadeRed: Float, _ fadeGreen: Float, _ fadeBlue: Float) -> CGError ``` | OS X 10.10 |
| To | ``` func CGConfigureDisplayFadeEffect(_ config: CGDisplayConfigRef, _ fadeOutSeconds: CGDisplayFadeInterval, _ fadeInSeconds: CGDisplayFadeInterval, _ fadeRed: Float, _ fadeGreen: Float, _ fadeBlue: Float) -> CGError ``` | OS X 10.2 |

Modified CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef, CGDirectDisplayID, CGDirectDisplayID) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGConfigureDisplayMirrorOfDisplay(_ config: CGDisplayConfig!, _ display: CGDirectDisplayID, _ master: CGDirectDisplayID) -> CGError ``` | OS X 10.10 |
| To | ``` func CGConfigureDisplayMirrorOfDisplay(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ master: CGDirectDisplayID) -> CGError ``` | OS X 10.2 |

Modified CGConfigureDisplayOrigin(CGDisplayConfigRef, CGDirectDisplayID, Int32, Int32) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGConfigureDisplayOrigin(_ config: CGDisplayConfig!, _ display: CGDirectDisplayID, _ x: Int32, _ y: Int32) -> CGError ``` | OS X 10.10 |
| To | ``` func CGConfigureDisplayOrigin(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ x: Int32, _ y: Int32) -> CGError ``` | OS X 10.0 |

Modified CGConfigureDisplayStereoOperation(CGDisplayConfigRef, CGDirectDisplayID, boolean_t, boolean_t) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGConfigureDisplayStereoOperation(_ config: CGDisplayConfig!, _ display: CGDirectDisplayID, _ stereo: boolean_t, _ forceBlueLine: boolean_t) -> CGError ``` | OS X 10.10 |
| To | ``` func CGConfigureDisplayStereoOperation(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ stereo: boolean_t, _ forceBlueLine: boolean_t) -> CGError ``` | OS X 10.4 |

Modified CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef, CGDirectDisplayID, CGDisplayMode!, CFDictionary!) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfig!, _ display: CGDirectDisplayID, _ mode: CGDisplayMode!, _ options: CFDictionary!) -> CGError ``` | OS X 10.10 |
| To | ``` func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfigRef, _ display: CGDirectDisplayID, _ mode: CGDisplayMode!, _ options: CFDictionary!) -> CGError ``` | OS X 10.6 |

Modified CGContextAddArc(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, Int32)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddArcToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddCurveToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextAddLineToPoint(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddLines(CGContext!, UnsafePointer<CGPoint>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextAddLines(_ c: CGContext!, _ points: ConstUnsafePointer<CGPoint>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextAddLines(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` | OS X 10.0 |

Modified CGContextAddPath(CGContext!, CGPath!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextAddQuadCurveToPoint(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextAddRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextAddRects(_ c: CGContext!, _ rects: ConstUnsafePointer<CGRect>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextAddRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` | OS X 10.0 |

Modified CGContextBeginPage(CGContext!, UnsafePointer<CGRect>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextBeginPage(_ c: CGContext!, _ mediaBox: ConstUnsafePointer<CGRect>) ``` | OS X 10.10 |
| To | ``` func CGContextBeginPage(_ c: CGContext!, _ mediaBox: UnsafePointer<CGRect>) ``` | OS X 10.0 |

Modified CGContextBeginPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextBeginTransparencyLayer(CGContext!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextBeginTransparencyLayerWithRect(CGContext!, CGRect, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextClearRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextClip(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextClipToMask(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextClipToRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextClipToRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextClipToRects(_ c: CGContext!, _ rects: ConstUnsafePointer<CGRect>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextClipToRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` | OS X 10.0 |

Modified CGContextClosePath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextConcatCTM(CGContext!, CGAffineTransform)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextConvertPointToDeviceSpace(CGContext!, CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextConvertPointToUserSpace(CGContext!, CGPoint) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextConvertRectToDeviceSpace(CGContext!, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextConvertRectToUserSpace(CGContext!, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextConvertSizeToDeviceSpace(CGContext!, CGSize) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextConvertSizeToUserSpace(CGContext!, CGSize) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextCopyPath(CGContext!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextDrawImage(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextDrawLayerAtPoint(CGContext!, CGPoint, CGLayer!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextDrawLayerInRect(CGContext!, CGRect, CGLayer!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextDrawLinearGradient(CGContext!, CGGradient!, CGPoint, CGPoint, CGGradientDrawingOptions)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextDrawPDFPage(CGContext!, CGPDFPage!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextDrawPath(CGContext!, CGPathDrawingMode)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextDrawRadialGradient(CGContext!, CGGradient!, CGPoint, CGFloat, CGPoint, CGFloat, CGGradientDrawingOptions)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextDrawShading(CGContext!, CGShading!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextDrawTiledImage(CGContext!, CGRect, CGImage!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextEOClip(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextEOFillPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextEndPage(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextEndTransparencyLayer(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextFillEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextFillPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextFillRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextFillRects(CGContext!, UnsafePointer<CGRect>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextFillRects(_ c: CGContext!, _ rects: ConstUnsafePointer<CGRect>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextFillRects(_ c: CGContext!, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` | OS X 10.0 |

Modified CGContextFlush(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetCTM(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetClipBoundingBox(CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextGetInterpolationQuality(CGContext!) -> CGInterpolationQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetPathBoundingBox(CGContext!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetPathCurrentPoint(CGContext!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetTextMatrix(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetTextPosition(CGContext!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextGetUserSpaceToDeviceSpaceTransform(CGContext!) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextIsPathEmpty(CGContext!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextMoveToPoint(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextPathContainsPoint(CGContext!, CGPoint, CGPathDrawingMode) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextReplacePathWithStrokedPath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextRestoreGState(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextRotateCTM(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSaveGState(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextScaleCTM(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetAllowsAntialiasing(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextSetAllowsFontSmoothing(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextSetAllowsFontSubpixelPositioning(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextSetAllowsFontSubpixelQuantization(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextSetAlpha(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetBlendMode(CGContext!, CGBlendMode)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextSetCMYKFillColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetCMYKStrokeColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetCharacterSpacing(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetFillColor(CGContext!, UnsafePointer<CGFloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextSetFillColor(_ context: CGContext!, _ components: ConstUnsafePointer<CGFloat>) ``` | OS X 10.10 |
| To | ``` func CGContextSetFillColor(_ context: CGContext!, _ components: UnsafePointer<CGFloat>) ``` | OS X 10.0 |

Modified CGContextSetFillColorSpace(CGContext!, CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetFillColorWithColor(CGContext!, CGColor!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextSetFillPattern(CGContext!, CGPattern!, UnsafePointer<CGFloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextSetFillPattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: ConstUnsafePointer<CGFloat>) ``` | OS X 10.10 |
| To | ``` func CGContextSetFillPattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) ``` | OS X 10.0 |

Modified CGContextSetFlatness(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetFont(CGContext!, CGFont!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetFontSize(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetGrayFillColor(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetGrayStrokeColor(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetInterpolationQuality(CGContext!, CGInterpolationQuality)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetLineCap(CGContext!, CGLineCap)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetLineDash(CGContext!, CGFloat, UnsafePointer<CGFloat>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextSetLineDash(_ c: CGContext!, _ phase: CGFloat, _ lengths: ConstUnsafePointer<CGFloat>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextSetLineDash(_ c: CGContext!, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) ``` | OS X 10.0 |

Modified CGContextSetLineJoin(CGContext!, CGLineJoin)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetLineWidth(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetMiterLimit(CGContext!, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetPatternPhase(CGContext!, CGSize)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetRGBFillColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetRGBStrokeColor(CGContext!, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetRenderingIntent(CGContext!, CGColorRenderingIntent)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetShadow(CGContext!, CGSize, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextSetShadowWithColor(CGContext!, CGSize, CGFloat, CGColor!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextSetShouldAntialias(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetShouldSmoothFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGContextSetShouldSubpixelPositionFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextSetShouldSubpixelQuantizeFonts(CGContext!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGContextSetStrokeColor(CGContext!, UnsafePointer<CGFloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextSetStrokeColor(_ context: CGContext!, _ components: ConstUnsafePointer<CGFloat>) ``` | OS X 10.10 |
| To | ``` func CGContextSetStrokeColor(_ context: CGContext!, _ components: UnsafePointer<CGFloat>) ``` | OS X 10.0 |

Modified CGContextSetStrokeColorSpace(CGContext!, CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetStrokeColorWithColor(CGContext!, CGColor!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGContextSetStrokePattern(CGContext!, CGPattern!, UnsafePointer<CGFloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextSetStrokePattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: ConstUnsafePointer<CGFloat>) ``` | OS X 10.10 |
| To | ``` func CGContextSetStrokePattern(_ context: CGContext!, _ pattern: CGPattern!, _ components: UnsafePointer<CGFloat>) ``` | OS X 10.0 |

Modified CGContextSetTextDrawingMode(CGContext!, CGTextDrawingMode)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetTextMatrix(CGContext!, CGAffineTransform)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSetTextPosition(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextShowGlyphsAtPositions(CGContext!, UnsafePointer<CGGlyph>, UnsafePointer<CGPoint>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextShowGlyphsAtPositions(_ context: CGContext!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ positions: ConstUnsafePointer<CGPoint>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextShowGlyphsAtPositions(_ context: CGContext!, _ glyphs: UnsafePointer<CGGlyph>, _ positions: UnsafePointer<CGPoint>, _ count: Int) ``` | OS X 10.5 |

Modified CGContextStrokeEllipseInRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGContextStrokeLineSegments(CGContext!, UnsafePointer<CGPoint>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGContextStrokeLineSegments(_ c: CGContext!, _ points: ConstUnsafePointer<CGPoint>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGContextStrokeLineSegments(_ c: CGContext!, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` | OS X 10.4 |

Modified CGContextStrokePath(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextStrokeRect(CGContext!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextStrokeRectWithWidth(CGContext!, CGRect, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextSynchronize(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGContextTranslateCTM(CGContext!, CGFloat, CGFloat)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDataConsumerCreate(UnsafeMutablePointer<Void>, UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDataConsumerCreate(_ info: UnsafePointer<()>, _ callbacks: ConstUnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer! ``` | OS X 10.10 |
| To | ``` func CGDataConsumerCreate(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer! ``` | OS X 10.0 |

Modified CGDataConsumerCreateWithCFData(CFMutableData!) -> CGDataConsumer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGDataConsumerCreateWithURL(CFURL!) -> CGDataConsumer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDataConsumerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDataConsumerPutBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerPutBytesCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataConsumerPutBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Int)> ``` |

Modified CGDataConsumerReleaseInfoCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerReleaseInfoCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGDataConsumerReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGDataProviderCopyData(CGDataProvider!) -> CFData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGDataProviderCreateDirect(UnsafeMutablePointer<Void>, off_t, UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDataProviderCreateDirect(_ info: UnsafePointer<()>, _ size: off_t, _ callbacks: ConstUnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider! ``` | OS X 10.10 |
| To | ``` func CGDataProviderCreateDirect(_ info: UnsafeMutablePointer<Void>, _ size: off_t, _ callbacks: UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider! ``` | OS X 10.5 |

Modified CGDataProviderCreateSequential(UnsafeMutablePointer<Void>, UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDataProviderCreateSequential(_ info: UnsafePointer<()>, _ callbacks: ConstUnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider! ``` | OS X 10.10 |
| To | ``` func CGDataProviderCreateSequential(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider! ``` | OS X 10.5 |

Modified CGDataProviderCreateWithCFData(CFData!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGDataProviderCreateWithData(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, CGDataProviderReleaseDataCallback) -> CGDataProvider!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDataProviderCreateWithData(_ info: UnsafePointer<()>, _ data: ConstUnsafePointer<()>, _ size: UInt, _ releaseData: CGDataProviderReleaseDataCallback) -> CGDataProvider! ``` | OS X 10.10 |
| To | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: Int, _ releaseData: CGDataProviderReleaseDataCallback) -> CGDataProvider! ``` | OS X 10.0 |

Modified CGDataProviderCreateWithFilename(UnsafePointer<Int8>) -> CGDataProvider!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDataProviderCreateWithFilename(_ filename: ConstUnsafePointer<Int8>) -> CGDataProvider! ``` | OS X 10.10 |
| To | ``` func CGDataProviderCreateWithFilename(_ filename: UnsafePointer<Int8>) -> CGDataProvider! ``` | OS X 10.0 |

Modified CGDataProviderCreateWithURL(CFURL!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDataProviderGetBytePointerCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytePointerCallback = CFunctionPointer<((UnsafePointer<()>) -> ConstUnsafePointer<()>)> ``` |
| To | ``` typealias CGDataProviderGetBytePointerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafePointer<Void>)> ``` |

Modified CGDataProviderGetBytesAtPositionCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesAtPositionCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, off_t, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataProviderGetBytesAtPositionCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, Int) -> Int)> ``` |

Modified CGDataProviderGetBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, UInt) -> UInt)> ``` |
| To | ``` typealias CGDataProviderGetBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Int)> ``` |

Modified CGDataProviderGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDataProviderReleaseBytePointerCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseBytePointerCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseBytePointerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void)> ``` |

Modified CGDataProviderReleaseDataCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseDataCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>, UInt) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseDataCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Void)> ``` |

Modified CGDataProviderReleaseInfoCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseInfoCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGDataProviderReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGDataProviderRewindCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderRewindCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGDataProviderRewindCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGDataProviderSkipForwardCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderSkipForwardCallback = CFunctionPointer<((UnsafePointer<()>, off_t) -> off_t)> ``` |
| To | ``` typealias CGDataProviderSkipForwardCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, off_t) -> off_t)> ``` |

Modified CGDisplayBounds(CGDirectDisplayID) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayCapture(CGDirectDisplayID) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayCaptureWithOptions(CGDirectDisplayID, CGCaptureOptions) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGDisplayConfigRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDisplayConfigRef = CGDisplayConfig ``` |
| To | ``` typealias CGDisplayConfigRef = COpaquePointer ``` |

Modified CGDisplayCopyAllDisplayModes(CGDirectDisplayID, CFDictionary!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayCopyColorSpace(CGDirectDisplayID) -> Unmanaged<CGColorSpace>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGDisplayCopyDisplayMode(CGDirectDisplayID) -> Unmanaged<CGDisplayMode>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayCreateImage(CGDirectDisplayID) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayCreateImageForRect(CGDirectDisplayID, CGRect) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayFade(CGDisplayFadeReservationToken, CGDisplayFadeInterval, CGDisplayBlendFraction, CGDisplayBlendFraction, Float, Float, Float, boolean_t) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayGammaTableCapacity(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGDisplayGetDrawingContext(CGDirectDisplayID) -> Unmanaged<CGContext>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGDisplayHideCursor(CGDirectDisplayID) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayIDToOpenGLDisplayMask(CGDirectDisplayID) -> CGOpenGLDisplayMask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayIsActive(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsAlwaysInMirrorSet(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsAsleep(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsBuiltin(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsInHWMirrorSet(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsInMirrorSet(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsMain(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsOnline(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayIsStereo(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGDisplayMirrorsDisplay(CGDirectDisplayID) -> CGDirectDisplayID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayModeCopyPixelEncoding(CGDisplayMode!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModeGetHeight(CGDisplayMode!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayModeGetHeight(_ mode: CGDisplayMode!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayModeGetHeight(_ mode: CGDisplayMode!) -> Int ``` | OS X 10.6 |

Modified CGDisplayModeGetIODisplayModeID(CGDisplayMode!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModeGetIOFlags(CGDisplayMode!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModeGetPixelHeight(CGDisplayMode!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayModeGetPixelHeight(_ mode: CGDisplayMode!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayModeGetPixelHeight(_ mode: CGDisplayMode!) -> Int ``` | OS X 10.8 |

Modified CGDisplayModeGetPixelWidth(CGDisplayMode!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayModeGetPixelWidth(_ mode: CGDisplayMode!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayModeGetPixelWidth(_ mode: CGDisplayMode!) -> Int ``` | OS X 10.8 |

Modified CGDisplayModeGetRefreshRate(CGDisplayMode!) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModeGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModeGetWidth(CGDisplayMode!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayModeGetWidth(_ mode: CGDisplayMode!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayModeGetWidth(_ mode: CGDisplayMode!) -> Int ``` | OS X 10.6 |

Modified CGDisplayModeIsUsableForDesktopGUI(CGDisplayMode!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplayModelNumber(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayMoveCursorToPoint(CGDirectDisplayID, CGPoint) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayPixelsHigh(CGDirectDisplayID) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayPixelsHigh(_ display: CGDirectDisplayID) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayPixelsHigh(_ display: CGDirectDisplayID) -> Int ``` | OS X 10.0 |

Modified CGDisplayPixelsWide(CGDirectDisplayID) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayPixelsWide(_ display: CGDirectDisplayID) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayPixelsWide(_ display: CGDirectDisplayID) -> Int ``` | OS X 10.0 |

Modified CGDisplayPrimaryDisplay(CGDirectDisplayID) -> CGDirectDisplayID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayReconfigurationCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDisplayReconfigurationCallBack = CFunctionPointer<((CGDirectDisplayID, CGDisplayChangeSummaryFlags, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGDisplayReconfigurationCallBack = CFunctionPointer<((CGDirectDisplayID, CGDisplayChangeSummaryFlags, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGDisplayRegisterReconfigurationCallback(CGDisplayReconfigurationCallBack, UnsafeMutablePointer<Void>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayRegisterReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafePointer<()>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGDisplayRegisterReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` | OS X 10.3 |

Modified CGDisplayRelease(CGDirectDisplayID) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayRemoveReconfigurationCallback(CGDisplayReconfigurationCallBack, UnsafeMutablePointer<Void>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayRemoveReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafePointer<()>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGDisplayRemoveReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> CGError ``` | OS X 10.3 |

Modified CGDisplayRestoreColorSyncSettings()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayRotation(CGDirectDisplayID) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGDisplayScreenSize(CGDirectDisplayID) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGDisplaySerialNumber(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplaySetDisplayMode(CGDirectDisplayID, CGDisplayMode!, CFDictionary!) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGDisplaySetStereoOperation(CGDirectDisplayID, boolean_t, boolean_t, CGConfigureOption) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGDisplayShowCursor(CGDirectDisplayID) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGDisplayStreamCreate(CGDirectDisplayID, Int, Int, Int32, CFDictionary!, CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayStreamCreate(_ display: CGDirectDisplayID, _ outputWidth: UInt, _ outputHeight: UInt, _ pixelFormat: Int32, _ properties: CFDictionary!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` | OS X 10.10 |
| To | ``` func CGDisplayStreamCreate(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` | OS X 10.8 |

Modified CGDisplayStreamCreateWithDispatchQueue(CGDirectDisplayID, Int, Int, Int32, CFDictionary!, dispatch_queue_t!, CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayStreamCreateWithDispatchQueue(_ display: CGDirectDisplayID, _ outputWidth: UInt, _ outputHeight: UInt, _ pixelFormat: Int32, _ properties: CFDictionary!, _ queue: dispatch_queue_t!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` | OS X 10.10 |
| To | ``` func CGDisplayStreamCreateWithDispatchQueue(_ display: CGDirectDisplayID, _ outputWidth: Int, _ outputHeight: Int, _ pixelFormat: Int32, _ properties: CFDictionary!, _ queue: dispatch_queue_t!, _ handler: CGDisplayStreamFrameAvailableHandler!) -> Unmanaged<CGDisplayStream>! ``` | OS X 10.8 |

Modified CGDisplayStreamGetRunLoopSource(CGDisplayStream!) -> Unmanaged<CFRunLoopSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayStreamGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayStreamStart(CGDisplayStream!) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayStreamStop(CGDisplayStream!) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayStreamUpdateCreateMergedUpdate(CGDisplayStreamUpdate!, CGDisplayStreamUpdate!) -> Unmanaged<CGDisplayStreamUpdate>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayStreamUpdateGetDropCount(CGDisplayStreamUpdate!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayStreamUpdateGetDropCount(_ updateRef: CGDisplayStreamUpdate!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGDisplayStreamUpdateGetDropCount(_ updateRef: CGDisplayStreamUpdate!) -> Int ``` | OS X 10.8 |

Modified CGDisplayStreamUpdateGetMovedRectsDelta(CGDisplayStreamUpdate!, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayStreamUpdateGetMovedRectsDelta(_ updateRef: CGDisplayStreamUpdate!, _ dx: UnsafePointer<CGFloat>, _ dy: UnsafePointer<CGFloat>) ``` | OS X 10.10 |
| To | ``` func CGDisplayStreamUpdateGetMovedRectsDelta(_ updateRef: CGDisplayStreamUpdate!, _ dx: UnsafeMutablePointer<CGFloat>, _ dy: UnsafeMutablePointer<CGFloat>) ``` | OS X 10.8 |

Modified CGDisplayStreamUpdateGetRects(CGDisplayStreamUpdate!, CGDisplayStreamUpdateRectType, UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGDisplayStreamUpdateGetRects(_ updateRef: CGDisplayStreamUpdate!, _ rectType: CGDisplayStreamUpdateRectType, _ rectCount: UnsafePointer<UInt>) -> ConstUnsafePointer<CGRect> ``` | OS X 10.10 |
| To | ``` func CGDisplayStreamUpdateGetRects(_ updateRef: CGDisplayStreamUpdate!, _ rectType: CGDisplayStreamUpdateRectType, _ rectCount: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect> ``` | OS X 10.8 |

Modified CGDisplayStreamUpdateGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGDisplayUnitNumber(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayUsesOpenGLAcceleration(CGDirectDisplayID) -> boolean_t

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGDisplayVendorNumber(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGEventCreate(CGEventSource!) -> Unmanaged<CGEvent>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateCopy(CGEvent!) -> Unmanaged<CGEvent>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateData(CFAllocator!, CGEvent!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateFromData(CFAllocator!, CFData!) -> Unmanaged<CGEvent>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateKeyboardEvent(CGEventSource!, CGKeyCode, Bool) -> Unmanaged<CGEvent>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateMouseEvent(CGEventSource!, CGEventType, CGPoint, CGMouseButton) -> Unmanaged<CGEvent>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventCreateSourceFromEvent(CGEvent!) -> Unmanaged<CGEventSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetDoubleValueField(CGEvent!, CGEventField) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetFlags(CGEvent!) -> CGEventFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetIntegerValueField(CGEvent!, CGEventField) -> Int64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetLocation(CGEvent!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetTimestamp(CGEvent!) -> CGEventTimestamp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetType(CGEvent!) -> CGEventType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventGetUnflippedLocation(CGEvent!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGEventKeyboardGetUnicodeString(CGEvent!, Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UniChar>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGEventKeyboardGetUnicodeString(_ event: CGEvent!, _ maxStringLength: UniCharCount, _ actualStringLength: UnsafePointer<UniCharCount>, _ unicodeString: UnsafePointer<UniChar>) ``` | OS X 10.10 |
| To | ``` func CGEventKeyboardGetUnicodeString(_ event: CGEvent!, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>, _ unicodeString: UnsafeMutablePointer<UniChar>) ``` | OS X 10.4 |

Modified CGEventKeyboardSetUnicodeString(CGEvent!, Int, UnsafePointer<UniChar>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGEventKeyboardSetUnicodeString(_ event: CGEvent!, _ stringLength: UniCharCount, _ unicodeString: ConstUnsafePointer<UniChar>) ``` | OS X 10.10 |
| To | ``` func CGEventKeyboardSetUnicodeString(_ event: CGEvent!, _ stringLength: Int, _ unicodeString: UnsafePointer<UniChar>) ``` | OS X 10.4 |

Modified CGEventPost(CGEventTapLocation, CGEvent!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventPostToPSN(UnsafeMutablePointer<Void>, CGEvent!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGEventPostToPSN(_ processSerialNumber: UnsafePointer<()>, _ event: CGEvent!) ``` | OS X 10.10 |
| To | ``` func CGEventPostToPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ event: CGEvent!) ``` | OS X 10.4 |

Modified CGEventSetDoubleValueField(CGEvent!, CGEventField, Double)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetFlags(CGEvent!, CGEventFlags)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetIntegerValueField(CGEvent!, CGEventField, Int64)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetLocation(CGEvent!, CGPoint)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetSource(CGEvent!, CGEventSource!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetTimestamp(CGEvent!, CGEventTimestamp)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSetType(CGEvent!, CGEventType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceButtonState(CGEventSourceStateID, CGMouseButton) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceCounterForEventType(CGEventSourceStateID, CGEventType) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceCreate(CGEventSourceStateID) -> Unmanaged<CGEventSource>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceFlagsState(CGEventSourceStateID) -> CGEventFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetKeyboardType(CGEventSource!) -> CGEventSourceKeyboardType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetLocalEventsFilterDuringSuppressionState(CGEventSource!, CGEventSuppressionState) -> CGEventFilterMask

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetLocalEventsSuppressionInterval(CGEventSource!) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetPixelsPerLine(CGEventSource!) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGEventSourceGetSourceStateID(CGEventSource!) -> CGEventSourceStateID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceGetUserData(CGEventSource!) -> Int64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceKeyState(CGEventSourceStateID, CGKeyCode) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceSecondsSinceLastEventType(CGEventSourceStateID, CGEventType) -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceSetKeyboardType(CGEventSource!, CGEventSourceKeyboardType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceSetLocalEventsFilterDuringSuppressionState(CGEventSource!, CGEventFilterMask, CGEventSuppressionState)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceSetLocalEventsSuppressionInterval(CGEventSource!, CFTimeInterval)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventSourceSetPixelsPerLine(CGEventSource!, Double)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGEventSourceSetUserData(CGEventSource!, Int64)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventTapCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CGEventTapCallBack = CFunctionPointer<((CGEventTapProxy, CGEventType, CGEvent!, UnsafePointer<()>) -> Unmanaged<CGEvent>!)> ``` |
| To | ``` typealias CGEventTapCallBack = CFunctionPointer<((CGEventTapProxy, CGEventType, CGEvent!, UnsafeMutablePointer<Void>) -> Unmanaged<CGEvent>!)> ``` |

Modified CGEventTapCreate(CGEventTapLocation, CGEventTapPlacement, CGEventTapOptions, CGEventMask, CGEventTapCallBack, UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGEventTapCreate(_ tap: CGEventTapLocation, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafePointer<()>) -> Unmanaged<CFMachPort>! ``` | OS X 10.10 |
| To | ``` func CGEventTapCreate(_ tap: CGEventTapLocation, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>! ``` | OS X 10.4 |

Modified CGEventTapCreateForPSN(UnsafeMutablePointer<Void>, CGEventTapPlacement, CGEventTapOptions, CGEventMask, CGEventTapCallBack, UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGEventTapCreateForPSN(_ processSerialNumber: UnsafePointer<()>, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafePointer<()>) -> Unmanaged<CFMachPort>! ``` | OS X 10.10 |
| To | ``` func CGEventTapCreateForPSN(_ processSerialNumber: UnsafeMutablePointer<Void>, _ place: CGEventTapPlacement, _ options: CGEventTapOptions, _ eventsOfInterest: CGEventMask, _ callback: CGEventTapCallBack, _ userInfo: UnsafeMutablePointer<Void>) -> Unmanaged<CFMachPort>! ``` | OS X 10.4 |

Modified CGEventTapEnable(CFMachPort!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventTapIsEnabled(CFMachPort!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGEventTapPostEvent(CGEventTapProxy, CGEvent!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCanCreatePostScriptSubset(CGFont!, CGFontPostScriptFormat) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCopyFullName(CGFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontCopyGlyphNameForGlyph(CGFont!, CGGlyph) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontCopyPostScriptName(CGFont!) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCopyTableForTag(CGFont!, UInt32) -> CFData!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontCopyTableTags(CGFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontCopyVariationAxes(CGFont!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCopyVariations(CGFont!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCreateCopyWithVariations(CGFont!, CFDictionary!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGFontCreatePostScriptEncoding(CGFont!, UnsafePointer<CGGlyph>) -> CFData!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFontCreatePostScriptEncoding(_ font: CGFont!, _ encoding: ConstUnsafePointer<CGGlyph>) -> CFData! ``` | OS X 10.10 |
| To | ``` func CGFontCreatePostScriptEncoding(_ font: CGFont!, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` | OS X 10.4 |

Modified CGFontCreatePostScriptSubset(CGFont!, CFString!, CGFontPostScriptFormat, UnsafePointer<CGGlyph>, Int, UnsafePointer<CGGlyph>) -> CFData!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFontCreatePostScriptSubset(_ font: CGFont!, _ subsetName: CFString!, _ format: CGFontPostScriptFormat, _ glyphs: ConstUnsafePointer<CGGlyph>, _ count: UInt, _ encoding: ConstUnsafePointer<CGGlyph>) -> CFData! ``` | OS X 10.10 |
| To | ``` func CGFontCreatePostScriptSubset(_ font: CGFont!, _ subsetName: CFString!, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ encoding: UnsafePointer<CGGlyph>) -> CFData! ``` | OS X 10.4 |

Modified CGFontCreateWithDataProvider(CGDataProvider!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontCreateWithFontName(CFString!) -> CGFont!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetAscent(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetCapHeight(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetDescent(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetFontBBox(CGFont!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetGlyphAdvances(CGFont!, UnsafePointer<CGGlyph>, Int, UnsafeMutablePointer<Int32>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFontGetGlyphAdvances(_ font: CGFont!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ count: UInt, _ advances: UnsafePointer<Int32>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGFontGetGlyphAdvances(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` | OS X 10.0 |

Modified CGFontGetGlyphBBoxes(CGFont!, UnsafePointer<CGGlyph>, Int, UnsafeMutablePointer<CGRect>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFontGetGlyphBBoxes(_ font: CGFont!, _ glyphs: ConstUnsafePointer<CGGlyph>, _ count: UInt, _ bboxes: UnsafePointer<CGRect>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGFontGetGlyphBBoxes(_ font: CGFont!, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` | OS X 10.5 |

Modified CGFontGetGlyphWithGlyphName(CGFont!, CFString!) -> CGGlyph

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetItalicAngle(CGFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetLeading(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetNumberOfGlyphs(CGFont!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont!) -> Int ``` | OS X 10.0 |

Modified CGFontGetStemV(CGFont!) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFontGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGFontGetUnitsPerEm(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGFontGetXHeight(CGFont!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGFunctionCreate(UnsafeMutablePointer<Void>, Int, UnsafePointer<CGFloat>, Int, UnsafePointer<CGFloat>, UnsafePointer<CGFunctionCallbacks>) -> CGFunction!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGFunctionCreate(_ info: UnsafePointer<()>, _ domainDimension: UInt, _ domain: ConstUnsafePointer<CGFloat>, _ rangeDimension: UInt, _ range: ConstUnsafePointer<CGFloat>, _ callbacks: ConstUnsafePointer<CGFunctionCallbacks>) -> CGFunction! ``` | OS X 10.10 |
| To | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: Int, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: Int, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction! ``` | OS X 10.2 |

Modified CGFunctionEvaluateCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionEvaluateCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<CGFloat>, UnsafePointer<CGFloat>) -> Void)> ``` |
| To | ``` typealias CGFunctionEvaluateCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void)> ``` |

Modified CGFunctionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGFunctionReleaseInfoCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionReleaseInfoCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGFunctionReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGGetActiveDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetActiveDisplayList(_ maxDisplays: UInt32, _ activeDisplays: UnsafePointer<CGDirectDisplayID>, _ displayCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetActiveDisplayList(_ maxDisplays: UInt32, _ activeDisplays: UnsafeMutablePointer<CGDirectDisplayID>, _ displayCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.0 |

Modified CGGetDisplayTransferByFormula(CGDirectDisplayID, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetDisplayTransferByFormula(_ display: CGDirectDisplayID, _ redMin: UnsafePointer<CGGammaValue>, _ redMax: UnsafePointer<CGGammaValue>, _ redGamma: UnsafePointer<CGGammaValue>, _ greenMin: UnsafePointer<CGGammaValue>, _ greenMax: UnsafePointer<CGGammaValue>, _ greenGamma: UnsafePointer<CGGammaValue>, _ blueMin: UnsafePointer<CGGammaValue>, _ blueMax: UnsafePointer<CGGammaValue>, _ blueGamma: UnsafePointer<CGGammaValue>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetDisplayTransferByFormula(_ display: CGDirectDisplayID, _ redMin: UnsafeMutablePointer<CGGammaValue>, _ redMax: UnsafeMutablePointer<CGGammaValue>, _ redGamma: UnsafeMutablePointer<CGGammaValue>, _ greenMin: UnsafeMutablePointer<CGGammaValue>, _ greenMax: UnsafeMutablePointer<CGGammaValue>, _ greenGamma: UnsafeMutablePointer<CGGammaValue>, _ blueMin: UnsafeMutablePointer<CGGammaValue>, _ blueMax: UnsafeMutablePointer<CGGammaValue>, _ blueGamma: UnsafeMutablePointer<CGGammaValue>) -> CGError ``` | OS X 10.0 |

Modified CGGetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<CGGammaValue>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetDisplayTransferByTable(_ display: CGDirectDisplayID, _ capacity: UInt32, _ redTable: UnsafePointer<CGGammaValue>, _ greenTable: UnsafePointer<CGGammaValue>, _ blueTable: UnsafePointer<CGGammaValue>, _ sampleCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetDisplayTransferByTable(_ display: CGDirectDisplayID, _ capacity: UInt32, _ redTable: UnsafeMutablePointer<CGGammaValue>, _ greenTable: UnsafeMutablePointer<CGGammaValue>, _ blueTable: UnsafeMutablePointer<CGGammaValue>, _ sampleCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.0 |

Modified CGGetDisplaysWithOpenGLDisplayMask(CGOpenGLDisplayMask, UInt32, UnsafeMutablePointer<CGDirectDisplayID>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetDisplaysWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ maxDisplays: UInt32, _ displays: UnsafePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetDisplaysWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ maxDisplays: UInt32, _ displays: UnsafeMutablePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.0 |

Modified CGGetDisplaysWithPoint(CGPoint, UInt32, UnsafeMutablePointer<CGDirectDisplayID>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetDisplaysWithPoint(_ point: CGPoint, _ maxDisplays: UInt32, _ displays: UnsafePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetDisplaysWithPoint(_ point: CGPoint, _ maxDisplays: UInt32, _ displays: UnsafeMutablePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.0 |

Modified CGGetDisplaysWithRect(CGRect, UInt32, UnsafeMutablePointer<CGDirectDisplayID>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetDisplaysWithRect(_ rect: CGRect, _ maxDisplays: UInt32, _ displays: UnsafePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetDisplaysWithRect(_ rect: CGRect, _ maxDisplays: UInt32, _ displays: UnsafeMutablePointer<CGDirectDisplayID>, _ matchingDisplayCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.0 |

Modified CGGetEventTapList(UInt32, UnsafeMutablePointer<CGEventTapInformation>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetEventTapList(_ maxNumberOfTaps: UInt32, _ tapList: UnsafePointer<CGEventTapInformation>, _ eventTapCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetEventTapList(_ maxNumberOfTaps: UInt32, _ tapList: UnsafeMutablePointer<CGEventTapInformation>, _ eventTapCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.4 |

Modified CGGetLastMouseDelta(UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetLastMouseDelta(_ deltaX: UnsafePointer<Int32>, _ deltaY: UnsafePointer<Int32>) ``` | OS X 10.10 |
| To | ``` func CGGetLastMouseDelta(_ deltaX: UnsafeMutablePointer<Int32>, _ deltaY: UnsafeMutablePointer<Int32>) ``` | OS X 10.0 |

Modified CGGetOnlineDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>, UnsafeMutablePointer<UInt32>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGetOnlineDisplayList(_ maxDisplays: UInt32, _ onlineDisplays: UnsafePointer<CGDirectDisplayID>, _ displayCount: UnsafePointer<UInt32>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGGetOnlineDisplayList(_ maxDisplays: UInt32, _ onlineDisplays: UnsafeMutablePointer<CGDirectDisplayID>, _ displayCount: UnsafeMutablePointer<UInt32>) -> CGError ``` | OS X 10.2 |

Modified CGGradientCreateWithColorComponents(CGColorSpace!, UnsafePointer<CGFloat>, UnsafePointer<CGFloat>, Int) -> CGGradient!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace!, _ components: ConstUnsafePointer<CGFloat>, _ locations: ConstUnsafePointer<CGFloat>, _ count: UInt) -> CGGradient! ``` | OS X 10.10 |
| To | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace!, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: Int) -> CGGradient! ``` | OS X 10.5 |

Modified CGGradientCreateWithColors(CGColorSpace!, CFArray!, UnsafePointer<CGFloat>) -> CGGradient!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGGradientCreateWithColors(_ space: CGColorSpace!, _ colors: CFArray!, _ locations: ConstUnsafePointer<CGFloat>) -> CGGradient! ``` | OS X 10.10 |
| To | ``` func CGGradientCreateWithColors(_ space: CGColorSpace!, _ colors: CFArray!, _ locations: UnsafePointer<CGFloat>) -> CGGradient! ``` | OS X 10.5 |

Modified CGGradientGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGImageCreate(Int, Int, Int, Int, Int, CGColorSpace!, CGBitmapInfo, CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageCreate(_ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bitsPerPixel: UInt, _ bytesPerRow: UInt, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider!, _ decode: ConstUnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.10 |
| To | ``` func CGImageCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ space: CGColorSpace!, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.0 |

Modified CGImageCreateCopy(CGImage!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageCreateCopyWithColorSpace(CGImage!, CGColorSpace!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGImageCreateWithImageInRect(CGImage!, CGRect) -> CGImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageCreateWithJPEGDataProvider(CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageCreateWithJPEGDataProvider(_ source: CGDataProvider!, _ decode: ConstUnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.10 |
| To | ``` func CGImageCreateWithJPEGDataProvider(_ source: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.1 |

Modified CGImageCreateWithMask(CGImage!, CGImage!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageCreateWithMaskingColors(CGImage!, UnsafePointer<CGFloat>) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageCreateWithMaskingColors(_ image: CGImage!, _ components: ConstUnsafePointer<CGFloat>) -> CGImage! ``` | OS X 10.10 |
| To | ``` func CGImageCreateWithMaskingColors(_ image: CGImage!, _ components: UnsafePointer<CGFloat>) -> CGImage! ``` | OS X 10.4 |

Modified CGImageCreateWithPNGDataProvider(CGDataProvider!, UnsafePointer<CGFloat>, Bool, CGColorRenderingIntent) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageCreateWithPNGDataProvider(_ source: CGDataProvider!, _ decode: ConstUnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.10 |
| To | ``` func CGImageCreateWithPNGDataProvider(_ source: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage! ``` | OS X 10.2 |

Modified CGImageGetAlphaInfo(CGImage!) -> CGImageAlphaInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageGetBitmapInfo(CGImage!) -> CGBitmapInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageGetBitsPerComponent(CGImage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetBitsPerComponent(_ image: CGImage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageGetBitsPerComponent(_ image: CGImage!) -> Int ``` | OS X 10.0 |

Modified CGImageGetBitsPerPixel(CGImage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetBitsPerPixel(_ image: CGImage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageGetBitsPerPixel(_ image: CGImage!) -> Int ``` | OS X 10.0 |

Modified CGImageGetBytesPerRow(CGImage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetBytesPerRow(_ image: CGImage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageGetBytesPerRow(_ image: CGImage!) -> Int ``` | OS X 10.0 |

Modified CGImageGetColorSpace(CGImage!) -> CGColorSpace!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageGetDataProvider(CGImage!) -> CGDataProvider!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageGetDecode(CGImage!) -> UnsafePointer<CGFloat>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetDecode(_ image: CGImage!) -> ConstUnsafePointer<CGFloat> ``` | OS X 10.10 |
| To | ``` func CGImageGetDecode(_ image: CGImage!) -> UnsafePointer<CGFloat> ``` | OS X 10.0 |

Modified CGImageGetHeight(CGImage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetHeight(_ image: CGImage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageGetHeight(_ image: CGImage!) -> Int ``` | OS X 10.0 |

Modified CGImageGetRenderingIntent(CGImage!) -> CGColorRenderingIntent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageGetShouldInterpolate(CGImage!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGImageGetWidth(CGImage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageGetWidth(_ image: CGImage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageGetWidth(_ image: CGImage!) -> Int ``` | OS X 10.0 |

Modified CGImageIsMask(CGImage!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGImageMaskCreate(Int, Int, Int, Int, Int, CGDataProvider!, UnsafePointer<CGFloat>, Bool) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMaskCreate(_ width: UInt, _ height: UInt, _ bitsPerComponent: UInt, _ bitsPerPixel: UInt, _ bytesPerRow: UInt, _ provider: CGDataProvider!, _ decode: ConstUnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage! ``` | OS X 10.10 |
| To | ``` func CGImageMaskCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ provider: CGDataProvider!, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage! ``` | OS X 10.0 |

Modified CGLayerCreateWithContext(CGContext!, CGSize, CFDictionary!) -> CGLayer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGLayerGetContext(CGLayer!) -> CGContext!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGLayerGetSize(CGLayer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGLayerGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGMainDisplayID() -> CGDirectDisplayID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGOpenGLDisplayMaskToDisplayID(CGOpenGLDisplayMask) -> CGDirectDisplayID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFArrayGetArray(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetArray(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetBoolean(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetCount(CGPDFArrayRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetCount(_ array: CGPDFArray!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetCount(_ array: CGPDFArrayRef) -> Int ``` | OS X 10.3 |

Modified CGPDFArrayGetDictionary(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetInteger(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetInteger(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<CGPDFInteger>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetName(CGPDFArrayRef, Int, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetName(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<ConstUnsafePointer<Int8>>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetNull(CGPDFArrayRef, Int) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetNull(_ array: CGPDFArray!, _ index: UInt) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetNull(_ array: CGPDFArrayRef, _ index: Int) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetNumber(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetNumber(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<CGPDFReal>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetObject(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetObject(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetStream(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetStream(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayGetString(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFArrayGetString(_ array: CGPDFArray!, _ index: UInt, _ value: UnsafePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFArrayRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFArrayRef = CGPDFArray ``` |
| To | ``` typealias CGPDFArrayRef = COpaquePointer ``` |

Modified CGPDFContentStreamCreateWithPage(CGPDFPage!) -> CGPDFContentStreamRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage!) -> CGPDFContentStream! ``` | OS X 10.10 |
| To | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage!) -> CGPDFContentStreamRef ``` | OS X 10.4 |

Modified CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStreamRef) -> CGPDFContentStreamRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStream!, _ streamResources: CGPDFDictionary!, _ parent: CGPDFContentStream!) -> CGPDFContentStream! ``` | OS X 10.10 |
| To | ``` func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStreamRef) -> CGPDFContentStreamRef ``` | OS X 10.4 |

Modified CGPDFContentStreamGetResource(CGPDFContentStreamRef, UnsafePointer<Int8>, UnsafePointer<Int8>) -> CGPDFObjectRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStream!, _ category: ConstUnsafePointer<Int8>, _ name: ConstUnsafePointer<Int8>) -> CGPDFObject! ``` | OS X 10.10 |
| To | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef ``` | OS X 10.4 |

Modified CGPDFContentStreamGetStreams(CGPDFContentStreamRef) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStream!) -> CFArray! ``` | OS X 10.10 |
| To | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray! ``` | OS X 10.4 |

Modified CGPDFContentStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFContentStreamRef = CGPDFContentStream ``` |
| To | ``` typealias CGPDFContentStreamRef = COpaquePointer ``` |

Modified CGPDFContextAddDestinationAtPoint(CGContext!, CFString!, CGPoint)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGPDFContextAddDocumentMetadata(CGContext!, CFData!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CGPDFContextBeginPage(CGContext!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGPDFContextClose(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGPDFContextCreate(CGDataConsumer!, UnsafePointer<CGRect>, CFDictionary!) -> CGContext!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContextCreate(_ consumer: CGDataConsumer!, _ mediaBox: ConstUnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` | OS X 10.10 |
| To | ``` func CGPDFContextCreate(_ consumer: CGDataConsumer!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` | OS X 10.0 |

Modified CGPDFContextCreateWithURL(CFURL!, UnsafePointer<CGRect>, CFDictionary!) -> CGContext!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFContextCreateWithURL(_ url: CFURL!, _ mediaBox: ConstUnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` | OS X 10.10 |
| To | ``` func CGPDFContextCreateWithURL(_ url: CFURL!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!) -> CGContext! ``` | OS X 10.0 |

Modified CGPDFContextEndPage(CGContext!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGPDFContextSetDestinationForRect(CGContext!, CFString!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGPDFContextSetURLForRect(CGContext!, CFURL!, CGRect)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGPDFDictionaryApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryApplierFunction = CFunctionPointer<((ConstUnsafePointer<Int8>, CGPDFObject!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPDFDictionaryApplierFunction = CFunctionPointer<((UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPDFDictionaryApplyFunction(CGPDFDictionaryRef, CGPDFDictionaryApplierFunction, UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionary!, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafeMutablePointer<Void>) ``` | OS X 10.3 |

Modified CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionary!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetCount(_ dict: CGPDFDictionaryRef) -> Int ``` | OS X 10.3 |

Modified CGPDFDictionaryGetDictionary(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetInteger(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<CGPDFInteger>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetName(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<ConstUnsafePointer<Int8>>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetNumber(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<CGPDFReal>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetObject(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetStream(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<Int8>, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionary!, _ key: ConstUnsafePointer<Int8>, _ value: UnsafePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | OS X 10.3 |

Modified CGPDFDictionaryRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryRef = CGPDFDictionary ``` |
| To | ``` typealias CGPDFDictionaryRef = COpaquePointer ``` |

Modified CGPDFDocumentAllowsCopying(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFDocumentAllowsPrinting(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFDocumentCreateWithProvider(CGDataProvider!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGPDFDocumentCreateWithURL(CFURL!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGPDFDocumentGetCatalog(CGPDFDocument!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument!) -> CGPDFDictionary! ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` | OS X 10.3 |

Modified CGPDFDocumentGetID(CGPDFDocument!) -> CGPDFArrayRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument!) -> CGPDFArray! ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument!) -> CGPDFArrayRef ``` | OS X 10.4 |

Modified CGPDFDocumentGetInfo(CGPDFDocument!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument!) -> CGPDFDictionary! ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument!) -> CGPDFDictionaryRef ``` | OS X 10.4 |

Modified CGPDFDocumentGetNumberOfPages(CGPDFDocument!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument!) -> Int ``` | OS X 10.0 |

Modified CGPDFDocumentGetPage(CGPDFDocument!, Int) -> CGPDFPage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument!, _ pageNumber: UInt) -> CGPDFPage! ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument!, _ pageNumber: Int) -> CGPDFPage! ``` | OS X 10.3 |

Modified CGPDFDocumentGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFDocumentGetVersion(CGPDFDocument!, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentGetVersion(_ document: CGPDFDocument!, _ majorVersion: UnsafePointer<Int32>, _ minorVersion: UnsafePointer<Int32>) ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentGetVersion(_ document: CGPDFDocument!, _ majorVersion: UnsafeMutablePointer<Int32>, _ minorVersion: UnsafeMutablePointer<Int32>) ``` | OS X 10.3 |

Modified CGPDFDocumentIsEncrypted(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFDocumentIsUnlocked(CGPDFDocument!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPDFDocumentUnlockWithPassword(CGPDFDocument!, UnsafePointer<Int8>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFDocumentUnlockWithPassword(_ document: CGPDFDocument!, _ password: ConstUnsafePointer<Int8>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFDocumentUnlockWithPassword(_ document: CGPDFDocument!, _ password: UnsafePointer<Int8>) -> Bool ``` | OS X 10.2 |

Modified CGPDFObjectGetType(CGPDFObjectRef) -> CGPDFObjectType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFObjectGetType(_ object: CGPDFObject!) -> CGPDFObjectType ``` | OS X 10.10 |
| To | ``` func CGPDFObjectGetType(_ object: CGPDFObjectRef) -> CGPDFObjectType ``` | OS X 10.3 |

Modified CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutablePointer<Void>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFObjectGetValue(_ object: CGPDFObject!, _ type: CGPDFObjectType, _ value: UnsafePointer<()>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutablePointer<Void>) -> Bool ``` | OS X 10.3 |

Modified CGPDFObjectRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFObjectRef = CGPDFObject ``` |
| To | ``` typealias CGPDFObjectRef = COpaquePointer ``` |

Modified CGPDFOperatorCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorCallback = CFunctionPointer<((CGPDFScanner!, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPDFOperatorCallback = CFunctionPointer<((CGPDFScannerRef, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTable! ``` | OS X 10.10 |
| To | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef ``` | OS X 10.4 |

Modified CGPDFOperatorTableRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorTableRef = CGPDFOperatorTable ``` |
| To | ``` typealias CGPDFOperatorTableRef = COpaquePointer ``` |

Modified CGPDFOperatorTableSetCallback(CGPDFOperatorTableRef, UnsafePointer<Int8>, CGPDFOperatorCallback)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTable!, _ name: ConstUnsafePointer<Int8>, _ callback: CGPDFOperatorCallback) ``` | OS X 10.10 |
| To | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback) ``` | OS X 10.4 |

Modified CGPDFPageGetBoxRect(CGPDFPage!, CGPDFBox) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPDFPageGetDictionary(CGPDFPage!) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage!) -> CGPDFDictionary! ``` | OS X 10.10 |
| To | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage!) -> CGPDFDictionaryRef ``` | OS X 10.3 |

Modified CGPDFPageGetDocument(CGPDFPage!) -> CGPDFDocument!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPDFPageGetDrawingTransform(CGPDFPage!, CGPDFBox, CGRect, Int32, Bool) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPDFPageGetPageNumber(CGPDFPage!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage!) -> Int ``` | OS X 10.3 |

Modified CGPDFPageGetRotationAngle(CGPDFPage!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPDFPageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPDFScannerCreate(CGPDFContentStreamRef, CGPDFOperatorTableRef, UnsafeMutablePointer<Void>) -> CGPDFScannerRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStream!, _ table: CGPDFOperatorTable!, _ info: UnsafePointer<()>) -> CGPDFScanner! ``` | OS X 10.10 |
| To | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef, _ info: UnsafeMutablePointer<Void>) -> CGPDFScannerRef ``` | OS X 10.4 |

Modified CGPDFScannerGetContentStream(CGPDFScannerRef) -> CGPDFContentStreamRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerGetContentStream(_ scanner: CGPDFScanner!) -> CGPDFContentStream! ``` | OS X 10.10 |
| To | ``` func CGPDFScannerGetContentStream(_ scanner: CGPDFScannerRef) -> CGPDFContentStreamRef ``` | OS X 10.4 |

Modified CGPDFScannerPopArray(CGPDFScannerRef, UnsafeMutablePointer<CGPDFArrayRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScanner!, _ value: UnsafePointer<Unmanaged<CGPDFArray>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopBoolean(CGPDFScannerRef, UnsafeMutablePointer<CGPDFBoolean>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScanner!, _ value: UnsafePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopDictionary(CGPDFScannerRef, UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScanner!, _ value: UnsafePointer<Unmanaged<CGPDFDictionary>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopInteger(CGPDFScannerRef, UnsafeMutablePointer<CGPDFInteger>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScanner!, _ value: UnsafePointer<CGPDFInteger>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopName(CGPDFScannerRef, UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopName(_ scanner: CGPDFScanner!, _ value: UnsafePointer<ConstUnsafePointer<Int8>>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopName(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopNumber(CGPDFScannerRef, UnsafeMutablePointer<CGPDFReal>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScanner!, _ value: UnsafePointer<CGPDFReal>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopObject(CGPDFScannerRef, UnsafeMutablePointer<CGPDFObjectRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScanner!, _ value: UnsafePointer<Unmanaged<CGPDFObject>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopStream(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStreamRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScanner!, _ value: UnsafePointer<Unmanaged<CGPDFStream>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerPopString(CGPDFScannerRef, UnsafeMutablePointer<CGPDFStringRef>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerPopString(_ scanner: CGPDFScanner!, _ value: UnsafePointer<Unmanaged<CGPDFString>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerPopString(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` | OS X 10.4 |

Modified CGPDFScannerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFScannerRef = CGPDFScanner ``` |
| To | ``` typealias CGPDFScannerRef = COpaquePointer ``` |

Modified CGPDFScannerScan(CGPDFScannerRef) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFScannerScan(_ scanner: CGPDFScanner!) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPDFScannerScan(_ scanner: CGPDFScannerRef) -> Bool ``` | OS X 10.4 |

Modified CGPDFStreamCopyData(CGPDFStreamRef, UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStreamCopyData(_ stream: CGPDFStream!, _ format: UnsafePointer<CGPDFDataFormat>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> Unmanaged<CFData>! ``` | OS X 10.3 |

Modified CGPDFStreamGetDictionary(CGPDFStreamRef) -> CGPDFDictionaryRef

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStream!) -> Unmanaged<CGPDFDictionary>! ``` | OS X 10.10 |
| To | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef ``` | OS X 10.3 |

Modified CGPDFStreamRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStreamRef = CGPDFStream ``` |
| To | ``` typealias CGPDFStreamRef = COpaquePointer ``` |

Modified CGPDFStringCopyDate(CGPDFStringRef) -> Unmanaged<CFDate>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringCopyDate(_ string: CGPDFString!) -> Unmanaged<CFDate>! ``` | OS X 10.10 |
| To | ``` func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> Unmanaged<CFDate>! ``` | OS X 10.4 |

Modified CGPDFStringCopyTextString(CGPDFStringRef) -> Unmanaged<CFString>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringCopyTextString(_ string: CGPDFString!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> Unmanaged<CFString>! ``` | OS X 10.3 |

Modified CGPDFStringGetBytePtr(CGPDFStringRef) -> UnsafePointer<UInt8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringGetBytePtr(_ string: CGPDFString!) -> ConstUnsafePointer<UInt8> ``` | OS X 10.10 |
| To | ``` func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8> ``` | OS X 10.3 |

Modified CGPDFStringGetLength(CGPDFStringRef) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPDFStringGetLength(_ string: CGPDFString!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGPDFStringGetLength(_ string: CGPDFStringRef) -> Int ``` | OS X 10.3 |

Modified CGPDFStringRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStringRef = CGPDFString ``` |
| To | ``` typealias CGPDFStringRef = COpaquePointer ``` |

Modified CGPSConverterAbort(CGPSConverter!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPSConverterBeginDocumentCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterBeginDocumentCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPSConverterBeginDocumentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPSConverterBeginPageCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterBeginPageCallback = CFunctionPointer<((UnsafePointer<()>, UInt, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CGPSConverterBeginPageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Int, CFDictionary!) -> Void)> ``` |

Modified CGPSConverterConvert(CGPSConverter!, CGDataProvider!, CGDataConsumer!, CFDictionary!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPSConverterCreate(UnsafeMutablePointer<Void>, UnsafePointer<CGPSConverterCallbacks>, CFDictionary!) -> CGPSConverter!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPSConverterCreate(_ info: UnsafePointer<()>, _ callbacks: ConstUnsafePointer<CGPSConverterCallbacks>, _ options: CFDictionary!) -> CGPSConverter! ``` | OS X 10.10 |
| To | ``` func CGPSConverterCreate(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGPSConverterCallbacks>, _ options: CFDictionary!) -> CGPSConverter! ``` | OS X 10.3 |

Modified CGPSConverterEndDocumentCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterEndDocumentCallback = CFunctionPointer<((UnsafePointer<()>, Bool) -> Void)> ``` |
| To | ``` typealias CGPSConverterEndDocumentCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Bool) -> Void)> ``` |

Modified CGPSConverterEndPageCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterEndPageCallback = CFunctionPointer<((UnsafePointer<()>, UInt, CFDictionary!) -> Void)> ``` |
| To | ``` typealias CGPSConverterEndPageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, Int, CFDictionary!) -> Void)> ``` |

Modified CGPSConverterGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPSConverterIsConverting(CGPSConverter!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGPSConverterMessageCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterMessageCallback = CFunctionPointer<((UnsafePointer<()>, CFString!) -> Void)> ``` |
| To | ``` typealias CGPSConverterMessageCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CFString!) -> Void)> ``` |

Modified CGPSConverterProgressCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterProgressCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPSConverterProgressCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPSConverterReleaseInfoCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPSConverterReleaseInfoCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPSConverterReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPathAddArc(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, Bool)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddArc(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Bool) ``` | OS X 10.10 |
| To | ``` func CGPathAddArc(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ endAngle: CGFloat, _ clockwise: Bool) ``` | OS X 10.2 |

Modified CGPathAddArcToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddArcToPoint(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddArcToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ radius: CGFloat) ``` | OS X 10.2 |

Modified CGPathAddCurveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddCurveToPoint(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddCurveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ cp1x: CGFloat, _ cp1y: CGFloat, _ cp2x: CGFloat, _ cp2y: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.2 |

Modified CGPathAddEllipseInRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddEllipseInRect(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` | OS X 10.10 |
| To | ``` func CGPathAddEllipseInRect(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` | OS X 10.4 |

Modified CGPathAddLineToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddLineToPoint(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddLineToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.2 |

Modified CGPathAddLines(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGPoint>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddLines(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ points: ConstUnsafePointer<CGPoint>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGPathAddLines(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ points: UnsafePointer<CGPoint>, _ count: Int) ``` | OS X 10.2 |

Modified CGPathAddPath(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGPath!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddPath(_ path1: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ path2: CGPath!) ``` | OS X 10.10 |
| To | ``` func CGPathAddPath(_ path1: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ path2: CGPath!) ``` | OS X 10.2 |

Modified CGPathAddQuadCurveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddQuadCurveToPoint(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddQuadCurveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ cpx: CGFloat, _ cpy: CGFloat, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.2 |

Modified CGPathAddRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddRect(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` | OS X 10.10 |
| To | ``` func CGPathAddRect(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rect: CGRect) ``` | OS X 10.2 |

Modified CGPathAddRects(CGMutablePath!, UnsafePointer<CGAffineTransform>, UnsafePointer<CGRect>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddRects(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ rects: ConstUnsafePointer<CGRect>, _ count: UInt) ``` | OS X 10.10 |
| To | ``` func CGPathAddRects(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ rects: UnsafePointer<CGRect>, _ count: Int) ``` | OS X 10.2 |

Modified CGPathAddRelativeArc(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddRelativeArc(_ path: CGMutablePath!, _ matrix: ConstUnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ delta: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddRelativeArc(_ path: CGMutablePath!, _ matrix: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat, _ radius: CGFloat, _ startAngle: CGFloat, _ delta: CGFloat) ``` | OS X 10.7 |

Modified CGPathAddRoundedRect(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGRect, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathAddRoundedRect(_ path: CGMutablePath!, _ transform: ConstUnsafePointer<CGAffineTransform>, _ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathAddRoundedRect(_ path: CGMutablePath!, _ transform: UnsafePointer<CGAffineTransform>, _ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat) ``` | OS X 10.9 |

Modified CGPathApplierFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPathApplierFunction = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<CGPathElement>) -> Void)> ``` |
| To | ``` typealias CGPathApplierFunction = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<CGPathElement>) -> Void)> ``` |

Modified CGPathApply(CGPath!, UnsafeMutablePointer<Void>, CGPathApplierFunction)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathApply(_ path: CGPath!, _ info: UnsafePointer<()>, _ function: CGPathApplierFunction) ``` | OS X 10.10 |
| To | ``` func CGPathApply(_ path: CGPath!, _ info: UnsafeMutablePointer<Void>, _ function: CGPathApplierFunction) ``` | OS X 10.2 |

Modified CGPathCloseSubpath(CGMutablePath!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathContainsPoint(CGPath!, UnsafePointer<CGAffineTransform>, CGPoint, Bool) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathContainsPoint(_ path: CGPath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ point: CGPoint, _ eoFill: Bool) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPathContainsPoint(_ path: CGPath!, _ m: UnsafePointer<CGAffineTransform>, _ point: CGPoint, _ eoFill: Bool) -> Bool ``` | OS X 10.4 |

Modified CGPathCreateCopy(CGPath!) -> CGPath!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathCreateCopyByDashingPath(CGPath!, UnsafePointer<CGAffineTransform>, CGFloat, UnsafePointer<CGFloat>, Int) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath!, _ transform: ConstUnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: ConstUnsafePointer<CGFloat>, _ count: UInt) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) -> CGPath! ``` | OS X 10.7 |

Modified CGPathCreateCopyByStrokingPath(CGPath!, UnsafePointer<CGAffineTransform>, CGFloat, CGLineCap, CGLineJoin, CGFloat) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateCopyByStrokingPath(_ path: CGPath!, _ transform: ConstUnsafePointer<CGAffineTransform>, _ lineWidth: CGFloat, _ lineCap: CGLineCap, _ lineJoin: CGLineJoin, _ miterLimit: CGFloat) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateCopyByStrokingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>, _ lineWidth: CGFloat, _ lineCap: CGLineCap, _ lineJoin: CGLineJoin, _ miterLimit: CGFloat) -> CGPath! ``` | OS X 10.7 |

Modified CGPathCreateCopyByTransformingPath(CGPath!, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateCopyByTransformingPath(_ path: CGPath!, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateCopyByTransformingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.7 |

Modified CGPathCreateMutable() -> CGMutablePath!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathCreateMutableCopy(CGPath!) -> CGMutablePath!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathCreateMutableCopyByTransformingPath(CGPath!, UnsafePointer<CGAffineTransform>) -> CGMutablePath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateMutableCopyByTransformingPath(_ path: CGPath!, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGMutablePath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateMutableCopyByTransformingPath(_ path: CGPath!, _ transform: UnsafePointer<CGAffineTransform>) -> CGMutablePath! ``` | OS X 10.7 |

Modified CGPathCreateWithEllipseInRect(CGRect, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateWithEllipseInRect(_ rect: CGRect, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateWithEllipseInRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.7 |

Modified CGPathCreateWithRect(CGRect, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateWithRect(_ rect: CGRect, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateWithRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.5 |

Modified CGPathCreateWithRoundedRect(CGRect, CGFloat, CGFloat, UnsafePointer<CGAffineTransform>) -> CGPath!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathCreateWithRoundedRect(_ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat, _ transform: ConstUnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.10 |
| To | ``` func CGPathCreateWithRoundedRect(_ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath! ``` | OS X 10.9 |

Modified CGPathEqualToPath(CGPath!, CGPath!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathGetBoundingBox(CGPath!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathGetCurrentPoint(CGPath!) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathGetPathBoundingBox(CGPath!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CGPathGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathIsEmpty(CGPath!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPathIsRect(CGPath!, UnsafeMutablePointer<CGRect>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathIsRect(_ path: CGPath!, _ rect: UnsafePointer<CGRect>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPathIsRect(_ path: CGPath!, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` | OS X 10.2 |

Modified CGPathMoveToPoint(CGMutablePath!, UnsafePointer<CGAffineTransform>, CGFloat, CGFloat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPathMoveToPoint(_ path: CGMutablePath!, _ m: ConstUnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.10 |
| To | ``` func CGPathMoveToPoint(_ path: CGMutablePath!, _ m: UnsafePointer<CGAffineTransform>, _ x: CGFloat, _ y: CGFloat) ``` | OS X 10.2 |

Modified CGPatternCreate(UnsafeMutablePointer<Void>, CGRect, CGAffineTransform, CGFloat, CGFloat, CGPatternTiling, Bool, UnsafePointer<CGPatternCallbacks>) -> CGPattern!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPatternCreate(_ info: UnsafePointer<()>, _ bounds: CGRect, _ matrix: CGAffineTransform, _ xStep: CGFloat, _ yStep: CGFloat, _ tiling: CGPatternTiling, _ isColored: Bool, _ callbacks: ConstUnsafePointer<CGPatternCallbacks>) -> CGPattern! ``` | OS X 10.10 |
| To | ``` func CGPatternCreate(_ info: UnsafeMutablePointer<Void>, _ bounds: CGRect, _ matrix: CGAffineTransform, _ xStep: CGFloat, _ yStep: CGFloat, _ tiling: CGPatternTiling, _ isColored: Bool, _ callbacks: UnsafePointer<CGPatternCallbacks>) -> CGPattern! ``` | OS X 10.0 |

Modified CGPatternDrawPatternCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternDrawPatternCallback = CFunctionPointer<((UnsafePointer<()>, CGContext!) -> Void)> ``` |
| To | ``` typealias CGPatternDrawPatternCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CGContext!) -> Void)> ``` |

Modified CGPatternGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGPatternReleaseInfoCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternReleaseInfoCallback = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGPatternReleaseInfoCallback = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGPointApplyAffineTransform(CGPoint, CGAffineTransform) -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGPointCreateDictionaryRepresentation(CGPoint) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGPointEqualToPoint(CGPoint, CGPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGPointMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGPoint>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ point: UnsafePointer<CGPoint>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGPointMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ point: UnsafeMutablePointer<CGPoint>) -> Bool ``` | OS X 10.5 |

Modified CGPointZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectApplyAffineTransform(CGRect, CGAffineTransform) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGRectContainsPoint(CGRect, CGPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectContainsRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectCreateDictionaryRepresentation() -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGRectDivide(CGRect, UnsafeMutablePointer<CGRect>, UnsafeMutablePointer<CGRect>, CGFloat, CGRectEdge)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGRectDivide(_ rect: CGRect, _ slice: UnsafePointer<CGRect>, _ remainder: UnsafePointer<CGRect>, _ amount: CGFloat, _ edge: CGRectEdge) ``` | OS X 10.10 |
| To | ``` func CGRectDivide(_ rect: CGRect, _ slice: UnsafeMutablePointer<CGRect>, _ remainder: UnsafeMutablePointer<CGRect>, _ amount: CGFloat, _ edge: CGRectEdge) ``` | OS X 10.0 |

Modified CGRectEqualToRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetHeight(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMaxX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMaxY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMidX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMidY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMinX(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetMinY(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectGetWidth(CGRect) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectInfinite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectIntegral(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectIntersection(CGRect, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectIntersectsRect(CGRect, CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectIsEmpty(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectIsInfinite(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGRectIsNull(CGRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGRect>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ rect: UnsafePointer<CGRect>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGRectMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` | OS X 10.5 |

Modified CGRectNull

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectStandardize(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectUnion(CGRect, CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGRectZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGReleaseAllDisplays() -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGReleaseDisplayFadeReservation(CGDisplayFadeReservationToken) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGRestorePermanentDisplayConfiguration()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGScreenRefreshCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGScreenRefreshCallback = CFunctionPointer<((UInt32, ConstUnsafePointer<CGRect>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGScreenRefreshCallback = CFunctionPointer<((UInt32, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGScreenUpdateMoveCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CGScreenUpdateMoveCallback = CFunctionPointer<((CGScreenUpdateMoveDelta, UInt, ConstUnsafePointer<CGRect>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CGScreenUpdateMoveCallback = CFunctionPointer<((CGScreenUpdateMoveDelta, Int, UnsafePointer<CGRect>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CGSessionCopyCurrentDictionary() -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CGSetDisplayTransferByByteTable(CGDirectDisplayID, UInt32, UnsafePointer<UInt8>, UnsafePointer<UInt8>, UnsafePointer<UInt8>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGSetDisplayTransferByByteTable(_ display: CGDirectDisplayID, _ tableSize: UInt32, _ redTable: ConstUnsafePointer<UInt8>, _ greenTable: ConstUnsafePointer<UInt8>, _ blueTable: ConstUnsafePointer<UInt8>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGSetDisplayTransferByByteTable(_ display: CGDirectDisplayID, _ tableSize: UInt32, _ redTable: UnsafePointer<UInt8>, _ greenTable: UnsafePointer<UInt8>, _ blueTable: UnsafePointer<UInt8>) -> CGError ``` | OS X 10.0 |

Modified CGSetDisplayTransferByFormula(CGDirectDisplayID, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGSetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafePointer<CGGammaValue>, UnsafePointer<CGGammaValue>, UnsafePointer<CGGammaValue>) -> CGError

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGSetDisplayTransferByTable(_ display: CGDirectDisplayID, _ tableSize: UInt32, _ redTable: ConstUnsafePointer<CGGammaValue>, _ greenTable: ConstUnsafePointer<CGGammaValue>, _ blueTable: ConstUnsafePointer<CGGammaValue>) -> CGError ``` | OS X 10.10 |
| To | ``` func CGSetDisplayTransferByTable(_ display: CGDirectDisplayID, _ tableSize: UInt32, _ redTable: UnsafePointer<CGGammaValue>, _ greenTable: UnsafePointer<CGGammaValue>, _ blueTable: UnsafePointer<CGGammaValue>) -> CGError ``` | OS X 10.0 |

Modified CGShadingCreateAxial(CGColorSpace!, CGPoint, CGPoint, CGFunction!, Bool, Bool) -> CGShading!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGShadingCreateRadial(CGColorSpace!, CGPoint, CGFloat, CGPoint, CGFloat, CGFunction!, Bool, Bool) -> CGShading!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGShadingGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CGShieldingWindowID(CGDirectDisplayID) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGShieldingWindowLevel() -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGSizeApplyAffineTransform(CGSize, CGAffineTransform) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGSizeCreateDictionaryRepresentation(CGSize) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGSizeEqualToSize(CGSize, CGSize) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGSizeMakeWithDictionaryRepresentation(CFDictionary!, UnsafeMutablePointer<CGSize>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ size: UnsafePointer<CGSize>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGSizeMakeWithDictionaryRepresentation(_ dict: CFDictionary!, _ size: UnsafeMutablePointer<CGSize>) -> Bool ``` | OS X 10.5 |

Modified CGSizeZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGWarpMouseCursorPosition(CGPoint) -> CGError

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGWindowLevelForKey(CGWindowLevelKey) -> CGWindowLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified CGWindowListCopyWindowInfo(CGWindowListOption, CGWindowID) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGWindowListCreate(CGWindowListOption, CGWindowID) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGWindowListCreateDescriptionFromArray(CFArray!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGWindowListCreateImage(CGRect, CGWindowListOption, CGWindowID, CGWindowImageOption) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGWindowListCreateImageFromArray(CGRect, CFArray!, CGWindowImageOption) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CGWindowServerCreateServerPort() -> Unmanaged<CFMachPort>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGColorBlack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGColorClear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGColorSpaceAdobeRGB1998

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGColorSpaceGenericCMYK

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGColorSpaceGenericGray

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGColorSpaceGenericGrayGamma2_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGColorSpaceGenericRGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGColorSpaceGenericRGBLinear

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGColorSpaceSRGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGColorWhite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGDisplayShowDuplicateLowResolutionModes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamColorSpace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamDestinationRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamMinimumFrameTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamPreserveAspectRatio

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamQueueDepth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamShowCursor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamSourceRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamYCbCrMatrix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamYCbCrMatrix_ITU_R_601_4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamYCbCrMatrix_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGFontVariationAxisDefaultValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGFontVariationAxisMaxValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGFontVariationAxisMinValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGFontVariationAxisName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextAllowsCopying

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextAllowsPrinting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextArtBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextAuthor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextBleedBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextCreator

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextCropBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextEncryptionKeyLength

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGPDFContextKeywords

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGPDFContextMediaBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextOutputIntent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextOutputIntents

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextOwnerPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextSubject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGPDFContextTitle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextTrimBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFContextUserPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXDestinationOutputProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXOutputCondition

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXOutputConditionIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXOutputIntentSubtype

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGPDFXRegistryName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGWindowAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowBackingLocationVideoMemory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowBounds

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowIsOnscreen

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowLayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowMemoryUsage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowOwnerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowOwnerPID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowSharingState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGWindowStoreType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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
