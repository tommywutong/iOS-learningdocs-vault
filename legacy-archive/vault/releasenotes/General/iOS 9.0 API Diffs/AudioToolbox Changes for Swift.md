---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AudioToolbox.html
archived_at: '2026-07-18T02:56:40.569514Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AudioToolbox Changes for Swift

### AudioToolbox

Removed AudioBalanceFade.init()Removed AudioBalanceFade.init(mLeftRightBalance: Float32, mBackFrontFade: Float32, mType: UInt32, mChannelLayout: UnsafePointer<AudioChannelLayout>)Removed AudioBytePacketTranslation.init(mByte: Int64, mPacket: Int64, mByteOffsetInPacket: UInt32, mFlags: UInt32)Removed AudioFileMarker.init(mFramePosition: Float64, mName: Unmanaged<CFString>!, mMarkerID: Int32, mSMPTETime: AudioFile_SMPTE_Time, mType: UInt32, mReserved: UInt16, mChannel: UInt16)Removed AudioFileRegion.init()Removed AudioFileRegion.init(mRegionID: UInt32, mName: Unmanaged<CFString>!, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers: (AudioFileMarker))Removed AudioFormatInfo.init()Removed AudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32)Removed AudioPanningInfo.init()Removed AudioPanningInfo.init(mPanningMode: UInt32, mCoordinateFlags: UInt32, mCoordinates: (Float32, Float32, Float32), mGainScale: Float32, mOutputChannelMap: UnsafePointer<AudioChannelLayout>)Removed AudioQueueBuffer.init()Removed AudioQueueBuffer.init(mAudioDataBytesCapacity: UInt32, mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize: UInt32, mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity: UInt32, mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount: UInt32)Removed AudioQueueChannelAssignment.init()Removed AudioQueueChannelAssignment.init(mDeviceUID: Unmanaged<CFString>!, mChannelNumber: UInt32)Removed AUPresetEvent.init()Removed AUPresetEvent.init(scope: AudioUnitScope, element: AudioUnitElement, preset: Unmanaged<CFPropertyList>!)Removed CAFAudioDescription.init(mSampleRate: Float64, mFormatID: UInt32, mFormatFlags: UInt32, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32)Removed CAFRegion.init(mRegionID: UInt32, mFlags: UInt32, mNumberMarkers: UInt32, mMarkers: (CAFMarker))Removed ExtendedAudioFormatInfo.init()Removed ExtendedAudioFormatInfo.init(mASBD: AudioStreamBasicDescription, mMagicCookie: UnsafePointer<Void>, mMagicCookieSize: UInt32, mClassDescription: AudioClassDescription)Removed kAudioBalanceFadeType_EqualPowerRemoved kAudioBalanceFadeType_MaxUnityGainRemoved kAudioFileFlags_DontPageAlignAudioDataRemoved kAudioFileFlags_EraseFileRemoved kAudioFileReadPermissionRemoved kAudioFileReadWritePermissionRemoved kAudioFileRegionFlag_LoopEnableRemoved kAudioFileRegionFlag_PlayBackwardRemoved kAudioFileRegionFlag_PlayForwardRemoved kAudioFileStreamParseFlag_DiscontinuityRemoved kAudioFileStreamPropertyFlag_CachePropertyRemoved kAudioFileStreamPropertyFlag_PropertyIsCachedRemoved kAudioFileStreamSeekFlag_OffsetIsEstimatedRemoved kAudioFileWritePermissionRemoved kAudioQueueProcessingTap_EndOfStreamRemoved kAudioQueueProcessingTap_PostEffectsRemoved kAudioQueueProcessingTap_PreEffectsRemoved kAudioQueueProcessingTap_SiphonRemoved kAudioQueueProcessingTap_StartOfStreamRemoved kBytePacketTranslationFlag_IsEstimateRemoved kCAFLinearPCMFormatFlagIsFloatRemoved kCAFLinearPCMFormatFlagIsLittleEndianRemoved kCAFRegionFlag_LoopEnableRemoved kCAFRegionFlag_PlayBackwardRemoved kCAFRegionFlag_PlayForwardRemoved kMusicSequenceFile_iMelodyTypeRemoved kMusicSequenceFile_MIDITypeRemoved kMusicSequenceFileFlags_EraseFileRemoved kMusicSequenceLoadSMF_ChannelsToTracksRemoved kMusicSequenceType_BeatsRemoved kMusicSequenceType_SamplesRemoved kMusicSequenceType_SecondsRemoved kPanningMode_SoundFieldRemoved kPanningMode_VectorBasedPanningRemoved MusicSequenceFileFlagsRemoved MusicSequenceFileTypeIDRemoved MusicSequenceLoadFlagsRemoved MusicSequenceTypeAdded [AudioBalanceFadeType [enum]](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype)Added [AudioBalanceFadeType.EqualPower](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype/equalpower)Added [AudioBalanceFadeType.MaxUnityGain](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype/maxunitygain)Added AudioBytePacketTranslation.init(mByte: Int64, mPacket: Int64, mByteOffsetInPacket: UInt32, mFlags: AudioBytePacketTranslationFlags)Added [AudioBytePacketTranslationFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags)Added [AudioBytePacketTranslationFlags.BytePacketTranslationFlag_IsEstimate](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslationflags/kbytepackettranslationflag_isestimate)Added AudioBytePacketTranslationFlags.init(rawValue: UInt32)Added [AudioFileFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofileflags)Added [AudioFileFlags.DontPageAlignAudioData](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/1502812-dontpagealignaudiodata)Added [AudioFileFlags.EraseFile](https://developer.apple.com/documentation/audiotoolbox/audiofileflags/kaudiofileflags_erasefile)Added AudioFileFlags.init(rawValue: UInt32)Added AudioFileMarker.init(mFramePosition: Float64, mName: Unmanaged<CFString>?, mMarkerID: Int32, mSMPTETime: AudioFile_SMPTE_Time, mType: UInt32, mReserved: UInt16, mChannel: UInt16)Added [AudioFilePermissions [enum]](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions)Added [AudioFilePermissions.ReadPermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/readpermission)Added [AudioFilePermissions.ReadWritePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/readwritepermission)Added [AudioFilePermissions.WritePermission](https://developer.apple.com/documentation/audiotoolbox/audiofilepermissions/kaudiofilewritepermission)Added [AudioFileRegionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags)Added AudioFileRegionFlags.init(rawValue: UInt32)Added [AudioFileRegionFlags.LoopEnable](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1503178-loopenable)Added [AudioFileRegionFlags.PlayBackward](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1502362-playbackward)Added [AudioFileRegionFlags.PlayForward](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags/1503175-playforward)Added [AudioFileStreamParseFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags)Added [AudioFileStreamParseFlags.Discontinuity](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparseflags/1391547-discontinuity)Added AudioFileStreamParseFlags.init(rawValue: UInt32)Added [AudioFileStreamPropertyFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags)Added [AudioFileStreamPropertyFlags.CacheProperty](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/1391561-cacheproperty)Added AudioFileStreamPropertyFlags.init(rawValue: UInt32)Added [AudioFileStreamPropertyFlags.PropertyIsCached](https://developer.apple.com/documentation/audiotoolbox/audiofilestreampropertyflags/kaudiofilestreampropertyflag_propertyiscached)Added [AudioFileStreamSeekFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags)Added AudioFileStreamSeekFlags.init(rawValue: UInt32)Added [AudioFileStreamSeekFlags.OffsetIsEstimated](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseekflags/1391553-offsetisestimated)Added [AudioPanningMode [enum]](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode)Added [AudioPanningMode.PanningMode_SoundField](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode/panningmode_soundfield)Added [AudioPanningMode.PanningMode_VectorBasedPanning](https://developer.apple.com/documentation/audiotoolbox/audiopanningmode/kpanningmode_vectorbasedpanning)Added [AudioQueueProcessingTapFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags)Added [AudioQueueProcessingTapFlags.EndOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_endofstream)Added AudioQueueProcessingTapFlags.init(rawValue: UInt32)Added [AudioQueueProcessingTapFlags.PostEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/kaudioqueueprocessingtap_posteffects)Added [AudioQueueProcessingTapFlags.PreEffects](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502092-preeffects)Added [AudioQueueProcessingTapFlags.Siphon](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1502728-siphon)Added [AudioQueueProcessingTapFlags.StartOfStream](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapflags/1503320-startofstream)Added CAFAudioDescription.init(mSampleRate: Float64, mFormatID: UInt32, mFormatFlags: CAFFormatFlags, mBytesPerPacket: UInt32, mFramesPerPacket: UInt32, mChannelsPerFrame: UInt32, mBitsPerChannel: UInt32)Added [CAFFormatFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/cafformatflags)Added CAFFormatFlags.init(rawValue: UInt32)Added [CAFFormatFlags.LinearPCMFormatFlagIsFloat](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagisfloat)Added [CAFFormatFlags.LinearPCMFormatFlagIsLittleEndian](https://developer.apple.com/documentation/audiotoolbox/cafformatflags/kcaflinearpcmformatflagislittleendian)Added CAFRegion.init(mRegionID: UInt32, mFlags: CAFRegionFlags, mNumberMarkers: UInt32, mMarkers: (CAFMarker))Added [CAFRegionFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/cafregionflags)Added CAFRegionFlags.init(rawValue: UInt32)Added [CAFRegionFlags.LoopEnable](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/1502336-loopenable)Added [CAFRegionFlags.PlayBackward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/1501777-playbackward)Added [CAFRegionFlags.PlayForward](https://developer.apple.com/documentation/audiotoolbox/cafregionflags/kcafregionflag_playforward)Added [MusicSequenceFileFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags)Added [MusicSequenceFileFlags.Default](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_default)Added [MusicSequenceFileFlags.EraseFile](https://developer.apple.com/documentation/audiotoolbox/musicsequencefileflags/kmusicsequencefileflags_erasefile)Added MusicSequenceFileFlags.init(rawValue: UInt32)Added [MusicSequenceFileTypeID [enum]](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid)Added [MusicSequenceFileTypeID.AnyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/anytype)Added [MusicSequenceFileTypeID.iMelodyType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/kmusicsequencefile_imelodytype)Added [MusicSequenceFileTypeID.MIDIType](https://developer.apple.com/documentation/audiotoolbox/musicsequencefiletypeid/kmusicsequencefile_miditype)Added [MusicSequenceLoadFlags [struct]](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags)Added MusicSequenceLoadFlags.init(rawValue: UInt32)Added [MusicSequenceLoadFlags.SMF_ChannelsToTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/kmusicsequenceloadsmf_channelstotracks)Added [MusicSequenceLoadFlags.SMF_PreserveTracks](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadflags/kmusicsequenceloadsmf_preservetracks)Added [MusicSequenceType [enum]](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype)Added [MusicSequenceType.Beats](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/beats)Added [MusicSequenceType.Samples](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/samples)Added [MusicSequenceType.Seconds](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype/seconds)Added [AudioServicesPlayAlertSoundWithCompletion(_: SystemSoundID, _: (() -> Void)?)](https://developer.apple.com/documentation/audiotoolbox/1405238-audioservicesplayalertsoundwithc)Added [AudioServicesPlaySystemSoundWithCompletion(_: SystemSoundID, _: (() -> Void)?)](https://developer.apple.com/documentation/audiotoolbox/1405210-audioservicesplaysystemsoundwith)Added [kAudioToolboxError_NoTrackDestination](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerror_notrackdestination)Added [NextAudioFileRegion(_: UnsafePointer<AudioFileRegion>) -> UnsafeMutablePointer<AudioFileRegion>](https://developer.apple.com/documentation/audiotoolbox/1501607-nextaudiofileregion)Added [NumAudioFileMarkersToNumBytes(_: Int) -> Int](https://developer.apple.com/documentation/audiotoolbox/1503350-numaudiofilemarkerstonumbytes)Added [NumBytesToNumAudioFileMarkers(_: Int) -> Int](https://developer.apple.com/documentation/audiotoolbox/1502677-numbytestonumaudiofilemarkers)Modified [AudioBalanceFade [struct]](https://developer.apple.com/documentation/audiotoolbox/audiobalancefade)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: UInt32     var mChannelLayout: UnsafePointer<AudioChannelLayout>     init()     init(mLeftRightBalance mLeftRightBalance: Float32, mBackFrontFade mBackFrontFade: Float32, mType mType: UInt32, mChannelLayout mChannelLayout: UnsafePointer<AudioChannelLayout>) } ``` |
| To | ``` struct AudioBalanceFade {     var mLeftRightBalance: Float32     var mBackFrontFade: Float32     var mType: AudioBalanceFadeType     var mChannelLayout: UnsafePointer<AudioChannelLayout> } ``` |

Modified [AudioBalanceFade.mType](https://developer.apple.com/documentation/audiotoolbox/audiobalancefade/1502748-mtype)

|  | Declaration |
| --- | --- |
| From | ``` var mType: UInt32 ``` |
| To | ``` var mType: AudioBalanceFadeType ``` |

Modified [AudioBytePacketTranslation [struct]](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslation)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBytePacketTranslation {     var mByte: Int64     var mPacket: Int64     var mByteOffsetInPacket: UInt32     var mFlags: UInt32     init()     init(mByte mByte: Int64, mPacket mPacket: Int64, mByteOffsetInPacket mByteOffsetInPacket: UInt32, mFlags mFlags: UInt32) } ``` |
| To | ``` struct AudioBytePacketTranslation {     var mByte: Int64     var mPacket: Int64     var mByteOffsetInPacket: UInt32     var mFlags: AudioBytePacketTranslationFlags     init()     init(mByte mByte: Int64, mPacket mPacket: Int64, mByteOffsetInPacket mByteOffsetInPacket: UInt32, mFlags mFlags: AudioBytePacketTranslationFlags) } ``` |

Modified [AudioBytePacketTranslation.mFlags](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslation/1501805-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: AudioBytePacketTranslationFlags ``` |

Modified [AudioFileMarker [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofilemarker)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileMarker {     var mFramePosition: Float64     var mName: Unmanaged<CFString>!     var mMarkerID: Int32     var mSMPTETime: AudioFile_SMPTE_Time     var mType: UInt32     var mReserved: UInt16     var mChannel: UInt16     init()     init(mFramePosition mFramePosition: Float64, mName mName: Unmanaged<CFString>!, mMarkerID mMarkerID: Int32, mSMPTETime mSMPTETime: AudioFile_SMPTE_Time, mType mType: UInt32, mReserved mReserved: UInt16, mChannel mChannel: UInt16) } ``` |
| To | ``` struct AudioFileMarker {     var mFramePosition: Float64     var mName: Unmanaged<CFString>?     var mMarkerID: Int32     var mSMPTETime: AudioFile_SMPTE_Time     var mType: UInt32     var mReserved: UInt16     var mChannel: UInt16     init()     init(mFramePosition mFramePosition: Float64, mName mName: Unmanaged<CFString>?, mMarkerID mMarkerID: Int32, mSMPTETime mSMPTETime: AudioFile_SMPTE_Time, mType mType: UInt32, mReserved mReserved: UInt16, mChannel mChannel: UInt16) } ``` |

Modified [AudioFileMarker.mName](https://developer.apple.com/documentation/audiotoolbox/audiofilemarker/1502334-mname)

|  | Declaration |
| --- | --- |
| From | ``` var mName: Unmanaged<CFString>! ``` |
| To | ``` var mName: Unmanaged<CFString>? ``` |

Modified [AudioFileRegion [struct]](https://developer.apple.com/documentation/audiotoolbox/audiofileregion)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFileRegion {     var mRegionID: UInt32     var mName: Unmanaged<CFString>!     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker)     init()     init(mRegionID mRegionID: UInt32, mName mName: Unmanaged<CFString>!, mFlags mFlags: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (AudioFileMarker)) } ``` |
| To | ``` struct AudioFileRegion {     var mRegionID: UInt32     var mName: Unmanaged<CFString>     var mFlags: AudioFileRegionFlags     var mNumberMarkers: UInt32     var mMarkers: (AudioFileMarker) } ``` |

Modified [AudioFileRegion.mFlags](https://developer.apple.com/documentation/audiotoolbox/audiofileregion/1502628-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: AudioFileRegionFlags ``` |

Modified [AudioFileRegion.mName](https://developer.apple.com/documentation/audiotoolbox/audiofileregion/1501797-mname)

|  | Declaration |
| --- | --- |
| From | ``` var mName: Unmanaged<CFString>! ``` |
| To | ``` var mName: Unmanaged<CFString> ``` |

Modified [AudioFormatInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audioformatinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32) } ``` |
| To | ``` struct AudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32 } ``` |

Modified [AudioPanningInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/audiopanninginfo)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioPanningInfo {     var mPanningMode: UInt32     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: UnsafePointer<AudioChannelLayout>     init()     init(mPanningMode mPanningMode: UInt32, mCoordinateFlags mCoordinateFlags: UInt32, mCoordinates mCoordinates: (Float32, Float32, Float32), mGainScale mGainScale: Float32, mOutputChannelMap mOutputChannelMap: UnsafePointer<AudioChannelLayout>) } ``` |
| To | ``` struct AudioPanningInfo {     var mPanningMode: AudioPanningMode     var mCoordinateFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     var mGainScale: Float32     var mOutputChannelMap: UnsafePointer<AudioChannelLayout> } ``` |

Modified [AudioPanningInfo.mPanningMode](https://developer.apple.com/documentation/audiotoolbox/audiopanninginfo/1503364-mpanningmode)

|  | Declaration |
| --- | --- |
| From | ``` var mPanningMode: UInt32 ``` |
| To | ``` var mPanningMode: AudioPanningMode ``` |

Modified [AudioQueueBuffer [struct]](https://developer.apple.com/documentation/audiotoolbox/audioqueuebuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32     init()     init(mAudioDataBytesCapacity mAudioDataBytesCapacity: UInt32, mAudioData mAudioData: UnsafeMutablePointer<Void>, mAudioDataByteSize mAudioDataByteSize: UInt32, mUserData mUserData: UnsafeMutablePointer<Void>, mPacketDescriptionCapacity mPacketDescriptionCapacity: UInt32, mPacketDescriptions mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, mPacketDescriptionCount mPacketDescriptionCount: UInt32) } ``` |
| To | ``` struct AudioQueueBuffer {     var mAudioDataBytesCapacity: UInt32     var mAudioData: UnsafeMutablePointer<Void>     var mAudioDataByteSize: UInt32     var mUserData: UnsafeMutablePointer<Void>     var mPacketDescriptionCapacity: UInt32     var mPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>     var mPacketDescriptionCount: UInt32 } ``` |

Modified [AudioQueueChannelAssignment [struct]](https://developer.apple.com/documentation/audiotoolbox/audioqueuechannelassignment)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioQueueChannelAssignment {     var mDeviceUID: Unmanaged<CFString>!     var mChannelNumber: UInt32     init()     init(mDeviceUID mDeviceUID: Unmanaged<CFString>!, mChannelNumber mChannelNumber: UInt32) } ``` |
| To | ``` struct AudioQueueChannelAssignment {     var mDeviceUID: Unmanaged<CFString>     var mChannelNumber: UInt32 } ``` |

Modified [AudioQueueChannelAssignment.mDeviceUID](https://developer.apple.com/documentation/audiotoolbox/audioqueuechannelassignment/1618730-mdeviceuid)

|  | Declaration |
| --- | --- |
| From | ``` var mDeviceUID: Unmanaged<CFString>! ``` |
| To | ``` var mDeviceUID: Unmanaged<CFString> ``` |

Modified [AUPresetEvent [struct]](https://developer.apple.com/documentation/audiotoolbox/aupresetevent)

|  | Declaration |
| --- | --- |
| From | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyList>!     init()     init(scope scope: AudioUnitScope, element element: AudioUnitElement, preset preset: Unmanaged<CFPropertyList>!) } ``` |
| To | ``` struct AUPresetEvent {     var scope: AudioUnitScope     var element: AudioUnitElement     var preset: Unmanaged<CFPropertyList> } ``` |

Modified [AUPresetEvent.preset](https://developer.apple.com/documentation/audiotoolbox/aupresetevent/1501634-preset)

|  | Declaration |
| --- | --- |
| From | ``` var preset: Unmanaged<CFPropertyList>! ``` |
| To | ``` var preset: Unmanaged<CFPropertyList> ``` |

Modified [CAFAudioDescription [struct]](https://developer.apple.com/documentation/audiotoolbox/cafaudiodescription)

|  | Declaration |
| --- | --- |
| From | ``` struct CAFAudioDescription {     var mSampleRate: Float64     var mFormatID: UInt32     var mFormatFlags: UInt32     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32     init()     init(mSampleRate mSampleRate: Float64, mFormatID mFormatID: UInt32, mFormatFlags mFormatFlags: UInt32, mBytesPerPacket mBytesPerPacket: UInt32, mFramesPerPacket mFramesPerPacket: UInt32, mChannelsPerFrame mChannelsPerFrame: UInt32, mBitsPerChannel mBitsPerChannel: UInt32) } ``` |
| To | ``` struct CAFAudioDescription {     var mSampleRate: Float64     var mFormatID: UInt32     var mFormatFlags: CAFFormatFlags     var mBytesPerPacket: UInt32     var mFramesPerPacket: UInt32     var mChannelsPerFrame: UInt32     var mBitsPerChannel: UInt32     init()     init(mSampleRate mSampleRate: Float64, mFormatID mFormatID: UInt32, mFormatFlags mFormatFlags: CAFFormatFlags, mBytesPerPacket mBytesPerPacket: UInt32, mFramesPerPacket mFramesPerPacket: UInt32, mChannelsPerFrame mChannelsPerFrame: UInt32, mBitsPerChannel mBitsPerChannel: UInt32) } ``` |

Modified [CAFAudioDescription.mFormatFlags](https://developer.apple.com/documentation/audiotoolbox/cafaudiodescription/1501974-mformatflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFormatFlags: UInt32 ``` |
| To | ``` var mFormatFlags: CAFFormatFlags ``` |

Modified [CAFRegion [struct]](https://developer.apple.com/documentation/audiotoolbox/cafregion)

|  | Declaration |
| --- | --- |
| From | ``` struct CAFRegion {     var mRegionID: UInt32     var mFlags: UInt32     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker)     init()     init(mRegionID mRegionID: UInt32, mFlags mFlags: UInt32, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (CAFMarker)) } ``` |
| To | ``` struct CAFRegion {     var mRegionID: UInt32     var mFlags: CAFRegionFlags     var mNumberMarkers: UInt32     var mMarkers: (CAFMarker)     init()     init(mRegionID mRegionID: UInt32, mFlags mFlags: CAFRegionFlags, mNumberMarkers mNumberMarkers: UInt32, mMarkers mMarkers: (CAFMarker)) } ``` |

Modified [CAFRegion.mFlags](https://developer.apple.com/documentation/audiotoolbox/cafregion/1503249-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: CAFRegionFlags ``` |

Modified [ExtendedAudioFormatInfo [struct]](https://developer.apple.com/documentation/audiotoolbox/extendedaudioformatinfo)

|  | Declaration |
| --- | --- |
| From | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription     init()     init(mASBD mASBD: AudioStreamBasicDescription, mMagicCookie mMagicCookie: UnsafePointer<Void>, mMagicCookieSize mMagicCookieSize: UInt32, mClassDescription mClassDescription: AudioClassDescription) } ``` |
| To | ``` struct ExtendedAudioFormatInfo {     var mASBD: AudioStreamBasicDescription     var mMagicCookie: UnsafePointer<Void>     var mMagicCookieSize: UInt32     var mClassDescription: AudioClassDescription } ``` |

Modified [AudioConverterComplexInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterComplexInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterComplexInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioConverterGetPropertyInfo(_: AudioConverterRef, _: AudioConverterPropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502563-audioconvertergetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioConverterGetPropertyInfo(_ inAudioConverter: AudioConverterRef, _ inPropertyID: AudioConverterPropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioConverterInputDataProc](https://developer.apple.com/documentation/audiotoolbox/audioconverterinputdataproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioConverterInputDataProc = CFunctionPointer<((AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioConverterInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioFile_GetSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_getsizeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_GetSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Int64)> ``` |
| To | ``` typealias AudioFile_GetSizeProc = (UnsafeMutablePointer<Void>) -> Int64 ``` |

Modified [AudioFile_ReadProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_readproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_ReadProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_ReadProc = (UnsafeMutablePointer<Void>, Int64, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioFile_SetSizeProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_setsizeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_SetSizeProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_SetSizeProc = (UnsafeMutablePointer<Void>, Int64) -> OSStatus ``` |

Modified [AudioFile_WriteProc](https://developer.apple.com/documentation/audiotoolbox/audiofile_writeproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFile_WriteProc = CFunctionPointer<((UnsafeMutablePointer<Void>, Int64, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus)> ``` |
| To | ``` typealias AudioFile_WriteProc = (UnsafeMutablePointer<Void>, Int64, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [AudioFileCreateWithURL(_: CFURL, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: AudioFileFlags, _: UnsafeMutablePointer<AudioFileID>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502333-audiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL!, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileCreateWithURL(_ inFileRef: CFURL, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |

Modified [AudioFileInitializeWithCallbacks(_: UnsafeMutablePointer<Void>, _: AudioFile_ReadProc, _: AudioFile_WriteProc, _: AudioFile_GetSizeProc, _: AudioFile_SetSizeProc, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: AudioFileFlags, _: UnsafeMutablePointer<AudioFileID>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502895-audiofileinitializewithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileInitializeWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileType: AudioFileTypeID, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: AudioFileFlags, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |

Modified [AudioFileOpenURL(_: CFURL, _: AudioFilePermissions, _: AudioFileTypeID, _: UnsafeMutablePointer<AudioFileID>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502304-audiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileOpenURL(_ inFileRef: CFURL!, _ inPermissions: Int8, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileOpenURL(_ inFileRef: CFURL, _ inPermissions: AudioFilePermissions, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |

Modified [AudioFileOpenWithCallbacks(_: UnsafeMutablePointer<Void>, _: AudioFile_ReadProc, _: AudioFile_WriteProc?, _: AudioFile_GetSizeProc, _: AudioFile_SetSizeProc?, _: AudioFileTypeID, _: UnsafeMutablePointer<AudioFileID>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502746-audiofileopenwithcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |
| To | ``` func AudioFileOpenWithCallbacks(_ inClientData: UnsafeMutablePointer<Void>, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc?, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc?, _ inFileTypeHint: AudioFileTypeID, _ outAudioFile: UnsafeMutablePointer<AudioFileID>) -> OSStatus ``` |

Modified [AudioFileReadBytes(_: AudioFileID, _: Bool, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503247-audiofilereadbytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioFileReadPacketData(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamPacketDescription>, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502788-audiofilereadpacketdata)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadPacketData(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioFileReadPackets(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamPacketDescription>, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503274-audiofilereadpackets)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileReadPackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioFileStream_PacketsProc](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_packetsproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PacketsProc = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> Void)> ``` |
| To | ``` typealias AudioFileStream_PacketsProc = (UnsafeMutablePointer<Void>, UInt32, UInt32, UnsafePointer<Void>, UnsafeMutablePointer<AudioStreamPacketDescription>) -> Void ``` |

Modified [AudioFileStream_PropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_propertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioFileStream_PropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<UInt32>) -> Void)> ``` |
| To | ``` typealias AudioFileStream_PropertyListenerProc = (UnsafeMutablePointer<Void>, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<AudioFileStreamPropertyFlags>) -> Void ``` |

Modified [AudioFileStreamGetPropertyInfo(_: AudioFileStreamID, _: AudioFileStreamPropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391500-audiofilestreamgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioFileStreamGetPropertyInfo(_ inAudioFileStream: AudioFileStreamID, _ inPropertyID: AudioFileStreamPropertyID, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioFileStreamParseBytes(_: AudioFileStreamID, _: UInt32, _: UnsafePointer<Void>, _: AudioFileStreamParseFlags) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391492-audiofilestreamparsebytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafePointer<Void>, _ inFlags: UInt32) -> OSStatus ``` |
| To | ``` func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafePointer<Void>, _ inFlags: AudioFileStreamParseFlags) -> OSStatus ``` |

Modified [AudioFileStreamSeek(_: AudioFileStreamID, _: Int64, _: UnsafeMutablePointer<Int64>, _: UnsafeMutablePointer<AudioFileStreamSeekFlags>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1391488-audiofilestreamseek)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileStreamSeek(_ inAudioFileStream: AudioFileStreamID, _ inPacketOffset: Int64, _ outDataByteOffset: UnsafeMutablePointer<Int64>, _ ioFlags: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func AudioFileStreamSeek(_ inAudioFileStream: AudioFileStreamID, _ inPacketOffset: Int64, _ outDataByteOffset: UnsafeMutablePointer<Int64>, _ ioFlags: UnsafeMutablePointer<AudioFileStreamSeekFlags>) -> OSStatus ``` |

Modified [AudioFileWriteBytes(_: AudioFileID, _: Bool, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502379-audiofilewritebytes)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |

Modified [AudioFileWritePackets(_: AudioFileID, _: Bool, _: UInt32, _: UnsafePointer<AudioStreamPacketDescription>, _: Int64, _: UnsafeMutablePointer<UInt32>, _: UnsafePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502135-audiofilewritepackets)

|  | Declaration |
| --- | --- |
| From | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Boolean, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafePointer<Void>) -> OSStatus ``` |

Modified [AudioQueueDispose(_: AudioQueueRef, _: Bool) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502229-audioqueuedispose)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueDispose(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` |
| To | ``` func AudioQueueDispose(_ inAQ: AudioQueueRef, _ inImmediate: Bool) -> OSStatus ``` |

Modified [AudioQueueGetCurrentTime(_: AudioQueueRef, _: AudioQueueTimelineRef, _: UnsafeMutablePointer<AudioTimeStamp>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502244-audioqueuegetcurrenttime)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioQueueGetCurrentTime(_ inAQ: AudioQueueRef, _ inTimeline: AudioQueueTimelineRef, _ outTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outTimelineDiscontinuity: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioQueueInputCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueinputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueInputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void)> ``` |
| To | ``` typealias AudioQueueInputCallback = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<AudioStreamPacketDescription>) -> Void ``` |

Modified [AudioQueueNewInput(_: UnsafePointer<AudioStreamBasicDescription>, _: AudioQueueInputCallback, _: UnsafeMutablePointer<Void>, _: CFRunLoop?, _: CFString?, _: UInt32, _: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501687-audioqueuenewinput)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |
| To | ``` func AudioQueueNewInput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueInputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |

Modified [AudioQueueNewOutput(_: UnsafePointer<AudioStreamBasicDescription>, _: AudioQueueOutputCallback, _: UnsafeMutablePointer<Void>, _: CFRunLoop?, _: CFString?, _: UInt32, _: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503207-audioqueuenewoutput)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop!, _ inCallbackRunLoopMode: CFString!, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |
| To | ``` func AudioQueueNewOutput(_ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inCallbackProc: AudioQueueOutputCallback, _ inUserData: UnsafeMutablePointer<Void>, _ inCallbackRunLoop: CFRunLoop?, _ inCallbackRunLoopMode: CFString?, _ inFlags: UInt32, _ outAQ: UnsafeMutablePointer<AudioQueueRef>) -> OSStatus ``` |

Modified [AudioQueueOutputCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef) -> Void)> ``` |
| To | ``` typealias AudioQueueOutputCallback = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueueBufferRef) -> Void ``` |

Modified [AudioQueueProcessingTapCallback](https://developer.apple.com/documentation/audiotoolbox/audioqueueprocessingtapcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueueProcessingTapCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void)> ``` |
| To | ``` typealias AudioQueueProcessingTapCallback = (UnsafeMutablePointer<Void>, AudioQueueProcessingTapRef, UInt32, UnsafeMutablePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioQueueProcessingTapFlags>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>) -> Void ``` |

Modified [AudioQueueProcessingTapGetSourceAudio(_: AudioQueueProcessingTapRef, _: UInt32, _: UnsafeMutablePointer<AudioTimeStamp>, _: UnsafeMutablePointer<AudioQueueProcessingTapFlags>, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502107-audioqueueprocessingtapgetsource)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTapRef, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<UInt32>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |
| To | ``` func AudioQueueProcessingTapGetSourceAudio(_ inAQTap: AudioQueueProcessingTapRef, _ inNumberFrames: UInt32, _ ioTimeStamp: UnsafeMutablePointer<AudioTimeStamp>, _ outFlags: UnsafeMutablePointer<AudioQueueProcessingTapFlags>, _ outNumberFrames: UnsafeMutablePointer<UInt32>, _ ioData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |

Modified [AudioQueueProcessingTapNew(_: AudioQueueRef, _: AudioQueueProcessingTapCallback, _: UnsafeMutablePointer<Void>, _: AudioQueueProcessingTapFlags, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<AudioStreamBasicDescription>, _: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503209-audioqueueprocessingtapnew)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: UInt32, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus ``` |
| To | ``` func AudioQueueProcessingTapNew(_ inAQ: AudioQueueRef, _ inCallback: AudioQueueProcessingTapCallback, _ inClientData: UnsafeMutablePointer<Void>, _ inFlags: AudioQueueProcessingTapFlags, _ outMaxFrames: UnsafeMutablePointer<UInt32>, _ outProcessingFormat: UnsafeMutablePointer<AudioStreamBasicDescription>, _ outAQTap: UnsafeMutablePointer<AudioQueueProcessingTapRef>) -> OSStatus ``` |

Modified [AudioQueuePropertyListenerProc](https://developer.apple.com/documentation/audiotoolbox/audioqueuepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioQueuePropertyListenerProc = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueuePropertyID) -> Void)> ``` |
| To | ``` typealias AudioQueuePropertyListenerProc = (UnsafeMutablePointer<Void>, AudioQueueRef, AudioQueuePropertyID) -> Void ``` |

Modified [AudioQueueStop(_: AudioQueueRef, _: Bool) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501970-audioqueuestop)

|  | Declaration |
| --- | --- |
| From | ``` func AudioQueueStop(_ inAQ: AudioQueueRef, _ inImmediate: Boolean) -> OSStatus ``` |
| To | ``` func AudioQueueStop(_ inAQ: AudioQueueRef, _ inImmediate: Bool) -> OSStatus ``` |

Modified [AudioServicesAddSystemSoundCompletion(_: SystemSoundID, _: CFRunLoop?, _: CFString?, _: AudioServicesSystemSoundCompletionProc, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405244-audioservicesaddsystemsoundcompl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop!, _ inRunLoopMode: CFString!, _ inCompletionRoutine: AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func AudioServicesAddSystemSoundCompletion(_ inSystemSoundID: SystemSoundID, _ inRunLoop: CFRunLoop?, _ inRunLoopMode: CFString?, _ inCompletionRoutine: AudioServicesSystemSoundCompletionProc, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioServicesCreateSystemSoundID(_: CFURL, _: UnsafeMutablePointer<SystemSoundID>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405240-audioservicescreatesystemsoundid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesCreateSystemSoundID(_ inFileURL: CFURL!, _ outSystemSoundID: UnsafeMutablePointer<SystemSoundID>) -> OSStatus ``` |
| To | ``` func AudioServicesCreateSystemSoundID(_ inFileURL: CFURL, _ outSystemSoundID: UnsafeMutablePointer<SystemSoundID>) -> OSStatus ``` |

Modified [AudioServicesGetPropertyInfo(_: AudioServicesPropertyID, _: UInt32, _: UnsafePointer<Void>, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1405258-audioservicesgetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioServicesGetPropertyInfo(_ inPropertyID: AudioServicesPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafePointer<Void>, _ outPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioServicesSystemSoundCompletionProc](https://developer.apple.com/documentation/audiotoolbox/audioservicessystemsoundcompletionproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioServicesSystemSoundCompletionProc = CFunctionPointer<((SystemSoundID, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias AudioServicesSystemSoundCompletionProc = (SystemSoundID, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [AudioSessionInterruptionListener](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptionlistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioSessionInterruptionListener = CFunctionPointer<((UnsafeMutablePointer<Void>, UInt32) -> Void)> ``` |
| To | ``` typealias AudioSessionInterruptionListener = (UnsafeMutablePointer<Void>, UInt32) -> Void ``` |

Modified [AudioSessionPropertyListener](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertylistener)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioSessionPropertyListener = CFunctionPointer<((UnsafeMutablePointer<Void>, AudioSessionPropertyID, UInt32, UnsafePointer<Void>) -> Void)> ``` |
| To | ``` typealias AudioSessionPropertyListener = (UnsafeMutablePointer<Void>, AudioSessionPropertyID, UInt32, UnsafePointer<Void>) -> Void ``` |

Modified [AUGraphIsInitialized(_: AUGraph, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502424-augraphisinitialized)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphIsInitialized(_ inGraph: AUGraph, _ outIsInitialized: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AUGraphIsInitialized(_ inGraph: AUGraph, _ outIsInitialized: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AUGraphIsOpen(_: AUGraph, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502285-augraphisopen)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphIsOpen(_ inGraph: AUGraph, _ outIsOpen: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AUGraphIsOpen(_ inGraph: AUGraph, _ outIsOpen: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AUGraphIsRunning(_: AUGraph, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1501730-augraphisrunning)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphIsRunning(_ inGraph: AUGraph, _ outIsRunning: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AUGraphIsRunning(_ inGraph: AUGraph, _ outIsRunning: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AUGraphUpdate(_: AUGraph, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502855-augraphupdate)

|  | Declaration |
| --- | --- |
| From | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [CopyInstrumentInfoFromSoundBank(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1475995-copyinstrumentinfofromsoundbank)

|  | Declaration |
| --- | --- |
| From | ``` func CopyInstrumentInfoFromSoundBank(_ inURL: CFURL!, _ outInstrumentInfo: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func CopyInstrumentInfoFromSoundBank(_ inURL: CFURL, _ outInstrumentInfo: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |

Modified [CopyNameFromSoundBank(_: CFURL, _: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1475986-copynamefromsoundbank)

|  | Declaration |
| --- | --- |
| From | ``` func CopyNameFromSoundBank(_ inURL: CFURL!, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CopyNameFromSoundBank(_ inURL: CFURL, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |

Modified [ExtAudioFileCreateWithURL(_: CFURL, _: AudioFileTypeID, _: UnsafePointer<AudioStreamBasicDescription>, _: UnsafePointer<AudioChannelLayout>, _: UInt32, _: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486878-extaudiofilecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL!, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileCreateWithURL(_ inURL: CFURL, _ inFileType: AudioFileTypeID, _ inStreamDesc: UnsafePointer<AudioStreamBasicDescription>, _ inChannelLayout: UnsafePointer<AudioChannelLayout>, _ inFlags: UInt32, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |

Modified [ExtAudioFileGetPropertyInfo(_: ExtAudioFileRef, _: ExtAudioFilePropertyID, _: UnsafeMutablePointer<UInt32>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486871-extaudiofilegetpropertyinfo)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func ExtAudioFileGetPropertyInfo(_ inExtAudioFile: ExtAudioFileRef, _ inPropertyID: ExtAudioFilePropertyID, _ outSize: UnsafeMutablePointer<UInt32>, _ outWritable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [ExtAudioFileOpenURL(_: CFURL, _: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486873-extaudiofileopenurl)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileOpenURL(_ inURL: CFURL!, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileOpenURL(_ inURL: CFURL, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |

Modified [ExtAudioFileWrapAudioFileID(_: AudioFileID, _: Bool, _: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1486852-extaudiofilewrapaudiofileid)

|  | Declaration |
| --- | --- |
| From | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Boolean, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |
| To | ``` func ExtAudioFileWrapAudioFileID(_ inFileID: AudioFileID, _ inForWriting: Bool, _ outExtAudioFile: UnsafeMutablePointer<ExtAudioFileRef>) -> OSStatus ``` |

Modified [kAppleHardwareAudioCodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/1620448-audio_codec_manufacturer_and_imp/kapplehardwareaudiocodecmanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleHardwareAudioCodecManufacturer: Int { get } ``` |
| To | ``` var kAppleHardwareAudioCodecManufacturer: UInt32 { get } ``` |

Modified [kAppleSoftwareAudioCodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/1620448-audio_codec_manufacturer_and_imp/kapplesoftwareaudiocodecmanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleSoftwareAudioCodecManufacturer: Int { get } ``` |
| To | ``` var kAppleSoftwareAudioCodecManufacturer: UInt32 { get } ``` |

Modified [kAudioConverterApplicableEncodeBitRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterapplicableencodebitrates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterApplicableEncodeBitRates: Int { get } ``` |
| To | ``` var kAudioConverterApplicableEncodeBitRates: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterApplicableEncodeSampleRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterapplicableencodesamplerates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterApplicableEncodeSampleRates: Int { get } ``` |
| To | ``` var kAudioConverterApplicableEncodeSampleRates: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterAvailableEncodeBitRates](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverteravailableencodebitrates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterAvailableEncodeBitRates: Int { get } ``` |
| To | ``` var kAudioConverterAvailableEncodeBitRates: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterAvailableEncodeChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverteravailableencodechannellayouttags)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterAvailableEncodeChannelLayoutTags: Int { get } ``` |
| To | ``` var kAudioConverterAvailableEncodeChannelLayoutTags: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterAvailableEncodeSampleRates](https://developer.apple.com/documentation/audiotoolbox/kaudioconverteravailableencodesamplerates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterAvailableEncodeSampleRates: Int { get } ``` |
| To | ``` var kAudioConverterAvailableEncodeSampleRates: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterChannelMap](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterchannelmap)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterChannelMap: Int { get } ``` |
| To | ``` var kAudioConverterChannelMap: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterCodecQuality](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertercodecquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterCodecQuality: Int { get } ``` |
| To | ``` var kAudioConverterCodecQuality: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterCompressionMagicCookie](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertercompressionmagiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterCompressionMagicCookie: Int { get } ``` |
| To | ``` var kAudioConverterCompressionMagicCookie: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterCurrentInputStreamDescription](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertercurrentinputstreamdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterCurrentInputStreamDescription: Int { get } ``` |
| To | ``` var kAudioConverterCurrentInputStreamDescription: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterCurrentOutputStreamDescription](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertercurrentoutputstreamdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterCurrentOutputStreamDescription: Int { get } ``` |
| To | ``` var kAudioConverterCurrentOutputStreamDescription: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterDecompressionMagicCookie](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterdecompressionmagiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterDecompressionMagicCookie: Int { get } ``` |
| To | ``` var kAudioConverterDecompressionMagicCookie: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterEncodeAdjustableSampleRate](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterencodeadjustablesamplerate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterEncodeAdjustableSampleRate: Int { get } ``` |
| To | ``` var kAudioConverterEncodeAdjustableSampleRate: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterEncodeBitRate](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterencodebitrate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterEncodeBitRate: Int { get } ``` |
| To | ``` var kAudioConverterEncodeBitRate: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterErr_BadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_badpropertysizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_BadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioConverterErr_BadPropertySizeError: OSStatus { get } ``` |

Modified [kAudioConverterErr_FormatNotSupported](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_formatnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_FormatNotSupported: Int { get } ``` |
| To | ``` var kAudioConverterErr_FormatNotSupported: OSStatus { get } ``` |

Modified [kAudioConverterErr_HardwareInUse](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_hardwareinuse)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_HardwareInUse: Int { get } ``` |
| To | ``` var kAudioConverterErr_HardwareInUse: OSStatus { get } ``` |

Modified [kAudioConverterErr_InputSampleRateOutOfRange](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_inputsamplerateoutofrange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_InputSampleRateOutOfRange: Int { get } ``` |
| To | ``` var kAudioConverterErr_InputSampleRateOutOfRange: OSStatus { get } ``` |

Modified [kAudioConverterErr_InvalidInputSize](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_invalidinputsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_InvalidInputSize: Int { get } ``` |
| To | ``` var kAudioConverterErr_InvalidInputSize: OSStatus { get } ``` |

Modified [kAudioConverterErr_InvalidOutputSize](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_invalidoutputsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_InvalidOutputSize: Int { get } ``` |
| To | ``` var kAudioConverterErr_InvalidOutputSize: OSStatus { get } ``` |

Modified [kAudioConverterErr_NoHardwarePermission](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_nohardwarepermission)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_NoHardwarePermission: Int { get } ``` |
| To | ``` var kAudioConverterErr_NoHardwarePermission: OSStatus { get } ``` |

Modified [kAudioConverterErr_OperationNotSupported](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_operationnotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_OperationNotSupported: Int { get } ``` |
| To | ``` var kAudioConverterErr_OperationNotSupported: OSStatus { get } ``` |

Modified [kAudioConverterErr_OutputSampleRateOutOfRange](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_outputsamplerateoutofrange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_OutputSampleRateOutOfRange: Int { get } ``` |
| To | ``` var kAudioConverterErr_OutputSampleRateOutOfRange: OSStatus { get } ``` |

Modified [kAudioConverterErr_PropertyNotSupported](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_propertynotsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_PropertyNotSupported: Int { get } ``` |
| To | ``` var kAudioConverterErr_PropertyNotSupported: OSStatus { get } ``` |

Modified [kAudioConverterErr_RequiresPacketDescriptionsError](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_requirespacketdescriptionserror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_RequiresPacketDescriptionsError: Int { get } ``` |
| To | ``` var kAudioConverterErr_RequiresPacketDescriptionsError: OSStatus { get } ``` |

Modified [kAudioConverterErr_UnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/1559930-anonymous/kaudioconvertererr_unspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterErr_UnspecifiedError: Int { get } ``` |
| To | ``` var kAudioConverterErr_UnspecifiedError: OSStatus { get } ``` |

Modified [kAudioConverterInputChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterinputchannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterInputChannelLayout: Int { get } ``` |
| To | ``` var kAudioConverterInputChannelLayout: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterOutputChannelLayout](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverteroutputchannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterOutputChannelLayout: Int { get } ``` |
| To | ``` var kAudioConverterOutputChannelLayout: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPrimeInfo](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterprimeinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPrimeInfo: Int { get } ``` |
| To | ``` var kAudioConverterPrimeInfo: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPrimeMethod](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterprimemethod)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPrimeMethod: Int { get } ``` |
| To | ``` var kAudioConverterPrimeMethod: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyBitDepthHint](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertybitdepthhint)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyBitDepthHint: Int { get } ``` |
| To | ``` var kAudioConverterPropertyBitDepthHint: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyCalculateInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertycalculateinputbuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyCalculateInputBufferSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyCalculateInputBufferSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyCalculateOutputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertycalculateoutputbuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyCalculateOutputBufferSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyCalculateOutputBufferSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyCanResumeFromInterruption](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertycanresumefrominterruption)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyCanResumeFromInterruption: Int { get } ``` |
| To | ``` var kAudioConverterPropertyCanResumeFromInterruption: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyFormatList](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyformatlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyFormatList: Int { get } ``` |
| To | ``` var kAudioConverterPropertyFormatList: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyInputCodecParameters](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyinputcodecparameters)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyInputCodecParameters: Int { get } ``` |
| To | ``` var kAudioConverterPropertyInputCodecParameters: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyMaximumInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertymaximuminputbuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyMaximumInputBufferSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyMaximumInputBufferSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyMaximumInputPacketSize](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertymaximuminputpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyMaximumInputPacketSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyMaximumInputPacketSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyMaximumOutputPacketSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertymaximumoutputpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyMaximumOutputPacketSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyMaximumOutputPacketSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyMinimumInputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertyminimuminputbuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyMinimumInputBufferSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyMinimumInputBufferSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyMinimumOutputBufferSize](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconverterpropertyminimumoutputbuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyMinimumOutputBufferSize: Int { get } ``` |
| To | ``` var kAudioConverterPropertyMinimumOutputBufferSize: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertyOutputCodecParameters](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyoutputcodecparameters)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertyOutputCodecParameters: Int { get } ``` |
| To | ``` var kAudioConverterPropertyOutputCodecParameters: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterPropertySettings](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertysettings)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterPropertySettings: Int { get } ``` |
| To | ``` var kAudioConverterPropertySettings: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterQuality_High](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_high)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterQuality_High: Int { get } ``` |
| To | ``` var kAudioConverterQuality_High: UInt32 { get } ``` |

Modified [kAudioConverterQuality_Low](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterquality_low)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterQuality_Low: Int { get } ``` |
| To | ``` var kAudioConverterQuality_Low: UInt32 { get } ``` |

Modified [kAudioConverterQuality_Max](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_max)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterQuality_Max: Int { get } ``` |
| To | ``` var kAudioConverterQuality_Max: UInt32 { get } ``` |

Modified [kAudioConverterQuality_Medium](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_medium)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterQuality_Medium: Int { get } ``` |
| To | ``` var kAudioConverterQuality_Medium: UInt32 { get } ``` |

Modified [kAudioConverterQuality_Min](https://developer.apple.com/documentation/audiotoolbox/1559924-sample_rate_conversion_quality_i/kaudioconverterquality_min)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterQuality_Min: Int { get } ``` |
| To | ``` var kAudioConverterQuality_Min: UInt32 { get } ``` |

Modified [kAudioConverterSampleRateConverterAlgorithm](https://developer.apple.com/documentation/audiotoolbox/1559928-audio_converter_properties/kaudioconvertersamplerateconverteralgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterAlgorithm: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterAlgorithm: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterSampleRateConverterComplexity](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterComplexity: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterComplexity: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterSampleRateConverterComplexity_Linear](https://developer.apple.com/documentation/audiotoolbox/1559923-sample_rate_conversion_complexit/kaudioconvertersamplerateconvertercomplexity_linear)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterComplexity_Linear: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterComplexity_Linear: UInt32 { get } ``` |

Modified [kAudioConverterSampleRateConverterComplexity_Mastering](https://developer.apple.com/documentation/audiotoolbox/1559923-sample_rate_conversion_complexit/kaudioconvertersamplerateconvertercomplexity_mastering)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterComplexity_Mastering: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterComplexity_Mastering: UInt32 { get } ``` |

Modified [kAudioConverterSampleRateConverterComplexity_Normal](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconvertercomplexity_normal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterComplexity_Normal: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterComplexity_Normal: UInt32 { get } ``` |

Modified [kAudioConverterSampleRateConverterInitialPhase](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconverterinitialphase)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterInitialPhase: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterInitialPhase: AudioConverterPropertyID { get } ``` |

Modified [kAudioConverterSampleRateConverterQuality](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertersamplerateconverterquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioConverterSampleRateConverterQuality: Int { get } ``` |
| To | ``` var kAudioConverterSampleRateConverterQuality: AudioConverterPropertyID { get } ``` |

Modified [kAudioDecoderComponentType](https://developer.apple.com/documentation/audiotoolbox/kaudiodecodercomponenttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDecoderComponentType: Int { get } ``` |
| To | ``` var kAudioDecoderComponentType: UInt32 { get } ``` |

Modified [kAudioEncoderComponentType](https://developer.apple.com/documentation/audiotoolbox/1494086-audio_codec_component_constants/kaudioencodercomponenttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEncoderComponentType: Int { get } ``` |
| To | ``` var kAudioEncoderComponentType: UInt32 { get } ``` |

Modified [kAudioFile3GP2Type](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofile3gp2type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFile3GP2Type: Int { get } ``` |
| To | ``` var kAudioFile3GP2Type: AudioFileTypeID { get } ``` |

Modified [kAudioFile3GPType](https://developer.apple.com/documentation/audiotoolbox/kaudiofile3gptype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFile3GPType: Int { get } ``` |
| To | ``` var kAudioFile3GPType: AudioFileTypeID { get } ``` |

Modified [kAudioFileAAC_ADTSType](https://developer.apple.com/documentation/audiotoolbox/kaudiofileaac_adtstype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileAAC_ADTSType: Int { get } ``` |
| To | ``` var kAudioFileAAC_ADTSType: AudioFileTypeID { get } ``` |

Modified [kAudioFileAC3Type](https://developer.apple.com/documentation/audiotoolbox/kaudiofileac3type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileAC3Type: Int { get } ``` |
| To | ``` var kAudioFileAC3Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileAIFCType](https://developer.apple.com/documentation/audiotoolbox/kaudiofileaifctype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileAIFCType: Int { get } ``` |
| To | ``` var kAudioFileAIFCType: AudioFileTypeID { get } ``` |

Modified [kAudioFileAIFFType](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofileaifftype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileAIFFType: Int { get } ``` |
| To | ``` var kAudioFileAIFFType: AudioFileTypeID { get } ``` |

Modified [kAudioFileAMRType](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofileamrtype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileAMRType: Int { get } ``` |
| To | ``` var kAudioFileAMRType: AudioFileTypeID { get } ``` |

Modified [kAudioFileBadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilebadpropertysizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileBadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioFileBadPropertySizeError: OSStatus { get } ``` |

Modified [kAudioFileCAFType](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilecaftype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileCAFType: Int { get } ``` |
| To | ``` var kAudioFileCAFType: AudioFileTypeID { get } ``` |

Modified [kAudioFileDoesNotAllow64BitDataSizeError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofiledoesnotallow64bitdatasizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileDoesNotAllow64BitDataSizeError: Int { get } ``` |
| To | ``` var kAudioFileDoesNotAllow64BitDataSizeError: OSStatus { get } ``` |

Modified [kAudioFileEndOfFileError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofileendoffileerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileEndOfFileError: Int { get } ``` |
| To | ``` var kAudioFileEndOfFileError: OSStatus { get } ``` |

Modified [kAudioFileFileNotFoundError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilefilenotfounderror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileFileNotFoundError: Int { get } ``` |
| To | ``` var kAudioFileFileNotFoundError: OSStatus { get } ``` |

Modified [kAudioFileGlobalInfo_AllExtensions](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_allextensions)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AllExtensions: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AllExtensions: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_AllHFSTypeCodes](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_allhfstypecodes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AllHFSTypeCodes: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AllHFSTypeCodes: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_AllMIMETypes](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_allmimetypes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AllMIMETypes: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AllMIMETypes: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_AllUTIs](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_allutis)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AllUTIs: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AllUTIs: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_AvailableFormatIDs](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_availableformatids)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AvailableFormatIDs: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AvailableFormatIDs: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_availablestreamdescriptionsforformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_ExtensionsForType](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_extensionsfortype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_ExtensionsForType: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_ExtensionsForType: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_FileTypeName](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_filetypename)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_FileTypeName: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_FileTypeName: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_HFSTypeCodesForType](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_hfstypecodesfortype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_HFSTypeCodesForType: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_HFSTypeCodesForType: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_MIMETypesForType](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_mimetypesfortype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_MIMETypesForType: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_MIMETypesForType: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_ReadableTypes](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_readabletypes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_ReadableTypes: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_ReadableTypes: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_TypesForExtension](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_typesforextension)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_TypesForExtension: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_TypesForExtension: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_TypesForHFSTypeCode](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_typesforhfstypecode)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_TypesForHFSTypeCode: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_TypesForHFSTypeCode: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_TypesForMIMEType](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_typesformimetype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_TypesForMIMEType: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_TypesForMIMEType: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_TypesForUTI](https://developer.apple.com/documentation/audiotoolbox/kaudiofileglobalinfo_typesforuti)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_TypesForUTI: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_TypesForUTI: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_UTIsForType](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_utisfortype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_UTIsForType: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_UTIsForType: AudioFilePropertyID { get } ``` |

Modified [kAudioFileGlobalInfo_WritableTypes](https://developer.apple.com/documentation/audiotoolbox/1576495-audio_file_global_info_propertie/kaudiofileglobalinfo_writabletypes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileGlobalInfo_WritableTypes: Int { get } ``` |
| To | ``` var kAudioFileGlobalInfo_WritableTypes: AudioFilePropertyID { get } ``` |

Modified [kAudioFileInvalidChunkError](https://developer.apple.com/documentation/audiotoolbox/kaudiofileinvalidchunkerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileInvalidChunkError: Int { get } ``` |
| To | ``` var kAudioFileInvalidChunkError: OSStatus { get } ``` |

Modified [kAudioFileInvalidFileError](https://developer.apple.com/documentation/audiotoolbox/kaudiofileinvalidfileerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileInvalidFileError: Int { get } ``` |
| To | ``` var kAudioFileInvalidFileError: OSStatus { get } ``` |

Modified [kAudioFileInvalidPacketOffsetError](https://developer.apple.com/documentation/audiotoolbox/kaudiofileinvalidpacketoffseterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileInvalidPacketOffsetError: Int { get } ``` |
| To | ``` var kAudioFileInvalidPacketOffsetError: OSStatus { get } ``` |

Modified [kAudioFileLoopDirection_Backward](https://developer.apple.com/documentation/audiotoolbox/kaudiofileloopdirection_backward)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileLoopDirection_Backward: Int { get } ``` |
| To | ``` var kAudioFileLoopDirection_Backward: UInt32 { get } ``` |

Modified [kAudioFileLoopDirection_Forward](https://developer.apple.com/documentation/audiotoolbox/kaudiofileloopdirection_forward)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileLoopDirection_Forward: Int { get } ``` |
| To | ``` var kAudioFileLoopDirection_Forward: UInt32 { get } ``` |

Modified [kAudioFileLoopDirection_ForwardAndBackward](https://developer.apple.com/documentation/audiotoolbox/1576494-audio_file_loop_direction_consta/kaudiofileloopdirection_forwardandbackward)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileLoopDirection_ForwardAndBackward: Int { get } ``` |
| To | ``` var kAudioFileLoopDirection_ForwardAndBackward: UInt32 { get } ``` |

Modified [kAudioFileLoopDirection_NoLooping](https://developer.apple.com/documentation/audiotoolbox/kaudiofileloopdirection_nolooping)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileLoopDirection_NoLooping: Int { get } ``` |
| To | ``` var kAudioFileLoopDirection_NoLooping: UInt32 { get } ``` |

Modified [kAudioFileM4AType](https://developer.apple.com/documentation/audiotoolbox/kaudiofilem4atype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileM4AType: Int { get } ``` |
| To | ``` var kAudioFileM4AType: AudioFileTypeID { get } ``` |

Modified [kAudioFileM4BType](https://developer.apple.com/documentation/audiotoolbox/kaudiofilem4btype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileM4BType: Int { get } ``` |
| To | ``` var kAudioFileM4BType: AudioFileTypeID { get } ``` |

Modified [kAudioFileMarkerType_Generic](https://developer.apple.com/documentation/audiotoolbox/1576492-audio_file_marker_types/kaudiofilemarkertype_generic)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileMarkerType_Generic: Int { get } ``` |
| To | ``` var kAudioFileMarkerType_Generic: UInt32 { get } ``` |

Modified [kAudioFileMP1Type](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilemp1type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileMP1Type: Int { get } ``` |
| To | ``` var kAudioFileMP1Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileMP2Type](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilemp2type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileMP2Type: Int { get } ``` |
| To | ``` var kAudioFileMP2Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileMP3Type](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilemp3type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileMP3Type: Int { get } ``` |
| To | ``` var kAudioFileMP3Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileMPEG4Type](https://developer.apple.com/documentation/audiotoolbox/kaudiofilempeg4type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileMPEG4Type: Int { get } ``` |
| To | ``` var kAudioFileMPEG4Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileNextType](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilenexttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileNextType: Int { get } ``` |
| To | ``` var kAudioFileNextType: AudioFileTypeID { get } ``` |

Modified [kAudioFileNotOpenError](https://developer.apple.com/documentation/audiotoolbox/kaudiofilenotopenerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileNotOpenError: Int { get } ``` |
| To | ``` var kAudioFileNotOpenError: OSStatus { get } ``` |

Modified [kAudioFileNotOptimizedError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilenotoptimizederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileNotOptimizedError: Int { get } ``` |
| To | ``` var kAudioFileNotOptimizedError: OSStatus { get } ``` |

Modified [kAudioFileOperationNotSupportedError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofileoperationnotsupportederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileOperationNotSupportedError: Int { get } ``` |
| To | ``` var kAudioFileOperationNotSupportedError: OSStatus { get } ``` |

Modified [kAudioFilePermissionsError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofilepermissionserror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePermissionsError: Int { get } ``` |
| To | ``` var kAudioFilePermissionsError: OSStatus { get } ``` |

Modified [kAudioFilePositionError](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepositionerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePositionError: Int { get } ``` |
| To | ``` var kAudioFilePositionError: OSStatus { get } ``` |

Modified [kAudioFilePropertyAlbumArtwork](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyalbumartwork)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyAlbumArtwork: Int { get } ``` |
| To | ``` var kAudioFilePropertyAlbumArtwork: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyAudioDataByteCount](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyaudiodatabytecount)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyAudioDataByteCount: Int { get } ``` |
| To | ``` var kAudioFilePropertyAudioDataByteCount: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyAudioDataPacketCount](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyaudiodatapacketcount)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyAudioDataPacketCount: Int { get } ``` |
| To | ``` var kAudioFilePropertyAudioDataPacketCount: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyAudioTrackCount](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyaudiotrackcount)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyAudioTrackCount: Int { get } ``` |
| To | ``` var kAudioFilePropertyAudioTrackCount: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyBitRate](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertybitrate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyBitRate: Int { get } ``` |
| To | ``` var kAudioFilePropertyBitRate: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyByteToPacket](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertybytetopacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyByteToPacket: Int { get } ``` |
| To | ``` var kAudioFilePropertyByteToPacket: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertychannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyChannelLayout: Int { get } ``` |
| To | ``` var kAudioFilePropertyChannelLayout: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyChunkIDs](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertychunkids)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyChunkIDs: Int { get } ``` |
| To | ``` var kAudioFilePropertyChunkIDs: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyDataFormat](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertydataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyDataFormat: Int { get } ``` |
| To | ``` var kAudioFilePropertyDataFormat: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyDataFormatName](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertydataformatname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyDataFormatName: Int { get } ``` |
| To | ``` var kAudioFilePropertyDataFormatName: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyDataOffset](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertydataoffset)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyDataOffset: Int { get } ``` |
| To | ``` var kAudioFilePropertyDataOffset: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyDeferSizeUpdates](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertydefersizeupdates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyDeferSizeUpdates: Int { get } ``` |
| To | ``` var kAudioFilePropertyDeferSizeUpdates: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyEstimatedDuration](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyestimatedduration)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyEstimatedDuration: Int { get } ``` |
| To | ``` var kAudioFilePropertyEstimatedDuration: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyFileFormat](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyfileformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyFileFormat: Int { get } ``` |
| To | ``` var kAudioFilePropertyFileFormat: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyFormatList](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyformatlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyFormatList: Int { get } ``` |
| To | ``` var kAudioFilePropertyFormatList: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyFrameToPacket](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyframetopacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyFrameToPacket: Int { get } ``` |
| To | ``` var kAudioFilePropertyFrameToPacket: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyID3Tag](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyid3tag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyID3Tag: Int { get } ``` |
| To | ``` var kAudioFilePropertyID3Tag: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyInfoDictionary](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyinfodictionary)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyInfoDictionary: Int { get } ``` |
| To | ``` var kAudioFilePropertyInfoDictionary: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyIsOptimized](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyisoptimized)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyIsOptimized: Int { get } ``` |
| To | ``` var kAudioFilePropertyIsOptimized: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyMagicCookieData](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertymagiccookiedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyMagicCookieData: Int { get } ``` |
| To | ``` var kAudioFilePropertyMagicCookieData: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyMarkerList](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertymarkerlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyMarkerList: Int { get } ``` |
| To | ``` var kAudioFilePropertyMarkerList: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyMaximumPacketSize](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertymaximumpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyMaximumPacketSize: Int { get } ``` |
| To | ``` var kAudioFilePropertyMaximumPacketSize: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyPacketSizeUpperBound](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertypacketsizeupperbound)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyPacketSizeUpperBound: Int { get } ``` |
| To | ``` var kAudioFilePropertyPacketSizeUpperBound: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyPacketTableInfo](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertypackettableinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyPacketTableInfo: Int { get } ``` |
| To | ``` var kAudioFilePropertyPacketTableInfo: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyPacketToByte](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertypackettobyte)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyPacketToByte: Int { get } ``` |
| To | ``` var kAudioFilePropertyPacketToByte: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyPacketToFrame](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertypackettoframe)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyPacketToFrame: Int { get } ``` |
| To | ``` var kAudioFilePropertyPacketToFrame: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyRegionList](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyregionlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyRegionList: Int { get } ``` |
| To | ``` var kAudioFilePropertyRegionList: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyReserveDuration](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyreserveduration)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyReserveDuration: Int { get } ``` |
| To | ``` var kAudioFilePropertyReserveDuration: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertySourceBitDepth](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertysourcebitdepth)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertySourceBitDepth: Int { get } ``` |
| To | ``` var kAudioFilePropertySourceBitDepth: AudioFilePropertyID { get } ``` |

Modified [kAudioFilePropertyUseAudioTrack](https://developer.apple.com/documentation/audiotoolbox/1576499-audio_file_properties/kaudiofilepropertyuseaudiotrack)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFilePropertyUseAudioTrack: Int { get } ``` |
| To | ``` var kAudioFilePropertyUseAudioTrack: AudioFilePropertyID { get } ``` |

Modified [kAudioFileSoundDesigner2Type](https://developer.apple.com/documentation/audiotoolbox/kaudiofilesounddesigner2type)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileSoundDesigner2Type: Int { get } ``` |
| To | ``` var kAudioFileSoundDesigner2Type: AudioFileTypeID { get } ``` |

Modified [kAudioFileStreamError_BadPropertySize](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_badpropertysize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_BadPropertySize: Int { get } ``` |
| To | ``` var kAudioFileStreamError_BadPropertySize: OSStatus { get } ``` |

Modified [kAudioFileStreamError_DataUnavailable](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_dataunavailable)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_DataUnavailable: Int { get } ``` |
| To | ``` var kAudioFileStreamError_DataUnavailable: OSStatus { get } ``` |

Modified [kAudioFileStreamError_DiscontinuityCantRecover](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_discontinuitycantrecover)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_DiscontinuityCantRecover: Int { get } ``` |
| To | ``` var kAudioFileStreamError_DiscontinuityCantRecover: OSStatus { get } ``` |

Modified [kAudioFileStreamError_IllegalOperation](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_illegaloperation)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_IllegalOperation: Int { get } ``` |
| To | ``` var kAudioFileStreamError_IllegalOperation: OSStatus { get } ``` |

Modified [kAudioFileStreamError_InvalidFile](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_invalidfile)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_InvalidFile: Int { get } ``` |
| To | ``` var kAudioFileStreamError_InvalidFile: OSStatus { get } ``` |

Modified [kAudioFileStreamError_InvalidPacketOffset](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_invalidpacketoffset)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_InvalidPacketOffset: Int { get } ``` |
| To | ``` var kAudioFileStreamError_InvalidPacketOffset: OSStatus { get } ``` |

Modified [kAudioFileStreamError_NotOptimized](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_notoptimized)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_NotOptimized: Int { get } ``` |
| To | ``` var kAudioFileStreamError_NotOptimized: OSStatus { get } ``` |

Modified [kAudioFileStreamError_UnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_unspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_UnspecifiedError: Int { get } ``` |
| To | ``` var kAudioFileStreamError_UnspecifiedError: OSStatus { get } ``` |

Modified [kAudioFileStreamError_UnsupportedDataFormat](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_unsupporteddataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_UnsupportedDataFormat: Int { get } ``` |
| To | ``` var kAudioFileStreamError_UnsupportedDataFormat: OSStatus { get } ``` |

Modified [kAudioFileStreamError_UnsupportedFileType](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_unsupportedfiletype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_UnsupportedFileType: Int { get } ``` |
| To | ``` var kAudioFileStreamError_UnsupportedFileType: OSStatus { get } ``` |

Modified [kAudioFileStreamError_UnsupportedProperty](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamerror_unsupportedproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_UnsupportedProperty: Int { get } ``` |
| To | ``` var kAudioFileStreamError_UnsupportedProperty: OSStatus { get } ``` |

Modified [kAudioFileStreamError_ValueUnknown](https://developer.apple.com/documentation/audiotoolbox/1391572-anonymous/kaudiofilestreamerror_valueunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamError_ValueUnknown: Int { get } ``` |
| To | ``` var kAudioFileStreamError_ValueUnknown: OSStatus { get } ``` |

Modified [kAudioFileStreamProperty_AudioDataByteCount](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_audiodatabytecount)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_AudioDataByteCount: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_AudioDataByteCount: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_AudioDataPacketCount](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_audiodatapacketcount)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_AudioDataPacketCount: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_AudioDataPacketCount: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_AverageBytesPerPacket](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_averagebytesperpacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_AverageBytesPerPacket: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_AverageBytesPerPacket: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_BitRate](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_bitrate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_BitRate: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_BitRate: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_ByteToPacket](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_bytetopacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_ByteToPacket: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_ByteToPacket: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_ChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_channellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_ChannelLayout: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_ChannelLayout: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_DataFormat](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_dataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_DataFormat: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_DataFormat: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_DataOffset](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_dataoffset)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_DataOffset: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_DataOffset: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_FileFormat](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_fileformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_FileFormat: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_FileFormat: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_FormatList](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_formatlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_FormatList: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_FormatList: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_FrameToPacket](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_frametopacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_FrameToPacket: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_FrameToPacket: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_InfoDictionary](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_infodictionary)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_InfoDictionary: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_InfoDictionary: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_MagicCookieData](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_magiccookiedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_MagicCookieData: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_MagicCookieData: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_MaximumPacketSize](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_maximumpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_MaximumPacketSize: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_MaximumPacketSize: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_PacketSizeUpperBound](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_packetsizeupperbound)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_PacketSizeUpperBound: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_PacketSizeUpperBound: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_PacketTableInfo](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_packettableinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_PacketTableInfo: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_PacketTableInfo: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_PacketToByte](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_packettobyte)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_PacketToByte: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_PacketToByte: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_PacketToFrame](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_packettoframe)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_PacketToFrame: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_PacketToFrame: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileStreamProperty_ReadyToProducePackets](https://developer.apple.com/documentation/audiotoolbox/1391506-audio_file_stream_properties/kaudiofilestreamproperty_readytoproducepackets)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileStreamProperty_ReadyToProducePackets: Int { get } ``` |
| To | ``` var kAudioFileStreamProperty_ReadyToProducePackets: AudioFileStreamPropertyID { get } ``` |

Modified [kAudioFileUnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofileunspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileUnspecifiedError: Int { get } ``` |
| To | ``` var kAudioFileUnspecifiedError: OSStatus { get } ``` |

Modified [kAudioFileUnsupportedDataFormatError](https://developer.apple.com/documentation/audiotoolbox/1576500-anonymous/kaudiofileunsupporteddataformaterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileUnsupportedDataFormatError: Int { get } ``` |
| To | ``` var kAudioFileUnsupportedDataFormatError: OSStatus { get } ``` |

Modified [kAudioFileUnsupportedFileTypeError](https://developer.apple.com/documentation/audiotoolbox/kaudiofileunsupportedfiletypeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileUnsupportedFileTypeError: Int { get } ``` |
| To | ``` var kAudioFileUnsupportedFileTypeError: OSStatus { get } ``` |

Modified [kAudioFileUnsupportedPropertyError](https://developer.apple.com/documentation/audiotoolbox/kaudiofileunsupportedpropertyerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileUnsupportedPropertyError: Int { get } ``` |
| To | ``` var kAudioFileUnsupportedPropertyError: OSStatus { get } ``` |

Modified [kAudioFileWAVEType](https://developer.apple.com/documentation/audiotoolbox/1576497-anonymous/kaudiofilewavetype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFileWAVEType: Int { get } ``` |
| To | ``` var kAudioFileWAVEType: AudioFileTypeID { get } ``` |

Modified [kAudioFormatBadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/1577851-anonymous/kaudioformatbadpropertysizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatBadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioFormatBadPropertySizeError: OSStatus { get } ``` |

Modified [kAudioFormatBadSpecifierSizeError](https://developer.apple.com/documentation/audiotoolbox/1577851-anonymous/kaudioformatbadspecifiersizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatBadSpecifierSizeError: Int { get } ``` |
| To | ``` var kAudioFormatBadSpecifierSizeError: OSStatus { get } ``` |

Modified [kAudioFormatProperty_AreChannelLayoutsEquivalent](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_arechannellayoutsequivalent)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_AreChannelLayoutsEquivalent: Int { get } ``` |
| To | ``` var kAudioFormatProperty_AreChannelLayoutsEquivalent: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ASBDFromESDS](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_asbdfromesds)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ASBDFromESDS: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ASBDFromESDS: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ASBDFromMPEGPacket](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_asbdfrommpegpacket)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ASBDFromMPEGPacket: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ASBDFromMPEGPacket: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_AvailableEncodeBitRates](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_availableencodebitrates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_AvailableEncodeBitRates: Int { get } ``` |
| To | ``` var kAudioFormatProperty_AvailableEncodeBitRates: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_AvailableEncodeChannelLayoutTags](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_availableencodechannellayouttags)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_AvailableEncodeChannelLayoutTags: Int { get } ``` |
| To | ``` var kAudioFormatProperty_AvailableEncodeChannelLayoutTags: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_AvailableEncodeNumberChannels](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_availableencodenumberchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_AvailableEncodeNumberChannels: Int { get } ``` |
| To | ``` var kAudioFormatProperty_AvailableEncodeNumberChannels: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_AvailableEncodeSampleRates](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_availableencodesamplerates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_AvailableEncodeSampleRates: Int { get } ``` |
| To | ``` var kAudioFormatProperty_AvailableEncodeSampleRates: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_BalanceFade](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_balancefade)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_BalanceFade: Int { get } ``` |
| To | ``` var kAudioFormatProperty_BalanceFade: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_BitmapForLayoutTag](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_bitmapforlayouttag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_BitmapForLayoutTag: Int { get } ``` |
| To | ``` var kAudioFormatProperty_BitmapForLayoutTag: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutForBitmap](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channellayoutforbitmap)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutForBitmap: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutForBitmap: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutForTag](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channellayoutfortag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutForTag: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutForTag: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutFromESDS](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_channellayoutfromesds)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutFromESDS: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutFromESDS: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutHash](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channellayouthash)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutHash: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutHash: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutName](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_channellayoutname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutName: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutName: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelLayoutSimpleName](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channellayoutsimplename)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelLayoutSimpleName: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelLayoutSimpleName: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelMap](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channelmap)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelMap: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelMap: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelName](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_channelname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelName: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelName: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ChannelShortName](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_channelshortname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ChannelShortName: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ChannelShortName: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_DecodeFormatIDs](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_decodeformatids)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_DecodeFormatIDs: Int { get } ``` |
| To | ``` var kAudioFormatProperty_DecodeFormatIDs: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_Decoders](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_decoders)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_Decoders: Int { get } ``` |
| To | ``` var kAudioFormatProperty_Decoders: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_EncodeFormatIDs](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_encodeformatids)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_EncodeFormatIDs: Int { get } ``` |
| To | ``` var kAudioFormatProperty_EncodeFormatIDs: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_Encoders](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_encoders)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_Encoders: Int { get } ``` |
| To | ``` var kAudioFormatProperty_Encoders: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FirstPlayableFormatFromList](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_firstplayableformatfromlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FirstPlayableFormatFromList: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FirstPlayableFormatFromList: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatInfo](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_formatinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatInfo: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatInfo: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatIsEncrypted](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_formatisencrypted)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatIsEncrypted: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatIsEncrypted: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatIsExternallyFramed](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_formatisexternallyframed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatIsExternallyFramed: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatIsExternallyFramed: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatIsVBR](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_formatisvbr)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatIsVBR: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatIsVBR: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatList](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_formatlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatList: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatList: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_FormatName](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_formatname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_FormatName: Int { get } ``` |
| To | ``` var kAudioFormatProperty_FormatName: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_HardwareCodecCapabilities](https://developer.apple.com/documentation/audiotoolbox/1620452-hardware_codec_capabilities/kaudioformatproperty_hardwarecodeccapabilities)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_HardwareCodecCapabilities: Int { get } ``` |
| To | ``` var kAudioFormatProperty_HardwareCodecCapabilities: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ID3TagSize](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_id3tagsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ID3TagSize: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ID3TagSize: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ID3TagToDictionary](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_id3tagtodictionary)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ID3TagToDictionary: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ID3TagToDictionary: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_MatrixMixMap](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_matrixmixmap)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_MatrixMixMap: Int { get } ``` |
| To | ``` var kAudioFormatProperty_MatrixMixMap: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_NumberOfChannelsForLayout](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_numberofchannelsforlayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_NumberOfChannelsForLayout: Int { get } ``` |
| To | ``` var kAudioFormatProperty_NumberOfChannelsForLayout: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_OutputFormatList](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_outputformatlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_OutputFormatList: Int { get } ``` |
| To | ``` var kAudioFormatProperty_OutputFormatList: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_PanningMatrix](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_panningmatrix)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_PanningMatrix: Int { get } ``` |
| To | ``` var kAudioFormatProperty_PanningMatrix: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_TagForChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_tagforchannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_TagForChannelLayout: Int { get } ``` |
| To | ``` var kAudioFormatProperty_TagForChannelLayout: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_TagsForNumberOfChannels](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_tagsfornumberofchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_TagsForNumberOfChannels: Int { get } ``` |
| To | ``` var kAudioFormatProperty_TagsForNumberOfChannels: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatProperty_ValidateChannelLayout](https://developer.apple.com/documentation/audiotoolbox/1577853-audio_format_property_identifier/kaudioformatproperty_validatechannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatProperty_ValidateChannelLayout: Int { get } ``` |
| To | ``` var kAudioFormatProperty_ValidateChannelLayout: AudioFormatPropertyID { get } ``` |

Modified [kAudioFormatUnknownFormatError](https://developer.apple.com/documentation/audiotoolbox/1577851-anonymous/kaudioformatunknownformaterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatUnknownFormatError: Int { get } ``` |
| To | ``` var kAudioFormatUnknownFormatError: OSStatus { get } ``` |

Modified [kAudioFormatUnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudioformatunspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatUnspecifiedError: Int { get } ``` |
| To | ``` var kAudioFormatUnspecifiedError: OSStatus { get } ``` |

Modified [kAudioFormatUnsupportedDataFormatError](https://developer.apple.com/documentation/audiotoolbox/kaudioformatunsupporteddataformaterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatUnsupportedDataFormatError: Int { get } ``` |
| To | ``` var kAudioFormatUnsupportedDataFormatError: OSStatus { get } ``` |

Modified [kAudioFormatUnsupportedPropertyError](https://developer.apple.com/documentation/audiotoolbox/1577851-anonymous/kaudioformatunsupportedpropertyerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatUnsupportedPropertyError: Int { get } ``` |
| To | ``` var kAudioFormatUnsupportedPropertyError: OSStatus { get } ``` |

Modified [kAudioQueueDeviceProperty_NumberChannels](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuedeviceproperty_numberchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueDeviceProperty_NumberChannels: Int { get } ``` |
| To | ``` var kAudioQueueDeviceProperty_NumberChannels: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueDeviceProperty_SampleRate](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuedeviceproperty_samplerate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueDeviceProperty_SampleRate: Int { get } ``` |
| To | ``` var kAudioQueueDeviceProperty_SampleRate: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueErr_BufferEmpty](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_bufferempty)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_BufferEmpty: Int { get } ``` |
| To | ``` var kAudioQueueErr_BufferEmpty: OSStatus { get } ``` |

Modified [kAudioQueueErr_BufferEnqueuedTwice](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_bufferenqueuedtwice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_BufferEnqueuedTwice: Int { get } ``` |
| To | ``` var kAudioQueueErr_BufferEnqueuedTwice: OSStatus { get } ``` |

Modified [kAudioQueueErr_BufferInQueue](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_bufferinqueue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_BufferInQueue: Int { get } ``` |
| To | ``` var kAudioQueueErr_BufferInQueue: OSStatus { get } ``` |

Modified [kAudioQueueErr_CannotStart](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_cannotstart)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_CannotStart: Int { get } ``` |
| To | ``` var kAudioQueueErr_CannotStart: OSStatus { get } ``` |

Modified [kAudioQueueErr_CodecNotFound](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_codecnotfound)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_CodecNotFound: Int { get } ``` |
| To | ``` var kAudioQueueErr_CodecNotFound: OSStatus { get } ``` |

Modified [kAudioQueueErr_DisposalPending](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_disposalpending)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_DisposalPending: Int { get } ``` |
| To | ``` var kAudioQueueErr_DisposalPending: OSStatus { get } ``` |

Modified [kAudioQueueErr_EnqueueDuringReset](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_enqueueduringreset)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_EnqueueDuringReset: Int { get } ``` |
| To | ``` var kAudioQueueErr_EnqueueDuringReset: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidBuffer](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidBuffer: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidBuffer: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidCodecAccess](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidcodecaccess)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidCodecAccess: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidCodecAccess: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidDevice](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invaliddevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidDevice: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidDevice: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidOfflineMode](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidofflinemode)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidOfflineMode: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidOfflineMode: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidParameter](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidParameter: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidParameter: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidProperty](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidProperty: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidProperty: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidPropertySize](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidpropertysize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidPropertySize: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidPropertySize: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidPropertyValue](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidpropertyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidPropertyValue: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidPropertyValue: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidQueueType](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidqueuetype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidQueueType: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidQueueType: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidRunState](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidrunstate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidRunState: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidRunState: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidTapContext](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_invalidtapcontext)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidTapContext: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidTapContext: OSStatus { get } ``` |

Modified [kAudioQueueErr_InvalidTapType](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_invalidtaptype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_InvalidTapType: Int { get } ``` |
| To | ``` var kAudioQueueErr_InvalidTapType: OSStatus { get } ``` |

Modified [kAudioQueueErr_Permissions](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_permissions)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_Permissions: Int { get } ``` |
| To | ``` var kAudioQueueErr_Permissions: OSStatus { get } ``` |

Modified [kAudioQueueErr_PrimeTimedOut](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_primetimedout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_PrimeTimedOut: Int { get } ``` |
| To | ``` var kAudioQueueErr_PrimeTimedOut: OSStatus { get } ``` |

Modified [kAudioQueueErr_QueueInvalidated](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_queueinvalidated)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_QueueInvalidated: Int { get } ``` |
| To | ``` var kAudioQueueErr_QueueInvalidated: OSStatus { get } ``` |

Modified [kAudioQueueErr_RecordUnderrun](https://developer.apple.com/documentation/audiotoolbox/1552627-anonymous/kaudioqueueerr_recordunderrun)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_RecordUnderrun: Int { get } ``` |
| To | ``` var kAudioQueueErr_RecordUnderrun: OSStatus { get } ``` |

Modified [kAudioQueueErr_TooManyTaps](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueerr_toomanytaps)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueErr_TooManyTaps: Int { get } ``` |
| To | ``` var kAudioQueueErr_TooManyTaps: OSStatus { get } ``` |

Modified [kAudioQueueHardwareCodecPolicy_Default](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuehardwarecodecpolicy_default)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueHardwareCodecPolicy_Default: Int { get } ``` |
| To | ``` var kAudioQueueHardwareCodecPolicy_Default: UInt32 { get } ``` |

Modified [kAudioQueueHardwareCodecPolicy_PreferHardware](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_preferhardware)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueHardwareCodecPolicy_PreferHardware: Int { get } ``` |
| To | ``` var kAudioQueueHardwareCodecPolicy_PreferHardware: UInt32 { get } ``` |

Modified [kAudioQueueHardwareCodecPolicy_PreferSoftware](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_prefersoftware)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueHardwareCodecPolicy_PreferSoftware: Int { get } ``` |
| To | ``` var kAudioQueueHardwareCodecPolicy_PreferSoftware: UInt32 { get } ``` |

Modified [kAudioQueueHardwareCodecPolicy_UseHardwareOnly](https://developer.apple.com/documentation/audiotoolbox/1618727-anonymous/kaudioqueuehardwarecodecpolicy_usehardwareonly)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueHardwareCodecPolicy_UseHardwareOnly: Int { get } ``` |
| To | ``` var kAudioQueueHardwareCodecPolicy_UseHardwareOnly: UInt32 { get } ``` |

Modified [kAudioQueueHardwareCodecPolicy_UseSoftwareOnly](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuehardwarecodecpolicy_usesoftwareonly)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueHardwareCodecPolicy_UseSoftwareOnly: Int { get } ``` |
| To | ``` var kAudioQueueHardwareCodecPolicy_UseSoftwareOnly: UInt32 { get } ``` |

Modified [kAudioQueueParam_Pan](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_pan)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueParam_Pan: Int { get } ``` |
| To | ``` var kAudioQueueParam_Pan: AudioQueueParameterID { get } ``` |

Modified [kAudioQueueParam_Pitch](https://developer.apple.com/documentation/audiotoolbox/1552626-audio_queue_parameters/kaudioqueueparam_pitch)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueParam_Pitch: Int { get } ``` |
| To | ``` var kAudioQueueParam_Pitch: AudioQueueParameterID { get } ``` |

Modified [kAudioQueueParam_PlayRate](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_playrate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueParam_PlayRate: Int { get } ``` |
| To | ``` var kAudioQueueParam_PlayRate: AudioQueueParameterID { get } ``` |

Modified [kAudioQueueParam_Volume](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_volume)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueParam_Volume: Int { get } ``` |
| To | ``` var kAudioQueueParam_Volume: AudioQueueParameterID { get } ``` |

Modified [kAudioQueueParam_VolumeRampTime](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_volumeramptime)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueParam_VolumeRampTime: Int { get } ``` |
| To | ``` var kAudioQueueParam_VolumeRampTime: AudioQueueParameterID { get } ``` |

Modified [kAudioQueueProperty_ChannelAssignments](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_channelassignments)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_ChannelAssignments: Int { get } ``` |
| To | ``` var kAudioQueueProperty_ChannelAssignments: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_ChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_channellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_ChannelLayout: Int { get } ``` |
| To | ``` var kAudioQueueProperty_ChannelLayout: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_ConverterError](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_convertererror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_ConverterError: Int { get } ``` |
| To | ``` var kAudioQueueProperty_ConverterError: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_CurrentDevice](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_currentdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_CurrentDevice: Int { get } ``` |
| To | ``` var kAudioQueueProperty_CurrentDevice: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_CurrentLevelMeter](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_currentlevelmeter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_CurrentLevelMeter: Int { get } ``` |
| To | ``` var kAudioQueueProperty_CurrentLevelMeter: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_CurrentLevelMeterDB](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_currentlevelmeterdb)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_CurrentLevelMeterDB: Int { get } ``` |
| To | ``` var kAudioQueueProperty_CurrentLevelMeterDB: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_DecodeBufferSizeFrames](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_decodebuffersizeframes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_DecodeBufferSizeFrames: Int { get } ``` |
| To | ``` var kAudioQueueProperty_DecodeBufferSizeFrames: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_EnableLevelMetering](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_enablelevelmetering)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_EnableLevelMetering: Int { get } ``` |
| To | ``` var kAudioQueueProperty_EnableLevelMetering: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_EnableTimePitch](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_enabletimepitch)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_EnableTimePitch: Int { get } ``` |
| To | ``` var kAudioQueueProperty_EnableTimePitch: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_HardwareCodecPolicy](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_hardwarecodecpolicy)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_HardwareCodecPolicy: Int { get } ``` |
| To | ``` var kAudioQueueProperty_HardwareCodecPolicy: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_IsRunning](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_isrunning)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_IsRunning: Int { get } ``` |
| To | ``` var kAudioQueueProperty_IsRunning: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_MagicCookie](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_magiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_MagicCookie: Int { get } ``` |
| To | ``` var kAudioQueueProperty_MagicCookie: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_MaximumOutputPacketSize](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_maximumoutputpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_MaximumOutputPacketSize: Int { get } ``` |
| To | ``` var kAudioQueueProperty_MaximumOutputPacketSize: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_StreamDescription](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_streamdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_StreamDescription: Int { get } ``` |
| To | ``` var kAudioQueueProperty_StreamDescription: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_TimePitchAlgorithm](https://developer.apple.com/documentation/audiotoolbox/1552629-anonymous/kaudioqueueproperty_timepitchalgorithm)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_TimePitchAlgorithm: Int { get } ``` |
| To | ``` var kAudioQueueProperty_TimePitchAlgorithm: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueProperty_TimePitchBypass](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueproperty_timepitchbypass)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueProperty_TimePitchBypass: Int { get } ``` |
| To | ``` var kAudioQueueProperty_TimePitchBypass: AudioQueuePropertyID { get } ``` |

Modified [kAudioQueueTimePitchAlgorithm_LowQualityZeroLatency](https://developer.apple.com/documentation/audiotoolbox/1618742-anonymous/kaudioqueuetimepitchalgorithm_lowqualityzerolatency)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueTimePitchAlgorithm_LowQualityZeroLatency: Int { get } ``` |
| To | ``` var kAudioQueueTimePitchAlgorithm_LowQualityZeroLatency: UInt32 { get } ``` |

Modified [kAudioQueueTimePitchAlgorithm_Spectral](https://developer.apple.com/documentation/audiotoolbox/1552630-anonymous/kaudioqueuetimepitchalgorithm_spectral)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueTimePitchAlgorithm_Spectral: Int { get } ``` |
| To | ``` var kAudioQueueTimePitchAlgorithm_Spectral: UInt32 { get } ``` |

Modified [kAudioQueueTimePitchAlgorithm_TimeDomain](https://developer.apple.com/documentation/audiotoolbox/1552630-anonymous/kaudioqueuetimepitchalgorithm_timedomain)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueTimePitchAlgorithm_TimeDomain: Int { get } ``` |
| To | ``` var kAudioQueueTimePitchAlgorithm_TimeDomain: UInt32 { get } ``` |

Modified [kAudioQueueTimePitchAlgorithm_Varispeed](https://developer.apple.com/documentation/audiotoolbox/kaudioqueuetimepitchalgorithm_varispeed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioQueueTimePitchAlgorithm_Varispeed: Int { get } ``` |
| To | ``` var kAudioQueueTimePitchAlgorithm_Varispeed: UInt32 { get } ``` |

Modified [kAudioServicesBadPropertySizeError](https://developer.apple.com/documentation/audiotoolbox/1405232-anonymous/kaudioservicesbadpropertysizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesBadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioServicesBadPropertySizeError: OSStatus { get } ``` |

Modified [kAudioServicesBadSpecifierSizeError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicesbadspecifiersizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesBadSpecifierSizeError: Int { get } ``` |
| To | ``` var kAudioServicesBadSpecifierSizeError: OSStatus { get } ``` |

Modified [kAudioServicesNoError](https://developer.apple.com/documentation/audiotoolbox/1405232-anonymous/kaudioservicesnoerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesNoError: Int { get } ``` |
| To | ``` var kAudioServicesNoError: OSStatus { get } ``` |

Modified [kAudioServicesPropertyCompletePlaybackIfAppDies](https://developer.apple.com/documentation/audiotoolbox/1405268-system_sound_services_property_i/kaudioservicespropertycompleteplaybackifappdies)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesPropertyCompletePlaybackIfAppDies: Int { get } ``` |
| To | ``` var kAudioServicesPropertyCompletePlaybackIfAppDies: AudioServicesPropertyID { get } ``` |

Modified [kAudioServicesPropertyIsUISound](https://developer.apple.com/documentation/audiotoolbox/kaudioservicespropertyisuisound)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesPropertyIsUISound: Int { get } ``` |
| To | ``` var kAudioServicesPropertyIsUISound: AudioServicesPropertyID { get } ``` |

Modified [kAudioServicesSystemSoundClientTimedOutError](https://developer.apple.com/documentation/audiotoolbox/1405232-anonymous/kaudioservicessystemsoundclienttimedouterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesSystemSoundClientTimedOutError: Int { get } ``` |
| To | ``` var kAudioServicesSystemSoundClientTimedOutError: OSStatus { get } ``` |

Modified [kAudioServicesSystemSoundUnspecifiedError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicessystemsoundunspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesSystemSoundUnspecifiedError: Int { get } ``` |
| To | ``` var kAudioServicesSystemSoundUnspecifiedError: OSStatus { get } ``` |

Modified [kAudioServicesUnsupportedPropertyError](https://developer.apple.com/documentation/audiotoolbox/kaudioservicesunsupportedpropertyerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioServicesUnsupportedPropertyError: Int { get } ``` |
| To | ``` var kAudioServicesUnsupportedPropertyError: OSStatus { get } ``` |

Modified [kAudioToolboxErr_CannotDoInCurrentContext](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_cannotdoincurrentcontext)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_CannotDoInCurrentContext: Int { get } ``` |
| To | ``` var kAudioToolboxErr_CannotDoInCurrentContext: OSStatus { get } ``` |

Modified [kAudioToolboxErr_EndOfTrack](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_endoftrack)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_EndOfTrack: Int { get } ``` |
| To | ``` var kAudioToolboxErr_EndOfTrack: OSStatus { get } ``` |

Modified [kAudioToolboxErr_IllegalTrackDestination](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_illegaltrackdestination)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_IllegalTrackDestination: Int { get } ``` |
| To | ``` var kAudioToolboxErr_IllegalTrackDestination: OSStatus { get } ``` |

Modified [kAudioToolboxErr_InvalidEventType](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_invalideventtype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_InvalidEventType: Int { get } ``` |
| To | ``` var kAudioToolboxErr_InvalidEventType: OSStatus { get } ``` |

Modified [kAudioToolboxErr_InvalidPlayerState](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_invalidplayerstate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_InvalidPlayerState: Int { get } ``` |
| To | ``` var kAudioToolboxErr_InvalidPlayerState: OSStatus { get } ``` |

Modified [kAudioToolboxErr_InvalidSequenceType](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_invalidsequencetype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_InvalidSequenceType: Int { get } ``` |
| To | ``` var kAudioToolboxErr_InvalidSequenceType: OSStatus { get } ``` |

Modified [kAudioToolboxErr_NoSequence](https://developer.apple.com/documentation/audiotoolbox/kaudiotoolboxerr_nosequence)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_NoSequence: Int { get } ``` |
| To | ``` var kAudioToolboxErr_NoSequence: OSStatus { get } ``` |

Modified [kAudioToolboxErr_StartOfTrack](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_startoftrack)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_StartOfTrack: Int { get } ``` |
| To | ``` var kAudioToolboxErr_StartOfTrack: OSStatus { get } ``` |

Modified [kAudioToolboxErr_TrackIndexError](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_trackindexerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_TrackIndexError: Int { get } ``` |
| To | ``` var kAudioToolboxErr_TrackIndexError: OSStatus { get } ``` |

Modified [kAudioToolboxErr_TrackNotFound](https://developer.apple.com/documentation/audiotoolbox/1515472-anonymous/kaudiotoolboxerr_tracknotfound)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioToolboxErr_TrackNotFound: Int { get } ``` |
| To | ``` var kAudioToolboxErr_TrackNotFound: OSStatus { get } ``` |

Modified [kAUGraphErr_CannotDoInCurrentContext](https://developer.apple.com/documentation/audiotoolbox/1537630-anonymous/kaugrapherr_cannotdoincurrentcontext)

|  | Declaration |
| --- | --- |
| From | ``` var kAUGraphErr_CannotDoInCurrentContext: Int { get } ``` |
| To | ``` var kAUGraphErr_CannotDoInCurrentContext: OSStatus { get } ``` |

Modified [kAUGraphErr_InvalidAudioUnit](https://developer.apple.com/documentation/audiotoolbox/1537630-anonymous/kaugrapherr_invalidaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` var kAUGraphErr_InvalidAudioUnit: Int { get } ``` |
| To | ``` var kAUGraphErr_InvalidAudioUnit: OSStatus { get } ``` |

Modified [kAUGraphErr_InvalidConnection](https://developer.apple.com/documentation/audiotoolbox/kaugrapherr_invalidconnection)

|  | Declaration |
| --- | --- |
| From | ``` var kAUGraphErr_InvalidConnection: Int { get } ``` |
| To | ``` var kAUGraphErr_InvalidConnection: OSStatus { get } ``` |

Modified [kAUGraphErr_NodeNotFound](https://developer.apple.com/documentation/audiotoolbox/kaugrapherr_nodenotfound)

|  | Declaration |
| --- | --- |
| From | ``` var kAUGraphErr_NodeNotFound: Int { get } ``` |
| To | ``` var kAUGraphErr_NodeNotFound: OSStatus { get } ``` |

Modified [kAUGraphErr_OutputNodeErr](https://developer.apple.com/documentation/audiotoolbox/kaugrapherr_outputnodeerr)

|  | Declaration |
| --- | --- |
| From | ``` var kAUGraphErr_OutputNodeErr: Int { get } ``` |
| To | ``` var kAUGraphErr_OutputNodeErr: OSStatus { get } ``` |

Modified [kAUNodeInteraction_Connection](https://developer.apple.com/documentation/audiotoolbox/kaunodeinteraction_connection)

|  | Declaration |
| --- | --- |
| From | ``` var kAUNodeInteraction_Connection: Int { get } ``` |
| To | ``` var kAUNodeInteraction_Connection: UInt32 { get } ``` |

Modified [kAUNodeInteraction_InputCallback](https://developer.apple.com/documentation/audiotoolbox/1537633-kaunodeinteraction_connection/kaunodeinteraction_inputcallback)

|  | Declaration |
| --- | --- |
| From | ``` var kAUNodeInteraction_InputCallback: Int { get } ``` |
| To | ``` var kAUNodeInteraction_InputCallback: UInt32 { get } ``` |

Modified [kCAF_AudioDataChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_audiodatachunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_AudioDataChunkID: Int { get } ``` |
| To | ``` var kCAF_AudioDataChunkID: UInt32 { get } ``` |

Modified [kCAF_ChannelLayoutChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_channellayoutchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_ChannelLayoutChunkID: Int { get } ``` |
| To | ``` var kCAF_ChannelLayoutChunkID: UInt32 { get } ``` |

Modified [kCAF_EditCommentsChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_editcommentschunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_EditCommentsChunkID: Int { get } ``` |
| To | ``` var kCAF_EditCommentsChunkID: UInt32 { get } ``` |

Modified [kCAF_FileType](https://developer.apple.com/documentation/audiotoolbox/1547255-anonymous/kcaf_filetype)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_FileType: Int { get } ``` |
| To | ``` var kCAF_FileType: UInt32 { get } ``` |

Modified [kCAF_FileVersion_Initial](https://developer.apple.com/documentation/audiotoolbox/kcaf_fileversion_initial)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_FileVersion_Initial: Int { get } ``` |
| To | ``` var kCAF_FileVersion_Initial: UInt32 { get } ``` |

Modified [kCAF_FillerChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_fillerchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_FillerChunkID: Int { get } ``` |
| To | ``` var kCAF_FillerChunkID: UInt32 { get } ``` |

Modified [kCAF_FormatListID](https://developer.apple.com/documentation/audiotoolbox/kcaf_formatlistid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_FormatListID: Int { get } ``` |
| To | ``` var kCAF_FormatListID: UInt32 { get } ``` |

Modified [kCAF_InfoStringsChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_infostringschunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_InfoStringsChunkID: Int { get } ``` |
| To | ``` var kCAF_InfoStringsChunkID: UInt32 { get } ``` |

Modified [kCAF_InstrumentChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_instrumentchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_InstrumentChunkID: Int { get } ``` |
| To | ``` var kCAF_InstrumentChunkID: UInt32 { get } ``` |

Modified [kCAF_iXMLChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_ixmlchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_iXMLChunkID: Int { get } ``` |
| To | ``` var kCAF_iXMLChunkID: UInt32 { get } ``` |

Modified [kCAF_MagicCookieID](https://developer.apple.com/documentation/audiotoolbox/kcaf_magiccookieid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_MagicCookieID: Int { get } ``` |
| To | ``` var kCAF_MagicCookieID: UInt32 { get } ``` |

Modified [kCAF_MarkerChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_markerchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_MarkerChunkID: Int { get } ``` |
| To | ``` var kCAF_MarkerChunkID: UInt32 { get } ``` |

Modified [kCAF_MIDIChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_midichunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_MIDIChunkID: Int { get } ``` |
| To | ``` var kCAF_MIDIChunkID: UInt32 { get } ``` |

Modified [kCAF_OverviewChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_overviewchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_OverviewChunkID: Int { get } ``` |
| To | ``` var kCAF_OverviewChunkID: UInt32 { get } ``` |

Modified [kCAF_PacketTableChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_packettablechunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_PacketTableChunkID: Int { get } ``` |
| To | ``` var kCAF_PacketTableChunkID: UInt32 { get } ``` |

Modified [kCAF_PeakChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_peakchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_PeakChunkID: Int { get } ``` |
| To | ``` var kCAF_PeakChunkID: UInt32 { get } ``` |

Modified [kCAF_RegionChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_regionchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_RegionChunkID: Int { get } ``` |
| To | ``` var kCAF_RegionChunkID: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType2398](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype2398)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType2398: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType2398: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType24](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype24)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType24: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType24: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType25](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype25)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType25: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType25: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType2997](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype2997)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType2997: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType2997: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType2997Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype2997drop)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType2997Drop: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType2997Drop: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType30](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype30)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType30: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType30: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType30Drop](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype30drop)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType30Drop: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType30Drop: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType50](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype50)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType50: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType50: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType5994](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype5994)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType5994: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType5994: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType5994Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype5994drop)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType5994Drop: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType5994Drop: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType60](https://developer.apple.com/documentation/audiotoolbox/kcaf_smpte_timetype60)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType60: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType60: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeType60Drop](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetype60drop)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeType60Drop: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeType60Drop: UInt32 { get } ``` |

Modified [kCAF_SMPTE_TimeTypeNone](https://developer.apple.com/documentation/audiotoolbox/1547262-anonymous/kcaf_smpte_timetypenone)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_SMPTE_TimeTypeNone: Int { get } ``` |
| To | ``` var kCAF_SMPTE_TimeTypeNone: UInt32 { get } ``` |

Modified [kCAF_StreamDescriptionChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_streamdescriptionchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_StreamDescriptionChunkID: Int { get } ``` |
| To | ``` var kCAF_StreamDescriptionChunkID: UInt32 { get } ``` |

Modified [kCAF_StringsChunkID](https://developer.apple.com/documentation/audiotoolbox/1547266-anonymous/kcaf_stringschunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_StringsChunkID: Int { get } ``` |
| To | ``` var kCAF_StringsChunkID: UInt32 { get } ``` |

Modified [kCAF_UMIDChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_umidchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_UMIDChunkID: Int { get } ``` |
| To | ``` var kCAF_UMIDChunkID: UInt32 { get } ``` |

Modified [kCAF_UUIDChunkID](https://developer.apple.com/documentation/audiotoolbox/kcaf_uuidchunkid)

|  | Declaration |
| --- | --- |
| From | ``` var kCAF_UUIDChunkID: Int { get } ``` |
| To | ``` var kCAF_UUIDChunkID: UInt32 { get } ``` |

Modified [kCAFMarkerType_EditDestinationBegin](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_editdestinationbegin)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_EditDestinationBegin: Int { get } ``` |
| To | ``` var kCAFMarkerType_EditDestinationBegin: UInt32 { get } ``` |

Modified [kCAFMarkerType_EditDestinationEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_editdestinationend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_EditDestinationEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_EditDestinationEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_EditSourceBegin](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_editsourcebegin)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_EditSourceBegin: Int { get } ``` |
| To | ``` var kCAFMarkerType_EditSourceBegin: UInt32 { get } ``` |

Modified [kCAFMarkerType_EditSourceEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_editsourceend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_EditSourceEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_EditSourceEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_Generic](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_generic)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_Generic: Int { get } ``` |
| To | ``` var kCAFMarkerType_Generic: UInt32 { get } ``` |

Modified [kCAFMarkerType_Index](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_index)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_Index: Int { get } ``` |
| To | ``` var kCAFMarkerType_Index: UInt32 { get } ``` |

Modified [kCAFMarkerType_KeySignature](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_keysignature)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_KeySignature: Int { get } ``` |
| To | ``` var kCAFMarkerType_KeySignature: UInt32 { get } ``` |

Modified [kCAFMarkerType_ProgramEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_programend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_ProgramEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_ProgramEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_ProgramStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_programstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_ProgramStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_ProgramStart: UInt32 { get } ``` |

Modified [kCAFMarkerType_RegionEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_regionend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_RegionEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_RegionEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_RegionStart](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_regionstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_RegionStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_RegionStart: UInt32 { get } ``` |

Modified [kCAFMarkerType_RegionSyncPoint](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_regionsyncpoint)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_RegionSyncPoint: Int { get } ``` |
| To | ``` var kCAFMarkerType_RegionSyncPoint: UInt32 { get } ``` |

Modified [kCAFMarkerType_ReleaseLoopEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_releaseloopend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_ReleaseLoopEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_ReleaseLoopEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_ReleaseLoopStart](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_releaseloopstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_ReleaseLoopStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_ReleaseLoopStart: UInt32 { get } ``` |

Modified [kCAFMarkerType_SavedPlayPosition](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_savedplayposition)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_SavedPlayPosition: Int { get } ``` |
| To | ``` var kCAFMarkerType_SavedPlayPosition: UInt32 { get } ``` |

Modified [kCAFMarkerType_SelectionEnd](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_selectionend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_SelectionEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_SelectionEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_SelectionStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_selectionstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_SelectionStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_SelectionStart: UInt32 { get } ``` |

Modified [kCAFMarkerType_SustainLoopEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_sustainloopend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_SustainLoopEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_SustainLoopEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_SustainLoopStart](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_sustainloopstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_SustainLoopStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_SustainLoopStart: UInt32 { get } ``` |

Modified [kCAFMarkerType_Tempo](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_tempo)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_Tempo: Int { get } ``` |
| To | ``` var kCAFMarkerType_Tempo: UInt32 { get } ``` |

Modified [kCAFMarkerType_TimeSignature](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_timesignature)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_TimeSignature: Int { get } ``` |
| To | ``` var kCAFMarkerType_TimeSignature: UInt32 { get } ``` |

Modified [kCAFMarkerType_TrackEnd](https://developer.apple.com/documentation/audiotoolbox/1547272-anonymous/kcafmarkertype_trackend)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_TrackEnd: Int { get } ``` |
| To | ``` var kCAFMarkerType_TrackEnd: UInt32 { get } ``` |

Modified [kCAFMarkerType_TrackStart](https://developer.apple.com/documentation/audiotoolbox/kcafmarkertype_trackstart)

|  | Declaration |
| --- | --- |
| From | ``` var kCAFMarkerType_TrackStart: Int { get } ``` |
| To | ``` var kCAFMarkerType_TrackStart: UInt32 { get } ``` |

Modified [kConverterPrimeMethod_None](https://developer.apple.com/documentation/audiotoolbox/kconverterprimemethod_none)

|  | Declaration |
| --- | --- |
| From | ``` var kConverterPrimeMethod_None: Int { get } ``` |
| To | ``` var kConverterPrimeMethod_None: UInt32 { get } ``` |

Modified [kConverterPrimeMethod_Normal](https://developer.apple.com/documentation/audiotoolbox/1559927-converter_priming_constants/kconverterprimemethod_normal)

|  | Declaration |
| --- | --- |
| From | ``` var kConverterPrimeMethod_Normal: Int { get } ``` |
| To | ``` var kConverterPrimeMethod_Normal: UInt32 { get } ``` |

Modified [kConverterPrimeMethod_Pre](https://developer.apple.com/documentation/audiotoolbox/1559927-converter_priming_constants/kconverterprimemethod_pre)

|  | Declaration |
| --- | --- |
| From | ``` var kConverterPrimeMethod_Pre: Int { get } ``` |
| To | ``` var kConverterPrimeMethod_Pre: UInt32 { get } ``` |

Modified [kExtAudioFileError_AsyncWriteBufferOverflow](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_asyncwritebufferoverflow)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_AsyncWriteBufferOverflow: Int { get } ``` |
| To | ``` var kExtAudioFileError_AsyncWriteBufferOverflow: OSStatus { get } ``` |

Modified [kExtAudioFileError_AsyncWriteTooLarge](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_asyncwritetoolarge)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_AsyncWriteTooLarge: Int { get } ``` |
| To | ``` var kExtAudioFileError_AsyncWriteTooLarge: OSStatus { get } ``` |

Modified [kExtAudioFileError_CodecUnavailableInputConsumed](https://developer.apple.com/documentation/audiotoolbox/1623673-anonymous/kextaudiofileerror_codecunavailableinputconsumed)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_CodecUnavailableInputConsumed: Int { get } ``` |
| To | ``` var kExtAudioFileError_CodecUnavailableInputConsumed: OSStatus { get } ``` |

Modified [kExtAudioFileError_CodecUnavailableInputNotConsumed](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_codecunavailableinputnotconsumed)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_CodecUnavailableInputNotConsumed: Int { get } ``` |
| To | ``` var kExtAudioFileError_CodecUnavailableInputNotConsumed: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidChannelMap](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidchannelmap)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidChannelMap: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidChannelMap: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_invaliddataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidDataFormat: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidDataFormat: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidOperationOrder](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidoperationorder)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidOperationOrder: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidOperationOrder: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidProperty](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidproperty)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidProperty: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidProperty: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidPropertySize](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidpropertysize)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidPropertySize: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidPropertySize: OSStatus { get } ``` |

Modified [kExtAudioFileError_InvalidSeek](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileerror_invalidseek)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_InvalidSeek: Int { get } ``` |
| To | ``` var kExtAudioFileError_InvalidSeek: OSStatus { get } ``` |

Modified [kExtAudioFileError_MaxPacketSizeUnknown](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_maxpacketsizeunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_MaxPacketSizeUnknown: Int { get } ``` |
| To | ``` var kExtAudioFileError_MaxPacketSizeUnknown: OSStatus { get } ``` |

Modified [kExtAudioFileError_NonPCMClientFormat](https://developer.apple.com/documentation/audiotoolbox/1486883-anonymous/kextaudiofileerror_nonpcmclientformat)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileError_NonPCMClientFormat: Int { get } ``` |
| To | ``` var kExtAudioFileError_NonPCMClientFormat: OSStatus { get } ``` |

Modified [kExtAudioFileProperty_AudioConverter](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_audioconverter)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_AudioConverter: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_AudioConverter: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_AudioFile](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_audiofile)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_AudioFile: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_AudioFile: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_ClientChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientchannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_ClientChannelLayout: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_ClientChannelLayout: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_ClientDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_clientdataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_ClientDataFormat: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_ClientDataFormat: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_ClientMaxPacketSize](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_clientmaxpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_ClientMaxPacketSize: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_ClientMaxPacketSize: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_CodecManufacturer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_codecmanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_CodecManufacturer: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_CodecManufacturer: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_ConverterConfig](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_converterconfig)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_ConverterConfig: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_ConverterConfig: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_FileChannelLayout](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_filechannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_FileChannelLayout: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_FileChannelLayout: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_FileDataFormat](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filedataformat)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_FileDataFormat: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_FileDataFormat: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_FileLengthFrames](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filelengthframes)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_FileLengthFrames: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_FileLengthFrames: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_FileMaxPacketSize](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_filemaxpacketsize)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_FileMaxPacketSize: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_FileMaxPacketSize: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_IOBuffer](https://developer.apple.com/documentation/audiotoolbox/kextaudiofileproperty_iobuffer)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_IOBuffer: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_IOBuffer: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_IOBufferSizeBytes](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_iobuffersizebytes)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_IOBufferSizeBytes: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_IOBufferSizeBytes: ExtAudioFilePropertyID { get } ``` |

Modified [kExtAudioFileProperty_PacketTable](https://developer.apple.com/documentation/audiotoolbox/1486859-property_identifiers_for_extende/kextaudiofileproperty_packettable)

|  | Declaration |
| --- | --- |
| From | ``` var kExtAudioFileProperty_PacketTable: Int { get } ``` |
| To | ``` var kExtAudioFileProperty_PacketTable: ExtAudioFilePropertyID { get } ``` |

Modified [kMusicEventType_AUPreset](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_aupreset)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_AUPreset: Int { get } ``` |
| To | ``` var kMusicEventType_AUPreset: UInt32 { get } ``` |

Modified [kMusicEventType_ExtendedNote](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_extendednote)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_ExtendedNote: Int { get } ``` |
| To | ``` var kMusicEventType_ExtendedNote: UInt32 { get } ``` |

Modified [kMusicEventType_ExtendedTempo](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_extendedtempo)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_ExtendedTempo: Int { get } ``` |
| To | ``` var kMusicEventType_ExtendedTempo: UInt32 { get } ``` |

Modified [kMusicEventType_Meta](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_meta)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_Meta: Int { get } ``` |
| To | ``` var kMusicEventType_Meta: UInt32 { get } ``` |

Modified [kMusicEventType_MIDIChannelMessage](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_midichannelmessage)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_MIDIChannelMessage: Int { get } ``` |
| To | ``` var kMusicEventType_MIDIChannelMessage: UInt32 { get } ``` |

Modified [kMusicEventType_MIDINoteMessage](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_midinotemessage)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_MIDINoteMessage: Int { get } ``` |
| To | ``` var kMusicEventType_MIDINoteMessage: UInt32 { get } ``` |

Modified [kMusicEventType_MIDIRawData](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_midirawdata)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_MIDIRawData: Int { get } ``` |
| To | ``` var kMusicEventType_MIDIRawData: UInt32 { get } ``` |

Modified [kMusicEventType_NULL](https://developer.apple.com/documentation/audiotoolbox/1515479-anonymous/kmusiceventtype_null)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_NULL: Int { get } ``` |
| To | ``` var kMusicEventType_NULL: UInt32 { get } ``` |

Modified [kMusicEventType_Parameter](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_parameter)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_Parameter: Int { get } ``` |
| To | ``` var kMusicEventType_Parameter: UInt32 { get } ``` |

Modified [kMusicEventType_User](https://developer.apple.com/documentation/audiotoolbox/kmusiceventtype_user)

|  | Declaration |
| --- | --- |
| From | ``` var kMusicEventType_User: Int { get } ``` |
| To | ``` var kMusicEventType_User: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_AutomatedParameters](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_automatedparameters)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_AutomatedParameters: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_AutomatedParameters: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_LoopInfo](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_loopinfo)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_LoopInfo: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_LoopInfo: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_MuteStatus](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_mutestatus)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_MuteStatus: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_MuteStatus: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_OffsetTime](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_offsettime)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_OffsetTime: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_OffsetTime: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_SoloStatus](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_solostatus)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_SoloStatus: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_SoloStatus: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_TimeResolution](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_timeresolution)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_TimeResolution: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_TimeResolution: UInt32 { get } ``` |

Modified [kSequenceTrackProperty_TrackLength](https://developer.apple.com/documentation/audiotoolbox/1515456-music_track_properties/ksequencetrackproperty_tracklength)

|  | Declaration |
| --- | --- |
| From | ``` var kSequenceTrackProperty_TrackLength: Int { get } ``` |
| To | ``` var kSequenceTrackProperty_TrackLength: UInt32 { get } ``` |

Modified [kSystemSoundID_Vibrate](https://developer.apple.com/documentation/audiotoolbox/1618202-alert_sound_identifiers/ksystemsoundid_vibrate)

|  | Declaration |
| --- | --- |
| From | ``` var kSystemSoundID_Vibrate: Int { get } ``` |
| To | ``` var kSystemSoundID_Vibrate: SystemSoundID { get } ``` |

Modified [MusicEventIteratorHasCurrentEvent(_: MusicEventIterator, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503065-musiceventiteratorhascurrenteven)

|  | Declaration |
| --- | --- |
| From | ``` func MusicEventIteratorHasCurrentEvent(_ inIterator: MusicEventIterator, _ outHasCurEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func MusicEventIteratorHasCurrentEvent(_ inIterator: MusicEventIterator, _ outHasCurEvent: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [MusicEventIteratorHasNextEvent(_: MusicEventIterator, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503205-musiceventiteratorhasnextevent)

|  | Declaration |
| --- | --- |
| From | ``` func MusicEventIteratorHasNextEvent(_ inIterator: MusicEventIterator, _ outHasNextEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func MusicEventIteratorHasNextEvent(_ inIterator: MusicEventIterator, _ outHasNextEvent: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [MusicEventIteratorHasPreviousEvent(_: MusicEventIterator, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502205-musiceventiteratorhaspreviouseve)

|  | Declaration |
| --- | --- |
| From | ``` func MusicEventIteratorHasPreviousEvent(_ inIterator: MusicEventIterator, _ outHasPrevEvent: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func MusicEventIteratorHasPreviousEvent(_ inIterator: MusicEventIterator, _ outHasPrevEvent: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [MusicPlayerIsPlaying(_: MusicPlayer, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502241-musicplayerisplaying)

|  | Declaration |
| --- | --- |
| From | ``` func MusicPlayerIsPlaying(_ inPlayer: MusicPlayer, _ outIsPlaying: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func MusicPlayerIsPlaying(_ inPlayer: MusicPlayer, _ outIsPlaying: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [MusicSequenceFileCreate(_: MusicSequence, _: CFURL, _: MusicSequenceFileTypeID, _: MusicSequenceFileFlags, _: Int16) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502760-musicsequencefilecreate)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceFileCreate(_ inSequence: MusicSequence, _ inFileRef: CFURL!, _ inFileType: MusicSequenceFileTypeID, _ inFlags: MusicSequenceFileFlags, _ inResolution: Int16) -> OSStatus ``` |
| To | ``` func MusicSequenceFileCreate(_ inSequence: MusicSequence, _ inFileRef: CFURL, _ inFileType: MusicSequenceFileTypeID, _ inFlags: MusicSequenceFileFlags, _ inResolution: Int16) -> OSStatus ``` |

Modified [MusicSequenceFileLoad(_: MusicSequence, _: CFURL, _: MusicSequenceFileTypeID, _: MusicSequenceLoadFlags) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502222-musicsequencefileload)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceFileLoad(_ inSequence: MusicSequence, _ inFileRef: CFURL!, _ inFileTypeHint: MusicSequenceFileTypeID, _ inFlags: MusicSequenceLoadFlags) -> OSStatus ``` |
| To | ``` func MusicSequenceFileLoad(_ inSequence: MusicSequence, _ inFileRef: CFURL, _ inFileTypeHint: MusicSequenceFileTypeID, _ inFlags: MusicSequenceLoadFlags) -> OSStatus ``` |

Modified [MusicSequenceFileLoadData(_: MusicSequence, _: CFData, _: MusicSequenceFileTypeID, _: MusicSequenceLoadFlags) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1502465-musicsequencefileloaddata)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceFileLoadData(_ inSequence: MusicSequence, _ inData: CFData!, _ inFileTypeHint: MusicSequenceFileTypeID, _ inFlags: MusicSequenceLoadFlags) -> OSStatus ``` |
| To | ``` func MusicSequenceFileLoadData(_ inSequence: MusicSequence, _ inData: CFData, _ inFileTypeHint: MusicSequenceFileTypeID, _ inFlags: MusicSequenceLoadFlags) -> OSStatus ``` |

Modified [MusicSequenceGetInfoDictionary(_: MusicSequence) -> CFDictionary](https://developer.apple.com/documentation/audiotoolbox/1502298-musicsequencegetinfodictionary)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceGetInfoDictionary(_ inSequence: MusicSequence) -> CFDictionary! ``` |
| To | ``` func MusicSequenceGetInfoDictionary(_ inSequence: MusicSequence) -> CFDictionary ``` |

Modified [MusicSequenceSetUserCallback(_: MusicSequence, _: MusicSequenceUserCallback?, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/audiotoolbox/1503188-musicsequencesetusercallback)

|  | Declaration |
| --- | --- |
| From | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func MusicSequenceSetUserCallback(_ inSequence: MusicSequence, _ inCallback: MusicSequenceUserCallback?, _ inClientData: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [MusicSequenceUserCallback](https://developer.apple.com/documentation/audiotoolbox/musicsequenceusercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias MusicSequenceUserCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, MusicSequence, MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Void)> ``` |
| To | ``` typealias MusicSequenceUserCallback = (UnsafeMutablePointer<Void>, MusicSequence, MusicTrack, MusicTimeStamp, UnsafePointer<MusicEventUserData>, MusicTimeStamp, MusicTimeStamp) -> Void ``` |

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
