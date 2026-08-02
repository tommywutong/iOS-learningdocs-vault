---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/QuartzCore.html
archived_at: '2026-07-18T02:54:06.136515Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

CABase.hRemoved #def CGFLOAT_DEFINEDRemoved [#def CGFLOAT_IS_DOUBLE](https://developer.apple.com/documentation/coregraphics/cgfloat_is_double)Removed [#def CGFLOAT_MAX](https://developer.apple.com/documentation/coregraphics/cgfloat_max)Removed [#def CGFLOAT_MIN](https://developer.apple.com/documentation/coregraphics/cgfloat_min)Removed [CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat) (no architecture available)CALayer.hAdded [CALayer.drawsAsynchronously](https://developer.apple.com/documentation/quartzcore/calayer/1410974-drawsasynchronously)CIContext.hModified [-[CIContext drawImage:atPoint:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

CIDetector.hAdded [-[CIDetector featuresInImage:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)Added [CIDetectorImageOrientation](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)Added [CIDetectorMinFeatureSize](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)Added [CIDetectorTracking](https://developer.apple.com/documentation/coreimage/cidetectortracking)CIFeature.hAdded [CIFaceFeature.hasTrackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437731-hastrackingframecount)Added [CIFaceFeature.hasTrackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437683-hastrackingid)Added [CIFaceFeature.trackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437953-trackingframecount)Added [CIFaceFeature.trackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437709-trackingid)CIImage.hAdded [-[CIImage autoAdjustmentFilters]](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Added [-[CIImage autoAdjustmentFiltersWithOptions:]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilters)Added [-[CIImage properties]](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)Added CIImage(AutoAdjustment)

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
