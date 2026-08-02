---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreAudio.html
archived_at: '2026-07-18T02:56:22.050517Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreAudio Changes

## CoreAudio

Added AudioBuffer.init()Added AudioBuffer.init(_: UnsafeMutableBufferPointer<T>, numberOfChannels: Int)Added AudioBuffer.init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutablePointer<Void>)Added AudioBufferList.init()Added AudioBufferList.allocate(Int) -> UnsafeMutableAudioBufferListPointer [static]Added AudioBufferList.init(mNumberBuffers: UInt32, mBuffers:(AudioBuffer))Added AudioBufferList.sizeInBytes(Int) -> Int [static]Added AudioChannelDescription.init()Added AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: UInt32, mCoordinates:(Float32, Float32, Float32))Added AudioChannelLayout.init()Added AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: UInt32, mNumberChannelDescriptions: UInt32, mChannelDescriptions:(AudioChannelDescription))Added AudioClassDescription.init()Added AudioClassDescription.init(mType: OSType, mSubType: OSType, mManufacturer: OSType)Added AudioStreamBasicDescription.init()Added AudioStreamBasicDescription.init(mSampleRate: Float64, mFormatID: AudioFormatID, mFormatFlags: AudioFormatFlags, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mBytesPerFrame: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32, mReserved: UInt32)Added AudioStreamPacketDescription.init()Added AudioStreamPacketDescription.init(mStartOffset: Int64, mVariableFramesInPacket: UInt32, mDataByteSize: UInt32)Added AudioTimeStamp.init()Added AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: UInt32, mReserved: UInt32)Added AudioValueRange.init()Added AudioValueRange.init(mMinimum: Float64, mMaximum: Float64)Added AudioValueTranslation.init()Added AudioValueTranslation.init(mInputData: UnsafeMutablePointer<Void>, mInputDataSize: UInt32, mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize: UInt32)Added SMPTETime.init()Added SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: UInt32, mFlags: UInt32, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Added UnsafeBufferPointer.init(_: AudioBuffer)Added UnsafeMutableAudioBufferListPointer [struct]Added UnsafeMutableAudioBufferListPointer.init(_: UnsafeMutablePointer<AudioBufferList>)Added UnsafeMutableAudioBufferListPointer.countAdded UnsafeMutableAudioBufferListPointer.endIndexAdded UnsafeMutableAudioBufferListPointer.generate() -> IndexingGenerator<UnsafeMutableAudioBufferListPointer>Added UnsafeMutableAudioBufferListPointer.startIndexAdded UnsafeMutableAudioBufferListPointer.unsafeMutablePointerAdded UnsafeMutableAudioBufferListPointer.unsafePointerAdded UnsafeMutableBufferPointer.init(_: AudioBuffer)Modified AudioBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } ``` |

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
| From | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32 } ``` |
| To | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32     init()     init(mInputData mInputData: UnsafeMutablePointer<Void>, mInputDataSize mInputDataSize: UInt32, mOutputData mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize mOutputDataSize: UInt32) } ``` |

Modified SMPTETime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: UInt32     var mFlags: UInt32     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16 } ``` |
| To | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: UInt32     var mFlags: UInt32     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16     init()     init(mSubframes mSubframes: Int16, mSubframeDivisor mSubframeDivisor: Int16, mCounter mCounter: UInt32, mType mType: UInt32, mFlags mFlags: UInt32, mHours mHours: Int16, mMinutes mMinutes: Int16, mSeconds mSeconds: Int16, mFrames mFrames: Int16) } ``` |

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
