---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreImage.html
archived_at: '2026-07-18T02:53:27.018684Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreImage Changes for Swift

### CoreImage (Added)

Added [CIColor.alpha](https://developer.apple.com/documentation/coreimage/cicolor/1437981-alpha)Added [CIColor.blue](https://developer.apple.com/documentation/coreimage/cicolor/1438033-blue)Added [CIColor.colorSpace](https://developer.apple.com/documentation/coreimage/cicolor/1437917-colorspace)Added [CIColor.components](https://developer.apple.com/documentation/coreimage/cicolor/1437862-components)Added [CIColor.green](https://developer.apple.com/documentation/coreimage/cicolor/1437607-green)Added [CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coreimage/cicolor/1438084-init)Added [CIColor.numberOfComponents](https://developer.apple.com/documentation/coreimage/cicolor/1438151-numberofcomponents)Added [CIColor.red](https://developer.apple.com/documentation/coreimage/cicolor/1437969-red)Added [CIColor.stringRepresentation](https://developer.apple.com/documentation/coreimage/cicolor/1437910-stringrepresentation)Added [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel)Added [CIColorKernel.applyWithExtent(_: CGRect, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438110-applywithextent)Added [CIColorKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438143-init)Added [CIContext.init(MTLDevice: MTLDevice)](https://developer.apple.com/documentation/coreimage/cicontext/1437609-contextwithmtldevice)Added [CIContext.init(MTLDevice: MTLDevice, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1437711-contextwithmtldevice)Added [CIContext.init(options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1438261-init)Added [CIContext.render(_: CIImage, toCVPixelBuffer: CVPixelBuffer)](https://developer.apple.com/documentation/coreimage/cicontext/1437853-render)Added [CIContext.render(_: CIImage, toCVPixelBuffer: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437835-render)Added [CIContext.render(_: CIImage, toMTLTexture: MTLTexture, commandBuffer: MTLCommandBuffer?, bounds: CGRect, colorSpace: CGColorSpace)](https://developer.apple.com/documentation/coreimage/cicontext/1438026-render)Added [CIContext.workingColorSpace](https://developer.apple.com/documentation/coreimage/cicontext/1438061-workingcolorspace)Added [CIFilter.attributes](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes)Added [CIFilter.inputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438013-inputkeys)Added [CIFilter.outputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438122-outputkeys)Added [CIFilterGenerator.classAttributes](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437855-classattributes)Added [CIFilterGenerator.exportedKeys](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437955-exportedkeys)Added [CIFilterShape.extent](https://developer.apple.com/documentation/coreimage/cifiltershape/1438022-extent)Added [CIImage.colorSpace](https://developer.apple.com/documentation/coreimage/ciimage/1437750-colorspace)Added [CIImage.definition](https://developer.apple.com/documentation/coreimage/ciimage/1437804-definition)Added [CIImage.extent](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)Added [CIImage.init(CVPixelBuffer: CVPixelBuffer)](https://developer.apple.com/documentation/coreimage/ciimage/1438072-init)Added [CIImage.init(CVPixelBuffer: CVPixelBuffer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438209-initwithcvpixelbuffer)Added [CIImage.init(MTLTexture: MTLTexture, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437890-init)Added [CIImage.properties](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)Added [CIImage.regionOfInterestForImage(_: CIImage, inRect: CGRect) -> CGRect](https://developer.apple.com/documentation/coreimage/ciimage/1437994-regionofinterest)Added [CIImage.url](https://developer.apple.com/documentation/coreimage/ciimage/1438195-url)Added [CIImageAccumulator.extent](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427714-extent)Added [CIImageAccumulator.format](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427716-format)Added [CIKernel.applyWithExtent(_: CGRect, roiCallback: CIKernelROICallback, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cikernel/1438243-applywithextent)Added [CIKernel.name](https://developer.apple.com/documentation/coreimage/cikernel/1438067-name)Added [CISampler.definition](https://developer.apple.com/documentation/coreimage/cisampler/1437877-definition)Added [CISampler.extent](https://developer.apple.com/documentation/coreimage/cisampler/1437872-extent)Added [CITextFeature](https://developer.apple.com/documentation/coreimage/citextfeature)Added [CITextFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438004-bottomleft)Added [CITextFeature.bottomRight](https://developer.apple.com/documentation/coreimage/citextfeature/1437659-bottomright)Added [CITextFeature.bounds](https://developer.apple.com/documentation/coreimage/citextfeature/1437885-bounds)Added [CITextFeature.subFeatures](https://developer.apple.com/documentation/coreimage/citextfeature/1437810-subfeatures)Added [CITextFeature.topLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438221-topleft)Added [CITextFeature.topRight](https://developer.apple.com/documentation/coreimage/citextfeature/1438282-topright)Added [CIVector.CGAffineTransformValue](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)Added [CIVector.CGPointValue](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)Added [CIVector.CGRectValue](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)Added [CIVector.count](https://developer.apple.com/documentation/coreimage/civector/1438197-count)Added [CIVector.stringRepresentation](https://developer.apple.com/documentation/coreimage/civector/1437752-stringrepresentation)Added [CIVector.W](https://developer.apple.com/documentation/coreimage/civector/1438058-w)Added [CIVector.X](https://developer.apple.com/documentation/coreimage/civector/1437738-x)Added [CIVector.Y](https://developer.apple.com/documentation/coreimage/civector/1437843-y)Added [CIVector.Z](https://developer.apple.com/documentation/coreimage/civector/1437627-z)Added [CIWarpKernel](https://developer.apple.com/documentation/coreimage/ciwarpkernel)Added [CIWarpKernel.applyWithExtent(_: CGRect, roiCallback: CIKernelROICallback, inputImage: CIImage, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1437798-apply)Added [CIWarpKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1438278-init)Added [CIDetectorNumberOfAngles](https://developer.apple.com/documentation/coreimage/cidetectornumberofangles)Added [CIDetectorReturnSubFeatures](https://developer.apple.com/documentation/coreimage/cidetectorreturnsubfeatures)Added [CIDetectorTypeText](https://developer.apple.com/documentation/coreimage/cidetectortypetext)Added [CIFeatureTypeQRCode](https://developer.apple.com/documentation/coreimage/cifeaturetypeqrcode)Added [CIFeatureTypeText](https://developer.apple.com/documentation/coreimage/cifeaturetypetext)Added [CIKernelROICallback](https://developer.apple.com/documentation/coreimage/cikernelroicallback)Added [kCIAttributeFilterAvailable_iOS](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_ios)Added [kCIAttributeFilterAvailable_Mac](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_mac)Added [kCIAttributeTypeColor](https://developer.apple.com/documentation/coreimage/kciattributetypecolor)Added [kCIAttributeTypeImage](https://developer.apple.com/documentation/coreimage/kciattributetypeimage)Added [kCIAttributeTypeTransform](https://developer.apple.com/documentation/coreimage/kciattributetypetransform)Added [kCIContextHighQualityDownsample](https://developer.apple.com/documentation/coreimage/cicontextoption/1437699-highqualitydownsample)Added [kCIContextWorkingFormat](https://developer.apple.com/documentation/coreimage/cicontextoption/1437788-workingformat)Added [kCIFormatA16](https://developer.apple.com/documentation/coreimage/kciformata16)Added [kCIFormatA8](https://developer.apple.com/documentation/coreimage/kciformata8)Added [kCIFormatABGR8](https://developer.apple.com/documentation/coreimage/kciformatabgr8)Added [kCIFormatAf](https://developer.apple.com/documentation/coreimage/kciformataf)Added [kCIFormatAh](https://developer.apple.com/documentation/coreimage/kciformatah)Added [kCIFormatBGRA8](https://developer.apple.com/documentation/coreimage/kciformatbgra8)Added [kCIFormatR16](https://developer.apple.com/documentation/coreimage/kciformatr16)Added [kCIFormatR8](https://developer.apple.com/documentation/coreimage/ciformat/1437695-r8)Added [kCIFormatRf](https://developer.apple.com/documentation/coreimage/kciformatrf)Added [kCIFormatRG16](https://developer.apple.com/documentation/coreimage/ciformat/1437648-rg16)Added [kCIFormatRG8](https://developer.apple.com/documentation/coreimage/kciformatrg8)Added [kCIFormatRGBA8](https://developer.apple.com/documentation/coreimage/kciformatrgba8)Added [kCIFormatRGf](https://developer.apple.com/documentation/coreimage/ciformat/1438157-rgf)Added [kCIFormatRGh](https://developer.apple.com/documentation/coreimage/kciformatrgh)Added [kCIFormatRh](https://developer.apple.com/documentation/coreimage/kciformatrh)Added [kCIInputVersionKey](https://developer.apple.com/documentation/coreimage/kciinputversionkey)Added [kCIInputWeightsKey](https://developer.apple.com/documentation/coreimage/kciinputweightskey)Added UNIFIED_CORE_IMAGEModified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIColor : NSObject, NSCoding, NSCopying {     init!(CGColor c: CGColor!) -> CIColor     class func colorWithCGColor(_ c: CGColor!) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor!     init!(string representation: String!) -> CIColor     class func colorWithString(_ representation: String!) -> CIColor!     init!(CGColor c: CGColor!)     func numberOfComponents() -> Int     func components() -> UnsafePointer<CGFloat>     func alpha() -> CGFloat     func colorSpace() -> Unmanaged<CGColorSpace>!     func red() -> CGFloat     func green() -> CGFloat     func blue() -> CGFloat     func stringRepresentation() -> String! } extension CIColor {     init?(color color: NSColor) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(CGColor c: CGColor)     class func colorWithCGColor(_ c: CGColor) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> Self     convenience init(string representation: String)     class func colorWithString(_ representation: String) -> Self     init(CGColor c: CGColor)     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     var numberOfComponents: Int { get }     var components: UnsafePointer<CGFloat> { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace { get }     var red: CGFloat { get }     var green: CGFloat { get }     var blue: CGFloat { get }     var stringRepresentation: String { get } } extension CIColor {     convenience init?(color color: NSColor) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIColor.init(CGColor: CGColor)](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGColor c: CGColor!) ``` | QuartzCore |
| To | ``` init(CGColor c: CGColor) ``` | CoreImage |

Modified [CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat)](https://developer.apple.com/documentation/coreimage/cicolor/1437941-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor ``` | QuartzCore |
| To | ``` convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat) ``` | CoreImage |

Modified [CIColor.init(string: String)](https://developer.apple.com/documentation/coreimage/cicolor/1438059-colorwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string representation: String!) -> CIColor ``` | QuartzCore |
| To | ``` convenience init(string representation: String) ``` | CoreImage |

Modified [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIContext : NSObject {     init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext!     init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, options dict: [NSObject : AnyObject]!) -> CIContext!     init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGContext(_ ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext!     class func offlineGPUCount() -> UInt32     init!(forOfflineGPUAtIndex index: UInt32) -> CIContext     class func contextForOfflineGPUAtIndex(_ index: UInt32) -> CIContext!     init!(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext     class func contextForOfflineGPUAtIndex(_ index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext!     func drawImage(_ im: CIImage!, atPoint p: CGPoint, fromRect src: CGRect)     func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect)     func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage!     func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage!     func createCGLayerWithSize(_ size: CGSize, info d: CFDictionary!) -> CGLayer!     func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!)     func render(_ im: CIImage!, toIOSurface surface: IOSurface!, bounds r: CGRect, colorSpace cs: CGColorSpace!)     func reclaimResources()     func clearCaches() } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIContext : NSObject {      init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?)     class func contextWithCGLContext(_ cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?) -> CIContext      init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, options options: [String : AnyObject]?)     class func contextWithCGLContext(_ cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, options options: [String : AnyObject]?) -> CIContext      init(CGContext cgctx: CGContext, options options: [String : AnyObject]?)     class func contextWithCGContext(_ cgctx: CGContext, options options: [String : AnyObject]?) -> CIContext      init(options options: [String : AnyObject]?)     class func contextWithOptions(_ options: [String : AnyObject]?) -> CIContext      init(MTLDevice device: MTLDevice)     class func contextWithMTLDevice(_ device: MTLDevice) -> CIContext      init(MTLDevice device: MTLDevice, options options: [String : AnyObject]?)     class func contextWithMTLDevice(_ device: MTLDevice, options options: [String : AnyObject]?) -> CIContext     var workingColorSpace: CGColorSpace { get }     func drawImage(_ image: CIImage, atPoint atPoint: CGPoint, fromRect fromRect: CGRect)     func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect)     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage     func createCGLayerWithSize(_ size: CGSize, info info: CFDictionary?) -> CGLayer     func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toIOSurface surface: IOSurface, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toMTLTexture texture: MTLTexture, commandBuffer commandBuffer: MTLCommandBuffer?, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace)     func reclaimResources()     func clearCaches()     func inputImageMaximumSize() -> CGSize     func outputImageMaximumSize() -> CGSize } extension CIContext {     class func offlineGPUCount() -> UInt32      init(forOfflineGPUAtIndex index: UInt32)     class func contextForOfflineGPUAtIndex(_ index: UInt32) -> CIContext      init(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj)     class func contextForOfflineGPUAtIndex(_ index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj) -> CIContext } ``` | OS X 10.4 | CoreImage |

Modified [CIContext.clearCaches()](https://developer.apple.com/documentation/coreimage/cicontext/1437790-clearcaches)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage! ``` | QuartzCore |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage ``` | CoreImage |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage! ``` | QuartzCore |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage ``` | CoreImage |

Modified [CIContext.createCGLayerWithSize(_: CGSize, info: CFDictionary?) -> CGLayer](https://developer.apple.com/documentation/coreimage/cicontext/1438267-createcglayerwithsize)

|  | Declaration | Introduction | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` func createCGLayerWithSize(_ size: CGSize, info d: CFDictionary!) -> CGLayer! ``` | OS X 10.10 | -- | QuartzCore |
| To | ``` func createCGLayerWithSize(_ size: CGSize, info info: CFDictionary?) -> CGLayer ``` | OS X 10.4 | OS X 10.11 | CoreImage |

Modified [CIContext.drawImage(_: CIImage, inRect: CGRect, fromRect: CGRect)](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect) ``` | QuartzCore |
| To | ``` func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect) ``` | CoreImage |

