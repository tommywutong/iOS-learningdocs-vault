---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CoreMedia.html
archived_at: '2026-07-18T02:56:09.881833Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CoreMedia Changes

## CoreMedia

Removed CMTimeFlags.valueAdded CMTimeFlags.init(rawValue: UInt32)Modified CMTimeFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMTimeFlags : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` |
| To | ``` struct CMTimeFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` |

Modified CMTimeFlags.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CMAudioClockCreate(CFAllocator!, UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMAudioFormatDescriptionCreate(CFAllocator!, UnsafePointer<AudioStreamBasicDescription>, UInt, UnsafePointer<AudioChannelLayout>, UInt, UnsafePointer<Void>, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionCreateSummary(CFAllocator!, CFArray!, UInt32, UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionEqual(CMAudioFormatDescription!, CMAudioFormatDescription!, CMAudioFormatDescriptionMask, UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetChannelLayout(CMAudioFormatDescription!, UnsafeMutablePointer<UInt>) -> UnsafePointer<AudioChannelLayout>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetFormatList(CMAudioFormatDescription!, UnsafeMutablePointer<UInt>) -> UnsafePointer<AudioFormatListItem>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetMagicCookie(CMAudioFormatDescription!, UnsafeMutablePointer<UInt>) -> UnsafePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetMostCompatibleFormat(CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetRichestDecodableFormat(CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioFormatDescriptionGetStreamBasicDescription(CMAudioFormatDescription!) -> UnsafePointer<AudioStreamBasicDescription>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMAudioSampleBufferCreateWithPacketDescriptions(CFAllocator!, CMBlockBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMFormatDescription!, CMItemCount, CMTime, UnsafePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferAccessDataBytes(CMBlockBuffer!, UInt, UInt, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferAppendBufferReference(CMBlockBuffer!, CMBlockBuffer!, UInt, UInt, CMBlockBufferFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferAppendMemoryBlock(CMBlockBuffer!, UnsafeMutablePointer<Void>, UInt, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, UInt, UInt, CMBlockBufferFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferAssureBlockMemory(CMBlockBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferCopyDataBytes(CMBlockBuffer!, UInt, UInt, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferCreateContiguous(CFAllocator!, CMBlockBuffer!, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, UInt, UInt, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferCreateEmpty(CFAllocator!, UInt32, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferCreateWithBufferReference(CFAllocator!, CMBlockBuffer!, UInt, UInt, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferCreateWithMemoryBlock(CFAllocator!, UnsafeMutablePointer<Void>, UInt, CFAllocator!, UnsafePointer<CMBlockBufferCustomBlockSource>, UInt, UInt, CMBlockBufferFlags, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferFillDataBytes(Int8, CMBlockBuffer!, UInt, UInt) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferGetDataLength(CMBlockBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferGetDataPointer(CMBlockBuffer!, UInt, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferIsEmpty(CMBlockBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferIsRangeContiguous(CMBlockBuffer!, UInt, UInt) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBlockBufferReplaceDataBytes(UnsafePointer<Void>, CMBlockBuffer!, UInt, UInt) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueCallForEachBuffer(CMBufferQueue!, CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueContainsEndOfData(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueCreate(CFAllocator!, CMItemCount, UnsafePointer<CMBufferCallbacks>, UnsafeMutablePointer<Unmanaged<CMBufferQueue>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueEnqueue(CMBufferQueue!, CMBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetBufferCount(CMBufferQueue!) -> CMItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetDuration(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetHead(CMBufferQueue!) -> Unmanaged<CMBuffer>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetMaxPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueGetTotalSize(CMBufferQueue!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified CMBufferQueueGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueInstallTrigger(CMBufferQueue!, CMBufferQueueTriggerCallback, UnsafeMutablePointer<Void>, CMBufferQueueTriggerCondition, CMTime, UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueInstallTriggerWithIntegerThreshold(CMBufferQueue!, CMBufferQueueTriggerCallback, UnsafeMutablePointer<Void>, CMBufferQueueTriggerCondition, CMItemCount, UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueIsAtEndOfData(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueIsEmpty(CMBufferQueue!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueMarkEndOfData(CMBufferQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueRemoveTrigger(CMBufferQueue!, CMBufferQueueTriggerToken) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueReset(CMBufferQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueResetWithCallback(CMBufferQueue!, CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueSetValidationCallback(CMBufferQueue!, CMBufferValidationCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMBufferQueueTestTrigger(CMBufferQueue!, CMBufferQueueTriggerToken) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMClockConvertHostTimeToSystemUnits(CMTime) -> UInt64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockGetAnchorTime(CMClock!, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<CMTime>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockGetHostTimeClock() -> CMClock!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockGetTime(CMClock!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockInvalidate(CMClock!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockMakeHostTimeFromSystemUnits(UInt64) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMClockMightDrift(CMClock!, CMClock!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMCopyDictionaryOfAttachments(CFAllocator!, CMAttachmentBearer!, CMAttachmentMode) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionCreate(CFAllocator!, CMMediaType, FourCharCode, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionEqual(CMFormatDescription!, CMFormatDescription!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionEqualIgnoringExtensionKeys(CMFormatDescription!, CMFormatDescription!, AnyObject!, AnyObject!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified CMFormatDescriptionGetExtension(CMFormatDescription!, CFString!) -> Unmanaged<CFPropertyList>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionGetExtensions(CMFormatDescription!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionGetMediaSubType(CMFormatDescription!) -> FourCharCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionGetMediaType(CMFormatDescription!) -> CMMediaType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMFormatDescriptionGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMGetAttachment(CMAttachmentBearer!, CFString!, UnsafeMutablePointer<CMAttachmentMode>) -> Unmanaged<AnyObject>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMMemoryPoolCreate(CFDictionary!) -> Unmanaged<CMMemoryPool>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMMemoryPoolFlush(CMMemoryPool!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMMemoryPoolGetAllocator(CMMemoryPool!) -> Unmanaged<CFAllocator>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMMemoryPoolGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMMemoryPoolInvalidate(CMMemoryPool!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMMetadataFormatDescriptionCreateWithKeys(CFAllocator!, CMMetadataFormatType, CFArray!, UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMMetadataFormatDescriptionGetKeyWithLocalID(CMMetadataFormatDescription!, OSType) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMMuxedFormatDescriptionCreate(CFAllocator!, CMMuxedStreamType, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMMuxedFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMPropagateAttachments(CMAttachmentBearer!, CMAttachmentBearer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMRemoveAllAttachments(CMAttachmentBearer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMRemoveAttachment(CMAttachmentBearer!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCallForEachSample(CMSampleBuffer!, CFunctionPointer<((CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus)>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer!, Int32, Int32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CMSampleBufferCopySampleBufferForRange(CFAllocator!, CMSampleBuffer!, CFRange, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCreate(CFAllocator!, CMBlockBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMFormatDescription!, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>, CMItemCount, UnsafePointer<UInt>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCreateCopy(CFAllocator!, CMSampleBuffer!, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCreateCopyWithNewTiming(CFAllocator!, CMSampleBuffer!, CMItemCount, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferCreateForImageBuffer(CFAllocator!, CVImageBuffer!, Boolean, CMSampleBufferMakeDataReadyCallback, UnsafeMutablePointer<Void>, CMVideoFormatDescription!, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferDataIsReady(CMSampleBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer!, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<AudioBufferList>, UInt, CFAllocator!, CFAllocator!, UInt32, UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer!, UInt, UnsafeMutablePointer<AudioStreamPacketDescription>, UnsafeMutablePointer<UInt>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer!, UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<UInt>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetDataBuffer(CMSampleBuffer!) -> CMBlockBuffer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetDecodeTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetDuration(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetFormatDescription(CMSampleBuffer!) -> CMFormatDescription!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetImageBuffer(CMSampleBuffer!) -> CVImageBuffer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetNumSamples(CMSampleBuffer!) -> CMItemCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetOutputDuration(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetPresentationTimeStamp(CMSampleBuffer!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetSampleAttachmentsArray(CMSampleBuffer!, Boolean) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetSampleSize(CMSampleBuffer!, CMItemIndex) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetSampleSizeArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetSampleTimingInfo(CMSampleBuffer!, CMItemIndex, UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMItemCount>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetTotalSampleSize(CMSampleBuffer!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferInvalidate(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferIsValid(CMSampleBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferMakeDataReady(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferSetDataBuffer(CMSampleBuffer!, CMBlockBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer!, CFAllocator!, CFAllocator!, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferSetDataReady(CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferSetInvalidateCallback(CMSampleBuffer!, CMSampleBufferInvalidateCallback, UInt64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer!, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSampleBufferTrackDataReadiness(CMSampleBuffer!, CMSampleBuffer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSetAttachment(CMAttachmentBearer!, CFString!, AnyObject!, CMAttachmentMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSetAttachments(CMAttachmentBearer!, CFDictionary!, CMAttachmentMode)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMSimpleQueueCreate(CFAllocator!, Int32, UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueDequeue(CMSimpleQueue!) -> UnsafePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueEnqueue(CMSimpleQueue!, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueGetCapacity(CMSimpleQueue!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueGetCount(CMSimpleQueue!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueGetHead(CMSimpleQueue!) -> UnsafePointer<Void>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSimpleQueueReset(CMSimpleQueue!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified CMSyncConvertTime(CMTime, CMClockOrTimebase!, CMClockOrTimebase!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMSyncGetRelativeRate(CMClockOrTimebase!, CMClockOrTimebase!) -> Float64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMSyncGetRelativeRateAndAnchorTime(CMClockOrTimebase!, CMClockOrTimebase!, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<CMTime>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMSyncGetTime(CMClockOrTimebase!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMSyncMightDrift(CMClockOrTimebase!, CMClockOrTimebase!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTextFormatDescriptionGetDefaultStyle(CMFormatDescription!, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTextFormatDescriptionGetDefaultTextBox(CMFormatDescription!, Boolean, CGFloat, UnsafeMutablePointer<CGRect>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTextFormatDescriptionGetDisplayFlags(CMFormatDescription!, UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTextFormatDescriptionGetFontName(CMFormatDescription!, UInt16, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTextFormatDescriptionGetJustification(CMFormatDescription!, UnsafeMutablePointer<CMTextJustificationValue>, UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeAbsoluteValue(CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeAdd(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeClampToRange(CMTime, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCodeFormatDescriptionCreate(CFAllocator!, CMTimeCodeFormatType, CMTime, UInt32, UInt32, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCodeFormatDescriptionGetFrameDuration(CMTimeCodeFormatDescription!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCodeFormatDescriptionGetFrameQuanta(CMTimeCodeFormatDescription!) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCodeFormatDescriptionGetTimeCodeFlags(CMTimeCodeFormatDescription!) -> UInt32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCompare(CMTime, CMTime) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeConvertScale(CMTime, Int32, CMTimeRoundingMethod) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCopyAsDictionary(CMTime, CFAllocator!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeCopyDescription(CFAllocator!, CMTime) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeGetSeconds(CMTime) -> Float64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMake(Int64, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMakeFromDictionary(CFDictionary!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMakeWithEpoch(Int64, Int32, Int64) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMakeWithSeconds(Float64, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMapDurationFromRangeToRange(CMTime, CMTimeRange, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMapTimeFromRangeToRange(CMTime, CMTimeRange, CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMaximum(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMinimum(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMultiply(CMTime, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMultiplyByFloat64(CMTime, Float64) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeMultiplyByRatio(CMTime, Int32, Int32) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified CMTimeRangeContainsTime(CMTimeRange, CMTime) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeContainsTimeRange(CMTimeRange, CMTimeRange) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeCopyAsDictionary(CMTimeRange, CFAllocator!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeCopyDescription(CFAllocator!, CMTimeRange) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeFromTimeToTime(CMTime, CMTime) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeGetEnd(CMTimeRange) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeGetIntersection(CMTimeRange, CMTimeRange) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeGetUnion(CMTimeRange, CMTimeRange) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeMake(CMTime, CMTime) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeMakeFromDictionary(CFDictionary!) -> CMTimeRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeRangeShow(CMTimeRange)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeShow(CMTime)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimeSubtract(CMTime, CMTime) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMTimebaseAddTimer(CMTimebase!, CFRunLoopTimer!, CFRunLoop!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseAddTimerDispatchSource(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseCreateWithMasterClock(CFAllocator!, CMClock!, UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseCreateWithMasterTimebase(CFAllocator!, CMTimebase!, UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetEffectiveRate(CMTimebase!) -> Float64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetMaster(CMTimebase!) -> CMClockOrTimebase!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetMasterClock(CMTimebase!) -> CMClock!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetMasterTimebase(CMTimebase!) -> CMTimebase!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetRate(CMTimebase!) -> Float64

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetTime(CMTimebase!) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetTimeAndRate(CMTimebase!, UnsafeMutablePointer<CMTime>, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetTimeWithTimeScale(CMTimebase!, CMTimeScale, CMTimeRoundingMethod) -> CMTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseGetUltimateMasterClock(CMTimebase!) -> CMClock!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseNotificationBarrier(CMTimebase!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseRemoveTimer(CMTimebase!, CFRunLoopTimer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseRemoveTimerDispatchSource(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetAnchorTime(CMTimebase!, CMTime, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetRate(CMTimebase!, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetRateAndAnchorTime(CMTimebase!, Float64, CMTime, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetTime(CMTimebase!, CMTime) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetTimerDispatchSourceNextFireTime(CMTimebase!, dispatch_source_t!, CMTime, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetTimerDispatchSourceToFireImmediately(CMTimebase!, dispatch_source_t!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetTimerNextFireTime(CMTimebase!, CFRunLoopTimer!, CMTime, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMTimebaseSetTimerToFireImmediately(CMTimebase!, CFRunLoopTimer!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CMVideoFormatDescriptionCreate(CFAllocator!, CMVideoCodecType, Int32, Int32, CFDictionary!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionCreateForImageBuffer(CFAllocator!, CVImageBuffer!, UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionCreateFromH264ParameterSets(CFAllocator!, UInt, UnsafePointer<UnsafePointer<UInt8>>, UnsafePointer<UInt>, Int32, UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CMVideoFormatDescriptionGetCleanAperture(CMVideoFormatDescription!, Boolean) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionGetDimensions(CMVideoFormatDescription!) -> CMVideoDimensions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionGetH264ParameterSetAtIndex(CMFormatDescription!, UInt, UnsafeMutablePointer<UnsafePointer<UInt8>>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CMVideoFormatDescriptionGetPresentationDimensions(CMVideoFormatDescription!, Boolean, Boolean) -> CGSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CMVideoFormatDescriptionMatchesImageBuffer(CMVideoFormatDescription!, CVImageBuffer!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionColorPrimaries_P22

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMFormatDescriptionConformsToMPEG2VideoProfile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtensionKey_MetadataKeyTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_BytesPerRow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_Depth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_FormatName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_FullRangeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCMFormatDescriptionExtension_ICCProfile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_OriginalCompressionSettings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_RevisionLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_SpatialQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_TemporalQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_Vendor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_VerbatimISOSampleEntry

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_VerbatimSampleDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionExtension_Version

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionKey_CleanApertureHeightRational

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionKey_CleanApertureWidthRational

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMFormatDescriptionVendor_Apple

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMMemoryPoolOption_AgeOutPeriod

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMMetadataFormatDescriptionKey_LocalID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMMetadataFormatDescriptionKey_Namespace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMMetadataFormatDescriptionKey_Value

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_DependsOnOthers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_DisplayImmediately

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_DoNotDisplay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_EarlierDisplayTimesAllowed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_HasRedundantCoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_IsDependedOnByOthers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_NotSync

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleAttachmentKey_PartialSync

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_DrainAfterDecoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_DroppedFrameReason

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMSampleBufferAttachmentKey_EmptyMedia

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_GradualDecoderRefresh

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCMSampleBufferAttachmentKey_PermanentEmptyMedia

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_ResumeOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_Reverse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_SampleReferenceByteOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_SampleReferenceURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_SpeedMultiplier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_TransitionID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_TrimDurationAtEnd

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferAttachmentKey_TrimDurationAtStart

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCMSampleBufferConduitNotificationParameter_ResumeTag

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCMSampleBufferConduitNotification_InhibitOutputUntil

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferConduitNotification_ResetOutput

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCMSampleBufferConsumerNotification_BufferConsumed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMSampleBufferDroppedFrameReason_Discontinuity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMSampleBufferDroppedFrameReason_FrameWasLate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMSampleBufferDroppedFrameReason_OutOfBuffers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMSampleBufferNotification_DataBecameReady

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionColor_Alpha

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionColor_Blue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionColor_Green

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionColor_Red

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_BackgroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_DefaultFontName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_DefaultStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_DefaultTextBox

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_DisplayFlags

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_FontTable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_HorizontalJustification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_TextJustification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionExtension_VerticalJustification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionRect_Bottom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionRect_Left

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionRect_Right

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionRect_Top

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_Ascent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_EndChar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_Font

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_FontFace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_FontSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_ForegroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_Height

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextFormatDescriptionStyle_StartChar

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTextMarkupAlignmentType_End

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAlignmentType_Left

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAlignmentType_Middle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAlignmentType_Right

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAlignmentType_Start

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_Alignment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_BackgroundColorARGB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_BoldStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_CharacterBackgroundColorARGB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_CharacterEdgeStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_FontFamilyName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_ForegroundColorARGB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_GenericFontFamilyName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_ItalicStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_RelativeFontSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_UnderlineStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTextMarkupAttribute_VerticalLayout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupAttribute_WritingDirectionSizePercentage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupCharacterEdgeStyle_Depressed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupCharacterEdgeStyle_DropShadow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupCharacterEdgeStyle_None

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupCharacterEdgeStyle_Raised

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupCharacterEdgeStyle_Uniform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Casual

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Cursive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Default

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Fantasy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Monospace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_MonospaceSansSerif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_MonospaceSerif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_ProportionalSansSerif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_ProportionalSerif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_SansSerif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_Serif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextMarkupGenericFontName_SmallCapital

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextVerticalLayout_LeftToRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTextVerticalLayout_RightToLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTimeCodeFormatDescriptionExtension_SourceReferenceName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeCodeFormatDescriptionKey_LangCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeCodeFormatDescriptionKey_Value

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeEpochKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeFlagsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeIndefinite

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeNegativeInfinity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimePositiveInfinity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeRangeDurationKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeRangeInvalid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeRangeStartKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeRangeZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeScaleKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeValueKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimeZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCMTimebaseNotificationKey_EventTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCMTimebaseNotification_EffectiveRateChanged

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTimebaseNotification_TimeJumped

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCMTimingInfoInvalid

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
