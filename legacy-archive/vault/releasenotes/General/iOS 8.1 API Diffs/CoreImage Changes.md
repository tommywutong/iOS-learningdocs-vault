---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreImage.html
archived_at: '2026-07-18T02:56:09.540020Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreImage Changes

## CoreImage

Modified CIColor.init(CGColor: CGColor!)

|  | Declaration |
| --- | --- |
| From | ``` init(CGColor c: CGColor!) ``` |
| To | ``` init!(CGColor c: CGColor!) ``` |

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

Modified CIContext.init(EAGLContext: EAGLContext!)

|  | Declaration |
| --- | --- |
| From | ``` init(EAGLContext eaglContext: EAGLContext!) -> CIContext ``` |
| To | ``` init!(EAGLContext eaglContext: EAGLContext!) -> CIContext ``` |

Modified CIContext.init(EAGLContext: EAGLContext!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(EAGLContext eaglContext: EAGLContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` |
| To | ``` init!(EAGLContext eaglContext: EAGLContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` |

Modified CIContext.inputImageMaximumSize() -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIContext.init(options: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(options dict: [NSObject : AnyObject]!) -> CIContext ``` |
| To | ``` init!(options dict: [NSObject : AnyObject]!) -> CIContext ``` |

Modified CIContext.outputImageMaximumSize() -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIContext.render(CIImage!, toCVPixelBuffer: CVPixelBuffer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIContext.render(CIImage!, toCVPixelBuffer: CVPixelBuffer!, bounds: CGRect, colorSpace: CGColorSpace!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetector.featuresInImage(CIImage!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetector.featuresInImage(CIImage!, options:[NSObject: AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetector.init(ofType: String!, context: CIContext!, options:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` |
| To | ``` init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` |

Modified CIFilter.filterArrayFromSerializedXMP(NSData!, inputImageExtent: CGRect, error: NSErrorPointer) -> [AnyObject]! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CIFilter.name() -> String!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
| From | iOS 8.0 |
| To | iOS 6.0 |

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

Modified CIImage.init(CVPixelBuffer: CVPixelBuffer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CVPixelBuffer buffer: CVPixelBuffer!) ``` | iOS 8.0 |
| To | ``` init!(CVPixelBuffer buffer: CVPixelBuffer!) ``` | iOS 5.0 |

Modified CIImage.init(CVPixelBuffer: CVPixelBuffer!, options:[NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) ``` | iOS 5.0 |

Modified CIImage.autoAdjustmentFilters() -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIImage.autoAdjustmentFiltersWithOptions([NSObject: AnyObject]!) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIImage.init(bitmapData: NSData!, bytesPerRow: UInt, size: CGSize, format: CIFormat, colorSpace: CGColorSpace!)

|  | Declaration |
| --- | --- |
| From | ``` init(bitmapData d: NSData!, bytesPerRow bpr: UInt, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` |
| To | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: UInt, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` |

Modified CIImage.init(color: CIColor!)

|  | Declaration |
| --- | --- |
| From | ``` init(color color: CIColor!) ``` |
| To | ``` init!(color color: CIColor!) ``` |

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

Modified CIImage.properties() -> [NSObject: AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIImage.regionOfInterestForImage(CIImage!, inRect: CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | iOS 8.0 |
| To | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | iOS 6.0 |

Modified CIKernel.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(string string: String!) ``` |
| To | ``` convenience init!(string string: String!) ``` |

Modified CIVector.init(CGAffineTransform: CGAffineTransform)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGAffineTransform r: CGAffineTransform) ``` | iOS 8.0 |
| To | ``` init!(CGAffineTransform r: CGAffineTransform) ``` | iOS 5.0 |

Modified CIVector.CGAffineTransformValue() -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIVector.init(CGPoint: CGPoint)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGPoint p: CGPoint) ``` | iOS 8.0 |
| To | ``` init!(CGPoint p: CGPoint) ``` | iOS 5.0 |

Modified CIVector.CGPointValue() -> CGPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIVector.init(CGRect: CGRect)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(CGRect r: CGRect) ``` | iOS 8.0 |
| To | ``` init!(CGRect r: CGRect) ``` | iOS 5.0 |

Modified CIVector.CGRectValue() -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIVector.init(string: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(string representation: String!) ``` |
| To | ``` init!(string representation: String!) ``` |

Modified CIVector.init(values: UnsafePointer<CGFloat>, count: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(values values: UnsafePointer<CGFloat>, count count: UInt) ``` |
| To | ``` init!(values values: UnsafePointer<CGFloat>, count count: UInt) ``` |

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

Modified CIDetectorAccuracy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetectorAccuracyHigh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetectorAccuracyLow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetectorEyeBlink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CIDetectorImageOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetectorMinFeatureSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CIDetectorSmile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CIDetectorTracking

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CIDetectorTypeFace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetectorTypeQRCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCIAttributeTypeCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIAttributeTypeImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIAttributeTypeInteger

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIAttributeTypeTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCICategoryReduction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIFormatARGB8

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCIFormatBGRA8

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIFormatRGBA8

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIFormatRGBAf

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIFormatRGBAh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCIImageAutoAdjustEnhance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIImageAutoAdjustFeatures

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIImageAutoAdjustRedEye

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIImageProperties

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIInputAngleKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputAspectRatioKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputBackgroundImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIInputBrightnessKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputCenterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputColorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputContrastKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputEVKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputExtentKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCIInputIntensityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputMaskImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputRadiusKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputSaturationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputScaleKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputSharpnessKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputTargetImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputTimeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputTransformKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIInputVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCIInputWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCIOutputImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
