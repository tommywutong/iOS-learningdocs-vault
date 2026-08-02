---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreVideo.html
archived_at: '2026-07-18T02:56:47.607204Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreVideo Changes for Swift

### CoreVideo

Removed CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack, refCon: UnsafeMutablePointer<Void>)Removed [CVPixelBufferLockFlags [struct]](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Removed CVPixelBufferLockFlags.init(_: UInt32)Removed CVPixelBufferLockFlags.valueAdded CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack?, refCon: UnsafeMutablePointer<Void>)Added COREVIDEO_DECLARE_NULLABILITYAdded [CVPixelBufferLockFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Added [CVPixelBufferPoolFlush(_: CVPixelBufferPool, _: CVPixelBufferPoolFlushFlags)](https://developer.apple.com/documentation/corevideo/1457177-cvpixelbufferpoolflush)Added [CVPixelBufferPoolFlushFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)Added [kCVImageBufferColorPrimaries_DCI_P3](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_dci_p3)Added [kCVImageBufferColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_itu_r_2020)Added [kCVImageBufferColorPrimaries_P3_D65](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_p3_d65)Added [kCVImageBufferTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_itu_r_2020)Added [kCVImageBufferYCbCrMatrix_DCI_P3](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_dci_p3)Added [kCVImageBufferYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_itu_r_2020)Added [kCVImageBufferYCbCrMatrix_P3_D65](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_p3_d65)Added [kCVPixelBufferOpenGLESTextureCacheCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglestexturecachecompatibilitykey)Added [kCVPixelBufferPoolFlushExcessBuffers](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/1456664-excessbuffers)Added [kCVPixelFormatComponentRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange)Added [kCVPixelFormatComponentRange_FullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_fullrange)Added [kCVPixelFormatComponentRange_VideoRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_videorange)Added [kCVPixelFormatComponentRange_WideRange](https://developer.apple.com/documentation/corevideo/kcvpixelformatcomponentrange_widerange)Added [kCVReturnUnsupported](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnunsupported)Modified [CVFillExtendedPixelsCallBackData [struct]](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata)

|  | Declaration |
| --- | --- |
| From | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: CFIndex, fillCallBack fillCallBack: CVFillExtendedPixelsCallBack, refCon refCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack?     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: CFIndex, fillCallBack fillCallBack: CVFillExtendedPixelsCallBack?, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

Modified [CVFillExtendedPixelsCallBackData.fillCallBack](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/1456760-fillcallback)

|  | Declaration |
| --- | --- |
| From | ``` var fillCallBack: CVFillExtendedPixelsCallBack ``` |
| To | ``` var fillCallBack: CVFillExtendedPixelsCallBack? ``` |

Modified [CVBufferGetAttachment(_: CVBuffer, _: CFString, _: UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>?](https://developer.apple.com/documentation/corevideo/1457103-cvbuffergetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferGetAttachment(_ buffer: CVBuffer!, _ key: CFString!, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func CVBufferGetAttachment(_ buffer: CVBuffer, _ key: CFString, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>? ``` |

Modified [CVBufferGetAttachments(_: CVBuffer, _: CVAttachmentMode) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/corevideo/1457272-cvbuffergetattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferGetAttachments(_ buffer: CVBuffer!, _ attachmentMode: CVAttachmentMode) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CVBufferGetAttachments(_ buffer: CVBuffer, _ attachmentMode: CVAttachmentMode) -> Unmanaged<CFDictionary>? ``` |

Modified [CVBufferPropagateAttachments(_: CVBuffer, _: CVBuffer)](https://developer.apple.com/documentation/corevideo/1457132-cvbufferpropagateattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferPropagateAttachments(_ sourceBuffer: CVBuffer!, _ destinationBuffer: CVBuffer!) ``` |
| To | ``` func CVBufferPropagateAttachments(_ sourceBuffer: CVBuffer, _ destinationBuffer: CVBuffer) ``` |

Modified [CVBufferRemoveAllAttachments(_: CVBuffer)](https://developer.apple.com/documentation/corevideo/1457268-cvbufferremoveallattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferRemoveAllAttachments(_ buffer: CVBuffer!) ``` |
| To | ``` func CVBufferRemoveAllAttachments(_ buffer: CVBuffer) ``` |

Modified [CVBufferRemoveAttachment(_: CVBuffer, _: CFString)](https://developer.apple.com/documentation/corevideo/1456862-cvbufferremoveattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferRemoveAttachment(_ buffer: CVBuffer!, _ key: CFString!) ``` |
| To | ``` func CVBufferRemoveAttachment(_ buffer: CVBuffer, _ key: CFString) ``` |

Modified [CVBufferSetAttachment(_: CVBuffer, _: CFString, _: AnyObject, _: CVAttachmentMode)](https://developer.apple.com/documentation/corevideo/1456974-cvbuffersetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferSetAttachment(_ buffer: CVBuffer!, _ key: CFString!, _ value: AnyObject!, _ attachmentMode: CVAttachmentMode) ``` |
| To | ``` func CVBufferSetAttachment(_ buffer: CVBuffer, _ key: CFString, _ value: AnyObject, _ attachmentMode: CVAttachmentMode) ``` |

Modified [CVBufferSetAttachments(_: CVBuffer, _: CFDictionary, _: CVAttachmentMode)](https://developer.apple.com/documentation/corevideo/1457076-cvbuffersetattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferSetAttachments(_ buffer: CVBuffer!, _ theAttachments: CFDictionary!, _ attachmentMode: CVAttachmentMode) ``` |
| To | ``` func CVBufferSetAttachments(_ buffer: CVBuffer, _ theAttachments: CFDictionary, _ attachmentMode: CVAttachmentMode) ``` |

Modified [CVFillExtendedPixelsCallBack](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVFillExtendedPixelsCallBack = CFunctionPointer<((CVPixelBuffer!, UnsafeMutablePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CVFillExtendedPixelsCallBack = (CVPixelBuffer, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |

Modified [CVImageBufferGetCleanRect(_: CVImageBuffer) -> CGRect](https://developer.apple.com/documentation/corevideo/1418328-cvimagebuffergetcleanrect)

|  | Declaration |
| --- | --- |
| From | ``` func CVImageBufferGetCleanRect(_ imageBuffer: CVImageBuffer!) -> CGRect ``` |
| To | ``` func CVImageBufferGetCleanRect(_ imageBuffer: CVImageBuffer) -> CGRect ``` |

Modified [CVImageBufferGetDisplaySize(_: CVImageBuffer) -> CGSize](https://developer.apple.com/documentation/corevideo/1418303-cvimagebuffergetdisplaysize)

|  | Declaration |
| --- | --- |
| From | ``` func CVImageBufferGetDisplaySize(_ imageBuffer: CVImageBuffer!) -> CGSize ``` |
| To | ``` func CVImageBufferGetDisplaySize(_ imageBuffer: CVImageBuffer) -> CGSize ``` |

Modified [CVImageBufferGetEncodedSize(_: CVImageBuffer) -> CGSize](https://developer.apple.com/documentation/corevideo/1418350-cvimagebuffergetencodedsize)

|  | Declaration |
| --- | --- |
| From | ``` func CVImageBufferGetEncodedSize(_ imageBuffer: CVImageBuffer!) -> CGSize ``` |
| To | ``` func CVImageBufferGetEncodedSize(_ imageBuffer: CVImageBuffer) -> CGSize ``` |

Modified [CVImageBufferIsFlipped(_: CVImageBuffer) -> Bool](https://developer.apple.com/documentation/corevideo/1418308-cvimagebufferisflipped)

|  | Declaration |
| --- | --- |
| From | ``` func CVImageBufferIsFlipped(_ imageBuffer: CVImageBuffer!) -> Boolean ``` |
| To | ``` func CVImageBufferIsFlipped(_ imageBuffer: CVImageBuffer) -> Bool ``` |

Modified [CVMetalTextureCacheCreate(_: CFAllocator?, _: CFDictionary?, _: MTLDevice, _: CFDictionary?, _: UnsafeMutablePointer<Unmanaged<CVMetalTextureCache>?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456774-cvmetaltexturecachecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheCreate(_ allocator: CFAllocator!, _ cacheAttributes: CFDictionary!, _ metalDevice: MTLDevice!, _ textureAttributes: CFDictionary!, _ cacheOut: UnsafeMutablePointer<Unmanaged<CVMetalTextureCache>?>) -> CVReturn ``` |
| To | ``` func CVMetalTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ metalDevice: MTLDevice, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<Unmanaged<CVMetalTextureCache>?>) -> CVReturn ``` |

Modified [CVMetalTextureCacheCreateTextureFromImage(_: CFAllocator?, _: CVMetalTextureCache, _: CVImageBuffer, _: CFDictionary?, _: MTLPixelFormat, _: Int, _: Int, _: Int, _: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456754-cvmetaltexturecachecreatetexture)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVMetalTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn ``` |
| To | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVMetalTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn ``` |

Modified [CVMetalTextureCacheFlush(_: CVMetalTextureCache, _: CVOptionFlags)](https://developer.apple.com/documentation/corevideo/1457001-cvmetaltexturecacheflush)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheFlush(_ textureCache: CVMetalTextureCache!, _ options: CVOptionFlags) ``` |
| To | ``` func CVMetalTextureCacheFlush(_ textureCache: CVMetalTextureCache, _ options: CVOptionFlags) ``` |

Modified [CVMetalTextureGetCleanTexCoords(_: CVMetalTexture, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<Float>, _: UnsafeMutablePointer<Float>)](https://developer.apple.com/documentation/corevideo/1457089-cvmetaltexturegetcleantexcoords)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureGetCleanTexCoords(_ image: CVMetalTexture!, _ lowerLeft: UnsafeMutablePointer<Float>, _ lowerRight: UnsafeMutablePointer<Float>, _ upperRight: UnsafeMutablePointer<Float>, _ upperLeft: UnsafeMutablePointer<Float>) ``` |
| To | ``` func CVMetalTextureGetCleanTexCoords(_ image: CVMetalTexture, _ lowerLeft: UnsafeMutablePointer<Float>, _ lowerRight: UnsafeMutablePointer<Float>, _ upperRight: UnsafeMutablePointer<Float>, _ upperLeft: UnsafeMutablePointer<Float>) ``` |

Modified [CVMetalTextureGetTexture(_: CVMetalTexture) -> MTLTexture?](https://developer.apple.com/documentation/corevideo/1456868-cvmetaltexturegettexture)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureGetTexture(_ image: CVMetalTexture!) -> MTLTexture! ``` |
| To | ``` func CVMetalTextureGetTexture(_ image: CVMetalTexture) -> MTLTexture? ``` |

Modified [CVMetalTextureIsFlipped(_: CVMetalTexture) -> Bool](https://developer.apple.com/documentation/corevideo/1456841-cvmetaltextureisflipped)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureIsFlipped(_ image: CVMetalTexture!) -> Boolean ``` |
| To | ``` func CVMetalTextureIsFlipped(_ image: CVMetalTexture) -> Bool ``` |

Modified [CVOpenGLESTextureCacheCreate(_: CFAllocator?, _: CFDictionary?, _: CVEAGLContext, _: CFDictionary?, _: UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1619858-cvopenglestexturecachecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureCacheCreate(_ allocator: CFAllocator!, _ cacheAttributes: CFDictionary!, _ eaglContext: CVEAGLContext!, _ textureAttributes: CFDictionary!, _ cacheOut: UnsafeMutablePointer<Unmanaged<CVOpenGLESTextureCache>?>) -> CVReturn ``` |
| To | ``` func CVOpenGLESTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ eaglContext: CVEAGLContext, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVOpenGLESTextureCache?>) -> CVReturn ``` |

Modified [CVOpenGLESTextureCacheCreateTextureFromImage(_: CFAllocator?, _: CVOpenGLESTextureCache, _: CVImageBuffer, _: CFDictionary?, _: GLenum, _: GLint, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: Int, _: UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1619860-cvopenglestexturecachecreatetext)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVOpenGLESTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ target: GLenum, _ internalFormat: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVOpenGLESTexture>?>) -> CVReturn ``` |
| To | ``` func CVOpenGLESTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVOpenGLESTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ target: GLenum, _ internalFormat: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<CVOpenGLESTexture?>) -> CVReturn ``` |

Modified [CVOpenGLESTextureCacheFlush(_: CVOpenGLESTextureCache, _: CVOptionFlags)](https://developer.apple.com/documentation/corevideo/1619857-cvopenglestexturecacheflush)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureCacheFlush(_ textureCache: CVOpenGLESTextureCache!, _ options: CVOptionFlags) ``` |
| To | ``` func CVOpenGLESTextureCacheFlush(_ textureCache: CVOpenGLESTextureCache, _ options: CVOptionFlags) ``` |

Modified [CVOpenGLESTextureGetCleanTexCoords(_: CVOpenGLESTexture, _: UnsafeMutablePointer<GLfloat>, _: UnsafeMutablePointer<GLfloat>, _: UnsafeMutablePointer<GLfloat>, _: UnsafeMutablePointer<GLfloat>)](https://developer.apple.com/documentation/corevideo/1621287-cvopenglestexturegetcleantexcoor)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture!, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>) ``` |

Modified [CVOpenGLESTextureGetName(_: CVOpenGLESTexture) -> GLuint](https://developer.apple.com/documentation/corevideo/1621290-cvopenglestexturegetname)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureGetName(_ image: CVOpenGLESTexture!) -> GLuint ``` |
| To | ``` func CVOpenGLESTextureGetName(_ image: CVOpenGLESTexture) -> GLuint ``` |

Modified [CVOpenGLESTextureGetTarget(_: CVOpenGLESTexture) -> GLenum](https://developer.apple.com/documentation/corevideo/1621289-cvopenglestexturegettarget)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureGetTarget(_ image: CVOpenGLESTexture!) -> GLenum ``` |
| To | ``` func CVOpenGLESTextureGetTarget(_ image: CVOpenGLESTexture) -> GLenum ``` |

Modified [CVOpenGLESTextureIsFlipped(_: CVOpenGLESTexture) -> Bool](https://developer.apple.com/documentation/corevideo/1621288-cvopenglestextureisflipped)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureIsFlipped(_ image: CVOpenGLESTexture!) -> Boolean ``` |
| To | ``` func CVOpenGLESTextureIsFlipped(_ image: CVOpenGLESTexture) -> Bool ``` |

Modified [CVPixelBufferCreate(_: CFAllocator?, _: Int, _: Int, _: OSType, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456758-cvpixelbuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreate(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreate(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferCreateResolvedAttributesDictionary(_: CFAllocator?, _: CFArray?, _: UnsafeMutablePointer<CFDictionary?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1457233-cvpixelbuffercreateresolvedattri)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateResolvedAttributesDictionary(_ allocator: CFAllocator!, _ attributes: CFArray!, _ resolvedDictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateResolvedAttributesDictionary(_ allocator: CFAllocator?, _ attributes: CFArray?, _ resolvedDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> CVReturn ``` |

Modified [CVPixelBufferCreateWithBytes(_: CFAllocator?, _: Int, _: Int, _: OSType, _: UnsafeMutablePointer<Void>, _: Int, _: CVPixelBufferReleaseBytesCallback?, _: UnsafeMutablePointer<Void>, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456979-cvpixelbuffercreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback?, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferCreateWithPlanarBytes(_: CFAllocator?, _: Int, _: Int, _: OSType, _: UnsafeMutablePointer<Void>, _: Int, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: CVPixelBufferReleasePlanarBytesCallback?, _: UnsafeMutablePointer<Void>, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456731-cvpixelbuffercreatewithplanarbyt)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<Int>, _ planeHeight: UnsafeMutablePointer<Int>, _ planeBytesPerRow: UnsafeMutablePointer<Int>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<Int>, _ planeHeight: UnsafeMutablePointer<Int>, _ planeBytesPerRow: UnsafeMutablePointer<Int>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback?, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferFillExtendedPixels(_: CVPixelBuffer) -> CVReturn](https://developer.apple.com/documentation/corevideo/1457265-cvpixelbufferfillextendedpixels)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferFillExtendedPixels(_ pixelBuffer: CVPixelBuffer!) -> CVReturn ``` |
| To | ``` func CVPixelBufferFillExtendedPixels(_ pixelBuffer: CVPixelBuffer) -> CVReturn ``` |

Modified [CVPixelBufferGetBaseAddress(_: CVPixelBuffer) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/corevideo/1457115-cvpixelbuffergetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer) -> UnsafeMutablePointer<Void> ``` |

Modified [CVPixelBufferGetBaseAddressOfPlane(_: CVPixelBuffer, _: Int) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/corevideo/1456821-cvpixelbuffergetbaseaddressofpla)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |

Modified [CVPixelBufferGetBytesPerRow(_: CVPixelBuffer) -> Int](https://developer.apple.com/documentation/corevideo/1456964-cvpixelbuffergetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |
| To | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer) -> Int ``` |

Modified [CVPixelBufferGetBytesPerRowOfPlane(_: CVPixelBuffer, _: Int) -> Int](https://developer.apple.com/documentation/corevideo/1456711-cvpixelbuffergetbytesperrowofpla)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |
| To | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> Int ``` |

Modified [CVPixelBufferGetDataSize(_: CVPixelBuffer) -> Int](https://developer.apple.com/documentation/corevideo/1457195-cvpixelbuffergetdatasize)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |
| To | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer) -> Int ``` |

Modified [CVPixelBufferGetExtendedPixels(_: CVPixelBuffer, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>)](https://developer.apple.com/documentation/corevideo/1457029-cvpixelbuffergetextendedpixels)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer!, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>, _ extraColumnsOnRight: UnsafeMutablePointer<Int>, _ extraRowsOnTop: UnsafeMutablePointer<Int>, _ extraRowsOnBottom: UnsafeMutablePointer<Int>) ``` |
| To | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>, _ extraColumnsOnRight: UnsafeMutablePointer<Int>, _ extraRowsOnTop: UnsafeMutablePointer<Int>, _ extraRowsOnBottom: UnsafeMutablePointer<Int>) ``` |

Modified [CVPixelBufferGetHeight(_: CVPixelBuffer) -> Int](https://developer.apple.com/documentation/corevideo/1456666-cvpixelbuffergetheight)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |
| To | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer) -> Int ``` |

Modified [CVPixelBufferGetHeightOfPlane(_: CVPixelBuffer, _: Int) -> Int](https://developer.apple.com/documentation/corevideo/1456698-cvpixelbuffergetheightofplane)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |
| To | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> Int ``` |

Modified [CVPixelBufferGetPixelFormatType(_: CVPixelBuffer) -> OSType](https://developer.apple.com/documentation/corevideo/1456851-cvpixelbuffergetpixelformattype)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetPixelFormatType(_ pixelBuffer: CVPixelBuffer!) -> OSType ``` |
| To | ``` func CVPixelBufferGetPixelFormatType(_ pixelBuffer: CVPixelBuffer) -> OSType ``` |

Modified [CVPixelBufferGetPlaneCount(_: CVPixelBuffer) -> Int](https://developer.apple.com/documentation/corevideo/1456976-cvpixelbuffergetplanecount)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |
| To | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer) -> Int ``` |

Modified [CVPixelBufferGetWidth(_: CVPixelBuffer) -> Int](https://developer.apple.com/documentation/corevideo/1457241-cvpixelbuffergetwidth)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |
| To | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer) -> Int ``` |

Modified [CVPixelBufferGetWidthOfPlane(_: CVPixelBuffer, _: Int) -> Int](https://developer.apple.com/documentation/corevideo/1456830-cvpixelbuffergetwidthofplane)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |
| To | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> Int ``` |

Modified [CVPixelBufferIsPlanar(_: CVPixelBuffer) -> Bool](https://developer.apple.com/documentation/corevideo/1456805-cvpixelbufferisplanar)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferIsPlanar(_ pixelBuffer: CVPixelBuffer!) -> Boolean ``` |
| To | ``` func CVPixelBufferIsPlanar(_ pixelBuffer: CVPixelBuffer) -> Bool ``` |

Modified [CVPixelBufferLockBaseAddress(_: CVPixelBuffer, _: CVPixelBufferLockFlags) -> CVReturn](https://developer.apple.com/documentation/corevideo/1457128-cvpixelbufferlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferLockBaseAddress(_ pixelBuffer: CVPixelBuffer!, _ lockFlags: CVOptionFlags) -> CVReturn ``` |
| To | ``` func CVPixelBufferLockBaseAddress(_ pixelBuffer: CVPixelBuffer, _ lockFlags: CVPixelBufferLockFlags) -> CVReturn ``` |

Modified [CVPixelBufferPoolCreate(_: CFAllocator?, _: CFDictionary?, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1457094-cvpixelbufferpoolcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolCreate(_ allocator: CFAllocator!, _ poolAttributes: CFDictionary!, _ pixelBufferAttributes: CFDictionary!, _ poolOut: UnsafeMutablePointer<Unmanaged<CVPixelBufferPool>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferPoolCreate(_ allocator: CFAllocator?, _ poolAttributes: CFDictionary?, _ pixelBufferAttributes: CFDictionary?, _ poolOut: UnsafeMutablePointer<CVPixelBufferPool?>) -> CVReturn ``` |

Modified [CVPixelBufferPoolCreatePixelBuffer(_: CFAllocator?, _: CVPixelBufferPool, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456992-cvpixelbufferpoolcreatepixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolCreatePixelBuffer(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferPoolCreatePixelBuffer(_ allocator: CFAllocator?, _ pixelBufferPool: CVPixelBufferPool, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_: CFAllocator?, _: CVPixelBufferPool, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456899-cvpixelbufferpoolcreatepixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ auxAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_ allocator: CFAllocator?, _ pixelBufferPool: CVPixelBufferPool, _ auxAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferPoolGetAttributes(_: CVPixelBufferPool) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/corevideo/1456983-cvpixelbufferpoolgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolGetAttributes(_ pool: CVPixelBufferPool!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CVPixelBufferPoolGetAttributes(_ pool: CVPixelBufferPool) -> Unmanaged<CFDictionary>? ``` |

Modified [CVPixelBufferPoolGetPixelBufferAttributes(_: CVPixelBufferPool) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/corevideo/1457222-cvpixelbufferpoolgetpixelbuffera)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolGetPixelBufferAttributes(_ pool: CVPixelBufferPool!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CVPixelBufferPoolGetPixelBufferAttributes(_ pool: CVPixelBufferPool) -> Unmanaged<CFDictionary>? ``` |

Modified [CVPixelBufferReleaseBytesCallback](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleasebytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleaseBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias CVPixelBufferReleaseBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void ``` |

Modified [CVPixelBufferReleasePlanarBytesCallback](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleaseplanarbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleasePlanarBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void)> ``` |
| To | ``` typealias CVPixelBufferReleasePlanarBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void ``` |

Modified [CVPixelBufferUnlockBaseAddress(_: CVPixelBuffer, _: CVPixelBufferLockFlags) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456843-cvpixelbufferunlockbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferUnlockBaseAddress(_ pixelBuffer: CVPixelBuffer!, _ unlockFlags: CVOptionFlags) -> CVReturn ``` |
| To | ``` func CVPixelBufferUnlockBaseAddress(_ pixelBuffer: CVPixelBuffer, _ unlockFlags: CVPixelBufferLockFlags) -> CVReturn ``` |

Modified [CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_: CFAllocator?) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/corevideo/1456798-cvpixelformatdescriptionarraycre)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_ allocator: CFAllocator!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_ allocator: CFAllocator?) -> Unmanaged<CFArray>? ``` |

Modified [CVPixelFormatDescriptionCreateWithPixelFormatType(_: CFAllocator?, _: OSType) -> Unmanaged<CFDictionary>?](https://developer.apple.com/documentation/corevideo/1456807-cvpixelformatdescriptioncreatewi)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelFormatDescriptionCreateWithPixelFormatType(_ allocator: CFAllocator!, _ pixelFormat: OSType) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CVPixelFormatDescriptionCreateWithPixelFormatType(_ allocator: CFAllocator?, _ pixelFormat: OSType) -> Unmanaged<CFDictionary>? ``` |

Modified [CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(_: CFDictionary, _: OSType)](https://developer.apple.com/documentation/corevideo/1456721-cvpixelformatdescriptionregister)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(_ description: CFDictionary!, _ pixelFormat: OSType) ``` |
| To | ``` func CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(_ description: CFDictionary, _ pixelFormat: OSType) ``` |

Modified [kCVAttachmentMode_ShouldNotPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/kcvattachmentmode_shouldnotpropagate)

|  | Declaration |
| --- | --- |
| From | ``` var kCVAttachmentMode_ShouldNotPropagate: Int { get } ``` |
| To | ``` var kCVAttachmentMode_ShouldNotPropagate: CVAttachmentMode { get } ``` |

Modified [kCVAttachmentMode_ShouldPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/kcvattachmentmode_shouldpropagate)

|  | Declaration |
| --- | --- |
| From | ``` var kCVAttachmentMode_ShouldPropagate: Int { get } ``` |
| To | ``` var kCVAttachmentMode_ShouldPropagate: CVAttachmentMode { get } ``` |

Modified [kCVBufferMovieTimeKey](https://developer.apple.com/documentation/corevideo/kcvbuffermovietimekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVBufferMovieTimeKey: CFString! ``` |
| To | ``` let kCVBufferMovieTimeKey: CFString ``` |

Modified [kCVBufferNonPropagatedAttachmentsKey](https://developer.apple.com/documentation/corevideo/kcvbuffernonpropagatedattachmentskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVBufferNonPropagatedAttachmentsKey: CFString! ``` |
| To | ``` let kCVBufferNonPropagatedAttachmentsKey: CFString ``` |

Modified [kCVBufferPropagatedAttachmentsKey](https://developer.apple.com/documentation/corevideo/kcvbufferpropagatedattachmentskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVBufferPropagatedAttachmentsKey: CFString! ``` |
| To | ``` let kCVBufferPropagatedAttachmentsKey: CFString ``` |

Modified [kCVBufferTimeScaleKey](https://developer.apple.com/documentation/corevideo/kcvbuffertimescalekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVBufferTimeScaleKey: CFString! ``` |
| To | ``` let kCVBufferTimeScaleKey: CFString ``` |

Modified [kCVBufferTimeValueKey](https://developer.apple.com/documentation/corevideo/kcvbuffertimevaluekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVBufferTimeValueKey: CFString! ``` |
| To | ``` let kCVBufferTimeValueKey: CFString ``` |

Modified [kCVImageBufferAlphaChannelIsOpaque](https://developer.apple.com/documentation/corevideo/kcvimagebufferalphachannelisopaque)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferAlphaChannelIsOpaque: CFString! ``` |
| To | ``` let kCVImageBufferAlphaChannelIsOpaque: CFString ``` |

Modified [kCVImageBufferCGColorSpaceKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercgcolorspacekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCGColorSpaceKey: CFString! ``` |
| To | ``` let kCVImageBufferCGColorSpaceKey: CFString ``` |

Modified [kCVImageBufferChromaLocation_Bottom](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_bottom)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_Bottom: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_Bottom: CFString ``` |

Modified [kCVImageBufferChromaLocation_BottomLeft](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_bottomleft)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_BottomLeft: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_BottomLeft: CFString ``` |

Modified [kCVImageBufferChromaLocation_Center](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_center)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_Center: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_Center: CFString ``` |

Modified [kCVImageBufferChromaLocation_DV420](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_dv420)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_DV420: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_DV420: CFString ``` |

Modified [kCVImageBufferChromaLocation_Left](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_left)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_Left: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_Left: CFString ``` |

Modified [kCVImageBufferChromaLocation_Top](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_top)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_Top: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_Top: CFString ``` |

Modified [kCVImageBufferChromaLocation_TopLeft](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocation_topleft)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocation_TopLeft: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocation_TopLeft: CFString ``` |

Modified [kCVImageBufferChromaLocationBottomFieldKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocationbottomfieldkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocationBottomFieldKey: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocationBottomFieldKey: CFString ``` |

Modified [kCVImageBufferChromaLocationTopFieldKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromalocationtopfieldkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaLocationTopFieldKey: CFString! ``` |
| To | ``` let kCVImageBufferChromaLocationTopFieldKey: CFString ``` |

Modified [kCVImageBufferChromaSubsampling_411](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsampling_411)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaSubsampling_411: CFString! ``` |
| To | ``` let kCVImageBufferChromaSubsampling_411: CFString ``` |

Modified [kCVImageBufferChromaSubsampling_420](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsampling_420)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaSubsampling_420: CFString! ``` |
| To | ``` let kCVImageBufferChromaSubsampling_420: CFString ``` |

Modified [kCVImageBufferChromaSubsampling_422](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsampling_422)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaSubsampling_422: CFString! ``` |
| To | ``` let kCVImageBufferChromaSubsampling_422: CFString ``` |

Modified [kCVImageBufferChromaSubsamplingKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferchromasubsamplingkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferChromaSubsamplingKey: CFString! ``` |
| To | ``` let kCVImageBufferChromaSubsamplingKey: CFString ``` |

Modified [kCVImageBufferCleanApertureHeightKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercleanapertureheightkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCleanApertureHeightKey: CFString! ``` |
| To | ``` let kCVImageBufferCleanApertureHeightKey: CFString ``` |

Modified [kCVImageBufferCleanApertureHorizontalOffsetKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercleanaperturehorizontaloffsetkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCleanApertureHorizontalOffsetKey: CFString! ``` |
| To | ``` let kCVImageBufferCleanApertureHorizontalOffsetKey: CFString ``` |

Modified [kCVImageBufferCleanApertureKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercleanaperturekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCleanApertureKey: CFString! ``` |
| To | ``` let kCVImageBufferCleanApertureKey: CFString ``` |

Modified [kCVImageBufferCleanApertureVerticalOffsetKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercleanapertureverticaloffsetkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCleanApertureVerticalOffsetKey: CFString! ``` |
| To | ``` let kCVImageBufferCleanApertureVerticalOffsetKey: CFString ``` |

Modified [kCVImageBufferCleanApertureWidthKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercleanaperturewidthkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferCleanApertureWidthKey: CFString! ``` |
| To | ``` let kCVImageBufferCleanApertureWidthKey: CFString ``` |

Modified [kCVImageBufferColorPrimaries_EBU_3213](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_ebu_3213)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferColorPrimaries_EBU_3213: CFString! ``` |
| To | ``` let kCVImageBufferColorPrimaries_EBU_3213: CFString ``` |

Modified [kCVImageBufferColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_itu_r_709_2)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferColorPrimaries_ITU_R_709_2: CFString! ``` |
| To | ``` let kCVImageBufferColorPrimaries_ITU_R_709_2: CFString ``` |

Modified [kCVImageBufferColorPrimaries_P22](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_p22)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferColorPrimaries_P22: CFString! ``` |
| To | ``` let kCVImageBufferColorPrimaries_P22: CFString ``` |

Modified [kCVImageBufferColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimaries_smpte_c)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferColorPrimaries_SMPTE_C: CFString! ``` |
| To | ``` let kCVImageBufferColorPrimaries_SMPTE_C: CFString ``` |

Modified [kCVImageBufferColorPrimariesKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffercolorprimarieskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferColorPrimariesKey: CFString! ``` |
| To | ``` let kCVImageBufferColorPrimariesKey: CFString ``` |

Modified [kCVImageBufferDisplayDimensionsKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaydimensionskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferDisplayDimensionsKey: CFString! ``` |
| To | ``` let kCVImageBufferDisplayDimensionsKey: CFString ``` |

Modified [kCVImageBufferDisplayHeightKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplayheightkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferDisplayHeightKey: CFString! ``` |
| To | ``` let kCVImageBufferDisplayHeightKey: CFString ``` |

Modified [kCVImageBufferDisplayWidthKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaywidthkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferDisplayWidthKey: CFString! ``` |
| To | ``` let kCVImageBufferDisplayWidthKey: CFString ``` |

Modified [kCVImageBufferFieldCountKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferfieldcountkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldCountKey: CFString! ``` |
| To | ``` let kCVImageBufferFieldCountKey: CFString ``` |

Modified [kCVImageBufferFieldDetailKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferfielddetailkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldDetailKey: CFString! ``` |
| To | ``` let kCVImageBufferFieldDetailKey: CFString ``` |

Modified [kCVImageBufferFieldDetailSpatialFirstLineEarly](https://developer.apple.com/documentation/corevideo/kcvimagebufferfielddetailspatialfirstlineearly)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldDetailSpatialFirstLineEarly: CFString! ``` |
| To | ``` let kCVImageBufferFieldDetailSpatialFirstLineEarly: CFString ``` |

Modified [kCVImageBufferFieldDetailSpatialFirstLineLate](https://developer.apple.com/documentation/corevideo/kcvimagebufferfielddetailspatialfirstlinelate)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldDetailSpatialFirstLineLate: CFString! ``` |
| To | ``` let kCVImageBufferFieldDetailSpatialFirstLineLate: CFString ``` |

Modified [kCVImageBufferFieldDetailTemporalBottomFirst](https://developer.apple.com/documentation/corevideo/kcvimagebufferfielddetailtemporalbottomfirst)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldDetailTemporalBottomFirst: CFString! ``` |
| To | ``` let kCVImageBufferFieldDetailTemporalBottomFirst: CFString ``` |

Modified [kCVImageBufferFieldDetailTemporalTopFirst](https://developer.apple.com/documentation/corevideo/kcvimagebufferfielddetailtemporaltopfirst)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferFieldDetailTemporalTopFirst: CFString! ``` |
| To | ``` let kCVImageBufferFieldDetailTemporalTopFirst: CFString ``` |

Modified [kCVImageBufferGammaLevelKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffergammalevelkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferGammaLevelKey: CFString! ``` |
| To | ``` let kCVImageBufferGammaLevelKey: CFString ``` |

Modified [kCVImageBufferICCProfileKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffericcprofilekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferICCProfileKey: CFString! ``` |
| To | ``` let kCVImageBufferICCProfileKey: CFString ``` |

Modified [kCVImageBufferPixelAspectRatioHorizontalSpacingKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpixelaspectratiohorizontalspacingkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferPixelAspectRatioHorizontalSpacingKey: CFString! ``` |
| To | ``` let kCVImageBufferPixelAspectRatioHorizontalSpacingKey: CFString ``` |

Modified [kCVImageBufferPixelAspectRatioKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpixelaspectratiokey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferPixelAspectRatioKey: CFString! ``` |
| To | ``` let kCVImageBufferPixelAspectRatioKey: CFString ``` |

Modified [kCVImageBufferPixelAspectRatioVerticalSpacingKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpixelaspectratioverticalspacingkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferPixelAspectRatioVerticalSpacingKey: CFString! ``` |
| To | ``` let kCVImageBufferPixelAspectRatioVerticalSpacingKey: CFString ``` |

Modified [kCVImageBufferPreferredCleanApertureKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpreferredcleanaperturekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferPreferredCleanApertureKey: CFString! ``` |
| To | ``` let kCVImageBufferPreferredCleanApertureKey: CFString ``` |

Modified [kCVImageBufferTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_itu_r_709_2)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferTransferFunction_ITU_R_709_2: CFString! ``` |
| To | ``` let kCVImageBufferTransferFunction_ITU_R_709_2: CFString ``` |

Modified [kCVImageBufferTransferFunction_SMPTE_240M_1995](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_smpte_240m_1995)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferTransferFunction_SMPTE_240M_1995: CFString! ``` |
| To | ``` let kCVImageBufferTransferFunction_SMPTE_240M_1995: CFString ``` |

Modified [kCVImageBufferTransferFunction_UseGamma](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_usegamma)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferTransferFunction_UseGamma: CFString! ``` |
| To | ``` let kCVImageBufferTransferFunction_UseGamma: CFString ``` |

Modified [kCVImageBufferTransferFunctionKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunctionkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferTransferFunctionKey: CFString! ``` |
| To | ``` let kCVImageBufferTransferFunctionKey: CFString ``` |

Modified [kCVImageBufferYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_itu_r_601_4)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferYCbCrMatrix_ITU_R_601_4: CFString! ``` |
| To | ``` let kCVImageBufferYCbCrMatrix_ITU_R_601_4: CFString ``` |

Modified [kCVImageBufferYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_itu_r_709_2)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferYCbCrMatrix_ITU_R_709_2: CFString! ``` |
| To | ``` let kCVImageBufferYCbCrMatrix_ITU_R_709_2: CFString ``` |

Modified [kCVImageBufferYCbCrMatrix_SMPTE_240M_1995](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrix_smpte_240m_1995)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferYCbCrMatrix_SMPTE_240M_1995: CFString! ``` |
| To | ``` let kCVImageBufferYCbCrMatrix_SMPTE_240M_1995: CFString ``` |

Modified [kCVImageBufferYCbCrMatrixKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferycbcrmatrixkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVImageBufferYCbCrMatrixKey: CFString! ``` |
| To | ``` let kCVImageBufferYCbCrMatrixKey: CFString ``` |

Modified [kCVMetalTextureCacheMaximumTextureAgeKey](https://developer.apple.com/documentation/corevideo/kcvmetaltexturecachemaximumtextureagekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVMetalTextureCacheMaximumTextureAgeKey: CFString! ``` |
| To | ``` let kCVMetalTextureCacheMaximumTextureAgeKey: CFString ``` |

Modified [kCVOpenGLESTextureCacheMaximumTextureAgeKey](https://developer.apple.com/documentation/corevideo/kcvopenglestexturecachemaximumtextureagekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVOpenGLESTextureCacheMaximumTextureAgeKey: CFString! ``` |
| To | ``` let kCVOpenGLESTextureCacheMaximumTextureAgeKey: CFString ``` |

Modified [kCVPixelBufferBytesPerRowAlignmentKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferbytesperrowalignmentkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferBytesPerRowAlignmentKey: CFString! ``` |
| To | ``` let kCVPixelBufferBytesPerRowAlignmentKey: CFString ``` |

Modified [kCVPixelBufferCGBitmapContextCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbuffercgbitmapcontextcompatibilitykey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferCGBitmapContextCompatibilityKey: CFString! ``` |
| To | ``` let kCVPixelBufferCGBitmapContextCompatibilityKey: CFString ``` |

Modified [kCVPixelBufferCGImageCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbuffercgimagecompatibilitykey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferCGImageCompatibilityKey: CFString! ``` |
| To | ``` let kCVPixelBufferCGImageCompatibilityKey: CFString ``` |

Modified [kCVPixelBufferExtendedPixelsBottomKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferextendedpixelsbottomkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferExtendedPixelsBottomKey: CFString! ``` |
| To | ``` let kCVPixelBufferExtendedPixelsBottomKey: CFString ``` |

Modified [kCVPixelBufferExtendedPixelsLeftKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferextendedpixelsleftkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferExtendedPixelsLeftKey: CFString! ``` |
| To | ``` let kCVPixelBufferExtendedPixelsLeftKey: CFString ``` |

Modified [kCVPixelBufferExtendedPixelsRightKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferextendedpixelsrightkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferExtendedPixelsRightKey: CFString! ``` |
| To | ``` let kCVPixelBufferExtendedPixelsRightKey: CFString ``` |

Modified [kCVPixelBufferExtendedPixelsTopKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferextendedpixelstopkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferExtendedPixelsTopKey: CFString! ``` |
| To | ``` let kCVPixelBufferExtendedPixelsTopKey: CFString ``` |

Modified [kCVPixelBufferHeightKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferheightkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferHeightKey: CFString! ``` |
| To | ``` let kCVPixelBufferHeightKey: CFString ``` |

Modified [kCVPixelBufferIOSurfacePropertiesKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfacepropertieskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferIOSurfacePropertiesKey: CFString! ``` |
| To | ``` let kCVPixelBufferIOSurfacePropertiesKey: CFString ``` |

Modified [kCVPixelBufferLock_ReadOnly](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags/1457186-readonly)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [kCVPixelBufferMemoryAllocatorKey](https://developer.apple.com/documentation/corevideo/kcvpixelbuffermemoryallocatorkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferMemoryAllocatorKey: CFString! ``` |
| To | ``` let kCVPixelBufferMemoryAllocatorKey: CFString ``` |

Modified [kCVPixelBufferMetalCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbuffermetalcompatibilitykey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferMetalCompatibilityKey: CFString! ``` |
| To | ``` let kCVPixelBufferMetalCompatibilityKey: CFString ``` |

Modified [kCVPixelBufferOpenGLCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglcompatibilitykey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferOpenGLCompatibilityKey: CFString! ``` |
| To | ``` let kCVPixelBufferOpenGLCompatibilityKey: CFString ``` |

Modified [kCVPixelBufferOpenGLESCompatibilityKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferopenglescompatibilitykey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferOpenGLESCompatibilityKey: CFString! ``` |
| To | ``` let kCVPixelBufferOpenGLESCompatibilityKey: CFString ``` |

Modified [kCVPixelBufferPixelFormatTypeKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpixelformattypekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPixelFormatTypeKey: CFString! ``` |
| To | ``` let kCVPixelBufferPixelFormatTypeKey: CFString ``` |

Modified [kCVPixelBufferPlaneAlignmentKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferplanealignmentkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPlaneAlignmentKey: CFString! ``` |
| To | ``` let kCVPixelBufferPlaneAlignmentKey: CFString ``` |

Modified [kCVPixelBufferPoolAllocationThresholdKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolallocationthresholdkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPoolAllocationThresholdKey: CFString! ``` |
| To | ``` let kCVPixelBufferPoolAllocationThresholdKey: CFString ``` |

Modified [kCVPixelBufferPoolFreeBufferNotification](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolfreebuffernotification)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPoolFreeBufferNotification: CFString! ``` |
| To | ``` let kCVPixelBufferPoolFreeBufferNotification: CFString ``` |

Modified [kCVPixelBufferPoolMaximumBufferAgeKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolmaximumbufferagekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPoolMaximumBufferAgeKey: CFString! ``` |
| To | ``` let kCVPixelBufferPoolMaximumBufferAgeKey: CFString ``` |

Modified [kCVPixelBufferPoolMinimumBufferCountKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferpoolminimumbuffercountkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferPoolMinimumBufferCountKey: CFString! ``` |
| To | ``` let kCVPixelBufferPoolMinimumBufferCountKey: CFString ``` |

Modified [kCVPixelBufferWidthKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferwidthkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelBufferWidthKey: CFString! ``` |
| To | ``` let kCVPixelBufferWidthKey: CFString ``` |

Modified [kCVPixelFormatBitsPerBlock](https://developer.apple.com/documentation/corevideo/kcvpixelformatbitsperblock)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBitsPerBlock: CFString! ``` |
| To | ``` let kCVPixelFormatBitsPerBlock: CFString ``` |

Modified [kCVPixelFormatBlackBlock](https://developer.apple.com/documentation/corevideo/kcvpixelformatblackblock)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBlackBlock: CFString! ``` |
| To | ``` let kCVPixelFormatBlackBlock: CFString ``` |

Modified [kCVPixelFormatBlockHeight](https://developer.apple.com/documentation/corevideo/kcvpixelformatblockheight)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBlockHeight: CFString! ``` |
| To | ``` let kCVPixelFormatBlockHeight: CFString ``` |

Modified [kCVPixelFormatBlockHorizontalAlignment](https://developer.apple.com/documentation/corevideo/kcvpixelformatblockhorizontalalignment)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBlockHorizontalAlignment: CFString! ``` |
| To | ``` let kCVPixelFormatBlockHorizontalAlignment: CFString ``` |

Modified [kCVPixelFormatBlockVerticalAlignment](https://developer.apple.com/documentation/corevideo/kcvpixelformatblockverticalalignment)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBlockVerticalAlignment: CFString! ``` |
| To | ``` let kCVPixelFormatBlockVerticalAlignment: CFString ``` |

Modified [kCVPixelFormatBlockWidth](https://developer.apple.com/documentation/corevideo/kcvpixelformatblockwidth)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatBlockWidth: CFString! ``` |
| To | ``` let kCVPixelFormatBlockWidth: CFString ``` |

Modified [kCVPixelFormatCGBitmapContextCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatcgbitmapcontextcompatibility)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatCGBitmapContextCompatibility: CFString! ``` |
| To | ``` let kCVPixelFormatCGBitmapContextCompatibility: CFString ``` |

Modified [kCVPixelFormatCGBitmapInfo](https://developer.apple.com/documentation/corevideo/kcvpixelformatcgbitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatCGBitmapInfo: CFString! ``` |
| To | ``` let kCVPixelFormatCGBitmapInfo: CFString ``` |

Modified [kCVPixelFormatCGImageCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatcgimagecompatibility)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatCGImageCompatibility: CFString! ``` |
| To | ``` let kCVPixelFormatCGImageCompatibility: CFString ``` |

Modified [kCVPixelFormatCodecType](https://developer.apple.com/documentation/corevideo/kcvpixelformatcodectype)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatCodecType: CFString! ``` |
| To | ``` let kCVPixelFormatCodecType: CFString ``` |

Modified [kCVPixelFormatConstant](https://developer.apple.com/documentation/corevideo/kcvpixelformatconstant)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatConstant: CFString! ``` |
| To | ``` let kCVPixelFormatConstant: CFString ``` |

Modified [kCVPixelFormatContainsAlpha](https://developer.apple.com/documentation/corevideo/kcvpixelformatcontainsalpha)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatContainsAlpha: CFString! ``` |
| To | ``` let kCVPixelFormatContainsAlpha: CFString ``` |

Modified [kCVPixelFormatContainsRGB](https://developer.apple.com/documentation/corevideo/kcvpixelformatcontainsrgb)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatContainsRGB: CFString! ``` |
| To | ``` let kCVPixelFormatContainsRGB: CFString ``` |

Modified [kCVPixelFormatContainsYCbCr](https://developer.apple.com/documentation/corevideo/kcvpixelformatcontainsycbcr)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatContainsYCbCr: CFString! ``` |
| To | ``` let kCVPixelFormatContainsYCbCr: CFString ``` |

Modified [kCVPixelFormatFillExtendedPixelsCallback](https://developer.apple.com/documentation/corevideo/kcvpixelformatfillextendedpixelscallback)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatFillExtendedPixelsCallback: CFString! ``` |
| To | ``` let kCVPixelFormatFillExtendedPixelsCallback: CFString ``` |

Modified [kCVPixelFormatFourCC](https://developer.apple.com/documentation/corevideo/kcvpixelformatfourcc)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatFourCC: CFString! ``` |
| To | ``` let kCVPixelFormatFourCC: CFString ``` |

Modified [kCVPixelFormatHorizontalSubsampling](https://developer.apple.com/documentation/corevideo/kcvpixelformathorizontalsubsampling)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatHorizontalSubsampling: CFString! ``` |
| To | ``` let kCVPixelFormatHorizontalSubsampling: CFString ``` |

Modified [kCVPixelFormatName](https://developer.apple.com/documentation/corevideo/kcvpixelformatname)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatName: CFString! ``` |
| To | ``` let kCVPixelFormatName: CFString ``` |

Modified [kCVPixelFormatOpenGLCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatopenglcompatibility)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatOpenGLCompatibility: CFString! ``` |
| To | ``` let kCVPixelFormatOpenGLCompatibility: CFString ``` |

Modified [kCVPixelFormatOpenGLESCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatopenglescompatibility)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatOpenGLESCompatibility: CFString! ``` |
| To | ``` let kCVPixelFormatOpenGLESCompatibility: CFString ``` |

Modified [kCVPixelFormatOpenGLFormat](https://developer.apple.com/documentation/corevideo/kcvpixelformatopenglformat)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatOpenGLFormat: CFString! ``` |
| To | ``` let kCVPixelFormatOpenGLFormat: CFString ``` |

Modified [kCVPixelFormatOpenGLInternalFormat](https://developer.apple.com/documentation/corevideo/kcvpixelformatopenglinternalformat)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatOpenGLInternalFormat: CFString! ``` |
| To | ``` let kCVPixelFormatOpenGLInternalFormat: CFString ``` |

Modified [kCVPixelFormatOpenGLType](https://developer.apple.com/documentation/corevideo/kcvpixelformatopengltype)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatOpenGLType: CFString! ``` |
| To | ``` let kCVPixelFormatOpenGLType: CFString ``` |

Modified [kCVPixelFormatPlanes](https://developer.apple.com/documentation/corevideo/kcvpixelformatplanes)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatPlanes: CFString! ``` |
| To | ``` let kCVPixelFormatPlanes: CFString ``` |

Modified [kCVPixelFormatQDCompatibility](https://developer.apple.com/documentation/corevideo/kcvpixelformatqdcompatibility)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatQDCompatibility: CFString! ``` |
| To | ``` let kCVPixelFormatQDCompatibility: CFString ``` |

Modified [kCVPixelFormatType_128RGBAFloat](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_128rgbafloat)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_128RGBAFloat: Int { get } ``` |
| To | ``` var kCVPixelFormatType_128RGBAFloat: OSType { get } ``` |

Modified [kCVPixelFormatType_16BE555](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_16be555)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16BE555: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16BE555: OSType { get } ``` |

Modified [kCVPixelFormatType_16BE565](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_16be565)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16BE565: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16BE565: OSType { get } ``` |

Modified [kCVPixelFormatType_16Gray](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_16gray)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16Gray: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16Gray: OSType { get } ``` |

Modified [kCVPixelFormatType_16LE555](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_16le555)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16LE555: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16LE555: OSType { get } ``` |

Modified [kCVPixelFormatType_16LE5551](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_16le5551)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16LE5551: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16LE5551: OSType { get } ``` |

Modified [kCVPixelFormatType_16LE565](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_16le565)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_16LE565: Int { get } ``` |
| To | ``` var kCVPixelFormatType_16LE565: OSType { get } ``` |

Modified [kCVPixelFormatType_1IndexedGray_WhiteIsZero](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_1indexedgray_whiteiszero)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_1IndexedGray_WhiteIsZero: Int { get } ``` |
| To | ``` var kCVPixelFormatType_1IndexedGray_WhiteIsZero: OSType { get } ``` |

Modified [kCVPixelFormatType_1Monochrome](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_1monochrome)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_1Monochrome: Int { get } ``` |
| To | ``` var kCVPixelFormatType_1Monochrome: OSType { get } ``` |

Modified [kCVPixelFormatType_24BGR](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_24bgr)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_24BGR: Int { get } ``` |
| To | ``` var kCVPixelFormatType_24BGR: OSType { get } ``` |

Modified [kCVPixelFormatType_24RGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_24rgb)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_24RGB: Int { get } ``` |
| To | ``` var kCVPixelFormatType_24RGB: OSType { get } ``` |

Modified [kCVPixelFormatType_2Indexed](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_2indexed)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_2Indexed: Int { get } ``` |
| To | ``` var kCVPixelFormatType_2Indexed: OSType { get } ``` |

Modified [kCVPixelFormatType_2IndexedGray_WhiteIsZero](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_2indexedgray_whiteiszero)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_2IndexedGray_WhiteIsZero: Int { get } ``` |
| To | ``` var kCVPixelFormatType_2IndexedGray_WhiteIsZero: OSType { get } ``` |

Modified [kCVPixelFormatType_30RGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_30rgb)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_30RGB: Int { get } ``` |
| To | ``` var kCVPixelFormatType_30RGB: OSType { get } ``` |

Modified [kCVPixelFormatType_32ABGR](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32abgr)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_32ABGR: Int { get } ``` |
| To | ``` var kCVPixelFormatType_32ABGR: OSType { get } ``` |

Modified [kCVPixelFormatType_32AlphaGray](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32alphagray)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_32AlphaGray: Int { get } ``` |
| To | ``` var kCVPixelFormatType_32AlphaGray: OSType { get } ``` |

Modified [kCVPixelFormatType_32ARGB](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_32argb)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_32ARGB: Int { get } ``` |
| To | ``` var kCVPixelFormatType_32ARGB: OSType { get } ``` |

Modified [kCVPixelFormatType_32BGRA](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32bgra)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_32BGRA: Int { get } ``` |
| To | ``` var kCVPixelFormatType_32BGRA: OSType { get } ``` |

Modified [kCVPixelFormatType_32RGBA](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_32rgba)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_32RGBA: Int { get } ``` |
| To | ``` var kCVPixelFormatType_32RGBA: OSType { get } ``` |

Modified [kCVPixelFormatType_420YpCbCr8BiPlanarFullRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8biplanarfullrange)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_420YpCbCr8BiPlanarFullRange: Int { get } ``` |
| To | ``` var kCVPixelFormatType_420YpCbCr8BiPlanarFullRange: OSType { get } ``` |

Modified [kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8biplanarvideorange)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange: Int { get } ``` |
| To | ``` var kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange: OSType { get } ``` |

Modified [kCVPixelFormatType_420YpCbCr8Planar](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_420ypcbcr8planar)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_420YpCbCr8Planar: Int { get } ``` |
| To | ``` var kCVPixelFormatType_420YpCbCr8Planar: OSType { get } ``` |

Modified [kCVPixelFormatType_420YpCbCr8PlanarFullRange](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_420ypcbcr8planarfullrange)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_420YpCbCr8PlanarFullRange: Int { get } ``` |
| To | ``` var kCVPixelFormatType_420YpCbCr8PlanarFullRange: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr10](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr10)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr10: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr10: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr16](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr16)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr16: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr16: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr8](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr8: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr8_yuvs](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr8_yuvs)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr8_yuvs: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr8_yuvs: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr8FullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr8fullrange)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr8FullRange: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr8FullRange: OSType { get } ``` |

Modified [kCVPixelFormatType_422YpCbCr_4A_8BiPlanar](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_422ypcbcr_4a_8biplanar)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_422YpCbCr_4A_8BiPlanar: Int { get } ``` |
| To | ``` var kCVPixelFormatType_422YpCbCr_4A_8BiPlanar: OSType { get } ``` |

Modified [kCVPixelFormatType_4444AYpCbCr16](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_4444aypcbcr16)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4444AYpCbCr16: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4444AYpCbCr16: OSType { get } ``` |

Modified [kCVPixelFormatType_4444AYpCbCr8](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_4444aypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4444AYpCbCr8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4444AYpCbCr8: OSType { get } ``` |

Modified [kCVPixelFormatType_4444YpCbCrA8](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_4444ypcbcra8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4444YpCbCrA8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4444YpCbCrA8: OSType { get } ``` |

Modified [kCVPixelFormatType_4444YpCbCrA8R](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_4444ypcbcra8r)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4444YpCbCrA8R: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4444YpCbCrA8R: OSType { get } ``` |

Modified [kCVPixelFormatType_444YpCbCr10](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_444ypcbcr10)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_444YpCbCr10: Int { get } ``` |
| To | ``` var kCVPixelFormatType_444YpCbCr10: OSType { get } ``` |

Modified [kCVPixelFormatType_444YpCbCr8](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_444ypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_444YpCbCr8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_444YpCbCr8: OSType { get } ``` |

Modified [kCVPixelFormatType_48RGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_48rgb)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_48RGB: Int { get } ``` |
| To | ``` var kCVPixelFormatType_48RGB: OSType { get } ``` |

Modified [kCVPixelFormatType_4Indexed](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_4indexed)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4Indexed: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4Indexed: OSType { get } ``` |

Modified [kCVPixelFormatType_4IndexedGray_WhiteIsZero](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_4indexedgray_whiteiszero)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_4IndexedGray_WhiteIsZero: Int { get } ``` |
| To | ``` var kCVPixelFormatType_4IndexedGray_WhiteIsZero: OSType { get } ``` |

Modified [kCVPixelFormatType_64ARGB](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_64argb)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_64ARGB: Int { get } ``` |
| To | ``` var kCVPixelFormatType_64ARGB: OSType { get } ``` |

Modified [kCVPixelFormatType_64RGBAHalf](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_64rgbahalf)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_64RGBAHalf: Int { get } ``` |
| To | ``` var kCVPixelFormatType_64RGBAHalf: OSType { get } ``` |

Modified [kCVPixelFormatType_8Indexed](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_8indexed)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_8Indexed: Int { get } ``` |
| To | ``` var kCVPixelFormatType_8Indexed: OSType { get } ``` |

Modified [kCVPixelFormatType_8IndexedGray_WhiteIsZero](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_8indexedgray_whiteiszero)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_8IndexedGray_WhiteIsZero: Int { get } ``` |
| To | ``` var kCVPixelFormatType_8IndexedGray_WhiteIsZero: OSType { get } ``` |

Modified [kCVPixelFormatType_OneComponent16Half](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_onecomponent16half)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_OneComponent16Half: Int { get } ``` |
| To | ``` var kCVPixelFormatType_OneComponent16Half: OSType { get } ``` |

Modified [kCVPixelFormatType_OneComponent32Float](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_onecomponent32float)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_OneComponent32Float: Int { get } ``` |
| To | ``` var kCVPixelFormatType_OneComponent32Float: OSType { get } ``` |

Modified [kCVPixelFormatType_OneComponent8](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_onecomponent8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_OneComponent8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_OneComponent8: OSType { get } ``` |

Modified [kCVPixelFormatType_TwoComponent16Half](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_twocomponent16half)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_TwoComponent16Half: Int { get } ``` |
| To | ``` var kCVPixelFormatType_TwoComponent16Half: OSType { get } ``` |

Modified [kCVPixelFormatType_TwoComponent32Float](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_twocomponent32float)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_TwoComponent32Float: Int { get } ``` |
| To | ``` var kCVPixelFormatType_TwoComponent32Float: OSType { get } ``` |

Modified [kCVPixelFormatType_TwoComponent8](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_twocomponent8)

|  | Declaration |
| --- | --- |
| From | ``` var kCVPixelFormatType_TwoComponent8: Int { get } ``` |
| To | ``` var kCVPixelFormatType_TwoComponent8: OSType { get } ``` |

Modified [kCVPixelFormatVerticalSubsampling](https://developer.apple.com/documentation/corevideo/kcvpixelformatverticalsubsampling)

|  | Declaration |
| --- | --- |
| From | ``` let kCVPixelFormatVerticalSubsampling: CFString! ``` |
| To | ``` let kCVPixelFormatVerticalSubsampling: CFString ``` |

Modified [kCVReturnAllocationFailed](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnallocationfailed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnAllocationFailed: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnAllocationFailed: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnDisplayLinkAlreadyRunning](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturndisplaylinkalreadyrunning)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnDisplayLinkAlreadyRunning: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnDisplayLinkAlreadyRunning: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnDisplayLinkCallbacksNotSet](https://developer.apple.com/documentation/corevideo/kcvreturndisplaylinkcallbacksnotset)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnDisplayLinkCallbacksNotSet: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnDisplayLinkCallbacksNotSet: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnDisplayLinkNotRunning](https://developer.apple.com/documentation/corevideo/kcvreturndisplaylinknotrunning)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnDisplayLinkNotRunning: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnDisplayLinkNotRunning: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnError](https://developer.apple.com/documentation/corevideo/kcvreturnerror)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnError: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnError: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnFirst](https://developer.apple.com/documentation/corevideo/kcvreturnfirst)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnFirst: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnFirst: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidArgument](https://developer.apple.com/documentation/corevideo/kcvreturninvalidargument)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidArgument: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidArgument: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidDisplay](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturninvaliddisplay)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidDisplay: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidDisplay: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidPixelBufferAttributes](https://developer.apple.com/documentation/corevideo/kcvreturninvalidpixelbufferattributes)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidPixelBufferAttributes: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidPixelBufferAttributes: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidPixelFormat](https://developer.apple.com/documentation/corevideo/kcvreturninvalidpixelformat)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidPixelFormat: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidPixelFormat: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidPoolAttributes](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturninvalidpoolattributes)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidPoolAttributes: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidPoolAttributes: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnInvalidSize](https://developer.apple.com/documentation/corevideo/kcvreturninvalidsize)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnInvalidSize: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnInvalidSize: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnLast](https://developer.apple.com/documentation/corevideo/kcvreturnlast)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnLast: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnLast: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnPixelBufferNotMetalCompatible](https://developer.apple.com/documentation/corevideo/kcvreturnpixelbuffernotmetalcompatible)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnPixelBufferNotMetalCompatible: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnPixelBufferNotMetalCompatible: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnPixelBufferNotOpenGLCompatible](https://developer.apple.com/documentation/corevideo/kcvreturnpixelbuffernotopenglcompatible)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnPixelBufferNotOpenGLCompatible: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnPixelBufferNotOpenGLCompatible: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnPoolAllocationFailed](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnpoolallocationfailed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnPoolAllocationFailed: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnPoolAllocationFailed: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnSuccess](https://developer.apple.com/documentation/corevideo/kcvreturnsuccess)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnSuccess: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnSuccess: CVReturn { get } ``` | iOS 9.0 |

Modified [kCVReturnWouldExceedAllocationThreshold](https://developer.apple.com/documentation/corevideo/1572713-result_codes/kcvreturnwouldexceedallocationthreshold)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kCVReturnWouldExceedAllocationThreshold: _CVReturn { get } ``` | iOS 8.0 |
| To | ``` var kCVReturnWouldExceedAllocationThreshold: CVReturn { get } ``` | iOS 9.0 |

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
