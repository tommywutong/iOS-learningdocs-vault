---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/CoreVideo.html
archived_at: '2026-07-18T02:57:40.167206Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreVideo Changes for Swift

### CoreVideo

Removed [CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack?, refCon: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/1457249-init)Removed [CVAttachmentMode](https://developer.apple.com/documentation/corevideo/cvattachmentmode)Removed [CVPixelBufferLockFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Removed [CVPixelBufferPoolFlushFlags](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)Removed [kCVAttachmentMode_ShouldNotPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/kcvattachmentmode_shouldnotpropagate)Removed [kCVAttachmentMode_ShouldPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/kcvattachmentmode_shouldpropagate)Removed [kCVPixelBufferLock_ReadOnly](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags/1457186-readonly)Removed [kCVPixelBufferPoolFlushExcessBuffers](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/1456664-excessbuffers)Removed [kCVSMPTETimeRunning](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags/1412038-running)Removed [kCVSMPTETimeType24](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/kcvsmptetimetype24)Removed [kCVSMPTETimeType25](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type25)Removed [kCVSMPTETimeType2997](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/kcvsmptetimetype2997)Removed [kCVSMPTETimeType2997Drop](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/kcvsmptetimetype2997drop)Removed [kCVSMPTETimeType30](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/kcvsmptetimetype30)Removed [kCVSMPTETimeType30Drop](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/kcvsmptetimetype30drop)Removed [kCVSMPTETimeType5994](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type5994)Removed [kCVSMPTETimeType60](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type60)Removed [kCVSMPTETimeValid](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags/1411992-valid)Removed [kCVTimeIsIndefinite](https://developer.apple.com/documentation/corevideo/cvtimeflags/1412036-isindefinite)Removed [kCVTimeStampBottomField](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampbottomfield)Removed [kCVTimeStampHostTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestamphosttimevalid)Removed [kCVTimeStampIsInterlaced](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1412007-isinterlaced)Removed [kCVTimeStampRateScalarValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampratescalarvalid)Removed [kCVTimeStampSMPTETimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1411931-smptetimevalid)Removed [kCVTimeStampTopField](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestamptopfield)Removed [kCVTimeStampVideoHostTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1411964-videohosttimevalid)Removed [kCVTimeStampVideoRefreshPeriodValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1412011-videorefreshperiodvalid)Removed [kCVTimeStampVideoTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampvideotimevalid)Added [CVAttachmentMode [enum]](https://developer.apple.com/documentation/corevideo/cvattachmentmode)Added [CVAttachmentMode.shouldNotPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/kcvattachmentmode_shouldnotpropagate)Added [CVAttachmentMode.shouldPropagate](https://developer.apple.com/documentation/corevideo/cvattachmentmode/shouldpropagate)Added [CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CoreVideo.CVFillExtendedPixelsCallBack?, refCon: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/1457249-init)Added [CVPixelBufferLockFlags [struct]](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)Added [CVPixelBufferLockFlags.init(rawValue: CVOptionFlags)](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags/1845289-init)Added [CVPixelBufferLockFlags.readOnly](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags/1457186-readonly)Added [CVPixelBufferPoolFlushFlags [struct]](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags)Added [CVPixelBufferPoolFlushFlags.excessBuffers](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/kcvpixelbufferpoolflushexcessbuffers)Added [CVPixelBufferPoolFlushFlags.init(rawValue: CVOptionFlags)](https://developer.apple.com/documentation/corevideo/cvpixelbufferpoolflushflags/1845284-init)Added [CVSMPTETimeFlags [struct]](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags)Added [CVSMPTETimeFlags.init(rawValue: UInt32)](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags/1845287-init)Added [CVSMPTETimeFlags.running](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags/1412038-running)Added [CVSMPTETimeFlags.valid](https://developer.apple.com/documentation/corevideo/cvsmptetimeflags/1411992-valid)Added [CVSMPTETimeType [enum]](https://developer.apple.com/documentation/corevideo/cvsmptetimetype)Added [CVSMPTETimeType.type24](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type24)Added [CVSMPTETimeType.type25](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type25)Added [CVSMPTETimeType.type2997](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type2997)Added [CVSMPTETimeType.type2997Drop](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type2997drop)Added [CVSMPTETimeType.type30](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type30)Added [CVSMPTETimeType.type30Drop](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type30drop)Added [CVSMPTETimeType.type5994](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type5994)Added [CVSMPTETimeType.type60](https://developer.apple.com/documentation/corevideo/cvsmptetimetype/type60)Added [CVTimeFlags [struct]](https://developer.apple.com/documentation/corevideo/cvtimeflags)Added [CVTimeFlags.init(rawValue: Int32)](https://developer.apple.com/documentation/corevideo/cvtimeflags/1845285-init)Added [CVTimeFlags.isIndefinite](https://developer.apple.com/documentation/corevideo/cvtimeflags/kcvtimeisindefinite)Added [CVTimeStampFlags [struct]](https://developer.apple.com/documentation/corevideo/cvtimestampflags)Added [CVTimeStampFlags.bottomField](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampbottomfield)Added [CVTimeStampFlags.hostTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestamphosttimevalid)Added [CVTimeStampFlags.init(rawValue: UInt64)](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1845286-init)Added [CVTimeStampFlags.isInterlaced](https://developer.apple.com/documentation/corevideo/cvtimestampflags/1412007-isinterlaced)Added [CVTimeStampFlags.rateScalarValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampratescalarvalid)Added [CVTimeStampFlags.smpteTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampsmptetimevalid)Added [CVTimeStampFlags.topField](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestamptopfield)Added [CVTimeStampFlags.videoHostTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampvideohosttimevalid)Added [CVTimeStampFlags.videoRefreshPeriodValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampvideorefreshperiodvalid)Added [CVTimeStampFlags.videoTimeValid](https://developer.apple.com/documentation/corevideo/cvtimestampflags/kcvtimestampvideotimevalid)Added [kCVImageBufferTransferFunction_SMPTE_ST_428_1](https://developer.apple.com/documentation/corevideo/kcvimagebuffertransferfunction_smpte_st_428_1)Added [kCVPixelFormatType_14Bayer_BGGR](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_14bayer_bggr)Added [kCVPixelFormatType_14Bayer_GBRG](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_14bayer_gbrg)Added [kCVPixelFormatType_14Bayer_GRBG](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_14bayer_grbg)Added [kCVPixelFormatType_14Bayer_RGGB](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_14bayer_rggb)Added [kCVPixelFormatType_30RGBLEPackedWideGamut](https://developer.apple.com/documentation/corevideo/1563591-pixel_format_identifiers/kcvpixelformattype_30rgblepackedwidegamut)Added [kCVReturnRetry](https://developer.apple.com/documentation/corevideo/kcvreturnretry)Modified [CVFillExtendedPixelsCallBackData [struct]](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata)

|  | Declaration |
| --- | --- |
| From | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack?     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: CFIndex, fillCallBack fillCallBack: CVFillExtendedPixelsCallBack?, refCon refCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CoreVideo.CVFillExtendedPixelsCallBack?     var refCon: UnsafeMutableRawPointer?     init()     init(version version: CFIndex, fillCallBack fillCallBack: CoreVideo.CVFillExtendedPixelsCallBack?, refCon refCon: UnsafeMutableRawPointer?) } ``` |

Modified [CVFillExtendedPixelsCallBackData.fillCallBack](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/1456760-fillcallback)

|  | Declaration |
| --- | --- |
| From | ``` var fillCallBack: CVFillExtendedPixelsCallBack? ``` |
| To | ``` var fillCallBack: CoreVideo.CVFillExtendedPixelsCallBack? ``` |

Modified [CVFillExtendedPixelsCallBackData.refCon](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata/1457038-refcon)

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafeMutablePointer<Void> ``` |
| To | ``` var refCon: UnsafeMutableRawPointer? ``` |

