---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreImage.html
archived_at: '2026-07-18T02:57:07.431848Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreImage Changes for Swift

### CoreImage

Modified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(CGColor c: CGColor)     class func colorWithCGColor(_ c: CGColor) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> Self     convenience init(string representation: String)     class func colorWithString(_ representation: String) -> Self     init(CGColor c: CGColor)     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     var numberOfComponents: Int { get }     var components: UnsafePointer<CGFloat> { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace { get }     var red: CGFloat { get }     var green: CGFloat { get }     var blue: CGFloat { get }     var stringRepresentation: String { get } } extension CIColor {     convenience init(color color: UIColor) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CIColor : NSObject, NSSecureCoding, NSCopying {     convenience init(CGColor c: CGColor)     class func colorWithCGColor(_ c: CGColor) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> Self     convenience init(string representation: String)     class func colorWithString(_ representation: String) -> Self     init(CGColor c: CGColor)     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     var numberOfComponents: Int { get }     var components: UnsafePointer<CGFloat> { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace { get }     var red: CGFloat { get }     var green: CGFloat { get }     var blue: CGFloat { get }     var stringRepresentation: String { get } } extension CIColor {     convenience init(color color: UIColor) } ``` | NSCopying, NSSecureCoding |

Modified [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CIFilter : NSObject, NSSecureCoding, NSCoding, NSCopying {     var outputImage: CIImage? { get }     var name: String { get }     var inputKeys: [String] { get }     var outputKeys: [String] { get }     func setDefaults()     var attributes: [String : AnyObject] { get }     func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? } extension CIFilter {      init?(name name: String)     class func filterWithName(_ name: String) -> CIFilter?      init?(name name: String, withInputParameters params: [String : AnyObject]?)     class func filterWithName(_ name: String, withInputParameters params: [String : AnyObject]?) -> CIFilter?     class func filterNamesInCategory(_ category: String?) -> [String]     class func filterNamesInCategories(_ categories: [String]?) -> [String]     class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject])     class func localizedNameForFilterName(_ filterName: String) -> String?     class func localizedNameForCategory(_ category: String) -> String     class func localizedDescriptionForFilterName(_ filterName: String) -> String?     class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData     class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CIFilter : NSObject, NSSecureCoding, NSCopying {     var outputImage: CIImage? { get }     var name: String { get }     var inputKeys: [String] { get }     var outputKeys: [String] { get }     func setDefaults()     var attributes: [String : AnyObject] { get }     func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? } extension CIFilter {      init?(name name: String)     class func filterWithName(_ name: String) -> CIFilter?      init?(name name: String, withInputParameters params: [String : AnyObject]?)     class func filterWithName(_ name: String, withInputParameters params: [String : AnyObject]?) -> CIFilter?     class func filterNamesInCategory(_ category: String?) -> [String]     class func filterNamesInCategories(_ categories: [String]?) -> [String]     class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject])     class func localizedNameForFilterName(_ filterName: String) -> String?     class func localizedNameForCategory(_ category: String) -> String     class func localizedDescriptionForFilterName(_ filterName: String) -> String?     class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData     class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] } ``` | NSCopying, NSSecureCoding |

Modified [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CIImage : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(CGImage image: CGImage)     class func imageWithCGImage(_ image: CGImage) -> CIImage      init(CGImage image: CGImage, options options: [String : AnyObject]?)     class func imageWithCGImage(_ image: CGImage, options options: [String : AnyObject]?) -> CIImage      init(CGLayer layer: CGLayer)     class func imageWithCGLayer(_ layer: CGLayer) -> CIImage      init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     class func imageWithCGLayer(_ layer: CGLayer, options options: [String : AnyObject]?) -> CIImage      init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     class func imageWithBitmapData(_ data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) -> CIImage      init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     class func imageWithMTLTexture(_ texture: MTLTexture, options options: [String : AnyObject]?) -> CIImage      init?(contentsOfURL url: NSURL)     class func imageWithContentsOfURL(_ url: NSURL) -> CIImage?      init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     class func imageWithContentsOfURL(_ url: NSURL, options options: [String : AnyObject]?) -> CIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> CIImage?      init?(data data: NSData, options options: [String : AnyObject]?)     class func imageWithData(_ data: NSData, options options: [String : AnyObject]?) -> CIImage?      init(CVImageBuffer imageBuffer: CVImageBuffer)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer) -> CIImage      init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) -> CIImage      init(color color: CIColor)     class func imageWithColor(_ color: CIColor) -> CIImage     class func emptyImage() -> CIImage     init(CGImage image: CGImage)     init(CGImage image: CGImage, options options: [String : AnyObject]?)     init(CGLayer layer: CGLayer)     init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     init?(data data: NSData)     init?(data data: NSData, options options: [String : AnyObject]?)     init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     init?(contentsOfURL url: NSURL)     init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     init(CVImageBuffer imageBuffer: CVImageBuffer)     init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     init(color color: CIColor)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage) -> CIImage     func imageByCroppingToRect(_ rect: CGRect) -> CIImage     func imageByClampingToExtent() -> CIImage     func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage     var extent: CGRect { get }     var properties: [String : AnyObject] { get }     var definition: CIFilterShape { get }     var url: NSURL? { get }     var colorSpace: CGColorSpace? { get }     func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect } extension CIImage {     func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] } extension CIImage {      init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?)     class func imageWithImageProvider(_ p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) -> CIImage     init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) } extension CIImage {     init?(image image: UIImage)     init?(image image: UIImage, options options: [NSObject : AnyObject]?) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CIImage : NSObject, NSSecureCoding, NSCopying {      init(CGImage image: CGImage)     class func imageWithCGImage(_ image: CGImage) -> CIImage      init(CGImage image: CGImage, options options: [String : AnyObject]?)     class func imageWithCGImage(_ image: CGImage, options options: [String : AnyObject]?) -> CIImage      init(CGLayer layer: CGLayer)     class func imageWithCGLayer(_ layer: CGLayer) -> CIImage      init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     class func imageWithCGLayer(_ layer: CGLayer, options options: [String : AnyObject]?) -> CIImage      init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     class func imageWithBitmapData(_ data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) -> CIImage      init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     class func imageWithMTLTexture(_ texture: MTLTexture, options options: [String : AnyObject]?) -> CIImage      init?(contentsOfURL url: NSURL)     class func imageWithContentsOfURL(_ url: NSURL) -> CIImage?      init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     class func imageWithContentsOfURL(_ url: NSURL, options options: [String : AnyObject]?) -> CIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> CIImage?      init?(data data: NSData, options options: [String : AnyObject]?)     class func imageWithData(_ data: NSData, options options: [String : AnyObject]?) -> CIImage?      init(CVImageBuffer imageBuffer: CVImageBuffer)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer) -> CIImage      init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) -> CIImage      init(color color: CIColor)     class func imageWithColor(_ color: CIColor) -> CIImage     class func emptyImage() -> CIImage     init(CGImage image: CGImage)     init(CGImage image: CGImage, options options: [String : AnyObject]?)     init(CGLayer layer: CGLayer)     init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     init?(data data: NSData)     init?(data data: NSData, options options: [String : AnyObject]?)     init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     init?(contentsOfURL url: NSURL)     init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     init(CVImageBuffer imageBuffer: CVImageBuffer)     init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     init(color color: CIColor)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage) -> CIImage     func imageByCroppingToRect(_ rect: CGRect) -> CIImage     func imageByClampingToExtent() -> CIImage     func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage     var extent: CGRect { get }     var properties: [String : AnyObject] { get }     var definition: CIFilterShape { get }     var url: NSURL? { get }     var colorSpace: CGColorSpace? { get }     func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect } extension CIImage {     func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] } extension CIImage {      init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?)     class func imageWithImageProvider(_ p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) -> CIImage     init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) } extension CIImage {     init?(image image: UIImage)     init?(image image: UIImage, options options: [NSObject : AnyObject]?) } ``` | NSCopying, NSSecureCoding |

Modified [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CITextFeature](https://developer.apple.com/documentation/coreimage/citextfeature)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CIVector : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(values values: UnsafePointer<CGFloat>, count count: Int)     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> Self     convenience init(x x: CGFloat)     class func vectorWithX(_ x: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> Self     convenience init(CGPoint p: CGPoint)     class func vectorWithCGPoint(_ p: CGPoint) -> Self     convenience init(CGRect r: CGRect)     class func vectorWithCGRect(_ r: CGRect) -> Self     convenience init(CGAffineTransform t: CGAffineTransform)     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> Self     convenience init(string representation: String)     class func vectorWithString(_ representation: String) -> Self     init(values values: UnsafePointer<CGFloat>, count count: Int)     convenience init(x x: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     convenience init(CGPoint p: CGPoint)     convenience init(CGRect r: CGRect)     convenience init(CGAffineTransform r: CGAffineTransform)     convenience init(string representation: String)     func valueAtIndex(_ index: Int) -> CGFloat     var count: Int { get }     var X: CGFloat { get }     var Y: CGFloat { get }     var Z: CGFloat { get }     var W: CGFloat { get }     var CGPointValue: CGPoint { get }     var CGRectValue: CGRect { get }     var CGAffineTransformValue: CGAffineTransform { get }     var stringRepresentation: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CIVector : NSObject, NSCopying, NSSecureCoding {     convenience init(values values: UnsafePointer<CGFloat>, count count: Int)     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> Self     convenience init(x x: CGFloat)     class func vectorWithX(_ x: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> Self     convenience init(CGPoint p: CGPoint)     class func vectorWithCGPoint(_ p: CGPoint) -> Self     convenience init(CGRect r: CGRect)     class func vectorWithCGRect(_ r: CGRect) -> Self     convenience init(CGAffineTransform t: CGAffineTransform)     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> Self     convenience init(string representation: String)     class func vectorWithString(_ representation: String) -> Self     init(values values: UnsafePointer<CGFloat>, count count: Int)     convenience init(x x: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     convenience init(CGPoint p: CGPoint)     convenience init(CGRect r: CGRect)     convenience init(CGAffineTransform r: CGAffineTransform)     convenience init(string representation: String)     func valueAtIndex(_ index: Int) -> CGFloat     var count: Int { get }     var X: CGFloat { get }     var Y: CGFloat { get }     var Z: CGFloat { get }     var W: CGFloat { get }     var CGPointValue: CGPoint { get }     var CGRectValue: CGRect { get }     var CGAffineTransformValue: CGAffineTransform { get }     var stringRepresentation: String { get } } ``` | NSCopying, NSSecureCoding |

Modified [CIWarpKernel](https://developer.apple.com/documentation/coreimage/ciwarpkernel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
