---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreImage.html
archived_at: '2026-07-18T02:56:45.326276Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreImage Changes for Swift

### CoreImage

Removed CIColor.alpha() -> CGFloatRemoved CIColor.blue() -> CGFloatRemoved CIColor.colorSpace() -> Unmanaged<CGColorSpace>!Removed CIColor.components() -> UnsafePointer<CGFloat>Removed CIColor.green() -> CGFloatRemoved CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CIColorRemoved CIColor.numberOfComponents() -> IntRemoved CIColor.red() -> CGFloatRemoved CIColor.stringRepresentation() -> String!Removed CIFilter.attributes() -> [NSObject : AnyObject]!Removed CIFilter.init(name: String!, elements: (NSCopying, AnyObject))Removed CIFilter.inputKeys() -> [AnyObject]!Removed CIFilter.name() -> String!Removed CIFilter.outputKeys() -> [AnyObject]!Removed [CIImage.autoAdjustmentFilters() -> [AnyObject]!](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Removed CIImage.extent() -> CGRectRemoved CIImage.properties() -> [NSObject : AnyObject]!Removed CIKernel.name() -> String!Removed CIVector.CGAffineTransformValue() -> CGAffineTransformRemoved CIVector.CGPointValue() -> CGPointRemoved CIVector.CGRectValue() -> CGRectRemoved CIVector.count() -> IntRemoved CIVector.stringRepresentation() -> String!Removed CIVector.W() -> CGFloatRemoved CIVector.X() -> CGFloatRemoved CIVector.Y() -> CGFloatRemoved CIVector.Z() -> CGFloatAdded [CIColor.alpha](https://developer.apple.com/documentation/coreimage/cicolor/1437981-alpha)Added [CIColor.blue](https://developer.apple.com/documentation/coreimage/cicolor/1438033-blue)Added [CIColor.colorSpace](https://developer.apple.com/documentation/coreimage/cicolor/1437917-colorspace)Added [CIColor.components](https://developer.apple.com/documentation/coreimage/cicolor/1437862-components)Added [CIColor.green](https://developer.apple.com/documentation/coreimage/cicolor/1437607-green)Added [CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coreimage/cicolor/1438084-init)Added [CIColor.numberOfComponents](https://developer.apple.com/documentation/coreimage/cicolor/1438151-numberofcomponents)Added [CIColor.red](https://developer.apple.com/documentation/coreimage/cicolor/1437969-red)Added [CIColor.stringRepresentation](https://developer.apple.com/documentation/coreimage/cicolor/1437910-stringrepresentation)Added [CIColorKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438143-init)Added [CIContext.init(CGContext: CGContext, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1437864-contextwithcgcontext)Added [CIContext.init(MTLDevice: MTLDevice)](https://developer.apple.com/documentation/coreimage/cicontext/1437609-contextwithmtldevice)Added [CIContext.init(MTLDevice: MTLDevice, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1437711-contextwithmtldevice)Added [CIContext.render(_: CIImage, toMTLTexture: MTLTexture, commandBuffer: MTLCommandBuffer?, bounds: CGRect, colorSpace: CGColorSpace)](https://developer.apple.com/documentation/coreimage/cicontext/1438026-render)Added [CIContext.workingColorSpace](https://developer.apple.com/documentation/coreimage/cicontext/1438061-workingcolorspace)Added [CIFilter.attributes](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes)Added [CIFilter.inputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438013-inputkeys)Added [CIFilter.localizedDescriptionForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)Added [CIFilter.localizedNameForCategory(_: String) -> String [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438057-localizednameforcategory)Added [CIFilter.localizedNameForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437697-localizednameforfiltername)Added [CIFilter.localizedReferenceDocumentationForFilterName(_: String) -> NSURL? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)Added [CIFilter.name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)Added [CIFilter.outputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438122-outputkeys)Added [CIFilter.registerFilterName(_: String, constructor: CIFilterConstructor, classAttributes: [String : AnyObject]) [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)Added [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)Added [CIFilterConstructor.filterWithName(_: String) -> CIFilter?](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)Added [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)Added [CIFilterShape.extent](https://developer.apple.com/documentation/coreimage/cifiltershape/1438022-extent)Added [CIFilterShape.init(rect: CGRect)](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-init)Added [CIFilterShape.insetByX(_: Int32, y: Int32) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetby)Added [CIFilterShape.intersectWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)Added [CIFilterShape.intersectWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437806-intersect)Added [CIFilterShape.transformBy(_: CGAffineTransform, interior: Bool) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437808-transformby)Added [CIFilterShape.unionWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1438227-unionwith)Added [CIFilterShape.unionWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437601-unionwithrect)Added [CIImage.colorSpace](https://developer.apple.com/documentation/coreimage/ciimage/1437750-colorspace)Added [CIImage.extent](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)Added [CIImage.init(CVImageBuffer: CVImageBuffer)](https://developer.apple.com/documentation/coreimage/ciimage/1438012-init)Added [CIImage.init(CVImageBuffer: CVImageBuffer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437617-initwithcvimagebuffer)Added [CIImage.init(imageProvider: AnyObject, size: Int, _: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)Added [CIImage.init(MTLTexture: MTLTexture, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437890-init)Added [CIImage.properties](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)Added [CIImage.url](https://developer.apple.com/documentation/coreimage/ciimage/1438195-url)Added [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)Added [CIImageAccumulator.clear()](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427720-clear)Added [CIImageAccumulator.extent](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427714-extent)Added [CIImageAccumulator.format](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427716-format)Added [CIImageAccumulator.image() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427704-image)Added [CIImageAccumulator.init(extent: CGRect, format: CIFormat)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-initwithextent)Added [CIImageAccumulator.init(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-initwithextent)Added [CIImageAccumulator.setImage(_: CIImage)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427702-setimage)Added [CIImageAccumulator.setImage(_: CIImage, dirtyRect: CGRect)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)Added [CIKernel.name](https://developer.apple.com/documentation/coreimage/cikernel/1438067-name)Added [CIKernel.setROISelector(_: Selector)](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)Added [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)Added [CISampler.definition](https://developer.apple.com/documentation/coreimage/cisampler/1437877-definition)Added [CISampler.extent](https://developer.apple.com/documentation/coreimage/cisampler/1437872-extent)Added [CISampler.init(image: CIImage)](https://developer.apple.com/documentation/coreimage/cisampler/1438117-init)Added [CISampler.init(image: CIImage, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cisampler/1437963-initwithimage)Added [CITextFeature](https://developer.apple.com/documentation/coreimage/citextfeature)Added [CITextFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438004-bottomleft)Added [CITextFeature.bottomRight](https://developer.apple.com/documentation/coreimage/citextfeature/1437659-bottomright)Added [CITextFeature.bounds](https://developer.apple.com/documentation/coreimage/citextfeature/1437885-bounds)Added [CITextFeature.subFeatures](https://developer.apple.com/documentation/coreimage/citextfeature/1437810-subfeatures)Added [CITextFeature.topLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438221-topleft)Added [CITextFeature.topRight](https://developer.apple.com/documentation/coreimage/citextfeature/1438282-topright)Added [CIVector.CGAffineTransformValue](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)Added [CIVector.CGPointValue](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)Added [CIVector.CGRectValue](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)Added [CIVector.count](https://developer.apple.com/documentation/coreimage/civector/1438197-count)Added [CIVector.stringRepresentation](https://developer.apple.com/documentation/coreimage/civector/1437752-stringrepresentation)Added [CIVector.W](https://developer.apple.com/documentation/coreimage/civector/1438058-w)Added [CIVector.X](https://developer.apple.com/documentation/coreimage/civector/1437738-x)Added [CIVector.Y](https://developer.apple.com/documentation/coreimage/civector/1437843-y)Added [CIVector.Z](https://developer.apple.com/documentation/coreimage/civector/1437627-z)Added [CIWarpKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1438278-init)Added [NSObject.provideImageData(_: UnsafeMutablePointer<Void>, bytesPerRow: Int, origin: Int, _: Int, size: Int, _: Int, userInfo: AnyObject?)](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)Added [CIDetectorNumberOfAngles](https://developer.apple.com/documentation/coreimage/cidetectornumberofangles)Added [CIDetectorReturnSubFeatures](https://developer.apple.com/documentation/coreimage/cidetectorreturnsubfeatures)Added [CIDetectorTypeText](https://developer.apple.com/documentation/coreimage/cidetectortypetext)Added [CIFeatureTypeQRCode](https://developer.apple.com/documentation/coreimage/cifeaturetypeqrcode)Added [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)Added [CIFeatureTypeText](https://developer.apple.com/documentation/coreimage/cifeaturetypetext)Added [kCIAttributeDescription](https://developer.apple.com/documentation/coreimage/kciattributedescription)Added [kCIAttributeFilterAvailable_iOS](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_ios)Added [kCIAttributeFilterAvailable_Mac](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_mac)Added [kCIAttributeReferenceDocumentation](https://developer.apple.com/documentation/coreimage/kciattributereferencedocumentation)Added [kCIAttributeTypeGradient](https://developer.apple.com/documentation/coreimage/kciattributetypegradient)Added [kCIAttributeTypeOpaqueColor](https://developer.apple.com/documentation/coreimage/kciattributetypeopaquecolor)Added [kCICategoryFilterGenerator](https://developer.apple.com/documentation/coreimage/kcicategoryfiltergenerator)Added [kCIContextHighQualityDownsample](https://developer.apple.com/documentation/coreimage/cicontextoption/1437699-highqualitydownsample)Added [kCIFormatA16](https://developer.apple.com/documentation/coreimage/kciformata16)Added [kCIFormatA8](https://developer.apple.com/documentation/coreimage/kciformata8)Added [kCIFormatABGR8](https://developer.apple.com/documentation/coreimage/kciformatabgr8)Added [kCIFormatAf](https://developer.apple.com/documentation/coreimage/kciformataf)Added [kCIFormatAh](https://developer.apple.com/documentation/coreimage/kciformatah)Added [kCIFormatR16](https://developer.apple.com/documentation/coreimage/kciformatr16)Added [kCIFormatR8](https://developer.apple.com/documentation/coreimage/ciformat/1437695-r8)Added [kCIFormatRf](https://developer.apple.com/documentation/coreimage/kciformatrf)Added [kCIFormatRG16](https://developer.apple.com/documentation/coreimage/ciformat/1437648-rg16)Added [kCIFormatRG8](https://developer.apple.com/documentation/coreimage/kciformatrg8)Added [kCIFormatRGf](https://developer.apple.com/documentation/coreimage/ciformat/1438157-rgf)Added [kCIFormatRGh](https://developer.apple.com/documentation/coreimage/kciformatrgh)Added [kCIFormatRh](https://developer.apple.com/documentation/coreimage/kciformatrh)Added [kCIImageProviderTileSize](https://developer.apple.com/documentation/coreimage/kciimageprovidertilesize)Added [kCIImageProviderUserInfo](https://developer.apple.com/documentation/coreimage/kciimageprovideruserinfo)Added [kCIInputBiasKey](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)Added [kCIInputGradientImageKey](https://developer.apple.com/documentation/coreimage/kciinputgradientimagekey)Added [kCIInputRefractionKey](https://developer.apple.com/documentation/coreimage/kciinputrefractionkey)Added [kCIInputShadingImageKey](https://developer.apple.com/documentation/coreimage/kciinputshadingimagekey)Added [kCIInputWeightsKey](https://developer.apple.com/documentation/coreimage/kciinputweightskey)Added [kCISamplerAffineMatrix](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)Added [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)Added [kCISamplerFilterLinear](https://developer.apple.com/documentation/coreimage/kcisamplerfilterlinear)Added [kCISamplerFilterMode](https://developer.apple.com/documentation/coreimage/kcisamplerfiltermode)Added [kCISamplerFilterNearest](https://developer.apple.com/documentation/coreimage/kcisamplerfilternearest)Added [kCISamplerWrapBlack](https://developer.apple.com/documentation/coreimage/kcisamplerwrapblack)Added [kCISamplerWrapClamp](https://developer.apple.com/documentation/coreimage/kcisamplerwrapclamp)Added [kCISamplerWrapMode](https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode)Added [kCIUIParameterSet](https://developer.apple.com/documentation/coreimage/kciuiparameterset)Added [kCIUISetAdvanced](https://developer.apple.com/documentation/coreimage/kciuisetadvanced)Added [kCIUISetBasic](https://developer.apple.com/documentation/coreimage/kciuisetbasic)Added [kCIUISetDevelopment](https://developer.apple.com/documentation/coreimage/kciuisetdevelopment)Added [kCIUISetIntermediate](https://developer.apple.com/documentation/coreimage/kciuisetintermediate)Added UNIFIED_CORE_IMAGEModified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` class CIColor : NSObject, NSCoding, NSCopying {     init!(CGColor c: CGColor!) -> CIColor     class func colorWithCGColor(_ c: CGColor!) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor!     init!(string representation: String!) -> CIColor     class func colorWithString(_ representation: String!) -> CIColor!     init!(CGColor c: CGColor!)     func numberOfComponents() -> Int     func components() -> UnsafePointer<CGFloat>     func alpha() -> CGFloat     func colorSpace() -> Unmanaged<CGColorSpace>!     func red() -> CGFloat     func green() -> CGFloat     func blue() -> CGFloat     func stringRepresentation() -> String! } extension CIColor {     init?(color color: UIColor) } ``` | AnyObject, NSCoding, NSCopying | iOS 8.0 |
| To | ``` class CIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(CGColor c: CGColor)     class func colorWithCGColor(_ c: CGColor) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> Self     convenience init(string representation: String)     class func colorWithString(_ representation: String) -> Self     init(CGColor c: CGColor)     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     var numberOfComponents: Int { get }     var components: UnsafePointer<CGFloat> { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace { get }     var red: CGFloat { get }     var green: CGFloat { get }     var blue: CGFloat { get }     var stringRepresentation: String { get } } extension CIColor {     convenience init(color color: UIColor) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | iOS 5.0 |

Modified [CIColor.init(CGColor: CGColor)](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGColor c: CGColor!) ``` |
| To | ``` init(CGColor c: CGColor) ``` |

Modified [CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat)](https://developer.apple.com/documentation/coreimage/cicolor/1437941-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor ``` |
| To | ``` convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat) ``` |

Modified [CIColor.init(string: String)](https://developer.apple.com/documentation/coreimage/cicolor/1438059-colorwithstring)

|  | Declaration |
| --- | --- |
| From | ``` init!(string representation: String!) -> CIColor ``` |
| To | ``` convenience init(string representation: String) ``` |

Modified [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel)

|  | Declaration |
| --- | --- |
| From | ``` class CIColorKernel : CIKernel {     func applyWithExtent(_ extent: CGRect, arguments args: [AnyObject]!) -> CIImage! } ``` |
| To | ``` class CIColorKernel : CIKernel {     convenience init?(string string: String)     class func kernelWithString(_ string: String) -> Self?     func applyWithExtent(_ extent: CGRect, arguments args: [AnyObject]?) -> CIImage? } ``` |

Modified [CIColorKernel.applyWithExtent(_: CGRect, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438110-applywithextent)

|  | Declaration |
| --- | --- |
| From | ``` func applyWithExtent(_ extent: CGRect, arguments args: [AnyObject]!) -> CIImage! ``` |
| To | ``` func applyWithExtent(_ extent: CGRect, arguments args: [AnyObject]?) -> CIImage? ``` |

Modified [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CIContext : NSObject {     init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGContext(_ ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext!     init!(options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithOptions(_ dict: [NSObject : AnyObject]!) -> CIContext!     init!(EAGLContext eaglContext: EAGLContext!) -> CIContext     class func contextWithEAGLContext(_ eaglContext: EAGLContext!) -> CIContext!     init!(EAGLContext eaglContext: EAGLContext!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithEAGLContext(_ eaglContext: EAGLContext!, options dict: [NSObject : AnyObject]!) -> CIContext!     func drawImage(_ im: CIImage!, atPoint p: CGPoint, fromRect src: CGRect)     func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect)     func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage!     func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage!     func createCGLayerWithSize(_ size: CGSize, info d: CFDictionary!) -> Unmanaged<CGLayer>!     func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!)     func render(_ image: CIImage!, toCVPixelBuffer buffer: CVPixelBuffer!)     func render(_ image: CIImage!, toCVPixelBuffer buffer: CVPixelBuffer!, bounds r: CGRect, colorSpace cs: CGColorSpace!)     func reclaimResources()     func clearCaches()     func inputImageMaximumSize() -> CGSize     func outputImageMaximumSize() -> CGSize } ``` | iOS 8.0 |
| To | ``` class CIContext : NSObject {      init(CGContext cgctx: CGContext, options options: [String : AnyObject]?)     class func contextWithCGContext(_ cgctx: CGContext, options options: [String : AnyObject]?) -> CIContext      init(options options: [String : AnyObject]?)     class func contextWithOptions(_ options: [String : AnyObject]?) -> CIContext      init(EAGLContext eaglContext: EAGLContext)     class func contextWithEAGLContext(_ eaglContext: EAGLContext) -> CIContext      init(EAGLContext eaglContext: EAGLContext, options options: [String : AnyObject]?)     class func contextWithEAGLContext(_ eaglContext: EAGLContext, options options: [String : AnyObject]?) -> CIContext      init(MTLDevice device: MTLDevice)     class func contextWithMTLDevice(_ device: MTLDevice) -> CIContext      init(MTLDevice device: MTLDevice, options options: [String : AnyObject]?)     class func contextWithMTLDevice(_ device: MTLDevice, options options: [String : AnyObject]?) -> CIContext     var workingColorSpace: CGColorSpace { get }     func drawImage(_ image: CIImage, atPoint atPoint: CGPoint, fromRect fromRect: CGRect)     func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect)     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage     func createCGLayerWithSize(_ size: CGSize, info info: CFDictionary?) -> CGLayer     func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toMTLTexture texture: MTLTexture, commandBuffer commandBuffer: MTLCommandBuffer?, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace)     func reclaimResources()     func clearCaches()     func inputImageMaximumSize() -> CGSize     func outputImageMaximumSize() -> CGSize } extension CIContext {     class func offlineGPUCount() -> UInt32 } ``` | iOS 5.0 |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)

|  | Declaration |
| --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage! ``` |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage ``` |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)

|  | Declaration |
| --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage! ``` |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage ``` |

Modified [CIContext.drawImage(_: CIImage, inRect: CGRect, fromRect: CGRect)](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)

|  | Declaration |
| --- | --- |
| From | ``` func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect) ``` |
| To | ``` func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect) ``` |

Modified [CIContext.init(EAGLContext: EAGLContext)](https://developer.apple.com/documentation/coreimage/cicontext/1620419-contextwitheaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(EAGLContext eaglContext: EAGLContext!) -> CIContext ``` |
| To | ``` init(EAGLContext eaglContext: EAGLContext) ``` |

Modified [CIContext.init(EAGLContext: EAGLContext, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1620362-contextwitheaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` init!(EAGLContext eaglContext: EAGLContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` |
| To | ``` init(EAGLContext eaglContext: EAGLContext, options options: [String : AnyObject]?) ``` |

Modified [CIContext.init(options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1438261-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(options dict: [NSObject : AnyObject]!) -> CIContext ``` |
| To | ``` init(options options: [String : AnyObject]?) ``` |

Modified [CIContext.render(_: CIImage, toBitmap: UnsafeMutablePointer<Void>, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)

|  | Declaration |
| --- | --- |
| From | ``` func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) ``` |
| To | ``` func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` |

Modified [CIContext.render(_: CIImage, toCVPixelBuffer: CVPixelBuffer)](https://developer.apple.com/documentation/coreimage/cicontext/1437853-render)

|  | Declaration |
| --- | --- |
| From | ``` func render(_ image: CIImage!, toCVPixelBuffer buffer: CVPixelBuffer!) ``` |
| To | ``` func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer) ``` |

Modified [CIContext.render(_: CIImage, toCVPixelBuffer: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437835-render)

|  | Declaration |
| --- | --- |
| From | ``` func render(_ image: CIImage!, toCVPixelBuffer buffer: CVPixelBuffer!, bounds r: CGRect, colorSpace cs: CGColorSpace!) ``` |
| To | ``` func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?) ``` |

Modified [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CIDetector : NSObject {     init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector     class func detectorOfType(_ type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector!     func featuresInImage(_ image: CIImage!) -> [AnyObject]!     func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! } ``` | iOS 8.0 |
| To | ``` class CIDetector : NSObject {      init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?)     class func detectorOfType(_ type: String, context context: CIContext?, options options: [String : AnyObject]?) -> CIDetector     func featuresInImage(_ image: CIImage) -> [CIFeature]     func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] } ``` | iOS 5.0 |

Modified [CIDetector.featuresInImage(_: CIImage) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)

|  | Declaration |
| --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!) -> [AnyObject]! ``` |
| To | ``` func featuresInImage(_ image: CIImage) -> [CIFeature] ``` |

Modified [CIDetector.featuresInImage(_: CIImage, options: [String : AnyObject]?) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)

|  | Declaration |
| --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] ``` |

Modified [CIDetector.init(ofType: String, context: CIContext?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` |
| To | ``` init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?) ``` |

Modified [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class CIFeature : NSObject {     var type: String! { get }     var bounds: CGRect { get } } ``` | iOS 8.0 |
| To | ``` class CIFeature : NSObject {     var type: String { get }     var bounds: CGRect { get } } ``` | iOS 5.0 |

Modified [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: String { get } ``` |

Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` class CIFilter : NSObject, NSCoding, NSCopying {     var outputImage: CIImage! { get }     func name() -> String!     func inputKeys() -> [AnyObject]!     func outputKeys() -> [AnyObject]!     func setDefaults()     func attributes() -> [NSObject : AnyObject]!     func apply(_ k: CIKernel!, arguments args: [AnyObject]!, options dict: [NSObject : AnyObject]!) -> CIImage! } extension CIFilter {     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } extension CIFilter {     init!(name name: String!) -> CIFilter     class func filterWithName(_ name: String!) -> CIFilter!     init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter     class func filterWithName(_ name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter!     class func filterNamesInCategory(_ category: String!) -> [AnyObject]!     class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]!     class func localizedNameForFilterName(_ filterName: String!) -> String!     class func localizedNameForCategory(_ category: String!) -> String!     class func localizedDescriptionForFilterName(_ filterName: String!) -> String!     class func localizedReferenceDocumentationForFilterName(_ filterName: String!) -> NSURL! } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData!     class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! } extension CIFilter {     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } ``` | AnyObject, NSCoding, NSCopying | iOS 8.0 |
| To | ``` class CIFilter : NSObject, NSSecureCoding, NSCoding, NSCopying {     var outputImage: CIImage? { get }     var name: String { get }     var inputKeys: [String] { get }     var outputKeys: [String] { get }     func setDefaults()     var attributes: [String : AnyObject] { get }     func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? } extension CIFilter {      init?(name name: String)     class func filterWithName(_ name: String) -> CIFilter?      init?(name name: String, withInputParameters params: [String : AnyObject]?)     class func filterWithName(_ name: String, withInputParameters params: [String : AnyObject]?) -> CIFilter?     class func filterNamesInCategory(_ category: String?) -> [String]     class func filterNamesInCategories(_ categories: [String]?) -> [String]     class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject])     class func localizedNameForFilterName(_ filterName: String) -> String?     class func localizedNameForCategory(_ category: String) -> String     class func localizedDescriptionForFilterName(_ filterName: String) -> String?     class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData     class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | iOS 5.0 |

Modified [CIFilter.filterArrayFromSerializedXMP(_: NSData, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)

|  | Declaration |
| --- | --- |
| From | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! ``` |
| To | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] ``` |

Modified [CIFilter.filterNamesInCategories(_: [String]?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)

|  | Declaration |
| --- | --- |
| From | ``` class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` class func filterNamesInCategories(_ categories: [String]?) -> [String] ``` |

Modified [CIFilter.filterNamesInCategory(_: String?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)

|  | Declaration |
| --- | --- |
| From | ``` class func filterNamesInCategory(_ category: String!) -> [AnyObject]! ``` |
| To | ``` class func filterNamesInCategory(_ category: String?) -> [String] ``` |

Modified [CIFilter.init(name: String)](https://developer.apple.com/documentation/coreimage/cifilter/1438255-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!) -> CIFilter ``` |
| To | ``` init?(name name: String) ``` |

Modified [CIFilter.init(name: String, withInputParameters: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter ``` |
| To | ``` init?(name name: String, withInputParameters params: [String : AnyObject]?) ``` |

Modified [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var outputImage: CIImage! { get } ``` | iOS 8.0 |
| To | ``` var outputImage: CIImage? { get } ``` | iOS 5.0 |

Modified [CIFilter.serializedXMPFromFilters(_: [CIFilter], inputImageExtent: CGRect) -> NSData [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)

|  | Declaration |
| --- | --- |
| From | ``` class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData! ``` |
| To | ``` class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData ``` |

Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` class CIImage : NSObject, NSCoding, NSCopying {     init!(CGImage image: CGImage!) -> CIImage     class func imageWithCGImage(_ image: CGImage!) -> CIImage!     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGImage(_ image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CGLayer layer: CGLayer!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!) -> CIImage!     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithBitmapData(_ d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage!     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage!     init!(contentsOfURL url: NSURL!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!) -> CIImage!     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(data data: NSData!) -> CIImage     class func imageWithData(_ data: NSData!) -> CIImage!     init!(data data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithData(_ data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(color color: CIColor!) -> CIImage     class func imageWithColor(_ color: CIColor!) -> CIImage!     class func emptyImage() -> CIImage!     init!(CGImage image: CGImage!)     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!)     init!(CGLayer layer: CGLayer!)     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!)     init!(data data: NSData!)     init!(data data: NSData!, options d: [NSObject : AnyObject]!)     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!)     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!)     init!(contentsOfURL url: NSURL!)     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!)     init!(CVPixelBuffer buffer: CVPixelBuffer!)     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!)     init!(color color: CIColor!)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage!     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage!     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage!     func imageByCroppingToRect(_ r: CGRect) -> CIImage!     func imageByClampingToExtent() -> CIImage!     func extent() -> CGRect     func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage!     func properties() -> [NSObject : AnyObject]!     func definition() -> CIFilterShape!     func url() -> NSURL!     func colorSpace() -> Unmanaged<CGColorSpace>!     func regionOfInterestForImage(_ im: CIImage!, inRect r: CGRect) -> CGRect } extension CIImage {     func autoAdjustmentFilters() -> [AnyObject]!     func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! } extension CIImage {     init!(image image: UIImage!)     init!(image image: UIImage!, options options: [NSObject : AnyObject]!) } ``` | AnyObject, NSCoding, NSCopying | iOS 8.0 |
| To | ``` class CIImage : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(CGImage image: CGImage)     class func imageWithCGImage(_ image: CGImage) -> CIImage      init(CGImage image: CGImage, options options: [String : AnyObject]?)     class func imageWithCGImage(_ image: CGImage, options options: [String : AnyObject]?) -> CIImage      init(CGLayer layer: CGLayer)     class func imageWithCGLayer(_ layer: CGLayer) -> CIImage      init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     class func imageWithCGLayer(_ layer: CGLayer, options options: [String : AnyObject]?) -> CIImage      init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     class func imageWithBitmapData(_ data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) -> CIImage      init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     class func imageWithMTLTexture(_ texture: MTLTexture, options options: [String : AnyObject]?) -> CIImage      init?(contentsOfURL url: NSURL)     class func imageWithContentsOfURL(_ url: NSURL) -> CIImage?      init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     class func imageWithContentsOfURL(_ url: NSURL, options options: [String : AnyObject]?) -> CIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> CIImage?      init?(data data: NSData, options options: [String : AnyObject]?)     class func imageWithData(_ data: NSData, options options: [String : AnyObject]?) -> CIImage?      init(CVImageBuffer imageBuffer: CVImageBuffer)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer) -> CIImage      init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) -> CIImage      init(color color: CIColor)     class func imageWithColor(_ color: CIColor) -> CIImage     class func emptyImage() -> CIImage     init(CGImage image: CGImage)     init(CGImage image: CGImage, options options: [String : AnyObject]?)     init(CGLayer layer: CGLayer)     init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     init?(data data: NSData)     init?(data data: NSData, options options: [String : AnyObject]?)     init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     init?(contentsOfURL url: NSURL)     init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     init(CVImageBuffer imageBuffer: CVImageBuffer)     init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     init(color color: CIColor)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage) -> CIImage     func imageByCroppingToRect(_ rect: CGRect) -> CIImage     func imageByClampingToExtent() -> CIImage     func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage     var extent: CGRect { get }     var properties: [String : AnyObject] { get }     var definition: CIFilterShape { get }     var url: NSURL? { get }     var colorSpace: CGColorSpace? { get }     func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect } extension CIImage {     func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] } extension CIImage {      init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?)     class func imageWithImageProvider(_ p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) -> CIImage     init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) } extension CIImage {     init?(image image: UIImage)     init?(image image: UIImage, options options: [NSObject : AnyObject]?) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | iOS 5.0 |

Modified [CIImage.autoAdjustmentFiltersWithOptions(_: [String : AnyObject]?) -> [CIFilter]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilterswithoptions)

|  | Declaration |
| --- | --- |
| From | ``` func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] ``` |

Modified [CIImage.emptyImage() -> CIImage [class]](https://developer.apple.com/documentation/coreimage/ciimage/1438023-emptyimage)

|  | Declaration |
| --- | --- |
| From | ``` class func emptyImage() -> CIImage! ``` |
| To | ``` class func emptyImage() -> CIImage ``` |

Modified [CIImage.imageByApplyingFilter(_: String, withInputParameters: [String : AnyObject]?) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437589-imagebyapplyingfilter)

|  | Declaration |
| --- | --- |
| From | ``` func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage! ``` |
| To | ``` func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage ``` |

Modified [CIImage.imageByApplyingOrientation(_: Int32) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438223-oriented)

|  | Declaration |
| --- | --- |
| From | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage! ``` |
| To | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage ``` |

Modified [CIImage.imageByApplyingTransform(_: CGAffineTransform) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438203-imagebyapplyingtransform)

|  | Declaration |
| --- | --- |
| From | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage! ``` |
| To | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage ``` |

Modified [CIImage.imageByClampingToExtent() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437628-imagebyclampingtoextent)

|  | Declaration |
| --- | --- |
| From | ``` func imageByClampingToExtent() -> CIImage! ``` |
| To | ``` func imageByClampingToExtent() -> CIImage ``` |

Modified [CIImage.imageByCompositingOverImage(_: CIImage) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437837-imagebycompositingoverimage)

|  | Declaration |
| --- | --- |
| From | ``` func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage! ``` |
| To | ``` func imageByCompositingOverImage(_ dest: CIImage) -> CIImage ``` |

Modified [CIImage.imageByCroppingToRect(_: CGRect) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437833-cropped)

|  | Declaration |
| --- | --- |
| From | ``` func imageByCroppingToRect(_ r: CGRect) -> CIImage! ``` |
| To | ``` func imageByCroppingToRect(_ rect: CGRect) -> CIImage ``` |

Modified [CIImage.init(bitmapData: NSData, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` |
| To | ``` init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` |

Modified [CIImage.init(CGImage: CGImage)](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGImage image: CGImage!) ``` |
| To | ``` init(CGImage image: CGImage) ``` |

Modified [CIImage.init(CGImage: CGImage, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init(CGImage image: CGImage, options options: [String : AnyObject]?) ``` |

Modified [CIImage.init(color: CIColor)](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` init!(color color: CIColor!) ``` |
| To | ``` init(color color: CIColor) ``` |

Modified [CIImage.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!) ``` |
| To | ``` init?(contentsOfURL url: NSURL) ``` |

Modified [CIImage.init(contentsOfURL: NSURL, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437867-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?) ``` |

Modified [CIImage.init(CVPixelBuffer: CVPixelBuffer)](https://developer.apple.com/documentation/coreimage/ciimage/1438072-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CVPixelBuffer buffer: CVPixelBuffer!) ``` |
| To | ``` init(CVPixelBuffer pixelBuffer: CVPixelBuffer) ``` |

Modified [CIImage.init(CVPixelBuffer: CVPixelBuffer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438209-initwithcvpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) ``` |
| To | ``` init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) ``` |

Modified [CIImage.init(data: NSData)](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!) ``` |
| To | ``` init?(data data: NSData) ``` |

Modified [CIImage.init(data: NSData, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438032-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` init!(data data: NSData!, options d: [NSObject : AnyObject]!) ``` |
| To | ``` init?(data data: NSData, options options: [String : AnyObject]?) ``` |

Modified [CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1438015-initwithtexture)

|  | Declaration |
| --- | --- |
| From | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` |
| To | ``` init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) ``` |

Modified [CIImage.regionOfInterestForImage(_: CIImage, inRect: CGRect) -> CGRect](https://developer.apple.com/documentation/coreimage/ciimage/1437994-regionofinterest)

|  | Declaration |
| --- | --- |
| From | ``` func regionOfInterestForImage(_ im: CIImage!, inRect r: CGRect) -> CGRect ``` |
| To | ``` func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect ``` |

Modified [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)

|  | Declaration |
| --- | --- |
| From | ``` class CIKernel : NSObject {     class func kernelsWithString(_ s: String!) -> [AnyObject]!     convenience init!(string string: String!)     class func kernelWithString(_ string: String!) -> Self!     func name() -> String!     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback!, arguments args: [AnyObject]!) -> CIImage! } ``` |
| To | ``` class CIKernel : NSObject {     class func kernelsWithString(_ string: String) -> [CIKernel]?     convenience init?(string string: String)     class func kernelWithString(_ string: String) -> Self?     var name: String { get }     func setROISelector(_ method: Selector)     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, arguments args: [AnyObject]?) -> CIImage? } ``` |

Modified [CIKernel.applyWithExtent(_: CGRect, roiCallback: CIKernelROICallback, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cikernel/1438243-applywithextent)

|  | Declaration |
| --- | --- |
| From | ``` func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback!, arguments args: [AnyObject]!) -> CIImage! ``` |
| To | ``` func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, arguments args: [AnyObject]?) -> CIImage? ``` |

Modified [CIKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(string string: String!) ``` |
| To | ``` convenience init?(string string: String) ``` |

Modified [CIKernel.kernelsWithString(_: String) -> [CIKernel]? [class]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)

|  | Declaration |
| --- | --- |
| From | ``` class func kernelsWithString(_ s: String!) -> [AnyObject]! ``` |
| To | ``` class func kernelsWithString(_ string: String) -> [CIKernel]? ``` |

Modified [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)

|  | Declaration |
| --- | --- |
| From | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String! { get } } ``` |
| To | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String { get } } ``` |

Modified [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)

|  | Declaration |
| --- | --- |
| From | ``` var messageString: String! { get } ``` |
| To | ``` var messageString: String { get } ``` |

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` class CIVector : NSObject, NSCopying, NSCoding {     init!(values values: UnsafePointer<CGFloat>, count count: Int) -> CIVector     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> CIVector!     init!(x x: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector!     init!(CGPoint p: CGPoint) -> CIVector     class func vectorWithCGPoint(_ p: CGPoint) -> CIVector!     init!(CGRect r: CGRect) -> CIVector     class func vectorWithCGRect(_ r: CGRect) -> CIVector!     init!(CGAffineTransform t: CGAffineTransform) -> CIVector     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> CIVector!     init!(string representation: String!) -> CIVector     class func vectorWithString(_ representation: String!) -> CIVector!     init!(values values: UnsafePointer<CGFloat>, count count: Int)     init!(x x: CGFloat)     init!(x x: CGFloat, y y: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     init!(CGPoint p: CGPoint)     init!(CGRect r: CGRect)     init!(CGAffineTransform r: CGAffineTransform)     init!(string representation: String!)     func valueAtIndex(_ index: Int) -> CGFloat     func count() -> Int     func X() -> CGFloat     func Y() -> CGFloat     func Z() -> CGFloat     func W() -> CGFloat     func CGPointValue() -> CGPoint     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func stringRepresentation() -> String! } ``` | AnyObject, NSCoding, NSCopying | iOS 8.0 |
| To | ``` class CIVector : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(values values: UnsafePointer<CGFloat>, count count: Int)     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> Self     convenience init(x x: CGFloat)     class func vectorWithX(_ x: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> Self     convenience init(CGPoint p: CGPoint)     class func vectorWithCGPoint(_ p: CGPoint) -> Self     convenience init(CGRect r: CGRect)     class func vectorWithCGRect(_ r: CGRect) -> Self     convenience init(CGAffineTransform t: CGAffineTransform)     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> Self     convenience init(string representation: String)     class func vectorWithString(_ representation: String) -> Self     init(values values: UnsafePointer<CGFloat>, count count: Int)     convenience init(x x: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     convenience init(CGPoint p: CGPoint)     convenience init(CGRect r: CGRect)     convenience init(CGAffineTransform r: CGAffineTransform)     convenience init(string representation: String)     func valueAtIndex(_ index: Int) -> CGFloat     var count: Int { get }     var X: CGFloat { get }     var Y: CGFloat { get }     var Z: CGFloat { get }     var W: CGFloat { get }     var CGPointValue: CGPoint { get }     var CGRectValue: CGRect { get }     var CGAffineTransformValue: CGAffineTransform { get }     var stringRepresentation: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | iOS 5.0 |

Modified [CIVector.init(CGAffineTransform: CGAffineTransform)](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGAffineTransform r: CGAffineTransform) ``` |
| To | ``` convenience init(CGAffineTransform r: CGAffineTransform) ``` |

Modified [CIVector.init(CGPoint: CGPoint)](https://developer.apple.com/documentation/coreimage/civector/1438133-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGPoint p: CGPoint) ``` |
| To | ``` convenience init(CGPoint p: CGPoint) ``` |

Modified [CIVector.init(CGRect: CGRect)](https://developer.apple.com/documentation/coreimage/civector/1437644-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGRect r: CGRect) ``` |
| To | ``` convenience init(CGRect r: CGRect) ``` |

Modified [CIVector.init(string: String)](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)

|  | Declaration |
| --- | --- |
| From | ``` init!(string representation: String!) ``` |
| To | ``` convenience init(string representation: String) ``` |

Modified [CIVector.init(values: UnsafePointer<CGFloat>, count: Int)](https://developer.apple.com/documentation/coreimage/civector/1437849-initwithvalues)

|  | Declaration |
| --- | --- |
| From | ``` init!(values values: UnsafePointer<CGFloat>, count count: Int) ``` |
| To | ``` init(values values: UnsafePointer<CGFloat>, count count: Int) ``` |

Modified [CIVector.init(x: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437657-initwithx)

|  | Declaration |
| --- | --- |
| From | ``` init!(x x: CGFloat) ``` |
| To | ``` convenience init(x x: CGFloat) ``` |

Modified [CIVector.init(x: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437865-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat) ``` |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat) ``` |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)

|  | Declaration |
| --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438088-initwithx)

|  | Declaration |
| --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` |

Modified [CIWarpKernel](https://developer.apple.com/documentation/coreimage/ciwarpkernel)

|  | Declaration |
| --- | --- |
| From | ``` class CIWarpKernel : CIKernel {     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback!, inputImage image: CIImage!, arguments args: [AnyObject]!) -> CIImage! } ``` |
| To | ``` class CIWarpKernel : CIKernel {     convenience init?(string string: String)     class func kernelWithString(_ string: String) -> Self?     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, inputImage image: CIImage, arguments args: [AnyObject]?) -> CIImage? } ``` |

Modified [CIWarpKernel.applyWithExtent(_: CGRect, roiCallback: CIKernelROICallback, inputImage: CIImage, arguments: [AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1437798-apply)

|  | Declaration |
| --- | --- |
| From | ``` func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback!, inputImage image: CIImage!, arguments args: [AnyObject]!) -> CIImage! ``` |
| To | ``` func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, inputImage image: CIImage, arguments args: [AnyObject]?) -> CIImage? ``` |

Modified [kCIAttributeTypeColor](https://developer.apple.com/documentation/coreimage/kciattributetypecolor)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified [kCIFormatBGRA8](https://developer.apple.com/documentation/coreimage/kciformatbgra8)

|  | Introduction |
| --- | --- |
| From | iOS 5.0 |
| To | iOS 8.0 |

Modified [kCIFormatRGBA8](https://developer.apple.com/documentation/coreimage/kciformatrgba8)

|  | Introduction |
| --- | --- |
| From | iOS 5.0 |
| To | iOS 8.0 |

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