Modified [CVBufferGetAttachment(_: CVBuffer, _: CFString, _: UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>?](https://developer.apple.com/documentation/corevideo/1457103-cvbuffergetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferGetAttachment(_ buffer: CVBuffer, _ key: CFString, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>? ``` |
| To | ``` func CVBufferGetAttachment(_ buffer: CVBuffer, _ key: CFString, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>?) -> Unmanaged<CFTypeRef>? ``` |

Modified [CVBufferGetAttachments(_: CVBuffer, _: CVAttachmentMode) -> CFDictionary?](https://developer.apple.com/documentation/corevideo/1457272-cvbuffergetattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferGetAttachments(_ buffer: CVBuffer, _ attachmentMode: CVAttachmentMode) -> Unmanaged<CFDictionary>? ``` |
| To | ``` func CVBufferGetAttachments(_ buffer: CVBuffer, _ attachmentMode: CVAttachmentMode) -> CFDictionary? ``` |

Modified [CVBufferSetAttachment(_: CVBuffer, _: CFString, _: CFTypeRef, _: CVAttachmentMode)](https://developer.apple.com/documentation/corevideo/1456974-cvbuffersetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CVBufferSetAttachment(_ buffer: CVBuffer, _ key: CFString, _ value: AnyObject, _ attachmentMode: CVAttachmentMode) ``` |
| To | ``` func CVBufferSetAttachment(_ buffer: CVBuffer, _ key: CFString, _ value: CFTypeRef, _ attachmentMode: CVAttachmentMode) ``` |

Modified [CVFillExtendedPixelsCallBack](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVFillExtendedPixelsCallBack = (CVPixelBuffer, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |
| To | ``` typealias CVFillExtendedPixelsCallBack = (CVPixelBuffer, UnsafeMutableRawPointer?) -> DarwinBoolean ``` |

Modified [CVImageBuffer](https://developer.apple.com/documentation/corevideo/cvimagebufferref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVImageBufferRef = CVImageBuffer ``` |
| To | ``` typealias CVImageBuffer = CVBuffer ``` |

Modified [CVMetalTextureCacheCreate(_: CFAllocator?, _: CFDictionary?, _: MTLDevice, _: CFDictionary?, _: UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456774-cvmetaltexturecachecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ metalDevice: MTLDevice, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<Unmanaged<CVMetalTextureCache>?>) -> CVReturn ``` |
| To | ``` func CVMetalTextureCacheCreate(_ allocator: CFAllocator?, _ cacheAttributes: CFDictionary?, _ metalDevice: MTLDevice, _ textureAttributes: CFDictionary?, _ cacheOut: UnsafeMutablePointer<CVMetalTextureCache?>) -> CVReturn ``` |

Modified [CVMetalTextureCacheCreateTextureFromImage(_: CFAllocator?, _: CVMetalTextureCache, _: CVImageBuffer, _: CFDictionary?, _: MTLPixelFormat, _: Int, _: Int, _: Int, _: UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456754-cvmetaltexturecachecreatetexture)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVMetalTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn ``` |
| To | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator?, _ textureCache: CVMetalTextureCache, _ sourceImage: CVImageBuffer, _ textureAttributes: CFDictionary?, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<CVMetalTexture?>) -> CVReturn ``` |

Modified [CVMetalTextureGetCleanTexCoords(_: CVMetalTexture, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!, _: UnsafeMutablePointer<Float>!)](https://developer.apple.com/documentation/corevideo/1457089-cvmetaltexturegetcleantexcoords)

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureGetCleanTexCoords(_ image: CVMetalTexture, _ lowerLeft: UnsafeMutablePointer<Float>, _ lowerRight: UnsafeMutablePointer<Float>, _ upperRight: UnsafeMutablePointer<Float>, _ upperLeft: UnsafeMutablePointer<Float>) ``` |
| To | ``` func CVMetalTextureGetCleanTexCoords(_ image: CVMetalTexture, _ lowerLeft: UnsafeMutablePointer<Float>!, _ lowerRight: UnsafeMutablePointer<Float>!, _ upperRight: UnsafeMutablePointer<Float>!, _ upperLeft: UnsafeMutablePointer<Float>!) ``` |

Modified [CVOpenGLESTextureGetCleanTexCoords(_: CVOpenGLESTexture, _: UnsafeMutablePointer<GLfloat>!, _: UnsafeMutablePointer<GLfloat>!, _: UnsafeMutablePointer<GLfloat>!, _: UnsafeMutablePointer<GLfloat>!)](https://developer.apple.com/documentation/corevideo/1621287-cvopenglestexturegetcleantexcoor)

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>) ``` |
| To | ``` func CVOpenGLESTextureGetCleanTexCoords(_ image: CVOpenGLESTexture, _ lowerLeft: UnsafeMutablePointer<GLfloat>!, _ lowerRight: UnsafeMutablePointer<GLfloat>!, _ upperRight: UnsafeMutablePointer<GLfloat>!, _ upperLeft: UnsafeMutablePointer<GLfloat>!) ``` |

Modified [CVPixelBufferCreateWithBytes(_: CFAllocator?, _: Int, _: Int, _: OSType, _: UnsafeMutableRawPointer, _: Int, _: CoreVideo.CVPixelBufferReleaseBytesCallback?, _: UnsafeMutableRawPointer?, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456979-cvpixelbuffercreatewithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback?, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutableRawPointer, _ bytesPerRow: Int, _ releaseCallback: CoreVideo.CVPixelBufferReleaseBytesCallback?, _ releaseRefCon: UnsafeMutableRawPointer?, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferCreateWithPlanarBytes(_: CFAllocator?, _: Int, _: Int, _: OSType, _: UnsafeMutableRawPointer?, _: Int, _: Int, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<Int>!, _: CoreVideo.CVPixelBufferReleasePlanarBytesCallback?, _: UnsafeMutableRawPointer?, _: CFDictionary?, _: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn](https://developer.apple.com/documentation/corevideo/1456731-cvpixelbuffercreatewithplanarbyt)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<Int>, _ planeHeight: UnsafeMutablePointer<Int>, _ planeBytesPerRow: UnsafeMutablePointer<Int>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback?, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator?, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutableRawPointer?, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ planeWidth: UnsafeMutablePointer<Int>!, _ planeHeight: UnsafeMutablePointer<Int>!, _ planeBytesPerRow: UnsafeMutablePointer<Int>!, _ releaseCallback: CoreVideo.CVPixelBufferReleasePlanarBytesCallback?, _ releaseRefCon: UnsafeMutableRawPointer?, _ pixelBufferAttributes: CFDictionary?, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> CVReturn ``` |

Modified [CVPixelBufferGetBaseAddress(_: CVPixelBuffer) -> UnsafeMutableRawPointer?](https://developer.apple.com/documentation/corevideo/1457115-cvpixelbuffergetbaseaddress)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer) -> UnsafeMutableRawPointer? ``` |

Modified [CVPixelBufferGetBaseAddressOfPlane(_: CVPixelBuffer, _: Int) -> UnsafeMutableRawPointer?](https://developer.apple.com/documentation/corevideo/1456821-cvpixelbuffergetbaseaddressofpla)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer, _ planeIndex: Int) -> UnsafeMutableRawPointer? ``` |

Modified [CVPixelBufferGetExtendedPixels(_: CVPixelBuffer, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int>?, _: UnsafeMutablePointer<Int>?)](https://developer.apple.com/documentation/corevideo/1457029-cvpixelbuffergetextendedpixels)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>, _ extraColumnsOnRight: UnsafeMutablePointer<Int>, _ extraRowsOnTop: UnsafeMutablePointer<Int>, _ extraRowsOnBottom: UnsafeMutablePointer<Int>) ``` |
| To | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>?, _ extraColumnsOnRight: UnsafeMutablePointer<Int>?, _ extraRowsOnTop: UnsafeMutablePointer<Int>?, _ extraRowsOnBottom: UnsafeMutablePointer<Int>?) ``` |

Modified [CVPixelBufferPoolGetAttributes(_: CVPixelBufferPool) -> CFDictionary?](https://developer.apple.com/documentation/corevideo/1456983-cvpixelbufferpoolgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolGetAttributes(_ pool: CVPixelBufferPool) -> Unmanaged<CFDictionary>? ``` |
| To | ``` func CVPixelBufferPoolGetAttributes(_ pool: CVPixelBufferPool) -> CFDictionary? ``` |

Modified [CVPixelBufferPoolGetPixelBufferAttributes(_: CVPixelBufferPool) -> CFDictionary?](https://developer.apple.com/documentation/corevideo/1457222-cvpixelbufferpoolgetpixelbuffera)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferPoolGetPixelBufferAttributes(_ pool: CVPixelBufferPool) -> Unmanaged<CFDictionary>? ``` |
| To | ``` func CVPixelBufferPoolGetPixelBufferAttributes(_ pool: CVPixelBufferPool) -> CFDictionary? ``` |

Modified [CVPixelBufferReleaseBytesCallback](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleasebytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleaseBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CVPixelBufferReleaseBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer?) -> Swift.Void ``` |

Modified [CVPixelBufferReleasePlanarBytesCallback](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleaseplanarbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleasePlanarBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void ``` |
| To | ``` typealias CVPixelBufferReleasePlanarBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?) -> Swift.Void ``` |

Modified [CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_: CFAllocator?) -> CFArray?](https://developer.apple.com/documentation/corevideo/1456798-cvpixelformatdescriptionarraycre)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_ allocator: CFAllocator?) -> Unmanaged<CFArray>? ``` |
| To | ``` func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_ allocator: CFAllocator?) -> CFArray? ``` |

Modified [CVPixelFormatDescriptionCreateWithPixelFormatType(_: CFAllocator?, _: OSType) -> CFDictionary?](https://developer.apple.com/documentation/corevideo/1456807-cvpixelformatdescriptioncreatewi)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelFormatDescriptionCreateWithPixelFormatType(_ allocator: CFAllocator?, _ pixelFormat: OSType) -> Unmanaged<CFDictionary>? ``` |
| To | ``` func CVPixelFormatDescriptionCreateWithPixelFormatType(_ allocator: CFAllocator?, _ pixelFormat: OSType) -> CFDictionary? ``` |

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
