---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreMedia.html
archived_at: '2026-07-18T02:56:23.100521Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreMedia Changes

## CoreMedia

Added CMBlockBufferCustomBlockSource.init()Added CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon: UnsafeMutablePointer<Void>)Added CMBufferCallbacks.init()Added CMBufferCallbacks.init(version: UInt32, refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration: CMBufferGetTimeCallback, isDataReady: CMBufferGetBooleanCallback, compare: CMBufferCompareCallback, dataBecameReadyNotification: Unmanaged<CFString>!, getSize: CMBufferGetSizeCallback)Added CMSampleTimingInfo.init()Added CMSampleTimingInfo.init(duration: CMTime, presentationTimeStamp: CMTime, decodeTimeStamp: CMTime)Added CMTime.init()Added CMTime.init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)Added CMTimeMapping.init()Added CMTimeMapping.init(source: CMTimeRange, target: CMTimeRange)Added CMTimeRange.init()Added CMTimeRange.init(start: CMTime, duration: CMTime)Added CMVideoDimensions.init()Added CMVideoDimensions.init(width: Int32, height: Int32)Modified CMBlockBufferCustomBlockSource [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt) -> UnsafeMutablePointer<Void>)>     var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UInt) -> Void)>     var refCon: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>     var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, AllocateBlock AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMBlockBufferCustomBlockSource.AllocateBlock

|  | Declaration |
| --- | --- |
| From | ``` var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UInt) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)> ``` |

Modified CMBlockBufferCustomBlockSource.FreeBlock

|  | Declaration |
| --- | --- |
| From | ``` var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UInt) -> Void)> ``` |
| To | ``` var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)> ``` |

Modified CMBufferCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback     var getPresentationTimeStamp: CMBufferGetTimeCallback     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback     var compare: CMBufferCompareCallback     var dataBecameReadyNotification: Unmanaged<CFString>!     var getSize: CMBufferGetSizeCallback } ``` |
| To | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback     var getPresentationTimeStamp: CMBufferGetTimeCallback     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback     var compare: CMBufferCompareCallback     var dataBecameReadyNotification: Unmanaged<CFString>!     var getSize: CMBufferGetSizeCallback     init()     init(version version: UInt32, refcon refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration getDuration: CMBufferGetTimeCallback, isDataReady isDataReady: CMBufferGetBooleanCallback, compare compare: CMBufferCompareCallback, dataBecameReadyNotification dataBecameReadyNotification: Unmanaged<CFString>!, getSize getSize: CMBufferGetSizeCallback) } ``` |

Modified CMSampleTimingInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMSampleTimingInfo {     var duration: CMTime     var presentationTimeStamp: CMTime     var decodeTimeStamp: CMTime } ``` |
| To | ``` struct CMSampleTimingInfo {     var duration: CMTime     var presentationTimeStamp: CMTime     var decodeTimeStamp: CMTime     init()     init(duration duration: CMTime, presentationTimeStamp presentationTimeStamp: CMTime, decodeTimeStamp decodeTimeStamp: CMTime) } ``` |

Modified CMTime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch } ``` |
| To | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch) } ``` |

Modified CMTimeMapping [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeMapping {     var source: CMTimeRange     var target: CMTimeRange } ``` |
| To | ``` struct CMTimeMapping {     var source: CMTimeRange     var target: CMTimeRange     init()     init(source source: CMTimeRange, target target: CMTimeRange) } ``` |

Modified CMTimeRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime } ``` |
| To | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime) } ``` |

Modified CMVideoDimensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMVideoDimensions {     var width: Int32     var height: Int32 } ``` |
| To | ``` struct CMVideoDimensions {     var width: Int32     var height: Int32     init()     init(width width: Int32, height height: Int32) } ``` |

Modified CMAudioFormatDescriptionCreate(CFAllocator!, UnsafePointer<AudioStreamBasicDescription>, Int, UnsafePointer<AudioChannelLayout>, Int, UnsafePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator!, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: UInt, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: UInt, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator!, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: Int, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |

Modified CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator!, _ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: UInt, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator!, _ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: Int, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |

Modified CMAudioFormatDescriptionGetChannelLayout(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout>

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription!, _ layoutSize: UnsafeMutablePointer<UInt>) -> UnsafePointer<AudioChannelLayout> ``` |
| To | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription!, _ layoutSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout> ``` |

Modified CMAudioFormatDescriptionGetFormatList(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem>

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription!, _ formatListSize: UnsafeMutablePointer<UInt>) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription!, _ formatListSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem> ``` |

Modified CMAudioFormatDescriptionGetMagicCookie(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription!, _ cookieSizeOut: UnsafeMutablePointer<UInt>) -> UnsafePointer<Void> ``` |
| To | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription!, _ cookieSizeOut: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |

Modified CMBlockBufferAccessDataBytes(CMBlockBuffer!, Int, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ length: UInt, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |

Modified CMBlockBufferAppendBufferReference(CMBlockBuffer!, CMBlockBuffer!, Int, Int, CMBlockBufferFlags) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer!, _ targetBBuf: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags) -> OSStatus ``` |
| To | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer!, _ targetBBuf: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |

