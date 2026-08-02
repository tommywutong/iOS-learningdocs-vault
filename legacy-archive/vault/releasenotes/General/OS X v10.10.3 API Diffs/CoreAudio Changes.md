---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CoreAudio.html
archived_at: '2026-07-18T02:52:09.786059Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CoreAudio Changes

## CoreAudio

Added AudioBuffer.init()Added AudioBuffer.init(_: UnsafeMutableBufferPointer<T>, numberOfChannels: Int)Added AudioBuffer.init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutablePointer<Void>)Added AudioBufferList.init()Added AudioBufferList.allocate(Int) -> UnsafeMutableAudioBufferListPointer [static]Added AudioBufferList.init(mNumberBuffers: UInt32, mBuffers:(AudioBuffer))Added AudioBufferList.sizeInBytes(Int) -> Int [static]Added AudioChannelDescription.init()Added AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: UInt32, mCoordinates:(Float32, Float32, Float32))Added AudioChannelLayout.init()Added AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: UInt32, mNumberChannelDescriptions: UInt32, mChannelDescriptions:(AudioChannelDescription))Added AudioClassDescription.init()Added AudioClassDescription.init(mType: OSType, mSubType: OSType, mManufacturer: OSType)Added AudioHardwareIOProcStreamUsage.init()Added AudioHardwareIOProcStreamUsage.init(mIOProc: UnsafeMutablePointer<Void>, mNumberStreams: UInt32, mStreamIsOn:(UInt32))Added AudioObjectPropertyAddress.init()Added AudioObjectPropertyAddress.init(mSelector: AudioObjectPropertySelector, mScope: AudioObjectPropertyScope, mElement: AudioObjectPropertyElement)Added AudioStreamBasicDescription.init()Added AudioStreamBasicDescription.init(mSampleRate: Float64, mFormatID: AudioFormatID, mFormatFlags: AudioFormatFlags, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mBytesPerFrame: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32, mReserved: UInt32)Added AudioStreamPacketDescription.init()Added AudioStreamPacketDescription.init(mStartOffset: Int64, mVariableFramesInPacket: UInt32, mDataByteSize: UInt32)Added AudioStreamRangedDescription.init()Added AudioStreamRangedDescription.init(mFormat: AudioStreamBasicDescription, mSampleRateRange: AudioValueRange)Added AudioTimeStamp.init()Added AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: UInt32, mReserved: UInt32)Added AudioValueRange.init()Added AudioValueRange.init(mMinimum: Float64, mMaximum: Float64)Added AudioValueTranslation.init()Added AudioValueTranslation.init(mInputData: UnsafeMutablePointer<Void>, mInputDataSize: UInt32, mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize: UInt32)Added SMPTETime.init()Added SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: UInt32, mFlags: UInt32, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Added UnsafeBufferPointer.init(_: AudioBuffer)Added UnsafeMutableAudioBufferListPointer [struct]Added UnsafeMutableAudioBufferListPointer.init(_: UnsafeMutablePointer<AudioBufferList>)Added UnsafeMutableAudioBufferListPointer.countAdded UnsafeMutableAudioBufferListPointer.endIndexAdded UnsafeMutableAudioBufferListPointer.generate() -> IndexingGenerator<UnsafeMutableAudioBufferListPointer>Added UnsafeMutableAudioBufferListPointer.startIndexAdded UnsafeMutableAudioBufferListPointer.unsafeMutablePointerAdded UnsafeMutableAudioBufferListPointer.unsafePointerAdded UnsafeMutableBufferPointer.init(_: AudioBuffer)Modified AudioBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafePointer<()> } ``` |
| To | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } ``` |

Modified AudioBuffer.mData

|  | Declaration |
| --- | --- |
| From | ``` var mData: UnsafePointer<()> ``` |
| To | ``` var mData: UnsafeMutablePointer<Void> ``` |

Modified AudioBufferList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBufferList {     var mNumberBuffers: UInt32     var mBuffers: (AudioBuffer) } ``` |
| To | ``` struct AudioBufferList {     var mNumberBuffers: UInt32     var mBuffers: (AudioBuffer)     init()     init(mNumberBuffers mNumberBuffers: UInt32, mBuffers mBuffers: (AudioBuffer)) } ``` |

Modified AudioChannelDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioChannelDescription {     var mChannelLabel: AudioChannelLabel     var mChannelFlags: UInt32     var mCoordinates: (Float32, Float32, Float32) } ``` |
| To | ``` struct AudioChannelDescription {     var mChannelLabel: AudioChannelLabel     var mChannelFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     init()     init(mChannelLabel mChannelLabel: AudioChannelLabel, mChannelFlags mChannelFlags: UInt32, mCoordinates mCoordinates: (Float32, Float32, Float32)) } ``` |

