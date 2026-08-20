---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/AudioToolbox.html
archived_at: '2026-07-18T02:56:21.754892Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# AudioToolbox Changes

## AudioToolbox

Added AUNodeInteraction.init()Added AUNodeRenderCallback.init()Added AUNodeRenderCallback.init(destNode: AUNode, destInputNumber: AudioUnitElement, cback: AURenderCallbackStruct)Added AUPresetEvent.init()Added AUPresetEvent.init(scope: AudioUnitScope, element: AudioUnitElement, preset: Unmanaged<CFPropertyList>!)Added AudioBalanceFade.init()Added AudioBalanceFade.init(mLeftRightBalance: Float32, mBackFrontFade: Float32, mType: UInt32, mChannelLayout: UnsafePointer<AudioChannelLayout>)Added AudioBytePacketTranslation.init()Added AudioBytePacketTranslation.init(mByte: Int64, mPacket: Int64, mByteOffsetInPacket: UInt32, mFlags: UInt32)Added AudioConverterPrimeInfo.init()Added AudioConverterPrimeInfo.init(leadingFrames: UInt32, trailingFrames: UInt32)Added AudioFileMarker.init()Added AudioFileMarker.init(mFramePosition: Float64, mName: Unmanaged<CFString>!, mMarkerID: Int32, mSMPTETime: AudioFile_SMPTE_Time, mType: UInt32, mReserved: UInt16, mChannel: UInt16)Added AudioFileMarkerList.init()Added AudioFileMarkerList.init(mSMPTE_TimeType: UInt32, mNumberMarkers: UInt32, mMarkers:(AudioFileMarker))Added AudioFilePacketTableInfo.init()Added AudioFilePacketTableInfo.init(mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32)Added AudioFileRegion.init()Added AudioFileRegion.init(mRegionID: UInt32, mName: Unmanaged<CFString>!, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers:(AudioFileMarker))Added AudioFileRegionList.init()Added AudioFileRegionList.init(mSMPTE_TimeType: UInt32, mNumberRegions: UInt32, mRegions:(AudioFileRegion))Added AudioFileTypeAndFormatID.init()Added AudioFileTypeAndFormatID.init(mFileType: AudioFileTypeID, mFormatID: UInt32)Added AudioFile_SMPTE_Time.init()Added AudioFile_SMPTE_Time.init(mHours: Int8, mMinutes: UInt8, mSeconds: UInt8, mFrames: UInt8, mSubFrameSampleOffset: UInt32)Added AudioFormatInfo.init()Added AudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32)Added AudioFormatListItem.init()Added AudioFormatListItem.init(mASBD: AudioStreamBasicDescription, mChannelLayoutTag: AudioChannelLayoutTag)Added AudioFramePacketTranslation.init()Added AudioFramePacketTranslation.init(mFrame: Int64, mPacket: Int64, mFrameOffsetInPacket: UInt32)Added AudioPanningInfo.init()Added AudioPanningInfo.init(mPanningMode: UInt32, mCoordinateFlags: UInt32, mCoordinates:(Float32, Float32, Float32), mGainScale: Float32, mOutputChannelMap: UnsafePointer<AudioChannelLayout>)Added AudioQueueBuffer.init()Added AudioQueueBuffer.init(mAudioDataBytesCapacity: UInt32, mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize: UInt32, mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity: UInt32, mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount: UInt32)Added AudioQueueChannelAssignment.init()Added AudioQueueChannelAssignment.init(mDeviceUID: Unmanaged<CFString>!, mChannelNumber: UInt32)Added AudioQueueLevelMeterState.init()Added AudioQueueLevelMeterState.init(mAveragePower: Float32, mPeakPower: Float32)Added AudioQueueParameterEvent.init()Added AudioQueueParameterEvent.init(mID: AudioQueueParameterID, mValue: AudioQueueParameterValue)Added AudioUnitNodeConnection.init()Added AudioUnitNodeConnection.init(sourceNode: AUNode, sourceOutputNumber: UInt32, destNode: AUNode, destInputNumber: UInt32)Added CABarBeatTime.init()Added CABarBeatTime.init(bar: Int32, beat: UInt16, subbeat: UInt16, subbeatDivisor: UInt16, reserved: UInt16)Added CAFAudioDescription.init()Added CAFAudioDescription.init(mSampleRate: Float64, mFormatID: UInt32, mFormatFlags: UInt32, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32)Added CAFAudioFormatListItem.init()Added CAFAudioFormatListItem.init(mFormat: CAFAudioDescription, mChannelLayoutTag: UInt32)Added CAFChunkHeader.init()Added CAFChunkHeader.init(mChunkType: UInt32, mChunkSize: Int64)Added CAFDataChunk.init()Added CAFDataChunk.init(mEditCount: UInt32, mData:(UInt8))Added CAFFileHeader.init()Added CAFFileHeader.init(mFileType: UInt32, mFileVersion: UInt16, mFileFlags: UInt16)Added CAFInfoStrings.init()Added CAFInfoStrings.init(mNumEntries: UInt32)Added CAFInstrumentChunk.init()Added CAFInstrumentChunk.init(mBaseNote: Float32, mMIDILowNote: UInt8, mMIDIHighNote: UInt8, mMIDILowVelocity: UInt8, mMIDIHighVelocity: UInt8, mdBGain: Float32, mStartRegionID: UInt32, mSustainRegionID: UInt32, mReleaseRegionID: UInt32, mInstrumentID: UInt32)Added CAFMarker.init()Added CAFMarker.init(mType: UInt32, mFramePosition: Float64, mMarkerID: UInt32, mSMPTETime: CAF_SMPTE_Time, mChannel: UInt32)Added CAFMarkerChunk.init()Added CAFMarkerChunk.init(mSMPTE_TimeType: UInt32, mNumberMarkers: UInt32, mMarkers:(CAFMarker))Added CAFOverviewChunk.init()Added CAFOverviewChunk.init(mEditCount: UInt32, mNumFramesPerOVWSample: UInt32, mData:(CAFOverviewSample))Added CAFOverviewSample.init()Added CAFOverviewSample.init(mMinValue: Int16, mMaxValue: Int16)Added CAFPacketTableHeader.init()Added CAFPacketTableHeader.init(mNumberPackets: Int64, mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32, mPacketDescriptions:(UInt8))Added CAFPeakChunk.init()Added CAFPeakChunk.init(mEditCount: UInt32, mPeaks:(CAFPositionPeak))Added CAFPositionPeak.init()Added CAFPositionPeak.init(mValue: Float32, mFrameNumber: UInt64)Added CAFRegion.init()Added CAFRegion.init(mRegionID: UInt32, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers:(CAFMarker))Added CAFRegionChunk.init()Added CAFRegionChunk.init(mSMPTE_TimeType: UInt32, mNumberRegions: UInt32, mRegions:(CAFRegion))Added CAFStringID.init()Added CAFStringID.init(mStringID: UInt32, mStringStartByteOffset: Int64)Added CAFStrings.init()Added CAFStrings.init(mNumEntries: UInt32, mStringsIDs:(CAFStringID))Added CAFUMIDChunk.init()Added CAFUMIDChunk.init(mBytes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added CAF_SMPTE_Time.init()Added CAF_SMPTE_Time.init(mHours: Int8, mMinutes: Int8, mSeconds: Int8, mFrames: Int8, mSubFrameSampleOffset: UInt32)Added CAF_UUID_ChunkHeader.init()Added CAF_UUID_ChunkHeader.init(mHeader: CAFChunkHeader, mUUID:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added ExtendedAudioFormatInfo.init()Added ExtendedAudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32, mClassDescription: AudioClassDescription)Added ExtendedNoteOnEvent.init()Added ExtendedNoteOnEvent.init(instrumentID: MusicDeviceInstrumentID, groupID: MusicDeviceGroupID, duration: Float32, extendedParams: MusicDeviceNoteParams)Added ExtendedTempoEvent.init()Added ExtendedTempoEvent.init(bpm: Float64)Added MIDIChannelMessage.init()Added MIDIChannelMessage.init(status: UInt8, data1: UInt8, data2: UInt8, reserved: UInt8)Added MIDIMetaEvent.init()Added MIDIMetaEvent.init(metaEventType: UInt8, unused1: UInt8, unused2: UInt8, unused3: UInt8, dataLength: UInt32, data:(UInt8))Added MIDINoteMessage.init()Added MIDINoteMessage.init(channel: UInt8, note: UInt8, velocity: UInt8, releaseVelocity: UInt8, duration: Float32)Added MIDIRawData.init()Added MIDIRawData.init(length: UInt32, data:(UInt8))Added MusicEventUserData.init()Added MusicEventUserData.init(length: UInt32, data:(UInt8))Added MusicTrackLoopInfo.init()Added MusicTrackLoopInfo.init(loopDuration: MusicTimeStamp, numberOfLoops: Int32)Added ParameterEvent.init()Added ParameterEvent.init(parameterID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement, value: AudioUnitParameterValue)Modified AUNodeInteraction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUNodeInteraction {     var nodeInteractionType: UInt32 } ``` |
| To | ``` struct AUNodeInteraction {     var nodeInteractionType: UInt32     init() } ``` |

Modified AUNodeRenderCallback [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUNodeRenderCallback {     var destNode: AUNode     var destInputNumber: AudioUnitElement     var cback: AURenderCallbackStruct } ``` |
| To | ``` struct AUNodeRenderCallback {     var destNode: AUNode     var destInputNumber: AudioUnitElement     var cback: AURenderCallbackStruct     init()     init(destNode destNode: AUNode, destInputNumber destInputNumber: AudioUnitElement, cback cback: AURenderCallbackStruct) } ``` |

Modified AUPresetEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyList>! } ``` |
| To | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyList>!     init()     init(scope scope: AudioUnitScope, element element: AudioUnitElement, preset preset: Unmanaged<CFPropertyList>!) } ``` |

