---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreMedia.html
archived_at: '2026-07-18T02:52:59.982097Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreMedia Changes for Objective-C

### CoreMedia

#### CMAttachment.h

Modified [CMCopyDictionaryOfAttachments()](https://developer.apple.com/documentation/coremedia/1470699-cmcopydictionaryofattachments)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CMCopyDictionaryOfAttachments (     CFAllocatorRef allocator,     CMAttachmentBearerRef target,     CMAttachmentMode attachmentMode ); ``` |
| To | ``` CFDictionaryRef _Nullable CMCopyDictionaryOfAttachments (     CFAllocatorRef _Nullable allocator,     CMAttachmentBearerRef _Nonnull target,     CMAttachmentMode attachmentMode ); ``` |

Modified [CMGetAttachment()](https://developer.apple.com/documentation/coremedia/1470707-cmgetattachment)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef CMGetAttachment (     CMAttachmentBearerRef target,     CFStringRef key,     CMAttachmentMode *attachmentModeOut ); ``` |
| To | ``` CFTypeRef _Nullable CMGetAttachment (     CMAttachmentBearerRef _Nonnull target,     CFStringRef _Nonnull key,     CMAttachmentMode * _Nullable attachmentModeOut ); ``` |

Modified [CMPropagateAttachments()](https://developer.apple.com/documentation/coremedia/1470701-cmpropagateattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CMPropagateAttachments (     CMAttachmentBearerRef source,     CMAttachmentBearerRef destination ); ``` |
| To | ``` void CMPropagateAttachments (     CMAttachmentBearerRef _Nonnull source,     CMAttachmentBearerRef _Nonnull destination ); ``` |

Modified [CMRemoveAllAttachments()](https://developer.apple.com/documentation/coremedia/1470705-cmremoveallattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CMRemoveAllAttachments (     CMAttachmentBearerRef target ); ``` |
| To | ``` void CMRemoveAllAttachments (     CMAttachmentBearerRef _Nonnull target ); ``` |

Modified [CMRemoveAttachment()](https://developer.apple.com/documentation/coremedia/1470692-cmremoveattachment)

|  | Declaration |
| --- | --- |
| From | ``` void CMRemoveAttachment (     CMAttachmentBearerRef target,     CFStringRef key ); ``` |
| To | ``` void CMRemoveAttachment (     CMAttachmentBearerRef _Nonnull target,     CFStringRef _Nonnull key ); ``` |

Modified [CMSetAttachment()](https://developer.apple.com/documentation/coremedia/1470696-cmsetattachment)

|  | Declaration |
| --- | --- |
| From | ``` void CMSetAttachment (     CMAttachmentBearerRef target,     CFStringRef key,     CFTypeRef value,     CMAttachmentMode attachmentMode ); ``` |
| To | ``` void CMSetAttachment (     CMAttachmentBearerRef _Nonnull target,     CFStringRef _Nonnull key,     CFTypeRef _Nullable value,     CMAttachmentMode attachmentMode ); ``` |

Modified [CMSetAttachments()](https://developer.apple.com/documentation/coremedia/1470690-cmsetattachments)

|  | Declaration |
| --- | --- |
| From | ``` void CMSetAttachments (     CMAttachmentBearerRef target,     CFDictionaryRef theAttachments,     CMAttachmentMode attachmentMode ); ``` |
| To | ``` void CMSetAttachments (     CMAttachmentBearerRef _Nonnull target,     CFDictionaryRef _Nonnull theAttachments,     CMAttachmentMode attachmentMode ); ``` |

#### CMAudioDeviceClock.h

Modified [CMAudioDeviceClockCreate()](https://developer.apple.com/documentation/coremedia/1409883-cmaudiodeviceclockcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioDeviceClockCreate (     CFAllocatorRef allocator,     CFStringRef deviceUID,     CMClockRef *clockOut ); ``` |
| To | ``` OSStatus CMAudioDeviceClockCreate (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nullable deviceUID,     CMClockRef  _Nullable * _Nonnull clockOut ); ``` |

Modified [CMAudioDeviceClockCreateFromAudioDeviceID()](https://developer.apple.com/documentation/coremedia/1409881-cmaudiodeviceclockcreatefromaudi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioDeviceClockCreateFromAudioDeviceID (     CFAllocatorRef allocator,     AudioDeviceID deviceID,     CMClockRef *clockOut ); ``` |
| To | ``` OSStatus CMAudioDeviceClockCreateFromAudioDeviceID (     CFAllocatorRef _Nullable allocator,     AudioDeviceID deviceID,     CMClockRef  _Nullable * _Nonnull clockOut ); ``` |

Modified [CMAudioDeviceClockGetAudioDevice()](https://developer.apple.com/documentation/coremedia/1409885-cmaudiodeviceclockgetaudiodevice)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioDeviceClockGetAudioDevice (     CMClockRef clock,     CFStringRef *deviceUIDOut,     AudioDeviceID *deviceIDOut,     Boolean *trackingDefaultDeviceOut ); ``` |
| To | ``` OSStatus CMAudioDeviceClockGetAudioDevice (     CMClockRef _Nonnull clock,     CFStringRef  _Nullable * _Nullable deviceUIDOut,     AudioDeviceID * _Nullable deviceIDOut,     Boolean * _Nullable trackingDefaultDeviceOut ); ``` |

Modified [CMAudioDeviceClockSetAudioDeviceID()](https://developer.apple.com/documentation/coremedia/1409877-cmaudiodeviceclocksetaudiodevice)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioDeviceClockSetAudioDeviceID (     CMClockRef clock,     AudioDeviceID deviceID ); ``` |
| To | ``` OSStatus CMAudioDeviceClockSetAudioDeviceID (     CMClockRef _Nonnull clock,     AudioDeviceID deviceID ); ``` |

Modified [CMAudioDeviceClockSetAudioDeviceUID()](https://developer.apple.com/documentation/coremedia/1409879-cmaudiodeviceclocksetaudiodevice)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioDeviceClockSetAudioDeviceUID (     CMClockRef clock,     CFStringRef deviceUID ); ``` |
| To | ``` OSStatus CMAudioDeviceClockSetAudioDeviceUID (     CMClockRef _Nonnull clock,     CFStringRef _Nullable deviceUID ); ``` |

#### CMBase.h

Added #def CM_ASSUME_NONNULL_BEGINAdded #def CM_ASSUME_NONNULL_ENDAdded #def CM_BRIDGED_TYPEAdded #def CM_NONNULLAdded #def CM_NULLABLEAdded #def CM_RETURNS_NOT_RETAINED_PARAMETERAdded #def CM_RETURNS_RETAINEDAdded #def CM_RETURNS_RETAINED_PARAMETERAdded #def COREMEDIA_DECLARE_BRIDGED_TYPESAdded #def COREMEDIA_DECLARE_NULLABILITYAdded #def COREMEDIA_DECLARE_NULLABILITY_BEGIN_ENDAdded #def COREMEDIA_DECLARE_RETURNS_NOT_RETAINED_ON_PARAMETERSAdded #def COREMEDIA_DECLARE_RETURNS_RETAINEDAdded #def COREMEDIA_DECLARE_RETURNS_RETAINED_ON_PARAMETERSAdded #def COREMEDIA_USE_DERIVED_ENUMS_FOR_CONSTANTS

#### CMBlockBuffer.h

Modified [CMBlockBufferAccessDataBytes()](https://developer.apple.com/documentation/coremedia/1489228-cmblockbufferaccessdatabytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferAccessDataBytes (     CMBlockBufferRef theBuffer,     size_t offset,     size_t length,     void *temporaryBlock,     char **returnedPointer ); ``` |
| To | ``` OSStatus CMBlockBufferAccessDataBytes (     CMBlockBufferRef _Nonnull theBuffer,     size_t offset,     size_t length,     void * _Nonnull temporaryBlock,     char * _Nullable * _Nonnull returnedPointer ); ``` |

Modified [CMBlockBufferAppendBufferReference()](https://developer.apple.com/documentation/coremedia/1489160-cmblockbufferappendbufferreferen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferAppendBufferReference (     CMBlockBufferRef theBuffer,     CMBlockBufferRef targetBBuf,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags ); ``` |
| To | ``` OSStatus CMBlockBufferAppendBufferReference (     CMBlockBufferRef _Nonnull theBuffer,     CMBlockBufferRef _Nonnull targetBBuf,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags ); ``` |

Modified [CMBlockBufferAppendMemoryBlock()](https://developer.apple.com/documentation/coremedia/1489394-cmblockbufferappendmemoryblock)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferAppendMemoryBlock (     CMBlockBufferRef theBuffer,     void *memoryBlock,     size_t blockLength,     CFAllocatorRef blockAllocator,     const CMBlockBufferCustomBlockSource *customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags ); ``` |
| To | ``` OSStatus CMBlockBufferAppendMemoryBlock (     CMBlockBufferRef _Nonnull theBuffer,     void * _Nullable memoryBlock,     size_t blockLength,     CFAllocatorRef _Nullable blockAllocator,     const CMBlockBufferCustomBlockSource * _Nullable customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags ); ``` |

Modified [CMBlockBufferAssureBlockMemory()](https://developer.apple.com/documentation/coremedia/1489560-cmblockbufferassureblockmemory)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferAssureBlockMemory (     CMBlockBufferRef theBuffer ); ``` |
| To | ``` OSStatus CMBlockBufferAssureBlockMemory (     CMBlockBufferRef _Nonnull theBuffer ); ``` |

Modified [CMBlockBufferCopyDataBytes()](https://developer.apple.com/documentation/coremedia/1489155-cmblockbuffercopydatabytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferCopyDataBytes (     CMBlockBufferRef theSourceBuffer,     size_t offsetToData,     size_t dataLength,     void *destination ); ``` |
| To | ``` OSStatus CMBlockBufferCopyDataBytes (     CMBlockBufferRef _Nonnull theSourceBuffer,     size_t offsetToData,     size_t dataLength,     void * _Nonnull destination ); ``` |

Modified [CMBlockBufferCreateContiguous()](https://developer.apple.com/documentation/coremedia/1489220-cmblockbuffercreatecontiguous)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferCreateContiguous (     CFAllocatorRef structureAllocator,     CMBlockBufferRef sourceBuffer,     CFAllocatorRef blockAllocator,     const CMBlockBufferCustomBlockSource *customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef *newBBufOut ); ``` |
| To | ``` OSStatus CMBlockBufferCreateContiguous (     CFAllocatorRef _Nullable structureAllocator,     CMBlockBufferRef _Nonnull sourceBuffer,     CFAllocatorRef _Nullable blockAllocator,     const CMBlockBufferCustomBlockSource * _Nullable customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef  _Nullable * _Nonnull newBBufOut ); ``` |

Modified [CMBlockBufferCreateEmpty()](https://developer.apple.com/documentation/coremedia/1489149-cmblockbuffercreateempty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferCreateEmpty (     CFAllocatorRef structureAllocator,     uint32_t subBlockCapacity,     CMBlockBufferFlags flags,     CMBlockBufferRef *newBBufOut ); ``` |
| To | ``` OSStatus CMBlockBufferCreateEmpty (     CFAllocatorRef _Nullable structureAllocator,     uint32_t subBlockCapacity,     CMBlockBufferFlags flags,     CMBlockBufferRef  _Nullable * _Nonnull newBBufOut ); ``` |

Modified [CMBlockBufferCreateWithBufferReference()](https://developer.apple.com/documentation/coremedia/1489279-cmblockbuffercreatewithbufferref)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferCreateWithBufferReference (     CFAllocatorRef structureAllocator,     CMBlockBufferRef targetBuffer,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef *newBBufOut ); ``` |
| To | ``` OSStatus CMBlockBufferCreateWithBufferReference (     CFAllocatorRef _Nullable structureAllocator,     CMBlockBufferRef _Nonnull targetBuffer,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef  _Nullable * _Nonnull newBBufOut ); ``` |

Modified [CMBlockBufferCreateWithMemoryBlock()](https://developer.apple.com/documentation/coremedia/1489501-cmblockbuffercreatewithmemoryblo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferCreateWithMemoryBlock (     CFAllocatorRef structureAllocator,     void *memoryBlock,     size_t blockLength,     CFAllocatorRef blockAllocator,     const CMBlockBufferCustomBlockSource *customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef *newBBufOut ); ``` |
| To | ``` OSStatus CMBlockBufferCreateWithMemoryBlock (     CFAllocatorRef _Nullable structureAllocator,     void * _Nullable memoryBlock,     size_t blockLength,     CFAllocatorRef _Nullable blockAllocator,     const CMBlockBufferCustomBlockSource * _Nullable customBlockSource,     size_t offsetToData,     size_t dataLength,     CMBlockBufferFlags flags,     CMBlockBufferRef  _Nullable * _Nonnull newBBufOut ); ``` |

Modified [CMBlockBufferFillDataBytes()](https://developer.apple.com/documentation/coremedia/1489550-cmblockbufferfilldatabytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferFillDataBytes (     char fillByte,     CMBlockBufferRef destinationBuffer,     size_t offsetIntoDestination,     size_t dataLength ); ``` |
| To | ``` OSStatus CMBlockBufferFillDataBytes (     char fillByte,     CMBlockBufferRef _Nonnull destinationBuffer,     size_t offsetIntoDestination,     size_t dataLength ); ``` |

Modified [CMBlockBufferGetDataLength()](https://developer.apple.com/documentation/coremedia/1489292-cmblockbuffergetdatalength)

|  | Declaration |
| --- | --- |
| From | ``` size_t CMBlockBufferGetDataLength (     CMBlockBufferRef theBuffer ); ``` |
| To | ``` size_t CMBlockBufferGetDataLength (     CMBlockBufferRef _Nonnull theBuffer ); ``` |

Modified [CMBlockBufferGetDataPointer()](https://developer.apple.com/documentation/coremedia/1489264-cmblockbuffergetdatapointer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferGetDataPointer (     CMBlockBufferRef theBuffer,     size_t offset,     size_t *lengthAtOffset,     size_t *totalLength,     char **dataPointer ); ``` |
| To | ``` OSStatus CMBlockBufferGetDataPointer (     CMBlockBufferRef _Nonnull theBuffer,     size_t offset,     size_t * _Nullable lengthAtOffset,     size_t * _Nullable totalLength,     char * _Nullable * _Nullable dataPointer ); ``` |

Modified [CMBlockBufferIsEmpty()](https://developer.apple.com/documentation/coremedia/1489813-cmblockbufferisempty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBlockBufferIsEmpty (     CMBlockBufferRef theBuffer ); ``` |
| To | ``` Boolean CMBlockBufferIsEmpty (     CMBlockBufferRef _Nonnull theBuffer ); ``` |

Modified [CMBlockBufferIsRangeContiguous()](https://developer.apple.com/documentation/coremedia/1489609-cmblockbufferisrangecontiguous)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBlockBufferIsRangeContiguous (     CMBlockBufferRef theBuffer,     size_t offset,     size_t length ); ``` |
| To | ``` Boolean CMBlockBufferIsRangeContiguous (     CMBlockBufferRef _Nonnull theBuffer,     size_t offset,     size_t length ); ``` |

Modified [CMBlockBufferReplaceDataBytes()](https://developer.apple.com/documentation/coremedia/1489222-cmblockbufferreplacedatabytes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBlockBufferReplaceDataBytes (     const void *sourceBytes,     CMBlockBufferRef destinationBuffer,     size_t offsetIntoDestination,     size_t dataLength ); ``` |
| To | ``` OSStatus CMBlockBufferReplaceDataBytes (     const void * _Nonnull sourceBytes,     CMBlockBufferRef _Nonnull destinationBuffer,     size_t offsetIntoDestination,     size_t dataLength ); ``` |

#### CMBufferQueue.h

Modified [CMBufferQueueCallForEachBuffer()](https://developer.apple.com/documentation/coremedia/1489798-cmbufferqueuecallforeachbuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueCallForEachBuffer (     CMBufferQueueRef queue,     OSStatus (*callback)(CMBufferRef buffer, void *refcon),     void *refcon ); ``` |
| To | ``` OSStatus CMBufferQueueCallForEachBuffer (     CMBufferQueueRef _Nonnull queue,     OSStatus (* _Nonnullcallback)(CMBufferRef _Nonnull buffer, void * _Nullable refcon),     void * _Nullable refcon ); ``` |

Modified [CMBufferQueueContainsEndOfData()](https://developer.apple.com/documentation/coremedia/1489480-cmbufferqueuecontainsendofdata)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBufferQueueContainsEndOfData (     CMBufferQueueRef queue ); ``` |
| To | ``` Boolean CMBufferQueueContainsEndOfData (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueCreate()](https://developer.apple.com/documentation/coremedia/1489604-cmbufferqueuecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueCreate (     CFAllocatorRef allocator,     CMItemCount capacity,     const CMBufferCallbacks *callbacks,     CMBufferQueueRef *queueOut ); ``` |
| To | ``` OSStatus CMBufferQueueCreate (     CFAllocatorRef _Nullable allocator,     CMItemCount capacity,     const CMBufferCallbacks * _Nonnull callbacks,     CMBufferQueueRef  _Nullable * _Nonnull queueOut ); ``` |

Modified [CMBufferQueueDequeueAndRetain()](https://developer.apple.com/documentation/coremedia/1564482-cmbufferqueuedequeue)

|  | Declaration |
| --- | --- |
| From | ``` CMBufferRef CMBufferQueueDequeueAndRetain (     CMBufferQueueRef queue ); ``` |
| To | ``` CMBufferRef _Nullable CMBufferQueueDequeueAndRetain (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueDequeueIfDataReadyAndRetain()](https://developer.apple.com/documentation/coremedia/1564483-cmbufferqueuedequeueifdataready)

|  | Declaration |
| --- | --- |
| From | ``` CMBufferRef CMBufferQueueDequeueIfDataReadyAndRetain (     CMBufferQueueRef queue ); ``` |
| To | ``` CMBufferRef _Nullable CMBufferQueueDequeueIfDataReadyAndRetain (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueEnqueue()](https://developer.apple.com/documentation/coremedia/1489422-cmbufferqueueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueEnqueue (     CMBufferQueueRef queue,     CMBufferRef buf ); ``` |
| To | ``` OSStatus CMBufferQueueEnqueue (     CMBufferQueueRef _Nonnull queue,     CMBufferRef _Nonnull buf ); ``` |

Modified [CMBufferQueueGetBufferCount()](https://developer.apple.com/documentation/coremedia/1489589-cmbufferqueuegetbuffercount)

|  | Declaration |
| --- | --- |
| From | ``` CMItemCount CMBufferQueueGetBufferCount (     CMBufferQueueRef queue ); ``` |
| To | ``` CMItemCount CMBufferQueueGetBufferCount (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS()](https://developer.apple.com/documentation/coremedia/1489625-cmbufferqueuegetcallbacksforsamp)

|  | Declaration |
| --- | --- |
| From | ``` const CMBufferCallbacks * CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS (     void ); ``` |
| To | ``` const CMBufferCallbacks * _Nonnull CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS (     void ); ``` |

Modified [CMBufferQueueGetCallbacksForUnsortedSampleBuffers()](https://developer.apple.com/documentation/coremedia/1489327-cmbufferqueuegetcallbacksforunso)

|  | Declaration |
| --- | --- |
| From | ``` const CMBufferCallbacks * CMBufferQueueGetCallbacksForUnsortedSampleBuffers (     void ); ``` |
| To | ``` const CMBufferCallbacks * _Nonnull CMBufferQueueGetCallbacksForUnsortedSampleBuffers (     void ); ``` |

Modified [CMBufferQueueGetDuration()](https://developer.apple.com/documentation/coremedia/1489766-cmbufferqueuegetduration)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetDuration (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetDuration (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetEndPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489229-cmbufferqueuegetendpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetEndPresentationTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetEndPresentationTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetFirstDecodeTimeStamp()](https://developer.apple.com/documentation/coremedia/1489487-cmbufferqueuegetfirstdecodetimes)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetFirstDecodeTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetFirstDecodeTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetFirstPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489143-cmbufferqueuegetfirstpresentatio)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetFirstPresentationTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetFirstPresentationTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetHead()](https://developer.apple.com/documentation/coremedia/1489558-cmbufferqueuegethead)

|  | Declaration |
| --- | --- |
| From | ``` CMBufferRef CMBufferQueueGetHead (     CMBufferQueueRef queue ); ``` |
| To | ``` CMBufferRef _Nullable CMBufferQueueGetHead (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetMaxPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489685-cmbufferqueuegetmaxpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetMaxPresentationTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetMaxPresentationTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetMinDecodeTimeStamp()](https://developer.apple.com/documentation/coremedia/1489486-cmbufferqueuegetmindecodetimesta)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetMinDecodeTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetMinDecodeTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetMinPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489317-cmbufferqueuegetminpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMBufferQueueGetMinPresentationTimeStamp (     CMBufferQueueRef queue ); ``` |
| To | ``` CMTime CMBufferQueueGetMinPresentationTimeStamp (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueGetTotalSize()](https://developer.apple.com/documentation/coremedia/1489793-cmbufferqueuegettotalsize)

|  | Declaration |
| --- | --- |
| From | ``` size_t CMBufferQueueGetTotalSize (     CMBufferQueueRef queue ); ``` |
| To | ``` size_t CMBufferQueueGetTotalSize (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueInstallTrigger()](https://developer.apple.com/documentation/coremedia/1489822-cmbufferqueueinstalltrigger)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueInstallTrigger (     CMBufferQueueRef queue,     CMBufferQueueTriggerCallback triggerCallback,     void *triggerRefcon,     CMBufferQueueTriggerCondition triggerCondition,     CMTime triggerTime,     CMBufferQueueTriggerToken *triggerTokenOut ); ``` |
| To | ``` OSStatus CMBufferQueueInstallTrigger (     CMBufferQueueRef _Nonnull queue,     CMBufferQueueTriggerCallback _Nullable triggerCallback,     void * _Nullable triggerRefcon,     CMBufferQueueTriggerCondition triggerCondition,     CMTime triggerTime,     CMBufferQueueTriggerToken  _Nullable * _Nonnull triggerTokenOut ); ``` |

Modified [CMBufferQueueInstallTriggerWithIntegerThreshold()](https://developer.apple.com/documentation/coremedia/1489140-cmbufferqueueinstalltriggerwithi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueInstallTriggerWithIntegerThreshold (     CMBufferQueueRef queue,     CMBufferQueueTriggerCallback triggerCallback,     void *triggerRefcon,     CMBufferQueueTriggerCondition triggerCondition,     CMItemCount triggerThreshold,     CMBufferQueueTriggerToken *triggerTokenOut ); ``` |
| To | ``` OSStatus CMBufferQueueInstallTriggerWithIntegerThreshold (     CMBufferQueueRef _Nonnull queue,     CMBufferQueueTriggerCallback _Nullable triggerCallback,     void * _Nullable triggerRefcon,     CMBufferQueueTriggerCondition triggerCondition,     CMItemCount triggerThreshold,     CMBufferQueueTriggerToken  _Nullable * _Nonnull triggerTokenOut ); ``` |

Modified [CMBufferQueueIsAtEndOfData()](https://developer.apple.com/documentation/coremedia/1489131-cmbufferqueueisatendofdata)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBufferQueueIsAtEndOfData (     CMBufferQueueRef queue ); ``` |
| To | ``` Boolean CMBufferQueueIsAtEndOfData (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueIsEmpty()](https://developer.apple.com/documentation/coremedia/1489479-cmbufferqueueisempty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBufferQueueIsEmpty (     CMBufferQueueRef queue ); ``` |
| To | ``` Boolean CMBufferQueueIsEmpty (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueMarkEndOfData()](https://developer.apple.com/documentation/coremedia/1489584-cmbufferqueuemarkendofdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueMarkEndOfData (     CMBufferQueueRef queue ); ``` |
| To | ``` OSStatus CMBufferQueueMarkEndOfData (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueRemoveTrigger()](https://developer.apple.com/documentation/coremedia/1489445-cmbufferqueueremovetrigger)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueRemoveTrigger (     CMBufferQueueRef queue,     CMBufferQueueTriggerToken triggerToken ); ``` |
| To | ``` OSStatus CMBufferQueueRemoveTrigger (     CMBufferQueueRef _Nonnull queue,     CMBufferQueueTriggerToken _Nonnull triggerToken ); ``` |

Modified [CMBufferQueueReset()](https://developer.apple.com/documentation/coremedia/1489291-cmbufferqueuereset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueReset (     CMBufferQueueRef queue ); ``` |
| To | ``` OSStatus CMBufferQueueReset (     CMBufferQueueRef _Nonnull queue ); ``` |

Modified [CMBufferQueueResetWithCallback()](https://developer.apple.com/documentation/coremedia/1489361-cmbufferqueueresetwithcallback)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueResetWithCallback (     CMBufferQueueRef queue,     void (*callback)(CMBufferRef buffer, void *refcon),     void *refcon ); ``` |
| To | ``` OSStatus CMBufferQueueResetWithCallback (     CMBufferQueueRef _Nonnull queue,     void (* _Nonnullcallback)(CMBufferRef _Nonnull buffer, void * _Nullable refcon),     void * _Nullable refcon ); ``` |

Modified [CMBufferQueueSetValidationCallback()](https://developer.apple.com/documentation/coremedia/1489350-cmbufferqueuesetvalidationcallba)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMBufferQueueSetValidationCallback (     CMBufferQueueRef queue,     CMBufferValidationCallback validationCallback,     void *validationRefCon ); ``` |
| To | ``` OSStatus CMBufferQueueSetValidationCallback (     CMBufferQueueRef _Nonnull queue,     CMBufferValidationCallback _Nonnull validationCallback,     void * _Nullable validationRefCon ); ``` |

Modified [CMBufferQueueTestTrigger()](https://developer.apple.com/documentation/coremedia/1489135-cmbufferqueuetesttrigger)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMBufferQueueTestTrigger (     CMBufferQueueRef queue,     CMBufferQueueTriggerToken triggerToken ); ``` |
| To | ``` Boolean CMBufferQueueTestTrigger (     CMBufferQueueRef _Nonnull queue,     CMBufferQueueTriggerToken _Nonnull triggerToken ); ``` |

#### CMFormatDescription.h

Added [kCMFormatDescriptionChromaLocation_Bottom](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottom)Added [kCMFormatDescriptionChromaLocation_BottomLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottomleft)Added [kCMFormatDescriptionChromaLocation_Center](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_center)Added [kCMFormatDescriptionChromaLocation_DV420](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_dv420)Added [kCMFormatDescriptionChromaLocation_Left](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_left)Added [kCMFormatDescriptionChromaLocation_Top](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_top)Added [kCMFormatDescriptionChromaLocation_TopLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_topleft)Added [kCMFormatDescriptionColorPrimaries_DCI_P3](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_dci_p3)Added [kCMFormatDescriptionColorPrimaries_EBU_3213](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_ebu_3213)Added [kCMFormatDescriptionColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_2020)Added [kCMFormatDescriptionColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_709_2)Added [kCMFormatDescriptionColorPrimaries_P3_D65](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p3_d65)Added [kCMFormatDescriptionColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_smpte_c)Added [kCMFormatDescriptionExtension_ChromaLocationBottomField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationbottomfield)Added [kCMFormatDescriptionExtension_ChromaLocationTopField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationtopfield)Added [kCMFormatDescriptionExtension_CleanAperture](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_cleanaperture)Added [kCMFormatDescriptionExtension_ColorPrimaries](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_colorprimaries)Added [kCMFormatDescriptionExtension_FieldCount](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fieldcount)Added [kCMFormatDescriptionExtension_FieldDetail](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fielddetail)Added [kCMFormatDescriptionExtension_GammaLevel](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_gammalevel)Added [kCMFormatDescriptionExtension_PixelAspectRatio](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_pixelaspectratio)Added [kCMFormatDescriptionExtension_TransferFunction](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_transferfunction)Added [kCMFormatDescriptionExtension_VerbatimImageDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_verbatimimagedescription)Added [kCMFormatDescriptionExtension_YCbCrMatrix](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_ycbcrmatrix)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineEarly](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlineearly)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineLate](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlinelate)Added [kCMFormatDescriptionFieldDetail_TemporalBottomFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporalbottomfirst)Added [kCMFormatDescriptionFieldDetail_TemporalTopFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporaltopfirst)Added [kCMFormatDescriptionKey_CleanApertureHeight](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureheight)Added [kCMFormatDescriptionKey_CleanApertureHorizontalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturehorizontaloffset)Added [kCMFormatDescriptionKey_CleanApertureVerticalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureverticaloffset)Added [kCMFormatDescriptionKey_CleanApertureWidth](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturewidth)Added [kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratiohorizontalspacing)Added [kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratioverticalspacing)Added [kCMFormatDescriptionTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_2020)Added [kCMFormatDescriptionTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_709_2)Added [kCMFormatDescriptionTransferFunction_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_smpte_240m_1995)Added [kCMFormatDescriptionTransferFunction_UseGamma](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_usegamma)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_2020)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_601_4)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_709_2)Added [kCMFormatDescriptionYCbCrMatrix_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_smpte_240m_1995)Added [kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescription_structuraldependencykey_dependencyisinvalidflag)Added [kCMMetadataFormatDescriptionKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_structuraldependency)Added [kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_structuraldependency)Added [kCMVideoCodecType_HEVC](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_hevc)Modified [CMAudioFormatDescriptionCreate()](https://developer.apple.com/documentation/coremedia/1489522-cmaudioformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioFormatDescriptionCreate (     CFAllocatorRef allocator,     const AudioStreamBasicDescription *asbd,     size_t layoutSize,     const AudioChannelLayout *layout,     size_t magicCookieSize,     const void *magicCookie,     CFDictionaryRef extensions,     CMAudioFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMAudioFormatDescriptionCreate (     CFAllocatorRef _Nullable allocator,     const AudioStreamBasicDescription * _Nonnull asbd,     size_t layoutSize,     const AudioChannelLayout * _Nullable layout,     size_t magicCookieSize,     const void * _Nullable magicCookie,     CFDictionaryRef _Nullable extensions,     CMAudioFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMAudioFormatDescriptionCreateSummary()](https://developer.apple.com/documentation/coremedia/1489608-cmaudioformatdescriptioncreatesu)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioFormatDescriptionCreateSummary (     CFAllocatorRef allocator,     CFArrayRef formatDescriptionArray,     uint32_t flags,     CMAudioFormatDescriptionRef *summaryFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMAudioFormatDescriptionCreateSummary (     CFAllocatorRef _Nullable allocator,     CFArrayRef _Nonnull formatDescriptionArray,     uint32_t flags,     CMAudioFormatDescriptionRef  _Nullable * _Nonnull summaryFormatDescriptionOut ); ``` |

Modified [CMAudioFormatDescriptionEqual()](https://developer.apple.com/documentation/coremedia/1489582-cmaudioformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMAudioFormatDescriptionEqual (     CMAudioFormatDescriptionRef desc1,     CMAudioFormatDescriptionRef desc2,     CMAudioFormatDescriptionMask equalityMask,     CMAudioFormatDescriptionMask *equalityMaskOut ); ``` |
| To | ``` Boolean CMAudioFormatDescriptionEqual (     CMAudioFormatDescriptionRef _Nonnull desc1,     CMAudioFormatDescriptionRef _Nonnull desc2,     CMAudioFormatDescriptionMask equalityMask,     CMAudioFormatDescriptionMask * _Nullable equalityMaskOut ); ``` |

Modified [CMAudioFormatDescriptionGetChannelLayout()](https://developer.apple.com/documentation/coremedia/1489137-cmaudioformatdescriptiongetchann)

|  | Declaration |
| --- | --- |
| From | ``` const AudioChannelLayout * CMAudioFormatDescriptionGetChannelLayout (     CMAudioFormatDescriptionRef desc,     size_t *layoutSize ); ``` |
| To | ``` const AudioChannelLayout * _Nullable CMAudioFormatDescriptionGetChannelLayout (     CMAudioFormatDescriptionRef _Nonnull desc,     size_t * _Nullable layoutSize ); ``` |

Modified [CMAudioFormatDescriptionGetFormatList()](https://developer.apple.com/documentation/coremedia/1489782-cmaudioformatdescriptiongetforma)

|  | Declaration |
| --- | --- |
| From | ``` const AudioFormatListItem * CMAudioFormatDescriptionGetFormatList (     CMAudioFormatDescriptionRef desc,     size_t *formatListSize ); ``` |
| To | ``` const AudioFormatListItem * _Nullable CMAudioFormatDescriptionGetFormatList (     CMAudioFormatDescriptionRef _Nonnull desc,     size_t * _Nullable formatListSize ); ``` |

Modified [CMAudioFormatDescriptionGetMagicCookie()](https://developer.apple.com/documentation/coremedia/1489508-cmaudioformatdescriptiongetmagic)

|  | Declaration |
| --- | --- |
| From | ``` const void * CMAudioFormatDescriptionGetMagicCookie (     CMAudioFormatDescriptionRef desc,     size_t *cookieSizeOut ); ``` |
| To | ``` const void * _Nullable CMAudioFormatDescriptionGetMagicCookie (     CMAudioFormatDescriptionRef _Nonnull desc,     size_t * _Nullable cookieSizeOut ); ``` |

Modified [CMAudioFormatDescriptionGetMostCompatibleFormat()](https://developer.apple.com/documentation/coremedia/1489474-cmaudioformatdescriptiongetmostc)

|  | Declaration |
| --- | --- |
| From | ``` const AudioFormatListItem * CMAudioFormatDescriptionGetMostCompatibleFormat (     CMAudioFormatDescriptionRef desc ); ``` |
| To | ``` const AudioFormatListItem * _Nullable CMAudioFormatDescriptionGetMostCompatibleFormat (     CMAudioFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMAudioFormatDescriptionGetRichestDecodableFormat()](https://developer.apple.com/documentation/coremedia/1489575-cmaudioformatdescriptiongetriche)

|  | Declaration |
| --- | --- |
| From | ``` const AudioFormatListItem * CMAudioFormatDescriptionGetRichestDecodableFormat (     CMAudioFormatDescriptionRef desc ); ``` |
| To | ``` const AudioFormatListItem * _Nullable CMAudioFormatDescriptionGetRichestDecodableFormat (     CMAudioFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMAudioFormatDescriptionGetStreamBasicDescription()](https://developer.apple.com/documentation/coremedia/1489226-cmaudioformatdescriptiongetstrea)

|  | Declaration |
| --- | --- |
| From | ``` const AudioStreamBasicDescription * CMAudioFormatDescriptionGetStreamBasicDescription (     CMAudioFormatDescriptionRef desc ); ``` |
| To | ``` const AudioStreamBasicDescription * _Nullable CMAudioFormatDescriptionGetStreamBasicDescription (     CMAudioFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMFormatDescriptionCreate()](https://developer.apple.com/documentation/coremedia/1489182-cmformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMFormatDescriptionCreate (     CFAllocatorRef allocator,     CMMediaType mediaType,     FourCharCode mediaSubtype,     CFDictionaryRef extensions,     CMFormatDescriptionRef *descOut ); ``` |
| To | ``` OSStatus CMFormatDescriptionCreate (     CFAllocatorRef _Nullable allocator,     CMMediaType mediaType,     FourCharCode mediaSubtype,     CFDictionaryRef _Nullable extensions,     CMFormatDescriptionRef  _Nullable * _Nonnull descOut ); ``` |

Modified [CMFormatDescriptionEqual()](https://developer.apple.com/documentation/coremedia/1489825-cmformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMFormatDescriptionEqual (     CMFormatDescriptionRef desc1,     CMFormatDescriptionRef desc2 ); ``` |
| To | ``` Boolean CMFormatDescriptionEqual (     CMFormatDescriptionRef _Nullable desc1,     CMFormatDescriptionRef _Nullable desc2 ); ``` |

Modified [CMFormatDescriptionEqualIgnoringExtensionKeys()](https://developer.apple.com/documentation/coremedia/1489465-cmformatdescriptionequalignoring)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMFormatDescriptionEqualIgnoringExtensionKeys (     CMFormatDescriptionRef desc1,     CMFormatDescriptionRef desc2,     CFTypeRef formatDescriptionExtensionKeysToIgnore,     CFTypeRef sampleDescriptionExtensionAtomKeysToIgnore ); ``` |
| To | ``` Boolean CMFormatDescriptionEqualIgnoringExtensionKeys (     CMFormatDescriptionRef _Nullable desc1,     CMFormatDescriptionRef _Nullable desc2,     CFTypeRef _Nullable formatDescriptionExtensionKeysToIgnore,     CFTypeRef _Nullable sampleDescriptionExtensionAtomKeysToIgnore ); ``` |

Modified [CMFormatDescriptionGetExtension()](https://developer.apple.com/documentation/coremedia/1489750-cmformatdescriptiongetextension)

|  | Declaration |
| --- | --- |
| From | ``` CFPropertyListRef CMFormatDescriptionGetExtension (     CMFormatDescriptionRef desc,     CFStringRef extensionKey ); ``` |
| To | ``` CFPropertyListRef _Nullable CMFormatDescriptionGetExtension (     CMFormatDescriptionRef _Nonnull desc,     CFStringRef _Nonnull extensionKey ); ``` |

Modified [CMFormatDescriptionGetExtensions()](https://developer.apple.com/documentation/coremedia/1489170-cmformatdescriptiongetextensions)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CMFormatDescriptionGetExtensions (     CMFormatDescriptionRef desc ); ``` |
| To | ``` CFDictionaryRef _Nullable CMFormatDescriptionGetExtensions (     CMFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMFormatDescriptionGetMediaSubType()](https://developer.apple.com/documentation/coremedia/1489255-cmformatdescriptiongetmediasubty)

|  | Declaration |
| --- | --- |
| From | ``` FourCharCode CMFormatDescriptionGetMediaSubType (     CMFormatDescriptionRef desc ); ``` |
| To | ``` FourCharCode CMFormatDescriptionGetMediaSubType (     CMFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMFormatDescriptionGetMediaType()](https://developer.apple.com/documentation/coremedia/1489174-cmformatdescriptiongetmediatype)

|  | Declaration |
| --- | --- |
| From | ``` CMMediaType CMFormatDescriptionGetMediaType (     CMFormatDescriptionRef desc ); ``` |
| To | ``` CMMediaType CMFormatDescriptionGetMediaType (     CMFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions()](https://developer.apple.com/documentation/coremedia/1489346-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions (     CFAllocatorRef allocator,     CMMetadataFormatDescriptionRef srcDesc1,     CMMetadataFormatDescriptionRef srcDesc2,     CMMetadataFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions (     CFAllocatorRef _Nullable allocator,     CMMetadataFormatDescriptionRef _Nonnull srcDesc1,     CMMetadataFormatDescriptionRef _Nonnull srcDesc2,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMMetadataFormatDescriptionCreateWithKeys()](https://developer.apple.com/documentation/coremedia/1489719-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateWithKeys (     CFAllocatorRef allocator,     CMMetadataFormatType metadataType,     CFArrayRef keys,     CMMetadataFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateWithKeys (     CFAllocatorRef _Nullable allocator,     CMMetadataFormatType metadataType,     CFArrayRef _Nullable keys,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications()](https://developer.apple.com/documentation/coremedia/1489454-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications (     CFAllocatorRef allocator,     CMMetadataFormatDescriptionRef srcDesc,     CFArrayRef metadataSpecifications,     CMMetadataFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications (     CFAllocatorRef _Nullable allocator,     CMMetadataFormatDescriptionRef _Nonnull srcDesc,     CFArrayRef _Nonnull metadataSpecifications,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMMetadataFormatDescriptionCreateWithMetadataSpecifications()](https://developer.apple.com/documentation/coremedia/1489368-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateWithMetadataSpecifications (     CFAllocatorRef allocator,     CMMetadataFormatType metadataType,     CFArrayRef metadataSpecifications,     CMMetadataFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateWithMetadataSpecifications (     CFAllocatorRef _Nullable allocator,     CMMetadataFormatType metadataType,     CFArrayRef _Nonnull metadataSpecifications,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMMetadataFormatDescriptionGetIdentifiers()](https://developer.apple.com/documentation/coremedia/1489457-cmmetadataformatdescriptiongetid)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CMMetadataFormatDescriptionGetIdentifiers (     CMMetadataFormatDescriptionRef desc ); ``` |
| To | ``` CFArrayRef _Nullable CMMetadataFormatDescriptionGetIdentifiers (     CMMetadataFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMMetadataFormatDescriptionGetKeyWithLocalID()](https://developer.apple.com/documentation/coremedia/1489196-cmmetadataformatdescriptiongetke)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CMMetadataFormatDescriptionGetKeyWithLocalID (     CMMetadataFormatDescriptionRef desc,     OSType localKeyID ); ``` |
| To | ``` CFDictionaryRef _Nullable CMMetadataFormatDescriptionGetKeyWithLocalID (     CMMetadataFormatDescriptionRef _Nonnull desc,     OSType localKeyID ); ``` |

Modified [CMMuxedFormatDescriptionCreate()](https://developer.apple.com/documentation/coremedia/1489271-cmmuxedformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMuxedFormatDescriptionCreate (     CFAllocatorRef allocator,     CMMuxedStreamType muxType,     CFDictionaryRef extensions,     CMMuxedFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMMuxedFormatDescriptionCreate (     CFAllocatorRef _Nullable allocator,     CMMuxedStreamType muxType,     CFDictionaryRef _Nullable extensions,     CMMuxedFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMTextFormatDescriptionGetDefaultStyle()](https://developer.apple.com/documentation/coremedia/1489145-cmtextformatdescriptiongetdefaul)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionGetDefaultStyle (     CMFormatDescriptionRef desc,     uint16_t *outLocalFontID,     Boolean *outBold,     Boolean *outItalic,     Boolean *outUnderline,     CGFloat *outFontSize,     CGFloat outColorComponents[4] ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionGetDefaultStyle (     CMFormatDescriptionRef _Nonnull desc,     uint16_t * _Nullable outLocalFontID,     Boolean * _Nullable outBold,     Boolean * _Nullable outItalic,     Boolean * _Nullable outUnderline,     CGFloat * _Nullable outFontSize,     CGFloat outColorComponents[4] ); ``` |

Modified [CMTextFormatDescriptionGetDefaultTextBox()](https://developer.apple.com/documentation/coremedia/1489452-cmtextformatdescriptiongetdefaul)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionGetDefaultTextBox (     CMFormatDescriptionRef desc,     Boolean originIsAtTopLeft,     CGFloat heightOfTextTrack,     CGRect *outDefaultTextBox ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionGetDefaultTextBox (     CMFormatDescriptionRef _Nonnull desc,     Boolean originIsAtTopLeft,     CGFloat heightOfTextTrack,     CGRect * _Nonnull outDefaultTextBox ); ``` |

Modified [CMTextFormatDescriptionGetDisplayFlags()](https://developer.apple.com/documentation/coremedia/1489707-cmtextformatdescriptiongetdispla)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionGetDisplayFlags (     CMFormatDescriptionRef desc,     CMTextDisplayFlags *outDisplayFlags ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionGetDisplayFlags (     CMFormatDescriptionRef _Nonnull desc,     CMTextDisplayFlags * _Nonnull outDisplayFlags ); ``` |

Modified [CMTextFormatDescriptionGetFontName()](https://developer.apple.com/documentation/coremedia/1489704-cmtextformatdescriptiongetfontna)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionGetFontName (     CMFormatDescriptionRef desc,     uint16_t localFontID,     CFStringRef *outFontName ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionGetFontName (     CMFormatDescriptionRef _Nonnull desc,     uint16_t localFontID,     CFStringRef  _Nullable * _Nonnull outFontName ); ``` |

Modified [CMTextFormatDescriptionGetJustification()](https://developer.apple.com/documentation/coremedia/1489232-cmtextformatdescriptiongetjustif)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionGetJustification (     CMFormatDescriptionRef desc,     CMTextJustificationValue *outHorizontalJust,     CMTextJustificationValue *outVerticalJust ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionGetJustification (     CMFormatDescriptionRef _Nonnull desc,     CMTextJustificationValue * _Nullable outHorizontalJust,     CMTextJustificationValue * _Nullable outVerticalJust ); ``` |

Modified [CMTimeCodeFormatDescriptionCreate()](https://developer.apple.com/documentation/coremedia/1489250-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimeCodeFormatDescriptionCreate (     CFAllocatorRef allocator,     CMTimeCodeFormatType timeCodeFormatType,     CMTime frameDuration,     uint32_t frameQuanta,     uint32_t tcFlags,     CFDictionaryRef extensions,     CMTimeCodeFormatDescriptionRef *descOut ); ``` |
| To | ``` OSStatus CMTimeCodeFormatDescriptionCreate (     CFAllocatorRef _Nullable allocator,     CMTimeCodeFormatType timeCodeFormatType,     CMTime frameDuration,     uint32_t frameQuanta,     uint32_t tcFlags,     CFDictionaryRef _Nullable extensions,     CMTimeCodeFormatDescriptionRef  _Nullable * _Nonnull descOut ); ``` |

Modified [CMTimeCodeFormatDescriptionGetFrameDuration()](https://developer.apple.com/documentation/coremedia/1489815-cmtimecodeformatdescriptiongetfr)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMTimeCodeFormatDescriptionGetFrameDuration (     CMTimeCodeFormatDescriptionRef timeCodeFormatDescription ); ``` |
| To | ``` CMTime CMTimeCodeFormatDescriptionGetFrameDuration (     CMTimeCodeFormatDescriptionRef _Nonnull timeCodeFormatDescription ); ``` |

Modified [CMTimeCodeFormatDescriptionGetFrameQuanta()](https://developer.apple.com/documentation/coremedia/1489418-cmtimecodeformatdescriptiongetfr)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t CMTimeCodeFormatDescriptionGetFrameQuanta (     CMTimeCodeFormatDescriptionRef timeCodeFormatDescription ); ``` |
| To | ``` uint32_t CMTimeCodeFormatDescriptionGetFrameQuanta (     CMTimeCodeFormatDescriptionRef _Nonnull timeCodeFormatDescription ); ``` |

Modified [CMTimeCodeFormatDescriptionGetTimeCodeFlags()](https://developer.apple.com/documentation/coremedia/1489390-cmtimecodeformatdescriptiongetti)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t CMTimeCodeFormatDescriptionGetTimeCodeFlags (     CMTimeCodeFormatDescriptionRef desc ); ``` |
| To | ``` uint32_t CMTimeCodeFormatDescriptionGetTimeCodeFlags (     CMTimeCodeFormatDescriptionRef _Nonnull desc ); ``` |

Modified [CMVideoFormatDescriptionCreate()](https://developer.apple.com/documentation/coremedia/1489743-cmvideoformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCreate (     CFAllocatorRef allocator,     CMVideoCodecType codecType,     int32_t width,     int32_t height,     CFDictionaryRef extensions,     CMVideoFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCreate (     CFAllocatorRef _Nullable allocator,     CMVideoCodecType codecType,     int32_t width,     int32_t height,     CFDictionaryRef _Nullable extensions,     CMVideoFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMVideoFormatDescriptionCreateForImageBuffer()](https://developer.apple.com/documentation/coremedia/1489730-cmvideoformatdescriptioncreatefo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCreateForImageBuffer (     CFAllocatorRef allocator,     CVImageBufferRef imageBuffer,     CMVideoFormatDescriptionRef *outDesc ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCreateForImageBuffer (     CFAllocatorRef _Nullable allocator,     CVImageBufferRef _Nonnull imageBuffer,     CMVideoFormatDescriptionRef  _Nullable * _Nonnull outDesc ); ``` |

Modified [CMVideoFormatDescriptionCreateFromH264ParameterSets()](https://developer.apple.com/documentation/coremedia/1489818-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCreateFromH264ParameterSets (     CFAllocatorRef allocator,     size_t parameterSetCount,     const uint8_t *const *parameterSetPointers,     const size_t *parameterSetSizes,     int NALUnitHeaderLength,     CMFormatDescriptionRef *formatDescriptionOut ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCreateFromH264ParameterSets (     CFAllocatorRef _Nullable allocator,     size_t parameterSetCount,     const uint8_t *const  _Nonnull * _Nonnull parameterSetPointers,     const size_t * _Nonnull parameterSetSizes,     int NALUnitHeaderLength,     CMFormatDescriptionRef  _Nullable * _Nonnull formatDescriptionOut ); ``` |

Modified [CMVideoFormatDescriptionGetCleanAperture()](https://developer.apple.com/documentation/coremedia/1489235-cmvideoformatdescriptiongetclean)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CMVideoFormatDescriptionGetCleanAperture (     CMVideoFormatDescriptionRef videoDesc,     Boolean originIsAtTopLeft ); ``` |
| To | ``` CGRect CMVideoFormatDescriptionGetCleanAperture (     CMVideoFormatDescriptionRef _Nonnull videoDesc,     Boolean originIsAtTopLeft ); ``` |

Modified [CMVideoFormatDescriptionGetDimensions()](https://developer.apple.com/documentation/coremedia/1489287-cmvideoformatdescriptiongetdimen)

|  | Declaration |
| --- | --- |
| From | ``` CMVideoDimensions CMVideoFormatDescriptionGetDimensions (     CMVideoFormatDescriptionRef videoDesc ); ``` |
| To | ``` CMVideoDimensions CMVideoFormatDescriptionGetDimensions (     CMVideoFormatDescriptionRef _Nonnull videoDesc ); ``` |

Modified [CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers()](https://developer.apple.com/documentation/coremedia/1489296-cmvideoformatdescriptiongetexten)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers (     void ); ``` |
| To | ``` CFArrayRef _Nonnull CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers (     void ); ``` |

Modified [CMVideoFormatDescriptionGetH264ParameterSetAtIndex()](https://developer.apple.com/documentation/coremedia/1489529-cmvideoformatdescriptiongeth264p)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionGetH264ParameterSetAtIndex (     CMFormatDescriptionRef videoDesc,     size_t parameterSetIndex,     const uint8_t **parameterSetPointerOut,     size_t *parameterSetSizeOut,     size_t *parameterSetCountOut,     int *NALUnitHeaderLengthOut ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionGetH264ParameterSetAtIndex (     CMFormatDescriptionRef _Nonnull videoDesc,     size_t parameterSetIndex,     const uint8_t * _Nullable * _Nullable parameterSetPointerOut,     size_t * _Nullable parameterSetSizeOut,     size_t * _Nullable parameterSetCountOut,     int * _Nullable NALUnitHeaderLengthOut ); ``` |

Modified [CMVideoFormatDescriptionGetPresentationDimensions()](https://developer.apple.com/documentation/coremedia/1489218-cmvideoformatdescriptiongetprese)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CMVideoFormatDescriptionGetPresentationDimensions (     CMVideoFormatDescriptionRef videoDesc,     Boolean usePixelAspectRatio,     Boolean useCleanAperture ); ``` |
| To | ``` CGSize CMVideoFormatDescriptionGetPresentationDimensions (     CMVideoFormatDescriptionRef _Nonnull videoDesc,     Boolean usePixelAspectRatio,     Boolean useCleanAperture ); ``` |

Modified [CMVideoFormatDescriptionMatchesImageBuffer()](https://developer.apple.com/documentation/coremedia/1489579-cmvideoformatdescriptionmatchesi)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMVideoFormatDescriptionMatchesImageBuffer (     CMVideoFormatDescriptionRef desc,     CVImageBufferRef imageBuffer ); ``` |
| To | ``` Boolean CMVideoFormatDescriptionMatchesImageBuffer (     CMVideoFormatDescriptionRef _Nonnull desc,     CVImageBufferRef _Nonnull imageBuffer ); ``` |

#### CMFormatDescriptionBridge.h

Modified [CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416293-cmaudioformatdescriptioncopyasbi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMAudioFormatDescriptionRef audioFormatDescription,     CFStringRef soundDescriptionFlavor,     CMBlockBufferRef *soundDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMAudioFormatDescriptionRef _Nonnull audioFormatDescription,     CFStringRef _Nullable soundDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull soundDescriptionBlockBufferOut ); ``` |

Modified [CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416264-cmaudioformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef soundDescriptionBlockBuffer,     CFStringRef soundDescriptionFlavor,     CMAudioFormatDescriptionRef *audioFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull soundDescriptionBlockBuffer,     CFStringRef _Nullable soundDescriptionFlavor,     CMAudioFormatDescriptionRef  _Nullable * _Nonnull audioFormatDescriptionOut ); ``` |

Modified [CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData()](https://developer.apple.com/documentation/coremedia/1416299-cmaudioformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData (     CFAllocatorRef allocator,     const uint8_t *soundDescriptionData,     size_t soundDescriptionSize,     CFStringRef soundDescriptionFlavor,     CMAudioFormatDescriptionRef *audioFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull soundDescriptionData,     size_t soundDescriptionSize,     CFStringRef _Nullable soundDescriptionFlavor,     CMAudioFormatDescriptionRef  _Nullable * _Nonnull audioFormatDescriptionOut ); ``` |

Modified [CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416313-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMClosedCaptionFormatDescriptionRef closedCaptionFormatDescription,     CFStringRef closedCaptionDescriptionFlavor,     CMBlockBufferRef *closedCaptionDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMClosedCaptionFormatDescriptionRef _Nonnull closedCaptionFormatDescription,     CFStringRef _Nullable closedCaptionDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull closedCaptionDescriptionBlockBufferOut ); ``` |

Modified [CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416291-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef closedCaptionDescriptionBlockBuffer,     CFStringRef closedCaptionDescriptionFlavor,     CMClosedCaptionFormatDescriptionRef *closedCaptionFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull closedCaptionDescriptionBlockBuffer,     CFStringRef _Nullable closedCaptionDescriptionFlavor,     CMClosedCaptionFormatDescriptionRef  _Nullable * _Nonnull closedCaptionFormatDescriptionOut ); ``` |

Modified [CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData()](https://developer.apple.com/documentation/coremedia/1416295-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData (     CFAllocatorRef allocator,     const uint8_t *closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize,     CFStringRef closedCaptionDescriptionFlavor,     CMClosedCaptionFormatDescriptionRef *closedCaptionFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize,     CFStringRef _Nullable closedCaptionDescriptionFlavor,     CMClosedCaptionFormatDescriptionRef  _Nullable * _Nonnull closedCaptionFormatDescriptionOut ); ``` |

Modified [CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout()](https://developer.apple.com/documentation/coremedia/1416317-cmdoesbigendiansounddescriptionr)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout (     CMBlockBufferRef soundDescriptionBlockBuffer,     CFStringRef soundDescriptionFlavor ); ``` |
| To | ``` Boolean CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout (     CMBlockBufferRef _Nonnull soundDescriptionBlockBuffer,     CFStringRef _Nullable soundDescriptionFlavor ); ``` |

Modified [CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416249-cmmetadataformatdescriptioncopya)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMMetadataFormatDescriptionRef metadataFormatDescription,     CFStringRef metadataDescriptionFlavor,     CMBlockBufferRef *metadataDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMMetadataFormatDescriptionRef _Nonnull metadataFormatDescription,     CFStringRef _Nullable metadataDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull metadataDescriptionBlockBufferOut ); ``` |

Modified [CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416301-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef metadataDescriptionBlockBuffer,     CFStringRef metadataDescriptionFlavor,     CMMetadataFormatDescriptionRef *metadataFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull metadataDescriptionBlockBuffer,     CFStringRef _Nullable metadataDescriptionFlavor,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull metadataFormatDescriptionOut ); ``` |

Modified [CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData()](https://developer.apple.com/documentation/coremedia/1416265-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData (     CFAllocatorRef allocator,     const uint8_t *metadataDescriptionData,     size_t metadataDescriptionSize,     CFStringRef metadataDescriptionFlavor,     CMMetadataFormatDescriptionRef *metadataFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull metadataDescriptionData,     size_t metadataDescriptionSize,     CFStringRef _Nullable metadataDescriptionFlavor,     CMMetadataFormatDescriptionRef  _Nullable * _Nonnull metadataFormatDescriptionOut ); ``` |

Modified [CMSwapBigEndianClosedCaptionDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416305-cmswapbigendianclosedcaptiondesc)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianClosedCaptionDescriptionToHost (     uint8_t *closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianClosedCaptionDescriptionToHost (     uint8_t * _Nonnull closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize ); ``` |

Modified [CMSwapBigEndianImageDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416289-cmswapbigendianimagedescriptiont)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianImageDescriptionToHost (     uint8_t *imageDescriptionData,     size_t imageDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianImageDescriptionToHost (     uint8_t * _Nonnull imageDescriptionData,     size_t imageDescriptionSize ); ``` |

Modified [CMSwapBigEndianMetadataDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416251-cmswapbigendianmetadatadescripti)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianMetadataDescriptionToHost (     uint8_t *metadataDescriptionData,     size_t metadataDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianMetadataDescriptionToHost (     uint8_t * _Nonnull metadataDescriptionData,     size_t metadataDescriptionSize ); ``` |

Modified [CMSwapBigEndianSoundDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416280-cmswapbigendiansounddescriptiont)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianSoundDescriptionToHost (     uint8_t *soundDescriptionData,     size_t soundDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianSoundDescriptionToHost (     uint8_t * _Nonnull soundDescriptionData,     size_t soundDescriptionSize ); ``` |

Modified [CMSwapBigEndianTextDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416258-cmswapbigendiantextdescriptionto)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianTextDescriptionToHost (     uint8_t *textDescriptionData,     size_t textDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianTextDescriptionToHost (     uint8_t * _Nonnull textDescriptionData,     size_t textDescriptionSize ); ``` |

Modified [CMSwapBigEndianTimeCodeDescriptionToHost()](https://developer.apple.com/documentation/coremedia/1416240-cmswapbigendiantimecodedescripti)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapBigEndianTimeCodeDescriptionToHost (     uint8_t *timeCodeDescriptionData,     size_t timeCodeDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapBigEndianTimeCodeDescriptionToHost (     uint8_t * _Nonnull timeCodeDescriptionData,     size_t timeCodeDescriptionSize ); ``` |

Modified [CMSwapHostEndianClosedCaptionDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416267-cmswaphostendianclosedcaptiondes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianClosedCaptionDescriptionToBig (     uint8_t *closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianClosedCaptionDescriptionToBig (     uint8_t * _Nonnull closedCaptionDescriptionData,     size_t closedCaptionDescriptionSize ); ``` |

Modified [CMSwapHostEndianImageDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416271-cmswaphostendianimagedescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianImageDescriptionToBig (     uint8_t *imageDescriptionData,     size_t imageDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianImageDescriptionToBig (     uint8_t * _Nonnull imageDescriptionData,     size_t imageDescriptionSize ); ``` |

Modified [CMSwapHostEndianMetadataDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416268-cmswaphostendianmetadatadescript)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianMetadataDescriptionToBig (     uint8_t *metadataDescriptionData,     size_t metadataDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianMetadataDescriptionToBig (     uint8_t * _Nonnull metadataDescriptionData,     size_t metadataDescriptionSize ); ``` |

Modified [CMSwapHostEndianSoundDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416254-cmswaphostendiansounddescription)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianSoundDescriptionToBig (     uint8_t *soundDescriptionData,     size_t soundDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianSoundDescriptionToBig (     uint8_t * _Nonnull soundDescriptionData,     size_t soundDescriptionSize ); ``` |

Modified [CMSwapHostEndianTextDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416262-cmswaphostendiantextdescriptiont)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianTextDescriptionToBig (     uint8_t *textDescriptionData,     size_t textDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianTextDescriptionToBig (     uint8_t * _Nonnull textDescriptionData,     size_t textDescriptionSize ); ``` |

Modified [CMSwapHostEndianTimeCodeDescriptionToBig()](https://developer.apple.com/documentation/coremedia/1416309-cmswaphostendiantimecodedescript)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSwapHostEndianTimeCodeDescriptionToBig (     uint8_t *timeCodeDescriptionData,     size_t timeCodeDescriptionSize ); ``` |
| To | ``` OSStatus CMSwapHostEndianTimeCodeDescriptionToBig (     uint8_t * _Nonnull timeCodeDescriptionData,     size_t timeCodeDescriptionSize ); ``` |

Modified [CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416246-cmtextformatdescriptioncopyasbig)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMTextFormatDescriptionRef textFormatDescription,     CFStringRef textDescriptionFlavor,     CMBlockBufferRef *textDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMTextFormatDescriptionRef _Nonnull textFormatDescription,     CFStringRef _Nullable textDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull textDescriptionBlockBufferOut ); ``` |

Modified [CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416283-cmtextformatdescriptioncreatefro)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef textDescriptionBlockBuffer,     CFStringRef textDescriptionFlavor,     CMMediaType mediaType,     CMTextFormatDescriptionRef *textFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull textDescriptionBlockBuffer,     CFStringRef _Nullable textDescriptionFlavor,     CMMediaType mediaType,     CMTextFormatDescriptionRef  _Nullable * _Nonnull textFormatDescriptionOut ); ``` |

Modified [CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData()](https://developer.apple.com/documentation/coremedia/1416260-cmtextformatdescriptioncreatefro)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData (     CFAllocatorRef allocator,     const uint8_t *textDescriptionData,     size_t textDescriptionSize,     CFStringRef textDescriptionFlavor,     CMMediaType mediaType,     CMTextFormatDescriptionRef *textFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull textDescriptionData,     size_t textDescriptionSize,     CFStringRef _Nullable textDescriptionFlavor,     CMMediaType mediaType,     CMTextFormatDescriptionRef  _Nullable * _Nonnull textFormatDescriptionOut ); ``` |

Modified [CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416287-cmtimecodeformatdescriptioncopya)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMTimeCodeFormatDescriptionRef timeCodeFormatDescription,     CFStringRef timeCodeDescriptionFlavor,     CMBlockBufferRef *timeCodeDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMTimeCodeFormatDescriptionRef _Nonnull timeCodeFormatDescription,     CFStringRef _Nullable timeCodeDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull timeCodeDescriptionBlockBufferOut ); ``` |

Modified [CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416315-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef timeCodeDescriptionBlockBuffer,     CFStringRef timeCodeDescriptionFlavor,     CMTimeCodeFormatDescriptionRef *timeCodeFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull timeCodeDescriptionBlockBuffer,     CFStringRef _Nullable timeCodeDescriptionFlavor,     CMTimeCodeFormatDescriptionRef  _Nullable * _Nonnull timeCodeFormatDescriptionOut ); ``` |

Modified [CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData()](https://developer.apple.com/documentation/coremedia/1416256-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData (     CFAllocatorRef allocator,     const uint8_t *timeCodeDescriptionData,     size_t timeCodeDescriptionSize,     CFStringRef timeCodeDescriptionFlavor,     CMTimeCodeFormatDescriptionRef *timeCodeFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull timeCodeDescriptionData,     size_t timeCodeDescriptionSize,     CFStringRef _Nullable timeCodeDescriptionFlavor,     CMTimeCodeFormatDescriptionRef  _Nullable * _Nonnull timeCodeFormatDescriptionOut ); ``` |

Modified [CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416273-cmvideoformatdescriptioncopyasbi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMVideoFormatDescriptionRef videoFormatDescription,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef imageDescriptionFlavor,     CMBlockBufferRef *imageDescriptionBlockBufferOut ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMVideoFormatDescriptionRef _Nonnull videoFormatDescription,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef _Nullable imageDescriptionFlavor,     CMBlockBufferRef  _Nullable * _Nonnull imageDescriptionBlockBufferOut ); ``` |

Modified [CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer()](https://developer.apple.com/documentation/coremedia/1416242-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer (     CFAllocatorRef allocator,     CMBlockBufferRef imageDescriptionBlockBuffer,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef imageDescriptionFlavor,     CMVideoFormatDescriptionRef *videoFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nonnull imageDescriptionBlockBuffer,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef _Nullable imageDescriptionFlavor,     CMVideoFormatDescriptionRef  _Nullable * _Nonnull videoFormatDescriptionOut ); ``` |

Modified [CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData()](https://developer.apple.com/documentation/coremedia/1416297-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData (     CFAllocatorRef allocator,     const uint8_t *imageDescriptionData,     size_t imageDescriptionSize,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef imageDescriptionFlavor,     CMVideoFormatDescriptionRef *videoFormatDescriptionOut ); ``` |
| To | ``` OSStatus CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData (     CFAllocatorRef _Nullable allocator,     const uint8_t * _Nonnull imageDescriptionData,     size_t imageDescriptionSize,     CFStringEncoding imageDescriptionStringEncoding,     CFStringRef _Nullable imageDescriptionFlavor,     CMVideoFormatDescriptionRef  _Nullable * _Nonnull videoFormatDescriptionOut ); ``` |

#### CMMemoryPool.h

Modified [CMMemoryPoolCreate()](https://developer.apple.com/documentation/coremedia/1489395-cmmemorypoolcreate)

|  | Declaration |
| --- | --- |
| From | ``` CMMemoryPoolRef CMMemoryPoolCreate (     CFDictionaryRef options ); ``` |
| To | ``` CMMemoryPoolRef _Nonnull CMMemoryPoolCreate (     CFDictionaryRef _Nullable options ); ``` |

Modified [CMMemoryPoolFlush()](https://developer.apple.com/documentation/coremedia/1489661-cmmemorypoolflush)

|  | Declaration |
| --- | --- |
| From | ``` void CMMemoryPoolFlush (     CMMemoryPoolRef pool ); ``` |
| To | ``` void CMMemoryPoolFlush (     CMMemoryPoolRef _Nonnull pool ); ``` |

Modified [CMMemoryPoolGetAllocator()](https://developer.apple.com/documentation/coremedia/1489675-cmmemorypoolgetallocator)

|  | Declaration |
| --- | --- |
| From | ``` CFAllocatorRef CMMemoryPoolGetAllocator (     CMMemoryPoolRef pool ); ``` |
| To | ``` CFAllocatorRef _Nonnull CMMemoryPoolGetAllocator (     CMMemoryPoolRef _Nonnull pool ); ``` |

Modified [CMMemoryPoolInvalidate()](https://developer.apple.com/documentation/coremedia/1489674-cmmemorypoolinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void CMMemoryPoolInvalidate (     CMMemoryPoolRef pool ); ``` |
| To | ``` void CMMemoryPoolInvalidate (     CMMemoryPoolRef _Nonnull pool ); ``` |

#### CMMetadata.h

Added [kCMMetadataBaseDataType_JSON](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_json)Added [kCMMetadataBaseDataType_PolygonF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polygonf32)Added [kCMMetadataBaseDataType_PolylineF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polylinef32)Added [kCMMetadataIdentifier_QuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatavideoorientation)Modified [CMMetadataCreateIdentifierForKeyAndKeySpace()](https://developer.apple.com/documentation/coremedia/1474037-cmmetadatacreateidentifierforkey)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataCreateIdentifierForKeyAndKeySpace (     CFAllocatorRef allocator,     CFTypeRef key,     CFStringRef keySpace,     CFStringRef *identifierOut ); ``` |
| To | ``` OSStatus CMMetadataCreateIdentifierForKeyAndKeySpace (     CFAllocatorRef _Nullable allocator,     CFTypeRef _Nonnull key,     CFStringRef _Nonnull keySpace,     CFStringRef  _Nullable * _Nonnull identifierOut ); ``` |

Modified [CMMetadataCreateKeyFromIdentifier()](https://developer.apple.com/documentation/coremedia/1474086-cmmetadatacreatekeyfromidentifie)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataCreateKeyFromIdentifier (     CFAllocatorRef allocator,     CFStringRef identifier,     CFTypeRef *keyOut ); ``` |
| To | ``` OSStatus CMMetadataCreateKeyFromIdentifier (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull identifier,     CFTypeRef  _Nullable * _Nonnull keyOut ); ``` |

Modified [CMMetadataCreateKeyFromIdentifierAsCFData()](https://developer.apple.com/documentation/coremedia/1473974-cmmetadatacreatekeyfromidentifie)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataCreateKeyFromIdentifierAsCFData (     CFAllocatorRef allocator,     CFStringRef identifier,     CFDataRef *keyOut ); ``` |
| To | ``` OSStatus CMMetadataCreateKeyFromIdentifierAsCFData (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull identifier,     CFDataRef  _Nullable * _Nonnull keyOut ); ``` |

Modified [CMMetadataCreateKeySpaceFromIdentifier()](https://developer.apple.com/documentation/coremedia/1474002-cmmetadatacreatekeyspacefromiden)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataCreateKeySpaceFromIdentifier (     CFAllocatorRef allocator,     CFStringRef identifier,     CFStringRef *keySpaceOut ); ``` |
| To | ``` OSStatus CMMetadataCreateKeySpaceFromIdentifier (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull identifier,     CFStringRef  _Nullable * _Nonnull keySpaceOut ); ``` |

Modified [CMMetadataDataTypeRegistryDataTypeConformsToDataType()](https://developer.apple.com/documentation/coremedia/1474024-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMMetadataDataTypeRegistryDataTypeConformsToDataType (     CFStringRef dataType,     CFStringRef conformsToDataType ); ``` |
| To | ``` Boolean CMMetadataDataTypeRegistryDataTypeConformsToDataType (     CFStringRef _Nonnull dataType,     CFStringRef _Nonnull conformsToDataType ); ``` |

Modified [CMMetadataDataTypeRegistryDataTypeIsBaseDataType()](https://developer.apple.com/documentation/coremedia/1473980-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMMetadataDataTypeRegistryDataTypeIsBaseDataType (     CFStringRef dataType ); ``` |
| To | ``` Boolean CMMetadataDataTypeRegistryDataTypeIsBaseDataType (     CFStringRef _Nonnull dataType ); ``` |

Modified [CMMetadataDataTypeRegistryDataTypeIsRegistered()](https://developer.apple.com/documentation/coremedia/1473986-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMMetadataDataTypeRegistryDataTypeIsRegistered (     CFStringRef dataType ); ``` |
| To | ``` Boolean CMMetadataDataTypeRegistryDataTypeIsRegistered (     CFStringRef _Nonnull dataType ); ``` |

Modified [CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType()](https://developer.apple.com/documentation/coremedia/1474035-cmmetadatadatatyperegistrygetbas)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType (     CFStringRef dataType ); ``` |
| To | ``` CFStringRef _Nonnull CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType (     CFStringRef _Nonnull dataType ); ``` |

Modified [CMMetadataDataTypeRegistryGetBaseDataTypes()](https://developer.apple.com/documentation/coremedia/1473994-cmmetadatadatatyperegistrygetbas)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CMMetadataDataTypeRegistryGetBaseDataTypes (     void ); ``` |
| To | ``` CFArrayRef _Nullable CMMetadataDataTypeRegistryGetBaseDataTypes (     void ); ``` |

Modified [CMMetadataDataTypeRegistryGetConformingDataTypes()](https://developer.apple.com/documentation/coremedia/1473964-cmmetadatadatatyperegistrygetcon)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CMMetadataDataTypeRegistryGetConformingDataTypes (     CFStringRef dataType ); ``` |
| To | ``` CFArrayRef _Nonnull CMMetadataDataTypeRegistryGetConformingDataTypes (     CFStringRef _Nonnull dataType ); ``` |

Modified [CMMetadataDataTypeRegistryGetDataTypeDescription()](https://developer.apple.com/documentation/coremedia/1474041-cmmetadatadatatyperegistrygetdat)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CMMetadataDataTypeRegistryGetDataTypeDescription (     CFStringRef dataType ); ``` |
| To | ``` CFStringRef _Nonnull CMMetadataDataTypeRegistryGetDataTypeDescription (     CFStringRef _Nonnull dataType ); ``` |

Modified [CMMetadataDataTypeRegistryRegisterDataType()](https://developer.apple.com/documentation/coremedia/1473992-cmmetadatadatatyperegistryregist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMMetadataDataTypeRegistryRegisterDataType (     CFStringRef dataType,     CFStringRef description,     CFArrayRef conformingDataTypes ); ``` |
| To | ``` OSStatus CMMetadataDataTypeRegistryRegisterDataType (     CFStringRef _Nonnull dataType,     CFStringRef _Nonnull description,     CFArrayRef _Nonnull conformingDataTypes ); ``` |

#### CMSampleBuffer.h

Modified [CMAudioSampleBufferCreateReadyWithPacketDescriptions()](https://developer.apple.com/documentation/coremedia/1489500-cmaudiosamplebuffercreatereadywi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioSampleBufferCreateReadyWithPacketDescriptions (     CFAllocatorRef allocator,     CMBlockBufferRef dataBuffer,     CMFormatDescriptionRef formatDescription,     CMItemCount numSamples,     CMTime sbufPTS,     const AudioStreamPacketDescription *packetDescriptions,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMAudioSampleBufferCreateReadyWithPacketDescriptions (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nullable dataBuffer,     CMFormatDescriptionRef _Nonnull formatDescription,     CMItemCount numSamples,     CMTime sbufPTS,     const AudioStreamPacketDescription * _Nullable packetDescriptions,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMAudioSampleBufferCreateWithPacketDescriptions()](https://developer.apple.com/documentation/coremedia/1489466-cmaudiosamplebuffercreatewithpac)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMAudioSampleBufferCreateWithPacketDescriptions (     CFAllocatorRef allocator,     CMBlockBufferRef dataBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback makeDataReadyCallback,     void *makeDataReadyRefcon,     CMFormatDescriptionRef formatDescription,     CMItemCount numSamples,     CMTime sbufPTS,     const AudioStreamPacketDescription *packetDescriptions,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMAudioSampleBufferCreateWithPacketDescriptions (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nullable dataBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback _Nullable makeDataReadyCallback,     void * _Nullable makeDataReadyRefcon,     CMFormatDescriptionRef _Nonnull formatDescription,     CMItemCount numSamples,     CMTime sbufPTS,     const AudioStreamPacketDescription * _Nullable packetDescriptions,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferCallBlockForEachSample()](https://developer.apple.com/documentation/coremedia/1489374-cmsamplebuffercallblockforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCallBlockForEachSample (     CMSampleBufferRef sbuf,     OSStatus (^handler)(CMSampleBufferRef sampleBuffer, CMItemCount index) ); ``` |
| To | ``` OSStatus CMSampleBufferCallBlockForEachSample (     CMSampleBufferRef _Nonnull sbuf,     OSStatus (^ _Nonnullhandler)(CMSampleBufferRef _Nonnull sampleBuffer, CMItemCount index) ); ``` |

Modified [CMSampleBufferCallForEachSample()](https://developer.apple.com/documentation/coremedia/1489563-cmsamplebuffercallforeachsample)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCallForEachSample (     CMSampleBufferRef sbuf,     OSStatus (*callback)(CMSampleBufferRef sampleBuffer, CMItemCount index, void *refcon),     void *refcon ); ``` |
| To | ``` OSStatus CMSampleBufferCallForEachSample (     CMSampleBufferRef _Nonnull sbuf,     OSStatus (* _Nonnullcallback)(CMSampleBufferRef _Nonnull sampleBuffer, CMItemCount index, void * _Nullable refcon),     void * _Nullable refcon ); ``` |

Modified [CMSampleBufferCopyPCMDataIntoAudioBufferList()](https://developer.apple.com/documentation/coremedia/1489200-cmsamplebuffercopypcmdataintoaud)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCopyPCMDataIntoAudioBufferList (     CMSampleBufferRef sbuf,     int32_t frameOffset,     int32_t numFrames,     AudioBufferList *bufferList ); ``` |
| To | ``` OSStatus CMSampleBufferCopyPCMDataIntoAudioBufferList (     CMSampleBufferRef _Nonnull sbuf,     int32_t frameOffset,     int32_t numFrames,     AudioBufferList * _Nonnull bufferList ); ``` |

Modified [CMSampleBufferCopySampleBufferForRange()](https://developer.apple.com/documentation/coremedia/1489461-cmsamplebuffercopysamplebufferfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCopySampleBufferForRange (     CFAllocatorRef allocator,     CMSampleBufferRef sbuf,     CFRange sampleRange,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMSampleBufferCopySampleBufferForRange (     CFAllocatorRef _Nullable allocator,     CMSampleBufferRef _Nonnull sbuf,     CFRange sampleRange,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferCreate()](https://developer.apple.com/documentation/coremedia/1489723-cmsamplebuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreate (     CFAllocatorRef allocator,     CMBlockBufferRef dataBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback makeDataReadyCallback,     void *makeDataReadyRefcon,     CMFormatDescriptionRef formatDescription,     CMItemCount numSamples,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo *sampleTimingArray,     CMItemCount numSampleSizeEntries,     const size_t *sampleSizeArray,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreate (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nullable dataBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback _Nullable makeDataReadyCallback,     void * _Nullable makeDataReadyRefcon,     CMFormatDescriptionRef _Nullable formatDescription,     CMItemCount numSamples,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo * _Nullable sampleTimingArray,     CMItemCount numSampleSizeEntries,     const size_t * _Nullable sampleSizeArray,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferCreateCopy()](https://developer.apple.com/documentation/coremedia/1489543-cmsamplebuffercreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreateCopy (     CFAllocatorRef allocator,     CMSampleBufferRef sbuf,     CMSampleBufferRef *sbufCopyOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreateCopy (     CFAllocatorRef _Nullable allocator,     CMSampleBufferRef _Nonnull sbuf,     CMSampleBufferRef  _Nullable * _Nonnull sbufCopyOut ); ``` |

Modified [CMSampleBufferCreateCopyWithNewTiming()](https://developer.apple.com/documentation/coremedia/1489645-cmsamplebuffercreatecopywithnewt)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreateCopyWithNewTiming (     CFAllocatorRef allocator,     CMSampleBufferRef originalSBuf,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo *sampleTimingArray,     CMSampleBufferRef *sBufCopyOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreateCopyWithNewTiming (     CFAllocatorRef _Nullable allocator,     CMSampleBufferRef _Nonnull originalSBuf,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo * _Nullable sampleTimingArray,     CMSampleBufferRef  _Nullable * _Nonnull sBufCopyOut ); ``` |

Modified [CMSampleBufferCreateForImageBuffer()](https://developer.apple.com/documentation/coremedia/1489414-cmsamplebuffercreateforimagebuff)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreateForImageBuffer (     CFAllocatorRef allocator,     CVImageBufferRef imageBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback makeDataReadyCallback,     void *makeDataReadyRefcon,     CMVideoFormatDescriptionRef formatDescription,     const CMSampleTimingInfo *sampleTiming,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreateForImageBuffer (     CFAllocatorRef _Nullable allocator,     CVImageBufferRef _Nonnull imageBuffer,     Boolean dataReady,     CMSampleBufferMakeDataReadyCallback _Nullable makeDataReadyCallback,     void * _Nullable makeDataReadyRefcon,     CMVideoFormatDescriptionRef _Nonnull formatDescription,     const CMSampleTimingInfo * _Nonnull sampleTiming,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferCreateReady()](https://developer.apple.com/documentation/coremedia/1489513-cmsamplebuffercreateready)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreateReady (     CFAllocatorRef allocator,     CMBlockBufferRef dataBuffer,     CMFormatDescriptionRef formatDescription,     CMItemCount numSamples,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo *sampleTimingArray,     CMItemCount numSampleSizeEntries,     const size_t *sampleSizeArray,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreateReady (     CFAllocatorRef _Nullable allocator,     CMBlockBufferRef _Nullable dataBuffer,     CMFormatDescriptionRef _Nullable formatDescription,     CMItemCount numSamples,     CMItemCount numSampleTimingEntries,     const CMSampleTimingInfo * _Nullable sampleTimingArray,     CMItemCount numSampleSizeEntries,     const size_t * _Nullable sampleSizeArray,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferCreateReadyWithImageBuffer()](https://developer.apple.com/documentation/coremedia/1489745-cmsamplebuffercreatereadywithima)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferCreateReadyWithImageBuffer (     CFAllocatorRef allocator,     CVImageBufferRef imageBuffer,     CMVideoFormatDescriptionRef formatDescription,     const CMSampleTimingInfo *sampleTiming,     CMSampleBufferRef *sBufOut ); ``` |
| To | ``` OSStatus CMSampleBufferCreateReadyWithImageBuffer (     CFAllocatorRef _Nullable allocator,     CVImageBufferRef _Nonnull imageBuffer,     CMVideoFormatDescriptionRef _Nonnull formatDescription,     const CMSampleTimingInfo * _Nonnull sampleTiming,     CMSampleBufferRef  _Nullable * _Nonnull sBufOut ); ``` |

Modified [CMSampleBufferDataIsReady()](https://developer.apple.com/documentation/coremedia/1489694-cmsamplebufferdataisready)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMSampleBufferDataIsReady (     CMSampleBufferRef sbuf ); ``` |
| To | ``` Boolean CMSampleBufferDataIsReady (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer()](https://developer.apple.com/documentation/coremedia/1489191-cmsamplebuffergetaudiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer (     CMSampleBufferRef sbuf,     size_t *bufferListSizeNeededOut,     AudioBufferList *bufferListOut,     size_t bufferListSize,     CFAllocatorRef bbufStructAllocator,     CFAllocatorRef bbufMemoryAllocator,     uint32_t flags,     CMBlockBufferRef *blockBufferOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer (     CMSampleBufferRef _Nonnull sbuf,     size_t * _Nullable bufferListSizeNeededOut,     AudioBufferList * _Nullable bufferListOut,     size_t bufferListSize,     CFAllocatorRef _Nullable bbufStructAllocator,     CFAllocatorRef _Nullable bbufMemoryAllocator,     uint32_t flags,     CMBlockBufferRef  _Nullable * _Nullable blockBufferOut ); ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptions()](https://developer.apple.com/documentation/coremedia/1489190-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetAudioStreamPacketDescriptions (     CMSampleBufferRef sbuf,     size_t packetDescriptionsSize,     AudioStreamPacketDescription *packetDescriptionsOut,     size_t *packetDescriptionsSizeNeededOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetAudioStreamPacketDescriptions (     CMSampleBufferRef _Nonnull sbuf,     size_t packetDescriptionsSize,     AudioStreamPacketDescription * _Nullable packetDescriptionsOut,     size_t * _Nullable packetDescriptionsSizeNeededOut ); ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptionsPtr()](https://developer.apple.com/documentation/coremedia/1489564-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetAudioStreamPacketDescriptionsPtr (     CMSampleBufferRef sbuf,     const AudioStreamPacketDescription **packetDescriptionsPtrOut,     size_t *packetDescriptionsSizeOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetAudioStreamPacketDescriptionsPtr (     CMSampleBufferRef _Nonnull sbuf,     const AudioStreamPacketDescription * _Nullable * _Nullable packetDescriptionsPtrOut,     size_t * _Nullable packetDescriptionsSizeOut ); ``` |

Modified [CMSampleBufferGetDataBuffer()](https://developer.apple.com/documentation/coremedia/1489629-cmsamplebuffergetdatabuffer)

|  | Declaration |
| --- | --- |
| From | ``` CMBlockBufferRef CMSampleBufferGetDataBuffer (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMBlockBufferRef _Nullable CMSampleBufferGetDataBuffer (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetDecodeTimeStamp()](https://developer.apple.com/documentation/coremedia/1489404-cmsamplebuffergetdecodetimestamp)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetDecodeTimeStamp (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetDecodeTimeStamp (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetDuration()](https://developer.apple.com/documentation/coremedia/1489562-cmsamplebuffergetduration)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetDuration (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetDuration (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetFormatDescription()](https://developer.apple.com/documentation/coremedia/1489185-cmsamplebuffergetformatdescripti)

|  | Declaration |
| --- | --- |
| From | ``` CMFormatDescriptionRef CMSampleBufferGetFormatDescription (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMFormatDescriptionRef _Nullable CMSampleBufferGetFormatDescription (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetImageBuffer()](https://developer.apple.com/documentation/coremedia/1489236-cmsamplebuffergetimagebuffer)

|  | Declaration |
| --- | --- |
| From | ``` CVImageBufferRef CMSampleBufferGetImageBuffer (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CVImageBufferRef _Nullable CMSampleBufferGetImageBuffer (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetNumSamples()](https://developer.apple.com/documentation/coremedia/1489399-cmsamplebuffergetnumsamples)

|  | Declaration |
| --- | --- |
| From | ``` CMItemCount CMSampleBufferGetNumSamples (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMItemCount CMSampleBufferGetNumSamples (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetOutputDecodeTimeStamp()](https://developer.apple.com/documentation/coremedia/1489742-cmsamplebuffergetoutputdecodetim)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetOutputDecodeTimeStamp (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetOutputDecodeTimeStamp (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetOutputDuration()](https://developer.apple.com/documentation/coremedia/1489237-cmsamplebuffergetoutputduration)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetOutputDuration (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetOutputDuration (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetOutputPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489655-cmsamplebuffergetoutputpresentat)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetOutputPresentationTimeStamp (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetOutputPresentationTimeStamp (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetOutputSampleTimingInfoArray()](https://developer.apple.com/documentation/coremedia/1489380-cmsamplebuffergetoutputsampletim)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetOutputSampleTimingInfoArray (     CMSampleBufferRef sbuf,     CMItemCount timingArrayEntries,     CMSampleTimingInfo *timingArrayOut,     CMItemCount *timingArrayEntriesNeededOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetOutputSampleTimingInfoArray (     CMSampleBufferRef _Nonnull sbuf,     CMItemCount timingArrayEntries,     CMSampleTimingInfo * _Nullable timingArrayOut,     CMItemCount * _Nullable timingArrayEntriesNeededOut ); ``` |

Modified [CMSampleBufferGetPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489252-cmsamplebuffergetpresentationtim)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSampleBufferGetPresentationTimeStamp (     CMSampleBufferRef sbuf ); ``` |
| To | ``` CMTime CMSampleBufferGetPresentationTimeStamp (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferGetSampleAttachmentsArray()](https://developer.apple.com/documentation/coremedia/1489189-cmsamplebuffergetsampleattachmen)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CMSampleBufferGetSampleAttachmentsArray (     CMSampleBufferRef sbuf,     Boolean createIfNecessary ); ``` |
| To | ``` CFArrayRef _Nullable CMSampleBufferGetSampleAttachmentsArray (     CMSampleBufferRef _Nonnull sbuf,     Boolean createIfNecessary ); ``` |

Modified [CMSampleBufferGetSampleSize()](https://developer.apple.com/documentation/coremedia/1489210-cmsamplebuffergetsamplesize)

|  | Declaration |
| --- | --- |
| From | ``` size_t CMSampleBufferGetSampleSize (     CMSampleBufferRef sbuf,     CMItemIndex sampleIndex ); ``` |
| To | ``` size_t CMSampleBufferGetSampleSize (     CMSampleBufferRef _Nonnull sbuf,     CMItemIndex sampleIndex ); ``` |

Modified [CMSampleBufferGetSampleSizeArray()](https://developer.apple.com/documentation/coremedia/1489295-cmsamplebuffergetsamplesizearray)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetSampleSizeArray (     CMSampleBufferRef sbuf,     CMItemCount sizeArrayEntries,     size_t *sizeArrayOut,     CMItemCount *sizeArrayEntriesNeededOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetSampleSizeArray (     CMSampleBufferRef _Nonnull sbuf,     CMItemCount sizeArrayEntries,     size_t * _Nullable sizeArrayOut,     CMItemCount * _Nullable sizeArrayEntriesNeededOut ); ``` |

Modified [CMSampleBufferGetSampleTimingInfo()](https://developer.apple.com/documentation/coremedia/1489670-cmsamplebuffergetsampletiminginf)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetSampleTimingInfo (     CMSampleBufferRef sbuf,     CMItemIndex sampleIndex,     CMSampleTimingInfo *timingInfoOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetSampleTimingInfo (     CMSampleBufferRef _Nonnull sbuf,     CMItemIndex sampleIndex,     CMSampleTimingInfo * _Nonnull timingInfoOut ); ``` |

Modified [CMSampleBufferGetSampleTimingInfoArray()](https://developer.apple.com/documentation/coremedia/1489652-cmsamplebuffergetsampletiminginf)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferGetSampleTimingInfoArray (     CMSampleBufferRef sbuf,     CMItemCount timingArrayEntries,     CMSampleTimingInfo *timingArrayOut,     CMItemCount *timingArrayEntriesNeededOut ); ``` |
| To | ``` OSStatus CMSampleBufferGetSampleTimingInfoArray (     CMSampleBufferRef _Nonnull sbuf,     CMItemCount timingArrayEntries,     CMSampleTimingInfo * _Nullable timingArrayOut,     CMItemCount * _Nullable timingArrayEntriesNeededOut ); ``` |

Modified [CMSampleBufferGetTotalSampleSize()](https://developer.apple.com/documentation/coremedia/1489481-cmsamplebuffergettotalsamplesize)

|  | Declaration |
| --- | --- |
| From | ``` size_t CMSampleBufferGetTotalSampleSize (     CMSampleBufferRef sbuf ); ``` |
| To | ``` size_t CMSampleBufferGetTotalSampleSize (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferHasDataFailed()](https://developer.apple.com/documentation/coremedia/1489503-cmsamplebufferhasdatafailed)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMSampleBufferHasDataFailed (     CMSampleBufferRef sbuf,     OSStatus *statusOut ); ``` |
| To | ``` Boolean CMSampleBufferHasDataFailed (     CMSampleBufferRef _Nonnull sbuf,     OSStatus * _Nonnull statusOut ); ``` |

Modified [CMSampleBufferInvalidate()](https://developer.apple.com/documentation/coremedia/1489640-cmsamplebufferinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferInvalidate (     CMSampleBufferRef sbuf ); ``` |
| To | ``` OSStatus CMSampleBufferInvalidate (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferIsValid()](https://developer.apple.com/documentation/coremedia/1489151-cmsamplebufferisvalid)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMSampleBufferIsValid (     CMSampleBufferRef sbuf ); ``` |
| To | ``` Boolean CMSampleBufferIsValid (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferMakeDataReady()](https://developer.apple.com/documentation/coremedia/1489314-cmsamplebuffermakedataready)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferMakeDataReady (     CMSampleBufferRef sbuf ); ``` |
| To | ``` OSStatus CMSampleBufferMakeDataReady (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferSetDataBuffer()](https://developer.apple.com/documentation/coremedia/1489381-cmsamplebuffersetdatabuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetDataBuffer (     CMSampleBufferRef sbuf,     CMBlockBufferRef dataBuffer ); ``` |
| To | ``` OSStatus CMSampleBufferSetDataBuffer (     CMSampleBufferRef _Nonnull sbuf,     CMBlockBufferRef _Nonnull dataBuffer ); ``` |

Modified [CMSampleBufferSetDataBufferFromAudioBufferList()](https://developer.apple.com/documentation/coremedia/1489725-cmsamplebuffersetdatabufferfroma)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetDataBufferFromAudioBufferList (     CMSampleBufferRef sbuf,     CFAllocatorRef bbufStructAllocator,     CFAllocatorRef bbufMemoryAllocator,     uint32_t flags,     const AudioBufferList *bufferList ); ``` |
| To | ``` OSStatus CMSampleBufferSetDataBufferFromAudioBufferList (     CMSampleBufferRef _Nonnull sbuf,     CFAllocatorRef _Nullable bbufStructAllocator,     CFAllocatorRef _Nullable bbufMemoryAllocator,     uint32_t flags,     const AudioBufferList * _Nonnull bufferList ); ``` |

Modified [CMSampleBufferSetDataFailed()](https://developer.apple.com/documentation/coremedia/1489697-cmsamplebuffersetdatafailed)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetDataFailed (     CMSampleBufferRef sbuf,     OSStatus status ); ``` |
| To | ``` OSStatus CMSampleBufferSetDataFailed (     CMSampleBufferRef _Nonnull sbuf,     OSStatus status ); ``` |

Modified [CMSampleBufferSetDataReady()](https://developer.apple.com/documentation/coremedia/1489482-cmsamplebuffersetdataready)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetDataReady (     CMSampleBufferRef sbuf ); ``` |
| To | ``` OSStatus CMSampleBufferSetDataReady (     CMSampleBufferRef _Nonnull sbuf ); ``` |

Modified [CMSampleBufferSetInvalidateCallback()](https://developer.apple.com/documentation/coremedia/1489773-cmsamplebuffersetinvalidatecallb)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetInvalidateCallback (     CMSampleBufferRef sbuf,     CMSampleBufferInvalidateCallback invalidateCallback,     uint64_t invalidateRefCon ); ``` |
| To | ``` OSStatus CMSampleBufferSetInvalidateCallback (     CMSampleBufferRef _Nonnull sbuf,     CMSampleBufferInvalidateCallback _Nonnull invalidateCallback,     uint64_t invalidateRefCon ); ``` |

Modified [CMSampleBufferSetInvalidateHandler()](https://developer.apple.com/documentation/coremedia/1489256-cmsamplebuffersetinvalidatehandl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetInvalidateHandler (     CMSampleBufferRef sbuf,     CMSampleBufferInvalidateHandler invalidateHandler ); ``` |
| To | ``` OSStatus CMSampleBufferSetInvalidateHandler (     CMSampleBufferRef _Nonnull sbuf,     CMSampleBufferInvalidateHandler _Nonnull invalidateHandler ); ``` |

Modified [CMSampleBufferSetOutputPresentationTimeStamp()](https://developer.apple.com/documentation/coremedia/1489442-cmsamplebuffersetoutputpresentat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferSetOutputPresentationTimeStamp (     CMSampleBufferRef sbuf,     CMTime outputPresentationTimeStamp ); ``` |
| To | ``` OSStatus CMSampleBufferSetOutputPresentationTimeStamp (     CMSampleBufferRef _Nonnull sbuf,     CMTime outputPresentationTimeStamp ); ``` |

Modified [CMSampleBufferTrackDataReadiness()](https://developer.apple.com/documentation/coremedia/1489667-cmsamplebuffertrackdatareadiness)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSampleBufferTrackDataReadiness (     CMSampleBufferRef sbuf,     CMSampleBufferRef sbufToTrack ); ``` |
| To | ``` OSStatus CMSampleBufferTrackDataReadiness (     CMSampleBufferRef _Nonnull sbuf,     CMSampleBufferRef _Nonnull sbufToTrack ); ``` |

#### CMSimpleQueue.h

Modified [CMSimpleQueueCreate()](https://developer.apple.com/documentation/coremedia/1489641-cmsimplequeuecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSimpleQueueCreate (     CFAllocatorRef allocator,     int32_t capacity,     CMSimpleQueueRef *queueOut ); ``` |
| To | ``` OSStatus CMSimpleQueueCreate (     CFAllocatorRef _Nullable allocator,     int32_t capacity,     CMSimpleQueueRef  _Nullable * _Nonnull queueOut ); ``` |

Modified [CMSimpleQueueDequeue()](https://developer.apple.com/documentation/coremedia/1489820-cmsimplequeuedequeue)

|  | Declaration |
| --- | --- |
| From | ``` const void * CMSimpleQueueDequeue (     CMSimpleQueueRef queue ); ``` |
| To | ``` const void * _Nullable CMSimpleQueueDequeue (     CMSimpleQueueRef _Nonnull queue ); ``` |

Modified [CMSimpleQueueEnqueue()](https://developer.apple.com/documentation/coremedia/1489315-cmsimplequeueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSimpleQueueEnqueue (     CMSimpleQueueRef queue,     const void *element ); ``` |
| To | ``` OSStatus CMSimpleQueueEnqueue (     CMSimpleQueueRef _Nonnull queue,     const void * _Nonnull element ); ``` |

Modified [CMSimpleQueueGetCapacity()](https://developer.apple.com/documentation/coremedia/1489168-cmsimplequeuegetcapacity)

|  | Declaration |
| --- | --- |
| From | ``` int32_t CMSimpleQueueGetCapacity (     CMSimpleQueueRef queue ); ``` |
| To | ``` int32_t CMSimpleQueueGetCapacity (     CMSimpleQueueRef _Nonnull queue ); ``` |

Modified [CMSimpleQueueGetCount()](https://developer.apple.com/documentation/coremedia/1489223-cmsimplequeuegetcount)

|  | Declaration |
| --- | --- |
| From | ``` int32_t CMSimpleQueueGetCount (     CMSimpleQueueRef queue ); ``` |
| To | ``` int32_t CMSimpleQueueGetCount (     CMSimpleQueueRef _Nonnull queue ); ``` |

Modified [CMSimpleQueueGetHead()](https://developer.apple.com/documentation/coremedia/1489410-cmsimplequeuegethead)

|  | Declaration |
| --- | --- |
| From | ``` const void * CMSimpleQueueGetHead (     CMSimpleQueueRef queue ); ``` |
| To | ``` const void * _Nullable CMSimpleQueueGetHead (     CMSimpleQueueRef _Nonnull queue ); ``` |

Modified [CMSimpleQueueReset()](https://developer.apple.com/documentation/coremedia/1489224-cmsimplequeuereset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSimpleQueueReset (     CMSimpleQueueRef queue ); ``` |
| To | ``` OSStatus CMSimpleQueueReset (     CMSimpleQueueRef _Nonnull queue ); ``` |

#### CMSync.h

Added [CMTimebaseCopyMaster()](https://developer.apple.com/documentation/coremedia/1489679-cmtimebasecopymaster)Added [CMTimebaseCopyMasterClock()](https://developer.apple.com/documentation/coremedia/1489238-cmtimebasecopymasterclock)Added [CMTimebaseCopyMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489341-cmtimebasecopymastertimebase)Added [CMTimebaseCopyUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489262-cmtimebasecopyultimatemastercloc)Modified [CMClockGetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489299-cmclockgetanchortime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMClockGetAnchorTime (     CMClockRef clock,     CMTime *outClockTime,     CMTime *outReferenceClockTime ); ``` |
| To | ``` OSStatus CMClockGetAnchorTime (     CMClockRef _Nonnull clock,     CMTime * _Nonnull outClockTime,     CMTime * _Nonnull outReferenceClockTime ); ``` |

Modified [CMClockGetHostTimeClock()](https://developer.apple.com/documentation/coremedia/1489402-cmclockgethosttimeclock)

|  | Declaration |
| --- | --- |
| From | ``` CMClockRef CMClockGetHostTimeClock (     void ); ``` |
| To | ``` CMClockRef _Nonnull CMClockGetHostTimeClock (     void ); ``` |

Modified [CMClockGetTime()](https://developer.apple.com/documentation/coremedia/1489382-cmclockgettime)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMClockGetTime (     CMClockRef clock ); ``` |
| To | ``` CMTime CMClockGetTime (     CMClockRef _Nonnull clock ); ``` |

Modified [CMClockInvalidate()](https://developer.apple.com/documentation/coremedia/1489202-cmclockinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void CMClockInvalidate (     CMClockRef clock ); ``` |
| To | ``` void CMClockInvalidate (     CMClockRef _Nonnull clock ); ``` |

Modified [CMClockMightDrift()](https://developer.apple.com/documentation/coremedia/1489494-cmclockmightdrift)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMClockMightDrift (     CMClockRef clock,     CMClockRef otherClock ); ``` |
| To | ``` Boolean CMClockMightDrift (     CMClockRef _Nonnull clock,     CMClockRef _Nonnull otherClock ); ``` |

Modified [CMSyncConvertTime()](https://developer.apple.com/documentation/coremedia/1489632-cmsyncconverttime)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSyncConvertTime (     CMTime time,     CMClockOrTimebaseRef fromClockOrTimebase,     CMClockOrTimebaseRef toClockOrTimebase ); ``` |
| To | ``` CMTime CMSyncConvertTime (     CMTime time,     CMClockOrTimebaseRef _Nonnull fromClockOrTimebase,     CMClockOrTimebaseRef _Nonnull toClockOrTimebase ); ``` |

Modified [CMSyncGetRelativeRate()](https://developer.apple.com/documentation/coremedia/1489528-cmsyncgetrelativerate)

|  | Declaration |
| --- | --- |
| From | ``` Float64 CMSyncGetRelativeRate (     CMClockOrTimebaseRef ofClockOrTimebase,     CMClockOrTimebaseRef relativeToClockOrTimebase ); ``` |
| To | ``` Float64 CMSyncGetRelativeRate (     CMClockOrTimebaseRef _Nonnull ofClockOrTimebase,     CMClockOrTimebaseRef _Nonnull relativeToClockOrTimebase ); ``` |

Modified [CMSyncGetRelativeRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489570-cmsyncgetrelativerateandanchorti)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSyncGetRelativeRateAndAnchorTime (     CMClockOrTimebaseRef ofClockOrTimebase,     CMClockOrTimebaseRef relativeToClockOrTimebase,     Float64 *outRelativeRate,     CMTime *outOfClockOrTimebaseAnchorTime,     CMTime *outRelativeToClockOrTimebaseAnchorTime ); ``` |
| To | ``` OSStatus CMSyncGetRelativeRateAndAnchorTime (     CMClockOrTimebaseRef _Nonnull ofClockOrTimebase,     CMClockOrTimebaseRef _Nonnull relativeToClockOrTimebase,     Float64 * _Nonnull outRelativeRate,     CMTime * _Nonnull outOfClockOrTimebaseAnchorTime,     CMTime * _Nonnull outRelativeToClockOrTimebaseAnchorTime ); ``` |

Modified [CMSyncGetTime()](https://developer.apple.com/documentation/coremedia/1489233-cmsyncgettime)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMSyncGetTime (     CMClockOrTimebaseRef clockOrTimebase ); ``` |
| To | ``` CMTime CMSyncGetTime (     CMClockOrTimebaseRef _Nonnull clockOrTimebase ); ``` |

Modified [CMSyncMightDrift()](https://developer.apple.com/documentation/coremedia/1489610-cmsyncmightdrift)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CMSyncMightDrift (     CMClockOrTimebaseRef clockOrTimebase1,     CMClockOrTimebaseRef clockOrTimebase2 ); ``` |
| To | ``` Boolean CMSyncMightDrift (     CMClockOrTimebaseRef _Nonnull clockOrTimebase1,     CMClockOrTimebaseRef _Nonnull clockOrTimebase2 ); ``` |

Modified [CMTimebaseAddTimer()](https://developer.apple.com/documentation/coremedia/1489654-cmtimebaseaddtimer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseAddTimer (     CMTimebaseRef timebase,     CFRunLoopTimerRef timer,     CFRunLoopRef runloop ); ``` |
| To | ``` OSStatus CMTimebaseAddTimer (     CMTimebaseRef _Nonnull timebase,     CFRunLoopTimerRef _Nonnull timer,     CFRunLoopRef _Nonnull runloop ); ``` |

Modified [CMTimebaseAddTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489429-cmtimebaseaddtimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseAddTimerDispatchSource (     CMTimebaseRef timebase,     dispatch_source_t timerSource ); ``` |
| To | ``` OSStatus CMTimebaseAddTimerDispatchSource (     CMTimebaseRef _Nonnull timebase,     dispatch_source_t _Nonnull timerSource ); ``` |

Modified [CMTimebaseCreateWithMasterClock()](https://developer.apple.com/documentation/coremedia/1489367-cmtimebasecreatewithmasterclock)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseCreateWithMasterClock (     CFAllocatorRef allocator,     CMClockRef masterClock,     CMTimebaseRef *timebaseOut ); ``` |
| To | ``` OSStatus CMTimebaseCreateWithMasterClock (     CFAllocatorRef _Nullable allocator,     CMClockRef _Nonnull masterClock,     CMTimebaseRef  _Nullable * _Nonnull timebaseOut ); ``` |

Modified [CMTimebaseCreateWithMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489132-cmtimebasecreatewithmastertimeba)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseCreateWithMasterTimebase (     CFAllocatorRef allocator,     CMTimebaseRef masterTimebase,     CMTimebaseRef *timebaseOut ); ``` |
| To | ``` OSStatus CMTimebaseCreateWithMasterTimebase (     CFAllocatorRef _Nullable allocator,     CMTimebaseRef _Nonnull masterTimebase,     CMTimebaseRef  _Nullable * _Nonnull timebaseOut ); ``` |

Modified [CMTimebaseGetEffectiveRate()](https://developer.apple.com/documentation/coremedia/1489313-cmtimebasegeteffectiverate)

|  | Declaration |
| --- | --- |
| From | ``` Float64 CMTimebaseGetEffectiveRate (     CMTimebaseRef timebase ); ``` |
| To | ``` Float64 CMTimebaseGetEffectiveRate (     CMTimebaseRef _Nonnull timebase ); ``` |

Modified [CMTimebaseGetMaster()](https://developer.apple.com/documentation/coremedia/1489764-cmtimebasegetmaster)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CMClockOrTimebaseRef CMTimebaseGetMaster (     CMTimebaseRef timebase ); ``` | -- |
| To | ``` CMClockOrTimebaseRef _Nullable CMTimebaseGetMaster (     CMTimebaseRef _Nonnull timebase ); ``` | OS X 10.11 |

Modified [CMTimebaseGetMasterClock()](https://developer.apple.com/documentation/coremedia/1489691-cmtimebasegetmasterclock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CMClockRef CMTimebaseGetMasterClock (     CMTimebaseRef timebase ); ``` | -- |
| To | ``` CMClockRef _Nullable CMTimebaseGetMasterClock (     CMTimebaseRef _Nonnull timebase ); ``` | OS X 10.11 |

Modified [CMTimebaseGetMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489484-cmtimebasegetmastertimebase)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CMTimebaseRef CMTimebaseGetMasterTimebase (     CMTimebaseRef timebase ); ``` | -- |
| To | ``` CMTimebaseRef _Nullable CMTimebaseGetMasterTimebase (     CMTimebaseRef _Nonnull timebase ); ``` | OS X 10.11 |

Modified [CMTimebaseGetRate()](https://developer.apple.com/documentation/coremedia/1489302-cmtimebasegetrate)

|  | Declaration |
| --- | --- |
| From | ``` Float64 CMTimebaseGetRate (     CMTimebaseRef timebase ); ``` |
| To | ``` Float64 CMTimebaseGetRate (     CMTimebaseRef _Nonnull timebase ); ``` |

Modified [CMTimebaseGetTime()](https://developer.apple.com/documentation/coremedia/1489812-cmtimebasegettime)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMTimebaseGetTime (     CMTimebaseRef timebase ); ``` |
| To | ``` CMTime CMTimebaseGetTime (     CMTimebaseRef _Nonnull timebase ); ``` |

Modified [CMTimebaseGetTimeAndRate()](https://developer.apple.com/documentation/coremedia/1489415-cmtimebasegettimeandrate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseGetTimeAndRate (     CMTimebaseRef timebase,     CMTime *outTime,     Float64 *outRate ); ``` |
| To | ``` OSStatus CMTimebaseGetTimeAndRate (     CMTimebaseRef _Nonnull timebase,     CMTime * _Nonnull outTime,     Float64 * _Nonnull outRate ); ``` |

Modified [CMTimebaseGetTimeWithTimeScale()](https://developer.apple.com/documentation/coremedia/1489700-cmtimebasegettimewithtimescale)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMTimebaseGetTimeWithTimeScale (     CMTimebaseRef timebase,     CMTimeScale timescale,     CMTimeRoundingMethod method ); ``` |
| To | ``` CMTime CMTimebaseGetTimeWithTimeScale (     CMTimebaseRef _Nonnull timebase,     CMTimeScale timescale,     CMTimeRoundingMethod method ); ``` |

Modified [CMTimebaseGetUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489671-cmtimebasegetultimatemasterclock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CMClockRef CMTimebaseGetUltimateMasterClock (     CMTimebaseRef timebase ); ``` | -- |
| To | ``` CMClockRef _Nullable CMTimebaseGetUltimateMasterClock (     CMTimebaseRef _Nonnull timebase ); ``` | OS X 10.11 |

Modified [CMTimebaseNotificationBarrier()](https://developer.apple.com/documentation/coremedia/1489171-cmtimebasenotificationbarrier)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseNotificationBarrier (     CMTimebaseRef timebase ); ``` |
| To | ``` OSStatus CMTimebaseNotificationBarrier (     CMTimebaseRef _Nonnull timebase ); ``` |

Modified [CMTimebaseRemoveTimer()](https://developer.apple.com/documentation/coremedia/1489746-cmtimebaseremovetimer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseRemoveTimer (     CMTimebaseRef timebase,     CFRunLoopTimerRef timer ); ``` |
| To | ``` OSStatus CMTimebaseRemoveTimer (     CMTimebaseRef _Nonnull timebase,     CFRunLoopTimerRef _Nonnull timer ); ``` |

Modified [CMTimebaseRemoveTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489198-cmtimebaseremovetimerdispatchsou)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseRemoveTimerDispatchSource (     CMTimebaseRef timebase,     dispatch_source_t timerSource ); ``` |
| To | ``` OSStatus CMTimebaseRemoveTimerDispatchSource (     CMTimebaseRef _Nonnull timebase,     dispatch_source_t _Nonnull timerSource ); ``` |

Modified [CMTimebaseSetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489504-cmtimebasesetanchortime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetAnchorTime (     CMTimebaseRef timebase,     CMTime timebaseTime,     CMTime immediateMasterTime ); ``` |
| To | ``` OSStatus CMTimebaseSetAnchorTime (     CMTimebaseRef _Nonnull timebase,     CMTime timebaseTime,     CMTime immediateMasterTime ); ``` |

Modified [CMTimebaseSetRate()](https://developer.apple.com/documentation/coremedia/1489590-cmtimebasesetrate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetRate (     CMTimebaseRef timebase,     Float64 rate ); ``` |
| To | ``` OSStatus CMTimebaseSetRate (     CMTimebaseRef _Nonnull timebase,     Float64 rate ); ``` |

Modified [CMTimebaseSetRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489332-cmtimebasesetrateandanchortime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetRateAndAnchorTime (     CMTimebaseRef timebase,     Float64 rate,     CMTime timebaseTime,     CMTime immediateMasterTime ); ``` |
| To | ``` OSStatus CMTimebaseSetRateAndAnchorTime (     CMTimebaseRef _Nonnull timebase,     Float64 rate,     CMTime timebaseTime,     CMTime immediateMasterTime ); ``` |

Modified [CMTimebaseSetTime()](https://developer.apple.com/documentation/coremedia/1489372-cmtimebasesettime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetTime (     CMTimebaseRef timebase,     CMTime time ); ``` |
| To | ``` OSStatus CMTimebaseSetTime (     CMTimebaseRef _Nonnull timebase,     CMTime time ); ``` |

Modified [CMTimebaseSetTimerDispatchSourceNextFireTime()](https://developer.apple.com/documentation/coremedia/1489489-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetTimerDispatchSourceNextFireTime (     CMTimebaseRef timebase,     dispatch_source_t timerSource,     CMTime fireTime,     uint32_t flags ); ``` |
| To | ``` OSStatus CMTimebaseSetTimerDispatchSourceNextFireTime (     CMTimebaseRef _Nonnull timebase,     dispatch_source_t _Nonnull timerSource,     CMTime fireTime,     uint32_t flags ); ``` |

Modified [CMTimebaseSetTimerDispatchSourceToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489552-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetTimerDispatchSourceToFireImmediately (     CMTimebaseRef timebase,     dispatch_source_t timerSource ); ``` |
| To | ``` OSStatus CMTimebaseSetTimerDispatchSourceToFireImmediately (     CMTimebaseRef _Nonnull timebase,     dispatch_source_t _Nonnull timerSource ); ``` |

Modified [CMTimebaseSetTimerNextFireTime()](https://developer.apple.com/documentation/coremedia/1489692-cmtimebasesettimernextfiretime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetTimerNextFireTime (     CMTimebaseRef timebase,     CFRunLoopTimerRef timer,     CMTime fireTime,     uint32_t flags ); ``` |
| To | ``` OSStatus CMTimebaseSetTimerNextFireTime (     CMTimebaseRef _Nonnull timebase,     CFRunLoopTimerRef _Nonnull timer,     CMTime fireTime,     uint32_t flags ); ``` |

Modified [CMTimebaseSetTimerToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489213-cmtimebasesettimertofireimmediat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMTimebaseSetTimerToFireImmediately (     CMTimebaseRef timebase,     CFRunLoopTimerRef timer ); ``` |
| To | ``` OSStatus CMTimebaseSetTimerToFireImmediately (     CMTimebaseRef _Nonnull timebase,     CFRunLoopTimerRef _Nonnull timer ); ``` |

#### CMTime.h

Modified [CMTimeCopyAsDictionary()](https://developer.apple.com/documentation/coremedia/1400845-cmtimecopyasdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CMTimeCopyAsDictionary (     CMTime time,     CFAllocatorRef allocator ); ``` |
| To | ``` CFDictionaryRef _Nullable CMTimeCopyAsDictionary (     CMTime time,     CFAllocatorRef _Nullable allocator ); ``` |

Modified [CMTimeCopyDescription()](https://developer.apple.com/documentation/coremedia/1400791-cmtimecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CMTimeCopyDescription (     CFAllocatorRef allocator,     CMTime time ); ``` |
| To | ``` CFStringRef _Nullable CMTimeCopyDescription (     CFAllocatorRef _Nullable allocator,     CMTime time ); ``` |

Modified [CMTimeMakeFromDictionary()](https://developer.apple.com/documentation/coremedia/1400819-cmtimemakefromdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CMTime CMTimeMakeFromDictionary (     CFDictionaryRef dict ); ``` |
| To | ``` CMTime CMTimeMakeFromDictionary (     CFDictionaryRef _Nullable dict ); ``` |

#### CMTimeRange.h

Added #def CMTIMEMAPPING_IS_EMPTYAdded #def CMTIMEMAPPING_IS_INVALIDAdded #def CMTIMEMAPPING_IS_VALIDAdded [CMTimeMappingCopyAsDictionary()](https://developer.apple.com/documentation/coremedia/1462805-cmtimemappingcopyasdictionary)Added [CMTimeMappingCopyDescription()](https://developer.apple.com/documentation/coremedia/1462811-cmtimemappingcopydescription)Added [CMTimeMappingMake()](https://developer.apple.com/documentation/coremedia/1462793-cmtimemappingmake)Added [CMTimeMappingMakeEmpty()](https://developer.apple.com/documentation/coremedia/1462828-cmtimemappingmakeempty)Added [CMTimeMappingMakeFromDictionary()](https://developer.apple.com/documentation/coremedia/1462796-cmtimemappingmakefromdictionary)Added [CMTimeMappingShow()](https://developer.apple.com/documentation/coremedia/1462835-cmtimemappingshow)Added [kCMTimeMappingInvalid](https://developer.apple.com/documentation/coremedia/cmtimemapping/1462795-invalid)Added [kCMTimeMappingSourceKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingsourcekey)Added [kCMTimeMappingTargetKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingtargetkey)Modified [CMTimeRangeCopyAsDictionary()](https://developer.apple.com/documentation/coremedia/1462781-cmtimerangecopyasdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CMTimeRangeCopyAsDictionary (     CMTimeRange range,     CFAllocatorRef allocator ); ``` |
| To | ``` CFDictionaryRef _Nullable CMTimeRangeCopyAsDictionary (     CMTimeRange range,     CFAllocatorRef _Nullable allocator ); ``` |

Modified [CMTimeRangeCopyDescription()](https://developer.apple.com/documentation/coremedia/1462823-cmtimerangecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CMTimeRangeCopyDescription (     CFAllocatorRef allocator,     CMTimeRange range ); ``` |
| To | ``` CFStringRef _Nullable CMTimeRangeCopyDescription (     CFAllocatorRef _Nullable allocator,     CMTimeRange range ); ``` |

Modified [CMTimeRangeMakeFromDictionary()](https://developer.apple.com/documentation/coremedia/1462777-cmtimerangemakefromdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CMTimeRange CMTimeRangeMakeFromDictionary (     CFDictionaryRef dict ); ``` |
| To | ``` CMTimeRange CMTimeRangeMakeFromDictionary (     CFDictionaryRef _Nonnull dict ); ``` |

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
