---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreVideo.html
archived_at: '2026-07-18T02:52:17.267925Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreVideo Changes

## CoreVideo

Added CVFillExtendedPixelsCallBackData.init()Added CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack, refCon: UnsafeMutablePointer<Void>)Added CVPlanarComponentInfo.init()Added CVPlanarComponentInfo.init(offset: Int32, rowBytes: UInt32)Added CVPlanarPixelBufferInfo.init()Added CVPlanarPixelBufferInfo.init(componentInfo: (CVPlanarComponentInfo))Added CVPlanarPixelBufferInfo_YCbCrBiPlanar.init()Added CVPlanarPixelBufferInfo_YCbCrBiPlanar.init(componentInfoY: CVPlanarComponentInfo, componentInfoCbCr: CVPlanarComponentInfo)Added CVPlanarPixelBufferInfo_YCbCrPlanar.init()Added CVPlanarPixelBufferInfo_YCbCrPlanar.init(componentInfoY: CVPlanarComponentInfo, componentInfoCb: CVPlanarComponentInfo, componentInfoCr: CVPlanarComponentInfo)Added CVSMPTETime.init()Added CVSMPTETime.init(subframes: Int16, subframeDivisor: Int16, counter: UInt32, type: UInt32, flags: UInt32, hours: Int16, minutes: Int16, seconds: Int16, frames: Int16)Added CVTime.init()Added CVTime.init(timeValue: Int64, timeScale: Int32, flags: Int32)Added CVTimeStamp.init()Added CVTimeStamp.init(version: UInt32, videoTimeScale: Int32, videoTime: Int64, hostTime: UInt64, rateScalar: Double, videoRefreshPeriod: Int64, smpteTime: CVSMPTETime, flags: UInt64, reserved: UInt64)Modified CVFillExtendedPixelsCallBackData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack     var refCon: UnsafePointer<()> } ``` |
| To | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: CFIndex, fillCallBack fillCallBack: CVFillExtendedPixelsCallBack, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

Modified CVFillExtendedPixelsCallBackData.refCon

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafePointer<()> ``` |
| To | ``` var refCon: UnsafeMutablePointer<Void> ``` |

Modified CVPlanarComponentInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVPlanarComponentInfo {     var offset: Int32     var rowBytes: UInt32 } ``` |
| To | ``` struct CVPlanarComponentInfo {     var offset: Int32     var rowBytes: UInt32     init()     init(offset offset: Int32, rowBytes rowBytes: UInt32) } ``` |

Modified CVPlanarPixelBufferInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVPlanarPixelBufferInfo {     var componentInfo: (CVPlanarComponentInfo) } ``` |
| To | ``` struct CVPlanarPixelBufferInfo {     var componentInfo: (CVPlanarComponentInfo)     init()     init(componentInfo componentInfo: (CVPlanarComponentInfo)) } ``` |

