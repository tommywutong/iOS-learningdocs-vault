---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/AudioToolbox.html
archived_at: '2026-07-18T02:56:07.478271Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# AudioToolbox Changes

## AudioToolbox

Modified AUGraphAddNode(AUGraph, UnsafePointer<AudioComponentDescription>, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphAddRenderNotify(AUGraph, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphClearConnections(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphClose(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphConnectNodeInput(AUGraph, AUNode, UInt32, AUNode, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphCountNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphDisconnectNodeInput(AUGraph, AUNode, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetIndNode(AUGraph, UInt32, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetInteractionInfo(AUGraph, UInt32, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetMaxCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetNodeCount(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphGetNumberOfInteractions(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphInitialize(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphIsInitialized(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphIsOpen(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphIsRunning(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphNodeInfo(AUGraph, AUNode, UnsafeMutablePointer<AudioComponentDescription>, UnsafeMutablePointer<AudioUnit>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphOpen(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphRemoveNode(AUGraph, AUNode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphRemoveRenderNotify(AUGraph, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphSetNodeInputCallback(AUGraph, AUNode, UInt32, UnsafePointer<AURenderCallbackStruct>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphStart(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphStop(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphUninitialize(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AUGraphUpdate(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioConverterComplexInputDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterComplexInputDataProc = CFunctionPointer<((AudioConverter!, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterComplexInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioConverterConvertBuffer(AudioConverterRef, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverter!, _ inInputDataSize: UInt32, _ inInputData: UnsafePointer<Void>, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataSize: UInt32, _ inInputData: UnsafePointer<Void>, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterConvertComplexBuffer(AudioConverterRef, UInt32, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterConvertComplexBuffer(_ inAudioConverter: AudioConverter!, _ inNumberPCMFrames: UInt32, _ inInputData: UnsafePointer<AudioBufferList>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterConvertComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inNumberPCMFrames: UInt32, _ inInputData: UnsafePointer<AudioBufferList>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | iOS 5.0 |

Modified AudioConverterDispose(AudioConverterRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterDispose(_ inAudioConverter: AudioConverter!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterDispose(_ inAudioConverter: AudioConverterRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterFillComplexBuffer(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverter!, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutablePointer<Void>, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutablePointer<Void>, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterGetPropertyInfo(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterInputDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterInputDataProc = CFunctionPointer<((AudioConverter!, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<Unmanaged<AudioConverter>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<Unmanaged<AudioConverter>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterRef = AudioConverter ``` |
| To | ``` typealias AudioConverterRef = COpaquePointer ``` |

Modified AudioConverterReset(AudioConverterRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterReset(_ inAudioConverter: AudioConverter!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterReset(_ inAudioConverter: AudioConverterRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | iOS 2.0 |

Modified AudioFileClose(AudioFileID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileCreateWithURL(CFURL!, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetGlobalInfo(AudioFilePropertyID, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetGlobalInfoSize(AudioFilePropertyID, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetPropertyInfo(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileInitializeWithCallbacks(UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileOpenURL(CFURL!, Int8, AudioFileTypeID, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileOpenWithCallbacks(UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileOptimize(AudioFileID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileReadBytes(AudioFileID, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileReadPacketData(AudioFileID, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

Modified AudioFileReadPackets(AudioFileID, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 8.0 |

Modified AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamClose(AudioFileStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamGetPropertyInfo(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamOpen(UnsafeMutablePointer<Void>, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamParseBytes(AudioFileStreamID, UInt32, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamSeek(AudioFileStreamID, Int64, UnsafeMutablePointer<Int64>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileStreamSetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileWriteBytes(AudioFileID, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFileWritePackets(AudioFileID, Boolean, UInt32, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFormatGetProperty(AudioFormatPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioFormatGetPropertyInfo(AudioFormatPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueAllocateBuffer(AudioQueueRef, UInt32, UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueue!, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueue!, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueue!, _ outTimeline: UnsafeMutablePointer<Unmanaged<AudioQueueTimeline>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueueRef, _ outTimeline: UnsafeMutablePointer<AudioQueueTimelineRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceGetCurrentTime(_ inAQ: AudioQueue!, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueDeviceGetCurrentTime(_ inAQ: AudioQueueRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceGetNearestStartTime(_ inAQ: AudioQueue!, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueDeviceGetNearestStartTime(_ inAQ: AudioQueueRef, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceTranslateTime(_ inAQ: AudioQueue!, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueDeviceTranslateTime(_ inAQ: AudioQueueRef, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueDispose(AudioQueueRef, Boolean) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDispose(_ inAQ: AudioQueue!, _ inImmediate: Boolean) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueDispose(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDisposeTimeline(_ inAQ: AudioQueue!, _ inTimeline: AudioQueueTimeline!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueDisposeTimeline(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueEnqueueBuffer(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>, _ inStartTime: UnsafePointer<AudioTimeStamp>, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>, _ inStartTime: UnsafePointer<AudioTimeStamp>, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueFlush(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueFlush(_ inAQ: AudioQueue!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueFlush(_ inAQ: AudioQueueRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueFreeBuffer(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueFreeBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueue!, _ inTimeline: AudioQueueTimeline!, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueGetParameter(AudioQueueRef, AudioQueueParameterID, UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetParameter(_ inAQ: AudioQueue!, _ inParamID: AudioQueueParameterID, _ outValue: UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueGetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ outValue: UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetProperty(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueGetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetPropertySize(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueGetPropertySize(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueInputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueInputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueue!, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |
| To | ``` typealias AudioQueueInputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |

Modified AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, UInt32, UnsafeMutablePointer<AudioQueueRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<Unmanaged<AudioQueue>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, UInt32, UnsafeMutablePointer<AudioQueueRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<Unmanaged<AudioQueue>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueOfflineRender(AudioQueueRef, UnsafePointer<AudioTimeStamp>, AudioQueueBufferRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueOfflineRender(_ inAQ: AudioQueue!, _ inTimestamp: UnsafePointer<AudioTimeStamp>, _ ioBuffer: AudioQueueBufferRef, _ inNumberFrames: UInt32) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueOfflineRender(_ inAQ: AudioQueueRef, _ inTimestamp: UnsafePointer<AudioTimeStamp>, _ ioBuffer: AudioQueueBufferRef, _ inNumberFrames: UInt32) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueue!, AudioQueueBufferRef) -> Void)> ``` |
| To | ``` typealias AudioQueueOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef) -> Void)> ``` |

Modified AudioQueuePause(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueuePause(_ inAQ: AudioQueue!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueuePause(_ inAQ: AudioQueueRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueuePrime(_ inAQ: AudioQueue!, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueuePrime(_ inAQ: AudioQueueRef, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueProcessingTapCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueProcessingTap!, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void)> ``` |
| To | ``` typealias AudioQueueProcessingTapCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void)> ``` |

Modified AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapDispose(_ inAQTap: AudioQueueProcessingTap!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueProcessingTapDispose(_ inAQTap: AudioQueueProcessingTapRef) -> OSStatus ``` | iOS 6.0 |

Modified AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapGetQueueTime(_ inAQTap: AudioQueueProcessingTap!, _ outQueueSampleTime: UnsafeMutablePointer<Float64>, _ outQueueFrameCount: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueProcessingTapGetQueueTime(_ inAQTap: AudioQueueProcessingTapRef, _ outQueueSampleTime: UnsafeMutablePointer<Float64>, _ outQueueFrameCount: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | iOS 6.0 |

Modified AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTap!, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<UInt32>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTapRef, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<UInt32>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | iOS 6.0 |

Modified AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueue!, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: UInt32, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<Unmanaged<AudioQueueProcessingTap>?>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: UInt32, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus ``` | iOS 6.0 |

Modified AudioQueueProcessingTapRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapRef = AudioQueueProcessingTap ``` |
| To | ``` typealias AudioQueueProcessingTapRef = COpaquePointer ``` |

Modified AudioQueuePropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueuePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueue!, AudioQueuePropertyID) -> Void)> ``` |
| To | ``` typealias AudioQueuePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueuePropertyID) -> Void)> ``` |

Modified AudioQueueRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueRef = AudioQueue ``` |
| To | ``` typealias AudioQueueRef = COpaquePointer ``` |

Modified AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueReset(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueReset(_ inAQ: AudioQueue!) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueReset(_ inAQ: AudioQueueRef) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueSetOfflineRenderFormat(AudioQueueRef, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueue!, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inLayout: UnsafePointer<AudioChannelLayout>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueueRef, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inLayout: UnsafePointer<AudioChannelLayout>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueSetParameter(AudioQueueRef, AudioQueueParameterID, AudioQueueParameterValue) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetParameter(_ inAQ: AudioQueue!, _ inParamID: AudioQueueParameterID, _ inValue: AudioQueueParameterValue) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueSetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ inValue: AudioQueueParameterValue) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetProperty(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueSetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueStart(_ inAQ: AudioQueue!, _ inStartTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueStart(_ inAQ: AudioQueueRef, _ inStartTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueStop(AudioQueueRef, Boolean) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueStop(_ inAQ: AudioQueue!, _ inImmediate: Boolean) -> OSStatus ``` | iOS 8.0 |
| To | ``` func AudioQueueStop(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` | iOS 2.0 |

Modified AudioQueueTimelineRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueTimelineRef = AudioQueueTimeline ``` |
| To | ``` typealias AudioQueueTimelineRef = COpaquePointer ``` |

Modified AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop!, CFString!, AudioServicesSystemSoundCompletionProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesCreateSystemSoundID(CFURL!, UnsafeMutablePointer<SystemSoundID>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesPlayAlertSound(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesPlaySystemSound(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesRemoveSystemSoundCompletion(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CAShow(UnsafeMutablePointer<Void>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CAShowFile(UnsafeMutablePointer<Void>, UnsafeMutablePointer<FILE>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CopyInstrumentInfoFromSoundBank(CFURL!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CopyNameFromSoundBank(CFURL!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified DisposeAUGraph(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified DisposeMusicEventIterator(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified DisposeMusicPlayer(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified DisposeMusicSequence(MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ExtAudioFileCreateWithURL(CFURL!, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>, UInt32, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileOpenURL(CFURL!, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileWrapAudioFileID(AudioFileID, Boolean, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.1 |

Modified MusicEventIteratorDeleteEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorGetEventInfo(MusicEventIterator, UnsafeMutablePointer<MusicTimeStamp>, UnsafeMutablePointer<MusicEventType>, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorHasCurrentEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorHasNextEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorHasPreviousEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorNextEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorPreviousEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorSeek(MusicEventIterator, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorSetEventInfo(MusicEventIterator, MusicEventType, UnsafePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicEventIteratorSetEventTime(MusicEventIterator, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerGetHostTimeForBeats(MusicPlayer, MusicTimeStamp, UnsafeMutablePointer<UInt64>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerGetTime(MusicPlayer, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerIsPlaying(MusicPlayer, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerPreroll(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerSetPlayRateScalar(MusicPlayer, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerSetSequence(MusicPlayer, MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerSetTime(MusicPlayer, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerStart(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicPlayerStop(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceBarBeatTimeToBeats(MusicSequence, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceBeatsToBarBeatTime(MusicSequence, MusicTimeStamp, UInt32, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceDisposeTrack(MusicSequence, MusicTrack) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceFileCreate(MusicSequence, CFURL!, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceFileCreateData(MusicSequence, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceFileLoad(MusicSequence, CFURL!, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceFileLoadData(MusicSequence, CFData!, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetAUGraph(MusicSequence, UnsafeMutablePointer<AUGraph>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetBeatsForSeconds(MusicSequence, Float64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetIndTrack(MusicSequence, UInt32, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetTempoTrack(MusicSequence, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetTrackCount(MusicSequence, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceGetTrackIndex(MusicSequence, MusicTrack, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceNewTrack(MusicSequence, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceReverse(MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceSetAUGraph(MusicSequence, AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceSetMIDIEndpoint(MusicSequence, MIDIEndpoint!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceSetSequenceType(MusicSequence, MusicSequenceType) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicSequenceSetUserCallback(MusicSequence, MusicSequenceUserCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackClear(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackCopyInsert(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackCut(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackGetDestNode(MusicTrack, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackGetProperty(MusicTrack, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackGetSequence(MusicTrack, UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackMerge(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackMoveEvents(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewAUPresetEvent(MusicTrack, MusicTimeStamp, UnsafePointer<AUPresetEvent>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewExtendedNoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewExtendedTempoEvent(MusicTrack, MusicTimeStamp, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewMIDIChannelEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIChannelMessage>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewMIDINoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDINoteMessage>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewMIDIRawDataEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIRawData>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewMetaEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIMetaEvent>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewParameterEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ParameterEvent>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackNewUserEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackSetDestMIDIEndpoint(MusicTrack, MIDIEndpoint!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackSetDestNode(MusicTrack, AUNode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MusicTrackSetProperty(MusicTrack, UInt32, UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NewAUGraph(UnsafeMutablePointer<AUGraph>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified NewMusicEventIterator(MusicTrack, UnsafeMutablePointer<MusicEventIterator>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NewMusicPlayer(UnsafeMutablePointer<MusicPlayer>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified NewMusicSequence(UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