Modified CMBlockBufferAppendMemoryBlock(CMBlockBuffer!, UnsafeMutablePointer<Void>, Int, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: UInt, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags) -> OSStatus ``` |
| To | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |

Modified CMBlockBufferCopyDataBytes(CMBlockBuffer!, Int, Int, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified CMBlockBufferCreateContiguous(CFAllocator!, CMBlockBuffer!, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator!, _ sourceBuffer: CMBlockBuffer!, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator!, _ sourceBuffer: CMBlockBuffer!, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMBlockBufferCreateWithBufferReference(CFAllocator!, CMBlockBuffer!, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator!, _ targetBuffer: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator!, _ targetBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMBlockBufferCreateWithMemoryBlock(CFAllocator!, UnsafeMutablePointer<Void>, Int, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: UInt, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMBlockBufferFillDataBytes(Int8, CMBlockBuffer!, Int, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: UInt, _ dataLength: UInt) -> OSStatus ``` |
| To | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |

Modified CMBlockBufferGetDataLength(CMBlockBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer!) -> UInt ``` |
| To | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer!) -> Int ``` |

Modified CMBlockBufferGetDataPointer(CMBlockBuffer!, Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ lengthAtOffset: UnsafeMutablePointer<UInt>, _ totalLength: UnsafeMutablePointer<UInt>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>, _ totalLength: UnsafeMutablePointer<Int>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |

Modified CMBlockBufferIsRangeContiguous(CMBlockBuffer!, Int, Int) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ length: UInt) -> Boolean ``` |
| To | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int) -> Boolean ``` |

Modified CMBlockBufferReplaceDataBytes(UnsafePointer<Void>, CMBlockBuffer!, Int, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: UInt, _ dataLength: UInt) -> OSStatus ``` |
| To | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |

Modified CMBufferGetSizeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetSizeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> UInt)> ``` |
| To | ``` typealias CMBufferGetSizeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Int)> ``` |

Modified CMBufferQueueGetTotalSize(CMBufferQueue!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue!) -> UInt ``` |
| To | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue!) -> Int ``` |

Modified CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator!, _ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: UInt, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator!, _ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: Int, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator!, _ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: UInt, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator!, _ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: Int, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMSampleBufferCreate(CFAllocator!, CMBlockBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMFormatDescription!, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>, CMItemCount, UnsafePointer<Int>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreate(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<UInt>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreate(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |

Modified CMSampleBufferCreateReady(CFAllocator!, CMBlockBuffer!, CMFormatDescription!, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>, CMItemCount, UnsafePointer<Int>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<UInt>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |

Modified CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer!, UnsafeMutablePointer<Int>, UnsafeMutablePointer<AudioBufferList>, Int, CFAllocator!, CFAllocator!, UInt32, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer!, _ bufferListSizeNeededOut: UnsafeMutablePointer<UInt>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: UInt, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer!, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer!, Int, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer!, _ packetDescriptionsSize: UInt, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<UInt>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer!, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer!, UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer!, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<UInt>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer!, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified CMSampleBufferGetSampleSize(CMSampleBuffer!, CMItemIndex) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex) -> UInt ``` |
| To | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex) -> Int ``` |

Modified CMSampleBufferGetSampleSizeArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Int>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer!, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<UInt>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer!, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |

Modified CMSampleBufferGetTotalSampleSize(CMSampleBuffer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer!) -> UInt ``` |
| To | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer!) -> Int ``` |

Modified CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianClosedCaptionDescriptionToHost(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianClosedCaptionDescriptionToHost(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianImageDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianImageDescriptionToHost(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianImageDescriptionToHost(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianMetadataDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianMetadataDescriptionToHost(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianMetadataDescriptionToHost(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianSoundDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianSoundDescriptionToHost(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianSoundDescriptionToHost(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianTextDescriptionToHost(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianTextDescriptionToHost(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianTimeCodeDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianTimeCodeDescriptionToHost(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianTimeCodeDescriptionToHost(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianClosedCaptionDescriptionToBig(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianClosedCaptionDescriptionToBig(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianImageDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianImageDescriptionToBig(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianImageDescriptionToBig(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianMetadataDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianMetadataDescriptionToBig(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianMetadataDescriptionToBig(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianSoundDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianSoundDescriptionToBig(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianSoundDescriptionToBig(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianTextDescriptionToBig(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianTextDescriptionToBig(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianTimeCodeDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianTimeCodeDescriptionToBig(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianTimeCodeDescriptionToBig(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: Int) -> OSStatus ``` |

Modified CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, CMMediaType, UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator!, _ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: UInt, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator!, _ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: Int, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |

Modified CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator!, _ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: UInt, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator!, _ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: Int, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFStringEncoding, CFString!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator!, _ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: UInt, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator!, _ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: Int, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionCreateFromH264ParameterSets(CFAllocator!, Int, UnsafePointer<UnsafePointer<UInt8>>, UnsafePointer<Int>, Int32, UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator!, _ parameterSetCount: UInt, _ parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, _ parameterSetSizes: UnsafePointer<UInt>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator!, _ parameterSetCount: Int, _ parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, _ parameterSetSizes: UnsafePointer<Int>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionGetH264ParameterSetAtIndex(CMFormatDescription!, Int, UnsafeMutablePointer<UnsafePointer<UInt8>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription!, _ parameterSetIndex: UInt, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<UInt>, _ parameterSetCountOut: UnsafeMutablePointer<UInt>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription!, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<Int>, _ parameterSetCountOut: UnsafeMutablePointer<Int>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` |

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
