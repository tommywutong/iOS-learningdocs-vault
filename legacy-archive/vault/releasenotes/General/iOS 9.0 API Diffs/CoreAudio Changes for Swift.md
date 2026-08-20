---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreAudio.html
archived_at: '2026-07-18T02:56:42.763626Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreAudio Changes for Swift

### CoreAudio

Removed AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: UInt32, mCoordinates: (Float32, Float32, Float32))Removed AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: UInt32, mNumberChannelDescriptions: UInt32, mChannelDescriptions: (AudioChannelDescription))Removed AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: UInt32, mReserved: UInt32)Removed AudioValueTranslation.init()Removed AudioValueTranslation.init(mInputData: UnsafeMutablePointer<Void>, mInputDataSize: UInt32, mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize: UInt32)Removed SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: UInt32, mFlags: UInt32, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Removed UnsafeMutableAudioBufferListPointer.generate() -> IndexingGenerator<UnsafeMutableAudioBufferListPointer>Removed kAudioChannelBit_CenterRemoved kAudioChannelBit_CenterSurroundRemoved kAudioChannelBit_LeftRemoved kAudioChannelBit_LeftCenterRemoved kAudioChannelBit_LeftSurroundRemoved kAudioChannelBit_LeftSurroundDirectRemoved kAudioChannelBit_LFEScreenRemoved kAudioChannelBit_RightRemoved kAudioChannelBit_RightCenterRemoved kAudioChannelBit_RightSurroundRemoved kAudioChannelBit_RightSurroundDirectRemoved kAudioChannelBit_TopBackCenterRemoved kAudioChannelBit_TopBackLeftRemoved kAudioChannelBit_TopBackRightRemoved kAudioChannelBit_TopCenterSurroundRemoved kAudioChannelBit_VerticalHeightCenterRemoved kAudioChannelBit_VerticalHeightLeftRemoved kAudioChannelBit_VerticalHeightRightRemoved kAudioChannelCoordinates_AzimuthRemoved kAudioChannelCoordinates_BackFrontRemoved kAudioChannelCoordinates_DistanceRemoved kAudioChannelCoordinates_DownUpRemoved kAudioChannelCoordinates_ElevationRemoved kAudioChannelCoordinates_LeftRightRemoved kAudioChannelFlags_AllOffRemoved kAudioChannelFlags_MetersRemoved kAudioChannelFlags_RectangularCoordinatesRemoved kAudioChannelFlags_SphericalCoordinatesRemoved kAudioTimeStampHostTimeValidRemoved kAudioTimeStampRateScalarValidRemoved kAudioTimeStampSampleHostTimeValidRemoved kAudioTimeStampSampleTimeValidRemoved kAudioTimeStampSMPTETimeValidRemoved kAudioTimeStampWordClockTimeValidRemoved kMPEG4Object_AAC_LCRemoved kMPEG4Object_AAC_LTPRemoved kMPEG4Object_AAC_MainRemoved kMPEG4Object_AAC_SBRRemoved kMPEG4Object_AAC_ScalableRemoved kMPEG4Object_AAC_SSRRemoved kMPEG4Object_CELPRemoved kMPEG4Object_HVXCRemoved kMPEG4Object_TwinVQRemoved kSMPTETimeRunningRemoved kSMPTETimeType2398Removed kSMPTETimeType24Removed kSMPTETimeType25Removed kSMPTETimeType2997Removed kSMPTETimeType2997DropRemoved kSMPTETimeType30Removed kSMPTETimeType30DropRemoved kSMPTETimeType50Removed kSMPTETimeType5994Removed kSMPTETimeType5994DropRemoved kSMPTETimeType60Removed kSMPTETimeType60DropRemoved kSMPTETimeValidAdded [AudioChannelBitmap [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap)Added [AudioChannelBitmap.Bit_Center](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422558-bit_center)Added [AudioChannelBitmap.Bit_CenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421862-bit_centersurround)Added [AudioChannelBitmap.Bit_Left](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422633-bit_left)Added [AudioChannelBitmap.Bit_LeftCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421656-bit_leftcenter)Added [AudioChannelBitmap.Bit_LeftSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422177-bit_leftsurround)Added [AudioChannelBitmap.Bit_LeftSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_leftsurrounddirect)Added [AudioChannelBitmap.Bit_LFEScreen](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422510-bit_lfescreen)Added [AudioChannelBitmap.Bit_Right](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421518-bit_right)Added [AudioChannelBitmap.Bit_RightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422165-bit_rightcenter)Added [AudioChannelBitmap.Bit_RightSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421938-bit_rightsurround)Added [AudioChannelBitmap.Bit_RightSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_rightsurrounddirect)Added [AudioChannelBitmap.Bit_TopBackCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_topbackcenter)Added [AudioChannelBitmap.Bit_TopBackLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423190-bit_topbackleft)Added [AudioChannelBitmap.Bit_TopBackRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423004-bit_topbackright)Added [AudioChannelBitmap.Bit_TopCenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422248-bit_topcentersurround)Added [AudioChannelBitmap.Bit_VerticalHeightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422161-bit_verticalheightcenter)Added [AudioChannelBitmap.Bit_VerticalHeightLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightleft)Added [AudioChannelBitmap.Bit_VerticalHeightRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightright)Added AudioChannelBitmap.init(rawValue: UInt32)Added [AudioChannelCoordinateIndex [enum]](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex)Added [AudioChannelCoordinateIndex.Coordinates_Azimuth](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_azimuth)Added [AudioChannelCoordinateIndex.Coordinates_BackFront](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_backfront)Added [AudioChannelCoordinateIndex.Coordinates_Distance](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_distance)Added [AudioChannelCoordinateIndex.Coordinates_DownUp](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_downup)Added [AudioChannelCoordinateIndex.Coordinates_Elevation](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_elevation)Added [AudioChannelCoordinateIndex.Coordinates_LeftRight](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_leftright)Added AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: AudioChannelFlags, mCoordinates: (Float32, Float32, Float32))Added [AudioChannelFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelflags)Added [AudioChannelFlags.AllOff](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_alloff)Added AudioChannelFlags.init(rawValue: UInt32)Added [AudioChannelFlags.Meters](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1422914-meters)Added [AudioChannelFlags.RectangularCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_rectangularcoordinates)Added [AudioChannelFlags.SphericalCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1421586-sphericalcoordinates)Added AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: AudioChannelBitmap, mNumberChannelDescriptions: UInt32, mChannelDescriptions: (AudioChannelDescription))Added AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: AudioTimeStampFlags, mReserved: UInt32)Added [AudioTimeStampFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiotimestampflags)Added [AudioTimeStampFlags.HostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423064-hosttimevalid)Added AudioTimeStampFlags.init(rawValue: UInt32)Added [AudioTimeStampFlags.NothingValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampnothingvalid)Added [AudioTimeStampFlags.RateScalarValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422238-ratescalarvalid)Added [AudioTimeStampFlags.SampleHostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422143-samplehosttimevalid)Added [AudioTimeStampFlags.SampleTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423034-sampletimevalid)Added [AudioTimeStampFlags.SMPTETimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampsmptetimevalid)Added [AudioTimeStampFlags.WordClockTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422676-wordclocktimevalid)Added [MPEG4ObjectID [enum]](https://developer.apple.com/documentation/coreaudio/mpeg4objectid)Added [MPEG4ObjectID.AAC_LC](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/aac_lc)Added [MPEG4ObjectID.AAC_LTP](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_ltp)Added [MPEG4ObjectID.AAC_Main](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_main)Added [MPEG4ObjectID.AAC_SBR](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_sbr)Added [MPEG4ObjectID.AAC_Scalable](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/aac_scalable)Added [MPEG4ObjectID.AAC_SSR](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_ssr)Added [MPEG4ObjectID.CELP](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/celp)Added [MPEG4ObjectID.HVXC](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_hvxc)Added [MPEG4ObjectID.TwinVQ](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/twinvq)Added SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: SMPTETimeType, mFlags: SMPTETimeFlags, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Added [SMPTETimeFlags [struct]](https://developer.apple.com/documentation/coreaudio/smptetimeflags)Added SMPTETimeFlags.init(rawValue: UInt32)Added [SMPTETimeFlags.Running](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimerunning)Added [SMPTETimeFlags.Unknown](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimeunknown)Added [SMPTETimeFlags.Valid](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimevalid)Added [SMPTETimeType [enum]](https://developer.apple.com/documentation/coreaudio/smptetimetype)Added [SMPTETimeType.Type2398](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2398)Added [SMPTETimeType.Type24](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype24)Added [SMPTETimeType.Type25](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype25)Added [SMPTETimeType.Type2997](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997)Added [SMPTETimeType.Type2997Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997drop)Added [SMPTETimeType.Type30](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30)Added [SMPTETimeType.Type30Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30drop)Added [SMPTETimeType.Type50](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype50)Added [SMPTETimeType.Type5994](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994)Added [SMPTETimeType.Type5994Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994drop)Added [SMPTETimeType.Type60](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60)Added [SMPTETimeType.Type60Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60drop)Added [AudioChannelLayoutTag_GetNumberOfChannels(_: AudioChannelLayoutTag) -> UInt32](https://developer.apple.com/documentation/coreaudio/1422032-audiochannellayouttag_getnumbero)Added [AudioSampleType](https://developer.apple.com/documentation/coreaudio/audiosampletype)Added [AudioUnitSampleType](https://developer.apple.com/documentation/coreaudio/audiounitsampletype)Added [kAudioFormatEnhancedAC3](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatenhancedac3)Added [kAudioFormatFlagsAudioUnitCanonical](https://developer.apple.com/documentation/coreaudio/1572098-audiostreambasicdescription_flag/kaudioformatflagsaudiounitcanonical)Added [kAudioFormatFlagsCanonical](https://developer.apple.com/documentation/coreaudio/1572098-audiostreambasicdescription_flag/kaudioformatflagscanonical)Modified [AudioBuffer [struct]](https://developer.apple.com/documentation/coreaudio/audiobuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } extension AudioBuffer {     init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) } ``` |
| To | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } ``` |

Modified AudioBuffer.init<Element>(_: UnsafeMutableBufferPointer<Element>, numberOfChannels: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) ``` | iOS 8.3 | -- |
| To | ``` init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) ``` | iOS 9.0 | Element |