Modified AudioBalanceFade [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: UInt32     var mChannelLayout: UnsafePointer<AudioChannelLayout> } ``` |
| To | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: UInt32     var mChannelLayout: UnsafePointer<AudioChannelLayout>     init()     init(mLeftRightBalance mLeftRightBalance: Float32, mBackFrontFade mBackFrontFade: Float32, mType mType: UInt32, mChannelLayout mChannelLayout: UnsafePointer<AudioChannelLayout>) } ``` |

Modified AudioBytePacketTranslation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBytePacketTranslation {     var mByte: Int64     var mPacket: Int64     var mByteOffsetInPacket: UInt32     var mFlags: UInt32 } ``` |
| To | ``` struct AudioBytePacketTranslation {     var mByte: Int64     var mPacket: Int64     var mByteOffsetInPacket: UInt32     var mFlags: UInt32     init()     init(mByte mByte: Int64, mPacket mPacket: Int64, mByteOffsetInPacket mByteOffsetInPacket: UInt32, mFlags mFlags: UInt32) } ``` |

Modified AudioConverterPrimeInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioConverterPrimeInfo {     var leadingFrames: UInt32     var trailingFrames: UInt32 } ``` |
| To | ``` struct AudioConverterPrimeInfo {     var leadingFrames: UInt32     var trailingFrames: UInt32     init()     init(leadingFrames leadingFrames: UInt32, trailingFrames trailingFrames: UInt32) } ``` |

