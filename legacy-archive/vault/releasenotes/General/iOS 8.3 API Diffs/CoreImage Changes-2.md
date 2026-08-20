---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreImage.html
archived_at: '2026-07-18T02:56:22.677242Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreImage Changes

## CoreImage

Removed CIContext.init(CGContext: CGContext!, options:[NSObject: AnyObject]!)Modified CIColor.numberOfComponents() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func numberOfComponents() -> UInt ``` | iOS 8.0 |
| To | ``` func numberOfComponents() -> Int ``` | iOS 8.3 |

Modified CIContext.init(EAGLContext: EAGLContext!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIContext.init(EAGLContext: EAGLContext!, options:[NSObject: AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIContext.init(options: [NSObject: AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIDetector.init(ofType: String!, context: CIContext!, options:[NSObject: AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CIImage.init(bitmapData: NSData!, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: UInt, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | iOS 8.0 |
| To | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | iOS 8.3 |

Modified CIVector.count() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func count() -> UInt ``` | iOS 8.0 |
| To | ``` func count() -> Int ``` | iOS 8.3 |

Modified CIVector.valueAtIndex(Int) -> CGFloat

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func valueAtIndex(_ index: UInt) -> CGFloat ``` | iOS 8.0 |
| To | ``` func valueAtIndex(_ index: Int) -> CGFloat ``` | iOS 8.3 |

Modified CIVector.init(values: UnsafePointer<CGFloat>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init!(values values: UnsafePointer<CGFloat>, count count: UInt) ``` | iOS 8.0 |
| To | ``` init!(values values: UnsafePointer<CGFloat>, count count: Int) ``` | iOS 8.3 |

Modified CIDetectorAccuracy

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorAccuracy: NSString! ``` |
| To | ``` let CIDetectorAccuracy: String ``` |

Modified CIDetectorAccuracyHigh

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorAccuracyHigh: NSString! ``` |
| To | ``` let CIDetectorAccuracyHigh: String ``` |

Modified CIDetectorAccuracyLow

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorAccuracyLow: NSString! ``` |
| To | ``` let CIDetectorAccuracyLow: String ``` |

Modified CIDetectorAspectRatio

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorAspectRatio: NSString! ``` |
| To | ``` let CIDetectorAspectRatio: String ``` |

Modified CIDetectorEyeBlink

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorEyeBlink: NSString! ``` |
| To | ``` let CIDetectorEyeBlink: String ``` |

Modified CIDetectorFocalLength

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorFocalLength: NSString! ``` |
| To | ``` let CIDetectorFocalLength: String ``` |

Modified CIDetectorImageOrientation

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorImageOrientation: NSString! ``` |
| To | ``` let CIDetectorImageOrientation: String ``` |

Modified CIDetectorMinFeatureSize

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorMinFeatureSize: NSString! ``` |
| To | ``` let CIDetectorMinFeatureSize: String ``` |

Modified CIDetectorSmile

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorSmile: NSString! ``` |
| To | ``` let CIDetectorSmile: String ``` |

Modified CIDetectorTracking

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorTracking: NSString! ``` |
| To | ``` let CIDetectorTracking: String ``` |

Modified CIDetectorTypeFace

|  | Declaration |
| --- | --- |
| From | ``` let CIDetectorTypeFace: NSString! ``` |
| To | ``` let CIDetectorTypeFace: String ``` |

Modified CIDetectorTypeQRCode

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let CIDetectorTypeQRCode: NSString! ``` | iOS 6.0 |
| To | ``` let CIDetectorTypeQRCode: String ``` | iOS 8.0 |

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

Modified kCIAttributeClass

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeClass: NSString! ``` |
| To | ``` let kCIAttributeClass: String ``` |

Modified kCIAttributeDefault

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeDefault: NSString! ``` |
| To | ``` let kCIAttributeDefault: String ``` |

Modified kCIAttributeDisplayName

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeDisplayName: NSString! ``` |
| To | ``` let kCIAttributeDisplayName: String ``` |