Modified [AudioChannelDescription [struct]](https://developer.apple.com/documentation/coreaudio/audiochanneldescription)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioChannelDescription {     var mChannelLabel: AudioChannelLabel     var mChannelFlags: UInt32     var mCoordinates: (Float32, Float32, Float32)     init()     init(mChannelLabel mChannelLabel: AudioChannelLabel, mChannelFlags mChannelFlags: UInt32, mCoordinates mCoordinates: (Float32, Float32, Float32)) } ``` |
| To | ``` struct AudioChannelDescription {     var mChannelLabel: AudioChannelLabel     var mChannelFlags: AudioChannelFlags     var mCoordinates: (Float32, Float32, Float32)     init()     init(mChannelLabel mChannelLabel: AudioChannelLabel, mChannelFlags mChannelFlags: AudioChannelFlags, mCoordinates mCoordinates: (Float32, Float32, Float32)) } ``` |

Modified [AudioChannelDescription.mChannelFlags](https://developer.apple.com/documentation/coreaudio/audiochanneldescription/1422252-mchannelflags)

|  | Declaration |
| --- | --- |
| From | ``` var mChannelFlags: UInt32 ``` |
| To | ``` var mChannelFlags: AudioChannelFlags ``` |

Modified [AudioChannelLayout [struct]](https://developer.apple.com/documentation/coreaudio/audiochannellayout)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioChannelLayout {     var mChannelLayoutTag: AudioChannelLayoutTag     var mChannelBitmap: UInt32     var mNumberChannelDescriptions: UInt32     var mChannelDescriptions: (AudioChannelDescription)     init()     init(mChannelLayoutTag mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap mChannelBitmap: UInt32, mNumberChannelDescriptions mNumberChannelDescriptions: UInt32, mChannelDescriptions mChannelDescriptions: (AudioChannelDescription)) } ``` |
| To | ``` struct AudioChannelLayout {     var mChannelLayoutTag: AudioChannelLayoutTag     var mChannelBitmap: AudioChannelBitmap     var mNumberChannelDescriptions: UInt32     var mChannelDescriptions: (AudioChannelDescription)     init()     init(mChannelLayoutTag mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap mChannelBitmap: AudioChannelBitmap, mNumberChannelDescriptions mNumberChannelDescriptions: UInt32, mChannelDescriptions mChannelDescriptions: (AudioChannelDescription)) } ``` |

Modified [AudioChannelLayout.mChannelBitmap](https://developer.apple.com/documentation/coreaudio/audiochannellayout/1421804-mchannelbitmap)

|  | Declaration |
| --- | --- |
| From | ``` var mChannelBitmap: UInt32 ``` |
| To | ``` var mChannelBitmap: AudioChannelBitmap ``` |

Modified [AudioTimeStamp [struct]](https://developer.apple.com/documentation/coreaudio/audiotimestamp)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioTimeStamp {     var mSampleTime: Float64     var mHostTime: UInt64     var mRateScalar: Float64     var mWordClockTime: UInt64     var mSMPTETime: SMPTETime     var mFlags: UInt32     var mReserved: UInt32     init()     init(mSampleTime mSampleTime: Float64, mHostTime mHostTime: UInt64, mRateScalar mRateScalar: Float64, mWordClockTime mWordClockTime: UInt64, mSMPTETime mSMPTETime: SMPTETime, mFlags mFlags: UInt32, mReserved mReserved: UInt32) } ``` |
| To | ``` struct AudioTimeStamp {     var mSampleTime: Float64     var mHostTime: UInt64     var mRateScalar: Float64     var mWordClockTime: UInt64     var mSMPTETime: SMPTETime     var mFlags: AudioTimeStampFlags     var mReserved: UInt32     init()     init(mSampleTime mSampleTime: Float64, mHostTime mHostTime: UInt64, mRateScalar mRateScalar: Float64, mWordClockTime mWordClockTime: UInt64, mSMPTETime mSMPTETime: SMPTETime, mFlags mFlags: AudioTimeStampFlags, mReserved mReserved: UInt32) } ``` |

Modified [AudioTimeStamp.mFlags](https://developer.apple.com/documentation/coreaudio/audiotimestamp/1423076-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: AudioTimeStampFlags ``` |

Modified [AudioValueTranslation [struct]](https://developer.apple.com/documentation/coreaudio/audiovaluetranslation)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32     init()     init(mInputData mInputData: UnsafeMutablePointer<Void>, mInputDataSize mInputDataSize: UInt32, mOutputData mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize mOutputDataSize: UInt32) } ``` |
| To | ``` struct AudioValueTranslation {     var mInputData: UnsafeMutablePointer<Void>     var mInputDataSize: UInt32     var mOutputData: UnsafeMutablePointer<Void>     var mOutputDataSize: UInt32 } ``` |

Modified [SMPTETime [struct]](https://developer.apple.com/documentation/coreaudio/smptetime)

|  | Declaration |
| --- | --- |
| From | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: UInt32     var mFlags: UInt32     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16     init()     init(mSubframes mSubframes: Int16, mSubframeDivisor mSubframeDivisor: Int16, mCounter mCounter: UInt32, mType mType: UInt32, mFlags mFlags: UInt32, mHours mHours: Int16, mMinutes mMinutes: Int16, mSeconds mSeconds: Int16, mFrames mFrames: Int16) } ``` |
| To | ``` struct SMPTETime {     var mSubframes: Int16     var mSubframeDivisor: Int16     var mCounter: UInt32     var mType: SMPTETimeType     var mFlags: SMPTETimeFlags     var mHours: Int16     var mMinutes: Int16     var mSeconds: Int16     var mFrames: Int16     init()     init(mSubframes mSubframes: Int16, mSubframeDivisor mSubframeDivisor: Int16, mCounter mCounter: UInt32, mType mType: SMPTETimeType, mFlags mFlags: SMPTETimeFlags, mHours mHours: Int16, mMinutes mMinutes: Int16, mSeconds mSeconds: Int16, mFrames mFrames: Int16) } ``` |

Modified [SMPTETime.mFlags](https://developer.apple.com/documentation/coreaudio/smptetime/1422528-mflags)

|  | Declaration |
| --- | --- |
| From | ``` var mFlags: UInt32 ``` |
| To | ``` var mFlags: SMPTETimeFlags ``` |

Modified [SMPTETime.mType](https://developer.apple.com/documentation/coreaudio/smptetime/1422020-mtype)

|  | Declaration |
| --- | --- |
| From | ``` var mType: UInt32 ``` |
| To | ``` var mType: SMPTETimeType ``` |

Modified UnsafeBufferPointer.init(_: AudioBuffer)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [UnsafeMutableAudioBufferListPointer [struct]](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollectionType {     func generate() -> IndexingGenerator<UnsafeMutableAudioBufferListPointer>     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> AudioBuffer { get nonmutating set } } ``` | MutableCollectionType |
| To | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollectionType, CollectionType, Indexable, SequenceType, MutableIndexable {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> AudioBuffer { get nonmutating set } } ``` | CollectionType, Indexable, MutableCollectionType, MutableIndexable, SequenceType |

Modified UnsafeMutableAudioBufferListPointer.subscript(_: Int) -> AudioBuffer

|  | Declaration |
| --- | --- |
| From | ``` subscript (index: Int) -> AudioBuffer { get nonmutating set } ``` |
| To | ``` subscript (_ index: Int) -> AudioBuffer { get nonmutating set } ``` |

Modified UnsafeMutableBufferPointer.init(_: AudioBuffer)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [kAppleLosslessFormatFlag_16BitSourceData](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kapplelosslessformatflag_16bitsourcedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleLosslessFormatFlag_16BitSourceData: Int { get } ``` |
| To | ``` var kAppleLosslessFormatFlag_16BitSourceData: AudioFormatFlags { get } ``` |

Modified [kAppleLosslessFormatFlag_20BitSourceData](https://developer.apple.com/documentation/coreaudio/kapplelosslessformatflag_20bitsourcedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleLosslessFormatFlag_20BitSourceData: Int { get } ``` |
| To | ``` var kAppleLosslessFormatFlag_20BitSourceData: AudioFormatFlags { get } ``` |

Modified [kAppleLosslessFormatFlag_24BitSourceData](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kapplelosslessformatflag_24bitsourcedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleLosslessFormatFlag_24BitSourceData: Int { get } ``` |
| To | ``` var kAppleLosslessFormatFlag_24BitSourceData: AudioFormatFlags { get } ``` |

Modified [kAppleLosslessFormatFlag_32BitSourceData](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kapplelosslessformatflag_32bitsourcedata)

|  | Declaration |
| --- | --- |
| From | ``` var kAppleLosslessFormatFlag_32BitSourceData: Int { get } ``` |
| To | ``` var kAppleLosslessFormatFlag_32BitSourceData: AudioFormatFlags { get } ``` |

Modified [kAudio_BadFilePathError](https://developer.apple.com/documentation/coreaudio/kaudio_badfilepatherror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_BadFilePathError: Int { get } ``` |
| To | ``` var kAudio_BadFilePathError: OSStatus { get } ``` |

Modified [kAudio_FileNotFoundError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filenotfounderror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_FileNotFoundError: Int { get } ``` |
| To | ``` var kAudio_FileNotFoundError: OSStatus { get } ``` |

Modified [kAudio_FilePermissionError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_filepermissionerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_FilePermissionError: Int { get } ``` |
| To | ``` var kAudio_FilePermissionError: OSStatus { get } ``` |

Modified [kAudio_MemFullError](https://developer.apple.com/documentation/coreaudio/kaudio_memfullerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_MemFullError: Int { get } ``` |
| To | ``` var kAudio_MemFullError: OSStatus { get } ``` |

Modified [kAudio_ParamError](https://developer.apple.com/documentation/coreaudio/kaudio_paramerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_ParamError: Int { get } ``` |
| To | ``` var kAudio_ParamError: OSStatus { get } ``` |

Modified [kAudio_TooManyFilesOpenError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_toomanyfilesopenerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_TooManyFilesOpenError: Int { get } ``` |
| To | ``` var kAudio_TooManyFilesOpenError: OSStatus { get } ``` |

Modified [kAudio_UnimplementedError](https://developer.apple.com/documentation/coreaudio/1572099-anonymous/kaudio_unimplementederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudio_UnimplementedError: Int { get } ``` |
| To | ``` var kAudio_UnimplementedError: OSStatus { get } ``` |

Modified [kAudioChannelLabel_Ambisonic_W](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_ambisonic_w)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Ambisonic_W: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Ambisonic_W: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Ambisonic_X](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_ambisonic_x)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Ambisonic_X: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Ambisonic_X: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Ambisonic_Y](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_ambisonic_y)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Ambisonic_Y: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Ambisonic_Y: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Ambisonic_Z](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_ambisonic_z)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Ambisonic_Z: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Ambisonic_Z: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Center](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_center)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Center: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Center: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_CenterSurround](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_centersurround)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_CenterSurround: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_CenterSurround: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_CenterSurroundDirect](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_centersurrounddirect)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_CenterSurroundDirect: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_CenterSurroundDirect: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_ClickTrack](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_clicktrack)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_ClickTrack: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_ClickTrack: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_DialogCentricMix](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_dialogcentricmix)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_DialogCentricMix: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_DialogCentricMix: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_0: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_1](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_1: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_10](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_10)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_10: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_10: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_11](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_11)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_11: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_11: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_12](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_12)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_12: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_12: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_13](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_13)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_13: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_13: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_14](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_14)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_14: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_14: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_15](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_15)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_15: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_15: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_2](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_2: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_2: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_3](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_3: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_3: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_4](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_4)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_4: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_4: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_5](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_5)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_5: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_5: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_6](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_6)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_6: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_6: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_65535](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_65535)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_65535: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_65535: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_7](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_7)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_7: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_7: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_8](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_discrete_8)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_8: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_8: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Discrete_9](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_discrete_9)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Discrete_9: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Discrete_9: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_ForeignLanguage](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_foreignlanguage)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_ForeignLanguage: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_ForeignLanguage: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Haptic](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_haptic)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Haptic: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Haptic: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_HeadphonesLeft](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_headphonesleft)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_HeadphonesLeft: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_HeadphonesLeft: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_HeadphonesRight](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_headphonesright)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_HeadphonesRight: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_HeadphonesRight: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_HearingImpaired](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_hearingimpaired)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_HearingImpaired: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_HearingImpaired: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Left](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_left)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Left: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Left: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LeftCenter](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_leftcenter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LeftCenter: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LeftCenter: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LeftSurround](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_leftsurround)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LeftSurround: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LeftSurround: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LeftSurroundDirect](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_leftsurrounddirect)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LeftSurroundDirect: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LeftSurroundDirect: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LeftTotal](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_lefttotal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LeftTotal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LeftTotal: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LeftWide](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_leftwide)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LeftWide: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LeftWide: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LFE2](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_lfe2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LFE2: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LFE2: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_LFEScreen](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_lfescreen)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_LFEScreen: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_LFEScreen: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Mono](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_mono)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Mono: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Mono: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_MS_Mid](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_ms_mid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_MS_Mid: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_MS_Mid: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_MS_Side](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_ms_side)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_MS_Side: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_MS_Side: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Narration](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_narration)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Narration: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Narration: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RearSurroundLeft](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_rearsurroundleft)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RearSurroundLeft: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RearSurroundLeft: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RearSurroundRight](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_rearsurroundright)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RearSurroundRight: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RearSurroundRight: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Right](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_right)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Right: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Right: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RightCenter](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_rightcenter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RightCenter: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RightCenter: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RightSurround](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_rightsurround)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RightSurround: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RightSurround: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RightSurroundDirect](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_rightsurrounddirect)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RightSurroundDirect: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RightSurroundDirect: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RightTotal](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_righttotal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RightTotal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RightTotal: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_RightWide](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_rightwide)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_RightWide: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_RightWide: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_TopBackCenter](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_topbackcenter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_TopBackCenter: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_TopBackCenter: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_TopBackLeft](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_topbackleft)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_TopBackLeft: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_TopBackLeft: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_TopBackRight](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_topbackright)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_TopBackRight: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_TopBackRight: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_TopCenterSurround](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_topcentersurround)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_TopCenterSurround: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_TopCenterSurround: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Unknown](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_unknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Unknown: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Unknown: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_Unused](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_unused)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_Unused: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_Unused: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_UseCoordinates](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_usecoordinates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_UseCoordinates: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_UseCoordinates: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_VerticalHeightCenter](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_verticalheightcenter)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_VerticalHeightCenter: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_VerticalHeightCenter: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_VerticalHeightLeft](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_verticalheightleft)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_VerticalHeightLeft: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_VerticalHeightLeft: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_VerticalHeightRight](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_verticalheightright)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_VerticalHeightRight: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_VerticalHeightRight: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_XY_X](https://developer.apple.com/documentation/coreaudio/1572103-audio_channel_label_constants/kaudiochannellabel_xy_x)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_XY_X: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_XY_X: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLabel_XY_Y](https://developer.apple.com/documentation/coreaudio/kaudiochannellabel_xy_y)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLabel_XY_Y: UInt32 { get } ``` |
| To | ``` var kAudioChannelLabel_XY_Y: AudioChannelLabel { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_3_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_3_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_3_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_3_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_4_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_4_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_4_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_4_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_5_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_5_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_5_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_5_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_5_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_5_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_5_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_5_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_6_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_6_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_6_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_6_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_6_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_6_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_6_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_6_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_7_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_7_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_7_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_7_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_7_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_7_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_7_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_7_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_7_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_aac_7_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_7_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_7_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_7_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_7_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_7_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_7_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_Octagonal](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_octagonal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_Octagonal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_Octagonal: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AAC_Quadraphonic](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_aac_quadraphonic)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AAC_Quadraphonic: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AAC_Quadraphonic: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_1_0_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_ac3_1_0_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_1_0_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_1_0_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_2_1_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_ac3_2_1_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_2_1_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_2_1_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_3_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_ac3_3_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_3_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_3_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_3_0_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_ac3_3_0_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_3_0_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_3_0_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_3_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_ac3_3_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_3_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_3_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AC3_3_1_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_ac3_3_1_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AC3_3_1_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AC3_3_1_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Ambisonic_B_Format](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_ambisonic_b_format)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Ambisonic_B_Format: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Ambisonic_B_Format: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_4](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_4)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_4: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_4: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_5](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_5)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_5: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_5: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_5_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_5_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_5_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_5_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_5_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_5_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_5_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_5_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_6](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_6)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_6: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_6: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_6_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_6_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_6_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_6_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_6_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_6_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_6_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_6_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_7_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_7_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_7_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_7_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_7_0_Front](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_7_0_front)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_7_0_Front: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_7_0_Front: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_7_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_audiounit_7_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_7_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_7_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_7_1_Front](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_7_1_front)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_7_1_Front: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_7_1_Front: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_AudioUnit_8](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_audiounit_8)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_AudioUnit_8: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_AudioUnit_8: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Binaural](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_binaural)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Binaural: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Binaural: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Cube](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_cube)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Cube: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Cube: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DiscreteInOrder](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_discreteinorder)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DiscreteInOrder: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DiscreteInOrder: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_3_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_3_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_3_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_3_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_4_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_4_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_4_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_4_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_0_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_0_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_0_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_0_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_0_C](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_0_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_0_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_0_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_6_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_6_1_D](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_6_1_d)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_6_1_D: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_6_1_D: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_7_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_7_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_7_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_7_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_7_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_7_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_7_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_7_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_8_0_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_8_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_8_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_8_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_8_0_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_8_0_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_8_0_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_8_0_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_8_1_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dts_8_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_8_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_8_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DTS_8_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dts_8_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DTS_8_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DTS_8_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_10](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_10)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_10: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_10: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_11](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_11)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_11: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_11: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_12](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_12)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_12: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_12: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_13](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_13)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_13: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_13: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_14](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_14)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_14: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_14: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_15](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_15)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_15: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_15: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_16](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_16)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_16: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_16: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_17](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_17)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_17: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_17: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_18](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_18)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_18: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_18: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_19](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_19)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_19: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_19: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_2](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_2: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_2: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_20](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_20)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_20: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_20: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_3](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_3: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_3: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_4](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_4)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_4: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_4: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_5](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_5)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_5: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_5: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_6](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_6)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_6: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_6: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_7](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_dvd_7)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_7: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_7: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_8](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_8)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_8: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_8: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_DVD_9](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_dvd_9)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_DVD_9: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_DVD_9: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_6_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_6_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_6_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_6_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_6_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_6_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_6_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_6_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_6_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_6_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_6_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_6_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac3_7_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_D](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_d)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_D: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_D: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_E](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_e)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_E: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_E: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_F](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_f)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_F: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_F: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_G](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_g)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_G: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_G: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC3_7_1_H](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_eac3_7_1_h)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC3_7_1_H: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC3_7_1_H: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC_6_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac_6_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC_6_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC_6_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_EAC_7_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_eac_7_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_EAC_7_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_EAC_7_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Emagic_Default_7_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_emagic_default_7_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Emagic_Default_7_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Emagic_Default_7_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Hexagonal](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_hexagonal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Hexagonal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Hexagonal: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_1_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_itu_1_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_1_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_1_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_2_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_itu_2_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_2_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_2_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_2_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_itu_2_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_2_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_2_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_2_2](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_itu_2_2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_2_2: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_2_2: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_3_0](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_itu_3_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_3_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_3_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_3_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_itu_3_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_3_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_3_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_3_2](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_itu_3_2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_3_2: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_3_2: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_3_2_1](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_itu_3_2_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_3_2_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_3_2_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_ITU_3_4_1](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_itu_3_4_1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_ITU_3_4_1: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_ITU_3_4_1: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MatrixStereo](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_matrixstereo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MatrixStereo: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MatrixStereo: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MidSide](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_midside)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MidSide: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MidSide: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Mono](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mono)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Mono: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Mono: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_1_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_1_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_1_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_1_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_2_0](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_2_0)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_2_0: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_2_0: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_3_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_3_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_3_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_3_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_3_0_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_3_0_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_3_0_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_3_0_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_4_0_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_4_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_4_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_4_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_4_0_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_4_0_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_4_0_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_4_0_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_0_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_5_0_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_0_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_0_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_0_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_5_0_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_0_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_0_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_0_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_5_0_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_0_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_0_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_0_D](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_5_0_d)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_0_D: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_0_D: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_5_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_1_B](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_5_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_1_C](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_5_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_5_1_D](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_5_1_d)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_5_1_D: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_5_1_D: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_6_1_A](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_6_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_6_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_6_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_7_1_A](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_7_1_a)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_7_1_A: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_7_1_A: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_7_1_B](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_mpeg_7_1_b)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_7_1_B: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_7_1_B: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_MPEG_7_1_C](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_mpeg_7_1_c)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_MPEG_7_1_C: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_MPEG_7_1_C: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Octagonal](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_octagonal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Octagonal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Octagonal: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Pentagonal](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_pentagonal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Pentagonal: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Pentagonal: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Quadraphonic](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_quadraphonic)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Quadraphonic: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Quadraphonic: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_SMPTE_DTV](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_smpte_dtv)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_SMPTE_DTV: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_SMPTE_DTV: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Stereo](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_stereo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Stereo: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Stereo: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_StereoHeadphones](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_stereoheadphones)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_StereoHeadphones: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_StereoHeadphones: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_TMH_10_2_full](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_tmh_10_2_full)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_TMH_10_2_full: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_TMH_10_2_full: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_TMH_10_2_std](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_tmh_10_2_std)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_TMH_10_2_std: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_TMH_10_2_std: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_Unknown](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_unknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_Unknown: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_Unknown: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_UseChannelBitmap](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_usechannelbitmap)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_UseChannelBitmap: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_UseChannelBitmap: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_UseChannelDescriptions](https://developer.apple.com/documentation/coreaudio/kaudiochannellayouttag_usechanneldescriptions)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_UseChannelDescriptions: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_UseChannelDescriptions: AudioChannelLayoutTag { get } ``` |

Modified [kAudioChannelLayoutTag_XY](https://developer.apple.com/documentation/coreaudio/1572101-audio_channel_layout_tags/kaudiochannellayouttag_xy)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioChannelLayoutTag_XY: UInt32 { get } ``` |
| To | ``` var kAudioChannelLayoutTag_XY: AudioChannelLayoutTag { get } ``` |

Modified [kAudioFormat60958AC3](https://developer.apple.com/documentation/coreaudio/kaudioformat60958ac3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormat60958AC3: Int { get } ``` |
| To | ``` var kAudioFormat60958AC3: AudioFormatID { get } ``` |

Modified [kAudioFormatAC3](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatac3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAC3: Int { get } ``` |
| To | ``` var kAudioFormatAC3: AudioFormatID { get } ``` |

Modified [kAudioFormatAES3](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformataes3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAES3: Int { get } ``` |
| To | ``` var kAudioFormatAES3: AudioFormatID { get } ``` |

Modified [kAudioFormatALaw](https://developer.apple.com/documentation/coreaudio/kaudioformatalaw)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatALaw: Int { get } ``` |
| To | ``` var kAudioFormatALaw: AudioFormatID { get } ``` |

Modified [kAudioFormatAMR](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatamr)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAMR: Int { get } ``` |
| To | ``` var kAudioFormatAMR: AudioFormatID { get } ``` |

Modified [kAudioFormatAMR_WB](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatamr_wb)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAMR_WB: Int { get } ``` |
| To | ``` var kAudioFormatAMR_WB: AudioFormatID { get } ``` |

Modified [kAudioFormatAppleIMA4](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatappleima4)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAppleIMA4: Int { get } ``` |
| To | ``` var kAudioFormatAppleIMA4: AudioFormatID { get } ``` |

Modified [kAudioFormatAppleLossless](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatapplelossless)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAppleLossless: Int { get } ``` |
| To | ``` var kAudioFormatAppleLossless: AudioFormatID { get } ``` |

Modified [kAudioFormatAudible](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformataudible)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatAudible: Int { get } ``` |
| To | ``` var kAudioFormatAudible: AudioFormatID { get } ``` |

Modified [kAudioFormatDVIIntelIMA](https://developer.apple.com/documentation/coreaudio/kaudioformatdviintelima)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatDVIIntelIMA: Int { get } ``` |
| To | ``` var kAudioFormatDVIIntelIMA: AudioFormatID { get } ``` |

Modified [kAudioFormatFlagIsAlignedHigh](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagisalignedhigh)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsAlignedHigh: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsAlignedHigh: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsBigEndian](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagisbigendian)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsBigEndian: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsBigEndian: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsFloat](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagisfloat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsFloat: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsFloat: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsNonInterleaved](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagisnoninterleaved)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsNonInterleaved: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsNonInterleaved: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsNonMixable](https://developer.apple.com/documentation/coreaudio/kaudioformatflagisnonmixable)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsNonMixable: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsNonMixable: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsPacked](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagispacked)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsPacked: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsPacked: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagIsSignedInteger](https://developer.apple.com/documentation/coreaudio/kaudioformatflagissignedinteger)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagIsSignedInteger: Int { get } ``` |
| To | ``` var kAudioFormatFlagIsSignedInteger: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagsAreAllClear](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/kaudioformatflagsareallclear)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagsAreAllClear: Int { get } ``` |
| To | ``` var kAudioFormatFlagsAreAllClear: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagsNativeEndian](https://developer.apple.com/documentation/coreaudio/kaudioformatflagsnativeendian)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagsNativeEndian: Int { get } ``` |
| To | ``` var kAudioFormatFlagsNativeEndian: AudioFormatFlags { get } ``` |

Modified [kAudioFormatFlagsNativeFloatPacked](https://developer.apple.com/documentation/coreaudio/kaudioformatflagsnativefloatpacked)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatFlagsNativeFloatPacked: Int { get } ``` |
| To | ``` var kAudioFormatFlagsNativeFloatPacked: AudioFormatFlags { get } ``` |

Modified [kAudioFormatiLBC](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatilbc)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatiLBC: Int { get } ``` |
| To | ``` var kAudioFormatiLBC: AudioFormatID { get } ``` |

Modified [kAudioFormatLinearPCM](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatlinearpcm)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatLinearPCM: Int { get } ``` |
| To | ``` var kAudioFormatLinearPCM: AudioFormatID { get } ``` |

Modified [kAudioFormatMACE3](https://developer.apple.com/documentation/coreaudio/kaudioformatmace3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMACE3: Int { get } ``` |
| To | ``` var kAudioFormatMACE3: AudioFormatID { get } ``` |

Modified [kAudioFormatMACE6](https://developer.apple.com/documentation/coreaudio/kaudioformatmace6)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMACE6: Int { get } ``` |
| To | ``` var kAudioFormatMACE6: AudioFormatID { get } ``` |

Modified [kAudioFormatMicrosoftGSM](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmicrosoftgsm)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMicrosoftGSM: Int { get } ``` |
| To | ``` var kAudioFormatMicrosoftGSM: AudioFormatID { get } ``` |

Modified [kAudioFormatMIDIStream](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmidistream)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMIDIStream: Int { get } ``` |
| To | ``` var kAudioFormatMIDIStream: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_ELD](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeg4aac_eld)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_ELD: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_ELD: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_ELD_SBR](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeg4aac_eld_sbr)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_ELD_SBR: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_ELD_SBR: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_ELD_V2](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_eld_v2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_ELD_V2: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_ELD_V2: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_HE](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_he)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_HE: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_HE: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_HE_V2](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_he_v2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_HE_V2: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_HE_V2: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_LD](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4aac_ld)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_LD: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_LD: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4AAC_Spatial](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeg4aac_spatial)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4AAC_Spatial: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4AAC_Spatial: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4CELP](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4celp)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4CELP: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4CELP: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4HVXC](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeg4hvxc)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4HVXC: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4HVXC: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEG4TwinVQ](https://developer.apple.com/documentation/coreaudio/kaudioformatmpeg4twinvq)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEG4TwinVQ: Int { get } ``` |
| To | ``` var kAudioFormatMPEG4TwinVQ: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEGLayer1](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeglayer1)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEGLayer1: Int { get } ``` |
| To | ``` var kAudioFormatMPEGLayer1: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEGLayer2](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeglayer2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEGLayer2: Int { get } ``` |
| To | ``` var kAudioFormatMPEGLayer2: AudioFormatID { get } ``` |

Modified [kAudioFormatMPEGLayer3](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatmpeglayer3)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatMPEGLayer3: Int { get } ``` |
| To | ``` var kAudioFormatMPEGLayer3: AudioFormatID { get } ``` |

Modified [kAudioFormatParameterValueStream](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatparametervaluestream)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatParameterValueStream: Int { get } ``` |
| To | ``` var kAudioFormatParameterValueStream: AudioFormatID { get } ``` |

Modified [kAudioFormatQDesign](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatqdesign)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatQDesign: Int { get } ``` |
| To | ``` var kAudioFormatQDesign: AudioFormatID { get } ``` |

Modified [kAudioFormatQDesign2](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatqdesign2)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatQDesign2: Int { get } ``` |
| To | ``` var kAudioFormatQDesign2: AudioFormatID { get } ``` |

Modified [kAudioFormatQUALCOMM](https://developer.apple.com/documentation/coreaudio/kaudioformatqualcomm)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatQUALCOMM: Int { get } ``` |
| To | ``` var kAudioFormatQUALCOMM: AudioFormatID { get } ``` |

Modified [kAudioFormatTimeCode](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformattimecode)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatTimeCode: Int { get } ``` |
| To | ``` var kAudioFormatTimeCode: AudioFormatID { get } ``` |

Modified [kAudioFormatULaw](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatulaw)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioFormatULaw: Int { get } ``` |
| To | ``` var kAudioFormatULaw: AudioFormatID { get } ``` |

Modified [kAudioStreamAnyRate](https://developer.apple.com/documentation/coreaudio/kaudiostreamanyrate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAudioStreamAnyRate: Int { get } ``` | iOS 8.0 |
| To | ``` let kAudioStreamAnyRate: Float64 ``` | iOS 9.0 |

Modified [kLinearPCMFormatFlagIsAlignedHigh](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagisalignedhigh)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsAlignedHigh: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsAlignedHigh: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsBigEndian](https://developer.apple.com/documentation/coreaudio/klinearpcmformatflagisbigendian)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsBigEndian: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsBigEndian: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsFloat](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagisfloat)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsFloat: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsFloat: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsNonInterleaved](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagisnoninterleaved)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsNonInterleaved: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsNonInterleaved: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsNonMixable](https://developer.apple.com/documentation/coreaudio/klinearpcmformatflagisnonmixable)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsNonMixable: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsNonMixable: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsPacked](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagispacked)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsPacked: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsPacked: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagIsSignedInteger](https://developer.apple.com/documentation/coreaudio/klinearpcmformatflagissignedinteger)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagIsSignedInteger: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagIsSignedInteger: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagsAreAllClear](https://developer.apple.com/documentation/coreaudio/klinearpcmformatflagsareallclear)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagsAreAllClear: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagsAreAllClear: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagsSampleFractionMask](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagssamplefractionmask)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagsSampleFractionMask: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagsSampleFractionMask: AudioFormatFlags { get } ``` |

Modified [kLinearPCMFormatFlagsSampleFractionShift](https://developer.apple.com/documentation/coreaudio/1572097-audiostreambasicdescription_flag/klinearpcmformatflagssamplefractionshift)

|  | Declaration |
| --- | --- |
| From | ``` var kLinearPCMFormatFlagsSampleFractionShift: Int { get } ``` |
| To | ``` var kLinearPCMFormatFlagsSampleFractionShift: AudioFormatFlags { get } ``` |

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