Modified AudioFileMarker [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileMarker {     var mFramePosition: Float64     var mName: Unmanaged<CFString>!     var mMarkerID: Int32     var mSMPTETime: AudioFile_SMPTE_Time     var mType: UInt32     var mReserved: UInt16     var mChannel: UInt16 } ``` |
| To | ``` struct AudioFileMarker {     var mFramePosition: Float64     var mName: Unmanaged<CFString>!     var mMarkerID: Int32     var mSMPTETime: AudioFile_SMPTE_Time     var mType: UInt32     var mReserved: UInt16     var mChannel: UInt16     init()     init(mFramePosition mFramePosition: Float64, mName mName: Unmanaged<CFString>!, mMarkerID mMarkerID: Int32, mSMPTETime mSMPTETime: AudioFile_SMPTE_Time, mType mType: UInt32, mReserved mReserved: UInt16, mChannel mChannel: UInt16) } ``` |

Modified AudioFileMarkerList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileMarkerList {     var mSMPTE_TimeType: UInt32     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker) } ``` |
| To | ``` struct AudioFileMarkerList {     var mSMPTE_TimeType: UInt32     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker)     init()     init(mSMPTE_TimeType mSMPTE_TimeType: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (AudioFileMarker)) } ``` |

Modified AudioFilePacketTableInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFilePacketTableInfo {     var mNumberValidFrames: Int64     var mPrimingFrames: Int32     var mRemainderFrames: Int32 } ``` |
| To | ``` struct AudioFilePacketTableInfo {     var mNumberValidFrames: Int64     var mPrimingFrames: Int32     var mRemainderFrames: Int32     init()     init(mNumberValidFrames mNumberValidFrames: Int64, mPrimingFrames mPrimingFrames: Int32, mRemainderFrames mRemainderFrames: Int32) } ``` |

Modified AudioFileRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileRegion {     var mRegionID: UInt32     var mName: Unmanaged<CFString>!     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker) } ``` |
| To | ``` struct AudioFileRegion {     var mRegionID: UInt32     var mName: Unmanaged<CFString>!     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker)     init()     init(mRegionID mRegionID: UInt32, mName mName: Unmanaged<CFString>!, mFlags mFlags: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (AudioFileMarker)) } ``` |

Modified AudioFileRegionList [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileRegionList {     var mSMPTE_TimeType: UInt32     var mNumberRegions: UInt32     var mRegions: (AudioFileRegion) } ``` |
| To | ``` struct AudioFileRegionList {     var mSMPTE_TimeType: UInt32     var mNumberRegions: UInt32     var mRegions: (AudioFileRegion)     init()     init(mSMPTE_TimeType mSMPTE_TimeType: UInt32, mNumberRegions mNumberRegions: UInt32, mRegions mRegions: (AudioFileRegion)) } ``` |

Modified AudioFileTypeAndFormatID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileTypeAndFormatID {     var mFileType: AudioFileTypeID     var mFormatID: UInt32 } ``` |
| To | ``` struct AudioFileTypeAndFormatID {     var mFileType: AudioFileTypeID     var mFormatID: UInt32     init()     init(mFileType mFileType: AudioFileTypeID, mFormatID mFormatID: UInt32) } ``` |

Modified AudioFile_SMPTE_Time [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFile_SMPTE_Time {     var mHours: Int8     var mMinutes: UInt8     var mSeconds: UInt8     var mFrames: UInt8     var mSubFrameSampleOffset: UInt32 } ``` |
| To | ``` struct AudioFile_SMPTE_Time {     var mHours: Int8     var mMinutes: UInt8     var mSeconds: UInt8     var mFrames: UInt8     var mSubFrameSampleOffset: UInt32     init()     init(mHours mHours: Int8, mMinutes mMinutes: UInt8, mSeconds mSeconds: UInt8, mFrames mFrames: UInt8, mSubFrameSampleOffset mSubFrameSampleOffset: UInt32) } ``` |

Modified AudioFormatInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32 } ``` |
| To | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32) } ``` |

Modified AudioFormatListItem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFormatListItem {     var mASBD: AudioStreamBasicDescription     var mChannelLayoutTag: AudioChannelLayoutTag } ``` |
| To | ``` struct AudioFormatListItem {     var mASBD: AudioStreamBasicDescription     var mChannelLayoutTag: AudioChannelLayoutTag     init()     init(mASBD mASBD: AudioStreamBasicDescription, mChannelLayoutTag mChannelLayoutTag: AudioChannelLayoutTag) } ``` |

Modified AudioFramePacketTranslation [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFramePacketTranslation {     var mFrame: Int64     var mPacket: Int64     var mFrameOffsetInPacket: UInt32 } ``` |
| To | ``` struct AudioFramePacketTranslation {     var mFrame: Int64     var mPacket: Int64     var mFrameOffsetInPacket: UInt32     init()     init(mFrame mFrame: Int64, mPacket mPacket: Int64, mFrameOffsetInPacket mFrameOffsetInPacket: UInt32) } ``` |

Modified AudioPanningInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioPanningInfo {     var mPanningMode: UInt32     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: UnsafePointer<AudioChannelLayout> } ``` |
| To | ``` struct AudioPanningInfo {     var mPanningMode: UInt32     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: UnsafePointer<AudioChannelLayout>     init()     init(mPanningMode mPanningMode: UInt32, mCoordinateFlags mCoordinateFlags: UInt32, mCoordinates mCoordinates: (Float32, Float32, Float32), mGainScale mGainScale: Float32, mOutputChannelMap mOutputChannelMap: UnsafePointer<AudioChannelLayout>) } ``` |

Modified AudioQueueBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32 } ``` |
| To | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32     init()     init(mAudioDataBytesCapacity mAudioDataBytesCapacity: UInt32, mAudioData mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize mAudioDataByteSize: UInt32, mUserData mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity mPacketDescriptionCapacity: UInt32, mPacketDescriptions mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount mPacketDescriptionCount: UInt32) } ``` |

Modified AudioQueueChannelAssignment [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueChannelAssignment {     var mDeviceUID: Unmanaged<CFString>!     var mChannelNumber: UInt32 } ``` |
| To | ``` struct AudioQueueChannelAssignment {     var mDeviceUID: Unmanaged<CFString>!     var mChannelNumber: UInt32     init()     init(mDeviceUID mDeviceUID: Unmanaged<CFString>!, mChannelNumber mChannelNumber: UInt32) } ``` |

Modified AudioQueueLevelMeterState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueLevelMeterState {     var mAveragePower: Float32     var mPeakPower: Float32 } ``` |
| To | ``` struct AudioQueueLevelMeterState {     var mAveragePower: Float32     var mPeakPower: Float32     init()     init(mAveragePower mAveragePower: Float32, mPeakPower mPeakPower: Float32) } ``` |

Modified AudioQueueParameterEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueParameterEvent {     var mID: AudioQueueParameterID     var mValue: AudioQueueParameterValue } ``` |
| To | ``` struct AudioQueueParameterEvent {     var mID: AudioQueueParameterID     var mValue: AudioQueueParameterValue     init()     init(mID mID: AudioQueueParameterID, mValue mValue: AudioQueueParameterValue) } ``` |

Modified AudioUnitNodeConnection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitNodeConnection {     var sourceNode: AUNode     var sourceOutputNumber: UInt32     var destNode: AUNode     var destInputNumber: UInt32 } ``` |
| To | ``` struct AudioUnitNodeConnection {     var sourceNode: AUNode     var sourceOutputNumber: UInt32     var destNode: AUNode     var destInputNumber: UInt32     init()     init(sourceNode sourceNode: AUNode, sourceOutputNumber sourceOutputNumber: UInt32, destNode destNode: AUNode, destInputNumber destInputNumber: UInt32) } ``` |

Modified CABarBeatTime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CABarBeatTime {     var bar: Int32     var beat: UInt16     var subbeat: UInt16     var subbeatDivisor: UInt16     var reserved: UInt16 } ``` |
| To | ``` struct CABarBeatTime {     var bar: Int32     var beat: UInt16     var subbeat: UInt16     var subbeatDivisor: UInt16     var reserved: UInt16     init()     init(bar bar: Int32, beat beat: UInt16, subbeat subbeat: UInt16, subbeatDivisor subbeatDivisor: UInt16, reserved reserved: UInt16) } ``` |

Modified CAFAudioDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFAudioDescription {     var mSampleRate: Float64     var mFormatID: UInt32     var mFormatFlags: UInt32     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32 } ``` |
| To | ``` struct CAFAudioDescription {     var mSampleRate: Float64     var mFormatID: UInt32     var mFormatFlags: UInt32     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32     init()     init(mSampleRate mSampleRate: Float64, mFormatID mFormatID: UInt32, mFormatFlags mFormatFlags: UInt32, mBytesPerPacket mBytesPerPacket: UInt32, mFramesPerPacket mFramesPerPacket: UInt32, mChannelsPerFrame mChannelsPerFrame: UInt32, mBitsPerChannel mBitsPerChannel: UInt32) } ``` |

Modified CAFAudioFormatListItem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFAudioFormatListItem {     var mFormat: CAFAudioDescription     var mChannelLayoutTag: UInt32 } ``` |
| To | ``` struct CAFAudioFormatListItem {     var mFormat: CAFAudioDescription     var mChannelLayoutTag: UInt32     init()     init(mFormat mFormat: CAFAudioDescription, mChannelLayoutTag mChannelLayoutTag: UInt32) } ``` |

Modified CAFChunkHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFChunkHeader {     var mChunkType: UInt32     var mChunkSize: Int64 } ``` |
| To | ``` struct CAFChunkHeader {     var mChunkType: UInt32     var mChunkSize: Int64     init()     init(mChunkType mChunkType: UInt32, mChunkSize mChunkSize: Int64) } ``` |

Modified CAFDataChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFDataChunk {     var mEditCount: UInt32     var mData: (UInt8) } ``` |
| To | ``` struct CAFDataChunk {     var mEditCount: UInt32     var mData: (UInt8)     init()     init(mEditCount mEditCount: UInt32, mData mData: (UInt8)) } ``` |

Modified CAFFileHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFFileHeader {     var mFileType: UInt32     var mFileVersion: UInt16     var mFileFlags: UInt16 } ``` |
| To | ``` struct CAFFileHeader {     var mFileType: UInt32     var mFileVersion: UInt16     var mFileFlags: UInt16     init()     init(mFileType mFileType: UInt32, mFileVersion mFileVersion: UInt16, mFileFlags mFileFlags: UInt16) } ``` |

Modified CAFInfoStrings [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFInfoStrings {     var mNumEntries: UInt32 } ``` |
| To | ``` struct CAFInfoStrings {     var mNumEntries: UInt32     init()     init(mNumEntries mNumEntries: UInt32) } ``` |

Modified CAFInstrumentChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFInstrumentChunk {     var mBaseNote: Float32     var mMIDILowNote: UInt8     var mMIDIHighNote: UInt8     var mMIDILowVelocity: UInt8     var mMIDIHighVelocity: UInt8     var mdBGain: Float32     var mStartRegionID: UInt32     var mSustainRegionID: UInt32     var mReleaseRegionID: UInt32     var mInstrumentID: UInt32 } ``` |
| To | ``` struct CAFInstrumentChunk {     var mBaseNote: Float32     var mMIDILowNote: UInt8     var mMIDIHighNote: UInt8     var mMIDILowVelocity: UInt8     var mMIDIHighVelocity: UInt8     var mdBGain: Float32     var mStartRegionID: UInt32     var mSustainRegionID: UInt32     var mReleaseRegionID: UInt32     var mInstrumentID: UInt32     init()     init(mBaseNote mBaseNote: Float32, mMIDILowNote mMIDILowNote: UInt8, mMIDIHighNote mMIDIHighNote: UInt8, mMIDILowVelocity mMIDILowVelocity: UInt8, mMIDIHighVelocity mMIDIHighVelocity: UInt8, mdBGain mdBGain: Float32, mStartRegionID mStartRegionID: UInt32, mSustainRegionID mSustainRegionID: UInt32, mReleaseRegionID mReleaseRegionID: UInt32, mInstrumentID mInstrumentID: UInt32) } ``` |

Modified CAFMarker [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFMarker {     var mType: UInt32     var mFramePosition: Float64     var mMarkerID: UInt32     var mSMPTETime: CAF_SMPTE_Time     var mChannel: UInt32 } ``` |
| To | ``` struct CAFMarker {     var mType: UInt32     var mFramePosition: Float64     var mMarkerID: UInt32     var mSMPTETime: CAF_SMPTE_Time     var mChannel: UInt32     init()     init(mType mType: UInt32, mFramePosition mFramePosition: Float64, mMarkerID mMarkerID: UInt32, mSMPTETime mSMPTETime: CAF_SMPTE_Time, mChannel mChannel: UInt32) } ``` |

Modified CAFMarkerChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFMarkerChunk {     var mSMPTE_TimeType: UInt32     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker) } ``` |
| To | ``` struct CAFMarkerChunk {     var mSMPTE_TimeType: UInt32     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker)     init()     init(mSMPTE_TimeType mSMPTE_TimeType: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (CAFMarker)) } ``` |

Modified CAFOverviewChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFOverviewChunk {     var mEditCount: UInt32     var mNumFramesPerOVWSample: UInt32     var mData: (CAFOverviewSample) } ``` |
| To | ``` struct CAFOverviewChunk {     var mEditCount: UInt32     var mNumFramesPerOVWSample: UInt32     var mData: (CAFOverviewSample)     init()     init(mEditCount mEditCount: UInt32, mNumFramesPerOVWSample mNumFramesPerOVWSample: UInt32, mData mData: (CAFOverviewSample)) } ``` |

Modified CAFOverviewSample [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFOverviewSample {     var mMinValue: Int16     var mMaxValue: Int16 } ``` |
| To | ``` struct CAFOverviewSample {     var mMinValue: Int16     var mMaxValue: Int16     init()     init(mMinValue mMinValue: Int16, mMaxValue mMaxValue: Int16) } ``` |

Modified CAFPacketTableHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFPacketTableHeader {     var mNumberPackets: Int64     var mNumberValidFrames: Int64     var mPrimingFrames: Int32     var mRemainderFrames: Int32     var mPacketDescriptions: (UInt8) } ``` |
| To | ``` struct CAFPacketTableHeader {     var mNumberPackets: Int64     var mNumberValidFrames: Int64     var mPrimingFrames: Int32     var mRemainderFrames: Int32     var mPacketDescriptions: (UInt8)     init()     init(mNumberPackets mNumberPackets: Int64, mNumberValidFrames mNumberValidFrames: Int64, mPrimingFrames mPrimingFrames: Int32, mRemainderFrames mRemainderFrames: Int32, mPacketDescriptions mPacketDescriptions: (UInt8)) } ``` |

Modified CAFPeakChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFPeakChunk {     var mEditCount: UInt32     var mPeaks: (CAFPositionPeak) } ``` |
| To | ``` struct CAFPeakChunk {     var mEditCount: UInt32     var mPeaks: (CAFPositionPeak)     init()     init(mEditCount mEditCount: UInt32, mPeaks mPeaks: (CAFPositionPeak)) } ``` |

Modified CAFPositionPeak [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFPositionPeak {     var mValue: Float32     var mFrameNumber: UInt64 } ``` |
| To | ``` struct CAFPositionPeak {     var mValue: Float32     var mFrameNumber: UInt64     init()     init(mValue mValue: Float32, mFrameNumber mFrameNumber: UInt64) } ``` |

Modified CAFRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFRegion {     var mRegionID: UInt32     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker) } ``` |
| To | ``` struct CAFRegion {     var mRegionID: UInt32     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker)     init()     init(mRegionID mRegionID: UInt32, mFlags mFlags: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (CAFMarker)) } ``` |

Modified CAFRegionChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFRegionChunk {     var mSMPTE_TimeType: UInt32     var mNumberRegions: UInt32     var mRegions: (CAFRegion) } ``` |
| To | ``` struct CAFRegionChunk {     var mSMPTE_TimeType: UInt32     var mNumberRegions: UInt32     var mRegions: (CAFRegion)     init()     init(mSMPTE_TimeType mSMPTE_TimeType: UInt32, mNumberRegions mNumberRegions: UInt32, mRegions mRegions: (CAFRegion)) } ``` |

Modified CAFStringID [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFStringID {     var mStringID: UInt32     var mStringStartByteOffset: Int64 } ``` |
| To | ``` struct CAFStringID {     var mStringID: UInt32     var mStringStartByteOffset: Int64     init()     init(mStringID mStringID: UInt32, mStringStartByteOffset mStringStartByteOffset: Int64) } ``` |

Modified CAFStrings [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFStrings {     var mNumEntries: UInt32     var mStringsIDs: (CAFStringID) } ``` |
| To | ``` struct CAFStrings {     var mNumEntries: UInt32     var mStringsIDs: (CAFStringID)     init()     init(mNumEntries mNumEntries: UInt32, mStringsIDs mStringsIDs: (CAFStringID)) } ``` |

Modified CAFUMIDChunk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAFUMIDChunk {     var mBytes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct CAFUMIDChunk {     var mBytes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(mBytes mBytes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified CAF_SMPTE_Time [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAF_SMPTE_Time {     var mHours: Int8     var mMinutes: Int8     var mSeconds: Int8     var mFrames: Int8     var mSubFrameSampleOffset: UInt32 } ``` |
| To | ``` struct CAF_SMPTE_Time {     var mHours: Int8     var mMinutes: Int8     var mSeconds: Int8     var mFrames: Int8     var mSubFrameSampleOffset: UInt32     init()     init(mHours mHours: Int8, mMinutes mMinutes: Int8, mSeconds mSeconds: Int8, mFrames mFrames: Int8, mSubFrameSampleOffset mSubFrameSampleOffset: UInt32) } ``` |

Modified CAF_UUID_ChunkHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAF_UUID_ChunkHeader {     var mHeader: CAFChunkHeader     var mUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct CAF_UUID_ChunkHeader {     var mHeader: CAFChunkHeader     var mUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(mHeader mHeader: CAFChunkHeader, mUUID mUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified ExtendedAudioFormatInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription } ``` |
| To | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32, mClassDescription mClassDescription: AudioClassDescription) } ``` |

Modified ExtendedNoteOnEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedNoteOnEvent {     var instrumentID: MusicDeviceInstrumentID     var groupID: MusicDeviceGroupID     var duration: Float32     var extendedParams: MusicDeviceNoteParams } ``` |
| To | ``` struct ExtendedNoteOnEvent {     var instrumentID: MusicDeviceInstrumentID     var groupID: MusicDeviceGroupID     var duration: Float32     var extendedParams: MusicDeviceNoteParams     init()     init(instrumentID instrumentID: MusicDeviceInstrumentID, groupID groupID: MusicDeviceGroupID, duration duration: Float32, extendedParams extendedParams: MusicDeviceNoteParams) } ``` |

Modified ExtendedTempoEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedTempoEvent {     var bpm: Float64 } ``` |
| To | ``` struct ExtendedTempoEvent {     var bpm: Float64     init()     init(bpm bpm: Float64) } ``` |

Modified MIDIChannelMessage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIChannelMessage {     var status: UInt8     var data1: UInt8     var data2: UInt8     var reserved: UInt8 } ``` |
| To | ``` struct MIDIChannelMessage {     var status: UInt8     var data1: UInt8     var data2: UInt8     var reserved: UInt8     init()     init(status status: UInt8, data1 data1: UInt8, data2 data2: UInt8, reserved reserved: UInt8) } ``` |

Modified MIDIMetaEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIMetaEvent {     var metaEventType: UInt8     var unused1: UInt8     var unused2: UInt8     var unused3: UInt8     var dataLength: UInt32     var data: (UInt8) } ``` |
| To | ``` struct MIDIMetaEvent {     var metaEventType: UInt8     var unused1: UInt8     var unused2: UInt8     var unused3: UInt8     var dataLength: UInt32     var data: (UInt8)     init()     init(metaEventType metaEventType: UInt8, unused1 unused1: UInt8, unused2 unused2: UInt8, unused3 unused3: UInt8, dataLength dataLength: UInt32, data data: (UInt8)) } ``` |

Modified MIDINoteMessage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDINoteMessage {     var channel: UInt8     var note: UInt8     var velocity: UInt8     var releaseVelocity: UInt8     var duration: Float32 } ``` |
| To | ``` struct MIDINoteMessage {     var channel: UInt8     var note: UInt8     var velocity: UInt8     var releaseVelocity: UInt8     var duration: Float32     init()     init(channel channel: UInt8, note note: UInt8, velocity velocity: UInt8, releaseVelocity releaseVelocity: UInt8, duration duration: Float32) } ``` |

Modified MIDIRawData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MIDIRawData {     var length: UInt32     var data: (UInt8) } ``` |
| To | ``` struct MIDIRawData {     var length: UInt32     var data: (UInt8)     init()     init(length length: UInt32, data data: (UInt8)) } ``` |

Modified MusicEventUserData [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MusicEventUserData {     var length: UInt32     var data: (UInt8) } ``` |
| To | ``` struct MusicEventUserData {     var length: UInt32     var data: (UInt8)     init()     init(length length: UInt32, data data: (UInt8)) } ``` |

Modified MusicTrackLoopInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MusicTrackLoopInfo {     var loopDuration: MusicTimeStamp     var numberOfLoops: Int32 } ``` |
| To | ``` struct MusicTrackLoopInfo {     var loopDuration: MusicTimeStamp     var numberOfLoops: Int32     init()     init(loopDuration loopDuration: MusicTimeStamp, numberOfLoops numberOfLoops: Int32) } ``` |

Modified ParameterEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ParameterEvent {     var parameterID: AudioUnitParameterID     var scope: AudioUnitScope     var element: AudioUnitElement     var value: AudioUnitParameterValue } ``` |
| To | ``` struct ParameterEvent {     var parameterID: AudioUnitParameterID     var scope: AudioUnitScope     var element: AudioUnitElement     var value: AudioUnitParameterValue     init()     init(parameterID parameterID: AudioUnitParameterID, scope scope: AudioUnitScope, element element: AudioUnitElement, value value: AudioUnitParameterValue) } ``` |

Modified MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetSMPTEResolution(_ inRes: Int16, _ fps: UnsafeMutablePointer<SignedByte>, _ ticks: UnsafeMutablePointer<Byte>) ``` | iOS 8.0 |
| To | ``` func MusicSequenceGetSMPTEResolution(_ inRes: Int16, _ fps: UnsafeMutablePointer<Int8>, _ ticks: UnsafeMutablePointer<UInt8>) ``` | iOS 8.3 |

Modified MusicSequenceSetMIDIEndpoint(MusicSequence, MIDIEndpointRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceSetMIDIEndpoint(_ inSequence: MusicSequence, _ inEndpoint: MIDIEndpoint!) -> OSStatus ``` |
| To | ``` func MusicSequenceSetMIDIEndpoint(_ inSequence: MusicSequence, _ inEndpoint: MIDIEndpointRef) -> OSStatus ``` |

Modified MusicSequenceSetSMPTEResolution(Int8, UInt8) -> Int16

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceSetSMPTEResolution(_ fps: SignedByte, _ ticks: Byte) -> Int16 ``` | iOS 8.0 |
| To | ``` func MusicSequenceSetSMPTEResolution(_ fps: Int8, _ ticks: UInt8) -> Int16 ``` | iOS 8.3 |

Modified MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MusicTrackGetDestMIDIEndpoint(_ inTrack: MusicTrack, _ outEndpoint: UnsafeMutablePointer<Unmanaged<MIDIEndpoint>?>) -> OSStatus ``` |
| To | ``` func MusicTrackGetDestMIDIEndpoint(_ inTrack: MusicTrack, _ outEndpoint: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` |

Modified MusicTrackSetDestMIDIEndpoint(MusicTrack, MIDIEndpointRef) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func MusicTrackSetDestMIDIEndpoint(_ inTrack: MusicTrack, _ inEndpoint: MIDIEndpoint!) -> OSStatus ``` |
| To | ``` func MusicTrackSetDestMIDIEndpoint(_ inTrack: MusicTrack, _ inEndpoint: MIDIEndpointRef) -> OSStatus ``` |

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
