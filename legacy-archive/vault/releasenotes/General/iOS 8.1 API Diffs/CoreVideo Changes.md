---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreVideo.html
archived_at: '2026-07-18T02:56:11.044189Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreVideo Changes

## CoreVideo

Modified CVBufferGetAttachment(CVBuffer!, CFString!, UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferGetAttachments(CVBuffer!, CVAttachmentMode) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferPropagateAttachments(CVBuffer!, CVBuffer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferRemoveAllAttachments(CVBuffer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferRemoveAttachment(CVBuffer!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferSetAttachment(CVBuffer!, CFString!, AnyObject!, CVAttachmentMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVBufferSetAttachments(CVBuffer!, CFDictionary!, CVAttachmentMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVImageBufferGetCleanRect(CVImageBuffer!) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVImageBufferGetDisplaySize(CVImageBuffer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVImageBufferGetEncodedSize(CVImageBuffer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVImageBufferIsFlipped(CVImageBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVOpenGLESTextureCacheCreate(CFAllocator!, CFDictionary!, CVEAGLContext!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVOpenGLESTextureCache>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator!, CVOpenGLESTextureCache!, CVImageBuffer!, CFDictionary!, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, UInt, UnsafeMutablePointer<Unmanaged<CVOpenGLESTexture>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureCacheFlush(CVOpenGLESTextureCache!, CVOptionFlags)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureCacheGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureGetCleanTexCoords(CVOpenGLESTexture!, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureGetName(CVOpenGLESTexture!) -> GLuint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureGetTarget(CVOpenGLESTexture!) -> GLenum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVOpenGLESTextureIsFlipped(CVOpenGLESTexture!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CVPixelBufferCreate(CFAllocator!, UInt, UInt, OSType, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator!, CFArray!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferCreateWithBytes(CFAllocator!, UInt, UInt, OSType, UnsafeMutablePointer<Void>, UInt, CVPixelBufferReleaseBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferCreateWithPlanarBytes(CFAllocator!, UInt, UInt, OSType, UnsafeMutablePointer<Void>, UInt, UInt, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, CVPixelBufferReleasePlanarBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferFillExtendedPixels(CVPixelBuffer!) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetBaseAddress(CVPixelBuffer!) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer!, UInt) -> UnsafeMutablePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetBytesPerRow(CVPixelBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer!, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetDataSize(CVPixelBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetExtendedPixels(CVPixelBuffer!, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetHeight(CVPixelBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetHeightOfPlane(CVPixelBuffer!, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetPixelFormatType(CVPixelBuffer!) -> OSType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetPlaneCount(CVPixelBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetWidth(CVPixelBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferGetWidthOfPlane(CVPixelBuffer!, UInt) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferIsPlanar(CVPixelBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferLockBaseAddress(CVPixelBuffer!, CVOptionFlags) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolCreate(CFAllocator!, CFDictionary!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBufferPool>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolCreatePixelBuffer(CFAllocator!, CVPixelBufferPool!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(CFAllocator!, CVPixelBufferPool!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolGetAttributes(CVPixelBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferPoolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelBufferUnlockBaseAddress(CVPixelBuffer!, CVOptionFlags) -> CVReturn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(CFAllocator!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelFormatDescriptionCreateWithPixelFormatType(CFAllocator!, OSType) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(CFDictionary!, OSType)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVBufferMovieTimeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVBufferNonPropagatedAttachmentsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVBufferPropagatedAttachmentsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVBufferTimeScaleKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVBufferTimeValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCGColorSpaceKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocationBottomFieldKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocationTopFieldKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_Bottom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_BottomLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_Center

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_DV420

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_Left

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_Top

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaLocation_TopLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaSubsamplingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaSubsampling_411

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaSubsampling_420

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferChromaSubsampling_422

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCleanApertureHeightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCleanApertureHorizontalOffsetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCleanApertureKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCleanApertureVerticalOffsetKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferCleanApertureWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferColorPrimariesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferColorPrimaries_EBU_3213

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferColorPrimaries_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferColorPrimaries_P22

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCVImageBufferColorPrimaries_SMPTE_C

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferDisplayDimensionsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferDisplayHeightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferDisplayWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldDetailKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldDetailSpatialFirstLineEarly

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldDetailSpatialFirstLineLate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldDetailTemporalBottomFirst

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferFieldDetailTemporalTopFirst

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferGammaLevelKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferICCProfileKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferPixelAspectRatioHorizontalSpacingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferPixelAspectRatioKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferPixelAspectRatioVerticalSpacingKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferPreferredCleanApertureKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferTransferFunctionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferTransferFunction_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferTransferFunction_SMPTE_240M_1995

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferTransferFunction_UseGamma

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferYCbCrMatrixKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferYCbCrMatrix_ITU_R_601_4

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferYCbCrMatrix_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVImageBufferYCbCrMatrix_SMPTE_240M_1995

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVOpenGLESTextureCacheMaximumTextureAgeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCVPixelBufferBytesPerRowAlignmentKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferCGBitmapContextCompatibilityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferCGImageCompatibilityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferExtendedPixelsBottomKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferExtendedPixelsLeftKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferExtendedPixelsRightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferExtendedPixelsTopKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferHeightKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferIOSurfacePropertiesKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferMemoryAllocatorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferOpenGLCompatibilityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferOpenGLESCompatibilityKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCVPixelBufferPixelFormatTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferPlaneAlignmentKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferPoolAllocationThresholdKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferPoolFreeBufferNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferPoolMaximumBufferAgeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferPoolMinimumBufferCountKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelBufferWidthKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBitsPerBlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBlackBlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBlockHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBlockHorizontalAlignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBlockVerticalAlignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatBlockWidth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatCGBitmapContextCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatCGBitmapInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatCGImageCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatCodecType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatConstant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatContainsAlpha

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCVPixelFormatFillExtendedPixelsCallback

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatFourCC

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatHorizontalSubsampling

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatOpenGLCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatOpenGLESCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCVPixelFormatOpenGLFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatOpenGLInternalFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatOpenGLType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatPlanes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatQDCompatibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCVPixelFormatVerticalSubsampling

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