Modified [CIContext.init(CGContext: CGContext, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1437864-contextwithcgcontext)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | OS X 10.10 | QuartzCore |
| To | ``` init(CGContext cgctx: CGContext, options options: [String : AnyObject]?) ``` | OS X 10.4 | CoreImage |

Modified [CIContext.init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, colorSpace: CGColorSpace?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1438137-contextwithcglcontext)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | QuartzCore |
| To | ``` init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIContext.init(forOfflineGPUAtIndex: UInt32)](https://developer.apple.com/documentation/coreimage/cicontext/1437772-contextforofflinegpuatindex)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(forOfflineGPUAtIndex index: UInt32) -> CIContext ``` | QuartzCore |
| To | ``` init(forOfflineGPUAtIndex index: UInt32) ``` | CoreImage |

Modified [CIContext.init(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [String : AnyObject]?, sharedContext: CGLContextObj)](https://developer.apple.com/documentation/coreimage/cicontext/1437758-contextforofflinegpuatindex)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext ``` | QuartzCore |
| To | ``` init(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj) ``` | CoreImage |

Modified [CIContext.offlineGPUCount() -> UInt32 [class]](https://developer.apple.com/documentation/coreimage/cicontext/1437817-offlinegpucount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIContext.reclaimResources()](https://developer.apple.com/documentation/coreimage/cicontext/1437967-reclaimresources)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIContext.render(_: CIImage, toBitmap: UnsafeMutablePointer<Void>, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIContext.render(_: CIImage, toIOSurface: IOSurface, bounds: CGRect, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437778-render)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func render(_ im: CIImage!, toIOSurface surface: IOSurface!, bounds r: CGRect, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` func render(_ image: CIImage, toIOSurface surface: IOSurface, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIDetector : NSObject {     init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector     class func detectorOfType(_ type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector!     func featuresInImage(_ image: CIImage!) -> [AnyObject]!     func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIDetector : NSObject {      init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?)     class func detectorOfType(_ type: String, context context: CIContext?, options options: [String : AnyObject]?) -> CIDetector     func featuresInImage(_ image: CIImage) -> [CIFeature]     func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] } ``` | OS X 10.7 | CoreImage |

Modified [CIDetector.featuresInImage(_: CIImage) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func featuresInImage(_ image: CIImage) -> [CIFeature] ``` | CoreImage |

Modified [CIDetector.featuresInImage(_: CIImage, options: [String : AnyObject]?) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] ``` | CoreImage |

Modified [CIDetector.init(ofType: String, context: CIContext?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` | QuartzCore |
| To | ``` init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.7 | CoreImage |

Modified [CIFaceFeature.bounds](https://developer.apple.com/documentation/coreimage/cifacefeature/1438068-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.faceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1437689-faceangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasFaceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1438165-hasfaceangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasLeftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437900-haslefteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasMouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437976-hasmouthposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasRightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438076-hasrighteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasSmile](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasTrackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437731-hastrackingframecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasTrackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437683-hastrackingid)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.leftEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437630-lefteyeclosed)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.leftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437923-lefteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.mouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438020-mouthposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.rightEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437615-righteyeclosed)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.rightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438213-righteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.trackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437953-trackingframecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.trackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437709-trackingid)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIFeature : NSObject {     var type: String! { get }     var bounds: CGRect { get } } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIFeature : NSObject {     var type: String { get }     var bounds: CGRect { get } } ``` | OS X 10.7 | CoreImage |

Modified [CIFeature.bounds](https://developer.apple.com/documentation/coreimage/cifeature/1437782-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var type: String! { get } ``` | QuartzCore |
| To | ``` var type: String { get } ``` | CoreImage |

Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIFilter : NSObject, NSCoding, NSCopying {     var outputImage: CIImage! { get }     func inputKeys() -> [AnyObject]!     func outputKeys() -> [AnyObject]!     func setDefaults()     func attributes() -> [NSObject : AnyObject]!     func apply(_ k: CIKernel!, arguments args: [AnyObject]!, options dict: [NSObject : AnyObject]!) -> CIImage! } extension CIFilter {     func viewForUIConfiguration(_ inUIConfiguration: [NSObject : AnyObject]!, excludedKeys inKeys: [AnyObject]!) -> IKFilterUIView! } extension CIFilter {     var name: String!     var enabled: Bool } extension CIFilter {     func apply(_ k: CIKernel!, args args: [AnyObject]!, options options: (NSCopying, AnyObject)...) -> CIImage     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } extension CIFilter {     init!(name name: String!) -> CIFilter     class func filterWithName(_ name: String!) -> CIFilter!     init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter     class func filterWithName(_ name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter!     class func filterNamesInCategory(_ category: String!) -> [AnyObject]!     class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]!     class func registerFilterName(_ name: String!, constructor anObject: CIFilterConstructor!, classAttributes attributes: [NSObject : AnyObject]!)     class func localizedNameForFilterName(_ filterName: String!) -> String!     class func localizedNameForCategory(_ category: String!) -> String!     class func localizedDescriptionForFilterName(_ filterName: String!) -> String!     class func localizedReferenceDocumentationForFilterName(_ filterName: String!) -> NSURL! } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData!     class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! } extension CIFilter {     init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter     class func filterWithImageURL(_ url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter!     init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter     class func filterWithImageData(_ data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter! } extension CIFilter {     func apply(_ k: CIKernel!, args args: [AnyObject]!, options options: (NSCopying, AnyObject)...) -> CIImage     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIFilter : NSObject, NSSecureCoding, NSCoding, NSCopying {     var outputImage: CIImage? { get }     var name: String     var enabled: Bool     var inputKeys: [String] { get }     var outputKeys: [String] { get }     func setDefaults()     var attributes: [String : AnyObject] { get }     func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? } extension CIFilter {      init?(name name: String)     class func filterWithName(_ name: String) -> CIFilter?      init?(name name: String, withInputParameters params: [String : AnyObject]?)     class func filterWithName(_ name: String, withInputParameters params: [String : AnyObject]?) -> CIFilter?     class func filterNamesInCategory(_ category: String?) -> [String]     class func filterNamesInCategories(_ categories: [String]?) -> [String]     class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject])     class func localizedNameForFilterName(_ filterName: String) -> String?     class func localizedNameForCategory(_ category: String) -> String     class func localizedDescriptionForFilterName(_ filterName: String) -> String?     class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData     class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] } extension CIFilter {      init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!)     class func filterWithImageURL(_ url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter!      init!(imageData data: NSData!, options options: [NSObject : AnyObject]!)     class func filterWithImageData(_ data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter! } extension CIFilter {     func viewForUIConfiguration(_ inUIConfiguration: [NSObject : AnyObject]!, excludedKeys inKeys: [AnyObject]!) -> IKFilterUIView! } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIFilter.apply(_: CIKernel, arguments: [AnyObject]?, options: [String : AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cifilter/1438077-apply)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` func apply(_ k: CIKernel!, arguments args: [AnyObject]!, options dict: [NSObject : AnyObject]!) -> CIImage! ``` | OS X 10.10 | QuartzCore |
| To | ``` func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.enabled](https://developer.apple.com/documentation/coreimage/cifilter/1438276-isenabled)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.5 | CoreImage |

Modified [CIFilter.filterArrayFromSerializedXMP(_: NSData, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] ``` | CoreImage |

Modified [CIFilter.filterNamesInCategories(_: [String]?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterNamesInCategories(_ categories: [String]?) -> [String] ``` | CoreImage |

Modified [CIFilter.filterNamesInCategory(_: String?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterNamesInCategory(_ category: String!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterNamesInCategory(_ category: String?) -> [String] ``` | CoreImage |

Modified [CIFilter.init(imageData: NSData!, options: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/coreimage/cifilter/1437879-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) ``` | CoreImage |

Modified [CIFilter.init(imageURL: NSURL!, options: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/coreimage/cifilter/1438096-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) ``` | CoreImage |

Modified [CIFilter.init(name: String)](https://developer.apple.com/documentation/coreimage/cifilter/1438255-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(name name: String!) -> CIFilter ``` | QuartzCore |
| To | ``` init?(name name: String) ``` | CoreImage |

Modified [CIFilter.init(name: String, withInputParameters: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init?(name name: String, withInputParameters params: [String : AnyObject]?) ``` | CoreImage |

Modified [CIFilter.localizedDescriptionForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedDescriptionForFilterName(_ filterName: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedDescriptionForFilterName(_ filterName: String) -> String? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedNameForCategory(_: String) -> String [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438057-localizednameforcategory)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedNameForCategory(_ category: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedNameForCategory(_ category: String) -> String ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedNameForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437697-localizednameforfiltername)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedNameForFilterName(_ filterName: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedNameForFilterName(_ filterName: String) -> String? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedReferenceDocumentationForFilterName(_: String) -> NSURL? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedReferenceDocumentationForFilterName(_ filterName: String!) -> NSURL! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 | QuartzCore |
| To | ``` var name: String ``` | OS X 10.5 | CoreImage |

Modified [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var outputImage: CIImage! { get } ``` | QuartzCore |
| To | ``` var outputImage: CIImage? { get } ``` | CoreImage |

Modified [CIFilter.registerFilterName(_: String, constructor: CIFilterConstructor, classAttributes: [String : AnyObject]) [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func registerFilterName(_ name: String!, constructor anObject: CIFilterConstructor!, classAttributes attributes: [NSObject : AnyObject]!) ``` | OS X 10.10 | QuartzCore |
| To | ``` class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject]) ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.serializedXMPFromFilters(_: [CIFilter], inputImageExtent: CGRect) -> NSData [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData! ``` | QuartzCore |
| To | ``` class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData ``` | CoreImage |

Modified [CIFilter.setDefaults()](https://developer.apple.com/documentation/coreimage/cifilter/1437902-setdefaults)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` protocol CIFilterConstructor {     func filterWithName(_ name: String!) -> CIFilter! } ``` | QuartzCore |
| To | ``` protocol CIFilterConstructor {     func filterWithName(_ name: String) -> CIFilter? } ``` | CoreImage |

Modified [CIFilterConstructor.filterWithName(_: String) -> CIFilter?](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` func filterWithName(_ name: String!) -> CIFilter! ``` | OS X 10.10 | QuartzCore |
| To | ``` func filterWithName(_ name: String) -> CIFilter? ``` | OS X 10.4 | CoreImage |

Modified [CIFilterGenerator](https://developer.apple.com/documentation/coreimage/cifiltergenerator)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIFilterGenerator : NSObject, NSCoding, NSCopying, CIFilterConstructor {     init!() -> CIFilterGenerator     class func filterGenerator() -> CIFilterGenerator!     init!(contentsOfURL aURL: NSURL!) -> CIFilterGenerator     class func filterGeneratorWithContentsOfURL(_ aURL: NSURL!) -> CIFilterGenerator!     init!(contentsOfURL aURL: NSURL!)     func connectObject(_ sourceObject: AnyObject!, withKey sourceKey: String!, toObject targetObject: AnyObject!, withKey targetKey: String!)     func disconnectObject(_ sourceObject: AnyObject!, withKey key: String!, toObject targetObject: AnyObject!, withKey targetKey: String!)     func exportKey(_ key: String!, fromObject targetObject: AnyObject!, withName exportedKeyName: String!)     func removeExportedKey(_ exportedKeyName: String!)     func exportedKeys() -> [NSObject : AnyObject]!     func setAttributes(_ attributes: [NSObject : AnyObject]!, forExportedKey key: String!)     func classAttributes() -> [NSObject : AnyObject]!     func setClassAttributes(_ attributes: [NSObject : AnyObject]!)     func filter() -> CIFilter!     func registerFilterName(_ name: String!)     func writeToURL(_ aURL: NSURL!, atomically flag: Bool) -> Bool } ``` | AnyObject, CIFilterConstructor, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIFilterGenerator : NSObject, NSSecureCoding, NSCoding, NSCopying, CIFilterConstructor {      init()     class func filterGenerator() -> CIFilterGenerator      init?(contentsOfURL aURL: NSURL)     class func filterGeneratorWithContentsOfURL(_ aURL: NSURL) -> CIFilterGenerator?     init?(contentsOfURL aURL: NSURL)     func connectObject(_ sourceObject: AnyObject, withKey sourceKey: String?, toObject targetObject: AnyObject, withKey targetKey: String)     func disconnectObject(_ sourceObject: AnyObject, withKey key: String, toObject targetObject: AnyObject, withKey targetKey: String)     func exportKey(_ key: String, fromObject targetObject: AnyObject, withName exportedKeyName: String?)     func removeExportedKey(_ exportedKeyName: String)     var exportedKeys: [NSObject : AnyObject] { get }     func setAttributes(_ attributes: [NSObject : AnyObject], forExportedKey key: String)     var classAttributes: [NSObject : AnyObject]     func filter() -> CIFilter     func registerFilterName(_ name: String)     func writeToURL(_ aURL: NSURL, atomically flag: Bool) -> Bool } ``` | AnyObject, CIFilterConstructor, NSCoding, NSCopying, NSSecureCoding | OS X 10.5 | CoreImage |

Modified [CIFilterGenerator.connectObject(_: AnyObject, withKey: String?, toObject: AnyObject, withKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438159-connect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func connectObject(_ sourceObject: AnyObject!, withKey sourceKey: String!, toObject targetObject: AnyObject!, withKey targetKey: String!) ``` | QuartzCore |
| To | ``` func connectObject(_ sourceObject: AnyObject, withKey sourceKey: String?, toObject targetObject: AnyObject, withKey targetKey: String) ``` | CoreImage |

Modified [CIFilterGenerator.disconnectObject(_: AnyObject, withKey: String, toObject: AnyObject, withKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438075-disconnectobject)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func disconnectObject(_ sourceObject: AnyObject!, withKey key: String!, toObject targetObject: AnyObject!, withKey targetKey: String!) ``` | QuartzCore |
| To | ``` func disconnectObject(_ sourceObject: AnyObject, withKey key: String, toObject targetObject: AnyObject, withKey targetKey: String) ``` | CoreImage |

Modified [CIFilterGenerator.exportKey(_: String, fromObject: AnyObject, withName: String?)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438155-exportkey)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func exportKey(_ key: String!, fromObject targetObject: AnyObject!, withName exportedKeyName: String!) ``` | QuartzCore |
| To | ``` func exportKey(_ key: String, fromObject targetObject: AnyObject, withName exportedKeyName: String?) ``` | CoreImage |

Modified [CIFilterGenerator.filter() -> CIFilter](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438044-filter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func filter() -> CIFilter! ``` | QuartzCore |
| To | ``` func filter() -> CIFilter ``` | CoreImage |

Modified [CIFilterGenerator.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437742-initwithcontentsofurl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL aURL: NSURL!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL aURL: NSURL) ``` | CoreImage |

Modified [CIFilterGenerator.registerFilterName(_: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437891-registerfiltername)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func registerFilterName(_ name: String!) ``` | QuartzCore |
| To | ``` func registerFilterName(_ name: String) ``` | CoreImage |

Modified [CIFilterGenerator.removeExportedKey(_: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438191-removeexportedkey)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func removeExportedKey(_ exportedKeyName: String!) ``` | QuartzCore |
| To | ``` func removeExportedKey(_ exportedKeyName: String) ``` | CoreImage |

Modified [CIFilterGenerator.setAttributes(_: [NSObject : AnyObject], forExportedKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438069-setattributes)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setAttributes(_ attributes: [NSObject : AnyObject]!, forExportedKey key: String!) ``` | QuartzCore |
| To | ``` func setAttributes(_ attributes: [NSObject : AnyObject], forExportedKey key: String) ``` | CoreImage |

Modified [CIFilterGenerator.writeToURL(_: NSURL, atomically: Bool) -> Bool](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438179-write)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func writeToURL(_ aURL: NSURL!, atomically flag: Bool) -> Bool ``` | QuartzCore |
| To | ``` func writeToURL(_ aURL: NSURL, atomically flag: Bool) -> Bool ``` | CoreImage |

Modified [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIFilterShape : NSObject, NSCopying {     class func shapeWithRect(_ r: CGRect) -> AnyObject!     init!(rect r: CGRect)     func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape!     func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape!     func unionWith(_ s2: CIFilterShape!) -> CIFilterShape!     func unionWithRect(_ r: CGRect) -> CIFilterShape!     func intersectWith(_ s2: CIFilterShape!) -> CIFilterShape!     func intersectWithRect(_ r: CGRect) -> CIFilterShape! } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIFilterShape : NSObject, NSCopying {     convenience init(rect r: CGRect)     class func shapeWithRect(_ r: CGRect) -> Self     init(rect r: CGRect)     func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape     func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape     func unionWith(_ s2: CIFilterShape) -> CIFilterShape     func unionWithRect(_ r: CGRect) -> CIFilterShape     func intersectWith(_ s2: CIFilterShape) -> CIFilterShape     func intersectWithRect(_ r: CGRect) -> CIFilterShape     var extent: CGRect { get } } ``` | OS X 10.4 | CoreImage |

Modified [CIFilterShape.init(rect: CGRect)](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(rect r: CGRect) ``` | QuartzCore |
| To | ``` init(rect r: CGRect) ``` | CoreImage |

Modified [CIFilterShape.insetByX(_: Int32, y: Int32) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetby)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.intersectWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func intersectWith(_ s2: CIFilterShape!) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func intersectWith(_ s2: CIFilterShape) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.intersectWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437806-intersect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func intersectWithRect(_ r: CGRect) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func intersectWithRect(_ r: CGRect) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.transformBy(_: CGAffineTransform, interior: Bool) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437808-transformby)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.unionWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1438227-unionwith)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func unionWith(_ s2: CIFilterShape!) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func unionWith(_ s2: CIFilterShape) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.unionWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437601-unionwithrect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func unionWithRect(_ r: CGRect) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func unionWithRect(_ r: CGRect) -> CIFilterShape ``` | CoreImage |

Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIImage : NSObject, NSCoding, NSCopying {     init!(CGImage image: CGImage!) -> CIImage     class func imageWithCGImage(_ image: CGImage!) -> CIImage!     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGImage(_ image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CGLayer layer: CGLayer!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!) -> CIImage!     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithBitmapData(_ d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage!     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage!     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) -> CIImage     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) -> CIImage!     init!(contentsOfURL url: NSURL!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!) -> CIImage!     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(data data: NSData!) -> CIImage     class func imageWithData(_ data: NSData!) -> CIImage!     init!(data data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithData(_ data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(IOSurface surface: IOSurface!) -> CIImage     class func imageWithIOSurface(_ surface: IOSurface!) -> CIImage!     init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithIOSurface(_ surface: IOSurface!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(color color: CIColor!) -> CIImage     class func imageWithColor(_ color: CIColor!) -> CIImage!     class func emptyImage() -> CIImage!     init!(CGImage image: CGImage!)     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!)     init!(CGLayer layer: CGLayer!)     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!)     init!(data data: NSData!)     init!(data data: NSData!, options d: [NSObject : AnyObject]!)     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!)     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!)     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!)     init!(contentsOfURL url: NSURL!)     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!)     init!(IOSurface surface: IOSurface!)     init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!)     init!(IOSurface surface: IOSurface!, plane plane: Int, format format: CIFormat, options d: [NSObject : AnyObject]!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!)     init!(CVPixelBuffer buffer: CVPixelBuffer!)     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!)     init!(color color: CIColor!)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage!     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage!     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage!     func imageByCroppingToRect(_ r: CGRect) -> CIImage!     func imageByClampingToExtent() -> CIImage!     func extent() -> CGRect     func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage!     func properties() -> [NSObject : AnyObject]!     func definition() -> CIFilterShape!     func url() -> NSURL!     func colorSpace() -> Unmanaged<CGColorSpace>! } extension CIImage {     init?(bitmapImageRep bitmapImageRep: NSBitmapImageRep)     func drawInRect(_ rect: NSRect, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)     func drawAtPoint(_ point: NSPoint, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat) } extension CIImage {     func autoAdjustmentFilters() -> [AnyObject]!     func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! } extension CIImage {     init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithImageProvider(_ p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIImage : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(CGImage image: CGImage)     class func imageWithCGImage(_ image: CGImage) -> CIImage      init(CGImage image: CGImage, options options: [String : AnyObject]?)     class func imageWithCGImage(_ image: CGImage, options options: [String : AnyObject]?) -> CIImage      init(CGLayer layer: CGLayer)     class func imageWithCGLayer(_ layer: CGLayer) -> CIImage      init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     class func imageWithCGLayer(_ layer: CGLayer, options options: [String : AnyObject]?) -> CIImage      init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     class func imageWithBitmapData(_ data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) -> CIImage      init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     class func imageWithMTLTexture(_ texture: MTLTexture, options options: [String : AnyObject]?) -> CIImage      init?(contentsOfURL url: NSURL)     class func imageWithContentsOfURL(_ url: NSURL) -> CIImage?      init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     class func imageWithContentsOfURL(_ url: NSURL, options options: [String : AnyObject]?) -> CIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> CIImage?      init?(data data: NSData, options options: [String : AnyObject]?)     class func imageWithData(_ data: NSData, options options: [String : AnyObject]?) -> CIImage?      init(CVImageBuffer imageBuffer: CVImageBuffer)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer) -> CIImage      init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) -> CIImage      init(IOSurface surface: IOSurface)     class func imageWithIOSurface(_ surface: IOSurface) -> CIImage      init(IOSurface surface: IOSurface, options options: [String : AnyObject]?)     class func imageWithIOSurface(_ surface: IOSurface, options options: [String : AnyObject]?) -> CIImage      init(color color: CIColor)     class func imageWithColor(_ color: CIColor) -> CIImage     class func emptyImage() -> CIImage     init(CGImage image: CGImage)     init(CGImage image: CGImage, options options: [String : AnyObject]?)     init(CGLayer layer: CGLayer)     init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     init?(data data: NSData)     init?(data data: NSData, options options: [String : AnyObject]?)     init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     init?(contentsOfURL url: NSURL)     init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     init(IOSurface surface: IOSurface)     init(IOSurface surface: IOSurface, options options: [String : AnyObject]?)     init(IOSurface surface: IOSurface, plane plane: Int, format format: CIFormat, options options: [String : AnyObject]?)     init(CVImageBuffer imageBuffer: CVImageBuffer)     init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     init(color color: CIColor)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage) -> CIImage     func imageByCroppingToRect(_ rect: CGRect) -> CIImage     func imageByClampingToExtent() -> CIImage     func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage     var extent: CGRect { get }     var properties: [String : AnyObject] { get }     var definition: CIFilterShape { get }     var url: NSURL? { get }     var colorSpace: CGColorSpace? { get }     func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect } extension CIImage {     init?(bitmapImageRep bitmapImageRep: NSBitmapImageRep)     func drawInRect(_ rect: NSRect, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)     func drawAtPoint(_ point: NSPoint, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat) } extension CIImage {     func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] } extension CIImage {      init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?)     class func imageWithImageProvider(_ p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) -> CIImage     init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIImage.autoAdjustmentFiltersWithOptions(_: [String : AnyObject]?) -> [CIFilter]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilterswithoptions)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] ``` | CoreImage |

Modified [CIImage.emptyImage() -> CIImage [class]](https://developer.apple.com/documentation/coreimage/ciimage/1438023-emptyimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func emptyImage() -> CIImage! ``` | QuartzCore |
| To | ``` class func emptyImage() -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingFilter(_: String, withInputParameters: [String : AnyObject]?) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437589-imagebyapplyingfilter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingOrientation(_: Int32) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438223-oriented)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingTransform(_: CGAffineTransform) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438203-imagebyapplyingtransform)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByClampingToExtent() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437628-imagebyclampingtoextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByClampingToExtent() -> CIImage! ``` | QuartzCore |
| To | ``` func imageByClampingToExtent() -> CIImage ``` | CoreImage |

Modified [CIImage.imageByCompositingOverImage(_: CIImage) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437837-imagebycompositingoverimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByCompositingOverImage(_ dest: CIImage) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByCroppingToRect(_: CGRect) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437833-cropped)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByCroppingToRect(_ r: CGRect) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByCroppingToRect(_ rect: CGRect) -> CIImage ``` | CoreImage |

Modified [CIImage.imageTransformForOrientation(_: Int32) -> CGAffineTransform](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIImage.init(bitmapData: NSData, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIImage.init(CGImage: CGImage)](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGImage image: CGImage!) ``` | QuartzCore |
| To | ``` init(CGImage image: CGImage) ``` | CoreImage |

Modified [CIImage.init(CGImage: CGImage, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(CGImage image: CGImage, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(CGLayer: CGLayer)](https://developer.apple.com/documentation/coreimage/ciimage/1438065-initwithcglayer)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGLayer layer: CGLayer!) ``` | -- | QuartzCore |
| To | ``` init(CGLayer layer: CGLayer) ``` | OS X 10.11 | CoreImage |

Modified [CIImage.init(CGLayer: CGLayer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437687-initwithcglayer)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) ``` | -- | QuartzCore |
| To | ``` init(CGLayer layer: CGLayer, options options: [String : AnyObject]?) ``` | OS X 10.11 | CoreImage |

Modified [CIImage.init(color: CIColor)](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(color color: CIColor!) ``` | QuartzCore |
| To | ``` init(color color: CIColor) ``` | CoreImage |

Modified [CIImage.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL url: NSURL) ``` | CoreImage |

Modified [CIImage.init(contentsOfURL: NSURL, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437867-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(CVImageBuffer: CVImageBuffer)](https://developer.apple.com/documentation/coreimage/ciimage/1438012-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!) ``` | QuartzCore |
| To | ``` init(CVImageBuffer imageBuffer: CVImageBuffer) ``` | CoreImage |

Modified [CIImage.init(CVImageBuffer: CVImageBuffer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437617-initwithcvimagebuffer)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(data: NSData)](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(data data: NSData!) ``` | QuartzCore |
| To | ``` init?(data data: NSData) ``` | CoreImage |

Modified [CIImage.init(data: NSData, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438032-initwithdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(data data: NSData!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init?(data data: NSData, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(imageProvider: AnyObject, size: Int, _: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.10 | QuartzCore |
| To | ``` init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) ``` | OS X 10.4 | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface)](https://developer.apple.com/documentation/coreimage/ciimage/1438030-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!) ``` | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface) ``` | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438181-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface, plane: Int, format: CIFormat, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437670-init)

|  | Declaration | Introduction | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!, plane plane: Int, format format: CIFormat, options d: [NSObject : AnyObject]!) ``` | OS X 10.10 | -- | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface, plane plane: Int, format format: CIFormat, options options: [String : AnyObject]?) ``` | OS X 10.9 | OS X 10.11 | CoreImage |

Modified [CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1438015-initwithtexture)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437880-initwithtexture)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIImageAccumulator : NSObject {     init!(extent extent: CGRect, format format: CIFormat) -> CIImageAccumulator     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat) -> CIImageAccumulator!     init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) -> CIImageAccumulator     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) -> CIImageAccumulator!     init!(extent extent: CGRect, format format: CIFormat)     init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!)     func extent() -> CGRect     func format() -> CIFormat     func image() -> CIImage!     func setImage(_ im: CIImage!)     func setImage(_ im: CIImage!, dirtyRect r: CGRect)     func clear() } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIImageAccumulator : NSObject {     convenience init(extent extent: CGRect, format format: CIFormat)     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat) -> Self     convenience init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace)     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace) -> Self     init(extent extent: CGRect, format format: CIFormat)     init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace)     var extent: CGRect { get }     var format: CIFormat { get }     func image() -> CIImage     func setImage(_ image: CIImage)     func setImage(_ image: CIImage, dirtyRect dirtyRect: CGRect)     func clear() } ``` | OS X 10.4 | CoreImage |

Modified [CIImageAccumulator.clear()](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427720-clear)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIImageAccumulator.image() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427704-image)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func image() -> CIImage! ``` | QuartzCore |
| To | ``` func image() -> CIImage ``` | CoreImage |

Modified [CIImageAccumulator.init(extent: CGRect, format: CIFormat)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-initwithextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(extent extent: CGRect, format format: CIFormat) ``` | QuartzCore |
| To | ``` init(extent extent: CGRect, format format: CIFormat) ``` | CoreImage |

Modified [CIImageAccumulator.init(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-initwithextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace) ``` | CoreImage |

Modified [CIImageAccumulator.setImage(_: CIImage)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427702-setimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setImage(_ im: CIImage!) ``` | QuartzCore |
| To | ``` func setImage(_ image: CIImage) ``` | CoreImage |

Modified [CIImageAccumulator.setImage(_: CIImage, dirtyRect: CGRect)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setImage(_ im: CIImage!, dirtyRect r: CGRect) ``` | QuartzCore |
| To | ``` func setImage(_ image: CIImage, dirtyRect dirtyRect: CGRect) ``` | CoreImage |

Modified [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIKernel : NSObject {     class func kernelsWithString(_ s: String!) -> [AnyObject]!     init!(string s: String!) -> CIKernel     class func kernelWithString(_ s: String!) -> CIKernel!     func name() -> String!     func setROISelector(_ aMethod: Selector) } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIKernel : NSObject {     class func kernelsWithString(_ string: String) -> [CIKernel]?     convenience init?(string string: String)     class func kernelWithString(_ string: String) -> Self?     var name: String { get }     func setROISelector(_ method: Selector)     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, arguments args: [AnyObject]?) -> CIImage? } ``` | OS X 10.4 | CoreImage |

Modified [CIKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string s: String!) -> CIKernel ``` | QuartzCore |
| To | ``` convenience init?(string string: String) ``` | CoreImage |

Modified [CIKernel.kernelsWithString(_: String) -> [CIKernel]? [class]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func kernelsWithString(_ s: String!) -> [AnyObject]! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func kernelsWithString(_ string: String) -> [CIKernel]? ``` | OS X 10.4 | CoreImage |

Modified [CIKernel.setROISelector(_: Selector)](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIPlugIn](https://developer.apple.com/documentation/coreimage/ciplugin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIPlugIn.loadAllPlugIns() [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1437653-loadallplugins)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugIn.loadNonExecutablePlugIns() [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1437599-loadnonexecutableplugins)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugIn.loadPlugIn(_: NSURL!, allowExecutableCode: Bool) [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1438187-loadplugin)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugInRegistration](https://developer.apple.com/documentation/coreimage/cipluginregistration)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugInRegistration.load(_: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/coreimage/cipluginregistration/1437823-load)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String! { get } } ``` | QuartzCore |
| To | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String { get } } ``` | CoreImage |

Modified [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var messageString: String! { get } ``` | QuartzCore |
| To | ``` var messageString: String { get } ``` | CoreImage |

Modified [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CISampler : NSObject, NSCopying {     init!(image im: CIImage!) -> CISampler     class func samplerWithImage(_ im: CIImage!) -> CISampler!     init!(image im: CIImage!, options dict: [NSObject : AnyObject]!) -> CISampler     class func samplerWithImage(_ im: CIImage!, options dict: [NSObject : AnyObject]!) -> CISampler!     init!(image im: CIImage!)     init!(image im: CIImage!, options dict: [NSObject : AnyObject]!)     func definition() -> CIFilterShape!     func extent() -> CGRect } extension CISampler {     convenience init(im im: CIImage!, elements elements: (NSCopying, AnyObject)...) } extension CISampler {     convenience init(im im: CIImage!, elements elements: (NSCopying, AnyObject)...) } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CISampler : NSObject, NSCopying {     convenience init(image im: CIImage)     class func samplerWithImage(_ im: CIImage) -> Self     convenience init(image im: CIImage, options dict: [NSObject : AnyObject]?)     class func samplerWithImage(_ im: CIImage, options dict: [NSObject : AnyObject]?) -> Self     convenience init(image im: CIImage)     init(image im: CIImage, options dict: [NSObject : AnyObject]?)     var definition: CIFilterShape { get }     var extent: CGRect { get } } ``` | OS X 10.4 | CoreImage |

Modified [CISampler.init(image: CIImage)](https://developer.apple.com/documentation/coreimage/cisampler/1438117-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(image im: CIImage!) ``` | QuartzCore |
| To | ``` convenience init(image im: CIImage) ``` | CoreImage |

Modified [CISampler.init(image: CIImage, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cisampler/1437963-initwithimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(image im: CIImage!, options dict: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(image im: CIImage, options dict: [NSObject : AnyObject]?) ``` | CoreImage |

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIVector : NSObject, NSCopying, NSCoding {     init!(values values: UnsafePointer<CGFloat>, count count: Int) -> CIVector     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> CIVector!     init!(x x: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector!     init!(CGPoint p: CGPoint) -> CIVector     class func vectorWithCGPoint(_ p: CGPoint) -> CIVector!     init!(CGRect r: CGRect) -> CIVector     class func vectorWithCGRect(_ r: CGRect) -> CIVector!     init!(CGAffineTransform t: CGAffineTransform) -> CIVector     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> CIVector!     init!(string representation: String!) -> CIVector     class func vectorWithString(_ representation: String!) -> CIVector!     init!(values values: UnsafePointer<CGFloat>, count count: Int)     init!(x x: CGFloat)     init!(x x: CGFloat, y y: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     init!(CGPoint p: CGPoint)     init!(CGRect r: CGRect)     init!(CGAffineTransform r: CGAffineTransform)     init!(string representation: String!)     func valueAtIndex(_ index: Int) -> CGFloat     func count() -> Int     func X() -> CGFloat     func Y() -> CGFloat     func Z() -> CGFloat     func W() -> CGFloat     func CGPointValue() -> CGPoint     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func stringRepresentation() -> String! } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIVector : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(values values: UnsafePointer<CGFloat>, count count: Int)     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> Self     convenience init(x x: CGFloat)     class func vectorWithX(_ x: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> Self     convenience init(CGPoint p: CGPoint)     class func vectorWithCGPoint(_ p: CGPoint) -> Self     convenience init(CGRect r: CGRect)     class func vectorWithCGRect(_ r: CGRect) -> Self     convenience init(CGAffineTransform t: CGAffineTransform)     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> Self     convenience init(string representation: String)     class func vectorWithString(_ representation: String) -> Self     init(values values: UnsafePointer<CGFloat>, count count: Int)     convenience init(x x: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     convenience init(CGPoint p: CGPoint)     convenience init(CGRect r: CGRect)     convenience init(CGAffineTransform r: CGAffineTransform)     convenience init(string representation: String)     func valueAtIndex(_ index: Int) -> CGFloat     var count: Int { get }     var X: CGFloat { get }     var Y: CGFloat { get }     var Z: CGFloat { get }     var W: CGFloat { get }     var CGPointValue: CGPoint { get }     var CGRectValue: CGRect { get }     var CGAffineTransformValue: CGAffineTransform { get }     var stringRepresentation: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIVector.init(CGAffineTransform: CGAffineTransform)](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGAffineTransform r: CGAffineTransform) ``` | QuartzCore |
| To | ``` convenience init(CGAffineTransform r: CGAffineTransform) ``` | CoreImage |

Modified [CIVector.init(CGPoint: CGPoint)](https://developer.apple.com/documentation/coreimage/civector/1438133-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGPoint p: CGPoint) ``` | QuartzCore |
| To | ``` convenience init(CGPoint p: CGPoint) ``` | CoreImage |

Modified [CIVector.init(CGRect: CGRect)](https://developer.apple.com/documentation/coreimage/civector/1437644-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGRect r: CGRect) ``` | QuartzCore |
| To | ``` convenience init(CGRect r: CGRect) ``` | CoreImage |

Modified [CIVector.init(string: String)](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string representation: String!) ``` | QuartzCore |
| To | ``` convenience init(string representation: String) ``` | CoreImage |

Modified [CIVector.init(values: UnsafePointer<CGFloat>, count: Int)](https://developer.apple.com/documentation/coreimage/civector/1437849-initwithvalues)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(values values: UnsafePointer<CGFloat>, count count: Int) ``` | QuartzCore |
| To | ``` init(values values: UnsafePointer<CGFloat>, count count: Int) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437657-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437865-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438088-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` | CoreImage |

Modified [CIVector.valueAtIndex(_: Int) -> CGFloat](https://developer.apple.com/documentation/coreimage/civector/1438207-value)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [NSObject.provideImageData(_: UnsafeMutablePointer<Void>, bytesPerRow: Int, origin: Int, _: Int, size: Int, _: Int, userInfo: AnyObject?)](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject!) ``` | QuartzCore |
| To | ``` func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject?) ``` | CoreImage |

Modified [CIDetectorAccuracy](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAccuracyHigh](https://developer.apple.com/documentation/coreimage/cidetectoraccuracyhigh)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAccuracyLow](https://developer.apple.com/documentation/coreimage/cidetectoraccuracylow)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAspectRatio](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorEyeBlink](https://developer.apple.com/documentation/coreimage/cidetectoreyeblink)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorFocalLength](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorImageOrientation](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorMinFeatureSize](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorSmile](https://developer.apple.com/documentation/coreimage/cidetectorsmile)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTracking](https://developer.apple.com/documentation/coreimage/cidetectortracking)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeFace](https://developer.apple.com/documentation/coreimage/cidetectortypeface)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeQRCode](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeRectangle](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeatureTypeFace](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFormat](https://developer.apple.com/documentation/coreimage/ciformat)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIActiveKeys](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438129-activekeys)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionColorSpace](https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionDefinition](https://developer.apple.com/documentation/coreimage/kciapplyoptiondefinition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionExtent](https://developer.apple.com/documentation/coreimage/kciapplyoptionextent)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionUserInfo](https://developer.apple.com/documentation/coreimage/kciapplyoptionuserinfo)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeClass](https://developer.apple.com/documentation/coreimage/kciattributeclass)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeDefault](https://developer.apple.com/documentation/coreimage/kciattributedefault)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeDescription](https://developer.apple.com/documentation/coreimage/kciattributedescription)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeDisplayName](https://developer.apple.com/documentation/coreimage/kciattributedisplayname)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterCategories](https://developer.apple.com/documentation/coreimage/kciattributefiltercategories)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterDisplayName](https://developer.apple.com/documentation/coreimage/kciattributefilterdisplayname)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterName](https://developer.apple.com/documentation/coreimage/kciattributefiltername)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeIdentity](https://developer.apple.com/documentation/coreimage/kciattributeidentity)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeMax](https://developer.apple.com/documentation/coreimage/kciattributemax)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeMin](https://developer.apple.com/documentation/coreimage/kciattributemin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeName](https://developer.apple.com/documentation/coreimage/kciattributename)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeReferenceDocumentation](https://developer.apple.com/documentation/coreimage/kciattributereferencedocumentation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeSliderMax](https://developer.apple.com/documentation/coreimage/kciattributeslidermax)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeSliderMin](https://developer.apple.com/documentation/coreimage/kciattributeslidermin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeType](https://developer.apple.com/documentation/coreimage/kciattributetype)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeAngle](https://developer.apple.com/documentation/coreimage/kciattributetypeangle)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeBoolean](https://developer.apple.com/documentation/coreimage/kciattributetypeboolean)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeCount](https://developer.apple.com/documentation/coreimage/kciattributetypecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeDistance](https://developer.apple.com/documentation/coreimage/kciattributetypedistance)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeGradient](https://developer.apple.com/documentation/coreimage/kciattributetypegradient)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeInteger](https://developer.apple.com/documentation/coreimage/kciattributetypeinteger)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeOffset](https://developer.apple.com/documentation/coreimage/kciattributetypeoffset)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeOpaqueColor](https://developer.apple.com/documentation/coreimage/kciattributetypeopaquecolor)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypePosition](https://developer.apple.com/documentation/coreimage/kciattributetypeposition)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypePosition3](https://developer.apple.com/documentation/coreimage/kciattributetypeposition3)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeRectangle](https://developer.apple.com/documentation/coreimage/kciattributetyperectangle)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeScalar](https://developer.apple.com/documentation/coreimage/kciattributetypescalar)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeTime](https://developer.apple.com/documentation/coreimage/kciattributetypetime)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryBlur](https://developer.apple.com/documentation/coreimage/kcicategoryblur)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryBuiltIn](https://developer.apple.com/documentation/coreimage/kcicategorybuiltin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryColorAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorycoloradjustment)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryColorEffect](https://developer.apple.com/documentation/coreimage/kcicategorycoloreffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryCompositeOperation](https://developer.apple.com/documentation/coreimage/kcicategorycompositeoperation)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryDistortionEffect](https://developer.apple.com/documentation/coreimage/kcicategorydistortioneffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryFilterGenerator](https://developer.apple.com/documentation/coreimage/kcicategoryfiltergenerator)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCICategoryGenerator](https://developer.apple.com/documentation/coreimage/kcicategorygenerator)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryGeometryAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorygeometryadjustment)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryGradient](https://developer.apple.com/documentation/coreimage/kcicategorygradient)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryHalftoneEffect](https://developer.apple.com/documentation/coreimage/kcicategoryhalftoneeffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryHighDynamicRange](https://developer.apple.com/documentation/coreimage/kcicategoryhighdynamicrange)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryInterlaced](https://developer.apple.com/documentation/coreimage/kcicategoryinterlaced)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryNonSquarePixels](https://developer.apple.com/documentation/coreimage/kcicategorynonsquarepixels)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryReduction](https://developer.apple.com/documentation/coreimage/kcicategoryreduction)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCICategorySharpen](https://developer.apple.com/documentation/coreimage/kcicategorysharpen)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryStillImage](https://developer.apple.com/documentation/coreimage/kcicategorystillimage)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryStylize](https://developer.apple.com/documentation/coreimage/kcicategorystylize)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryTileEffect](https://developer.apple.com/documentation/coreimage/kcicategorytileeffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryTransition](https://developer.apple.com/documentation/coreimage/kcicategorytransition)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryVideo](https://developer.apple.com/documentation/coreimage/kcicategoryvideo)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextOutputColorSpace](https://developer.apple.com/documentation/coreimage/cicontextoption/1438052-outputcolorspace)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextUseSoftwareRenderer](https://developer.apple.com/documentation/coreimage/cicontextoption/1438047-usesoftwarerenderer)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextWorkingColorSpace](https://developer.apple.com/documentation/coreimage/kcicontextworkingcolorspace)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIFilterGeneratorExportedKey](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFilterGeneratorExportedKeyName](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeyname)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFilterGeneratorExportedKeyTargetObject](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeytargetobject)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatARGB8](https://developer.apple.com/documentation/coreimage/kciformatargb8)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBA16](https://developer.apple.com/documentation/coreimage/kciformatrgba16)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBAf](https://developer.apple.com/documentation/coreimage/kciformatrgbaf)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBAh](https://developer.apple.com/documentation/coreimage/kciformatrgbah)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustCrop](https://developer.apple.com/documentation/coreimage/kciimageautoadjustcrop)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustEnhance](https://developer.apple.com/documentation/coreimage/kciimageautoadjustenhance)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustFeatures](https://developer.apple.com/documentation/coreimage/kciimageautoadjustfeatures)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustLevel](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438040-level)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustRedEye](https://developer.apple.com/documentation/coreimage/kciimageautoadjustredeye)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageColorSpace](https://developer.apple.com/documentation/coreimage/ciimageoption/1438131-colorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProperties](https://developer.apple.com/documentation/coreimage/ciimageoption/1437679-properties)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProviderTileSize](https://developer.apple.com/documentation/coreimage/kciimageprovidertilesize)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProviderUserInfo](https://developer.apple.com/documentation/coreimage/kciimageprovideruserinfo)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageTextureFormat](https://developer.apple.com/documentation/coreimage/ciimageoption/1437934-textureformat)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageTextureTarget](https://developer.apple.com/documentation/coreimage/kciimagetexturetarget)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAllowDraftModeKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438010-allowdraftmode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAngleKey](https://developer.apple.com/documentation/coreimage/kciinputanglekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAspectRatioKey](https://developer.apple.com/documentation/coreimage/kciinputaspectratiokey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBackgroundImageKey](https://developer.apple.com/documentation/coreimage/kciinputbackgroundimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBiasKey](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBoostKey](https://developer.apple.com/documentation/coreimage/kciinputboostkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBoostShadowAmountKey](https://developer.apple.com/documentation/coreimage/kciinputboostshadowamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBrightnessKey](https://developer.apple.com/documentation/coreimage/kciinputbrightnesskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputCenterKey](https://developer.apple.com/documentation/coreimage/kciinputcenterkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputColorKey](https://developer.apple.com/documentation/coreimage/kciinputcolorkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputColorNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputcolornoisereductionamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputContrastKey](https://developer.apple.com/documentation/coreimage/kciinputcontrastkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputDecoderVersionKey](https://developer.apple.com/documentation/coreimage/kciinputdecoderversionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableChromaticNoiseTrackingKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438231-enablechromaticnoisetracking)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableSharpeningKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438016-enablesharpening)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableVendorLensCorrectionKey](https://developer.apple.com/documentation/coreimage/kciinputenablevendorlenscorrectionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEVKey](https://developer.apple.com/documentation/coreimage/kciinputevkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputExtentKey](https://developer.apple.com/documentation/coreimage/kciinputextentkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputGradientImageKey](https://developer.apple.com/documentation/coreimage/kciinputgradientimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputIgnoreImageOrientationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437949-ignoreimageorientation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputImageKey](https://developer.apple.com/documentation/coreimage/kciinputimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputImageOrientationKey](https://developer.apple.com/documentation/coreimage/kciinputimageorientationkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputIntensityKey](https://developer.apple.com/documentation/coreimage/kciinputintensitykey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputLinearSpaceFilter](https://developer.apple.com/documentation/coreimage/kciinputlinearspacefilter)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputLuminanceNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputluminancenoisereductionamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputMaskImageKey](https://developer.apple.com/documentation/coreimage/kciinputmaskimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralChromaticityXKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437605-neutralchromaticityx)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralChromaticityYKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438039-neutralchromaticityy)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralLocationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437915-neutrallocation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralTemperatureKey](https://developer.apple.com/documentation/coreimage/kciinputneutraltemperaturekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralTintKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438113-neutraltint)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437990-noisereductionamount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionContrastAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductioncontrastamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionDetailAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductiondetailamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionSharpnessAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438009-noisereductionsharpnessamount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputRadiusKey](https://developer.apple.com/documentation/coreimage/kciinputradiuskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputRefractionKey](https://developer.apple.com/documentation/coreimage/kciinputrefractionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputSaturationKey](https://developer.apple.com/documentation/coreimage/kciinputsaturationkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputScaleFactorKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437936-scalefactor)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputScaleKey](https://developer.apple.com/documentation/coreimage/kciinputscalekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputShadingImageKey](https://developer.apple.com/documentation/coreimage/kciinputshadingimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputSharpnessKey](https://developer.apple.com/documentation/coreimage/kciinputsharpnesskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTargetImageKey](https://developer.apple.com/documentation/coreimage/kciinputtargetimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTimeKey](https://developer.apple.com/documentation/coreimage/kciinputtimekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTransformKey](https://developer.apple.com/documentation/coreimage/kciinputtransformkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputWidthKey](https://developer.apple.com/documentation/coreimage/kciinputwidthkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIOutputImageKey](https://developer.apple.com/documentation/coreimage/kcioutputimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIOutputNativeSizeKey](https://developer.apple.com/documentation/coreimage/kcioutputnativesizekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerAffineMatrix](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterLinear](https://developer.apple.com/documentation/coreimage/kcisamplerfilterlinear)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterMode](https://developer.apple.com/documentation/coreimage/kcisamplerfiltermode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterNearest](https://developer.apple.com/documentation/coreimage/kcisamplerfilternearest)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [kCISamplerWrapBlack](https://developer.apple.com/documentation/coreimage/kcisamplerwrapblack)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [kCISamplerWrapClamp](https://developer.apple.com/documentation/coreimage/kcisamplerwrapclamp)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerWrapMode](https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISupportedDecoderVersionsKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437927-supporteddecoderversions)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUIParameterSet](https://developer.apple.com/documentation/coreimage/kciuiparameterset)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetAdvanced](https://developer.apple.com/documentation/coreimage/kciuisetadvanced)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetBasic](https://developer.apple.com/documentation/coreimage/kciuisetbasic)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetDevelopment](https://developer.apple.com/documentation/coreimage/kciuisetdevelopment)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetIntermediate](https://developer.apple.com/documentation/coreimage/kciuisetintermediate)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

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
