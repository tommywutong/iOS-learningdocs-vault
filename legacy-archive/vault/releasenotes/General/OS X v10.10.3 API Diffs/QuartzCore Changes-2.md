---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/QuartzCore.html
archived_at: '2026-07-18T02:52:37.584500Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

Removed CAAutoresizingMask.valueRemoved CAEdgeAntialiasingMask.valueRemoved CIBarcodeFeatureRemoved CIBarcodeFeature.bottomLeftRemoved CIBarcodeFeature.bottomRightRemoved CIBarcodeFeature.boundsRemoved CIBarcodeFeature.codeRawDataRemoved CIBarcodeFeature.codeStringRemoved CIBarcodeFeature.codeTypeRemoved CIBarcodeFeature.errorCorrectionLevelRemoved CIBarcodeFeature.topLeftRemoved CIBarcodeFeature.topRightRemoved CIContext.init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, options:[NSObject: AnyObject]!)Removed CIContext.offlineGPUAtIndex(UInt32) -> CIContext! [class]Removed CIContext.offlineGPUAtIndex(UInt32, colorSpace: CGColorSpace!, options:[NSObject: AnyObject]!, sharedContext: CGLContextObj) -> CIContext! [class]Added CAAutoresizingMask.init(rawValue: UInt32)Added CAEdgeAntialiasingMask.init(rawValue: UInt32)Added CATransform3D.init()Added CATransform3D.init(m11: CGFloat, m12: CGFloat, m13: CGFloat, m14: CGFloat, m21: CGFloat, m22: CGFloat, m23: CGFloat, m24: CGFloat, m31: CGFloat, m32: CGFloat, m33: CGFloat, m34: CGFloat, m41: CGFloat, m42: CGFloat, m43: CGFloat, m44: CGFloat)Added CIContext.init(forOfflineGPUAtIndex: UInt32)Added CIContext.init(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace!, options:[NSObject: AnyObject]!, sharedContext: CGLContextObj)Added CIQRCodeFeatureAdded CIQRCodeFeature.bottomLeftAdded CIQRCodeFeature.bottomRightAdded CIQRCodeFeature.boundsAdded CIQRCodeFeature.messageStringAdded CIQRCodeFeature.topLeftAdded CIQRCodeFeature.topRightAdded NSObject.actionForLayer(CALayer!, forKey: String!) -> CAAction!Added NSObject.animationDidStart(CAAnimation!)Added NSObject.animationDidStop(CAAnimation!, finished: Bool)Added NSObject.displayLayer(CALayer!)Added NSObject.drawLayer(CALayer!, inContext: CGContext!)Added NSObject.invalidateLayoutOfLayer(CALayer!)Added NSObject.layoutSublayersOfLayer(CALayer!)Added NSObject.preferredSizeOfLayer(CALayer!) -> CGSizeAdded NSObject.provideImageData(UnsafeMutablePointer<Void>, bytesPerRow: Int, origin: Int, _: Int, size: Int, _: Int, userInfo: AnyObject!)Added NSValue.init(CATransform3D: CATransform3D)Added NSValue.CATransform3DValueModified CAAutoresizingMask [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAAutoresizingMask : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var LayerNotSizable: CAAutoresizingMask { get }     static var LayerMinXMargin: CAAutoresizingMask { get }     static var LayerWidthSizable: CAAutoresizingMask { get }     static var LayerMaxXMargin: CAAutoresizingMask { get }     static var LayerMinYMargin: CAAutoresizingMask { get }     static var LayerHeightSizable: CAAutoresizingMask { get }     static var LayerMaxYMargin: CAAutoresizingMask { get } } ``` | RawOptionSet |
| To | ``` struct CAAutoresizingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerNotSizable: CAAutoresizingMask { get }     static var LayerMinXMargin: CAAutoresizingMask { get }     static var LayerWidthSizable: CAAutoresizingMask { get }     static var LayerMaxXMargin: CAAutoresizingMask { get }     static var LayerMinYMargin: CAAutoresizingMask { get }     static var LayerHeightSizable: CAAutoresizingMask { get }     static var LayerMaxYMargin: CAAutoresizingMask { get } } ``` | RawOptionSetType |

Modified CAAutoresizingMask.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CAConstraint.init(attribute: CAConstraintAttribute, relativeTo: String!, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(attribute attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) ``` |
| To | ``` init!(attribute attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) ``` |

