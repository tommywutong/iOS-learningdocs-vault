---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/VideoToolbox.html
archived_at: '2026-07-18T02:56:38.234747Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# VideoToolbox Changes for Objective-C

### VideoToolbox

#### VTCompressionSession.h

Added [VTCompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputhandler)Added [VTCompressionSessionEncodeFrameWithOutputHandler()](https://developer.apple.com/documentation/videotoolbox/1428281-vtcompressionsessionencodeframew)

#### VTDecompressionSession.h

Added [VTDecompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputhandler)Added [VTDecompressionSessionDecodeFrameWithOutputHandler()](https://developer.apple.com/documentation/videotoolbox/1536067-vtdecompressionsessiondecodefram)

#### VTPixelTransferProperties.h (Added)

Added [kVTDownsamplingMode_Average](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_average)Added [kVTDownsamplingMode_Decimate](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_decimate)Added [kVTPixelTransferPropertyKey_DestinationCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationcleanaperture)Added [kVTPixelTransferPropertyKey_DestinationPixelAspectRatio](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationpixelaspectratio)Added [kVTPixelTransferPropertyKey_DestinationYCbCrMatrix](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationycbcrmatrix)Added [kVTPixelTransferPropertyKey_DownsamplingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_downsamplingmode)Added [kVTPixelTransferPropertyKey_ScalingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_scalingmode)Added [kVTScalingMode_CropSourceToCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_cropsourcetocleanaperture)Added [kVTScalingMode_Letterbox](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_letterbox)Added [kVTScalingMode_Normal](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_normal)Added [kVTScalingMode_Trim](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_trim)Added #def VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER

#### VTUtilities.h (Added)

Added [VTCreateCGImageFromCVPixelBuffer()](https://developer.apple.com/documentation/videotoolbox/1536089-vtcreatecgimagefromcvpixelbuffer)

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