Modified kCIAttributeFilterCategories

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeFilterCategories: NSString! ``` |
| To | ``` let kCIAttributeFilterCategories: String ``` |

Modified kCIAttributeFilterDisplayName

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeFilterDisplayName: NSString! ``` |
| To | ``` let kCIAttributeFilterDisplayName: String ``` |

Modified kCIAttributeFilterName

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeFilterName: NSString! ``` |
| To | ``` let kCIAttributeFilterName: String ``` |

Modified kCIAttributeIdentity

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeIdentity: NSString! ``` |
| To | ``` let kCIAttributeIdentity: String ``` |

Modified kCIAttributeMax

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeMax: NSString! ``` |
| To | ``` let kCIAttributeMax: String ``` |

Modified kCIAttributeMin

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeMin: NSString! ``` |
| To | ``` let kCIAttributeMin: String ``` |

Modified kCIAttributeName

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeName: NSString! ``` |
| To | ``` let kCIAttributeName: String ``` |

Modified kCIAttributeSliderMax

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeSliderMax: NSString! ``` |
| To | ``` let kCIAttributeSliderMax: String ``` |

Modified kCIAttributeSliderMin

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeSliderMin: NSString! ``` |
| To | ``` let kCIAttributeSliderMin: String ``` |

Modified kCIAttributeType

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeType: NSString! ``` |
| To | ``` let kCIAttributeType: String ``` |

Modified kCIAttributeTypeAngle

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeAngle: NSString! ``` |
| To | ``` let kCIAttributeTypeAngle: String ``` |

Modified kCIAttributeTypeBoolean

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeBoolean: NSString! ``` |
| To | ``` let kCIAttributeTypeBoolean: String ``` |

Modified kCIAttributeTypeColor

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeColor: NSString! ``` |
| To | ``` let kCIAttributeTypeColor: String ``` |

Modified kCIAttributeTypeCount

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeCount: NSString! ``` |
| To | ``` let kCIAttributeTypeCount: String ``` |

Modified kCIAttributeTypeDistance

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeDistance: NSString! ``` |
| To | ``` let kCIAttributeTypeDistance: String ``` |

Modified kCIAttributeTypeImage

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeImage: NSString! ``` |
| To | ``` let kCIAttributeTypeImage: String ``` |

Modified kCIAttributeTypeInteger

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeInteger: NSString! ``` |
| To | ``` let kCIAttributeTypeInteger: String ``` |

Modified kCIAttributeTypeOffset

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeOffset: NSString! ``` |
| To | ``` let kCIAttributeTypeOffset: String ``` |

Modified kCIAttributeTypePosition

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypePosition: NSString! ``` |
| To | ``` let kCIAttributeTypePosition: String ``` |

Modified kCIAttributeTypePosition3

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypePosition3: NSString! ``` |
| To | ``` let kCIAttributeTypePosition3: String ``` |

Modified kCIAttributeTypeRectangle

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeRectangle: NSString! ``` |
| To | ``` let kCIAttributeTypeRectangle: String ``` |

Modified kCIAttributeTypeScalar

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeScalar: NSString! ``` |
| To | ``` let kCIAttributeTypeScalar: String ``` |

Modified kCIAttributeTypeTime

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeTime: NSString! ``` |
| To | ``` let kCIAttributeTypeTime: String ``` |

Modified kCIAttributeTypeTransform

|  | Declaration |
| --- | --- |
| From | ``` var kCIAttributeTypeTransform: NSString! ``` |
| To | ``` let kCIAttributeTypeTransform: String ``` |

Modified kCICategoryBlur

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryBlur: NSString! ``` |
| To | ``` let kCICategoryBlur: String ``` |

Modified kCICategoryBuiltIn

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryBuiltIn: NSString! ``` |
| To | ``` let kCICategoryBuiltIn: String ``` |

Modified kCICategoryColorAdjustment

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryColorAdjustment: NSString! ``` |
| To | ``` let kCICategoryColorAdjustment: String ``` |