Modified AudioChannelLayout [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioChannelLayout {     var mChannelLayoutTag: AudioChannelLayoutTag     var mChannelBitmap: UInt32     var mNumberChannelDescriptions: UInt32     var mChannelDescriptions: (AudioChannelDescription) } ``` |
| To | ``` struct AudioChannelLayout {     var mChannelLayoutTag: AudioChannelLayoutTag     var mChannelBitmap: UInt32     var mNumberChannelDescriptions: UInt32     var mChannelDescriptions: (AudioChannelDescription)     init()     init(mChannelLayoutTag mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap mChannelBitmap: UInt32, mNumberChannelDescriptions mNumberChannelDescriptions: UInt32, mChannelDescriptions mChannelDescriptions: (AudioChannelDescription)) } ``` |

Modified AudioClassDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioClassDescription {     var mType: OSType     var mSubType: OSType     var mManufacturer: OSType } ``` |
| To | ``` struct AudioClassDescription {     var mType: OSType     var mSubType: OSType     var mManufacturer: OSType     init()     init(mType mType: OSType, mSubType mSubType: OSType, mManufacturer mManufacturer: OSType) } ``` |

Modified AudioHardwareIOProcStreamUsage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafePointer<()>     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32) } ``` |
| To | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafeMutablePointer<Void>     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32)     init()     init(mIOProc mIOProc: UnsafeMutablePointer<Void>, mNumberStreams mNumberStreams: UInt32, mStreamIsOn mStreamIsOn: (UInt32)) } ``` |

Modified AudioHardwareIOProcStreamUsage.mIOProc

|  | Declaration |
| --- | --- |
| From | ``` var mIOProc: UnsafePointer<()> ``` |
| To | ``` var mIOProc: UnsafeMutablePointer<Void> ``` |