Modified CVPlanarPixelBufferInfo_YCbCrBiPlanar [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVPlanarPixelBufferInfo_YCbCrBiPlanar {     var componentInfoY: CVPlanarComponentInfo     var componentInfoCbCr: CVPlanarComponentInfo } ``` |
| To | ``` struct CVPlanarPixelBufferInfo_YCbCrBiPlanar {     var componentInfoY: CVPlanarComponentInfo     var componentInfoCbCr: CVPlanarComponentInfo     init()     init(componentInfoY componentInfoY: CVPlanarComponentInfo, componentInfoCbCr componentInfoCbCr: CVPlanarComponentInfo) } ``` |

Modified CVPlanarPixelBufferInfo_YCbCrPlanar [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVPlanarPixelBufferInfo_YCbCrPlanar {     var componentInfoY: CVPlanarComponentInfo     var componentInfoCb: CVPlanarComponentInfo     var componentInfoCr: CVPlanarComponentInfo } ``` |
| To | ``` struct CVPlanarPixelBufferInfo_YCbCrPlanar {     var componentInfoY: CVPlanarComponentInfo     var componentInfoCb: CVPlanarComponentInfo     var componentInfoCr: CVPlanarComponentInfo     init()     init(componentInfoY componentInfoY: CVPlanarComponentInfo, componentInfoCb componentInfoCb: CVPlanarComponentInfo, componentInfoCr componentInfoCr: CVPlanarComponentInfo) } ``` |

Modified CVSMPTETime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVSMPTETime {     var subframes: Int16     var subframeDivisor: Int16     var counter: UInt32     var type: UInt32     var flags: UInt32     var hours: Int16     var minutes: Int16     var seconds: Int16     var frames: Int16 } ``` |
| To | ``` struct CVSMPTETime {     var subframes: Int16     var subframeDivisor: Int16     var counter: UInt32     var type: UInt32     var flags: UInt32     var hours: Int16     var minutes: Int16     var seconds: Int16     var frames: Int16     init()     init(subframes subframes: Int16, subframeDivisor subframeDivisor: Int16, counter counter: UInt32, type type: UInt32, flags flags: UInt32, hours hours: Int16, minutes minutes: Int16, seconds seconds: Int16, frames frames: Int16) } ``` |

Modified CVTime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVTime {     var timeValue: Int64     var timeScale: Int32     var flags: Int32 } ``` |
| To | ``` struct CVTime {     var timeValue: Int64     var timeScale: Int32     var flags: Int32     init()     init(timeValue timeValue: Int64, timeScale timeScale: Int32, flags flags: Int32) } ``` |

Modified CVTimeStamp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVTimeStamp {     var version: UInt32     var videoTimeScale: Int32     var videoTime: Int64     var hostTime: UInt64     var rateScalar: Double     var videoRefreshPeriod: Int64     var smpteTime: CVSMPTETime     var flags: UInt64     var reserved: UInt64 } ``` |
| To | ``` struct CVTimeStamp {     var version: UInt32     var videoTimeScale: Int32     var videoTime: Int64     var hostTime: UInt64     var rateScalar: Double     var videoRefreshPeriod: Int64     var smpteTime: CVSMPTETime     var flags: UInt64     var reserved: UInt64     init()     init(version version: UInt32, videoTimeScale videoTimeScale: Int32, videoTime videoTime: Int64, hostTime hostTime: UInt64, rateScalar rateScalar: Double, videoRefreshPeriod videoRefreshPeriod: Int64, smpteTime smpteTime: CVSMPTETime, flags flags: UInt64, reserved reserved: UInt64) } ``` |

Modified CVBufferGetAttachment(CVBuffer!, CFString!, UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVBufferGetAttachment(_ buffer: CVBuffer!, _ key: CFString!, _ attachmentMode: UnsafePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func CVBufferGetAttachment(_ buffer: CVBuffer!, _ key: CFString!, _ attachmentMode: UnsafeMutablePointer<CVAttachmentMode>) -> Unmanaged<AnyObject>! ``` | OS X 10.4 |

Modified CVBufferGetAttachments(CVBuffer!, CVAttachmentMode) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVBufferPropagateAttachments(CVBuffer!, CVBuffer!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVBufferRemoveAllAttachments(CVBuffer!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVBufferRemoveAttachment(CVBuffer!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVBufferSetAttachment(CVBuffer!, CFString!, AnyObject!, CVAttachmentMode)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVBufferSetAttachments(CVBuffer!, CFDictionary!, CVAttachmentMode)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkCreateWithActiveCGDisplays(_ displayLinkOut: UnsafePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkCreateWithActiveCGDisplays(_ displayLinkOut: UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkCreateWithCGDisplay(_ displayID: CGDirectDisplayID, _ displayLinkOut: UnsafePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkCreateWithCGDisplay(_ displayID: CGDirectDisplayID, _ displayLinkOut: UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkCreateWithCGDisplays(_ displayArray: UnsafePointer<CGDirectDisplayID>, _ count: CFIndex, _ displayLinkOut: UnsafePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkCreateWithCGDisplays(_ displayArray: UnsafeMutablePointer<CGDirectDisplayID>, _ count: CFIndex, _ displayLinkOut: UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkCreateWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ displayLinkOut: UnsafePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkCreateWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ displayLinkOut: UnsafeMutablePointer<Unmanaged<CVDisplayLink>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkGetActualOutputVideoRefreshPeriod(CVDisplayLink!) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink!) -> CGDirectDisplayID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkGetCurrentTime(CVDisplayLink!, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkGetCurrentTime(_ displayLink: CVDisplayLink!, _ outTime: UnsafePointer<CVTimeStamp>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkGetCurrentTime(_ displayLink: CVDisplayLink!, _ outTime: UnsafeMutablePointer<CVTimeStamp>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink!) -> CVTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkGetOutputVideoLatency(CVDisplayLink!) -> CVTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkIsRunning(CVDisplayLink!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CVDisplayLinkOutputCallback = CFunctionPointer<((CVDisplayLink!, ConstUnsafePointer<CVTimeStamp>, ConstUnsafePointer<CVTimeStamp>, CVOptionFlags, UnsafePointer<CVOptionFlags>, UnsafePointer<()>) -> CVReturn)> ``` |
| To | ``` typealias CVDisplayLinkOutputCallback = CFunctionPointer<((CVDisplayLink!, UnsafePointer<CVTimeStamp>, UnsafePointer<CVTimeStamp>, CVOptionFlags, UnsafeMutablePointer<CVOptionFlags>, UnsafeMutablePointer<Void>) -> CVReturn)> ``` |

Modified CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink!, CGDirectDisplayID) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink!, CGLContextObj, CGLPixelFormatObj) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkSetOutputCallback(CVDisplayLink!, CVDisplayLinkOutputCallback, UnsafeMutablePointer<Void>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkSetOutputCallback(_ displayLink: CVDisplayLink!, _ callback: CVDisplayLinkOutputCallback, _ userInfo: UnsafePointer<()>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkSetOutputCallback(_ displayLink: CVDisplayLink!, _ callback: CVDisplayLinkOutputCallback, _ userInfo: UnsafeMutablePointer<Void>) -> CVReturn ``` | OS X 10.4 |

Modified CVDisplayLinkStart(CVDisplayLink!) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkStop(CVDisplayLink!) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVDisplayLinkTranslateTime(CVDisplayLink!, UnsafePointer<CVTimeStamp>, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVDisplayLinkTranslateTime(_ displayLink: CVDisplayLink!, _ inTime: ConstUnsafePointer<CVTimeStamp>, _ outTime: UnsafePointer<CVTimeStamp>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVDisplayLinkTranslateTime(_ displayLink: CVDisplayLink!, _ inTime: UnsafePointer<CVTimeStamp>, _ outTime: UnsafeMutablePointer<CVTimeStamp>) -> CVReturn ``` | OS X 10.4 |

Modified CVFillExtendedPixelsCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CVFillExtendedPixelsCallBack = CFunctionPointer<((CVPixelBuffer!, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CVFillExtendedPixelsCallBack = CFunctionPointer<((CVPixelBuffer!, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified CVGetCurrentHostTime() -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVGetHostClockFrequency() -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVGetHostClockMinimumTimeDelta() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVImageBufferCreateColorSpaceFromAttachments(CFDictionary!) -> Unmanaged<CGColorSpace>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CVImageBufferGetCleanRect(CVImageBuffer!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVImageBufferGetColorSpace(CVImageBuffer!) -> Unmanaged<CGColorSpace>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVImageBufferGetDisplaySize(CVImageBuffer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVImageBufferGetEncodedSize(CVImageBuffer!) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVImageBufferIsFlipped(CVImageBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferAttach(CVOpenGLBuffer!, CGLContextObj, GLenum, GLint, GLint) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferCreate(CFAllocator!, Int, Int, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLBufferCreate(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ attributes: CFDictionary!, _ bufferOut: UnsafePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVOpenGLBufferCreate(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ attributes: CFDictionary!, _ bufferOut: UnsafeMutablePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVOpenGLBufferGetAttributes(CVOpenGLBuffer!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferPoolCreate(CFAllocator!, CFDictionary!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVOpenGLBufferPool>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLBufferPoolCreate(_ allocator: CFAllocator!, _ poolAttributes: CFDictionary!, _ openGLBufferAttributes: CFDictionary!, _ poolOut: UnsafePointer<Unmanaged<CVOpenGLBufferPool>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVOpenGLBufferPoolCreate(_ allocator: CFAllocator!, _ poolAttributes: CFDictionary!, _ openGLBufferAttributes: CFDictionary!, _ poolOut: UnsafeMutablePointer<Unmanaged<CVOpenGLBufferPool>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVOpenGLBufferPoolCreateOpenGLBuffer(CFAllocator!, CVOpenGLBufferPool!, UnsafeMutablePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLBufferPoolCreateOpenGLBuffer(_ allocator: CFAllocator!, _ openGLBufferPool: CVOpenGLBufferPool!, _ openGLBufferOut: UnsafePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVOpenGLBufferPoolCreateOpenGLBuffer(_ allocator: CFAllocator!, _ openGLBufferPool: CVOpenGLBufferPool!, _ openGLBufferOut: UnsafeMutablePointer<Unmanaged<CVOpenGLBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVOpenGLBufferPoolGetAttributes(CVOpenGLBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferPoolGetOpenGLBufferAttributes(CVOpenGLBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLBufferPoolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureCacheCreate(CFAllocator!, CFDictionary!, CGLContextObj, CGLPixelFormatObj, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVOpenGLTextureCache>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLTextureCacheCreate(_ allocator: CFAllocator!, _ cacheAttributes: CFDictionary!, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj, _ textureAttributes: CFDictionary!, _ cacheOut: UnsafePointer<Unmanaged<CVOpenGLTextureCache>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVOpenGLTextureCacheCreate(_ allocator: CFAllocator!, _ cacheAttributes: CFDictionary!, _ cglContext: CGLContextObj, _ cglPixelFormat: CGLPixelFormatObj, _ textureAttributes: CFDictionary!, _ cacheOut: UnsafeMutablePointer<Unmanaged<CVOpenGLTextureCache>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVOpenGLTextureCacheCreateTextureFromImage(CFAllocator!, CVOpenGLTextureCache!, CVImageBuffer!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVOpenGLTexture>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVOpenGLTextureCache!, _ sourceImage: CVImageBuffer!, _ attributes: CFDictionary!, _ textureOut: UnsafePointer<Unmanaged<CVOpenGLTexture>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVOpenGLTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVOpenGLTextureCache!, _ sourceImage: CVImageBuffer!, _ attributes: CFDictionary!, _ textureOut: UnsafeMutablePointer<Unmanaged<CVOpenGLTexture>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVOpenGLTextureCacheFlush(CVOpenGLTextureCache!, CVOptionFlags)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureCacheGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureGetCleanTexCoords(CVOpenGLTexture!, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>, UnsafeMutablePointer<GLfloat>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVOpenGLTextureGetCleanTexCoords(_ image: CVOpenGLTexture!, _ lowerLeft: UnsafePointer<GLfloat>, _ lowerRight: UnsafePointer<GLfloat>, _ upperRight: UnsafePointer<GLfloat>, _ upperLeft: UnsafePointer<GLfloat>) ``` | OS X 10.10 |
| To | ``` func CVOpenGLTextureGetCleanTexCoords(_ image: CVOpenGLTexture!, _ lowerLeft: UnsafeMutablePointer<GLfloat>, _ lowerRight: UnsafeMutablePointer<GLfloat>, _ upperRight: UnsafeMutablePointer<GLfloat>, _ upperLeft: UnsafeMutablePointer<GLfloat>) ``` | OS X 10.4 |

Modified CVOpenGLTextureGetName(CVOpenGLTexture!) -> GLuint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureGetTarget(CVOpenGLTexture!) -> GLenum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVOpenGLTextureIsFlipped(CVOpenGLTexture!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferCreate(CFAllocator!, Int, Int, OSType, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferCreate(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferCreate(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferCreateResolvedAttributesDictionary(CFAllocator!, CFArray!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferCreateResolvedAttributesDictionary(_ allocator: CFAllocator!, _ attributes: CFArray!, _ resolvedDictionaryOut: UnsafePointer<Unmanaged<CFDictionary>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferCreateResolvedAttributesDictionary(_ allocator: CFAllocator!, _ attributes: CFArray!, _ resolvedDictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferCreateWithBytes(CFAllocator!, Int, Int, OSType, UnsafeMutablePointer<Void>, Int, CVPixelBufferReleaseBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ baseAddress: UnsafePointer<()>, _ bytesPerRow: UInt, _ releaseCallback: CVPixelBufferReleaseBytesCallback, _ releaseRefCon: UnsafePointer<()>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferCreateWithIOSurface(CFAllocator!, IOSurface!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferCreateWithIOSurface(_ allocator: CFAllocator!, _ surface: IOSurface!, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferCreateWithIOSurface(_ allocator: CFAllocator!, _ surface: IOSurface!, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.6 |

Modified CVPixelBufferCreateWithPlanarBytes(CFAllocator!, Int, Int, OSType, UnsafeMutablePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ dataPtr: UnsafePointer<()>, _ dataSize: UInt, _ numberOfPlanes: UInt, _ planeBaseAddress: UnsafePointer<UnsafePointer<()>>, _ planeWidth: UnsafePointer<UInt>, _ planeHeight: UnsafePointer<UInt>, _ planeBytesPerRow: UnsafePointer<UInt>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback, _ releaseRefCon: UnsafePointer<()>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<Int>, _ planeHeight: UnsafeMutablePointer<Int>, _ planeBytesPerRow: UnsafeMutablePointer<Int>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferFillExtendedPixels(CVPixelBuffer!) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferGetBaseAddress(CVPixelBuffer!) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer!) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetBaseAddress(_ pixelBuffer: CVPixelBuffer!) -> UnsafeMutablePointer<Void> ``` | OS X 10.4 |

Modified CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer!, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.4 |

Modified CVPixelBufferGetBytesPerRow(CVPixelBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer!) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetDataSize(CVPixelBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer!) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetExtendedPixels(CVPixelBuffer!, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer!, _ extraColumnsOnLeft: UnsafePointer<UInt>, _ extraColumnsOnRight: UnsafePointer<UInt>, _ extraRowsOnTop: UnsafePointer<UInt>, _ extraRowsOnBottom: UnsafePointer<UInt>) ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer!, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>, _ extraColumnsOnRight: UnsafeMutablePointer<Int>, _ extraRowsOnTop: UnsafeMutablePointer<Int>, _ extraRowsOnBottom: UnsafeMutablePointer<Int>) ``` | OS X 10.4 |

Modified CVPixelBufferGetHeight(CVPixelBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer!) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetHeightOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetIOSurface(CVPixelBuffer!) -> Unmanaged<IOSurface>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CVPixelBufferGetPixelFormatType(CVPixelBuffer!) -> OSType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferGetPlaneCount(CVPixelBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer!) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferGetWidth(CVPixelBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer!) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferGetWidthOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` | OS X 10.10 |
| To | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` | OS X 10.4 |

Modified CVPixelBufferIsPlanar(CVPixelBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferLockBaseAddress(CVPixelBuffer!, CVOptionFlags) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferPoolCreate(CFAllocator!, CFDictionary!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBufferPool>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferPoolCreate(_ allocator: CFAllocator!, _ poolAttributes: CFDictionary!, _ pixelBufferAttributes: CFDictionary!, _ poolOut: UnsafePointer<Unmanaged<CVPixelBufferPool>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferPoolCreate(_ allocator: CFAllocator!, _ poolAttributes: CFDictionary!, _ pixelBufferAttributes: CFDictionary!, _ poolOut: UnsafeMutablePointer<Unmanaged<CVPixelBufferPool>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferPoolCreatePixelBuffer(CFAllocator!, CVPixelBufferPool!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferPoolCreatePixelBuffer(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferPoolCreatePixelBuffer(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.4 |

Modified CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(CFAllocator!, CVPixelBufferPool!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ auxAttributes: CFDictionary!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.10 |
| To | ``` func CVPixelBufferPoolCreatePixelBufferWithAuxAttributes(_ allocator: CFAllocator!, _ pixelBufferPool: CVPixelBufferPool!, _ auxAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` | OS X 10.7 |

Modified CVPixelBufferPoolGetAttributes(CVPixelBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferPoolGetPixelBufferAttributes(CVPixelBufferPool!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferPoolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelBufferReleaseBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleaseBytesCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CVPixelBufferReleaseBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void)> ``` |

Modified CVPixelBufferReleasePlanarBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleasePlanarBytesCallback = CFunctionPointer<((UnsafePointer<()>, ConstUnsafePointer<()>, UInt, UInt, UnsafePointer<ConstUnsafePointer<()>>) -> Void)> ``` |
| To | ``` typealias CVPixelBufferReleasePlanarBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void)> ``` |

Modified CVPixelBufferUnlockBaseAddress(CVPixelBuffer!, CVOptionFlags) -> CVReturn

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(CFAllocator!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelFormatDescriptionCreateWithPixelFormatType(CFAllocator!, OSType) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(CFDictionary!, OSType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVBufferMovieTimeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVBufferNonPropagatedAttachmentsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVBufferPropagatedAttachmentsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVBufferTimeScaleKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVBufferTimeValueKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferCGColorSpaceKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferChromaLocationBottomFieldKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocationTopFieldKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_Bottom

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_BottomLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_Center

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_DV420

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_Left

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_Top

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaLocation_TopLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaSubsamplingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaSubsampling_411

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaSubsampling_420

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferChromaSubsampling_422

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferCleanApertureHeightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferCleanApertureHorizontalOffsetKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferCleanApertureKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferCleanApertureVerticalOffsetKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferCleanApertureWidthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferColorPrimariesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferColorPrimaries_EBU_3213

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferColorPrimaries_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferColorPrimaries_P22

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCVImageBufferColorPrimaries_SMPTE_C

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferDisplayDimensionsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferDisplayHeightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferDisplayWidthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldDetailKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldDetailSpatialFirstLineEarly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldDetailSpatialFirstLineLate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldDetailTemporalBottomFirst

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferFieldDetailTemporalTopFirst

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferGammaLevelKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferICCProfileKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVImageBufferPixelAspectRatioHorizontalSpacingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferPixelAspectRatioKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferPixelAspectRatioVerticalSpacingKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferPreferredCleanApertureKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferTransferFunctionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferTransferFunction_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCVImageBufferTransferFunction_SMPTE_240M_1995

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVImageBufferTransferFunction_UseGamma

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVImageBufferYCbCrMatrixKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferYCbCrMatrix_ITU_R_601_4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferYCbCrMatrix_ITU_R_709_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVImageBufferYCbCrMatrix_SMPTE_240M_1995

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferInternalFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferMaximumMipmapLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferPoolMaximumBufferAgeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferPoolMinimumBufferCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferTarget

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLBufferWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLTextureCacheChromaSamplingModeAutomatic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLTextureCacheChromaSamplingModeBestPerformance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLTextureCacheChromaSamplingModeHighestQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVOpenGLTextureCacheChromaSamplingModeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferBytesPerRowAlignmentKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferCGBitmapContextCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferCGImageCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferExtendedPixelsBottomKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferExtendedPixelsLeftKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferExtendedPixelsRightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferExtendedPixelsTopKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferHeightKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelBufferIOSurfacePropertiesKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelBufferMemoryAllocatorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferOpenGLCompatibilityKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferPixelFormatTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferPlaneAlignmentKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelBufferPoolAllocationThresholdKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCVPixelBufferPoolFreeBufferNotification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCVPixelBufferPoolMaximumBufferAgeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferPoolMinimumBufferCountKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelBufferWidthKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatBitsPerBlock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatBlackBlock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCVPixelFormatBlockHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatBlockHorizontalAlignment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatBlockVerticalAlignment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatBlockWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatCGBitmapContextCompatibility

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatCGBitmapInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatCGImageCompatibility

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatCodecType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatConstant

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatContainsAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCVPixelFormatFillExtendedPixelsCallback

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatFourCC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatHorizontalSubsampling

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatOpenGLCompatibility

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatOpenGLFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatOpenGLInternalFormat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatOpenGLType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatPlanes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatQDCompatibility

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCVPixelFormatVerticalSubsampling

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

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
