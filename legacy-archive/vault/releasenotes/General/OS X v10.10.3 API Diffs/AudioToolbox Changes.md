---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/AudioToolbox.html
archived_at: '2026-07-18T02:52:05.565995Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# AudioToolbox Changes

## AudioToolbox

Added AUNodeInteraction.init()Added AUNodeRenderCallback.init()Added AUNodeRenderCallback.init(destNode: AUNode, destInputNumber: AudioUnitElement, cback: AURenderCallbackStruct)Added AUPresetEvent.init()Added AUPresetEvent.init(scope: AudioUnitScope, element: AudioUnitElement, preset: Unmanaged<CFPropertyList>!)Added AudioBalanceFade.init()Added AudioBalanceFade.init(mLeftRightBalance: Float32, mBackFrontFade: Float32, mType: UInt32, mChannelLayout: UnsafePointer<AudioChannelLayout>)Added AudioBytePacketTranslation.init()Added AudioBytePacketTranslation.init(mByte: Int64, mPacket: Int64, mByteOffsetInPacket: UInt32, mFlags: UInt32)Added AudioConverterPrimeInfo.init()Added AudioConverterPrimeInfo.init(leadingFrames: UInt32, trailingFrames: UInt32)Added AudioFileFDFTable.init()Added AudioFileFDFTable.init(mComponentStorage: UnsafeMutablePointer<Void>, mReadBytesFDF: ReadBytesFDF, mWriteBytesFDF: WriteBytesFDF, mReadPacketsFDF: ReadPacketsFDF, mWritePacketsFDF: WritePacketsFDF, mGetPropertyInfoFDF: GetPropertyInfoFDF, mGetPropertyFDF: GetPropertyFDF, mSetPropertyFDF: SetPropertyFDF, mCountUserDataFDF: CountUserDataFDF, mGetUserDataSizeFDF: GetUserDataSizeFDF, mGetUserDataFDF: GetUserDataFDF, mSetUserDataFDF: SetUserDataFDF)Added AudioFileFDFTableExtended.init()Added AudioFileFDFTableExtended.init(mComponentStorage: UnsafeMutablePointer<Void>, mReadBytesFDF: ReadBytesFDF, mWriteBytesFDF: WriteBytesFDF, mReadPacketsFDF: ReadPacketsFDF, mWritePacketsFDF: WritePacketsFDF, mGetPropertyInfoFDF: GetPropertyInfoFDF, mGetPropertyFDF: GetPropertyFDF, mSetPropertyFDF: SetPropertyFDF, mCountUserDataFDF: CountUserDataFDF, mGetUserDataSizeFDF: GetUserDataSizeFDF, mGetUserDataFDF: GetUserDataFDF, mSetUserDataFDF: SetUserDataFDF, mReadPacketDataFDF: ReadPacketDataFDF)Added AudioFileMarker.init()Added AudioFileMarker.init(mFramePosition: Float64, mName: Unmanaged<CFString>!, mMarkerID: Int32, mSMPTETime: AudioFile_SMPTE_Time, mType: UInt32, mReserved: UInt16, mChannel: UInt16)Added AudioFileMarkerList.init()Added AudioFileMarkerList.init(mSMPTE_TimeType: UInt32, mNumberMarkers: UInt32, mMarkers:(AudioFileMarker))Added AudioFilePacketTableInfo.init()Added AudioFilePacketTableInfo.init(mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32)Added AudioFileRegion.init()Added AudioFileRegion.init(mRegionID: UInt32, mName: Unmanaged<CFString>!, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers:(AudioFileMarker))Added AudioFileRegionList.init()Added AudioFileRegionList.init(mSMPTE_TimeType: UInt32, mNumberRegions: UInt32, mRegions:(AudioFileRegion))Added AudioFileTypeAndFormatID.init()Added AudioFileTypeAndFormatID.init(mFileType: AudioFileTypeID, mFormatID: UInt32)Added AudioFile_SMPTE_Time.init()Added AudioFile_SMPTE_Time.init(mHours: Int8, mMinutes: UInt8, mSeconds: UInt8, mFrames: UInt8, mSubFrameSampleOffset: UInt32)Added AudioFormatInfo.init()Added AudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32)Added AudioFormatListItem.init()Added AudioFormatListItem.init(mASBD: AudioStreamBasicDescription, mChannelLayoutTag: AudioChannelLayoutTag)Added AudioFramePacketTranslation.init()Added AudioFramePacketTranslation.init(mFrame: Int64, mPacket: Int64, mFrameOffsetInPacket: UInt32)Added AudioPanningInfo.init()Added AudioPanningInfo.init(mPanningMode: UInt32, mCoordinateFlags: UInt32, mCoordinates:(Float32, Float32, Float32), mGainScale: Float32, mOutputChannelMap: UnsafePointer<AudioChannelLayout>)Added AudioQueueBuffer.init()Added AudioQueueBuffer.init(mAudioDataBytesCapacity: UInt32, mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize: UInt32, mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity: UInt32, mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount: UInt32)Added AudioQueueLevelMeterState.init()Added AudioQueueLevelMeterState.init(mAveragePower: Float32, mPeakPower: Float32)Added AudioQueueParameterEvent.init()Added AudioQueueParameterEvent.init(mID: AudioQueueParameterID, mValue: AudioQueueParameterValue)Added AudioUnitEvent.init()Added AudioUnitNodeConnection.init()Added AudioUnitNodeConnection.init(sourceNode: AUNode, sourceOutputNumber: UInt32, destNode: AUNode, destInputNumber: UInt32)Added CABarBeatTime.init()Added CABarBeatTime.init(bar: Int32, beat: UInt16, subbeat: UInt16, subbeatDivisor: UInt16, reserved: UInt16)Added CAClockTime.init()Added CAFAudioDescription.init()Added CAFAudioDescription.init(mSampleRate: Float64, mFormatID: UInt32, mFormatFlags: UInt32, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32)Added CAFAudioFormatListItem.init()Added CAFAudioFormatListItem.init(mFormat: CAFAudioDescription, mChannelLayoutTag: UInt32)Added CAFChunkHeader.init()Added CAFChunkHeader.init(mChunkType: UInt32, mChunkSize: Int64)Added CAFDataChunk.init()Added CAFDataChunk.init(mEditCount: UInt32, mData:(UInt8))Added CAFFileHeader.init()Added CAFFileHeader.init(mFileType: UInt32, mFileVersion: UInt16, mFileFlags: UInt16)Added CAFInfoStrings.init()Added CAFInfoStrings.init(mNumEntries: UInt32)Added CAFInstrumentChunk.init()Added CAFInstrumentChunk.init(mBaseNote: Float32, mMIDILowNote: UInt8, mMIDIHighNote: UInt8, mMIDILowVelocity: UInt8, mMIDIHighVelocity: UInt8, mdBGain: Float32, mStartRegionID: UInt32, mSustainRegionID: UInt32, mReleaseRegionID: UInt32, mInstrumentID: UInt32)Added CAFMarker.init()Added CAFMarker.init(mType: UInt32, mFramePosition: Float64, mMarkerID: UInt32, mSMPTETime: CAF_SMPTE_Time, mChannel: UInt32)Added CAFMarkerChunk.init()Added CAFMarkerChunk.init(mSMPTE_TimeType: UInt32, mNumberMarkers: UInt32, mMarkers:(CAFMarker))Added CAFOverviewChunk.init()Added CAFOverviewChunk.init(mEditCount: UInt32, mNumFramesPerOVWSample: UInt32, mData:(CAFOverviewSample))Added CAFOverviewSample.init()Added CAFOverviewSample.init(mMinValue: Int16, mMaxValue: Int16)Added CAFPacketTableHeader.init()Added CAFPacketTableHeader.init(mNumberPackets: Int64, mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32, mPacketDescriptions:(UInt8))Added CAFPeakChunk.init()Added CAFPeakChunk.init(mEditCount: UInt32, mPeaks:(CAFPositionPeak))Added CAFPositionPeak.init()Added CAFPositionPeak.init(mValue: Float32, mFrameNumber: UInt64)Added CAFRegion.init()Added CAFRegion.init(mRegionID: UInt32, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers:(CAFMarker))Added CAFRegionChunk.init()Added CAFRegionChunk.init(mSMPTE_TimeType: UInt32, mNumberRegions: UInt32, mRegions:(CAFRegion))Added CAFStringID.init()Added CAFStringID.init(mStringID: UInt32, mStringStartByteOffset: Int64)Added CAFStrings.init()Added CAFStrings.init(mNumEntries: UInt32, mStringsIDs:(CAFStringID))Added CAFUMIDChunk.init()Added CAFUMIDChunk.init(mBytes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added CAF_SMPTE_Time.init()Added CAF_SMPTE_Time.init(mHours: Int8, mMinutes: Int8, mSeconds: Int8, mFrames: Int8, mSubFrameSampleOffset: UInt32)Added CAF_UUID_ChunkHeader.init()Added CAF_UUID_ChunkHeader.init(mHeader: CAFChunkHeader, mUUID:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added CAMeterTrackEntry.init()Added CAMeterTrackEntry.init(beats: CAClockBeats, meterNumer: UInt16, meterDenom: UInt16)Added CATempoMapEntry.init()Added CATempoMapEntry.init(beats: CAClockBeats, tempoBPM: CAClockTempo)Added ExtendedAudioFormatInfo.init()Added ExtendedAudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32, mClassDescription: AudioClassDescription)Added ExtendedControlEvent.init()Added ExtendedControlEvent.init(groupID: MusicDeviceGroupID, controlID: AudioUnitParameterID, value: AudioUnitParameterValue)Added ExtendedNoteOnEvent.init()Added ExtendedNoteOnEvent.init(instrumentID: MusicDeviceInstrumentID, groupID: MusicDeviceGroupID, duration: Float32, extendedParams: MusicDeviceNoteParams)Added ExtendedTempoEvent.init()Added ExtendedTempoEvent.init(bpm: Float64)Added MIDIChannelMessage.init()Added MIDIChannelMessage.init(status: UInt8, data1: UInt8, data2: UInt8, reserved: UInt8)Added MIDIMetaEvent.init()Added MIDIMetaEvent.init(metaEventType: UInt8, unused1: UInt8, unused2: UInt8, unused3: UInt8, dataLength: UInt32, data:(UInt8))Added MIDINoteMessage.init()Added MIDINoteMessage.init(channel: UInt8, note: UInt8, velocity: UInt8, releaseVelocity: UInt8, duration: Float32)Added MIDIRawData.init()Added MIDIRawData.init(length: UInt32, data:(UInt8))Added MusicEventUserData.init()Added MusicEventUserData.init(length: UInt32, data:(UInt8))Added MusicTrackLoopInfo.init()Added MusicTrackLoopInfo.init(loopDuration: MusicTimeStamp, numberOfLoops: Int32)Added ParameterEvent.init()Added ParameterEvent.init(parameterID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement, value: AudioUnitParameterValue)Modified AUNodeInteraction [struct]

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
| From | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyListRef>! } ``` |
| To | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyList>!     init()     init(scope scope: AudioUnitScope, element element: AudioUnitElement, preset preset: Unmanaged<CFPropertyList>!) } ``` |

Modified AUPresetEvent.preset

|  | Declaration |
| --- | --- |
| From | ``` var preset: Unmanaged<CFPropertyListRef>! ``` |
| To | ``` var preset: Unmanaged<CFPropertyList>! ``` |

Modified AudioBalanceFade [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: UInt32     var mChannelLayout: ConstUnsafePointer<AudioChannelLayout> } ``` |
| To | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: UInt32     var mChannelLayout: UnsafePointer<AudioChannelLayout>     init()     init(mLeftRightBalance mLeftRightBalance: Float32, mBackFrontFade mBackFrontFade: Float32, mType mType: UInt32, mChannelLayout mChannelLayout: UnsafePointer<AudioChannelLayout>) } ``` |

Modified AudioBalanceFade.mChannelLayout

|  | Declaration |
| --- | --- |
| From | ``` var mChannelLayout: ConstUnsafePointer<AudioChannelLayout> ``` |
| To | ``` var mChannelLayout: UnsafePointer<AudioChannelLayout> ``` |

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

