---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreVideo.html
archived_at: '2026-07-18T02:56:23.512662Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreVideo Changes

## CoreVideo

Added CVFillExtendedPixelsCallBackData.init()Added CVFillExtendedPixelsCallBackData.init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack, refCon: UnsafeMutablePointer<Void>)Added CVPlanarComponentInfo.init()Added CVPlanarComponentInfo.init(offset: Int32, rowBytes: UInt32)Added CVPlanarPixelBufferInfo.init()Added CVPlanarPixelBufferInfo.init(componentInfo: (CVPlanarComponentInfo))Added CVPlanarPixelBufferInfo_YCbCrBiPlanar.init()Added CVPlanarPixelBufferInfo_YCbCrBiPlanar.init(componentInfoY: CVPlanarComponentInfo, componentInfoCbCr: CVPlanarComponentInfo)Added CVPlanarPixelBufferInfo_YCbCrPlanar.init()Added CVPlanarPixelBufferInfo_YCbCrPlanar.init(componentInfoY: CVPlanarComponentInfo, componentInfoCb: CVPlanarComponentInfo, componentInfoCr: CVPlanarComponentInfo)Added CVSMPTETime.init()Added CVSMPTETime.init(subframes: Int16, subframeDivisor: Int16, counter: UInt32, type: UInt32, flags: UInt32, hours: Int16, minutes: Int16, seconds: Int16, frames: Int16)Added CVTime.init()Added CVTime.init(timeValue: Int64, timeScale: Int32, flags: Int32)Added CVTimeStamp.init()Added CVTimeStamp.init(version: UInt32, videoTimeScale: Int32, videoTime: Int64, hostTime: UInt64, rateScalar: Double, videoRefreshPeriod: Int64, smpteTime: CVSMPTETime, flags: UInt64, reserved: UInt64)Modified CVFillExtendedPixelsCallBackData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack     var refCon: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct CVFillExtendedPixelsCallBackData {     var version: CFIndex     var fillCallBack: CVFillExtendedPixelsCallBack     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: CFIndex, fillCallBack fillCallBack: CVFillExtendedPixelsCallBack, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

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

Modified CVMetalTextureCacheCreateTextureFromImage(CFAllocator!, CVMetalTextureCache!, CVImageBuffer!, CFDictionary!, MTLPixelFormat, Int, Int, Int, UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn

|  | Declaration |
| --- | --- |
| From | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVMetalTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ pixelFormat: MTLPixelFormat, _ width: UInt, _ height: UInt, _ planeIndex: UInt, _ textureOut: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn ``` |
| To | ``` func CVMetalTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVMetalTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ pixelFormat: MTLPixelFormat, _ width: Int, _ height: Int, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVMetalTexture>?>) -> CVReturn ``` |

Modified CVOpenGLESTextureCacheCreateTextureFromImage(CFAllocator!, CVOpenGLESTextureCache!, CVImageBuffer!, CFDictionary!, GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, Int, UnsafeMutablePointer<Unmanaged<CVOpenGLESTexture>?>) -> CVReturn

|  | Declaration |
| --- | --- |
| From | ``` func CVOpenGLESTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVOpenGLESTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ target: GLenum, _ internalFormat: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ planeIndex: UInt, _ textureOut: UnsafeMutablePointer<Unmanaged<CVOpenGLESTexture>?>) -> CVReturn ``` |
| To | ``` func CVOpenGLESTextureCacheCreateTextureFromImage(_ allocator: CFAllocator!, _ textureCache: CVOpenGLESTextureCache!, _ sourceImage: CVImageBuffer!, _ textureAttributes: CFDictionary!, _ target: GLenum, _ internalFormat: GLint, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ planeIndex: Int, _ textureOut: UnsafeMutablePointer<Unmanaged<CVOpenGLESTexture>?>) -> CVReturn ``` |

Modified CVPixelBufferCreate(CFAllocator!, Int, Int, OSType, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreate(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreate(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |

Modified CVPixelBufferCreateWithBytes(CFAllocator!, Int, Int, OSType, UnsafeMutablePointer<Void>, Int, CVPixelBufferReleaseBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: UInt, _ releaseCallback: CVPixelBufferReleaseBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ baseAddress: UnsafeMutablePointer<Void>, _ bytesPerRow: Int, _ releaseCallback: CVPixelBufferReleaseBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |

Modified CVPixelBufferCreateWithPlanarBytes(CFAllocator!, Int, Int, OSType, UnsafeMutablePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, CVPixelBufferReleasePlanarBytesCallback, UnsafeMutablePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator!, _ width: UInt, _ height: UInt, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: UInt, _ numberOfPlanes: UInt, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<UInt>, _ planeHeight: UnsafeMutablePointer<UInt>, _ planeBytesPerRow: UnsafeMutablePointer<UInt>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |
| To | ``` func CVPixelBufferCreateWithPlanarBytes(_ allocator: CFAllocator!, _ width: Int, _ height: Int, _ pixelFormatType: OSType, _ dataPtr: UnsafeMutablePointer<Void>, _ dataSize: Int, _ numberOfPlanes: Int, _ planeBaseAddress: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ planeWidth: UnsafeMutablePointer<Int>, _ planeHeight: UnsafeMutablePointer<Int>, _ planeBytesPerRow: UnsafeMutablePointer<Int>, _ releaseCallback: CVPixelBufferReleasePlanarBytesCallback, _ releaseRefCon: UnsafeMutablePointer<Void>, _ pixelBufferAttributes: CFDictionary!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> CVReturn ``` |

Modified CVPixelBufferGetBaseAddressOfPlane(CVPixelBuffer!, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func CVPixelBufferGetBaseAddressOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> UnsafeMutablePointer<Void> ``` |

Modified CVPixelBufferGetBytesPerRow(CVPixelBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` |
| To | ``` func CVPixelBufferGetBytesPerRow(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |

Modified CVPixelBufferGetBytesPerRowOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` |
| To | ``` func CVPixelBufferGetBytesPerRowOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |

Modified CVPixelBufferGetDataSize(CVPixelBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` |
| To | ``` func CVPixelBufferGetDataSize(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |

Modified CVPixelBufferGetExtendedPixels(CVPixelBuffer!, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>)

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer!, _ extraColumnsOnLeft: UnsafeMutablePointer<UInt>, _ extraColumnsOnRight: UnsafeMutablePointer<UInt>, _ extraRowsOnTop: UnsafeMutablePointer<UInt>, _ extraRowsOnBottom: UnsafeMutablePointer<UInt>) ``` |
| To | ``` func CVPixelBufferGetExtendedPixels(_ pixelBuffer: CVPixelBuffer!, _ extraColumnsOnLeft: UnsafeMutablePointer<Int>, _ extraColumnsOnRight: UnsafeMutablePointer<Int>, _ extraRowsOnTop: UnsafeMutablePointer<Int>, _ extraRowsOnBottom: UnsafeMutablePointer<Int>) ``` |

Modified CVPixelBufferGetHeight(CVPixelBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` |
| To | ``` func CVPixelBufferGetHeight(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |

Modified CVPixelBufferGetHeightOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` |
| To | ``` func CVPixelBufferGetHeightOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |

Modified CVPixelBufferGetPlaneCount(CVPixelBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` |
| To | ``` func CVPixelBufferGetPlaneCount(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |

Modified CVPixelBufferGetWidth(CVPixelBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer!) -> UInt ``` |
| To | ``` func CVPixelBufferGetWidth(_ pixelBuffer: CVPixelBuffer!) -> Int ``` |

Modified CVPixelBufferGetWidthOfPlane(CVPixelBuffer!, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: UInt) -> UInt ``` |
| To | ``` func CVPixelBufferGetWidthOfPlane(_ pixelBuffer: CVPixelBuffer!, _ planeIndex: Int) -> Int ``` |

Modified CVPixelBufferReleasePlanarBytesCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferReleasePlanarBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UInt, UInt, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void)> ``` |
| To | ``` typealias CVPixelBufferReleasePlanarBytesCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<UnsafePointer<Void>>) -> Void)> ``` |

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
