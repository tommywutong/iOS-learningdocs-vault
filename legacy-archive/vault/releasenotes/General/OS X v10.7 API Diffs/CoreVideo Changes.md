---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/CoreVideo.html
archived_at: '2026-07-18T02:54:27.519627Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# CoreVideo Changes

## CoreVideo

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CVBase.hAdded #def COREVIDEO_SUPPORTS_DIRECT3DCVImageBuffer.hModified [kCVImageBufferTransferFunction_EBU_3213](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_ebu_3213)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [kCVImageBufferTransferFunction_SMPTE_C](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_smpte_c)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

CVPixelBuffer.hAdded [CVPlanarPixelBufferInfo_YCbCrBiPlanar](https://developer.apple.com/documentation/corevideo/cvplanarpixelbufferinfo_ycbcrbiplanar)Added [kCVPixelFormatType_30RGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_30rgb)Added [kCVPixelFormatType_420YpCbCr8BiPlanarFullRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8biplanarfullrange)Added [kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8biplanarvideorange)Added [kCVPixelFormatType_420YpCbCr8PlanarFullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_420ypcbcr8planarfullrange)Added [kCVPixelFormatType_422YpCbCr8FullRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_422ypcbcr8fullrange)Added [kCVPixelFormatType_422YpCbCr8_yuvs](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr8_yuvs)Added [kCVPixelFormatType_4444AYpCbCr16](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_4444aypcbcr16)Added [kCVPixelFormatType_4444AYpCbCr8](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_4444aypcbcr8)CVPixelBufferIOSurface.hModified [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfacecoreanimationcompatibilitykey)

|  | Header |
| --- | --- |
| From | CVPixelBuffer.h |
| To | CVPixelBufferIOSurface.h |

Modified [kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfaceopengltexturecompatibilitykey)

|  | Header |
| --- | --- |
| From | CVPixelBuffer.h |
| To | CVPixelBufferIOSurface.h |

Modified [kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfaceopenglfbocompatibilitykey)

|  | Header |
| --- | --- |
| From | CVPixelBuffer.h |
| To | CVPixelBufferIOSurface.h |

Modified [CVPixelBufferGetIOSurface()](https://developer.apple.com/documentation/corevideo/1456690-cvpixelbuffergetiosurface)

|  | Header |
| --- | --- |
| From | CVPixelBuffer.h |
| To | CVPixelBufferIOSurface.h |

Modified [CVPixelBufferCreateWithIOSurface()](https://developer.apple.com/documentation/corevideo/1456968-cvpixelbuffercreatewithiosurface)

|  | Header |
| --- | --- |
| From | CVPixelBuffer.h |
| To | CVPixelBufferIOSurface.h |

CVPixelBufferPool.hAdded [CVPixelBufferPoolCreatePixelBufferWithAuxAttributes()](https://developer.apple.com/documentation/corevideo/1456899-cvpixelbufferpoolcreatepixelbuff)Added [kCVPixelBufferPoolAllocationThresholdKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolallocationthresholdkey)Added [kCVPixelBufferPoolFreeBufferNotification](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolfreebuffernotification)CVPixelFormatDescription.hAdded [kCVPixelFormatContainsAlpha](https://developer.apple.com/documentation/corevideo/kcvpixelformatcontainsalpha)Added kCVPixelFormatDirect3DCompatibility (no architecture available)Added kCVPixelFormatDirect3DFormat (no architecture available)Added kCVPixelFormatDirect3DInternalFormat (no architecture available)Added kCVPixelFormatDirect3DType (no architecture available)CVReturn.hAdded [kCVReturnWouldExceedAllocationThreshold](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnwouldexceedallocationthreshold)

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