Modified AudioFileFDFTable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileFDFTable {     var mComponentStorage: UnsafePointer<()>     var mReadBytesFDF: ReadBytesFDF     var mWriteBytesFDF: WriteBytesFDF     var mReadPacketsFDF: ReadPacketsFDF     var mWritePacketsFDF: WritePacketsFDF     var mGetPropertyInfoFDF: GetPropertyInfoFDF     var mGetPropertyFDF: GetPropertyFDF     var mSetPropertyFDF: SetPropertyFDF     var mCountUserDataFDF: CountUserDataFDF     var mGetUserDataSizeFDF: GetUserDataSizeFDF     var mGetUserDataFDF: GetUserDataFDF     var mSetUserDataFDF: SetUserDataFDF } ``` |
| To | ``` struct AudioFileFDFTable {     var mComponentStorage: UnsafeMutablePointer<Void>     var mReadBytesFDF: ReadBytesFDF     var mWriteBytesFDF: WriteBytesFDF     var mReadPacketsFDF: ReadPacketsFDF     var mWritePacketsFDF: WritePacketsFDF     var mGetPropertyInfoFDF: GetPropertyInfoFDF     var mGetPropertyFDF: GetPropertyFDF     var mSetPropertyFDF: SetPropertyFDF     var mCountUserDataFDF: CountUserDataFDF     var mGetUserDataSizeFDF: GetUserDataSizeFDF     var mGetUserDataFDF: GetUserDataFDF     var mSetUserDataFDF: SetUserDataFDF     init()     init(mComponentStorage mComponentStorage: UnsafeMutablePointer<Void>, mReadBytesFDF mReadBytesFDF: ReadBytesFDF, mWriteBytesFDF mWriteBytesFDF: WriteBytesFDF, mReadPacketsFDF mReadPacketsFDF: ReadPacketsFDF, mWritePacketsFDF mWritePacketsFDF: WritePacketsFDF, mGetPropertyInfoFDF mGetPropertyInfoFDF: GetPropertyInfoFDF, mGetPropertyFDF mGetPropertyFDF: GetPropertyFDF, mSetPropertyFDF mSetPropertyFDF: SetPropertyFDF, mCountUserDataFDF mCountUserDataFDF: CountUserDataFDF, mGetUserDataSizeFDF mGetUserDataSizeFDF: GetUserDataSizeFDF, mGetUserDataFDF mGetUserDataFDF: GetUserDataFDF, mSetUserDataFDF mSetUserDataFDF: SetUserDataFDF) } ``` |

Modified AudioFileFDFTable.mComponentStorage

|  | Declaration |
| --- | --- |
| From | ``` var mComponentStorage: UnsafePointer<()> ``` |
| To | ``` var mComponentStorage: UnsafeMutablePointer<Void> ``` |

Modified AudioFileFDFTableExtended [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileFDFTableExtended {     var mComponentStorage: UnsafePointer<()>     var mReadBytesFDF: ReadBytesFDF     var mWriteBytesFDF: WriteBytesFDF     var mReadPacketsFDF: ReadPacketsFDF     var mWritePacketsFDF: WritePacketsFDF     var mGetPropertyInfoFDF: GetPropertyInfoFDF     var mGetPropertyFDF: GetPropertyFDF     var mSetPropertyFDF: SetPropertyFDF     var mCountUserDataFDF: CountUserDataFDF     var mGetUserDataSizeFDF: GetUserDataSizeFDF     var mGetUserDataFDF: GetUserDataFDF     var mSetUserDataFDF: SetUserDataFDF     var mReadPacketDataFDF: ReadPacketDataFDF } ``` |
| To | ``` struct AudioFileFDFTableExtended {     var mComponentStorage: UnsafeMutablePointer<Void>     var mReadBytesFDF: ReadBytesFDF     var mWriteBytesFDF: WriteBytesFDF     var mReadPacketsFDF: ReadPacketsFDF     var mWritePacketsFDF: WritePacketsFDF     var mGetPropertyInfoFDF: GetPropertyInfoFDF     var mGetPropertyFDF: GetPropertyFDF     var mSetPropertyFDF: SetPropertyFDF     var mCountUserDataFDF: CountUserDataFDF     var mGetUserDataSizeFDF: GetUserDataSizeFDF     var mGetUserDataFDF: GetUserDataFDF     var mSetUserDataFDF: SetUserDataFDF     var mReadPacketDataFDF: ReadPacketDataFDF     init()     init(mComponentStorage mComponentStorage: UnsafeMutablePointer<Void>, mReadBytesFDF mReadBytesFDF: ReadBytesFDF, mWriteBytesFDF mWriteBytesFDF: WriteBytesFDF, mReadPacketsFDF mReadPacketsFDF: ReadPacketsFDF, mWritePacketsFDF mWritePacketsFDF: WritePacketsFDF, mGetPropertyInfoFDF mGetPropertyInfoFDF: GetPropertyInfoFDF, mGetPropertyFDF mGetPropertyFDF: GetPropertyFDF, mSetPropertyFDF mSetPropertyFDF: SetPropertyFDF, mCountUserDataFDF mCountUserDataFDF: CountUserDataFDF, mGetUserDataSizeFDF mGetUserDataSizeFDF: GetUserDataSizeFDF, mGetUserDataFDF mGetUserDataFDF: GetUserDataFDF, mSetUserDataFDF mSetUserDataFDF: SetUserDataFDF, mReadPacketDataFDF mReadPacketDataFDF: ReadPacketDataFDF) } ``` |

Modified AudioFileFDFTableExtended.mComponentStorage

|  | Declaration |
| --- | --- |
| From | ``` var mComponentStorage: UnsafePointer<()> ``` |
| To | ``` var mComponentStorage: UnsafeMutablePointer<Void> ``` |

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
| From | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: ConstUnsafePointer<()>     var mMagicCookieSize: UInt32 } ``` |
| To | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32) } ``` |

Modified AudioFormatInfo.mMagicCookie

|  | Declaration |
| --- | --- |
| From | ``` var mMagicCookie: ConstUnsafePointer<()> ``` |
| To | ``` var mMagicCookie: UnsafePointer<Void> ``` |

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
| From | ``` struct AudioPanningInfo {     var mPanningMode: UInt32     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: ConstUnsafePointer<AudioChannelLayout> } ``` |
| To | ``` struct AudioPanningInfo {     var mPanningMode: UInt32     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: UnsafePointer<AudioChannelLayout>     init()     init(mPanningMode mPanningMode: UInt32, mCoordinateFlags mCoordinateFlags: UInt32, mCoordinates mCoordinates: (Float32, Float32, Float32), mGainScale mGainScale: Float32, mOutputChannelMap mOutputChannelMap: UnsafePointer<AudioChannelLayout>) } ``` |

Modified AudioPanningInfo.mOutputChannelMap

|  | Declaration |
| --- | --- |
| From | ``` var mOutputChannelMap: ConstUnsafePointer<AudioChannelLayout> ``` |
| To | ``` var mOutputChannelMap: UnsafePointer<AudioChannelLayout> ``` |

Modified AudioQueueBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafePointer<()>     var mAudioDataByteSize: UInt32     var mUserData: UnsafePointer<()>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32 } ``` |
| To | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32     init()     init(mAudioDataBytesCapacity mAudioDataBytesCapacity: UInt32, mAudioData mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize mAudioDataByteSize: UInt32, mUserData mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity mPacketDescriptionCapacity: UInt32, mPacketDescriptions mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount mPacketDescriptionCount: UInt32) } ``` |

Modified AudioQueueBuffer.mAudioData

|  | Declaration |
| --- | --- |
| From | ``` var mAudioData: UnsafePointer<()> ``` |
| To | ``` var mAudioData: UnsafeMutablePointer<Void> ``` |

Modified AudioQueueBuffer.mPacketDescriptions

|  | Declaration |
| --- | --- |
| From | ``` var mPacketDescriptions: UnsafePointer<AudioStreamPacketDescription> ``` |
| To | ``` var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription> ``` |

Modified AudioQueueBuffer.mUserData

|  | Declaration |
| --- | --- |
| From | ``` var mUserData: UnsafePointer<()> ``` |
| To | ``` var mUserData: UnsafeMutablePointer<Void> ``` |

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

Modified AudioUnitEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AudioUnitEvent {     var mEventType: AudioUnitEventType } ``` |
| To | ``` struct AudioUnitEvent {     var mEventType: AudioUnitEventType     init() } ``` |

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

Modified CAClockTime [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAClockTime {     var format: CAClockTimeFormat     var reserved: UInt32 } ``` |
| To | ``` struct CAClockTime {     var format: CAClockTimeFormat     var reserved: UInt32     init() } ``` |

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

Modified CAMeterTrackEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAMeterTrackEntry {     var beats: CAClockBeats     var meterNumer: UInt16     var meterDenom: UInt16 } ``` |
| To | ``` struct CAMeterTrackEntry {     var beats: CAClockBeats     var meterNumer: UInt16     var meterDenom: UInt16     init()     init(beats beats: CAClockBeats, meterNumer meterNumer: UInt16, meterDenom meterDenom: UInt16) } ``` |

Modified CATempoMapEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CATempoMapEntry {     var beats: CAClockBeats     var tempoBPM: CAClockTempo } ``` |
| To | ``` struct CATempoMapEntry {     var beats: CAClockBeats     var tempoBPM: CAClockTempo     init()     init(beats beats: CAClockBeats, tempoBPM tempoBPM: CAClockTempo) } ``` |

Modified ExtendedAudioFormatInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: ConstUnsafePointer<()>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription } ``` |
| To | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32, mClassDescription mClassDescription: AudioClassDescription) } ``` |

Modified ExtendedAudioFormatInfo.mMagicCookie

|  | Declaration |
| --- | --- |
| From | ``` var mMagicCookie: ConstUnsafePointer<()> ``` |
| To | ``` var mMagicCookie: UnsafePointer<Void> ``` |

Modified ExtendedControlEvent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedControlEvent {     var groupID: MusicDeviceGroupID     var controlID: AudioUnitParameterID     var value: AudioUnitParameterValue } ``` |
| To | ``` struct ExtendedControlEvent {     var groupID: MusicDeviceGroupID     var controlID: AudioUnitParameterID     var value: AudioUnitParameterValue     init()     init(groupID groupID: MusicDeviceGroupID, controlID controlID: AudioUnitParameterID, value value: AudioUnitParameterValue) } ``` |

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

Modified AUEventListenerAddEventType(AUEventListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUEventListenerAddEventType(_ inListener: AUEventListener!, _ inObject: UnsafePointer<()>, _ inEvent: ConstUnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUEventListenerAddEventType(_ inListener: AUEventListenerRef, _ inObject: UnsafeMutablePointer<Void>, _ inEvent: UnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.3 |

Modified AUEventListenerBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AUEventListenerBlock = (UnsafePointer<()>, ConstUnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void ``` |
| To | ``` typealias AUEventListenerBlock = (UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void ``` |

