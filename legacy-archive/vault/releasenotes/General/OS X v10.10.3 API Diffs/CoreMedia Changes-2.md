---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreMedia.html
archived_at: '2026-07-18T02:52:13.578290Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreMedia Changes

## CoreMedia

Removed CMTimeFlags.valueAdded CMBlockBufferCustomBlockSource.init()Added CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon: UnsafeMutablePointer<Void>)Added CMBufferCallbacks.init()Added CMBufferCallbacks.init(version: UInt32, refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration: CMBufferGetTimeCallback, isDataReady: CMBufferGetBooleanCallback, compare: CMBufferCompareCallback, dataBecameReadyNotification: Unmanaged<CFString>!, getSize: CMBufferGetSizeCallback)Added CMSampleTimingInfo.init()Added CMSampleTimingInfo.init(duration: CMTime, presentationTimeStamp: CMTime, decodeTimeStamp: CMTime)Added CMTime.init()Added CMTime.init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)Added CMTimeFlags.init(rawValue: UInt32)Added CMTimeMapping.init()Added CMTimeMapping.init(source: CMTimeRange, target: CMTimeRange)Added CMTimeRange.init()Added CMTimeRange.init(start: CMTime, duration: CMTime)Added CMVideoDimensions.init()Added CMVideoDimensions.init(width: Int32, height: Int32)Added CMAudioSampleBufferCreateReadyWithPacketDescriptions(CFAllocator!, CMBlockBuffer!, CMFormatDescription!, CMItemCount, CMTime, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatusAdded CMSampleBufferCallBlockForEachSample(CMSampleBuffer!,((CMSampleBuffer!, CMItemCount) -> OSStatus)!) -> OSStatusAdded CMSampleBufferCreateReady(CFAllocator!, CMBlockBuffer!, CMFormatDescription!, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>, CMItemCount, UnsafePointer<Int>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatusAdded CMSampleBufferCreateReadyWithImageBuffer(CFAllocator!, CVImageBuffer!, CMVideoFormatDescription!, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatusAdded CMSampleBufferInvalidateHandlerAdded CMSampleBufferSetInvalidateHandler(CMSampleBuffer!, CMSampleBufferInvalidateHandler!) -> OSStatusModified CMBlockBufferCustomBlockSource [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: CFunctionPointer<((UnsafePointer<()>, UInt) -> UnsafePointer<()>)>     var FreeBlock: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, UInt) -> Void)>     var refCon: UnsafePointer<()> } ``` |
| To | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>     var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, AllocateBlock AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

Modified CMBlockBufferCustomBlockSource.AllocateBlock

|  | Declaration |
| --- | --- |
| From | ``` var AllocateBlock: CFunctionPointer<((UnsafePointer<()>, UInt) -> UnsafePointer<()>)> ``` |
| To | ``` var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)> ``` |

Modified CMBlockBufferCustomBlockSource.FreeBlock

|  | Declaration |
| --- | --- |
| From | ``` var FreeBlock: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, UInt) -> Void)> ``` |
| To | ``` var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)> ``` |

Modified CMBlockBufferCustomBlockSource.refCon

|  | Declaration |
| --- | --- |
| From | ``` var refCon: UnsafePointer<()> ``` |
| To | ``` var refCon: UnsafeMutablePointer<Void> ``` |

Modified CMBufferCallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafePointer<()>     var getDecodeTimeStamp: CMBufferGetTimeCallback     var getPresentationTimeStamp: CMBufferGetTimeCallback     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback     var compare: CMBufferCompareCallback     var dataBecameReadyNotification: Unmanaged<CFString>!     var getSize: CMBufferGetSizeCallback } ``` |
| To | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback     var getPresentationTimeStamp: CMBufferGetTimeCallback     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback     var compare: CMBufferCompareCallback     var dataBecameReadyNotification: Unmanaged<CFString>!     var getSize: CMBufferGetSizeCallback     init()     init(version version: UInt32, refcon refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration getDuration: CMBufferGetTimeCallback, isDataReady isDataReady: CMBufferGetBooleanCallback, compare compare: CMBufferCompareCallback, dataBecameReadyNotification dataBecameReadyNotification: Unmanaged<CFString>!, getSize getSize: CMBufferGetSizeCallback) } ``` |

Modified CMBufferCallbacks.refcon

|  | Declaration |
| --- | --- |
| From | ``` var refcon: UnsafePointer<()> ``` |
| To | ``` var refcon: UnsafeMutablePointer<Void> ``` |

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

Modified CMTimeFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMTimeFlags : RawOptionSet {     init(_ value: UInt32)     var value: UInt32     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` | RawOptionSet |
| To | ``` struct CMTimeFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` | RawOptionSetType |

Modified CMTimeFlags.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

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

Modified CMAttachmentBearerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAttachmentBearerRef = AnyObject ``` |
| To | ``` typealias CMAttachmentBearerRef = CMAttachmentBearer ``` |

Modified CMAudioDeviceClockCreate(CFAllocator!, CFString!, UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioDeviceClockCreate(_ allocator: CFAllocator!, _ deviceUID: CFString!, _ clockOut: UnsafePointer<Unmanaged<CMClock>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioDeviceClockCreate(_ allocator: CFAllocator!, _ deviceUID: CFString!, _ clockOut: UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus ``` | OS X 10.8 |

