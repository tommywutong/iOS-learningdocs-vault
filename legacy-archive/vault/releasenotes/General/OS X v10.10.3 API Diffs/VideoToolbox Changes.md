---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/VideoToolbox.html
archived_at: '2026-07-18T02:52:44.753266Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# VideoToolbox Changes

## VideoToolbox

Removed VTCompressionSessionOptionFlags.valueAdded VTCompressionSessionOptionFlags.init(rawValue: UInt32)Added VTDecompressionOutputCallbackRecord.init()Added VTDecompressionOutputCallbackRecord.init(decompressionOutputCallback: VTDecompressionOutputCallback, decompressionOutputRefCon: UnsafeMutablePointer<Void>)Modified VTCompressionSessionOptionFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTCompressionSessionOptionFlags : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` | RawOptionSet |
| To | ``` struct VTCompressionSessionOptionFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` | RawOptionSetType |

Modified VTCompressionSessionOptionFlags.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified VTDecompressionOutputCallbackRecord [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VTDecompressionOutputCallback     var decompressionOutputRefCon: UnsafePointer<()> } ``` |
| To | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VTDecompressionOutputCallback     var decompressionOutputRefCon: UnsafeMutablePointer<Void>     init()     init(decompressionOutputCallback decompressionOutputCallback: VTDecompressionOutputCallback, decompressionOutputRefCon decompressionOutputRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified VTDecompressionOutputCallbackRecord.decompressionOutputRefCon

|  | Declaration |
| --- | --- |
| From | ``` var decompressionOutputRefCon: UnsafePointer<()> ``` |
| To | ``` var decompressionOutputRefCon: UnsafeMutablePointer<Void> ``` |

Modified VTCompressionOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias VTCompressionOutputCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, OSStatus, VTEncodeInfoFlags, CMSampleBuffer!) -> Void)> ``` |
| To | ``` typealias VTCompressionOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTEncodeInfoFlags, CMSampleBuffer!) -> Void)> ``` |

Modified VTCompressionSessionBeginPass(VTCompressionSession!, VTCompressionSessionOptionFlags, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession!, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession!, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified VTCompressionSessionCompleteFrames(VTCompressionSession!, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTCompressionSessionCreate(CFAllocator!, Int32, Int32, CMVideoCodecType, CFDictionary!, CFDictionary!, CFAllocator!, VTCompressionOutputCallback, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Unmanaged<VTCompressionSession>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator!, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary!, _ sourceImageBufferAttributes: CFDictionary!, _ compressedDataAllocator: CFAllocator!, _ outputCallback: VTCompressionOutputCallback, _ outputCallbackRefCon: UnsafePointer<()>, _ compressionSessionOut: UnsafePointer<Unmanaged<VTCompressionSession>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator!, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary!, _ sourceImageBufferAttributes: CFDictionary!, _ compressedDataAllocator: CFAllocator!, _ outputCallback: VTCompressionOutputCallback, _ outputCallbackRefCon: UnsafeMutablePointer<Void>, _ compressionSessionOut: UnsafeMutablePointer<Unmanaged<VTCompressionSession>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTCompressionSessionEncodeFrame(VTCompressionSession!, CVImageBuffer!, CMTime, CMTime, CFDictionary!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession!, _ imageBuffer: CVImageBuffer!, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary!, _ sourceFrameRefCon: UnsafePointer<()>, _ infoFlagsOut: UnsafePointer<VTEncodeInfoFlags>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession!, _ imageBuffer: CVImageBuffer!, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary!, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus ``` | OS X 10.8 |