Modified kCICategoryColorEffect

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryColorEffect: NSString! ``` |
| To | ``` let kCICategoryColorEffect: String ``` |

Modified kCICategoryCompositeOperation

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryCompositeOperation: NSString! ``` |
| To | ``` let kCICategoryCompositeOperation: String ``` |

Modified kCICategoryDistortionEffect

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryDistortionEffect: NSString! ``` |
| To | ``` let kCICategoryDistortionEffect: String ``` |

Modified kCICategoryGenerator

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryGenerator: NSString! ``` |
| To | ``` let kCICategoryGenerator: String ``` |

Modified kCICategoryGeometryAdjustment

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryGeometryAdjustment: NSString! ``` |
| To | ``` let kCICategoryGeometryAdjustment: String ``` |

Modified kCICategoryGradient

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryGradient: NSString! ``` |
| To | ``` let kCICategoryGradient: String ``` |

Modified kCICategoryHalftoneEffect

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryHalftoneEffect: NSString! ``` |
| To | ``` let kCICategoryHalftoneEffect: String ``` |

Modified kCICategoryHighDynamicRange

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryHighDynamicRange: NSString! ``` |
| To | ``` let kCICategoryHighDynamicRange: String ``` |

Modified kCICategoryInterlaced

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryInterlaced: NSString! ``` |
| To | ``` let kCICategoryInterlaced: String ``` |

Modified kCICategoryNonSquarePixels

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryNonSquarePixels: NSString! ``` |
| To | ``` let kCICategoryNonSquarePixels: String ``` |

Modified kCICategoryReduction

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryReduction: NSString! ``` |
| To | ``` let kCICategoryReduction: String ``` |

Modified kCICategorySharpen

|  | Declaration |
| --- | --- |
| From | ``` var kCICategorySharpen: NSString! ``` |
| To | ``` let kCICategorySharpen: String ``` |

Modified kCICategoryStillImage

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryStillImage: NSString! ``` |
| To | ``` let kCICategoryStillImage: String ``` |

Modified kCICategoryStylize

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryStylize: NSString! ``` |
| To | ``` let kCICategoryStylize: String ``` |

Modified kCICategoryTileEffect

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryTileEffect: NSString! ``` |
| To | ``` let kCICategoryTileEffect: String ``` |

Modified kCICategoryTransition

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryTransition: NSString! ``` |
| To | ``` let kCICategoryTransition: String ``` |

Modified kCICategoryVideo

|  | Declaration |
| --- | --- |
| From | ``` var kCICategoryVideo: NSString! ``` |
| To | ``` let kCICategoryVideo: String ``` |

Modified kCIContextOutputColorSpace

|  | Declaration |
| --- | --- |
| From | ``` let kCIContextOutputColorSpace: NSString! ``` |
| To | ``` let kCIContextOutputColorSpace: String ``` |

Modified kCIContextPriorityRequestLow

|  | Declaration |
| --- | --- |
| From | ``` let kCIContextPriorityRequestLow: NSString! ``` |
| To | ``` let kCIContextPriorityRequestLow: String ``` |

Modified kCIContextUseSoftwareRenderer

|  | Declaration |
| --- | --- |
| From | ``` let kCIContextUseSoftwareRenderer: NSString! ``` |
| To | ``` let kCIContextUseSoftwareRenderer: String ``` |

Modified kCIContextWorkingColorSpace

|  | Declaration |
| --- | --- |
| From | ``` let kCIContextWorkingColorSpace: NSString! ``` |
| To | ``` let kCIContextWorkingColorSpace: String ``` |

Modified kCIContextWorkingFormat

|  | Declaration |
| --- | --- |
| From | ``` let kCIContextWorkingFormat: NSString! ``` |
| To | ``` let kCIContextWorkingFormat: String ``` |

Modified kCIImageAutoAdjustCrop

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustCrop: NSString! ``` |
| To | ``` let kCIImageAutoAdjustCrop: String ``` |

