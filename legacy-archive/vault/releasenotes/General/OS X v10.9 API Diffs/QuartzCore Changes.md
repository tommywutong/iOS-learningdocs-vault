---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/QuartzCore.html
archived_at: '2026-07-18T02:54:18.747058Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

CAEmitterBehavior.hAdded CAEmitterBehaviorAdded +[CAEmitterBehavior attributesForKey:]Added -[CAEmitterBehavior attributesForKeyPath:]Added +[CAEmitterBehavior behaviorTypes]Added +[CAEmitterBehavior behaviorWithType:]Added CAEmitterBehavior.enabledAdded -[CAEmitterBehavior initWithType:]Added -[CAEmitterBehavior inputKeys]Added CAEmitterBehavior.nameAdded CAEmitterBehavior.typeAdded kCAEmitterBehaviorAlignToMotionAdded kCAEmitterBehaviorAttractorAdded kCAEmitterBehaviorColorOverLifeAdded kCAEmitterBehaviorDragAdded kCAEmitterBehaviorLightAdded kCAEmitterBehaviorValueOverLifeAdded kCAEmitterBehaviorWaveCIDetector.hAdded [CIDetectorEyeBlink](https://developer.apple.com/documentation/coreimage/cidetectoreyeblink)Added [CIDetectorSmile](https://developer.apple.com/documentation/coreimage/cidetectorsmile)CIFeature.hAdded [CIFaceFeature.bounds](https://developer.apple.com/documentation/coreimage/cifacefeature/1438068-bounds)Added [CIFaceFeature.faceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1437689-faceangle)Added [CIFaceFeature.hasFaceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1438165-hasfaceangle)Added [CIFaceFeature.hasSmile](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)Added [CIFaceFeature.leftEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437630-lefteyeclosed)Added [CIFaceFeature.rightEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437615-righteyeclosed)CIFilter.hAdded [+[CIFilter filterArrayFromSerializedXMP:inputImageExtent:error:]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)Added [+[CIFilter serializedXMPFromFilters:inputImageExtent:]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)Added CIFilter(CIFilterXMPSerialization)CIImage.hAdded [+[CIImage imageWithTexture:size:flipped:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547000-imagewithtexture)Added [-[CIImage initWithIOSurface:plane:format:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437670-init)Added [-[CIImage initWithTexture:size:flipped:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437880-init)Added [kCIImageTextureFormat](https://developer.apple.com/documentation/coreimage/kciimagetextureformat)Added [kCIImageTextureTarget](https://developer.apple.com/documentation/coreimage/kciimagetexturetarget)CIVector.hAdded [-[CIVector CGAffineTransformValue]](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)Added [-[CIVector CGPointValue]](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)Added [-[CIVector CGRectValue]](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)Added [-[CIVector initWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)Added [-[CIVector initWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1438133-initwithcgpoint)Added [-[CIVector initWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1437644-init)Added [+[CIVector vectorWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1564090-vectorwithcgaffinetransform)Added [+[CIVector vectorWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1564086-vectorwithcgpoint)Added [+[CIVector vectorWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1564085-vectorwithcgrect)

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