Modified VTCompressionSessionEndPass(VTCompressionSession!, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession!, _ furtherPassesRequestedOut: UnsafePointer<Boolean>, _ reserved: UnsafePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession!, _ furtherPassesRequestedOut: UnsafeMutablePointer<Boolean>, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified VTCompressionSessionGetPixelBufferPool(VTCompressionSession!) -> CVPixelBufferPool!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTCompressionSessionGetPixelBufferPool(_ session: VTCompressionSession!) -> Unmanaged<CVPixelBufferPool>! ``` | OS X 10.10 |
| To | ``` func VTCompressionSessionGetPixelBufferPool(_ session: VTCompressionSession!) -> CVPixelBufferPool! ``` | OS X 10.8 |

Modified VTCompressionSessionGetTimeRangesForNextPass(VTCompressionSession!, UnsafeMutablePointer<CMItemCount>, UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession!, _ timeRangeCountOut: UnsafePointer<CMItemCount>, _ timeRangeArrayOut: UnsafePointer<ConstUnsafePointer<CMTimeRange>>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession!, _ timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, _ timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus ``` |

Modified VTCompressionSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTCompressionSessionInvalidate(VTCompressionSession!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTCompressionSessionPrepareToEncodeFrames(VTCompressionSession!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified VTCopyVideoEncoderList(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTCopyVideoEncoderList(_ options: CFDictionary!, _ listOfVideoEncodersOut: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTCopyVideoEncoderList(_ options: CFDictionary!, _ listOfVideoEncodersOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTDecompressionOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias VTDecompressionOutputCallback = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, OSStatus, VTDecodeInfoFlags, CVImageBuffer!, CMTime, CMTime) -> Void)> ``` |
| To | ``` typealias VTDecompressionOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTDecodeInfoFlags, CVImageBuffer!, CMTime, CMTime) -> Void)> ``` |

Modified VTDecompressionSessionCanAcceptFormatDescription(VTDecompressionSession!, CMFormatDescription!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTDecompressionSessionCopyBlackPixelBuffer(VTDecompressionSession!, UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTDecompressionSessionCopyBlackPixelBuffer(_ session: VTDecompressionSession!, _ pixelBufferOut: UnsafePointer<Unmanaged<CVPixelBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTDecompressionSessionCopyBlackPixelBuffer(_ session: VTDecompressionSession!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTDecompressionSessionCreate(CFAllocator!, CMVideoFormatDescription!, CFDictionary!, CFDictionary!, UnsafePointer<VTDecompressionOutputCallbackRecord>, UnsafeMutablePointer<Unmanaged<VTDecompressionSession>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ videoDecoderSpecification: CFDictionary!, _ destinationImageBufferAttributes: CFDictionary!, _ outputCallback: ConstUnsafePointer<VTDecompressionOutputCallbackRecord>, _ decompressionSessionOut: UnsafePointer<Unmanaged<VTDecompressionSession>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ videoDecoderSpecification: CFDictionary!, _ destinationImageBufferAttributes: CFDictionary!, _ outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>, _ decompressionSessionOut: UnsafeMutablePointer<Unmanaged<VTDecompressionSession>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTDecompressionSessionDecodeFrame(VTDecompressionSession!, CMSampleBuffer!, VTDecodeFrameFlags, UnsafeMutablePointer<Void>, UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession!, _ sampleBuffer: CMSampleBuffer!, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafePointer<()>, _ infoFlagsOut: UnsafePointer<VTDecodeInfoFlags>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession!, _ sampleBuffer: CMSampleBuffer!, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus ``` | OS X 10.8 |

Modified VTDecompressionSessionFinishDelayedFrames(VTDecompressionSession!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTDecompressionSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTDecompressionSessionInvalidate(VTDecompressionSession!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTDecompressionSessionWaitForAsynchronousFrames(VTDecompressionSession!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTFrameSiloCallFunctionForEachSampleBuffer(VTFrameSilo!, CMTimeRange, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, CMSampleBuffer!) -> OSStatus)>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo!, _ timeRange: CMTimeRange, _ callbackInfo: UnsafePointer<()>, _ callback: CFunctionPointer<((UnsafePointer<()>, CMSampleBuffer!) -> OSStatus)>) -> OSStatus ``` |
| To | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo!, _ timeRange: CMTimeRange, _ callbackInfo: UnsafeMutablePointer<Void>, _ callback: CFunctionPointer<((UnsafeMutablePointer<Void>, CMSampleBuffer!) -> OSStatus)>) -> OSStatus ``` |

Modified VTFrameSiloCreate(CFAllocator!, CFURL!, CMTimeRange, CFDictionary!, UnsafeMutablePointer<Unmanaged<VTFrameSilo>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ siloOut: UnsafePointer<Unmanaged<VTFrameSilo>?>) -> OSStatus ``` |
| To | ``` func VTFrameSiloCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ siloOut: UnsafeMutablePointer<Unmanaged<VTFrameSilo>?>) -> OSStatus ``` |

Modified VTFrameSiloGetProgressOfCurrentPass(VTFrameSilo!, UnsafeMutablePointer<Float32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloGetProgressOfCurrentPass(_ silo: VTFrameSilo!, _ progressOut: UnsafePointer<Float32>) -> OSStatus ``` |
| To | ``` func VTFrameSiloGetProgressOfCurrentPass(_ silo: VTFrameSilo!, _ progressOut: UnsafeMutablePointer<Float32>) -> OSStatus ``` |

Modified VTFrameSiloSetTimeRangesForNextPass(VTFrameSilo!, CMItemCount, UnsafePointer<CMTimeRange>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloSetTimeRangesForNextPass(_ silo: VTFrameSilo!, _ timeRangeCount: CMItemCount, _ timeRangeArray: ConstUnsafePointer<CMTimeRange>) -> OSStatus ``` |
| To | ``` func VTFrameSiloSetTimeRangesForNextPass(_ silo: VTFrameSilo!, _ timeRangeCount: CMItemCount, _ timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus ``` |

Modified VTMultiPassStorageCreate(CFAllocator!, CFURL!, CMTimeRange, CFDictionary!, UnsafeMutablePointer<Unmanaged<VTMultiPassStorage>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func VTMultiPassStorageCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ multiPassStorageOut: UnsafePointer<Unmanaged<VTMultiPassStorage>?>) -> OSStatus ``` |
| To | ``` func VTMultiPassStorageCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ multiPassStorageOut: UnsafeMutablePointer<Unmanaged<VTMultiPassStorage>?>) -> OSStatus ``` |

Modified VTPixelTransferSessionCreate(CFAllocator!, UnsafeMutablePointer<Unmanaged<VTPixelTransferSession>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTPixelTransferSessionCreate(_ allocator: CFAllocator!, _ pixelTransferSessionOut: UnsafePointer<Unmanaged<VTPixelTransferSession>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTPixelTransferSessionCreate(_ allocator: CFAllocator!, _ pixelTransferSessionOut: UnsafeMutablePointer<Unmanaged<VTPixelTransferSession>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTPixelTransferSessionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTPixelTransferSessionInvalidate(VTPixelTransferSession!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTPixelTransferSessionTransferImage(VTPixelTransferSession!, CVPixelBuffer!, CVPixelBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified VTSessionCopyProperty(VTSession!, CFString!, CFAllocator!, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTSessionCopyProperty(_ session: VTSessionRef!, _ propertyKey: CFString!, _ allocator: CFAllocator!, _ propertyValueOut: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTSessionCopyProperty(_ session: VTSession!, _ propertyKey: CFString!, _ allocator: CFAllocator!, _ propertyValueOut: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.8 |

Modified VTSessionCopySerializableProperties(VTSession!, CFAllocator!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTSessionCopySerializableProperties(_ session: VTSessionRef!, _ allocator: CFAllocator!, _ dictionaryOut: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTSessionCopySerializableProperties(_ session: VTSession!, _ allocator: CFAllocator!, _ dictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTSessionCopySupportedPropertyDictionary(VTSession!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTSessionCopySupportedPropertyDictionary(_ session: VTSessionRef!, _ supportedPropertyDictionaryOut: UnsafePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTSessionCopySupportedPropertyDictionary(_ session: VTSession!, _ supportedPropertyDictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` | OS X 10.8 |

Modified VTSessionRef

|  | Declaration |
| --- | --- |
| From | ``` typealias VTSessionRef = AnyObject ``` |
| To | ``` typealias VTSessionRef = VTSession ``` |

Modified VTSessionSetProperties(VTSession!, CFDictionary!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTSessionSetProperties(_ session: VTSessionRef!, _ propertyDictionary: CFDictionary!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTSessionSetProperties(_ session: VTSession!, _ propertyDictionary: CFDictionary!) -> OSStatus ``` | OS X 10.8 |

Modified VTSessionSetProperty(VTSession!, CFString!, AnyObject!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func VTSessionSetProperty(_ session: VTSessionRef!, _ propertyKey: CFString!, _ propertyValue: AnyObject!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func VTSessionSetProperty(_ session: VTSession!, _ propertyKey: CFString!, _ propertyValue: AnyObject!) -> OSStatus ``` | OS X 10.8 |

Modified kVTCompressionPropertyKey_AllowFrameReordering

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_AllowTemporalCompression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_AspectRatio16x9

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_AverageBitRate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_CleanAperture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_ColorPrimaries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_DataRateLimits

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_Depth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_ExpectedDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_ExpectedFrameRate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_FieldCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_FieldDetail

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_H264EntropyMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTCompressionPropertyKey_ICCProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MaxFrameDelayCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MaxH264SliceBytes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MaxKeyFrameInterval

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MoreFramesAfterEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_MoreFramesBeforeStart

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_NumberOfPendingFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_PixelAspectRatio

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_PixelBufferPoolIsShared

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_PixelTransferProperties

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_ProfileLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_ProgressiveScan

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_Quality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_RealTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTCompressionPropertyKey_SourceFrameCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_TransferFunction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTCompressionPropertyKey_YCbCrMatrix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_ContentHasInterframeDependencies

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_DeinterlaceMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_FieldMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_OnlyTheseFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTDecompressionPropertyKey_PixelBufferPool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_PixelBufferPoolIsShared

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_PixelTransferProperties

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_ReducedCoefficientDecode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_ReducedFrameDelivery

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_ReducedResolutionDecode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_ThreadCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTDecompressionProperty_DeinterlaceMode_Temporal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_DeinterlaceMode_VerticalFilter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_FieldMode_BothFields

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_FieldMode_BottomFieldOnly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_FieldMode_DeinterlaceFields

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_FieldMode_SingleField

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_FieldMode_TopFieldOnly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_OnlyTheseFrames_AllFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_OnlyTheseFrames_IFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_OnlyTheseFrames_KeyFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionResolutionKey_Height

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDecompressionResolutionKey_Width

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDownsamplingMode_Average

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTDownsamplingMode_Decimate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTEncodeFrameOptionKey_ForceKeyFrame

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTH264EntropyMode_CABAC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTH264EntropyMode_CAVLC

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTPixelTransferPropertyKey_DestinationCleanAperture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DestinationColorPrimaries

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DestinationICCProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DestinationPixelAspectRatio

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DestinationTransferFunction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DestinationYCbCrMatrix

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_DownsamplingMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPixelTransferPropertyKey_ScalingMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H263_Profile0_Level10

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H263_Profile0_Level45

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H263_Profile3_Level45

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_1_3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_3_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_3_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_3_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_4_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Baseline_4_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Baseline_4_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Baseline_5_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Baseline_5_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Baseline_5_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Baseline_AutoLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Extended_5_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Extended_AutoLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_3_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_3_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_3_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_4_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_4_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_4_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_5_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_High_5_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_5_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_High_AutoLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Main_3_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_3_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_3_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_4_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_4_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_4_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Main_5_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_H264_Main_5_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Main_5_2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_H264_Main_AutoLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTProfileLevel_MP4V_AdvancedSimple_L0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_AdvancedSimple_L1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_AdvancedSimple_L2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_AdvancedSimple_L3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_AdvancedSimple_L4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Main_L2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Main_L3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Main_L4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Simple_L0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Simple_L1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Simple_L2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTProfileLevel_MP4V_Simple_L3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyDocumentationKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyReadWriteStatusKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyReadWriteStatus_ReadOnly

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyReadWriteStatus_ReadWrite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyShouldBeSerializedKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertySupportedValueListKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertySupportedValueMaximumKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertySupportedValueMinimumKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyType_Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyType_Enumeration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTPropertyType_Number

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTScalingMode_CropSourceToCleanAperture

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTScalingMode_Letterbox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTScalingMode_Normal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTScalingMode_Trim

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTVideoEncoderList_CodecName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderList_CodecType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderList_DisplayName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderList_EncoderID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderList_EncoderName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kVTVideoEncoderSpecification_EncoderID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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
