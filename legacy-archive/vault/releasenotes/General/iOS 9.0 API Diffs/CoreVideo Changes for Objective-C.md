---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreVideo.html
archived_at: '2026-07-18T02:56:32.640971Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreVideo Changes for Objective-C

### CoreVideo

#### CVBase.h

Added #def COREVIDEO_DECLARE_NULLABILITYAdded #def COREVIDEO_USE_DERIVED_ENUMS_FOR_CONSTANTSAdded #def CV_BRIDGED_TYPEAdded #def CV_NONNULLAdded #def CV_NULLABLEAdded #def CV_RELEASES_ARGUMENTAdded #def CV_RETURNS_RETAINED_PARAMETER

#### CVImageBuffer.h

Added [kCVImageBufferColorPrimaries_DCI_P3](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_dci_p3)Added [kCVImageBufferColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_itu_r_2020)Added [kCVImageBufferColorPrimaries_P3_D65](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_p3_d65)Added [kCVImageBufferTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_itu_r_2020)Added [kCVImageBufferYCbCrMatrix_DCI_P3](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_dci_p3)Added [kCVImageBufferYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_itu_r_2020)Added [kCVImageBufferYCbCrMatrix_P3_D65](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_p3_d65)

#### CVPixelBuffer.h

Removed CVPixelBufferLockFlagsAdded [CVPixelBufferLockFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Added [kCVPixelBufferOpenGLESTextureCacheCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglestexturecachecompatibilitykey)Modified [CVPixelBufferLockBaseAddress()](https://developer.apple.com/documentation/corevideo/1457128-cvpixelbufferlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferLockBaseAddress (     CVPixelBufferRef pixelBuffer,     CVOptionFlags lockFlags ); ``` |
| To | ``` CVReturn CVPixelBufferLockBaseAddress (     CVPixelBufferRef _Nonnull pixelBuffer,     CVPixelBufferLockFlags lockFlags ); ``` |

Modified [CVPixelBufferUnlockBaseAddress()](https://developer.apple.com/documentation/corevideo/1456843-cvpixelbufferunlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` CVReturn CVPixelBufferUnlockBaseAddress (     CVPixelBufferRef pixelBuffer,     CVOptionFlags unlockFlags ); ``` |
| To | ``` CVReturn CVPixelBufferUnlockBaseAddress (     CVPixelBufferRef _Nonnull pixelBuffer,     CVPixelBufferLockFlags unlockFlags ); ``` |

#### CVPixelBufferPool.h

Added [CVPixelBufferPoolFlush()](https://developer.apple.com/documentation/corevideo/1457177-cvpixelbufferpoolflush)Added [CVPixelBufferPoolFlushFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)Added [kCVPixelBufferPoolFlushExcessBuffers](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/kcvpixelbufferpoolflushexcessbuffers)

#### CVPixelFormatDescription.h

Added [kCVPixelFormatComponentRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange)Added [kCVPixelFormatComponentRange_FullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_fullrange)Added [kCVPixelFormatComponentRange_VideoRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_videorange)Added [kCVPixelFormatComponentRange_WideRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_widerange)

#### CVReturn.h

Added [kCVReturnUnsupported](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnunsupported)

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