Modified CAEdgeAntialiasingMask [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAEdgeAntialiasingMask : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | RawOptionSet |
| To | ``` struct CAEdgeAntialiasingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | RawOptionSetType |

Modified CAEdgeAntialiasingMask.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CAEmitterBehavior.init(type: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: String!) ``` |
| To | ``` init!(type type: String!) ``` |

Modified CALayer.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CALayer.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` weak var delegate: AnyObject! ``` |

Modified CALayer.init(layer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(layer layer: AnyObject!) ``` |
| To | ``` init!(layer layer: AnyObject!) ``` |

Modified CALayer.init(remoteClientId: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(remoteClientId client_id: UInt32) -> CALayer ``` |
| To | ``` init!(remoteClientId client_id: UInt32) -> CALayer ``` |

Modified CAMediaTimingFunction.init(controlPoints: Float, _: Float, _: Float, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |
| To | ``` init!(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |

Modified CAMediaTimingFunction.getControlPointAtIndex(Int, values: UnsafeMutablePointer<Float>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getControlPointAtIndex(_ idx: UInt, values ptr: UnsafePointer<Float>) ``` | OS X 10.10 |
| To | ``` func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) ``` | OS X 10.10.3 |

Modified CAMediaTimingFunction.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init!(name name: String!) ``` |

Modified CAOpenGLLayer.canDrawInCGLContext(CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func canDrawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: ConstUnsafePointer<CVTimeStamp>) -> Bool ``` |
| To | ``` func canDrawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) -> Bool ``` |

Modified CAOpenGLLayer.drawInCGLContext(CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>)

|  | Declaration |
| --- | --- |
| From | ``` func drawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: ConstUnsafePointer<CVTimeStamp>) ``` |
| To | ``` func drawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) ``` |

Modified CAPropertyAnimation.init(keyPath: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(keyPath path: String!) ``` |
| To | ``` convenience init!(keyPath path: String!) ``` |

Modified CARemoteLayerClient.init(serverPort: mach_port_t)

|  | Declaration |
| --- | --- |
| From | ``` init(serverPort port: mach_port_t) ``` |
| To | ``` init!(serverPort port: mach_port_t) ``` |

Modified CARenderer.init(CGLContext: UnsafeMutablePointer<Void>, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGLContext ctx: UnsafePointer<()>, options dict: [NSObject : AnyObject]!) -> CARenderer ``` |
| To | ``` init!(CGLContext ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]!) -> CARenderer ``` |

Modified CARenderer.beginFrameAtTime(CFTimeInterval, timeStamp: UnsafeMutablePointer<CVTimeStamp>)

|  | Declaration |
| --- | --- |
| From | ``` func beginFrameAtTime(_ t: CFTimeInterval, timeStamp ts: UnsafePointer<CVTimeStamp>) ``` |
| To | ``` func beginFrameAtTime(_ t: CFTimeInterval, timeStamp ts: UnsafeMutablePointer<CVTimeStamp>) ``` |

Modified CATextLayer.string

|  | Declaration |
| --- | --- |
| From | ``` var string: AnyObject! ``` |
| To | ``` @NSCopying var string: AnyObject! ``` |

Modified CATiledLayer.levelsOfDetail

|  | Declaration |
| --- | --- |
| From | ``` var levelsOfDetail: UInt ``` |
| To | ``` var levelsOfDetail: Int ``` |

Modified CATiledLayer.levelsOfDetailBias

|  | Declaration |
| --- | --- |
| From | ``` var levelsOfDetailBias: UInt ``` |
| To | ``` var levelsOfDetailBias: Int ``` |

Modified CATransform3D [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat } ``` |
| To | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat     init()     init(m11 m11: CGFloat, m12 m12: CGFloat, m13 m13: CGFloat, m14 m14: CGFloat, m21 m21: CGFloat, m22 m22: CGFloat, m23 m23: CGFloat, m24 m24: CGFloat, m31 m31: CGFloat, m32 m32: CGFloat, m33 m33: CGFloat, m34 m34: CGFloat, m41 m41: CGFloat, m42 m42: CGFloat, m43 m43: CGFloat, m44 m44: CGFloat) } ``` |

Modified CAValueFunction.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init!(name name: String!) ``` |

Modified CIColor.init(CGColor: CGColor!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGColor c: CGColor!) ``` |
| To | ``` init!(CGColor c: CGColor!) ``` |

Modified CIColor.components() -> UnsafePointer<CGFloat>

|  | Declaration |
| --- | --- |
| From | ``` func components() -> ConstUnsafePointer<CGFloat> ``` |
| To | ``` func components() -> UnsafePointer<CGFloat> ``` |

Modified CIColor.numberOfComponents() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func numberOfComponents() -> UInt ``` | OS X 10.10 |
| To | ``` func numberOfComponents() -> Int ``` | OS X 10.10.3 |

Modified CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor ``` |
| To | ``` init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor ``` |

Modified CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor ``` |
| To | ``` init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor ``` |

Modified CIColor.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string representation: String!) -> CIColor ``` |
| To | ``` init!(string representation: String!) -> CIColor ``` |

Modified CIContext.init(CGContext: CGContext!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` |
| To | ``` init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` |

Modified CIContext.init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, colorSpace: CGColorSpace!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | OS X 10.10 |
| To | ``` init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | OS X 10.6 |

Modified CIContext.render(CIImage!, toBitmap: UnsafeMutablePointer<Void>, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace!)

|  | Declaration |
| --- | --- |
| From | ``` func render(_ im: CIImage!, toBitmap data: UnsafePointer<()>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) ``` |
| To | ``` func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) ``` |

Modified CIContext.render(CIImage!, toIOSurface: IOSurface!, bounds: CGRect, colorSpace: CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CIDetector.featuresInImage(CIImage!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CIDetector.featuresInImage(CIImage!, options:[NSObject: AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CIDetector.init(ofType: String!, context: CIContext!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` | OS X 10.10 |
| To | ``` init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` | OS X 10.7 |

Modified CIFilter.filterArrayFromSerializedXMP(NSData!, inputImageExtent: CGRect, error: NSErrorPointer) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CIFilter.init(imageData: NSData!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter ``` |
| To | ``` init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter ``` |

Modified CIFilter.init(imageURL: NSURL!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter ``` |
| To | ``` init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter ``` |

Modified CIFilter.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!) -> CIFilter ``` |
| To | ``` init!(name name: String!) -> CIFilter ``` |

Modified CIFilter.init(name: String!, withInputParameters:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter ``` |
| To | ``` init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter ``` |

Modified CIFilter.serializedXMPFromFilters([AnyObject]!, inputImageExtent: CGRect) -> NSData! [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CIFilterGenerator.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL aURL: NSURL!) ``` |
| To | ``` init!(contentsOfURL aURL: NSURL!) ``` |

Modified CIFilterShape.init(rect: CGRect)

|  | Declaration |
| --- | --- |
| From | ``` init(rect r: CGRect) ``` |
| To | ``` init!(rect r: CGRect) ``` |

Modified CIImage.init(CGImage: CGImage!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGImage image: CGImage!) ``` |
| To | ``` init!(CGImage image: CGImage!) ``` |

Modified CIImage.init(CGImage: CGImage!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) ``` |

Modified CIImage.init(CGLayer: CGLayer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGLayer layer: CGLayer!) ``` | OS X 10.10 |
| To | ``` init!(CGLayer layer: CGLayer!) ``` | OS X 10.4 |

Modified CIImage.init(CGLayer: CGLayer!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) ``` | OS X 10.4 |

Modified CIImage.init(CVImageBuffer: CVImageBuffer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CVImageBuffer imageBuffer: CVImageBuffer!) ``` | OS X 10.10 |
| To | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!) ``` | OS X 10.4 |

Modified CIImage.init(CVImageBuffer: CVImageBuffer!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.4 |

Modified CIImage.init(IOSurface: IOSurface!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(IOSurface surface: IOSurface!) ``` | OS X 10.10 |
| To | ``` init!(IOSurface surface: IOSurface!) ``` | OS X 10.6 |

Modified CIImage.init(IOSurface: IOSurface!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) ``` | OS X 10.6 |

Modified CIImage.init(IOSurface: IOSurface!, plane: Int, format: CIFormat, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(IOSurface surface: IOSurface!, plane plane: UInt, format format: CIFormat, options d: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(IOSurface surface: IOSurface!, plane plane: Int, format format: CIFormat, options d: [NSObject : AnyObject]!) ``` | OS X 10.10.3 |

Modified CIImage.autoAdjustmentFilters() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CIImage.autoAdjustmentFiltersWithOptions([NSObject: AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CIImage.init(bitmapData: NSData!, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bitmapData d: NSData!, bytesPerRow bpr: UInt, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | OS X 10.10 |
| To | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | OS X 10.10.3 |

Modified CIImage.init(color: CIColor!)

|  | Declaration |
| --- | --- |
| From | ``` init(color color: CIColor!) ``` |
| To | ``` init!(color color: CIColor!) ``` |

Modified CIImage.colorSpace() -> Unmanaged<CGColorSpace>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CIImage.init(contentsOfURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!) ``` |
| To | ``` init!(contentsOfURL url: NSURL!) ``` |

Modified CIImage.init(contentsOfURL: NSURL!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) ``` |

Modified CIImage.init(data: NSData!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!) ``` |
| To | ``` init!(data data: NSData!) ``` |

Modified CIImage.init(data: NSData!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: NSData!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init!(data data: NSData!, options d: [NSObject : AnyObject]!) ``` |

Modified CIImage.definition() -> CIFilterShape!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CIImage.imageByCompositingOverImage(CIImage!) -> CIImage!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CIImage.init(imageProvider: AnyObject!, size: Int, _: Int, format: CIFormat, colorSpace: CGColorSpace!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(imageProvider p: AnyObject!, size width: UInt, _ height: UInt, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.10.3 |

Modified CIImage.properties() -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | OS X 10.10 |
| To | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | OS X 10.4 |

Modified CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) ``` | OS X 10.9 |

Modified CIImage.url() -> NSURL!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CIImageAccumulator.init(extent: CGRect, format: CIFormat)

|  | Declaration |
| --- | --- |
| From | ``` init(extent extent: CGRect, format format: CIFormat) ``` |
| To | ``` init!(extent extent: CGRect, format format: CIFormat) ``` |

Modified CIImageAccumulator.init(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) ``` | OS X 10.10 |
| To | ``` init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) ``` | OS X 10.7 |

Modified CIKernel.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string s: String!) -> CIKernel ``` |
| To | ``` init!(string s: String!) -> CIKernel ``` |

Modified CIPlugIn.loadPlugIn(NSURL!, allowExecutableCode: Bool) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CIPlugInRegistration.load(UnsafeMutablePointer<Void>) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func load(_ host: UnsafePointer<()>) -> Bool ``` |
| To | ``` func load(_ host: UnsafeMutablePointer<Void>) -> Bool ``` |

Modified CISampler.init(image: CIImage!)

|  | Declaration |
| --- | --- |
| From | ``` init(image im: CIImage!) ``` |
| To | ``` init!(image im: CIImage!) ``` |

Modified CISampler.init(image: CIImage!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(image im: CIImage!, options dict: [NSObject : AnyObject]!) ``` |
| To | ``` init!(image im: CIImage!, options dict: [NSObject : AnyObject]!) ``` |

Modified CIVector.init(CGAffineTransform: CGAffineTransform)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGAffineTransform r: CGAffineTransform) ``` | OS X 10.10 |
| To | ``` init!(CGAffineTransform r: CGAffineTransform) ``` | OS X 10.9 |

Modified CIVector.CGAffineTransformValue() -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CIVector.init(CGPoint: CGPoint)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGPoint p: CGPoint) ``` | OS X 10.10 |
| To | ``` init!(CGPoint p: CGPoint) ``` | OS X 10.9 |

Modified CIVector.CGPointValue() -> CGPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CIVector.init(CGRect: CGRect)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGRect r: CGRect) ``` | OS X 10.10 |
| To | ``` init!(CGRect r: CGRect) ``` | OS X 10.9 |

Modified CIVector.CGRectValue() -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified CIVector.count() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func count() -> UInt ``` | OS X 10.10 |
| To | ``` func count() -> Int ``` | OS X 10.10.3 |

Modified CIVector.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string representation: String!) ``` |
| To | ``` init!(string representation: String!) ``` |

Modified CIVector.valueAtIndex(Int) -> CGFloat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func valueAtIndex(_ index: UInt) -> CGFloat ``` | OS X 10.10 |
| To | ``` func valueAtIndex(_ index: Int) -> CGFloat ``` | OS X 10.10.3 |

Modified CIVector.init(values: UnsafePointer<CGFloat>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(values values: ConstUnsafePointer<CGFloat>, count count: UInt) ``` | OS X 10.10 |
| To | ``` init!(values values: UnsafePointer<CGFloat>, count count: Int) ``` | OS X 10.10.3 |

Modified CIVector.init(x: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(x x: CGFloat) ``` |
| To | ``` init!(x x: CGFloat) ``` |

Modified CIVector.init(x: CGFloat, y: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(x x: CGFloat, y y: CGFloat) ``` |
| To | ``` init!(x x: CGFloat, y y: CGFloat) ``` |

Modified CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` |
| To | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` |

Modified CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` |
| To | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` |

Modified CACurrentMediaTime() -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DConcat(CATransform3D, CATransform3D) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DEqualToTransform(CATransform3D, CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DGetAffineTransform(CATransform3D) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DIdentity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DInvert(CATransform3D) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DIsAffine(CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DIsIdentity(CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DMakeAffineTransform(CGAffineTransform) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DRotate(CATransform3D, CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DScale(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CATransform3DTranslate(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CIDetectorAccuracy

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorAccuracy: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorAccuracy: String ``` | OS X 10.7 |

Modified CIDetectorAccuracyHigh

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorAccuracyHigh: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorAccuracyHigh: String ``` | OS X 10.7 |

Modified CIDetectorAccuracyLow

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorAccuracyLow: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorAccuracyLow: String ``` | OS X 10.7 |

Modified CIDetectorAspectRatio

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorAspectRatio: NSString! ``` |
| To | ``` let CIDetectorAspectRatio: String ``` |

Modified CIDetectorEyeBlink

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorEyeBlink: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorEyeBlink: String ``` | OS X 10.9 |

Modified CIDetectorFocalLength

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorFocalLength: NSString! ``` |
| To | ``` let CIDetectorFocalLength: String ``` |

Modified CIDetectorImageOrientation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorImageOrientation: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorImageOrientation: String ``` | OS X 10.8 |

Modified CIDetectorMinFeatureSize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorMinFeatureSize: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorMinFeatureSize: String ``` | OS X 10.8 |

Modified CIDetectorSmile

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorSmile: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorSmile: String ``` | OS X 10.9 |

Modified CIDetectorTracking

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorTracking: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorTracking: String ``` | OS X 10.8 |

Modified CIDetectorTypeFace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorTypeFace: NSString! ``` | OS X 10.10 |
| To | ``` let CIDetectorTypeFace: String ``` | OS X 10.7 |

Modified CIDetectorTypeQRCode

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorTypeQRCode: NSString! ``` |
| To | ``` let CIDetectorTypeQRCode: String ``` |

Modified CIDetectorTypeRectangle

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorTypeRectangle: NSString! ``` |
| To | ``` let CIDetectorTypeRectangle: String ``` |

Modified CIFeatureTypeFace

|  | Declaration |
| --- | --- |
| From | ``` let CIFeatureTypeFace: NSString! ``` |
| To | ``` let CIFeatureTypeFace: String ``` |

Modified CIFeatureTypeRectangle

|  | Declaration |
| --- | --- |
| From | ``` let CIFeatureTypeRectangle: NSString! ``` |
| To | ``` let CIFeatureTypeRectangle: String ``` |

Modified kCAAlignmentCenter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAlignmentCenter: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAlignmentCenter: String ``` | OS X 10.5 |

Modified kCAAlignmentJustified

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAlignmentJustified: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAlignmentJustified: String ``` | OS X 10.5 |

Modified kCAAlignmentLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAlignmentLeft: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAlignmentLeft: String ``` | OS X 10.5 |

Modified kCAAlignmentNatural

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAlignmentNatural: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAlignmentNatural: String ``` | OS X 10.5 |

Modified kCAAlignmentRight

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAlignmentRight: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAlignmentRight: String ``` | OS X 10.5 |

Modified kCAAnimationCubic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationCubic: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationCubic: String ``` | OS X 10.7 |

Modified kCAAnimationCubicPaced

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationCubicPaced: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationCubicPaced: String ``` | OS X 10.7 |

Modified kCAAnimationDiscrete

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationDiscrete: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationDiscrete: String ``` | OS X 10.5 |

Modified kCAAnimationLinear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationLinear: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationLinear: String ``` | OS X 10.5 |

Modified kCAAnimationPaced

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationPaced: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationPaced: String ``` | OS X 10.5 |

Modified kCAAnimationRotateAuto

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationRotateAuto: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationRotateAuto: String ``` | OS X 10.5 |

Modified kCAAnimationRotateAutoReverse

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAAnimationRotateAutoReverse: NSString! ``` | OS X 10.10 |
| To | ``` let kCAAnimationRotateAutoReverse: String ``` | OS X 10.5 |

Modified kCAEmitterBehaviorAlignToMotion

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorAlignToMotion: NSString! ``` |
| To | ``` let kCAEmitterBehaviorAlignToMotion: String ``` |

Modified kCAEmitterBehaviorAttractor

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorAttractor: NSString! ``` |
| To | ``` let kCAEmitterBehaviorAttractor: String ``` |

Modified kCAEmitterBehaviorColorOverLife

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorColorOverLife: NSString! ``` |
| To | ``` let kCAEmitterBehaviorColorOverLife: String ``` |

Modified kCAEmitterBehaviorDrag

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorDrag: NSString! ``` |
| To | ``` let kCAEmitterBehaviorDrag: String ``` |

Modified kCAEmitterBehaviorLight

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorLight: NSString! ``` |
| To | ``` let kCAEmitterBehaviorLight: String ``` |

Modified kCAEmitterBehaviorValueOverLife

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorValueOverLife: NSString! ``` |
| To | ``` let kCAEmitterBehaviorValueOverLife: String ``` |

Modified kCAEmitterBehaviorWave

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorWave: NSString! ``` |
| To | ``` let kCAEmitterBehaviorWave: String ``` |

Modified kCAEmitterLayerAdditive

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerAdditive: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerAdditive: String ``` | OS X 10.6 |

Modified kCAEmitterLayerBackToFront

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerBackToFront: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerBackToFront: String ``` | OS X 10.6 |

Modified kCAEmitterLayerCircle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerCircle: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerCircle: String ``` | OS X 10.6 |

Modified kCAEmitterLayerCuboid

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerCuboid: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerCuboid: String ``` | OS X 10.6 |

Modified kCAEmitterLayerLine

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerLine: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerLine: String ``` | OS X 10.6 |

Modified kCAEmitterLayerOldestFirst

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerOldestFirst: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerOldestFirst: String ``` | OS X 10.6 |

Modified kCAEmitterLayerOldestLast

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerOldestLast: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerOldestLast: String ``` | OS X 10.6 |

Modified kCAEmitterLayerOutline

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerOutline: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerOutline: String ``` | OS X 10.6 |

Modified kCAEmitterLayerPoint

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerPoint: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerPoint: String ``` | OS X 10.6 |

Modified kCAEmitterLayerPoints

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerPoints: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerPoints: String ``` | OS X 10.6 |

Modified kCAEmitterLayerRectangle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerRectangle: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerRectangle: String ``` | OS X 10.6 |

Modified kCAEmitterLayerSphere

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerSphere: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerSphere: String ``` | OS X 10.6 |

Modified kCAEmitterLayerSurface

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerSurface: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerSurface: String ``` | OS X 10.6 |

Modified kCAEmitterLayerUnordered

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerUnordered: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerUnordered: String ``` | OS X 10.6 |

Modified kCAEmitterLayerVolume

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAEmitterLayerVolume: NSString! ``` | OS X 10.10 |
| To | ``` let kCAEmitterLayerVolume: String ``` | OS X 10.6 |

Modified kCAFillModeBackwards

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillModeBackwards: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillModeBackwards: String ``` | OS X 10.5 |

Modified kCAFillModeBoth

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillModeBoth: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillModeBoth: String ``` | OS X 10.5 |

Modified kCAFillModeForwards

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillModeForwards: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillModeForwards: String ``` | OS X 10.5 |

Modified kCAFillModeRemoved

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillModeRemoved: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillModeRemoved: String ``` | OS X 10.5 |

Modified kCAFillRuleEvenOdd

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillRuleEvenOdd: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillRuleEvenOdd: String ``` | OS X 10.6 |

Modified kCAFillRuleNonZero

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFillRuleNonZero: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFillRuleNonZero: String ``` | OS X 10.6 |

Modified kCAFilterLinear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFilterLinear: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFilterLinear: String ``` | OS X 10.5 |

Modified kCAFilterNearest

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFilterNearest: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFilterNearest: String ``` | OS X 10.5 |

Modified kCAFilterTrilinear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAFilterTrilinear: NSString! ``` | OS X 10.10 |
| To | ``` let kCAFilterTrilinear: String ``` | OS X 10.6 |

Modified kCAGradientLayerAxial

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGradientLayerAxial: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGradientLayerAxial: String ``` | OS X 10.6 |

Modified kCAGravityBottom

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityBottom: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityBottom: String ``` | OS X 10.5 |

Modified kCAGravityBottomLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityBottomLeft: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityBottomLeft: String ``` | OS X 10.5 |

Modified kCAGravityBottomRight

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityBottomRight: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityBottomRight: String ``` | OS X 10.5 |

Modified kCAGravityCenter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityCenter: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityCenter: String ``` | OS X 10.5 |

Modified kCAGravityLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityLeft: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityLeft: String ``` | OS X 10.5 |

Modified kCAGravityResize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityResize: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityResize: String ``` | OS X 10.5 |

Modified kCAGravityResizeAspect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityResizeAspect: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityResizeAspect: String ``` | OS X 10.5 |

Modified kCAGravityResizeAspectFill

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityResizeAspectFill: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityResizeAspectFill: String ``` | OS X 10.5 |

Modified kCAGravityRight

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityRight: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityRight: String ``` | OS X 10.5 |

Modified kCAGravityTop

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityTop: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityTop: String ``` | OS X 10.5 |

Modified kCAGravityTopLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityTopLeft: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityTopLeft: String ``` | OS X 10.5 |

Modified kCAGravityTopRight

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAGravityTopRight: NSString! ``` | OS X 10.10 |
| To | ``` let kCAGravityTopRight: String ``` | OS X 10.5 |

Modified kCALineCapButt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineCapButt: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineCapButt: String ``` | OS X 10.6 |

Modified kCALineCapRound

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineCapRound: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineCapRound: String ``` | OS X 10.6 |

Modified kCALineCapSquare

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineCapSquare: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineCapSquare: String ``` | OS X 10.6 |

Modified kCALineJoinBevel

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineJoinBevel: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineJoinBevel: String ``` | OS X 10.6 |

Modified kCALineJoinMiter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineJoinMiter: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineJoinMiter: String ``` | OS X 10.6 |

Modified kCALineJoinRound

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCALineJoinRound: NSString! ``` | OS X 10.10 |
| To | ``` let kCALineJoinRound: String ``` | OS X 10.6 |

Modified kCAMediaTimingFunctionDefault

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAMediaTimingFunctionDefault: NSString! ``` | OS X 10.10 |
| To | ``` let kCAMediaTimingFunctionDefault: String ``` | OS X 10.6 |

Modified kCAMediaTimingFunctionEaseIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseIn: NSString! ``` | OS X 10.10 |
| To | ``` let kCAMediaTimingFunctionEaseIn: String ``` | OS X 10.5 |

Modified kCAMediaTimingFunctionEaseInEaseOut

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseInEaseOut: NSString! ``` | OS X 10.10 |
| To | ``` let kCAMediaTimingFunctionEaseInEaseOut: String ``` | OS X 10.5 |

Modified kCAMediaTimingFunctionEaseOut

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseOut: NSString! ``` | OS X 10.10 |
| To | ``` let kCAMediaTimingFunctionEaseOut: String ``` | OS X 10.5 |

Modified kCAMediaTimingFunctionLinear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAMediaTimingFunctionLinear: NSString! ``` | OS X 10.10 |
| To | ``` let kCAMediaTimingFunctionLinear: String ``` | OS X 10.5 |

Modified kCAOnOrderIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAOnOrderIn: NSString! ``` | OS X 10.10 |
| To | ``` let kCAOnOrderIn: String ``` | OS X 10.5 |

Modified kCAOnOrderOut

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAOnOrderOut: NSString! ``` | OS X 10.10 |
| To | ``` let kCAOnOrderOut: String ``` | OS X 10.5 |

Modified kCAScrollBoth

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAScrollBoth: NSString! ``` | OS X 10.10 |
| To | ``` let kCAScrollBoth: String ``` | OS X 10.5 |

Modified kCAScrollHorizontally

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAScrollHorizontally: NSString! ``` | OS X 10.10 |
| To | ``` let kCAScrollHorizontally: String ``` | OS X 10.5 |

Modified kCAScrollNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAScrollNone: NSString! ``` | OS X 10.10 |
| To | ``` let kCAScrollNone: String ``` | OS X 10.5 |

Modified kCAScrollVertically

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAScrollVertically: NSString! ``` | OS X 10.10 |
| To | ``` let kCAScrollVertically: String ``` | OS X 10.5 |

Modified kCATransactionAnimationDuration

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransactionAnimationDuration: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransactionAnimationDuration: String ``` | OS X 10.5 |

Modified kCATransactionAnimationTimingFunction

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransactionAnimationTimingFunction: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransactionAnimationTimingFunction: String ``` | OS X 10.6 |

Modified kCATransactionCompletionBlock

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransactionCompletionBlock: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransactionCompletionBlock: String ``` | OS X 10.6 |

Modified kCATransactionDisableActions

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransactionDisableActions: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransactionDisableActions: String ``` | OS X 10.5 |

Modified kCATransition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransition: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransition: String ``` | OS X 10.5 |

Modified kCATransitionFade

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionFade: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionFade: String ``` | OS X 10.5 |

Modified kCATransitionFromBottom

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionFromBottom: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionFromBottom: String ``` | OS X 10.5 |

Modified kCATransitionFromLeft

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionFromLeft: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionFromLeft: String ``` | OS X 10.5 |

Modified kCATransitionFromRight

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionFromRight: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionFromRight: String ``` | OS X 10.5 |

Modified kCATransitionFromTop

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionFromTop: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionFromTop: String ``` | OS X 10.5 |

Modified kCATransitionMoveIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionMoveIn: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionMoveIn: String ``` | OS X 10.5 |

Modified kCATransitionPush

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionPush: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionPush: String ``` | OS X 10.5 |

Modified kCATransitionReveal

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATransitionReveal: NSString! ``` | OS X 10.10 |
| To | ``` let kCATransitionReveal: String ``` | OS X 10.5 |

Modified kCATruncationEnd

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATruncationEnd: NSString! ``` | OS X 10.10 |
| To | ``` let kCATruncationEnd: String ``` | OS X 10.5 |

Modified kCATruncationMiddle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATruncationMiddle: NSString! ``` | OS X 10.10 |
| To | ``` let kCATruncationMiddle: String ``` | OS X 10.5 |

Modified kCATruncationNone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATruncationNone: NSString! ``` | OS X 10.10 |
| To | ``` let kCATruncationNone: String ``` | OS X 10.5 |

Modified kCATruncationStart

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCATruncationStart: NSString! ``` | OS X 10.10 |
| To | ``` let kCATruncationStart: String ``` | OS X 10.5 |

Modified kCAValueFunctionRotateX

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionRotateX: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionRotateX: String ``` | OS X 10.6 |

Modified kCAValueFunctionRotateY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionRotateY: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionRotateY: String ``` | OS X 10.6 |

Modified kCAValueFunctionRotateZ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionRotateZ: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionRotateZ: String ``` | OS X 10.6 |

Modified kCAValueFunctionScale

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionScale: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionScale: String ``` | OS X 10.6 |

Modified kCAValueFunctionScaleX

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionScaleX: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionScaleX: String ``` | OS X 10.6 |

Modified kCAValueFunctionScaleY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionScaleY: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionScaleY: String ``` | OS X 10.6 |

Modified kCAValueFunctionScaleZ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionScaleZ: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionScaleZ: String ``` | OS X 10.6 |

Modified kCAValueFunctionTranslate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionTranslate: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionTranslate: String ``` | OS X 10.6 |

Modified kCAValueFunctionTranslateX

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionTranslateX: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionTranslateX: String ``` | OS X 10.6 |

Modified kCAValueFunctionTranslateY

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionTranslateY: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionTranslateY: String ``` | OS X 10.6 |

Modified kCAValueFunctionTranslateZ

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCAValueFunctionTranslateZ: NSString! ``` | OS X 10.10 |
| To | ``` let kCAValueFunctionTranslateZ: String ``` | OS X 10.6 |

Modified kCIActiveKeys

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIActiveKeys: NSString! ``` | OS X 10.10 |
| To | ``` let kCIActiveKeys: String ``` | OS X 10.7 |

Modified kCIApplyOptionColorSpace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIApplyOptionColorSpace: NSString! ``` | OS X 10.10 |
| To | ``` let kCIApplyOptionColorSpace: String ``` | OS X 10.4 |

Modified kCIApplyOptionDefinition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIApplyOptionDefinition: NSString! ``` | OS X 10.10 |
| To | ``` let kCIApplyOptionDefinition: String ``` | OS X 10.4 |

Modified kCIApplyOptionExtent

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIApplyOptionExtent: NSString! ``` | OS X 10.10 |
| To | ``` let kCIApplyOptionExtent: String ``` | OS X 10.4 |

Modified kCIApplyOptionUserInfo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIApplyOptionUserInfo: NSString! ``` | OS X 10.10 |
| To | ``` let kCIApplyOptionUserInfo: String ``` | OS X 10.4 |

Modified kCIAttributeClass

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeClass: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeClass: String ``` | OS X 10.4 |

Modified kCIAttributeDefault

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeDefault: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeDefault: String ``` | OS X 10.4 |

Modified kCIAttributeDescription

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeDescription: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeDescription: String ``` | OS X 10.5 |

Modified kCIAttributeDisplayName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeDisplayName: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeDisplayName: String ``` | OS X 10.4 |

Modified kCIAttributeFilterCategories

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeFilterCategories: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeFilterCategories: String ``` | OS X 10.4 |

Modified kCIAttributeFilterDisplayName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeFilterDisplayName: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeFilterDisplayName: String ``` | OS X 10.4 |

Modified kCIAttributeFilterName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeFilterName: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeFilterName: String ``` | OS X 10.4 |

Modified kCIAttributeIdentity

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeIdentity: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeIdentity: String ``` | OS X 10.4 |

Modified kCIAttributeMax

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeMax: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeMax: String ``` | OS X 10.4 |

Modified kCIAttributeMin

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeMin: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeMin: String ``` | OS X 10.4 |

Modified kCIAttributeName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeName: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeName: String ``` | OS X 10.4 |

Modified kCIAttributeReferenceDocumentation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeReferenceDocumentation: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeReferenceDocumentation: String ``` | OS X 10.5 |

Modified kCIAttributeSliderMax

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeSliderMax: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeSliderMax: String ``` | OS X 10.4 |

Modified kCIAttributeSliderMin

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeSliderMin: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeSliderMin: String ``` | OS X 10.4 |

Modified kCIAttributeType

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeType: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeType: String ``` | OS X 10.4 |

Modified kCIAttributeTypeAngle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeAngle: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeAngle: String ``` | OS X 10.4 |

Modified kCIAttributeTypeBoolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeBoolean: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeBoolean: String ``` | OS X 10.4 |

Modified kCIAttributeTypeCount

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeCount: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeCount: String ``` | OS X 10.5 |

Modified kCIAttributeTypeDistance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeDistance: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeDistance: String ``` | OS X 10.4 |

Modified kCIAttributeTypeGradient

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeGradient: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeGradient: String ``` | OS X 10.4 |

Modified kCIAttributeTypeInteger

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeInteger: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeInteger: String ``` | OS X 10.5 |

Modified kCIAttributeTypeOffset

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeOffset: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeOffset: String ``` | OS X 10.4 |

Modified kCIAttributeTypeOpaqueColor

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeOpaqueColor: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeOpaqueColor: String ``` | OS X 10.4 |

Modified kCIAttributeTypePosition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypePosition: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypePosition: String ``` | OS X 10.4 |

Modified kCIAttributeTypePosition3

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypePosition3: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypePosition3: String ``` | OS X 10.4 |

Modified kCIAttributeTypeRectangle

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeRectangle: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeRectangle: String ``` | OS X 10.4 |

Modified kCIAttributeTypeScalar

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeScalar: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeScalar: String ``` | OS X 10.4 |

Modified kCIAttributeTypeTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIAttributeTypeTime: NSString! ``` | OS X 10.10 |
| To | ``` let kCIAttributeTypeTime: String ``` | OS X 10.4 |

Modified kCICategoryBlur

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryBlur: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryBlur: String ``` | OS X 10.4 |

Modified kCICategoryBuiltIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryBuiltIn: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryBuiltIn: String ``` | OS X 10.4 |

Modified kCICategoryColorAdjustment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryColorAdjustment: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryColorAdjustment: String ``` | OS X 10.4 |

Modified kCICategoryColorEffect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryColorEffect: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryColorEffect: String ``` | OS X 10.4 |

Modified kCICategoryCompositeOperation

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryCompositeOperation: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryCompositeOperation: String ``` | OS X 10.4 |

Modified kCICategoryDistortionEffect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryDistortionEffect: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryDistortionEffect: String ``` | OS X 10.4 |

Modified kCICategoryFilterGenerator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryFilterGenerator: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryFilterGenerator: String ``` | OS X 10.5 |

Modified kCICategoryGenerator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryGenerator: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryGenerator: String ``` | OS X 10.4 |

Modified kCICategoryGeometryAdjustment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryGeometryAdjustment: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryGeometryAdjustment: String ``` | OS X 10.4 |

Modified kCICategoryGradient

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryGradient: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryGradient: String ``` | OS X 10.4 |

Modified kCICategoryHalftoneEffect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryHalftoneEffect: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryHalftoneEffect: String ``` | OS X 10.4 |

Modified kCICategoryHighDynamicRange

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryHighDynamicRange: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryHighDynamicRange: String ``` | OS X 10.4 |

Modified kCICategoryInterlaced

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryInterlaced: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryInterlaced: String ``` | OS X 10.4 |

Modified kCICategoryNonSquarePixels

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryNonSquarePixels: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryNonSquarePixels: String ``` | OS X 10.4 |

Modified kCICategoryReduction

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryReduction: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryReduction: String ``` | OS X 10.5 |

Modified kCICategorySharpen

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategorySharpen: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategorySharpen: String ``` | OS X 10.4 |

Modified kCICategoryStillImage

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryStillImage: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryStillImage: String ``` | OS X 10.4 |

Modified kCICategoryStylize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryStylize: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryStylize: String ``` | OS X 10.4 |

Modified kCICategoryTileEffect

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryTileEffect: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryTileEffect: String ``` | OS X 10.4 |

Modified kCICategoryTransition

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryTransition: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryTransition: String ``` | OS X 10.4 |

Modified kCICategoryVideo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCICategoryVideo: NSString! ``` | OS X 10.10 |
| To | ``` let kCICategoryVideo: String ``` | OS X 10.4 |

Modified kCIContextOutputColorSpace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIContextOutputColorSpace: NSString! ``` | OS X 10.10 |
| To | ``` let kCIContextOutputColorSpace: String ``` | OS X 10.4 |

Modified kCIContextUseSoftwareRenderer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIContextUseSoftwareRenderer: NSString! ``` | OS X 10.10 |
| To | ``` let kCIContextUseSoftwareRenderer: String ``` | OS X 10.4 |

Modified kCIContextWorkingColorSpace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIContextWorkingColorSpace: NSString! ``` | OS X 10.10 |
| To | ``` let kCIContextWorkingColorSpace: String ``` | OS X 10.4 |

Modified kCIFilterGeneratorExportedKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIFilterGeneratorExportedKey: NSString! ``` |
| To | ``` let kCIFilterGeneratorExportedKey: String ``` |

Modified kCIFilterGeneratorExportedKeyName

|  | Declaration |
| --- | --- |
| From | ``` let kCIFilterGeneratorExportedKeyName: NSString! ``` |
| To | ``` let kCIFilterGeneratorExportedKeyName: String ``` |

Modified kCIFilterGeneratorExportedKeyTargetObject

|  | Declaration |
| --- | --- |
| From | ``` let kCIFilterGeneratorExportedKeyTargetObject: NSString! ``` |
| To | ``` let kCIFilterGeneratorExportedKeyTargetObject: String ``` |

Modified kCIFormatARGB8

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCIFormatRGBA16

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCIFormatRGBAf

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCIFormatRGBAh

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCIImageAutoAdjustCrop

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustCrop: NSString! ``` |
| To | ``` let kCIImageAutoAdjustCrop: String ``` |

Modified kCIImageAutoAdjustEnhance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageAutoAdjustEnhance: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageAutoAdjustEnhance: String ``` | OS X 10.8 |

Modified kCIImageAutoAdjustFeatures

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageAutoAdjustFeatures: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageAutoAdjustFeatures: String ``` | OS X 10.8 |

Modified kCIImageAutoAdjustLevel

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustLevel: NSString! ``` |
| To | ``` let kCIImageAutoAdjustLevel: String ``` |

Modified kCIImageAutoAdjustRedEye

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageAutoAdjustRedEye: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageAutoAdjustRedEye: String ``` | OS X 10.8 |

Modified kCIImageColorSpace

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageColorSpace: NSString! ``` |
| To | ``` let kCIImageColorSpace: String ``` |

Modified kCIImageProperties

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageProperties: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageProperties: String ``` | OS X 10.8 |

Modified kCIImageProviderTileSize

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageProviderTileSize: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageProviderTileSize: String ``` | OS X 10.4 |

Modified kCIImageProviderUserInfo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageProviderUserInfo: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageProviderUserInfo: String ``` | OS X 10.4 |

Modified kCIImageTextureFormat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageTextureFormat: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageTextureFormat: String ``` | OS X 10.9 |

Modified kCIImageTextureTarget

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIImageTextureTarget: NSString! ``` | OS X 10.10 |
| To | ``` let kCIImageTextureTarget: String ``` | OS X 10.9 |

Modified kCIInputAllowDraftModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputAllowDraftModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputAllowDraftModeKey: String ``` | OS X 10.5 |

Modified kCIInputAngleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputAngleKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputAngleKey: String ``` | OS X 10.5 |

Modified kCIInputAspectRatioKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputAspectRatioKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputAspectRatioKey: String ``` | OS X 10.5 |

Modified kCIInputBackgroundImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputBackgroundImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputBackgroundImageKey: String ``` | OS X 10.5 |

Modified kCIInputBiasKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputBiasKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputBiasKey: String ``` | OS X 10.5 |

Modified kCIInputBoostKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputBoostKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputBoostKey: String ``` | OS X 10.5 |

Modified kCIInputBoostShadowAmountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputBoostShadowAmountKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputBoostShadowAmountKey: String ``` | OS X 10.5 |

Modified kCIInputBrightnessKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputBrightnessKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputBrightnessKey: String ``` | OS X 10.5 |

Modified kCIInputCenterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputCenterKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputCenterKey: String ``` | OS X 10.5 |

Modified kCIInputColorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputColorKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputColorKey: String ``` | OS X 10.5 |

Modified kCIInputColorNoiseReductionAmountKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputColorNoiseReductionAmountKey: NSString! ``` |
| To | ``` let kCIInputColorNoiseReductionAmountKey: String ``` |

Modified kCIInputContrastKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputContrastKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputContrastKey: String ``` | OS X 10.5 |

Modified kCIInputDecoderVersionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputDecoderVersionKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputDecoderVersionKey: String ``` | OS X 10.5 |

Modified kCIInputEVKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputEVKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputEVKey: String ``` | OS X 10.5 |

Modified kCIInputEnableChromaticNoiseTrackingKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputEnableChromaticNoiseTrackingKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputEnableChromaticNoiseTrackingKey: String ``` | OS X 10.5 |

Modified kCIInputEnableSharpeningKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputEnableSharpeningKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputEnableSharpeningKey: String ``` | OS X 10.5 |

Modified kCIInputEnableVendorLensCorrectionKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputEnableVendorLensCorrectionKey: NSString! ``` |
| To | ``` let kCIInputEnableVendorLensCorrectionKey: String ``` |

Modified kCIInputExtentKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputExtentKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputExtentKey: String ``` | OS X 10.5 |

Modified kCIInputGradientImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputGradientImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputGradientImageKey: String ``` | OS X 10.5 |

Modified kCIInputIgnoreImageOrientationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputIgnoreImageOrientationKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputIgnoreImageOrientationKey: String ``` | OS X 10.5 |

Modified kCIInputImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputImageKey: String ``` | OS X 10.5 |

Modified kCIInputImageOrientationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputImageOrientationKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputImageOrientationKey: String ``` | OS X 10.5 |

Modified kCIInputIntensityKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputIntensityKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputIntensityKey: String ``` | OS X 10.5 |

Modified kCIInputLinearSpaceFilter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputLinearSpaceFilter: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputLinearSpaceFilter: String ``` | OS X 10.7 |

Modified kCIInputLuminanceNoiseReductionAmountKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputLuminanceNoiseReductionAmountKey: NSString! ``` |
| To | ``` let kCIInputLuminanceNoiseReductionAmountKey: String ``` |

Modified kCIInputMaskImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputMaskImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputMaskImageKey: String ``` | OS X 10.5 |

Modified kCIInputNeutralChromaticityXKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNeutralChromaticityXKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNeutralChromaticityXKey: String ``` | OS X 10.5 |

Modified kCIInputNeutralChromaticityYKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNeutralChromaticityYKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNeutralChromaticityYKey: String ``` | OS X 10.5 |

Modified kCIInputNeutralLocationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNeutralLocationKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNeutralLocationKey: String ``` | OS X 10.5 |

Modified kCIInputNeutralTemperatureKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNeutralTemperatureKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNeutralTemperatureKey: String ``` | OS X 10.5 |

Modified kCIInputNeutralTintKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNeutralTintKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNeutralTintKey: String ``` | OS X 10.5 |

Modified kCIInputNoiseReductionAmountKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputNoiseReductionAmountKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputNoiseReductionAmountKey: String ``` | OS X 10.7 |

Modified kCIInputNoiseReductionContrastAmountKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputNoiseReductionContrastAmountKey: NSString! ``` |
| To | ``` let kCIInputNoiseReductionContrastAmountKey: String ``` |

Modified kCIInputNoiseReductionDetailAmountKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputNoiseReductionDetailAmountKey: NSString! ``` |
| To | ``` let kCIInputNoiseReductionDetailAmountKey: String ``` |

Modified kCIInputNoiseReductionSharpnessAmountKey

|  | Declaration |
| --- | --- |
| From | ``` let kCIInputNoiseReductionSharpnessAmountKey: NSString! ``` |
| To | ``` let kCIInputNoiseReductionSharpnessAmountKey: String ``` |

Modified kCIInputRadiusKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputRadiusKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputRadiusKey: String ``` | OS X 10.5 |

Modified kCIInputRefractionKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputRefractionKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputRefractionKey: String ``` | OS X 10.5 |

Modified kCIInputSaturationKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputSaturationKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputSaturationKey: String ``` | OS X 10.5 |

Modified kCIInputScaleFactorKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIInputScaleFactorKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputScaleFactorKey: String ``` | OS X 10.5 |

Modified kCIInputScaleKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputScaleKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputScaleKey: String ``` | OS X 10.5 |

Modified kCIInputShadingImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputShadingImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputShadingImageKey: String ``` | OS X 10.5 |

Modified kCIInputSharpnessKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputSharpnessKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputSharpnessKey: String ``` | OS X 10.5 |

Modified kCIInputTargetImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputTargetImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputTargetImageKey: String ``` | OS X 10.5 |

Modified kCIInputTimeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputTimeKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputTimeKey: String ``` | OS X 10.5 |

Modified kCIInputTransformKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputTransformKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputTransformKey: String ``` | OS X 10.5 |

Modified kCIInputWidthKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIInputWidthKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIInputWidthKey: String ``` | OS X 10.5 |

Modified kCIOutputImageKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIOutputImageKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIOutputImageKey: String ``` | OS X 10.5 |

Modified kCIOutputNativeSizeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCIOutputNativeSizeKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCIOutputNativeSizeKey: String ``` | OS X 10.5 |

Modified kCISamplerAffineMatrix

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerAffineMatrix: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerAffineMatrix: String ``` | OS X 10.4 |

Modified kCISamplerColorSpace

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerColorSpace: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerColorSpace: String ``` | OS X 10.4 |

Modified kCISamplerFilterLinear

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerFilterLinear: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerFilterLinear: String ``` | OS X 10.4 |

Modified kCISamplerFilterMode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerFilterMode: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerFilterMode: String ``` | OS X 10.4 |

Modified kCISamplerFilterNearest

|  | Declaration |
| --- | --- |
| From | ``` var kCISamplerFilterNearest: NSString! ``` |
| To | ``` let kCISamplerFilterNearest: String ``` |

Modified kCISamplerWrapBlack

|  | Declaration |
| --- | --- |
| From | ``` var kCISamplerWrapBlack: NSString! ``` |
| To | ``` let kCISamplerWrapBlack: String ``` |

Modified kCISamplerWrapClamp

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerWrapClamp: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerWrapClamp: String ``` | OS X 10.4 |

Modified kCISamplerWrapMode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCISamplerWrapMode: NSString! ``` | OS X 10.10 |
| To | ``` let kCISamplerWrapMode: String ``` | OS X 10.4 |

Modified kCISupportedDecoderVersionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let kCISupportedDecoderVersionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let kCISupportedDecoderVersionsKey: String ``` | OS X 10.5 |

Modified kCIUIParameterSet

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIUIParameterSet: NSString! ``` | OS X 10.10 |
| To | ``` let kCIUIParameterSet: String ``` | OS X 10.5 |

Modified kCIUISetAdvanced

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIUISetAdvanced: NSString! ``` | OS X 10.10 |
| To | ``` let kCIUISetAdvanced: String ``` | OS X 10.5 |

Modified kCIUISetBasic

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIUISetBasic: NSString! ``` | OS X 10.10 |
| To | ``` let kCIUISetBasic: String ``` | OS X 10.5 |

Modified kCIUISetDevelopment

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIUISetDevelopment: NSString! ``` | OS X 10.10 |
| To | ``` let kCIUISetDevelopment: String ``` | OS X 10.5 |

Modified kCIUISetIntermediate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCIUISetIntermediate: NSString! ``` | OS X 10.10 |
| To | ``` let kCIUISetIntermediate: String ``` | OS X 10.5 |

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