Modified CMAudioDeviceClockCreateFromAudioDeviceID(CFAllocator!, AudioDeviceID, UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioDeviceClockCreateFromAudioDeviceID(_ allocator: CFAllocator!, _ deviceID: AudioDeviceID, _ clockOut: UnsafePointer<Unmanaged<CMClock>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioDeviceClockCreateFromAudioDeviceID(_ allocator: CFAllocator!, _ deviceID: AudioDeviceID, _ clockOut: UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus ``` | OS X 10.8 |

Modified CMAudioDeviceClockGetAudioDevice(CMClock!, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<AudioDeviceID>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioDeviceClockGetAudioDevice(_ clock: CMClock!, _ deviceUIDOut: UnsafePointer<Unmanaged<CFString>?>, _ deviceIDOut: UnsafePointer<AudioDeviceID>, _ trackingDefaultDeviceOut: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioDeviceClockGetAudioDevice(_ clock: CMClock!, _ deviceUIDOut: UnsafeMutablePointer<Unmanaged<CFString>?>, _ deviceIDOut: UnsafeMutablePointer<AudioDeviceID>, _ trackingDefaultDeviceOut: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.8 |

Modified CMAudioDeviceClockSetAudioDeviceID(CMClock!, AudioDeviceID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMAudioDeviceClockSetAudioDeviceUID(CMClock!, CFString!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(CFAllocator!, CMAudioFormatDescription!, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ audioFormatDescription: CMAudioFormatDescription!, _ soundDescriptionFlavor: CFString!, _ soundDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ audioFormatDescription: CMAudioFormatDescription!, _ soundDescriptionFlavor: CFString!, _ soundDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMAudioFormatDescriptionCreate(CFAllocator!, UnsafePointer<AudioStreamBasicDescription>, Int, UnsafePointer<AudioChannelLayout>, Int, UnsafePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator!, _ asbd: ConstUnsafePointer<AudioStreamBasicDescription>, _ layoutSize: UInt, _ layout: ConstUnsafePointer<AudioChannelLayout>, _ magicCookieSize: UInt, _ magicCookie: ConstUnsafePointer<()>, _ extensions: CFDictionary!, _ outDesc: UnsafePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator!, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: Int, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFString!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ soundDescriptionBlockBuffer: CMBlockBuffer!, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ soundDescriptionBlockBuffer: CMBlockBuffer!, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |

Modified CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator!, _ soundDescriptionData: ConstUnsafePointer<UInt8>, _ soundDescriptionSize: UInt, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator!, _ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: Int, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |

Modified CMAudioFormatDescriptionCreateSummary(CFAllocator!, CFArray!, UInt32, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateSummary(_ allocator: CFAllocator!, _ formatDescriptionArray: CFArray!, _ flags: UInt32, _ summaryFormatDescriptionOut: UnsafePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionCreateSummary(_ allocator: CFAllocator!, _ formatDescriptionArray: CFArray!, _ flags: UInt32, _ summaryFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionEqual(CMAudioFormatDescription!, CMAudioFormatDescription!, CMAudioFormatDescriptionMask, UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription!, _ desc2: CMAudioFormatDescription!, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafePointer<CMAudioFormatDescriptionMask>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription!, _ desc2: CMAudioFormatDescription!, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Boolean ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetChannelLayout(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription!, _ layoutSize: UnsafePointer<UInt>) -> ConstUnsafePointer<AudioChannelLayout> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription!, _ layoutSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout> ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetFormatList(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription!, _ formatListSize: UnsafePointer<UInt>) -> ConstUnsafePointer<AudioFormatListItem> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription!, _ formatListSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem> ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetMagicCookie(CMAudioFormatDescription!, UnsafeMutablePointer<Int>) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription!, _ cookieSizeOut: UnsafePointer<UInt>) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription!, _ cookieSizeOut: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetMostCompatibleFormat(CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription!) -> ConstUnsafePointer<AudioFormatListItem> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem> ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetRichestDecodableFormat(CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription!) -> ConstUnsafePointer<AudioFormatListItem> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem> ``` | OS X 10.7 |

Modified CMAudioFormatDescriptionGetStreamBasicDescription(CMAudioFormatDescription!) -> UnsafePointer<AudioStreamBasicDescription>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription!) -> ConstUnsafePointer<AudioStreamBasicDescription> ``` | OS X 10.10 |
| To | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioStreamBasicDescription> ``` | OS X 10.7 |

Modified CMAudioSampleBufferCreateWithPacketDescriptions(CFAllocator!, CMBlockBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMFormatDescription!, CMItemCount, CMTime, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafePointer<()>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: ConstUnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferAccessDataBytes(CMBlockBuffer!, Int, Int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ length: UInt, _ temporaryBlock: UnsafePointer<()>, _ returnedPointer: UnsafePointer<UnsafePointer<Int8>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferAppendBufferReference(CMBlockBuffer!, CMBlockBuffer!, Int, Int, CMBlockBufferFlags) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer!, _ targetBBuf: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer!, _ targetBBuf: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferAppendMemoryBlock(CMBlockBuffer!, UnsafeMutablePointer<Void>, Int, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer!, _ memoryBlock: UnsafePointer<()>, _ blockLength: UInt, _ blockAllocator: CFAllocator!, _ customBlockSource: ConstUnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferAssureBlockMemory(CMBlockBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBlockBufferCopyDataBytes(CMBlockBuffer!, Int, Int, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ destination: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferCreateContiguous(CFAllocator!, CMBlockBuffer!, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator!, _ sourceBuffer: CMBlockBuffer!, _ blockAllocator: CFAllocator!, _ customBlockSource: ConstUnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator!, _ sourceBuffer: CMBlockBuffer!, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferCreateEmpty(CFAllocator!, UInt32, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferCreateEmpty(_ structureAllocator: CFAllocator!, _ subBlockCapacity: UInt32, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferCreateEmpty(_ structureAllocator: CFAllocator!, _ subBlockCapacity: UInt32, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferCreateWithBufferReference(CFAllocator!, CMBlockBuffer!, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator!, _ targetBuffer: CMBlockBuffer!, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator!, _ targetBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferCreateWithMemoryBlock(CFAllocator!, UnsafeMutablePointer<Void>, Int, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, Int, Int, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator!, _ memoryBlock: UnsafePointer<()>, _ blockLength: UInt, _ blockAllocator: CFAllocator!, _ customBlockSource: ConstUnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: UInt, _ dataLength: UInt, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferFillDataBytes(Int8, CMBlockBuffer!, Int, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: UInt, _ dataLength: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferGetDataLength(CMBlockBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer!) -> Int ``` | OS X 10.7 |

Modified CMBlockBufferGetDataPointer(CMBlockBuffer!, Int, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ lengthAtOffset: UnsafePointer<UInt>, _ totalLength: UnsafePointer<UInt>, _ dataPointer: UnsafePointer<UnsafePointer<Int8>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>, _ totalLength: UnsafeMutablePointer<Int>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` | OS X 10.7 |

Modified CMBlockBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBlockBufferIsEmpty(CMBlockBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBlockBufferIsRangeContiguous(CMBlockBuffer!, Int, Int) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer!, _ offset: UInt, _ length: UInt) -> Boolean ``` | OS X 10.10 |
| To | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int) -> Boolean ``` | OS X 10.7 |

Modified CMBlockBufferReplaceDataBytes(UnsafePointer<Void>, CMBlockBuffer!, Int, Int) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: ConstUnsafePointer<()>, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: UInt, _ dataLength: UInt) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferCompareCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferCompareCallback = CFunctionPointer<((CMBufferRef!, CMBufferRef!, UnsafePointer<()>) -> CFComparisonResult)> ``` |
| To | ``` typealias CMBufferCompareCallback = CFunctionPointer<((CMBuffer!, CMBuffer!, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |

Modified CMBufferGetBooleanCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetBooleanCallback = CFunctionPointer<((CMBufferRef!, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias CMBufferGetBooleanCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified CMBufferGetSizeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetSizeCallback = CFunctionPointer<((CMBufferRef!, UnsafePointer<()>) -> UInt)> ``` |
| To | ``` typealias CMBufferGetSizeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Int)> ``` |

Modified CMBufferGetTimeCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetTimeCallback = CFunctionPointer<((CMBufferRef!, UnsafePointer<()>) -> CMTime)> ``` |
| To | ``` typealias CMBufferGetTimeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> CMTime)> ``` |

Modified CMBufferQueueCallForEachBuffer(CMBufferQueue!, CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBufferRef!, UnsafePointer<()>) -> OSStatus)>, _ refcon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueContainsEndOfData(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueCreate(CFAllocator!, CMItemCount, UnsafePointer<CMBufferCallbacks>, UnsafeMutablePointer<Unmanaged<CMBufferQueue>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueCreate(_ allocator: CFAllocator!, _ capacity: CMItemCount, _ callbacks: ConstUnsafePointer<CMBufferCallbacks>, _ queueOut: UnsafePointer<Unmanaged<CMBufferQueue>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueCreate(_ allocator: CFAllocator!, _ capacity: CMItemCount, _ callbacks: UnsafePointer<CMBufferCallbacks>, _ queueOut: UnsafeMutablePointer<Unmanaged<CMBufferQueue>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueEnqueue(CMBufferQueue!, CMBuffer!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueEnqueue(_ queue: CMBufferQueue!, _ buf: CMBufferRef!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueEnqueue(_ queue: CMBufferQueue!, _ buf: CMBuffer!) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueGetBufferCount(CMBufferQueue!) -> CMItemCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> ConstUnsafePointer<CMBufferCallbacks> ``` | OS X 10.10 |
| To | ``` func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks> ``` | OS X 10.7 |

Modified CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> ConstUnsafePointer<CMBufferCallbacks> ``` | OS X 10.10 |
| To | ``` func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks> ``` | OS X 10.7 |

Modified CMBufferQueueGetDuration(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetHead(CMBufferQueue!) -> Unmanaged<CMBuffer>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueGetHead(_ queue: CMBufferQueue!) -> Unmanaged<CMBufferRef>! ``` | OS X 10.10 |
| To | ``` func CMBufferQueueGetHead(_ queue: CMBufferQueue!) -> Unmanaged<CMBuffer>! ``` | OS X 10.7 |

Modified CMBufferQueueGetMaxPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueGetTotalSize(CMBufferQueue!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue!) -> UInt ``` |
| To | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue!) -> Int ``` |

Modified CMBufferQueueGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueInstallTrigger(CMBufferQueue!, CMBufferQueueTriggerCallback, UnsafeMutablePointer<Void>, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafePointer<()>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue!, CMBufferQueueTriggerCallback, UnsafeMutablePointer<Void>, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafePointer<()>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueIsAtEndOfData(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueIsEmpty(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueMarkEndOfData(CMBufferQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueRemoveTrigger(CMBufferQueue!, CMBufferQueueTriggerToken) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueReset(CMBufferQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueResetWithCallback(CMBufferQueue!, CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBufferRef!, UnsafePointer<()>) -> Void)>, _ refcon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Void)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueSetValidationCallback(CMBufferQueue!, CMBufferValidationCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue!, _ validationCallback: CMBufferValidationCallback, _ validationRefCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue!, _ validationCallback: CMBufferValidationCallback, _ validationRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMBufferQueueTestTrigger(CMBufferQueue!, CMBufferQueueTriggerToken) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMBufferQueueTriggerCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferQueueTriggerCallback = CFunctionPointer<((UnsafePointer<()>, CMBufferQueueTriggerToken) -> Void)> ``` |
| To | ``` typealias CMBufferQueueTriggerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CMBufferQueueTriggerToken) -> Void)> ``` |

Modified CMBufferRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferRef = AnyObject ``` |
| To | ``` typealias CMBufferRef = CMBuffer ``` |

Modified CMBufferValidationCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferValidationCallback = CFunctionPointer<((CMBufferQueue!, CMBufferRef!, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias CMBufferValidationCallback = CFunctionPointer<((CMBufferQueue!, CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified CMClockConvertHostTimeToSystemUnits(CMTime) -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockGetAnchorTime(CMClock!, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<CMTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMClockGetAnchorTime(_ clock: CMClock!, _ outClockTime: UnsafePointer<CMTime>, _ outReferenceClockTime: UnsafePointer<CMTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMClockGetAnchorTime(_ clock: CMClock!, _ outClockTime: UnsafeMutablePointer<CMTime>, _ outReferenceClockTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` | OS X 10.8 |

Modified CMClockGetHostTimeClock() -> CMClock!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMClockGetHostTimeClock() -> Unmanaged<CMClock>! ``` | OS X 10.10 |
| To | ``` func CMClockGetHostTimeClock() -> CMClock! ``` | OS X 10.8 |

Modified CMClockGetTime(CMClock!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockInvalidate(CMClock!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockMakeHostTimeFromSystemUnits(UInt64) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockMightDrift(CMClock!, CMClock!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMClockOrTimebaseRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CMClockOrTimebaseRef = AnyObject ``` |
| To | ``` typealias CMClockOrTimebaseRef = CMClockOrTimebase ``` |

Modified CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(CFAllocator!, CMClosedCaptionFormatDescription!, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionFormatDescription: CMClosedCaptionFormatDescription!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionFormatDescription: CMClosedCaptionFormatDescription!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFString!, UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionDescriptionBlockBuffer: CMBlockBuffer!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionDescriptionBlockBuffer: CMBlockBuffer!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |

Modified CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator!, _ closedCaptionDescriptionData: ConstUnsafePointer<UInt8>, _ closedCaptionDescriptionSize: UInt, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator!, _ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: Int, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |

Modified CMCopyDictionaryOfAttachments(CFAllocator!, CMAttachmentBearer!, CMAttachmentMode) -> Unmanaged<CFDictionary>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMCopyDictionaryOfAttachments(_ allocator: CFAllocator!, _ target: CMAttachmentBearerRef!, _ attachmentMode: CMAttachmentMode) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func CMCopyDictionaryOfAttachments(_ allocator: CFAllocator!, _ target: CMAttachmentBearer!, _ attachmentMode: CMAttachmentMode) -> Unmanaged<CFDictionary>! ``` | OS X 10.7 |

Modified CMFormatDescriptionCreate(CFAllocator!, CMMediaType, FourCharCode, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMFormatDescriptionCreate(_ allocator: CFAllocator!, _ mediaType: CMMediaType, _ mediaSubtype: FourCharCode, _ extensions: CFDictionary!, _ descOut: UnsafePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMFormatDescriptionCreate(_ allocator: CFAllocator!, _ mediaType: CMMediaType, _ mediaSubtype: FourCharCode, _ extensions: CFDictionary!, _ descOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMFormatDescriptionEqual(CMFormatDescription!, CMFormatDescription!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMFormatDescriptionEqualIgnoringExtensionKeys(CMFormatDescription!, CMFormatDescription!, AnyObject!, AnyObject!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMFormatDescriptionGetExtension(CMFormatDescription!, CFString!) -> Unmanaged<CFPropertyList>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMFormatDescriptionGetExtension(_ desc: CMFormatDescription!, _ extensionKey: CFString!) -> Unmanaged<CFPropertyListRef>! ``` | OS X 10.10 |
| To | ``` func CMFormatDescriptionGetExtension(_ desc: CMFormatDescription!, _ extensionKey: CFString!) -> Unmanaged<CFPropertyList>! ``` | OS X 10.7 |

Modified CMFormatDescriptionGetExtensions(CMFormatDescription!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMFormatDescriptionGetMediaSubType(CMFormatDescription!) -> FourCharCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMFormatDescriptionGetMediaType(CMFormatDescription!) -> CMMediaType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMFormatDescriptionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMGetAttachment(CMAttachmentBearer!, CFString!, UnsafeMutablePointer<CMAttachmentMode>) -> Unmanaged<AnyObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMGetAttachment(_ target: CMAttachmentBearerRef!, _ key: CFString!, _ attachmentModeOut: UnsafePointer<CMAttachmentMode>) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func CMGetAttachment(_ target: CMAttachmentBearer!, _ key: CFString!, _ attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>) -> Unmanaged<AnyObject>! ``` | OS X 10.7 |

Modified CMMemoryPoolCreate(CFDictionary!) -> Unmanaged<CMMemoryPool>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMMemoryPoolFlush(CMMemoryPool!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMMemoryPoolGetAllocator(CMMemoryPool!) -> Unmanaged<CFAllocator>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMMemoryPoolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMMemoryPoolInvalidate(CMMemoryPool!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMMetadataCreateIdentifierForKeyAndKeySpace(CFAllocator!, AnyObject!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator!, _ key: AnyObject!, _ keySpace: CFString!, _ identifierOut: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator!, _ key: AnyObject!, _ keySpace: CFString!, _ identifierOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |

Modified CMMetadataCreateKeyFromIdentifier(CFAllocator!, CFString!, UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |

Modified CMMetadataCreateKeyFromIdentifierAsCFData(CFAllocator!, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeyFromIdentifierAsCFData(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeyFromIdentifierAsCFData(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |

Modified CMMetadataCreateKeySpaceFromIdentifier(CFAllocator!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeySpaceFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keySpaceOut: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeySpaceFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keySpaceOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(CFAllocator!, CMMetadataFormatDescription!, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataFormatDescription: CMMetadataFormatDescription!, _ metadataDescriptionFlavor: CFString!, _ metadataDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataFormatDescription: CMMetadataFormatDescription!, _ metadataDescriptionFlavor: CFString!, _ metadataDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(CFAllocator!, CMMetadataFormatDescription!, CMMetadataFormatDescription!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(_ allocator: CFAllocator!, _ srcDesc1: CMMetadataFormatDescription!, _ srcDesc2: CMMetadataFormatDescription!, _ outDesc: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(_ allocator: CFAllocator!, _ srcDesc1: CMMetadataFormatDescription!, _ srcDesc2: CMMetadataFormatDescription!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFString!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataDescriptionBlockBuffer: CMBlockBuffer!, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataDescriptionBlockBuffer: CMBlockBuffer!, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator!, _ metadataDescriptionData: ConstUnsafePointer<UInt8>, _ metadataDescriptionSize: UInt, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator!, _ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: Int, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateWithKeys(CFAllocator!, CMMetadataFormatType, CFArray!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithKeys(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ keys: CFArray!, _ outDesc: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMMetadataFormatDescriptionCreateWithKeys(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ keys: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(CFAllocator!, CMMetadataFormatDescription!, CFArray!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(_ allocator: CFAllocator!, _ srcDesc: CMMetadataFormatDescription!, _ metadataSpecifications: CFArray!, _ outDesc: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(_ allocator: CFAllocator!, _ srcDesc: CMMetadataFormatDescription!, _ metadataSpecifications: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionCreateWithMetadataSpecifications(CFAllocator!, CMMetadataFormatType, CFArray!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ metadataSpecifications: CFArray!, _ outDesc: UnsafePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ metadataSpecifications: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |

Modified CMMetadataFormatDescriptionGetKeyWithLocalID(CMMetadataFormatDescription!, OSType) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMMuxedFormatDescriptionCreate(CFAllocator!, CMMuxedStreamType, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMMuxedFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMMuxedFormatDescriptionCreate(_ allocator: CFAllocator!, _ muxType: CMMuxedStreamType, _ extensions: CFDictionary!, _ outDesc: UnsafePointer<Unmanaged<CMMuxedFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMMuxedFormatDescriptionCreate(_ allocator: CFAllocator!, _ muxType: CMMuxedStreamType, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMuxedFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMPropagateAttachments(CMAttachmentBearer!, CMAttachmentBearer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMPropagateAttachments(_ source: CMAttachmentBearerRef!, _ destination: CMAttachmentBearerRef!) ``` | OS X 10.10 |
| To | ``` func CMPropagateAttachments(_ source: CMAttachmentBearer!, _ destination: CMAttachmentBearer!) ``` | OS X 10.7 |

Modified CMRemoveAllAttachments(CMAttachmentBearer!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMRemoveAllAttachments(_ target: CMAttachmentBearerRef!) ``` | OS X 10.10 |
| To | ``` func CMRemoveAllAttachments(_ target: CMAttachmentBearer!) ``` | OS X 10.7 |

Modified CMRemoveAttachment(CMAttachmentBearer!, CFString!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMRemoveAttachment(_ target: CMAttachmentBearerRef!, _ key: CFString!) ``` | OS X 10.10 |
| To | ``` func CMRemoveAttachment(_ target: CMAttachmentBearer!, _ key: CFString!) ``` | OS X 10.7 |

Modified CMSampleBufferCallForEachSample(CMSampleBuffer!, CFunctionPointer<((CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer!, _ callback: CFunctionPointer<((CMSampleBuffer!, CMItemCount, UnsafePointer<()>) -> OSStatus)>, _ refcon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer!, _ callback: CFunctionPointer<((CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer!, Int32, Int32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCopyPCMDataIntoAudioBufferList(_ sbuf: CMSampleBuffer!, _ frameOffset: Int32, _ numFrames: Int32, _ bufferList: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCopyPCMDataIntoAudioBufferList(_ sbuf: CMSampleBuffer!, _ frameOffset: Int32, _ numFrames: Int32, _ bufferList: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.9 |

Modified CMSampleBufferCopySampleBufferForRange(CFAllocator!, CMSampleBuffer!, CFRange, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCopySampleBufferForRange(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sampleRange: CFRange, _ sBufOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCopySampleBufferForRange(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sampleRange: CFRange, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferCreate(CFAllocator!, CMBlockBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMFormatDescription!, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>, CMItemCount, UnsafePointer<Int>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCreate(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafePointer<()>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: ConstUnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: ConstUnsafePointer<UInt>, _ sBufOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCreate(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferCreateCopy(CFAllocator!, CMSampleBuffer!, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCreateCopy(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sbufCopyOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCreateCopy(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sbufCopyOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferCreateCopyWithNewTiming(CFAllocator!, CMSampleBuffer!, CMItemCount, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator!, _ originalSBuf: CMSampleBuffer!, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: ConstUnsafePointer<CMSampleTimingInfo>, _ sBufCopyOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator!, _ originalSBuf: CMSampleBuffer!, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ sBufCopyOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferCreateForImageBuffer(CFAllocator!, CVImageBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMVideoFormatDescription!, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafePointer<()>, _ formatDescription: CMVideoFormatDescription!, _ sampleTiming: ConstUnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMVideoFormatDescription!, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferDataIsReady(CMSampleBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer!, UnsafeMutablePointer<Int>, UnsafeMutablePointer<AudioBufferList>, Int, CFAllocator!, CFAllocator!, UInt32, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer!, _ bufferListSizeNeededOut: UnsafePointer<UInt>, _ bufferListOut: UnsafePointer<AudioBufferList>, _ bufferListSize: UInt, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ blockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer!, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer!, Int, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer!, _ packetDescriptionsSize: UInt, _ packetDescriptionsOut: UnsafePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer!, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer!, UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer!, _ packetDescriptionsPtrOut: UnsafePointer<ConstUnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafePointer<UInt>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer!, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetDataBuffer(CMSampleBuffer!) -> CMBlockBuffer!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetDataBuffer(_ sbuf: CMSampleBuffer!) -> Unmanaged<CMBlockBuffer>! ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetDataBuffer(_ sbuf: CMSampleBuffer!) -> CMBlockBuffer! ``` | OS X 10.7 |

Modified CMSampleBufferGetDecodeTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetDuration(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetFormatDescription(CMSampleBuffer!) -> CMFormatDescription!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetFormatDescription(_ sbuf: CMSampleBuffer!) -> Unmanaged<CMFormatDescription>! ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetFormatDescription(_ sbuf: CMSampleBuffer!) -> CMFormatDescription! ``` | OS X 10.7 |

Modified CMSampleBufferGetImageBuffer(CMSampleBuffer!) -> CVImageBuffer!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetImageBuffer(_ sbuf: CMSampleBuffer!) -> Unmanaged<CVImageBuffer>! ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetImageBuffer(_ sbuf: CMSampleBuffer!) -> CVImageBuffer! ``` | OS X 10.7 |

Modified CMSampleBufferGetNumSamples(CMSampleBuffer!) -> CMItemCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetOutputDuration(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafePointer<CMItemCount>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetPresentationTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferGetSampleAttachmentsArray(CMSampleBuffer!, Boolean) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetSampleAttachmentsArray(_ sbuf: CMSampleBuffer!, _ createIfNecessary: Boolean) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetSampleAttachmentsArray(_ sbuf: CMSampleBuffer!, _ createIfNecessary: Boolean) -> CFArray! ``` | OS X 10.7 |

Modified CMSampleBufferGetSampleSize(CMSampleBuffer!, CMItemIndex) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex) -> UInt ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex) -> Int ``` | OS X 10.7 |

Modified CMSampleBufferGetSampleSizeArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Int>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer!, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafePointer<UInt>, _ sizeArrayEntriesNeededOut: UnsafePointer<CMItemCount>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer!, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetSampleTimingInfo(CMSampleBuffer!, CMItemIndex, UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetSampleTimingInfo(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex, _ timingInfoOut: UnsafePointer<CMSampleTimingInfo>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetSampleTimingInfo(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex, _ timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafePointer<CMItemCount>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferGetTotalSampleSize(CMSampleBuffer!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer!) -> UInt ``` | OS X 10.10 |
| To | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer!) -> Int ``` | OS X 10.7 |

Modified CMSampleBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferHasDataFailed(CMSampleBuffer!, UnsafeMutablePointer<OSStatus>) -> Boolean

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferHasDataFailed(_ sbuf: CMSampleBuffer!, _ statusOut: UnsafePointer<OSStatus>) -> Boolean ``` |
| To | ``` func CMSampleBufferHasDataFailed(_ sbuf: CMSampleBuffer!, _ statusOut: UnsafeMutablePointer<OSStatus>) -> Boolean ``` |

Modified CMSampleBufferInvalidate(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferIsValid(CMSampleBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferMakeDataReady(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferMakeDataReadyCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferMakeDataReadyCallback = CFunctionPointer<((CMSampleBuffer!, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias CMSampleBufferMakeDataReadyCallback = CFunctionPointer<((CMSampleBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified CMSampleBufferSetDataBuffer(CMSampleBuffer!, CMBlockBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer!, CFAllocator!, CFAllocator!, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSampleBufferSetDataBufferFromAudioBufferList(_ sbuf: CMSampleBuffer!, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ bufferList: ConstUnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSampleBufferSetDataBufferFromAudioBufferList(_ sbuf: CMSampleBuffer!, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ bufferList: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.7 |

Modified CMSampleBufferSetDataReady(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferSetInvalidateCallback(CMSampleBuffer!, CMSampleBufferInvalidateCallback, UInt64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer!, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSampleBufferTrackDataReadiness(CMSampleBuffer!, CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSetAttachment(CMAttachmentBearer!, CFString!, AnyObject!, CMAttachmentMode)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSetAttachment(_ target: CMAttachmentBearerRef!, _ key: CFString!, _ value: AnyObject!, _ attachmentMode: CMAttachmentMode) ``` | OS X 10.10 |
| To | ``` func CMSetAttachment(_ target: CMAttachmentBearer!, _ key: CFString!, _ value: AnyObject!, _ attachmentMode: CMAttachmentMode) ``` | OS X 10.7 |

Modified CMSetAttachments(CMAttachmentBearer!, CFDictionary!, CMAttachmentMode)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSetAttachments(_ target: CMAttachmentBearerRef!, _ theAttachments: CFDictionary!, _ attachmentMode: CMAttachmentMode) ``` | OS X 10.10 |
| To | ``` func CMSetAttachments(_ target: CMAttachmentBearer!, _ theAttachments: CFDictionary!, _ attachmentMode: CMAttachmentMode) ``` | OS X 10.7 |

Modified CMSimpleQueueCreate(CFAllocator!, Int32, UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSimpleQueueCreate(_ allocator: CFAllocator!, _ capacity: Int32, _ queueOut: UnsafePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSimpleQueueCreate(_ allocator: CFAllocator!, _ capacity: Int32, _ queueOut: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMSimpleQueueDequeue(CMSimpleQueue!) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue!) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue!) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified CMSimpleQueueEnqueue(CMSimpleQueue!, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue!, _ element: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue!, _ element: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.7 |

Modified CMSimpleQueueGetCapacity(CMSimpleQueue!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSimpleQueueGetCount(CMSimpleQueue!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSimpleQueueGetHead(CMSimpleQueue!) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue!) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue!) -> UnsafePointer<Void> ``` | OS X 10.7 |

Modified CMSimpleQueueGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSimpleQueueReset(CMSimpleQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMSwapBigEndianClosedCaptionDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianClosedCaptionDescriptionToHost(_ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianClosedCaptionDescriptionToHost(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianImageDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianImageDescriptionToHost(_ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianImageDescriptionToHost(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianMetadataDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianMetadataDescriptionToHost(_ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianMetadataDescriptionToHost(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianSoundDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianSoundDescriptionToHost(_ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianSoundDescriptionToHost(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianTextDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianTextDescriptionToHost(_ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianTextDescriptionToHost(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapBigEndianTimeCodeDescriptionToHost(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapBigEndianTimeCodeDescriptionToHost(_ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapBigEndianTimeCodeDescriptionToHost(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianClosedCaptionDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianClosedCaptionDescriptionToBig(_ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianClosedCaptionDescriptionToBig(_ closedCaptionDescriptionData: UnsafeMutablePointer<UInt8>, _ closedCaptionDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianImageDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianImageDescriptionToBig(_ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianImageDescriptionToBig(_ imageDescriptionData: UnsafeMutablePointer<UInt8>, _ imageDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianMetadataDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianMetadataDescriptionToBig(_ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianMetadataDescriptionToBig(_ metadataDescriptionData: UnsafeMutablePointer<UInt8>, _ metadataDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianSoundDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianSoundDescriptionToBig(_ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianSoundDescriptionToBig(_ soundDescriptionData: UnsafeMutablePointer<UInt8>, _ soundDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianTextDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianTextDescriptionToBig(_ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianTextDescriptionToBig(_ textDescriptionData: UnsafeMutablePointer<UInt8>, _ textDescriptionSize: Int) -> OSStatus ``` |

Modified CMSwapHostEndianTimeCodeDescriptionToBig(UnsafeMutablePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMSwapHostEndianTimeCodeDescriptionToBig(_ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: UInt) -> OSStatus ``` |
| To | ``` func CMSwapHostEndianTimeCodeDescriptionToBig(_ timeCodeDescriptionData: UnsafeMutablePointer<UInt8>, _ timeCodeDescriptionSize: Int) -> OSStatus ``` |

Modified CMSyncConvertTime(CMTime, CMClockOrTimebase!, CMClockOrTimebase!) -> CMTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSyncConvertTime(_ time: CMTime, _ fromClockOrTimebase: CMClockOrTimebaseRef!, _ toClockOrTimebase: CMClockOrTimebaseRef!) -> CMTime ``` | OS X 10.10 |
| To | ``` func CMSyncConvertTime(_ time: CMTime, _ fromClockOrTimebase: CMClockOrTimebase!, _ toClockOrTimebase: CMClockOrTimebase!) -> CMTime ``` | OS X 10.8 |

Modified CMSyncGetRelativeRate(CMClockOrTimebase!, CMClockOrTimebase!) -> Float64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSyncGetRelativeRate(_ ofClockOrTimebase: CMClockOrTimebaseRef!, _ relativeToClockOrTimebase: CMClockOrTimebaseRef!) -> Float64 ``` | OS X 10.10 |
| To | ``` func CMSyncGetRelativeRate(_ ofClockOrTimebase: CMClockOrTimebase!, _ relativeToClockOrTimebase: CMClockOrTimebase!) -> Float64 ``` | OS X 10.8 |

Modified CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebase!, CMClockOrTimebase!, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<CMTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSyncGetRelativeRateAndAnchorTime(_ ofClockOrTimebase: CMClockOrTimebaseRef!, _ relativeToClockOrTimebase: CMClockOrTimebaseRef!, _ outRelativeRate: UnsafePointer<Float64>, _ outOfClockOrTimebaseAnchorTime: UnsafePointer<CMTime>, _ outRelativeToClockOrTimebaseAnchorTime: UnsafePointer<CMTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMSyncGetRelativeRateAndAnchorTime(_ ofClockOrTimebase: CMClockOrTimebase!, _ relativeToClockOrTimebase: CMClockOrTimebase!, _ outRelativeRate: UnsafeMutablePointer<Float64>, _ outOfClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>, _ outRelativeToClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` | OS X 10.8 |

Modified CMSyncGetTime(CMClockOrTimebase!) -> CMTime

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSyncGetTime(_ clockOrTimebase: CMClockOrTimebaseRef!) -> CMTime ``` | OS X 10.10 |
| To | ``` func CMSyncGetTime(_ clockOrTimebase: CMClockOrTimebase!) -> CMTime ``` | OS X 10.8 |

Modified CMSyncMightDrift(CMClockOrTimebase!, CMClockOrTimebase!) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMSyncMightDrift(_ clockOrTimebase1: CMClockOrTimebaseRef!, _ clockOrTimebase2: CMClockOrTimebaseRef!) -> Boolean ``` | OS X 10.10 |
| To | ``` func CMSyncMightDrift(_ clockOrTimebase1: CMClockOrTimebase!, _ clockOrTimebase2: CMClockOrTimebase!) -> Boolean ``` | OS X 10.8 |

Modified CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(CFAllocator!, CMTextFormatDescription!, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textFormatDescription: CMTextFormatDescription!, _ textDescriptionFlavor: CFString!, _ textDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textFormatDescription: CMTextFormatDescription!, _ textDescriptionFlavor: CFString!, _ textDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFString!, CMMediaType, UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textDescriptionBlockBuffer: CMBlockBuffer!, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textDescriptionBlockBuffer: CMBlockBuffer!, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |

Modified CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, CMMediaType, UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator!, _ textDescriptionData: ConstUnsafePointer<UInt8>, _ textDescriptionSize: UInt, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator!, _ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: Int, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |

Modified CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription!, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription!, _ outLocalFontID: UnsafePointer<UInt16>, _ outBold: UnsafePointer<Boolean>, _ outItalic: UnsafePointer<Boolean>, _ outUnderline: UnsafePointer<Boolean>, _ outFontSize: UnsafePointer<CGFloat>, _ outColorComponents: UnsafePointer<CGFloat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription!, _ outLocalFontID: UnsafeMutablePointer<UInt16>, _ outBold: UnsafeMutablePointer<Boolean>, _ outItalic: UnsafeMutablePointer<Boolean>, _ outUnderline: UnsafeMutablePointer<Boolean>, _ outFontSize: UnsafeMutablePointer<CGFloat>, _ outColorComponents: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` | OS X 10.7 |

Modified CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription!, Boolean, CGFloat, UnsafeMutablePointer<CGRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTextFormatDescriptionGetDefaultTextBox(_ desc: CMFormatDescription!, _ originIsAtTopLeft: Boolean, _ heightOfTextTrack: CGFloat, _ outDefaultTextBox: UnsafePointer<CGRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTextFormatDescriptionGetDefaultTextBox(_ desc: CMFormatDescription!, _ originIsAtTopLeft: Boolean, _ heightOfTextTrack: CGFloat, _ outDefaultTextBox: UnsafeMutablePointer<CGRect>) -> OSStatus ``` | OS X 10.7 |

Modified CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription!, UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTextFormatDescriptionGetDisplayFlags(_ desc: CMFormatDescription!, _ outDisplayFlags: UnsafePointer<CMTextDisplayFlags>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTextFormatDescriptionGetDisplayFlags(_ desc: CMFormatDescription!, _ outDisplayFlags: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus ``` | OS X 10.7 |

Modified CMTextFormatDescriptionGetFontName(CMFormatDescription!, UInt16, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTextFormatDescriptionGetFontName(_ desc: CMFormatDescription!, _ localFontID: UInt16, _ outFontName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTextFormatDescriptionGetFontName(_ desc: CMFormatDescription!, _ localFontID: UInt16, _ outFontName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMTextFormatDescriptionGetJustification(CMFormatDescription!, UnsafeMutablePointer<CMTextJustificationValue>, UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription!, _ outHorizontalJust: UnsafePointer<CMTextJustificationValue>, _ outVerticalJust: UnsafePointer<CMTextJustificationValue>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription!, _ outHorizontalJust: UnsafeMutablePointer<CMTextJustificationValue>, _ outVerticalJust: UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus ``` | OS X 10.7 |

Modified CMTimeAbsoluteValue(CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeAdd(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeClampToRange(CMTime, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(CFAllocator!, CMTimeCodeFormatDescription!, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeFormatDescription: CMTimeCodeFormatDescription!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeFormatDescription: CMTimeCodeFormatDescription!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMTimeCodeFormatDescriptionCreate(CFAllocator!, CMTimeCodeFormatType, CMTime, UInt32, UInt32, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreate(_ allocator: CFAllocator!, _ timeCodeFormatType: CMTimeCodeFormatType, _ frameDuration: CMTime, _ frameQuanta: UInt32, _ tcFlags: UInt32, _ extensions: CFDictionary!, _ descOut: UnsafePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTimeCodeFormatDescriptionCreate(_ allocator: CFAllocator!, _ timeCodeFormatType: CMTimeCodeFormatType, _ frameDuration: CMTime, _ frameQuanta: UInt32, _ tcFlags: UInt32, _ extensions: CFDictionary!, _ descOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFString!, UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeDescriptionBlockBuffer: CMBlockBuffer!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeDescriptionBlockBuffer: CMBlockBuffer!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |

Modified CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFString!, UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator!, _ timeCodeDescriptionData: ConstUnsafePointer<UInt8>, _ timeCodeDescriptionSize: UInt, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator!, _ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: Int, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |

Modified CMTimeCodeFormatDescriptionGetFrameDuration(CMTimeCodeFormatDescription!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCodeFormatDescriptionGetFrameQuanta(CMTimeCodeFormatDescription!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCodeFormatDescriptionGetTimeCodeFlags(CMTimeCodeFormatDescription!) -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCompare(CMTime, CMTime) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeConvertScale(CMTime, Int32, CMTimeRoundingMethod) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCopyAsDictionary(CMTime, CFAllocator!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeCopyDescription(CFAllocator!, CMTime) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeGetSeconds(CMTime) -> Float64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMake(Int64, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMakeFromDictionary(CFDictionary!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMakeWithEpoch(Int64, Int32, Int64) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMakeWithSeconds(Float64, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMapDurationFromRangeToRange(CMTime, CMTimeRange, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMapTimeFromRangeToRange(CMTime, CMTimeRange, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMaximum(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMinimum(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMultiply(CMTime, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeMultiplyByFloat64(CMTime, Float64) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeContainsTime(CMTimeRange, CMTime) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeContainsTimeRange(CMTimeRange, CMTimeRange) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeCopyAsDictionary(CMTimeRange, CFAllocator!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeCopyDescription(CFAllocator!, CMTimeRange) -> CFString!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeFromTimeToTime(CMTime, CMTime) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeGetEnd(CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeGetIntersection(CMTimeRange, CMTimeRange) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeGetUnion(CMTimeRange, CMTimeRange) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeMake(CMTime, CMTime) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeMakeFromDictionary(CFDictionary!) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeRangeShow(CMTimeRange)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeShow(CMTime)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimeSubtract(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMTimebaseAddTimer(CMTimebase!, CFRunLoopTimer!, CFRunLoop!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseAddTimerDispatchSource(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseCreateWithMasterClock(CFAllocator!, CMClock!, UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseCreateWithMasterClock(_ allocator: CFAllocator!, _ masterClock: CMClock!, _ timebaseOut: UnsafePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTimebaseCreateWithMasterClock(_ allocator: CFAllocator!, _ masterClock: CMClock!, _ timebaseOut: UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` | OS X 10.8 |

Modified CMTimebaseCreateWithMasterTimebase(CFAllocator!, CMTimebase!, UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseCreateWithMasterTimebase(_ allocator: CFAllocator!, _ masterTimebase: CMTimebase!, _ timebaseOut: UnsafePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTimebaseCreateWithMasterTimebase(_ allocator: CFAllocator!, _ masterTimebase: CMTimebase!, _ timebaseOut: UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` | OS X 10.8 |

Modified CMTimebaseGetEffectiveRate(CMTimebase!) -> Float64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseGetMaster(CMTimebase!) -> CMClockOrTimebase!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMaster(_ timebase: CMTimebase!) -> Unmanaged<CMClockOrTimebaseRef>! ``` | OS X 10.10 |
| To | ``` func CMTimebaseGetMaster(_ timebase: CMTimebase!) -> CMClockOrTimebase! ``` | OS X 10.8 |

Modified CMTimebaseGetMasterClock(CMTimebase!) -> CMClock!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMasterClock(_ timebase: CMTimebase!) -> Unmanaged<CMClock>! ``` | OS X 10.10 |
| To | ``` func CMTimebaseGetMasterClock(_ timebase: CMTimebase!) -> CMClock! ``` | OS X 10.8 |

Modified CMTimebaseGetMasterTimebase(CMTimebase!) -> CMTimebase!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMasterTimebase(_ timebase: CMTimebase!) -> Unmanaged<CMTimebase>! ``` | OS X 10.10 |
| To | ``` func CMTimebaseGetMasterTimebase(_ timebase: CMTimebase!) -> CMTimebase! ``` | OS X 10.8 |

Modified CMTimebaseGetRate(CMTimebase!) -> Float64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseGetTime(CMTimebase!) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseGetTimeAndRate(CMTimebase!, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseGetTimeAndRate(_ timebase: CMTimebase!, _ outTime: UnsafePointer<CMTime>, _ outRate: UnsafePointer<Float64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMTimebaseGetTimeAndRate(_ timebase: CMTimebase!, _ outTime: UnsafeMutablePointer<CMTime>, _ outRate: UnsafeMutablePointer<Float64>) -> OSStatus ``` | OS X 10.8 |

Modified CMTimebaseGetTimeWithTimeScale(CMTimebase!, CMTimeScale, CMTimeRoundingMethod) -> CMTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseGetUltimateMasterClock(CMTimebase!) -> CMClock!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMTimebaseGetUltimateMasterClock(_ timebase: CMTimebase!) -> Unmanaged<CMClock>! ``` | OS X 10.10 |
| To | ``` func CMTimebaseGetUltimateMasterClock(_ timebase: CMTimebase!) -> CMClock! ``` | OS X 10.8 |

Modified CMTimebaseNotificationBarrier(CMTimebase!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseRemoveTimer(CMTimebase!, CFRunLoopTimer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseRemoveTimerDispatchSource(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetAnchorTime(CMTimebase!, CMTime, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetRate(CMTimebase!, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetRateAndAnchorTime(CMTimebase!, Float64, CMTime, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetTime(CMTimebase!, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase!, dispatch_source_t!, CMTime, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetTimerNextFireTime(CMTimebase!, CFRunLoopTimer!, CMTime, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMTimebaseSetTimerToFireImmediately(CMTimebase!, CFRunLoopTimer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(CFAllocator!, CMVideoFormatDescription!, CFStringEncoding, CFString!, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ imageDescriptionBlockBufferOut: UnsafePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ imageDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionCreate(CFAllocator!, CMVideoCodecType, Int32, Int32, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMVideoFormatDescriptionCreate(_ allocator: CFAllocator!, _ codecType: CMVideoCodecType, _ width: Int32, _ height: Int32, _ extensions: CFDictionary!, _ outDesc: UnsafePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMVideoFormatDescriptionCreate(_ allocator: CFAllocator!, _ codecType: CMVideoCodecType, _ width: Int32, _ height: Int32, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMVideoFormatDescriptionCreateForImageBuffer(CFAllocator!, CVImageBuffer!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ outDesc: UnsafePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMVideoFormatDescriptionCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` | OS X 10.7 |

Modified CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(CFAllocator!, CMBlockBuffer!, CFStringEncoding, CFString!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ imageDescriptionBlockBuffer: CMBlockBuffer!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ imageDescriptionBlockBuffer: CMBlockBuffer!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(CFAllocator!, UnsafePointer<UInt8>, Int, CFStringEncoding, CFString!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator!, _ imageDescriptionData: ConstUnsafePointer<UInt8>, _ imageDescriptionSize: UInt, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator!, _ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: Int, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |

Modified CMVideoFormatDescriptionCreateFromH264ParameterSets(CFAllocator!, Int, UnsafePointer<UnsafePointer<UInt8>>, UnsafePointer<Int>, Int32, UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator!, _ parameterSetCount: UInt, _ parameterSetPointers: ConstUnsafePointer<ConstUnsafePointer<UInt8>>, _ parameterSetSizes: ConstUnsafePointer<UInt>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator!, _ parameterSetCount: Int, _ parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, _ parameterSetSizes: UnsafePointer<Int>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` | OS X 10.9 |

Modified CMVideoFormatDescriptionGetCleanAperture(CMVideoFormatDescription!, Boolean) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMVideoFormatDescriptionGetDimensions(CMVideoFormatDescription!) -> CMVideoDimensions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMVideoFormatDescriptionGetH264ParameterSetAtIndex(CMFormatDescription!, Int, UnsafeMutablePointer<UnsafePointer<UInt8>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription!, _ parameterSetIndex: UInt, _ parameterSetPointerOut: UnsafePointer<ConstUnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafePointer<UInt>, _ parameterSetCountOut: UnsafePointer<UInt>, _ NALUnitHeaderLengthOut: UnsafePointer<Int32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription!, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<Int>, _ parameterSetCountOut: UnsafeMutablePointer<Int>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` | OS X 10.9 |

Modified CMVideoFormatDescriptionGetPresentationDimensions(CMVideoFormatDescription!, Boolean, Boolean) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified CMVideoFormatDescriptionMatchesImageBuffer(CMVideoFormatDescription!, CVImageBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionColorPrimaries_P22

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCMFormatDescriptionConformsToMPEG2VideoProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtensionKey_MetadataKeyTable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_BytesPerRow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_Depth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_FormatName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_FullRangeVideo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_ICCProfile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_OriginalCompressionSettings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_RevisionLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_SpatialQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_TemporalQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_Vendor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_VerbatimISOSampleEntry

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_VerbatimSampleDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionExtension_Version

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionKey_CleanApertureHeightRational

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionKey_CleanApertureWidthRational

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMFormatDescriptionVendor_Apple

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMMemoryPoolOption_AgeOutPeriod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCMMetadataFormatDescriptionKey_LocalID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMMetadataFormatDescriptionKey_Namespace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMMetadataFormatDescriptionKey_Value

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_DependsOnOthers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_DisplayImmediately

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_DoNotDisplay

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_EarlierDisplayTimesAllowed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_HasRedundantCoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_IsDependedOnByOthers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_NotSync

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleAttachmentKey_PartialSync

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_DrainAfterDecoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_EmptyMedia

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_GradualDecoderRefresh

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_PermanentEmptyMedia

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_ResumeOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_Reverse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_SampleReferenceByteOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_SampleReferenceURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_SpeedMultiplier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_TransitionID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_TrimDurationAtEnd

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferAttachmentKey_TrimDurationAtStart

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotificationParameter_ResumeTag

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotification_InhibitOutputUntil

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotification_ResetOutput

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferConsumerNotification_BufferConsumed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMSampleBufferNotification_DataBecameReady

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionColor_Alpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionColor_Blue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionColor_Green

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionColor_Red

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_BackgroundColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_DefaultFontName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_DefaultStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_DefaultTextBox

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_DisplayFlags

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_FontTable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_HorizontalJustification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_TextJustification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionExtension_VerticalJustification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionRect_Bottom

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionRect_Left

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionRect_Right

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionRect_Top

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_Ascent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_EndChar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_Font

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_FontFace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_FontSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_ForegroundColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_Height

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextFormatDescriptionStyle_StartChar

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTextMarkupAlignmentType_End

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAlignmentType_Left

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAlignmentType_Middle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAlignmentType_Right

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAlignmentType_Start

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_Alignment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_BackgroundColorARGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_BoldStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_CharacterBackgroundColorARGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_CharacterEdgeStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_FontFamilyName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_ForegroundColorARGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_GenericFontFamilyName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_ItalicStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_RelativeFontSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_UnderlineStyle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_VerticalLayout

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupAttribute_WritingDirectionSizePercentage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupCharacterEdgeStyle_Depressed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupCharacterEdgeStyle_DropShadow

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupCharacterEdgeStyle_None

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupCharacterEdgeStyle_Raised

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupCharacterEdgeStyle_Uniform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Casual

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Cursive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Default

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Fantasy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Monospace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_MonospaceSansSerif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_MonospaceSerif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_ProportionalSansSerif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_ProportionalSerif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_SansSerif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_Serif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextMarkupGenericFontName_SmallCapital

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextVerticalLayout_LeftToRight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTextVerticalLayout_RightToLeft

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTimeCodeFormatDescriptionExtension_SourceReferenceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeCodeFormatDescriptionKey_LangCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeCodeFormatDescriptionKey_Value

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeEpochKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeFlagsKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeIndefinite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeNegativeInfinity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimePositiveInfinity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeRangeDurationKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeRangeInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeRangeStartKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeRangeZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeScaleKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeValueKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimeZero

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCMTimebaseNotificationKey_EventTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCMTimebaseNotification_EffectiveRateChanged

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCMTimebaseNotification_TimeJumped

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCMTimingInfoInvalid

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

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