Modified AudioObjectPropertyAddress [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioObjectPropertyAddress {     var mSelector: AudioObjectPropertySelector     var mScope: AudioObjectPropertyScope     var mElement: AudioObjectPropertyElement } ``` |
| To | ``` struct AudioObjectPropertyAddress {     var mSelector: AudioObjectPropertySelector     var mScope: AudioObjectPropertyScope     var mElement: AudioObjectPropertyElement     init()     init(mSelector mSelector: AudioObjectPropertySelector, mScope mScope: AudioObjectPropertyScope, mElement mElement: AudioObjectPropertyElement) } ``` |

Modified AudioStreamBasicDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioStreamBasicDescription {     var mSampleRate: Float64     var mFormatID: AudioFormatID     var mFormatFlags: AudioFormatFlags     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mBytesPerFrame: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32     var mReserved: UInt32 } ``` |
| To | ``` struct AudioStreamBasicDescription {     var mSampleRate: Float64     var mFormatID: AudioFormatID     var mFormatFlags: AudioFormatFlags     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mBytesPerFrame: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32     var mReserved: UInt32     init()     init(mSampleRate mSampleRate: Float64, mFormatID mFormatID: AudioFormatID, mFormatFlags mFormatFlags: AudioFormatFlags, mBytesPerPacket mBytesPerPacket: UInt32, mFramesPerPacket mFramesPerPacket: UInt32, mBytesPerFrame mBytesPerFrame: UInt32, mChannelsPerFrame mChannelsPerFrame: UInt32, mBitsPerChannel mBitsPerChannel: UInt32, mReserved mReserved: UInt32) } ``` |

Modified AudioStreamPacketDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioStreamPacketDescription {     var mStartOffset: Int64     var mVariableFramesInPacket: UInt32     var mDataByteSize: UInt32 } ``` |
| To | ``` struct AudioStreamPacketDescription {     var mStartOffset: Int64     var mVariableFramesInPacket: UInt32     var mDataByteSize: UInt32     init()     init(mStartOffset mStartOffset: Int64, mVariableFramesInPacket mVariableFramesInPacket: UInt32, mDataByteSize mDataByteSize: UInt32) } ``` |

Modified AudioStreamRangedDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioStreamRangedDescription {     var mFormat: AudioStreamBasicDescription     var mSampleRateRange: AudioValueRange } ``` |
| To | ``` struct AudioStreamRangedDescription {     var mFormat: AudioStreamBasicDescription     var mSampleRateRange: AudioValueRange     init()     init(mFormat mFormat: AudioStreamBasicDescription, mSampleRateRange mSampleRateRange: AudioValueRange) } ``` |

Modified AudioTimeStamp [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioTimeStamp {     var mSampleTime: Float64     var mHostTime: UInt64     var mRateScalar: Float64     var mWordClockTime: UInt64     var mSMPTETime: SMPTETime     var mFlags: UInt32     var mReserved: UInt32 } ``` |
| To | ``` struct AudioTimeStamp {     var mSampleTime: Float64     var mHostTime: UInt64     var mRateScalar: Float64     var mWordClockTime: UInt64     var mSMPTETime: SMPTETime     var mFlags: UInt32     var mReserved: UInt32     init()     init(mSampleTime mSampleTime: Float64, mHostTime mHostTime: UInt64, mRateScalar mRateScalar: Float64, mWordClockTime mWordClockTime: UInt64, mSMPTETime mSMPTETime: SMPTETime, mFlags mFlags: UInt32, mReserved mReserved: UInt32) } ``` |

Modified AudioValueRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioValueRange {     var mMinimum: Float64     var mMaximum: Float64 } ``` |
| To | ``` struct AudioValueRange {     var mMinimum: Float64     var mMaximum: Float64     init()     init(mMinimum mMinimum: Float64, mMaximum mMaximum: Float64) } ``` |

Modified AudioValueTranslation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioValueTranslation {     var mInputData: UnsafePointer<()>     var mInputDataSize: UInt32     var mOutputData: UnsafePointer<()>     var mOutputDataSize: UInt32 } ``` |
| To | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32     init()     init(mInputData mInputData: UnsafeMutablePointer<Void>, mInputDataSize mInputDataSize: UInt32, mOutputData mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize mOutputDataSize: UInt32) } ``` |

Modified AudioValueTranslation.mInputData

|  | Declaration |
| --- | --- |
| From | ``` var mInputData: UnsafePointer<()> ``` |
| To | ``` var mInputData: UnsafeMutablePointer<Void> ``` |

Modified AudioValueTranslation.mOutputData

|  | Declaration |
| --- | --- |
| From | ``` var mOutputData: UnsafePointer<()> ``` |
| To | ``` var mOutputData: UnsafeMutablePointer<Void> ``` |

Modified SMPTETime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: UInt32     var mFlags: UInt32     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16 } ``` |
| To | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: UInt32     var mFlags: UInt32     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16     init()     init(mSubframes mSubframes: Int16, mSubframeDivisor mSubframeDivisor: Int16, mCounter mCounter: UInt32, mType mType: UInt32, mFlags mFlags: UInt32, mHours mHours: Int16, mMinutes mMinutes: Int16, mSeconds mSeconds: Int16, mFrames mFrames: Int16) } ``` |

Modified AudioConvertHostTimeToNanos(UInt64) -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioConvertNanosToHostTime(UInt64) -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioDeviceCreateIOProcID(AudioObjectID, AudioDeviceIOProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<AudioDeviceIOProcID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafePointer<()>, _ outIOProcID: UnsafePointer<AudioDeviceIOProcID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutablePointer<Void>, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID>) -> OSStatus ``` | OS X 10.5 |

Modified AudioDeviceCreateIOProcIDWithBlock(UnsafeMutablePointer<AudioDeviceIOProcID>, AudioObjectID, dispatch_queue_t!, AudioDeviceIOBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafePointer<AudioDeviceIOProcID>, _ inDevice: AudioObjectID, _ inDispatchQueue: dispatch_queue_t!, _ inIOBlock: AudioDeviceIOBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID>, _ inDevice: AudioObjectID, _ inDispatchQueue: dispatch_queue_t!, _ inIOBlock: AudioDeviceIOBlock!) -> OSStatus ``` | OS X 10.7 |

Modified AudioDeviceDestroyIOProcID(AudioObjectID, AudioDeviceIOProcID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioDeviceGetCurrentTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceGetCurrentTime(_ inDevice: AudioObjectID, _ outTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceGetCurrentTime(_ inDevice: AudioObjectID, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.0 |

Modified AudioDeviceGetNearestStartTime(AudioObjectID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceGetNearestStartTime(_ inDevice: AudioObjectID, _ ioRequestedStartTime: UnsafePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceGetNearestStartTime(_ inDevice: AudioObjectID, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.3 |

Modified AudioDeviceIOBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOBlock = (ConstUnsafePointer<AudioTimeStamp>, ConstUnsafePointer<AudioBufferList>, ConstUnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, ConstUnsafePointer<AudioTimeStamp>) -> Void ``` |
| To | ``` typealias AudioDeviceIOBlock = (UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>) -> Void ``` |

Modified AudioDeviceIOProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOProc = CFunctionPointer<((AudioObjectID, ConstUnsafePointer<AudioTimeStamp>, ConstUnsafePointer<AudioBufferList>, ConstUnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, ConstUnsafePointer<AudioTimeStamp>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioDeviceIOProc = CFunctionPointer<((AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioDevicePropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDevicePropertyListenerProc = CFunctionPointer<((AudioDeviceID, UInt32, Boolean, AudioDevicePropertyID, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioDevicePropertyListenerProc = CFunctionPointer<((AudioDeviceID, UInt32, Boolean, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioDeviceStart(AudioObjectID, AudioDeviceIOProcID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioDeviceStartAtTime(AudioObjectID, AudioDeviceIOProcID, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID, _ ioRequestedStartTime: UnsafePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.3 |

Modified AudioDeviceStop(AudioObjectID, AudioDeviceIOProcID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioDeviceTranslateTime(AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioDeviceTranslateTime(_ inDevice: AudioObjectID, _ inTime: ConstUnsafePointer<AudioTimeStamp>, _ outTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioDeviceTranslateTime(_ inDevice: AudioObjectID, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.0 |

Modified AudioGetCurrentHostTime() -> UInt64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioGetHostClockFrequency() -> Float64

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioGetHostClockMinimumTimeDelta() -> UInt32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AudioHardwareCreateAggregateDevice(CFDictionary!, UnsafeMutablePointer<AudioObjectID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareCreateAggregateDevice(_ inDescription: CFDictionary!, _ outDeviceID: UnsafePointer<AudioObjectID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareCreateAggregateDevice(_ inDescription: CFDictionary!, _ outDeviceID: UnsafeMutablePointer<AudioObjectID>) -> OSStatus ``` | OS X 10.9 |

Modified AudioHardwareDestroyAggregateDevice(AudioObjectID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified AudioHardwarePropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioHardwarePropertyListenerProc = CFunctionPointer<((AudioHardwarePropertyID, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioHardwarePropertyListenerProc = CFunctionPointer<((AudioHardwarePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioHardwareUnload() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified AudioObjectAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectAddPropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t!, AudioObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.7 |

Modified AudioObjectGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ ioDataSize: UnsafePointer<UInt32>, _ outData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ outDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectHasProperty(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>) -> Boolean ``` | OS X 10.10 |
| To | ``` func AudioObjectHasProperty(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>) -> Boolean ``` | OS X 10.4 |

Modified AudioObjectIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectPropertyListenerBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioObjectPropertyListenerBlock = (UInt32, ConstUnsafePointer<AudioObjectPropertyAddress>) -> Void ``` |
| To | ``` typealias AudioObjectPropertyListenerBlock = (UInt32, UnsafePointer<AudioObjectPropertyAddress>) -> Void ``` |

Modified AudioObjectPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioObjectPropertyListenerProc = CFunctionPointer<((AudioObjectID, UInt32, ConstUnsafePointer<AudioObjectPropertyAddress>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioObjectPropertyListenerProc = CFunctionPointer<((AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioObjectRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectRemovePropertyListenerBlock(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, dispatch_queue_t!, AudioObjectPropertyListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` | OS X 10.7 |

Modified AudioObjectSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioObjectSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ inDataSize: UInt32, _ inData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioObjectSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ inDataSize: UInt32, _ inData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioObjectShow(AudioObjectID)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified AudioStreamPropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioStreamPropertyListenerProc = CFunctionPointer<((AudioStreamID, UInt32, AudioDevicePropertyID, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioStreamPropertyListenerProc = CFunctionPointer<((AudioStreamID, UInt32, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

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