Modified kCIImageAutoAdjustEnhance

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustEnhance: NSString! ``` |
| To | ``` let kCIImageAutoAdjustEnhance: String ``` |

Modified kCIImageAutoAdjustFeatures

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustFeatures: NSString! ``` |
| To | ``` let kCIImageAutoAdjustFeatures: String ``` |

Modified kCIImageAutoAdjustLevel

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustLevel: NSString! ``` |
| To | ``` let kCIImageAutoAdjustLevel: String ``` |

Modified kCIImageAutoAdjustRedEye

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageAutoAdjustRedEye: NSString! ``` |
| To | ``` let kCIImageAutoAdjustRedEye: String ``` |

Modified kCIImageColorSpace

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageColorSpace: NSString! ``` |
| To | ``` let kCIImageColorSpace: String ``` |

Modified kCIImageProperties

|  | Declaration |
| --- | --- |
| From | ``` var kCIImageProperties: NSString! ``` |
| To | ``` let kCIImageProperties: String ``` |

Modified kCIInputAngleKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputAngleKey: NSString! ``` |
| To | ``` let kCIInputAngleKey: String ``` |

Modified kCIInputAspectRatioKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputAspectRatioKey: NSString! ``` |
| To | ``` let kCIInputAspectRatioKey: String ``` |

Modified kCIInputBackgroundImageKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputBackgroundImageKey: NSString! ``` |
| To | ``` let kCIInputBackgroundImageKey: String ``` |

Modified kCIInputBrightnessKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputBrightnessKey: NSString! ``` |
| To | ``` let kCIInputBrightnessKey: String ``` |

Modified kCIInputCenterKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputCenterKey: NSString! ``` |
| To | ``` let kCIInputCenterKey: String ``` |

Modified kCIInputColorKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputColorKey: NSString! ``` |
| To | ``` let kCIInputColorKey: String ``` |

Modified kCIInputContrastKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputContrastKey: NSString! ``` |
| To | ``` let kCIInputContrastKey: String ``` |

Modified kCIInputEVKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputEVKey: NSString! ``` |
| To | ``` let kCIInputEVKey: String ``` |

Modified kCIInputExtentKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputExtentKey: NSString! ``` |
| To | ``` let kCIInputExtentKey: String ``` |

Modified kCIInputImageKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputImageKey: NSString! ``` |
| To | ``` let kCIInputImageKey: String ``` |

Modified kCIInputIntensityKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputIntensityKey: NSString! ``` |
| To | ``` let kCIInputIntensityKey: String ``` |

Modified kCIInputMaskImageKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputMaskImageKey: NSString! ``` |
| To | ``` let kCIInputMaskImageKey: String ``` |

Modified kCIInputRadiusKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputRadiusKey: NSString! ``` |
| To | ``` let kCIInputRadiusKey: String ``` |

Modified kCIInputSaturationKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputSaturationKey: NSString! ``` |
| To | ``` let kCIInputSaturationKey: String ``` |

Modified kCIInputScaleKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputScaleKey: NSString! ``` |
| To | ``` let kCIInputScaleKey: String ``` |

Modified kCIInputSharpnessKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputSharpnessKey: NSString! ``` |
| To | ``` let kCIInputSharpnessKey: String ``` |

Modified kCIInputTargetImageKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputTargetImageKey: NSString! ``` |
| To | ``` let kCIInputTargetImageKey: String ``` |

Modified kCIInputTimeKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputTimeKey: NSString! ``` |
| To | ``` let kCIInputTimeKey: String ``` |

Modified kCIInputTransformKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputTransformKey: NSString! ``` |
| To | ``` let kCIInputTransformKey: String ``` |

Modified kCIInputVersionKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputVersionKey: NSString! ``` |
| To | ``` let kCIInputVersionKey: String ``` |

Modified kCIInputWidthKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIInputWidthKey: NSString! ``` |
| To | ``` let kCIInputWidthKey: String ``` |

Modified kCIOutputImageKey

|  | Declaration |
| --- | --- |
| From | ``` var kCIOutputImageKey: NSString! ``` |
| To | ``` let kCIOutputImageKey: String ``` |

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
