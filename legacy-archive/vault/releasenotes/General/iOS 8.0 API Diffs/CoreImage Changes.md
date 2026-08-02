---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/CoreImage.html
archived_at: '2026-07-18T02:55:56.545062Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# CoreImage Changes

## CoreImage

CIContext.hAdded [kCIContextPriorityRequestLow](https://developer.apple.com/documentation/coreimage/kcicontextpriorityrequestlow)Added [kCIContextWorkingFormat](https://developer.apple.com/documentation/coreimage/cicontextoption/1437788-workingformat)CIDetector.hAdded [CIDetectorAspectRatio](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)Added [CIDetectorFocalLength](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)Added [CIDetectorTypeQRCode](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)Added [CIDetectorTypeRectangle](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)CIFeature.hAdded [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)Added [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)Added [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)Added [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)Added [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)Added [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)Added [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)Added [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)Added [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)Added [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)Added [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)Added [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)Added [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)CIFilter.hAdded [+[CIFilter filterWithName:withInputParameters:]](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)CIImage.hAdded [-[CIImage imageByApplyingFilter:withInputParameters:]](https://developer.apple.com/documentation/coreimage/ciimage/1437589-applyingfilter)Added [-[CIImage imageByApplyingOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1438223-imagebyapplyingorientation)Added [-[CIImage imageByClampingToExtent]](https://developer.apple.com/documentation/coreimage/ciimage/1437628-clampedtoextent)Added [-[CIImage imageByCompositingOverImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437837-composited)Added [-[CIImage imageTransformForOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)Added [kCIFormatRGBAf](https://developer.apple.com/documentation/coreimage/kciformatrgbaf)Added [kCIImageAutoAdjustCrop](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438229-crop)Added [kCIImageAutoAdjustLevel](https://developer.apple.com/documentation/coreimage/kciimageautoadjustlevel)CIKernel.h (Added)Added [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel)Added [-[CIColorKernel applyWithExtent:arguments:]](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438110-applywithextent)Added [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)Added [-[CIKernel applyWithExtent:roiCallback:arguments:]](https://developer.apple.com/documentation/coreimage/cikernel/1438243-applywithextent)Added [+[CIKernel kernelWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)Added [+[CIKernel kernelsWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)Added [-[CIKernel name]](https://developer.apple.com/documentation/coreimage/cikernel/1438067-name)Added [CIWarpKernel](https://developer.apple.com/documentation/coreimage/ciwarpkernel)Added [-[CIWarpKernel applyWithExtent:roiCallback:inputImage:arguments:]](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1437798-apply)Added [CIKernelROICallback](https://developer.apple.com/documentation/coreimage/cikernelroicallback)

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