Modified AUEventListenerCreate(AUEventListenerProc, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, Float32, Float32, UnsafeMutablePointer<AUEventListenerRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUEventListenerCreate(_ inProc: AUEventListenerProc, _ inUserData: UnsafePointer<()>, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inNotificationInterval: Float32, _ inValueChangeGranularity: Float32, _ outListener: UnsafePointer<Unmanaged<AUEventListener>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUEventListenerCreate(_ inProc: AUEventListenerProc, _ inUserData: UnsafeMutablePointer<Void>, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inNotificationInterval: Float32, _ inValueChangeGranularity: Float32, _ outListener: UnsafeMutablePointer<AUEventListenerRef>) -> OSStatus ``` | OS X 10.3 |

Modified AUEventListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUEventListenerRef>, Float32, Float32, dispatch_queue_t!, AUEventListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUEventListenerCreateWithDispatchQueue(_ outListener: UnsafePointer<Unmanaged<AUEventListener>?>, _ inNotificationInterval: Float32, _ inValueChangeGranularity: Float32, _ inDispatchQueue: dispatch_queue_t!, _ inBlock: AUEventListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUEventListenerCreateWithDispatchQueue(_ outListener: UnsafeMutablePointer<AUEventListenerRef>, _ inNotificationInterval: Float32, _ inValueChangeGranularity: Float32, _ inDispatchQueue: dispatch_queue_t!, _ inBlock: AUEventListenerBlock!) -> OSStatus ``` | OS X 10.6 |

Modified AUEventListenerNotify(AUEventListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUEventListenerNotify(_ inSendingListener: AUEventListener!, _ inSendingObject: UnsafePointer<()>, _ inEvent: ConstUnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUEventListenerNotify(_ inSendingListener: AUEventListenerRef, _ inSendingObject: UnsafeMutablePointer<Void>, _ inEvent: UnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.3 |

Modified AUEventListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AUEventListenerProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, ConstUnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void)> ``` |
| To | ``` typealias AUEventListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitEvent>, UInt64, AudioUnitParameterValue) -> Void)> ``` |

Modified AUEventListenerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AUEventListenerRef = AUEventListener ``` |
| To | ``` typealias AUEventListenerRef = AUParameterListenerRef ``` |

Modified AUEventListenerRemoveEventType(AUEventListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUEventListenerRemoveEventType(_ inListener: AUEventListener!, _ inObject: UnsafePointer<()>, _ inEvent: ConstUnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUEventListenerRemoveEventType(_ inListener: AUEventListenerRef, _ inObject: UnsafeMutablePointer<Void>, _ inEvent: UnsafePointer<AudioUnitEvent>) -> OSStatus ``` | OS X 10.3 |

Modified AUGraphAddNode(AUGraph, UnsafePointer<AudioComponentDescription>, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphAddNode(_ inGraph: AUGraph, _ inDescription: ConstUnsafePointer<AudioComponentDescription>, _ outNode: UnsafePointer<AUNode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphAddNode(_ inGraph: AUGraph, _ inDescription: UnsafePointer<AudioComponentDescription>, _ outNode: UnsafeMutablePointer<AUNode>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphAddRenderNotify(AUGraph, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphAddRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphAddRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AUGraphClearConnections(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphClose(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphConnectNodeInput(AUGraph, AUNode, UInt32, AUNode, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphCountNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphCountNodeInteractions(_ inGraph: AUGraph, _ inNode: AUNode, _ outNumInteractions: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphCountNodeInteractions(_ inGraph: AUGraph, _ inNode: AUNode, _ outNumInteractions: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphDisconnectNodeInput(AUGraph, AUNode, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphGetCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetCPULoad(_ inGraph: AUGraph, _ outAverageCPULoad: UnsafePointer<Float32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetCPULoad(_ inGraph: AUGraph, _ outAverageCPULoad: UnsafeMutablePointer<Float32>) -> OSStatus ``` | OS X 10.1 |

Modified AUGraphGetIndNode(AUGraph, UInt32, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetIndNode(_ inGraph: AUGraph, _ inIndex: UInt32, _ outNode: UnsafePointer<AUNode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetIndNode(_ inGraph: AUGraph, _ inIndex: UInt32, _ outNode: UnsafeMutablePointer<AUNode>) -> OSStatus ``` | OS X 10.0 |

Modified AUGraphGetInteractionInfo(AUGraph, UInt32, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetInteractionInfo(_ inGraph: AUGraph, _ inInteractionIndex: UInt32, _ outInteraction: UnsafePointer<AUNodeInteraction>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetInteractionInfo(_ inGraph: AUGraph, _ inInteractionIndex: UInt32, _ outInteraction: UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphGetMaxCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetMaxCPULoad(_ inGraph: AUGraph, _ outMaxLoad: UnsafePointer<Float32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetMaxCPULoad(_ inGraph: AUGraph, _ outMaxLoad: UnsafeMutablePointer<Float32>) -> OSStatus ``` | OS X 10.3 |

Modified AUGraphGetNodeCount(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetNodeCount(_ inGraph: AUGraph, _ outNumberOfNodes: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetNodeCount(_ inGraph: AUGraph, _ outNumberOfNodes: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified AUGraphGetNodeInfoSubGraph(AUGraph, AUNode, UnsafeMutablePointer<AUGraph>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetNodeInfoSubGraph(_ inGraph: AUGraph, _ inNode: AUNode, _ outSubGraph: UnsafePointer<AUGraph>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetNodeInfoSubGraph(_ inGraph: AUGraph, _ inNode: AUNode, _ outSubGraph: UnsafeMutablePointer<AUGraph>) -> OSStatus ``` | OS X 10.2 |

Modified AUGraphGetNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetNodeInteractions(_ inGraph: AUGraph, _ inNode: AUNode, _ ioNumInteractions: UnsafePointer<UInt32>, _ outInteractions: UnsafePointer<AUNodeInteraction>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetNodeInteractions(_ inGraph: AUGraph, _ inNode: AUNode, _ ioNumInteractions: UnsafeMutablePointer<UInt32>, _ outInteractions: UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphGetNumberOfInteractions(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphGetNumberOfInteractions(_ inGraph: AUGraph, _ outNumInteractions: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphGetNumberOfInteractions(_ inGraph: AUGraph, _ outNumInteractions: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphInitialize(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphIsInitialized(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphIsInitialized(_ inGraph: AUGraph, _ outIsInitialized: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphIsInitialized(_ inGraph: AUGraph, _ outIsInitialized: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified AUGraphIsNodeSubGraph(AUGraph, AUNode, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphIsNodeSubGraph(_ inGraph: AUGraph, _ inNode: AUNode, _ outFlag: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphIsNodeSubGraph(_ inGraph: AUGraph, _ inNode: AUNode, _ outFlag: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.2 |

Modified AUGraphIsOpen(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphIsOpen(_ inGraph: AUGraph, _ outIsOpen: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphIsOpen(_ inGraph: AUGraph, _ outIsOpen: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified AUGraphIsRunning(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphIsRunning(_ inGraph: AUGraph, _ outIsRunning: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphIsRunning(_ inGraph: AUGraph, _ outIsRunning: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified AUGraphNewNodeSubGraph(AUGraph, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphNewNodeSubGraph(_ inGraph: AUGraph, _ outNode: UnsafePointer<AUNode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphNewNodeSubGraph(_ inGraph: AUGraph, _ outNode: UnsafeMutablePointer<AUNode>) -> OSStatus ``` | OS X 10.2 |

Modified AUGraphNodeInfo(AUGraph, AUNode, UnsafeMutablePointer<AudioComponentDescription>, UnsafeMutablePointer<AudioUnit>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphNodeInfo(_ inGraph: AUGraph, _ inNode: AUNode, _ outDescription: UnsafePointer<AudioComponentDescription>, _ outAudioUnit: UnsafePointer<AudioUnit>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphNodeInfo(_ inGraph: AUGraph, _ inNode: AUNode, _ outDescription: UnsafeMutablePointer<AudioComponentDescription>, _ outAudioUnit: UnsafeMutablePointer<AudioUnit>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphOpen(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphRemoveNode(AUGraph, AUNode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphRemoveRenderNotify(AUGraph, AURenderCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphRemoveRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphRemoveRenderNotify(_ inGraph: AUGraph, _ inCallback: AURenderCallback, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AUGraphSetNodeInputCallback(AUGraph, AUNode, UInt32, UnsafePointer<AURenderCallbackStruct>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphSetNodeInputCallback(_ inGraph: AUGraph, _ inDestNode: AUNode, _ inDestInputNumber: UInt32, _ inInputCallback: ConstUnsafePointer<AURenderCallbackStruct>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphSetNodeInputCallback(_ inGraph: AUGraph, _ inDestNode: AUNode, _ inDestInputNumber: UInt32, _ inInputCallback: UnsafePointer<AURenderCallbackStruct>) -> OSStatus ``` | OS X 10.5 |

Modified AUGraphStart(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphStop(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphUninitialize(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified AUGraphUpdate(AUGraph, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified AUListenerAddParameter(AUParameterListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUListenerAddParameter(_ inListener: AUParameterListener!, _ inObject: UnsafePointer<()>, _ inParameter: ConstUnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUListenerAddParameter(_ inListener: AUParameterListenerRef, _ inObject: UnsafeMutablePointer<Void>, _ inParameter: UnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.2 |

Modified AUListenerCreate(AUParameterListenerProc, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, Float32, UnsafeMutablePointer<AUParameterListenerRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUListenerCreate(_ inProc: AUParameterListenerProc, _ inUserData: UnsafePointer<()>, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inNotificationInterval: Float32, _ outListener: UnsafePointer<Unmanaged<AUParameterListener>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUListenerCreate(_ inProc: AUParameterListenerProc, _ inUserData: UnsafeMutablePointer<Void>, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inNotificationInterval: Float32, _ outListener: UnsafeMutablePointer<AUParameterListenerRef>) -> OSStatus ``` | OS X 10.2 |

Modified AUListenerCreateWithDispatchQueue(UnsafeMutablePointer<AUParameterListenerRef>, Float32, dispatch_queue_t!, AUParameterListenerBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUListenerCreateWithDispatchQueue(_ outListener: UnsafePointer<Unmanaged<AUParameterListener>?>, _ inNotificationInterval: Float32, _ inDispatchQueue: dispatch_queue_t!, _ inBlock: AUParameterListenerBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUListenerCreateWithDispatchQueue(_ outListener: UnsafeMutablePointer<AUParameterListenerRef>, _ inNotificationInterval: Float32, _ inDispatchQueue: dispatch_queue_t!, _ inBlock: AUParameterListenerBlock!) -> OSStatus ``` | OS X 10.6 |

Modified AUListenerDispose(AUParameterListenerRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUListenerDispose(_ inListener: AUParameterListener!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUListenerDispose(_ inListener: AUParameterListenerRef) -> OSStatus ``` | OS X 10.2 |

Modified AUListenerRemoveParameter(AUParameterListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUListenerRemoveParameter(_ inListener: AUParameterListener!, _ inObject: UnsafePointer<()>, _ inParameter: ConstUnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUListenerRemoveParameter(_ inListener: AUParameterListenerRef, _ inObject: UnsafeMutablePointer<Void>, _ inParameter: UnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.2 |

Modified AUParameterFormatValue(Float64, UnsafePointer<AudioUnitParameter>, UnsafeMutablePointer<Int8>, UInt32) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUParameterFormatValue(_ inParameterValue: Float64, _ inParameter: ConstUnsafePointer<AudioUnitParameter>, _ inTextBuffer: UnsafePointer<Int8>, _ inDigits: UInt32) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func AUParameterFormatValue(_ inParameterValue: Float64, _ inParameter: UnsafePointer<AudioUnitParameter>, _ inTextBuffer: UnsafeMutablePointer<Int8>, _ inDigits: UInt32) -> UnsafeMutablePointer<Int8> ``` | OS X 10.2 |

Modified AUParameterListenerBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AUParameterListenerBlock = (UnsafePointer<()>, ConstUnsafePointer<AudioUnitParameter>, AudioUnitParameterValue) -> Void ``` |
| To | ``` typealias AUParameterListenerBlock = (UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue) -> Void ``` |

Modified AUParameterListenerNotify(AUParameterListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUParameterListenerNotify(_ inSendingListener: AUParameterListener!, _ inSendingObject: UnsafePointer<()>, _ inParameter: ConstUnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUParameterListenerNotify(_ inSendingListener: AUParameterListenerRef, _ inSendingObject: UnsafeMutablePointer<Void>, _ inParameter: UnsafePointer<AudioUnitParameter>) -> OSStatus ``` | OS X 10.2 |

Modified AUParameterListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AUParameterListenerProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, ConstUnsafePointer<AudioUnitParameter>, AudioUnitParameterValue) -> Void)> ``` |
| To | ``` typealias AUParameterListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue) -> Void)> ``` |

Modified AUParameterListenerRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AUParameterListenerRef = AUParameterListener ``` |
| To | ``` typealias AUParameterListenerRef = COpaquePointer ``` |

Modified AUParameterSet(AUParameterListenerRef, UnsafeMutablePointer<Void>, UnsafePointer<AudioUnitParameter>, AudioUnitParameterValue, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUParameterSet(_ inSendingListener: AUParameterListener!, _ inSendingObject: UnsafePointer<()>, _ inParameter: ConstUnsafePointer<AudioUnitParameter>, _ inValue: AudioUnitParameterValue, _ inBufferOffsetInFrames: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AUParameterSet(_ inSendingListener: AUParameterListenerRef, _ inSendingObject: UnsafeMutablePointer<Void>, _ inParameter: UnsafePointer<AudioUnitParameter>, _ inValue: AudioUnitParameterValue, _ inBufferOffsetInFrames: UInt32) -> OSStatus ``` | OS X 10.2 |

Modified AUParameterValueFromLinear(Float32, UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUParameterValueFromLinear(_ inLinearValue: Float32, _ inParameter: ConstUnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue ``` | OS X 10.10 |
| To | ``` func AUParameterValueFromLinear(_ inLinearValue: Float32, _ inParameter: UnsafePointer<AudioUnitParameter>) -> AudioUnitParameterValue ``` | OS X 10.2 |

Modified AUParameterValueToLinear(AudioUnitParameterValue, UnsafePointer<AudioUnitParameter>) -> Float32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AUParameterValueToLinear(_ inParameterValue: AudioUnitParameterValue, _ inParameter: ConstUnsafePointer<AudioUnitParameter>) -> Float32 ``` | OS X 10.10 |
| To | ``` func AUParameterValueToLinear(_ inParameterValue: AudioUnitParameterValue, _ inParameter: UnsafePointer<AudioUnitParameter>) -> Float32 ``` | OS X 10.2 |

Modified AudioConverterComplexInputDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterComplexInputDataProc = CFunctionPointer<((AudioConverter!, UnsafePointer<UInt32>, UnsafePointer<AudioBufferList>, UnsafePointer<UnsafePointer<AudioStreamPacketDescription>>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterComplexInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioConverterConvertBuffer(AudioConverterRef, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverter!, _ inInputDataSize: UInt32, _ inInputData: ConstUnsafePointer<()>, _ ioOutputDataSize: UnsafePointer<UInt32>, _ outOutputData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataSize: UInt32, _ inInputData: UnsafePointer<Void>, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterConvertComplexBuffer(AudioConverterRef, UInt32, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterConvertComplexBuffer(_ inAudioConverter: AudioConverter!, _ inNumberPCMFrames: UInt32, _ inInputData: ConstUnsafePointer<AudioBufferList>, _ outOutputData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterConvertComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inNumberPCMFrames: UInt32, _ inInputData: UnsafePointer<AudioBufferList>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.7 |

Modified AudioConverterDispose(AudioConverterRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterDispose(_ inAudioConverter: AudioConverter!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterDispose(_ inAudioConverter: AudioConverterRef) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterFillComplexBuffer(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverter!, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafePointer<()>, _ ioOutputDataPacketSize: UnsafePointer<UInt32>, _ outOutputData: UnsafePointer<AudioBufferList>, _ outPacketDescription: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutablePointer<Void>, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.2 |

Modified AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterGetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterGetPropertyInfo(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterInputDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterInputDataProc = CFunctionPointer<((AudioConverter!, UnsafePointer<UInt32>, UnsafePointer<UnsafePointer<()>>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterNew(_ inSourceFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafePointer<Unmanaged<AudioConverter>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterNewSpecific(_ inSourceFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: ConstUnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafePointer<Unmanaged<AudioConverter>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef>) -> OSStatus ``` | OS X 10.4 |

Modified AudioConverterRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterRef = AudioConverter ``` |
| To | ``` typealias AudioConverterRef = COpaquePointer ``` |

Modified AudioConverterReset(AudioConverterRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterReset(_ inAudioConverter: AudioConverter!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterReset(_ inAudioConverter: AudioConverterRef) -> OSStatus ``` | OS X 10.1 |

Modified AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverter!, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioConverterSetProperty(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.1 |

Modified AudioFileClose(AudioFileID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified AudioFileComponentCloseFile(AudioFileComponent) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified AudioFileComponentCloseProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentCloseProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentCloseProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentCountUserData(AudioFileComponent, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentCountUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ outNumberItems: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentCountUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ outNumberItems: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentCountUserDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentCountUserDataProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentCountUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentCreate(AudioFileComponent, UnsafePointer<FSRef>, CFString!, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafeMutablePointer<FSRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentCreate(_ inComponent: AudioFileComponent, _ inParentRef: ConstUnsafePointer<FSRef>, _ inFileName: CFString!, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outNewFileRef: UnsafePointer<FSRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentCreate(_ inComponent: AudioFileComponent, _ inParentRef: UnsafePointer<FSRef>, _ inFileName: CFString!, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outNewFileRef: UnsafeMutablePointer<FSRef>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentCreateURL(AudioFileComponent, CFURL!, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentCreateURL(_ inComponent: AudioFileComponent, _ inFileRef: CFURL!, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentCreateURL(_ inComponent: AudioFileComponent, _ inFileRef: CFURL!, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileComponentCreateURLProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentCreateURLProc = CFunctionPointer<((UnsafePointer<()>, CFURL!, ConstUnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentCreateURLProc = CFunctionPointer<((UnsafeMutablePointer<Void>, CFURL!, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus)> ``` |

Modified AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString!, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentExtensionIsThisFormat(_ inComponent: AudioFileComponent, _ inExtension: CFString!, _ outResult: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentExtensionIsThisFormat(_ inComponent: AudioFileComponent, _ inExtension: CFString!, _ outResult: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentExtensionIsThisFormatProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentExtensionIsThisFormatProc = CFunctionPointer<((UnsafePointer<()>, CFString!, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentExtensionIsThisFormatProc = CFunctionPointer<((UnsafeMutablePointer<Void>, CFString!, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentFileDataIsThisFormat(_ inComponent: AudioFileComponent, _ inDataByteSize: UInt32, _ inData: ConstUnsafePointer<()>, _ outResult: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentFileDataIsThisFormat(_ inComponent: AudioFileComponent, _ inDataByteSize: UInt32, _ inData: UnsafePointer<Void>, _ outResult: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentFileDataIsThisFormatProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentFileDataIsThisFormatProc = CFunctionPointer<((UnsafePointer<()>, UInt32, ConstUnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentFileDataIsThisFormatProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetGlobalInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetGlobalInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetGlobalInfoProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetGlobalInfoProc = CFunctionPointer<((UnsafePointer<()>, AudioFileComponentPropertyID, UInt32, ConstUnsafePointer<()>, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetGlobalInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetGlobalInfoSize(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ outPropertySize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetGlobalInfoSize(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertySize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetGlobalInfoSizeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetGlobalInfoSizeProc = CFunctionPointer<((UnsafePointer<()>, AudioFileComponentPropertyID, UInt32, ConstUnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetGlobalInfoSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetPropertyInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ outPropertySize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetPropertyInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ outPropertySize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetPropertyInfoProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetPropertyInfoProc = CFunctionPointer<((UnsafePointer<()>, AudioFileComponentPropertyID, UnsafePointer<UInt32>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetPropertyInfoProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentGetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioFileComponentPropertyID, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafePointer<UInt32>, _ outUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetUserDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetUserDataProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentGetUserDataSize(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentGetUserDataSize(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentGetUserDataSize(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentGetUserDataSizeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentGetUserDataSizeProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentGetUserDataSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFileComponentInitialize(AudioFileComponent, UnsafePointer<FSRef>, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentInitialize(_ inComponent: AudioFileComponent, _ inFileRef: ConstUnsafePointer<FSRef>, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentInitialize(_ inComponent: AudioFileComponent, _ inFileRef: UnsafePointer<FSRef>, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentInitializeWithCallbacks(AudioFileComponent, UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentInitializeWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafePointer<()>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: UInt32, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentInitializeWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: UInt32, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentInitializeWithCallbacksProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentInitializeWithCallbacksProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, ConstUnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentInitializeWithCallbacksProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus)> ``` |

Modified AudioFileComponentOpenFile(AudioFileComponent, UnsafePointer<FSRef>, Int8, Int16) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentOpenFile(_ inComponent: AudioFileComponent, _ inFileRef: ConstUnsafePointer<FSRef>, _ inPermissions: Int8, _ inRefNum: Int16) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentOpenFile(_ inComponent: AudioFileComponent, _ inFileRef: UnsafePointer<FSRef>, _ inPermissions: Int8, _ inRefNum: Int16) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentOpenURL(AudioFileComponent, CFURL!, Int8, Int32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioFileComponentOpenURLProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentOpenURLProc = CFunctionPointer<((UnsafePointer<()>, CFURL!, Int8, Int32) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentOpenURLProc = CFunctionPointer<((UnsafeMutablePointer<Void>, CFURL!, Int8, Int32) -> OSStatus)> ``` |

Modified AudioFileComponentOpenWithCallbacks(AudioFileComponent, UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentOpenWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafePointer<()>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentOpenWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentOpenWithCallbacksProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentOpenWithCallbacksProc = CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentOpenWithCallbacksProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus)> ``` |

Modified AudioFileComponentOptimize(AudioFileComponent) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified AudioFileComponentOptimizeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentOptimizeProc = CFunctionPointer<((UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentOptimizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentReadBytes(AudioFileComponent, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentReadBytes(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentReadBytes(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentReadBytesProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentReadBytesProc = CFunctionPointer<((UnsafePointer<()>, Boolean, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentReadBytesProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentReadPacketData(AudioFileComponent, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentReadPacketData(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ ioNumBytes: UnsafePointer<UInt32>, _ outPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentReadPacketData(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentReadPacketDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentReadPacketDataProc = CFunctionPointer<((UnsafePointer<()>, Boolean, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentReadPacketDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentReadPackets(AudioFileComponent, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentReadPackets(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ outNumBytes: UnsafePointer<UInt32>, _ outPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentReadPackets(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentReadPacketsProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentReadPacketsProc = CFunctionPointer<((UnsafePointer<()>, Boolean, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentReadPacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentRemoveUserData(AudioFileComponent, UInt32, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioFileComponentRemoveUserDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentRemoveUserDataProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentRemoveUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32) -> OSStatus)> ``` |

Modified AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentSetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentSetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentSetPropertyProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentSetPropertyProc = CFunctionPointer<((UnsafePointer<()>, AudioFileComponentPropertyID, UInt32, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentSetPropertyProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileComponentPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentSetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentSetUserData(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentSetUserDataProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentSetUserDataProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UInt32, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentSetUserDataProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentWriteBytes(AudioFileComponent, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentWriteBytes(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafePointer<UInt32>, _ inBuffer: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentWriteBytes(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentWriteBytesProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentWriteBytesProc = CFunctionPointer<((UnsafePointer<()>, Boolean, Int64, UnsafePointer<UInt32>, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentWriteBytesProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileComponentWritePackets(AudioFileComponent, Boolean, UInt32, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileComponentWritePackets(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inNumBytes: UInt32, _ inPacketDescriptions: ConstUnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ inBuffer: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileComponentWritePackets(_ inComponent: AudioFileComponent, _ inUseCache: Boolean, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileComponentWritePacketsProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileComponentWritePacketsProc = CFunctionPointer<((UnsafePointer<()>, Boolean, UInt32, ConstUnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias AudioFileComponentWritePacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UInt32, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileCountUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ outNumberItems: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileCountUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ outNumberItems: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileCreateWithURL(CFURL!, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL!, _ inFileType: AudioFileTypeID, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafePointer<AudioFileID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL!, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileGetGlobalInfo(AudioFilePropertyID, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetGlobalInfo(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<()>, _ ioDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetGlobalInfo(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.3 |

Modified AudioFileGetGlobalInfoSize(AudioFilePropertyID, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetGlobalInfoSize(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<()>, _ outDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetGlobalInfoSize(_ inPropertyID: AudioFilePropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeMutablePointer<Void>, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified AudioFileGetProperty(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ ioDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFileGetPropertyInfo(AudioFileID, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetPropertyInfo(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ outDataSize: UnsafePointer<UInt32>, _ isWritable: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetPropertyInfo(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>, _ isWritable: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafePointer<UInt32>, _ outUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileGetUserDataSize(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileGetUserDataSize(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileInitializeWithCallbacks(UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafePointer<()>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafePointer<AudioFileID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` | OS X 10.3 |

Modified AudioFileOpenURL(CFURL!, Int8, AudioFileTypeID, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileOpenURL(_ inFileRef: CFURL!, _ inPermissions: Int8, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafePointer<AudioFileID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileOpenURL(_ inFileRef: CFURL!, _ inPermissions: Int8, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileOpenWithCallbacks(UnsafeMutablePointer<Void>, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafePointer<()>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafePointer<AudioFileID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` | OS X 10.3 |

Modified AudioFileOptimize(AudioFileID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified AudioFileReadBytes(AudioFileID, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFileReadPacketData(AudioFileID, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ ioNumBytes: UnsafePointer<UInt32>, _ outPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.6 |

Modified AudioFileReadPackets(AudioFileID, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ outNumBytes: UnsafePointer<UInt32>, _ outPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ outBuffer: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 | -- |
| To | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.2 | OS X 10.10 |

Modified AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioFileSetProperty(AudioFileID, AudioFilePropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileSetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ inDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileSetProperty(_ inAudioFile: AudioFileID, _ inPropertyID: AudioFilePropertyID, _ inDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileSetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileSetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inUserDataSize: UInt32, _ inUserData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified AudioFileStreamClose(AudioFileStreamID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioFileStreamGetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamGetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamGetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStreamGetPropertyInfo(AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStreamOpen(UnsafeMutablePointer<Void>, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamOpen(_ inClientData: UnsafePointer<()>, _ inPropertyListenerProc: AudioFileStream_PropertyListenerProc, _ inPacketsProc: AudioFileStream_PacketsProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFileStream: UnsafePointer<AudioFileStreamID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamOpen(_ inClientData: UnsafeMutablePointer<Void>, _ inPropertyListenerProc: AudioFileStream_PropertyListenerProc, _ inPacketsProc: AudioFileStream_PacketsProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFileStream: UnsafeMutablePointer<AudioFileStreamID>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStreamParseBytes(AudioFileStreamID, UInt32, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: ConstUnsafePointer<()>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafePointer<Void>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStreamSeek(AudioFileStreamID, Int64, UnsafeMutablePointer<Int64>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamSeek(_ inAudioFileStream: AudioFileStreamID, _ inPacketOffset: Int64, _ outDataByteOffset: UnsafePointer<Int64>, _ ioFlags: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamSeek(_ inAudioFileStream: AudioFileStreamID, _ inPacketOffset: Int64, _ outDataByteOffset: UnsafeMutablePointer<Int64>, _ ioFlags: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStreamSetProperty(AudioFileStreamID, AudioFileStreamPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileStreamSetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileStreamSetProperty(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioFileStream_PacketsProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PacketsProc = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, ConstUnsafePointer<()>, UnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |
| To | ``` typealias AudioFileStream_PacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> Void)> ``` |

Modified AudioFileStream_PropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PropertyListenerProc = CFunctionPointer<((UnsafePointer<()>, AudioFileStreamID, AudioFileStreamPropertyID, UnsafePointer<UInt32>) -> Void)> ``` |
| To | ``` typealias AudioFileStream_PropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>) -> Void)> ``` |

Modified AudioFileWriteBytes(AudioFileID, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafePointer<UInt32>, _ inBuffer: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFileWritePackets(AudioFileID, Boolean, UInt32, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inNumBytes: UInt32, _ inPacketDescriptions: ConstUnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafePointer<UInt32>, _ inBuffer: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified AudioFile_GetSizeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_GetSizeProc = CFunctionPointer<((UnsafePointer<()>) -> Int64)> ``` |
| To | ``` typealias AudioFile_GetSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Int64)> ``` |

Modified AudioFile_ReadProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_ReadProc = CFunctionPointer<((UnsafePointer<()>, Int64, UInt32, UnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_ReadProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFile_SetSizeProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_SetSizeProc = CFunctionPointer<((UnsafePointer<()>, Int64) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_SetSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64) -> OSStatus)> ``` |

Modified AudioFile_WriteProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_WriteProc = CFunctionPointer<((UnsafePointer<()>, Int64, UInt32, ConstUnsafePointer<()>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_WriteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified AudioFormatGetProperty(AudioFormatPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFormatGetProperty(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFormatGetProperty(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.3 |

Modified AudioFormatGetPropertyInfo(AudioFormatPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioFormatGetPropertyInfo(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ outPropertyDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioFormatGetPropertyInfo(_ inPropertyID: AudioFormatPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified AudioHardwareServiceAddPropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceAddPropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioHardwareServiceGetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ ioDataSize: UnsafePointer<UInt32>, _ outData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceGetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>, _ outData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioHardwareServiceGetPropertyDataSize(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ outDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceGetPropertyDataSize(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AudioHardwareServiceHasProperty(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceHasProperty(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>) -> Boolean ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceHasProperty(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>) -> Boolean ``` | OS X 10.5 |

Modified AudioHardwareServiceIsPropertySettable(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified AudioHardwareServiceRemovePropertyListener(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, AudioObjectPropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceRemovePropertyListener(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inListener: AudioObjectPropertyListenerProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioHardwareServiceSetPropertyData(AudioObjectID, UnsafePointer<AudioObjectPropertyAddress>, UInt32, UnsafePointer<Void>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioHardwareServiceSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: ConstUnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: ConstUnsafePointer<()>, _ inDataSize: UInt32, _ inData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioHardwareServiceSetPropertyData(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inQualifierDataSize: UInt32, _ inQualifierData: UnsafePointer<Void>, _ inDataSize: UInt32, _ inData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueAddPropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueAllocateBuffer(AudioQueueRef, UInt32, UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueue!, _ inBufferByteSize: UInt32, _ outBuffer: UnsafePointer<AudioQueueBufferRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueAllocateBuffer(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueAllocateBufferWithPacketDescriptions(AudioQueueRef, UInt32, UInt32, UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueue!, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafePointer<AudioQueueBufferRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueAllocateBufferWithPacketDescriptions(_ inAQ: AudioQueueRef, _ inBufferByteSize: UInt32, _ inNumberPacketDescriptions: UInt32, _ outBuffer: UnsafeMutablePointer<AudioQueueBufferRef>) -> OSStatus ``` | OS X 10.6 |

Modified AudioQueueBufferRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueBufferRef = UnsafePointer<AudioQueueBuffer> ``` |
| To | ``` typealias AudioQueueBufferRef = UnsafeMutablePointer<AudioQueueBuffer> ``` |

Modified AudioQueueCreateTimeline(AudioQueueRef, UnsafeMutablePointer<AudioQueueTimelineRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueue!, _ outTimeline: UnsafePointer<Unmanaged<AudioQueueTimeline>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueCreateTimeline(_ inAQ: AudioQueueRef, _ outTimeline: UnsafeMutablePointer<AudioQueueTimelineRef>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueDeviceGetCurrentTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceGetCurrentTime(_ inAQ: AudioQueue!, _ outTimeStamp: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueDeviceGetCurrentTime(_ inAQ: AudioQueueRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueDeviceGetNearestStartTime(AudioQueueRef, UnsafeMutablePointer<AudioTimeStamp>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceGetNearestStartTime(_ inAQ: AudioQueue!, _ ioRequestedStartTime: UnsafePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueDeviceGetNearestStartTime(_ inAQ: AudioQueueRef, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueDeviceTranslateTime(AudioQueueRef, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDeviceTranslateTime(_ inAQ: AudioQueue!, _ inTime: ConstUnsafePointer<AudioTimeStamp>, _ outTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueDeviceTranslateTime(_ inAQ: AudioQueueRef, _ inTime: UnsafePointer<AudioTimeStamp>, _ outTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueDispose(AudioQueueRef, Boolean) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDispose(_ inAQ: AudioQueue!, _ inImmediate: Boolean) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueDispose(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueDisposeTimeline(AudioQueueRef, AudioQueueTimelineRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueDisposeTimeline(_ inAQ: AudioQueue!, _ inTimeline: AudioQueueTimeline!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueDisposeTimeline(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueEnqueueBuffer(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: ConstUnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueEnqueueBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueEnqueueBufferWithParameters(AudioQueueRef, AudioQueueBufferRef, UInt32, UnsafePointer<AudioStreamPacketDescription>, UInt32, UInt32, UInt32, UnsafePointer<AudioQueueParameterEvent>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: ConstUnsafePointer<AudioStreamPacketDescription>, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: ConstUnsafePointer<AudioQueueParameterEvent>, _ inStartTime: ConstUnsafePointer<AudioTimeStamp>, _ outActualStartTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueEnqueueBufferWithParameters(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef, _ inNumPacketDescs: UInt32, _ inPacketDescs: UnsafePointer<AudioStreamPacketDescription>, _ inTrimFramesAtStart: UInt32, _ inTrimFramesAtEnd: UInt32, _ inNumParamValues: UInt32, _ inParamValues: UnsafePointer<AudioQueueParameterEvent>, _ inStartTime: UnsafePointer<AudioTimeStamp>, _ outActualStartTime: UnsafeMutablePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueFlush(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueFlush(_ inAQ: AudioQueue!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueFlush(_ inAQ: AudioQueueRef) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueFreeBuffer(AudioQueueRef, AudioQueueBufferRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueFreeBuffer(_ inAQ: AudioQueue!, _ inBuffer: AudioQueueBufferRef) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueFreeBuffer(_ inAQ: AudioQueueRef, _ inBuffer: AudioQueueBufferRef) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueGetCurrentTime(AudioQueueRef, AudioQueueTimelineRef, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueue!, _ inTimeline: AudioQueueTimeline!, _ outTimeStamp: UnsafePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueGetParameter(AudioQueueRef, AudioQueueParameterID, UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetParameter(_ inAQ: AudioQueue!, _ inParamID: AudioQueueParameterID, _ outValue: UnsafePointer<AudioQueueParameterValue>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueGetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ outValue: UnsafeMutablePointer<AudioQueueParameterValue>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueGetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetProperty(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ outData: UnsafePointer<()>, _ ioDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueGetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutablePointer<Void>, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueGetPropertySize(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ outDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueGetPropertySize(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueInputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueInputCallback = CFunctionPointer<((UnsafePointer<()>, AudioQueue!, AudioQueueBufferRef, ConstUnsafePointer<AudioTimeStamp>, UInt32, ConstUnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |
| To | ``` typealias AudioQueueInputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |

Modified AudioQueueInputCallbackBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueInputCallbackBlock = (AudioQueue!, AudioQueueBufferRef, ConstUnsafePointer<AudioTimeStamp>, UInt32, ConstUnsafePointer<AudioStreamPacketDescription>) -> Void ``` |
| To | ``` typealias AudioQueueInputCallbackBlock = (AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void ``` |

Modified AudioQueueNewInput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueInputCallback, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, UInt32, UnsafeMutablePointer<AudioQueueRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewInput(_ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafePointer<()>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafePointer<Unmanaged<AudioQueue>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueNewInputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t!, AudioQueueInputCallbackBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewInputWithDispatchQueue(_ outAQ: UnsafePointer<Unmanaged<AudioQueue>?>, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ inCallbackDispatchQueue: dispatch_queue_t!, _ inCallbackBlock: AudioQueueInputCallbackBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueNewInputWithDispatchQueue(_ outAQ: UnsafeMutablePointer<AudioQueueRef>, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ inCallbackDispatchQueue: dispatch_queue_t!, _ inCallbackBlock: AudioQueueInputCallbackBlock!) -> OSStatus ``` | OS X 10.6 |

Modified AudioQueueNewOutput(UnsafePointer<AudioStreamBasicDescription>, AudioQueueOutputCallback, UnsafeMutablePointer<Void>, CFRunLoop!, CFString!, UInt32, UnsafeMutablePointer<AudioQueueRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewOutput(_ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafePointer<()>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafePointer<Unmanaged<AudioQueue>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueNewOutputWithDispatchQueue(UnsafeMutablePointer<AudioQueueRef>, UnsafePointer<AudioStreamBasicDescription>, UInt32, dispatch_queue_t!, AudioQueueOutputCallbackBlock!) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueNewOutputWithDispatchQueue(_ outAQ: UnsafePointer<Unmanaged<AudioQueue>?>, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ inCallbackDispatchQueue: dispatch_queue_t!, _ inCallbackBlock: AudioQueueOutputCallbackBlock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueNewOutputWithDispatchQueue(_ outAQ: UnsafeMutablePointer<AudioQueueRef>, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ inCallbackDispatchQueue: dispatch_queue_t!, _ inCallbackBlock: AudioQueueOutputCallbackBlock!) -> OSStatus ``` | OS X 10.6 |

Modified AudioQueueOfflineRender(AudioQueueRef, UnsafePointer<AudioTimeStamp>, AudioQueueBufferRef, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueOfflineRender(_ inAQ: AudioQueue!, _ inTimestamp: ConstUnsafePointer<AudioTimeStamp>, _ ioBuffer: AudioQueueBufferRef, _ inNumberFrames: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueOfflineRender(_ inAQ: AudioQueueRef, _ inTimestamp: UnsafePointer<AudioTimeStamp>, _ ioBuffer: AudioQueueBufferRef, _ inNumberFrames: UInt32) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueOutputCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueOutputCallback = CFunctionPointer<((UnsafePointer<()>, AudioQueue!, AudioQueueBufferRef) -> Void)> ``` |
| To | ``` typealias AudioQueueOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef) -> Void)> ``` |

Modified AudioQueueOutputCallbackBlock

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueOutputCallbackBlock = (AudioQueue!, AudioQueueBufferRef) -> Void ``` |
| To | ``` typealias AudioQueueOutputCallbackBlock = (AudioQueueRef, AudioQueueBufferRef) -> Void ``` |

Modified AudioQueuePause(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueuePause(_ inAQ: AudioQueue!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueuePause(_ inAQ: AudioQueueRef) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueuePrime(AudioQueueRef, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueuePrime(_ inAQ: AudioQueue!, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueuePrime(_ inAQ: AudioQueueRef, _ inNumberOfFramesToPrepare: UInt32, _ outNumberOfFramesPrepared: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueProcessingTapCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapCallback = CFunctionPointer<((UnsafePointer<()>, AudioQueueProcessingTap!, UInt32, UnsafePointer<AudioTimeStamp>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, UnsafePointer<AudioBufferList>) -> Void)> ``` |
| To | ``` typealias AudioQueueProcessingTapCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void)> ``` |

Modified AudioQueueProcessingTapDispose(AudioQueueProcessingTapRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapDispose(_ inAQTap: AudioQueueProcessingTap!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueProcessingTapDispose(_ inAQTap: AudioQueueProcessingTapRef) -> OSStatus ``` | OS X 10.7 |

Modified AudioQueueProcessingTapGetQueueTime(AudioQueueProcessingTapRef, UnsafeMutablePointer<Float64>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapGetQueueTime(_ inAQTap: AudioQueueProcessingTap!, _ outQueueSampleTime: UnsafePointer<Float64>, _ outQueueFrameCount: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueProcessingTapGetQueueTime(_ inAQTap: AudioQueueProcessingTapRef, _ outQueueSampleTime: UnsafeMutablePointer<Float64>, _ outQueueFrameCount: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.8 |

Modified AudioQueueProcessingTapGetSourceAudio(AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTap!, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafePointer<AudioTimeStamp>, _ outFlags: UnsafePointer<UInt32>, _ outNumberFrames: UnsafePointer<UInt32>, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTapRef, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<UInt32>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.7 |

Modified AudioQueueProcessingTapNew(AudioQueueRef, AudioQueueProcessingTapCallback, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueue!, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafePointer<()>, _ inFlags: UInt32, _ outMaxFrames: UnsafePointer<UInt32>, _ outProcessingFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafePointer<Unmanaged<AudioQueueProcessingTap>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: UInt32, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus ``` | OS X 10.7 |

Modified AudioQueueProcessingTapRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapRef = AudioQueueProcessingTap ``` |
| To | ``` typealias AudioQueueProcessingTapRef = COpaquePointer ``` |

Modified AudioQueuePropertyListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueuePropertyListenerProc = CFunctionPointer<((UnsafePointer<()>, AudioQueue!, AudioQueuePropertyID) -> Void)> ``` |
| To | ``` typealias AudioQueuePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueuePropertyID) -> Void)> ``` |

Modified AudioQueueRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueRef = AudioQueue ``` |
| To | ``` typealias AudioQueueRef = COpaquePointer ``` |

Modified AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueRemovePropertyListener(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inProc: AudioQueuePropertyListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueReset(AudioQueueRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueReset(_ inAQ: AudioQueue!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueReset(_ inAQ: AudioQueueRef) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueSetOfflineRenderFormat(AudioQueueRef, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueue!, _ inFormat: ConstUnsafePointer<AudioStreamBasicDescription>, _ inLayout: ConstUnsafePointer<AudioChannelLayout>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueSetOfflineRenderFormat(_ inAQ: AudioQueueRef, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inLayout: UnsafePointer<AudioChannelLayout>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueSetParameter(AudioQueueRef, AudioQueueParameterID, AudioQueueParameterValue) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetParameter(_ inAQ: AudioQueue!, _ inParamID: AudioQueueParameterID, _ inValue: AudioQueueParameterValue) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueSetParameter(_ inAQ: AudioQueueRef, _ inParamID: AudioQueueParameterID, _ inValue: AudioQueueParameterValue) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueSetProperty(_ inAQ: AudioQueue!, _ inID: AudioQueuePropertyID, _ inData: ConstUnsafePointer<()>, _ inDataSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueSetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ inData: UnsafePointer<Void>, _ inDataSize: UInt32) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueStart(AudioQueueRef, UnsafePointer<AudioTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueStart(_ inAQ: AudioQueue!, _ inStartTime: ConstUnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueStart(_ inAQ: AudioQueueRef, _ inStartTime: UnsafePointer<AudioTimeStamp>) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueStop(AudioQueueRef, Boolean) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioQueueStop(_ inAQ: AudioQueue!, _ inImmediate: Boolean) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioQueueStop(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` | OS X 10.5 |

Modified AudioQueueTimelineRef

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueTimelineRef = AudioQueueTimeline ``` |
| To | ``` typealias AudioQueueTimelineRef = COpaquePointer ``` |

Modified AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop!, CFString!, AudioServicesSystemSoundCompletionProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inCompletionRoutine: AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inCompletionRoutine: AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioServicesCreateSystemSoundID(CFURL!, UnsafeMutablePointer<SystemSoundID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioServicesCreateSystemSoundID(_ inFileURL: CFURL!, _ outSystemSoundID: UnsafePointer<SystemSoundID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioServicesCreateSystemSoundID(_ inFileURL: CFURL!, _ outSystemSoundID: UnsafeMutablePointer<SystemSoundID>) -> OSStatus ``` | OS X 10.5 |

Modified AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioServicesGetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioServicesGetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ outPropertyDataSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified AudioServicesPlayAlertSound(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioServicesPlaySystemSound(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioServicesRemoveSystemSoundCompletion(SystemSoundID)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafePointer<Void>, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func AudioServicesSetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: ConstUnsafePointer<()>, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func AudioServicesSetProperty(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.5 |

Modified AudioServicesSystemSoundCompletionProc

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioServicesSystemSoundCompletionProc = CFunctionPointer<((SystemSoundID, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias AudioServicesSystemSoundCompletionProc = CFunctionPointer<((SystemSoundID, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CAClockAddListener(CAClockRef, CAClockListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockAddListener(_ inCAClock: CAClock!, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockAddListener(_ inCAClock: CAClockRef, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockArm(CAClockRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockArm(_ inCAClock: CAClock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockArm(_ inCAClock: CAClockRef) -> OSStatus ``` | OS X 10.4 |

Modified CAClockBarBeatTimeToBeats(CAClockRef, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<CAClockBeats>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockBarBeatTimeToBeats(_ inCAClock: CAClock!, _ inBarBeatTime: ConstUnsafePointer<CABarBeatTime>, _ outBeats: UnsafePointer<CAClockBeats>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockBarBeatTimeToBeats(_ inCAClock: CAClockRef, _ inBarBeatTime: UnsafePointer<CABarBeatTime>, _ outBeats: UnsafeMutablePointer<CAClockBeats>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockBeatsToBarBeatTime(CAClockRef, CAClockBeats, UInt16, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockBeatsToBarBeatTime(_ inCAClock: CAClock!, _ inBeats: CAClockBeats, _ inSubbeatDivisor: UInt16, _ outBarBeatTime: UnsafePointer<CABarBeatTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockBeatsToBarBeatTime(_ inCAClock: CAClockRef, _ inBeats: CAClockBeats, _ inSubbeatDivisor: UInt16, _ outBarBeatTime: UnsafeMutablePointer<CABarBeatTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockDisarm(CAClockRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockDisarm(_ inCAClock: CAClock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockDisarm(_ inCAClock: CAClockRef) -> OSStatus ``` | OS X 10.4 |

Modified CAClockDispose(CAClockRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockDispose(_ inCAClock: CAClock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockDispose(_ inCAClock: CAClockRef) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetCurrentTempo(CAClockRef, UnsafeMutablePointer<CAClockTempo>, UnsafeMutablePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetCurrentTempo(_ inCAClock: CAClock!, _ outTempo: UnsafePointer<CAClockTempo>, _ outTimestamp: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetCurrentTempo(_ inCAClock: CAClockRef, _ outTempo: UnsafeMutablePointer<CAClockTempo>, _ outTimestamp: UnsafeMutablePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetCurrentTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetCurrentTime(_ inCAClock: CAClock!, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetCurrentTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetPlayRate(CAClockRef, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetPlayRate(_ inCAClock: CAClock!, _ outPlayRate: UnsafePointer<Float64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetPlayRate(_ inCAClock: CAClockRef, _ outPlayRate: UnsafeMutablePointer<Float64>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetProperty(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetProperty(_ inCAClock: CAClock!, _ inPropertyID: CAClockPropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetPropertyInfo(CAClockRef, CAClockPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetPropertyInfo(_ inCAClock: CAClock!, _ inPropertyID: CAClockPropertyID, _ outSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetPropertyInfo(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockGetStartTime(CAClockRef, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockGetStartTime(_ inCAClock: CAClock!, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockGetStartTime(_ inCAClock: CAClockRef, _ inTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockListenerProc

|  | Declaration |
| --- | --- |
| From | ``` typealias CAClockListenerProc = CFunctionPointer<((UnsafePointer<()>, CAClockMessage, ConstUnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CAClockListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, CAClockMessage, UnsafePointer<Void>) -> Void)> ``` |

Modified CAClockNew(UInt32, UnsafeMutablePointer<CAClockRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockNew(_ inReservedFlags: UInt32, _ outCAClock: UnsafePointer<Unmanaged<CAClock>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockNew(_ inReservedFlags: UInt32, _ outCAClock: UnsafeMutablePointer<CAClockRef>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockParseMIDI(CAClockRef, UnsafePointer<MIDIPacketList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockParseMIDI(_ inCAClock: CAClock!, _ inMIDIPacketList: ConstUnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockParseMIDI(_ inCAClock: CAClockRef, _ inMIDIPacketList: UnsafePointer<MIDIPacketList>) -> OSStatus ``` | OS X 10.5 |

Modified CAClockRef

|  | Declaration |
| --- | --- |
| From | ``` typealias CAClockRef = CAClock ``` |
| To | ``` typealias CAClockRef = COpaquePointer ``` |

Modified CAClockRemoveListener(CAClockRef, CAClockListenerProc, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockRemoveListener(_ inCAClock: CAClock!, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockRemoveListener(_ inCAClock: CAClockRef, _ inListenerProc: CAClockListenerProc, _ inUserData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSMPTETimeToSeconds(CAClockRef, UnsafePointer<SMPTETime>, UnsafeMutablePointer<CAClockSeconds>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSMPTETimeToSeconds(_ inCAClock: CAClock!, _ inSMPTETime: ConstUnsafePointer<SMPTETime>, _ outSeconds: UnsafePointer<CAClockSeconds>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSMPTETimeToSeconds(_ inCAClock: CAClockRef, _ inSMPTETime: UnsafePointer<SMPTETime>, _ outSeconds: UnsafeMutablePointer<CAClockSeconds>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSecondsToSMPTETime(CAClockRef, CAClockSeconds, UInt16, UnsafeMutablePointer<SMPTETime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSecondsToSMPTETime(_ inCAClock: CAClock!, _ inSeconds: CAClockSeconds, _ inSubframeDivisor: UInt16, _ outSMPTETime: UnsafePointer<SMPTETime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSecondsToSMPTETime(_ inCAClock: CAClockRef, _ inSeconds: CAClockSeconds, _ inSubframeDivisor: UInt16, _ outSMPTETime: UnsafeMutablePointer<SMPTETime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSetCurrentTempo(CAClockRef, CAClockTempo, UnsafePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSetCurrentTempo(_ inCAClock: CAClock!, _ inTempo: CAClockTempo, _ inTimestamp: ConstUnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSetCurrentTempo(_ inCAClock: CAClockRef, _ inTempo: CAClockTempo, _ inTimestamp: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSetCurrentTime(CAClockRef, UnsafePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSetCurrentTime(_ inCAClock: CAClock!, _ inTime: ConstUnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSetCurrentTime(_ inCAClock: CAClockRef, _ inTime: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSetPlayRate(CAClockRef, Float64) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSetPlayRate(_ inCAClock: CAClock!, _ inPlayRate: Float64) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSetPlayRate(_ inCAClock: CAClockRef, _ inPlayRate: Float64) -> OSStatus ``` | OS X 10.4 |

Modified CAClockSetProperty(CAClockRef, CAClockPropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockSetProperty(_ inCAClock: CAClock!, _ inPropertyID: CAClockPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockSetProperty(_ inCAClock: CAClockRef, _ inPropertyID: CAClockPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified CAClockStart(CAClockRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockStart(_ inCAClock: CAClock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockStart(_ inCAClock: CAClockRef) -> OSStatus ``` | OS X 10.4 |

Modified CAClockStop(CAClockRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockStop(_ inCAClock: CAClock!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockStop(_ inCAClock: CAClockRef) -> OSStatus ``` | OS X 10.4 |

Modified CAClockTranslateTime(CAClockRef, UnsafePointer<CAClockTime>, CAClockTimeFormat, UnsafeMutablePointer<CAClockTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAClockTranslateTime(_ inCAClock: CAClock!, _ inTime: ConstUnsafePointer<CAClockTime>, _ inOutputTimeFormat: CAClockTimeFormat, _ outTime: UnsafePointer<CAClockTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CAClockTranslateTime(_ inCAClock: CAClockRef, _ inTime: UnsafePointer<CAClockTime>, _ inOutputTimeFormat: CAClockTimeFormat, _ outTime: UnsafeMutablePointer<CAClockTime>) -> OSStatus ``` | OS X 10.4 |

Modified CAShow(UnsafeMutablePointer<Void>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAShow(_ inObject: UnsafePointer<()>) ``` | OS X 10.10 |
| To | ``` func CAShow(_ inObject: UnsafeMutablePointer<Void>) ``` | OS X 10.2 |

Modified CAShowFile(UnsafeMutablePointer<Void>, UnsafeMutablePointer<FILE>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CAShowFile(_ inObject: UnsafePointer<()>, _ inFile: UnsafePointer<FILE>) ``` | OS X 10.10 |
| To | ``` func CAShowFile(_ inObject: UnsafeMutablePointer<Void>, _ inFile: UnsafeMutablePointer<FILE>) ``` | OS X 10.2 |

Modified CopyInstrumentInfoFromSoundBank(CFURL!, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyInstrumentInfoFromSoundBank(_ inURL: CFURL!, _ outInstrumentInfo: UnsafePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CopyInstrumentInfoFromSoundBank(_ inURL: CFURL!, _ outInstrumentInfo: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` | OS X 10.8 |

Modified CopyNameFromSoundBank(CFURL!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CopyNameFromSoundBank(_ inURL: CFURL!, _ outName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func CopyNameFromSoundBank(_ inURL: CFURL!, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.5 |

Modified CountUserDataFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias CountUserDataFDF = CFunctionPointer<((UnsafePointer<()>, UInt32, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias CountUserDataFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified DisposeAUGraph(AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeMusicEventIterator(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeMusicPlayer(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified DisposeMusicSequence(MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified ExtAudioFileCreateWithURL(CFURL!, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioChannelLayout>, UInt32, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL!, _ inFileType: AudioFileTypeID, _ inStreamDesc: ConstUnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: ConstUnsafePointer<AudioChannelLayout>, _ inFlags: UInt32, _ outExtAudioFile: UnsafePointer<Unmanaged<ExtAudioFile>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL!, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` | OS X 10.5 |

Modified ExtAudioFileDispose(ExtAudioFileRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileDispose(_ inExtAudioFile: ExtAudioFile!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileDispose(_ inExtAudioFile: ExtAudioFileRef) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileGetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileGetProperty(_ inExtAudioFile: ExtAudioFile!, _ inPropertyID: ExtAudioFilePropertyID, _ ioPropertyDataSize: UnsafePointer<UInt32>, _ outPropertyData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileGetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileGetPropertyInfo(ExtAudioFileRef, ExtAudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFile!, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafePointer<UInt32>, _ outWritable: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileOpenURL(CFURL!, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileOpenURL(_ inURL: CFURL!, _ outExtAudioFile: UnsafePointer<Unmanaged<ExtAudioFile>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileOpenURL(_ inURL: CFURL!, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` | OS X 10.5 |

Modified ExtAudioFileRead(ExtAudioFileRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileRead(_ inExtAudioFile: ExtAudioFile!, _ ioNumberFrames: UnsafePointer<UInt32>, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileRead(_ inExtAudioFile: ExtAudioFileRef, _ ioNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileRef

|  | Declaration |
| --- | --- |
| From | ``` typealias ExtAudioFileRef = ExtAudioFile ``` |
| To | ``` typealias ExtAudioFileRef = COpaquePointer ``` |

Modified ExtAudioFileSeek(ExtAudioFileRef, Int64) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileSeek(_ inExtAudioFile: ExtAudioFile!, _ inFrameOffset: Int64) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileSeek(_ inExtAudioFile: ExtAudioFileRef, _ inFrameOffset: Int64) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileSetProperty(ExtAudioFileRef, ExtAudioFilePropertyID, UInt32, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileSetProperty(_ inExtAudioFile: ExtAudioFile!, _ inPropertyID: ExtAudioFilePropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileSetProperty(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileTell(ExtAudioFileRef, UnsafeMutablePointer<Int64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileTell(_ inExtAudioFile: ExtAudioFile!, _ outFrameOffset: UnsafePointer<Int64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileTell(_ inExtAudioFile: ExtAudioFileRef, _ outFrameOffset: UnsafeMutablePointer<Int64>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileWrapAudioFileID(AudioFileID, Boolean, UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Boolean, _ outExtAudioFile: UnsafePointer<Unmanaged<ExtAudioFile>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Boolean, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileWrite(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileWrite(_ inExtAudioFile: ExtAudioFile!, _ inNumberFrames: UInt32, _ ioData: ConstUnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileWrite(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.4 |

Modified ExtAudioFileWriteAsync(ExtAudioFileRef, UInt32, UnsafePointer<AudioBufferList>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ExtAudioFileWriteAsync(_ inExtAudioFile: ExtAudioFile!, _ inNumberFrames: UInt32, _ ioData: ConstUnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func ExtAudioFileWriteAsync(_ inExtAudioFile: ExtAudioFileRef, _ inNumberFrames: UInt32, _ ioData: UnsafePointer<AudioBufferList>) -> OSStatus ``` | OS X 10.4 |

Modified GetPropertyFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias GetPropertyFDF = CFunctionPointer<((UnsafePointer<()>, AudioFilePropertyID, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias GetPropertyFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified GetPropertyInfoFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias GetPropertyInfoFDF = CFunctionPointer<((UnsafePointer<()>, AudioFilePropertyID, UnsafePointer<UInt32>, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias GetPropertyInfoFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified GetUserDataFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias GetUserDataFDF = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias GetUserDataFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified GetUserDataSizeFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias GetUserDataSizeFDF = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UnsafePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias GetUserDataSizeFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |

Modified MusicEventIteratorDeleteEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicEventIteratorGetEventInfo(MusicEventIterator, UnsafeMutablePointer<MusicTimeStamp>, UnsafeMutablePointer<MusicEventType>, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicEventIteratorGetEventInfo(_ inIterator: MusicEventIterator, _ outTimeStamp: UnsafePointer<MusicTimeStamp>, _ outEventType: UnsafePointer<MusicEventType>, _ outEventData: UnsafePointer<ConstUnsafePointer<()>>, _ outEventDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicEventIteratorGetEventInfo(_ inIterator: MusicEventIterator, _ outTimeStamp: UnsafeMutablePointer<MusicTimeStamp>, _ outEventType: UnsafeMutablePointer<MusicEventType>, _ outEventData: UnsafeMutablePointer<UnsafePointer<Void>>, _ outEventDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified MusicEventIteratorHasCurrentEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicEventIteratorHasCurrentEvent(_ inIterator: MusicEventIterator, _ outHasCurEvent: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicEventIteratorHasCurrentEvent(_ inIterator: MusicEventIterator, _ outHasCurEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.2 |

Modified MusicEventIteratorHasNextEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicEventIteratorHasNextEvent(_ inIterator: MusicEventIterator, _ outHasNextEvent: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicEventIteratorHasNextEvent(_ inIterator: MusicEventIterator, _ outHasNextEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified MusicEventIteratorHasPreviousEvent(MusicEventIterator, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicEventIteratorHasPreviousEvent(_ inIterator: MusicEventIterator, _ outHasPrevEvent: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicEventIteratorHasPreviousEvent(_ inIterator: MusicEventIterator, _ outHasPrevEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.0 |

Modified MusicEventIteratorNextEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicEventIteratorPreviousEvent(MusicEventIterator) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicEventIteratorSeek(MusicEventIterator, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicEventIteratorSetEventInfo(MusicEventIterator, MusicEventType, UnsafePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicEventIteratorSetEventInfo(_ inIterator: MusicEventIterator, _ inEventType: MusicEventType, _ inEventData: ConstUnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicEventIteratorSetEventInfo(_ inIterator: MusicEventIterator, _ inEventType: MusicEventType, _ inEventData: UnsafePointer<Void>) -> OSStatus ``` | OS X 10.2 |

Modified MusicEventIteratorSetEventTime(MusicEventIterator, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicPlayerGetBeatsForHostTime(MusicPlayer, UInt64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerGetBeatsForHostTime(_ inPlayer: MusicPlayer, _ inHostTime: UInt64, _ outBeats: UnsafePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerGetBeatsForHostTime(_ inPlayer: MusicPlayer, _ inHostTime: UInt64, _ outBeats: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.2 |

Modified MusicPlayerGetHostTimeForBeats(MusicPlayer, MusicTimeStamp, UnsafeMutablePointer<UInt64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerGetHostTimeForBeats(_ inPlayer: MusicPlayer, _ inBeats: MusicTimeStamp, _ outHostTime: UnsafePointer<UInt64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerGetHostTimeForBeats(_ inPlayer: MusicPlayer, _ inBeats: MusicTimeStamp, _ outHostTime: UnsafeMutablePointer<UInt64>) -> OSStatus ``` | OS X 10.2 |

Modified MusicPlayerGetPlayRateScalar(MusicPlayer, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerGetPlayRateScalar(_ inPlayer: MusicPlayer, _ outScaleRate: UnsafePointer<Float64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerGetPlayRateScalar(_ inPlayer: MusicPlayer, _ outScaleRate: UnsafeMutablePointer<Float64>) -> OSStatus ``` | OS X 10.3 |

Modified MusicPlayerGetSequence(MusicPlayer, UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerGetSequence(_ inPlayer: MusicPlayer, _ outSequence: UnsafePointer<MusicSequence>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerGetSequence(_ inPlayer: MusicPlayer, _ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` | OS X 10.3 |

Modified MusicPlayerGetTime(MusicPlayer, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerGetTime(_ inPlayer: MusicPlayer, _ outTime: UnsafePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerGetTime(_ inPlayer: MusicPlayer, _ outTime: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.0 |

Modified MusicPlayerIsPlaying(MusicPlayer, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicPlayerIsPlaying(_ inPlayer: MusicPlayer, _ outIsPlaying: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicPlayerIsPlaying(_ inPlayer: MusicPlayer, _ outIsPlaying: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.2 |

Modified MusicPlayerPreroll(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicPlayerSetPlayRateScalar(MusicPlayer, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified MusicPlayerSetSequence(MusicPlayer, MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicPlayerSetTime(MusicPlayer, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicPlayerStart(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicPlayerStop(MusicPlayer) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicSequenceBarBeatTimeToBeats(MusicSequence, UnsafePointer<CABarBeatTime>, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceBarBeatTimeToBeats(_ inSequence: MusicSequence, _ inBarBeatTime: ConstUnsafePointer<CABarBeatTime>, _ outBeats: UnsafePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceBarBeatTimeToBeats(_ inSequence: MusicSequence, _ inBarBeatTime: UnsafePointer<CABarBeatTime>, _ outBeats: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.5 |

Modified MusicSequenceBeatsToBarBeatTime(MusicSequence, MusicTimeStamp, UInt32, UnsafeMutablePointer<CABarBeatTime>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceBeatsToBarBeatTime(_ inSequence: MusicSequence, _ inBeats: MusicTimeStamp, _ inSubbeatDivisor: UInt32, _ outBarBeatTime: UnsafePointer<CABarBeatTime>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceBeatsToBarBeatTime(_ inSequence: MusicSequence, _ inBeats: MusicTimeStamp, _ inSubbeatDivisor: UInt32, _ outBarBeatTime: UnsafeMutablePointer<CABarBeatTime>) -> OSStatus ``` | OS X 10.5 |

Modified MusicSequenceDisposeTrack(MusicSequence, MusicTrack) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicSequenceFileCreate(MusicSequence, CFURL!, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified MusicSequenceFileCreateData(MusicSequence, MusicSequenceFileTypeID, MusicSequenceFileFlags, Int16, UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceFileCreateData(_ inSequence: MusicSequence, _ inFileType: MusicSequenceFileTypeID, _ inFlags: MusicSequenceFileFlags, _ inResolution: Int16, _ outData: UnsafePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceFileCreateData(_ inSequence: MusicSequence, _ inFileType: MusicSequenceFileTypeID, _ inFlags: MusicSequenceFileFlags, _ inResolution: Int16, _ outData: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` | OS X 10.5 |

Modified MusicSequenceFileLoad(MusicSequence, CFURL!, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified MusicSequenceFileLoadData(MusicSequence, CFData!, MusicSequenceFileTypeID, MusicSequenceLoadFlags) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified MusicSequenceGetAUGraph(MusicSequence, UnsafeMutablePointer<AUGraph>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetAUGraph(_ inSequence: MusicSequence, _ outGraph: UnsafePointer<AUGraph>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetAUGraph(_ inSequence: MusicSequence, _ outGraph: UnsafeMutablePointer<AUGraph>) -> OSStatus ``` | OS X 10.0 |

Modified MusicSequenceGetBeatsForSeconds(MusicSequence, Float64, UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetBeatsForSeconds(_ inSequence: MusicSequence, _ inSeconds: Float64, _ outBeats: UnsafePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetBeatsForSeconds(_ inSequence: MusicSequence, _ inSeconds: Float64, _ outBeats: UnsafeMutablePointer<MusicTimeStamp>) -> OSStatus ``` | OS X 10.2 |

Modified MusicSequenceGetIndTrack(MusicSequence, UInt32, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetIndTrack(_ inSequence: MusicSequence, _ inTrackIndex: UInt32, _ outTrack: UnsafePointer<MusicTrack>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetIndTrack(_ inSequence: MusicSequence, _ inTrackIndex: UInt32, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` | OS X 10.0 |

Modified MusicSequenceGetInfoDictionary(MusicSequence) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified MusicSequenceGetSMPTEResolution(Int16, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UInt8>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetSMPTEResolution(_ inRes: Int16, _ fps: UnsafePointer<SignedByte>, _ ticks: UnsafePointer<Byte>) ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetSMPTEResolution(_ inRes: Int16, _ fps: UnsafeMutablePointer<Int8>, _ ticks: UnsafeMutablePointer<UInt8>) ``` | OS X 10.10.3 |

Modified MusicSequenceGetSecondsForBeats(MusicSequence, MusicTimeStamp, UnsafeMutablePointer<Float64>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetSecondsForBeats(_ inSequence: MusicSequence, _ inBeats: MusicTimeStamp, _ outSeconds: UnsafePointer<Float64>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetSecondsForBeats(_ inSequence: MusicSequence, _ inBeats: MusicTimeStamp, _ outSeconds: UnsafeMutablePointer<Float64>) -> OSStatus ``` | OS X 10.2 |

Modified MusicSequenceGetSequenceType(MusicSequence, UnsafeMutablePointer<MusicSequenceType>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetSequenceType(_ inSequence: MusicSequence, _ outType: UnsafePointer<MusicSequenceType>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetSequenceType(_ inSequence: MusicSequence, _ outType: UnsafeMutablePointer<MusicSequenceType>) -> OSStatus ``` | OS X 10.5 |

Modified MusicSequenceGetTempoTrack(MusicSequence, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetTempoTrack(_ inSequence: MusicSequence, _ outTrack: UnsafePointer<MusicTrack>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetTempoTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` | OS X 10.1 |

Modified MusicSequenceGetTrackCount(MusicSequence, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetTrackCount(_ inSequence: MusicSequence, _ outNumberOfTracks: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetTrackCount(_ inSequence: MusicSequence, _ outNumberOfTracks: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified MusicSequenceGetTrackIndex(MusicSequence, MusicTrack, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceGetTrackIndex(_ inSequence: MusicSequence, _ inTrack: MusicTrack, _ outTrackIndex: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceGetTrackIndex(_ inSequence: MusicSequence, _ inTrack: MusicTrack, _ outTrackIndex: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified MusicSequenceNewTrack(MusicSequence, UnsafeMutablePointer<MusicTrack>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceNewTrack(_ inSequence: MusicSequence, _ outTrack: UnsafePointer<MusicTrack>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceNewTrack(_ inSequence: MusicSequence, _ outTrack: UnsafeMutablePointer<MusicTrack>) -> OSStatus ``` | OS X 10.0 |

Modified MusicSequenceReverse(MusicSequence) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicSequenceSetAUGraph(MusicSequence, AUGraph) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicSequenceSetMIDIEndpoint(MusicSequence, MIDIEndpointRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MusicSequenceSetSMPTEResolution(Int8, UInt8) -> Int16

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceSetSMPTEResolution(_ fps: SignedByte, _ ticks: Byte) -> Int16 ``` | OS X 10.10 |
| To | ``` func MusicSequenceSetSMPTEResolution(_ fps: Int8, _ ticks: UInt8) -> Int16 ``` | OS X 10.10.3 |

Modified MusicSequenceSetSequenceType(MusicSequence, MusicSequenceType) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified MusicSequenceSetUserCallback(MusicSequence, MusicSequenceUserCallback, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback, _ inClientData: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.3 |

Modified MusicSequenceUserCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicSequenceUserCallback = CFunctionPointer<((UnsafePointer<()>, MusicSequence, MusicTrack, MusicTimeStamp, ConstUnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Void)> ``` |
| To | ``` typealias MusicSequenceUserCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicSequence, MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Void)> ``` |

Modified MusicTrackClear(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackCopyInsert(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackCut(MusicTrack, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackGetDestMIDIEndpoint(MusicTrack, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackGetDestMIDIEndpoint(_ inTrack: MusicTrack, _ outEndpoint: UnsafePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackGetDestMIDIEndpoint(_ inTrack: MusicTrack, _ outEndpoint: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus ``` | OS X 10.1 |

Modified MusicTrackGetDestNode(MusicTrack, UnsafeMutablePointer<AUNode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackGetDestNode(_ inTrack: MusicTrack, _ outNode: UnsafePointer<AUNode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackGetDestNode(_ inTrack: MusicTrack, _ outNode: UnsafeMutablePointer<AUNode>) -> OSStatus ``` | OS X 10.1 |

Modified MusicTrackGetProperty(MusicTrack, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackGetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ outData: UnsafePointer<()>, _ ioLength: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackGetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ outData: UnsafeMutablePointer<Void>, _ ioLength: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackGetSequence(MusicTrack, UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackGetSequence(_ inTrack: MusicTrack, _ outSequence: UnsafePointer<MusicSequence>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackGetSequence(_ inTrack: MusicTrack, _ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackMerge(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTrack, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackMoveEvents(MusicTrack, MusicTimeStamp, MusicTimeStamp, MusicTimeStamp) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackNewAUPresetEvent(MusicTrack, MusicTimeStamp, UnsafePointer<AUPresetEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewAUPresetEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inPresetEvent: ConstUnsafePointer<AUPresetEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewAUPresetEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inPresetEvent: UnsafePointer<AUPresetEvent>) -> OSStatus ``` | OS X 10.3 |

Modified MusicTrackNewExtendedNoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewExtendedNoteEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inInfo: ConstUnsafePointer<ExtendedNoteOnEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewExtendedNoteEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inInfo: UnsafePointer<ExtendedNoteOnEvent>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackNewExtendedTempoEvent(MusicTrack, MusicTimeStamp, Float64) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackNewMIDIChannelEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIChannelMessage>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewMIDIChannelEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMessage: ConstUnsafePointer<MIDIChannelMessage>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewMIDIChannelEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMessage: UnsafePointer<MIDIChannelMessage>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackNewMIDINoteEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDINoteMessage>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewMIDINoteEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMessage: ConstUnsafePointer<MIDINoteMessage>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewMIDINoteEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMessage: UnsafePointer<MIDINoteMessage>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackNewMIDIRawDataEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIRawData>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewMIDIRawDataEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inRawData: ConstUnsafePointer<MIDIRawData>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewMIDIRawDataEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inRawData: UnsafePointer<MIDIRawData>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackNewMetaEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MIDIMetaEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewMetaEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMetaEvent: ConstUnsafePointer<MIDIMetaEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewMetaEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inMetaEvent: UnsafePointer<MIDIMetaEvent>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackNewParameterEvent(MusicTrack, MusicTimeStamp, UnsafePointer<ParameterEvent>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewParameterEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inInfo: ConstUnsafePointer<ParameterEvent>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewParameterEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inInfo: UnsafePointer<ParameterEvent>) -> OSStatus ``` | OS X 10.2 |

Modified MusicTrackNewUserEvent(MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackNewUserEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inUserData: ConstUnsafePointer<MusicEventUserData>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackNewUserEvent(_ inTrack: MusicTrack, _ inTimeStamp: MusicTimeStamp, _ inUserData: UnsafePointer<MusicEventUserData>) -> OSStatus ``` | OS X 10.0 |

Modified MusicTrackSetDestMIDIEndpoint(MusicTrack, MIDIEndpointRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified MusicTrackSetDestNode(MusicTrack, AUNode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified MusicTrackSetProperty(MusicTrack, UInt32, UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MusicTrackSetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ inData: UnsafePointer<()>, _ inLength: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func MusicTrackSetProperty(_ inTrack: MusicTrack, _ inPropertyID: UInt32, _ inData: UnsafeMutablePointer<Void>, _ inLength: UInt32) -> OSStatus ``` | OS X 10.0 |

Modified NewAUGraph(UnsafeMutablePointer<AUGraph>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NewAUGraph(_ outGraph: UnsafePointer<AUGraph>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func NewAUGraph(_ outGraph: UnsafeMutablePointer<AUGraph>) -> OSStatus ``` | OS X 10.0 |

Modified NewMusicEventIterator(MusicTrack, UnsafeMutablePointer<MusicEventIterator>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NewMusicEventIterator(_ inTrack: MusicTrack, _ outIterator: UnsafePointer<MusicEventIterator>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func NewMusicEventIterator(_ inTrack: MusicTrack, _ outIterator: UnsafeMutablePointer<MusicEventIterator>) -> OSStatus ``` | OS X 10.0 |

Modified NewMusicPlayer(UnsafeMutablePointer<MusicPlayer>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NewMusicPlayer(_ outPlayer: UnsafePointer<MusicPlayer>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func NewMusicPlayer(_ outPlayer: UnsafeMutablePointer<MusicPlayer>) -> OSStatus ``` | OS X 10.0 |

Modified NewMusicSequence(UnsafeMutablePointer<MusicSequence>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func NewMusicSequence(_ outSequence: UnsafePointer<MusicSequence>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func NewMusicSequence(_ outSequence: UnsafeMutablePointer<MusicSequence>) -> OSStatus ``` | OS X 10.0 |

Modified ReadBytesFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias ReadBytesFDF = CFunctionPointer<((UnsafePointer<()>, Boolean, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ReadBytesFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ReadPacketDataFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias ReadPacketDataFDF = CFunctionPointer<((UnsafePointer<()>, Boolean, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ReadPacketDataFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified ReadPacketsFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias ReadPacketsFDF = CFunctionPointer<((UnsafePointer<()>, Boolean, UnsafePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, UnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias ReadPacketsFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |

Modified SetPropertyFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias SetPropertyFDF = CFunctionPointer<((UnsafePointer<()>, AudioFilePropertyID, UInt32, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias SetPropertyFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFilePropertyID, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified SetUserDataFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias SetUserDataFDF = CFunctionPointer<((UnsafePointer<()>, UInt32, UInt32, UInt32, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias SetUserDataFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UInt32, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified WriteBytesFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias WriteBytesFDF = CFunctionPointer<((UnsafePointer<()>, Boolean, Int64, UnsafePointer<UInt32>, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias WriteBytesFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus)> ``` |

Modified WritePacketsFDF

|  | Declaration |
| --- | --- |
| From | ``` typealias WritePacketsFDF = CFunctionPointer<((UnsafePointer<()>, Boolean, UInt32, ConstUnsafePointer<AudioStreamPacketDescription>, Int64, UnsafePointer<UInt32>, ConstUnsafePointer<()>) -> OSStatus)> ``` |
| To | ``` typealias WritePacketsFDF = CFunctionPointer<((UnsafeMutablePointer<Void>, Boolean, UInt32, UnsafePointer<AudioStreamPacketDescription>, Int64, UnsafeMutablePointer<UInt32>, UnsafePointer<Void>) -> OSStatus)> ``` |

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
