---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreAudio.html
archived_at: '2026-07-18T02:53:23.639990Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreAudio Changes for Swift

### CoreAudio

Removed AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: UInt32, mCoordinates: (Float32, Float32, Float32))Removed AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: UInt32, mNumberChannelDescriptions: UInt32, mChannelDescriptions: (AudioChannelDescription))Removed AudioHardwareIOProcStreamUsage.init()Removed AudioHardwareIOProcStreamUsage.init(mIOProc: UnsafeMutablePointer<Void>, mNumberStreams: UInt32, mStreamIsOn: (UInt32))Removed AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: UInt32, mReserved: UInt32)Removed AudioValueTranslation.init()Removed AudioValueTranslation.init(mInputData: UnsafeMutablePointer<Void>, mInputDataSize: UInt32, mOutputData: UnsafeMutablePointer<Void>, mOutputDataSize: UInt32)Removed SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: UInt32, mFlags: UInt32, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Removed UnsafeMutableAudioBufferListPointer.generate() -> IndexingGenerator<UnsafeMutableAudioBufferListPointer>Removed kAudioChannelBit_CenterRemoved kAudioChannelBit_CenterSurroundRemoved kAudioChannelBit_LeftRemoved kAudioChannelBit_LeftCenterRemoved kAudioChannelBit_LeftSurroundRemoved kAudioChannelBit_LeftSurroundDirectRemoved kAudioChannelBit_LFEScreenRemoved kAudioChannelBit_RightRemoved kAudioChannelBit_RightCenterRemoved kAudioChannelBit_RightSurroundRemoved kAudioChannelBit_RightSurroundDirectRemoved kAudioChannelBit_TopBackCenterRemoved kAudioChannelBit_TopBackLeftRemoved kAudioChannelBit_TopBackRightRemoved kAudioChannelBit_TopCenterSurroundRemoved kAudioChannelBit_VerticalHeightCenterRemoved kAudioChannelBit_VerticalHeightLeftRemoved kAudioChannelBit_VerticalHeightRightRemoved kAudioChannelCoordinates_AzimuthRemoved kAudioChannelCoordinates_BackFrontRemoved kAudioChannelCoordinates_DistanceRemoved kAudioChannelCoordinates_DownUpRemoved kAudioChannelCoordinates_ElevationRemoved kAudioChannelCoordinates_LeftRightRemoved kAudioChannelFlags_AllOffRemoved kAudioChannelFlags_MetersRemoved kAudioChannelFlags_RectangularCoordinatesRemoved kAudioChannelFlags_SphericalCoordinatesRemoved kAudioHardwarePowerHintFavorSavingPowerRemoved kAudioHardwarePowerHintNoneRemoved kAudioLevelControlTranferFunction10Over1Removed kAudioLevelControlTranferFunction11Over1Removed kAudioLevelControlTranferFunction12Over1Removed kAudioLevelControlTranferFunction1Over2Removed kAudioLevelControlTranferFunction1Over3Removed kAudioLevelControlTranferFunction2Over1Removed kAudioLevelControlTranferFunction3Over1Removed kAudioLevelControlTranferFunction3Over2Removed kAudioLevelControlTranferFunction3Over4Removed kAudioLevelControlTranferFunction4Over1Removed kAudioLevelControlTranferFunction5Over1Removed kAudioLevelControlTranferFunction6Over1Removed kAudioLevelControlTranferFunction7Over1Removed kAudioLevelControlTranferFunction8Over1Removed kAudioLevelControlTranferFunction9Over1Removed kAudioLevelControlTranferFunctionLinearRemoved kAudioTimeStampHostTimeValidRemoved kAudioTimeStampRateScalarValidRemoved kAudioTimeStampSampleHostTimeValidRemoved kAudioTimeStampSampleTimeValidRemoved kAudioTimeStampSMPTETimeValidRemoved kAudioTimeStampWordClockTimeValidRemoved kMPEG4Object_AAC_LCRemoved kMPEG4Object_AAC_LTPRemoved kMPEG4Object_AAC_MainRemoved kMPEG4Object_AAC_SBRRemoved kMPEG4Object_AAC_ScalableRemoved kMPEG4Object_AAC_SSRRemoved kMPEG4Object_CELPRemoved kMPEG4Object_HVXCRemoved kMPEG4Object_TwinVQRemoved kSMPTETimeRunningRemoved kSMPTETimeType2398Removed kSMPTETimeType24Removed kSMPTETimeType25Removed kSMPTETimeType2997Removed kSMPTETimeType2997DropRemoved kSMPTETimeType30Removed kSMPTETimeType30DropRemoved kSMPTETimeType50Removed kSMPTETimeType5994Removed kSMPTETimeType5994DropRemoved kSMPTETimeType60Removed kSMPTETimeType60DropRemoved kSMPTETimeValidAdded [AudioChannelBitmap [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap)Added [AudioChannelBitmap.Bit_Center](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422558-bit_center)Added [AudioChannelBitmap.Bit_CenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421862-bit_centersurround)Added [AudioChannelBitmap.Bit_Left](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422633-bit_left)Added [AudioChannelBitmap.Bit_LeftCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421656-bit_leftcenter)Added [AudioChannelBitmap.Bit_LeftSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422177-bit_leftsurround)Added [AudioChannelBitmap.Bit_LeftSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_leftsurrounddirect)Added [AudioChannelBitmap.Bit_LFEScreen](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422510-bit_lfescreen)Added [AudioChannelBitmap.Bit_Right](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421518-bit_right)Added [AudioChannelBitmap.Bit_RightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422165-bit_rightcenter)Added [AudioChannelBitmap.Bit_RightSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1421938-bit_rightsurround)Added [AudioChannelBitmap.Bit_RightSurroundDirect](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_rightsurrounddirect)Added [AudioChannelBitmap.Bit_TopBackCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_topbackcenter)Added [AudioChannelBitmap.Bit_TopBackLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423190-bit_topbackleft)Added [AudioChannelBitmap.Bit_TopBackRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1423004-bit_topbackright)Added [AudioChannelBitmap.Bit_TopCenterSurround](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422248-bit_topcentersurround)Added [AudioChannelBitmap.Bit_VerticalHeightCenter](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/1422161-bit_verticalheightcenter)Added [AudioChannelBitmap.Bit_VerticalHeightLeft](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightleft)Added [AudioChannelBitmap.Bit_VerticalHeightRight](https://developer.apple.com/documentation/coreaudio/audiochannelbitmap/kaudiochannelbit_verticalheightright)Added AudioChannelBitmap.init(rawValue: UInt32)Added [AudioChannelCoordinateIndex [enum]](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex)Added [AudioChannelCoordinateIndex.Coordinates_Azimuth](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_azimuth)Added [AudioChannelCoordinateIndex.Coordinates_BackFront](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_backfront)Added [AudioChannelCoordinateIndex.Coordinates_Distance](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_distance)Added [AudioChannelCoordinateIndex.Coordinates_DownUp](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/coordinates_downup)Added [AudioChannelCoordinateIndex.Coordinates_Elevation](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_elevation)Added [AudioChannelCoordinateIndex.Coordinates_LeftRight](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex/kaudiochannelcoordinates_leftright)Added AudioChannelDescription.init(mChannelLabel: AudioChannelLabel, mChannelFlags: AudioChannelFlags, mCoordinates: (Float32, Float32, Float32))Added [AudioChannelFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiochannelflags)Added [AudioChannelFlags.AllOff](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_alloff)Added AudioChannelFlags.init(rawValue: UInt32)Added [AudioChannelFlags.Meters](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1422914-meters)Added [AudioChannelFlags.RectangularCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/kaudiochannelflags_rectangularcoordinates)Added [AudioChannelFlags.SphericalCoordinates](https://developer.apple.com/documentation/coreaudio/audiochannelflags/1421586-sphericalcoordinates)Added AudioChannelLayout.init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: AudioChannelBitmap, mNumberChannelDescriptions: UInt32, mChannelDescriptions: (AudioChannelDescription))Added [AudioHardwarePowerHint [enum]](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint)Added [AudioHardwarePowerHint.FavorSavingPower](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintfavorsavingpower)Added [AudioHardwarePowerHint.None](https://developer.apple.com/documentation/coreaudio/audiohardwarepowerhint/kaudiohardwarepowerhintnone)Added [AudioLevelControlTransferFunction [enum]](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction)Added [AudioLevelControlTransferFunction.TranferFunction10Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction10over1)Added [AudioLevelControlTransferFunction.TranferFunction11Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction11over1)Added [AudioLevelControlTransferFunction.TranferFunction12Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction12over1)Added [AudioLevelControlTransferFunction.TranferFunction1Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction1over2)Added [AudioLevelControlTransferFunction.TranferFunction1Over3](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction1over3)Added [AudioLevelControlTransferFunction.TranferFunction2Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction2over1)Added [AudioLevelControlTransferFunction.TranferFunction3Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction3over1)Added [AudioLevelControlTransferFunction.TranferFunction3Over2](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction3over2)Added [AudioLevelControlTransferFunction.TranferFunction3Over4](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction3over4)Added [AudioLevelControlTransferFunction.TranferFunction4Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction4over1)Added [AudioLevelControlTransferFunction.TranferFunction5Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction5over1)Added [AudioLevelControlTransferFunction.TranferFunction6Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction6over1)Added [AudioLevelControlTransferFunction.TranferFunction7Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction7over1)Added [AudioLevelControlTransferFunction.TranferFunction8Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/kaudiolevelcontroltranferfunction8over1)Added [AudioLevelControlTransferFunction.TranferFunction9Over1](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunction9over1)Added [AudioLevelControlTransferFunction.TranferFunctionLinear](https://developer.apple.com/documentation/coreaudio/audiolevelcontroltransferfunction/tranferfunctionlinear)Added AudioTimeStamp.init(mSampleTime: Float64, mHostTime: UInt64, mRateScalar: Float64, mWordClockTime: UInt64, mSMPTETime: SMPTETime, mFlags: AudioTimeStampFlags, mReserved: UInt32)Added [AudioTimeStampFlags [struct]](https://developer.apple.com/documentation/coreaudio/audiotimestampflags)Added [AudioTimeStampFlags.HostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423064-hosttimevalid)Added AudioTimeStampFlags.init(rawValue: UInt32)Added [AudioTimeStampFlags.NothingValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampnothingvalid)Added [AudioTimeStampFlags.RateScalarValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422238-ratescalarvalid)Added [AudioTimeStampFlags.SampleHostTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422143-samplehosttimevalid)Added [AudioTimeStampFlags.SampleTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1423034-sampletimevalid)Added [AudioTimeStampFlags.SMPTETimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/kaudiotimestampsmptetimevalid)Added [AudioTimeStampFlags.WordClockTimeValid](https://developer.apple.com/documentation/coreaudio/audiotimestampflags/1422676-wordclocktimevalid)Added [MPEG4ObjectID [enum]](https://developer.apple.com/documentation/coreaudio/mpeg4objectid)Added [MPEG4ObjectID.AAC_LC](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/aac_lc)Added [MPEG4ObjectID.AAC_LTP](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_ltp)Added [MPEG4ObjectID.AAC_Main](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_main)Added [MPEG4ObjectID.AAC_SBR](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_sbr)Added [MPEG4ObjectID.AAC_Scalable](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/aac_scalable)Added [MPEG4ObjectID.AAC_SSR](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_aac_ssr)Added [MPEG4ObjectID.CELP](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/celp)Added [MPEG4ObjectID.HVXC](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/kmpeg4object_hvxc)Added [MPEG4ObjectID.TwinVQ](https://developer.apple.com/documentation/coreaudio/mpeg4objectid/twinvq)Added SMPTETime.init(mSubframes: Int16, mSubframeDivisor: Int16, mCounter: UInt32, mType: SMPTETimeType, mFlags: SMPTETimeFlags, mHours: Int16, mMinutes: Int16, mSeconds: Int16, mFrames: Int16)Added [SMPTETimeFlags [struct]](https://developer.apple.com/documentation/coreaudio/smptetimeflags)Added SMPTETimeFlags.init(rawValue: UInt32)Added [SMPTETimeFlags.Running](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimerunning)Added [SMPTETimeFlags.Unknown](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimeunknown)Added [SMPTETimeFlags.Valid](https://developer.apple.com/documentation/coreaudio/smptetimeflags/ksmptetimevalid)Added [SMPTETimeType [enum]](https://developer.apple.com/documentation/coreaudio/smptetimetype)Added [SMPTETimeType.Type2398](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2398)Added [SMPTETimeType.Type24](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype24)Added [SMPTETimeType.Type25](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype25)Added [SMPTETimeType.Type2997](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997)Added [SMPTETimeType.Type2997Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype2997drop)Added [SMPTETimeType.Type30](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30)Added [SMPTETimeType.Type30Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype30drop)Added [SMPTETimeType.Type50](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype50)Added [SMPTETimeType.Type5994](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994)Added [SMPTETimeType.Type5994Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype5994drop)Added [SMPTETimeType.Type60](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60)Added [SMPTETimeType.Type60Drop](https://developer.apple.com/documentation/coreaudio/smptetimetype/ksmptetimetype60drop)Added [AudioChannelLayoutTag_GetNumberOfChannels(_: AudioChannelLayoutTag) -> UInt32](https://developer.apple.com/documentation/coreaudio/1422032-audiochannellayouttag_getnumbero)Added [AudioSampleType](https://developer.apple.com/documentation/coreaudio/audiosampletype)Added [AudioUnitSampleType](https://developer.apple.com/documentation/coreaudio/audiounitsampletype)Added [kAudioFormatEnhancedAC3](https://developer.apple.com/documentation/coreaudio/1572096-audio_data_format_identifiers/kaudioformatenhancedac3)Added [kAudioFormatFlagsAudioUnitCanonical](https://developer.apple.com/documentation/coreaudio/1572098-audiostreambasicdescription_flag/kaudioformatflagsaudiounitcanonical)Added [kAudioFormatFlagsCanonical](https://developer.apple.com/documentation/coreaudio/1572098-audiostreambasicdescription_flag/kaudioformatflagscanonical)Modified [AudioBuffer [struct]](https://developer.apple.com/documentation/coreaudio/audiobuffer)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } extension AudioBuffer {     init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) } ``` |
| To | ``` struct AudioBuffer {     var mNumberChannels: UInt32     var mDataByteSize: UInt32     var mData: UnsafeMutablePointer<Void>     init()     init(mNumberChannels mNumberChannels: UInt32, mDataByteSize mDataByteSize: UInt32, mData mData: UnsafeMutablePointer<Void>) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } extension AudioBuffer {     init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) } ``` |

Modified AudioBuffer.init<Element>(_: UnsafeMutableBufferPointer<Element>, numberOfChannels: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` init<T>(_ typedBuffer: UnsafeMutableBufferPointer<T>, numberOfChannels numberOfChannels: Int) ``` | OS X 10.10.3 | -- |
| To | ``` init<Element>(_ typedBuffer: UnsafeMutableBufferPointer<Element>, numberOfChannels numberOfChannels: Int) ``` | OS X 10.11 | Element |

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

Modified [AudioHardwareIOProcStreamUsage [struct]](https://developer.apple.com/documentation/coreaudio/audiohardwareioprocstreamusage)

|  | Declaration |
| --- | --- |
| From | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafeMutablePointer<Void>     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32)     init()     init(mIOProc mIOProc: UnsafeMutablePointer<Void>, mNumberStreams mNumberStreams: UInt32, mStreamIsOn mStreamIsOn: (UInt32)) } ``` |
| To | ``` struct AudioHardwareIOProcStreamUsage {     var mIOProc: UnsafeMutablePointer<Void>     var mNumberStreams: UInt32     var mStreamIsOn: (UInt32) } ``` |

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
| From | OS X 10.10.3 |
| To | OS X 10.11 |

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
| From | OS X 10.10.3 |
| To | OS X 10.11 |

Modified [AudioDeviceCreateIOProcID(_: AudioObjectID, _: AudioDeviceIOProc, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1423215-audiodevicecreateioprocid)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutablePointer<Void>, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID>) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcID(_ inDevice: AudioObjectID, _ inProc: AudioDeviceIOProc, _ inClientData: UnsafeMutablePointer<Void>, _ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>) -> OSStatus ``` |

Modified [AudioDeviceCreateIOProcIDWithBlock(_: UnsafeMutablePointer<AudioDeviceIOProcID?>, _: AudioObjectID, _: dispatch_queue_t?, _: AudioDeviceIOBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422986-audiodevicecreateioprocidwithblo)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID>, _ inDevice: AudioObjectID, _ inDispatchQueue: dispatch_queue_t!, _ inIOBlock: AudioDeviceIOBlock!) -> OSStatus ``` |
| To | ``` func AudioDeviceCreateIOProcIDWithBlock(_ outIOProcID: UnsafeMutablePointer<AudioDeviceIOProcID?>, _ inDevice: AudioObjectID, _ inDispatchQueue: dispatch_queue_t?, _ inIOBlock: AudioDeviceIOBlock) -> OSStatus ``` |

Modified [AudioDeviceIOProc](https://developer.apple.com/documentation/coreaudio/audiodeviceioproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDeviceIOProc = CFunctionPointer<((AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioDeviceIOProc = (AudioObjectID, UnsafePointer<AudioTimeStamp>, UnsafePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AudioTimeStamp>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioDevicePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiodevicepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioDevicePropertyListenerProc = CFunctionPointer<((AudioDeviceID, UInt32, Boolean, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioDevicePropertyListenerProc = (AudioDeviceID, UInt32, DarwinBoolean, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioDeviceStart(_: AudioObjectID, _: AudioDeviceIOProcID?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422884-audiodevicestart)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStart(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID) -> OSStatus ``` |
| To | ``` func AudioDeviceStart(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?) -> OSStatus ``` |

Modified [AudioDeviceStartAtTime(_: AudioObjectID, _: AudioDeviceIOProcID?, _: UnsafeMutablePointer<AudioTimeStamp>, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422331-audiodevicestartattime)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` |
| To | ``` func AudioDeviceStartAtTime(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?, _ ioRequestedStartTime: UnsafeMutablePointer<AudioTimeStamp>, _ inFlags: UInt32) -> OSStatus ``` |

Modified [AudioDeviceStop(_: AudioObjectID, _: AudioDeviceIOProcID?) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1421761-audiodevicestop)

|  | Declaration |
| --- | --- |
| From | ``` func AudioDeviceStop(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID) -> OSStatus ``` |
| To | ``` func AudioDeviceStop(_ inDevice: AudioObjectID, _ inProcID: AudioDeviceIOProcID?) -> OSStatus ``` |

Modified [AudioHardwareCreateAggregateDevice(_: CFDictionary, _: UnsafeMutablePointer<AudioObjectID>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422096-audiohardwarecreateaggregatedevi)

|  | Declaration |
| --- | --- |
| From | ``` func AudioHardwareCreateAggregateDevice(_ inDescription: CFDictionary!, _ outDeviceID: UnsafeMutablePointer<AudioObjectID>) -> OSStatus ``` |
| To | ``` func AudioHardwareCreateAggregateDevice(_ inDescription: CFDictionary, _ outDeviceID: UnsafeMutablePointer<AudioObjectID>) -> OSStatus ``` |

Modified [AudioHardwarePropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiohardwarepropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioHardwarePropertyListenerProc = CFunctionPointer<((AudioHardwarePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioHardwarePropertyListenerProc = (AudioHardwarePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioObjectAddPropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: dispatch_queue_t?, _: AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1422686-audioobjectaddpropertylistenerbl)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` |
| To | ``` func AudioObjectAddPropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t?, _ inListener: AudioObjectPropertyListenerBlock) -> OSStatus ``` |

Modified [AudioObjectHasProperty(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>) -> Bool](https://developer.apple.com/documentation/coreaudio/1422538-audioobjecthasproperty)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectHasProperty(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>) -> Boolean ``` |
| To | ``` func AudioObjectHasProperty(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>) -> Bool ``` |

Modified [AudioObjectIsPropertySettable(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1423182-audioobjectispropertysettable)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func AudioObjectIsPropertySettable(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ outIsSettable: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified [AudioObjectPropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audioobjectpropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioObjectPropertyListenerProc = CFunctionPointer<((AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioObjectPropertyListenerProc = (AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [AudioObjectRemovePropertyListenerBlock(_: AudioObjectID, _: UnsafePointer<AudioObjectPropertyAddress>, _: dispatch_queue_t?, _: AudioObjectPropertyListenerBlock) -> OSStatus](https://developer.apple.com/documentation/coreaudio/1421640-audioobjectremovepropertylistene)

|  | Declaration |
| --- | --- |
| From | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t!, _ inListener: AudioObjectPropertyListenerBlock!) -> OSStatus ``` |
| To | ``` func AudioObjectRemovePropertyListenerBlock(_ inObjectID: AudioObjectID, _ inAddress: UnsafePointer<AudioObjectPropertyAddress>, _ inDispatchQueue: dispatch_queue_t?, _ inListener: AudioObjectPropertyListenerBlock) -> OSStatus ``` |

Modified [AudioStreamPropertyListenerProc](https://developer.apple.com/documentation/coreaudio/audiostreampropertylistenerproc)

|  | Declaration |
| --- | --- |
| From | ``` typealias AudioStreamPropertyListenerProc = CFunctionPointer<((AudioStreamID, UInt32, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias AudioStreamPropertyListenerProc = (AudioStreamID, UInt32, AudioDevicePropertyID, UnsafeMutablePointer<Void>) -> OSStatus ``` |

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

Modified [kAudioAggregateDeviceClassID](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedeviceclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioAggregateDeviceClassID: Int { get } ``` |
| To | ``` var kAudioAggregateDeviceClassID: AudioClassID { get } ``` |

Modified [kAudioAggregateDevicePropertyActiveSubDeviceList](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedevicepropertyactivesubdevicelist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioAggregateDevicePropertyActiveSubDeviceList: Int { get } ``` |
| To | ``` var kAudioAggregateDevicePropertyActiveSubDeviceList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioAggregateDevicePropertyComposition](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedevicepropertycomposition)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioAggregateDevicePropertyComposition: Int { get } ``` |
| To | ``` var kAudioAggregateDevicePropertyComposition: AudioObjectPropertySelector { get } ``` |

Modified [kAudioAggregateDevicePropertyFullSubDeviceList](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedevicepropertyfullsubdevicelist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioAggregateDevicePropertyFullSubDeviceList: Int { get } ``` |
| To | ``` var kAudioAggregateDevicePropertyFullSubDeviceList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioAggregateDevicePropertyMasterSubDevice](https://developer.apple.com/documentation/coreaudio/kaudioaggregatedevicepropertymastersubdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioAggregateDevicePropertyMasterSubDevice: Int { get } ``` |
| To | ``` var kAudioAggregateDevicePropertyMasterSubDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBooleanControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiobooleancontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBooleanControlClassID: Int { get } ``` |
| To | ``` var kAudioBooleanControlClassID: AudioClassID { get } ``` |

Modified [kAudioBooleanControlPropertyValue](https://developer.apple.com/documentation/coreaudio/kaudiobooleancontrolpropertyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBooleanControlPropertyValue: Int { get } ``` |
| To | ``` var kAudioBooleanControlPropertyValue: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBootChimeVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/1580719-anonymous/kaudiobootchimevolumecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBootChimeVolumeControlClassID: Int { get } ``` |
| To | ``` var kAudioBootChimeVolumeControlClassID: AudioClassID { get } ``` |

Modified [kAudioBoxClassID](https://developer.apple.com/documentation/coreaudio/kaudioboxclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxClassID: Int { get } ``` |
| To | ``` var kAudioBoxClassID: AudioClassID { get } ``` |

Modified [kAudioBoxPropertyAcquired](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyacquired)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyAcquired: Int { get } ``` |
| To | ``` var kAudioBoxPropertyAcquired: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyAcquisitionFailed](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyacquisitionfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyAcquisitionFailed: Int { get } ``` |
| To | ``` var kAudioBoxPropertyAcquisitionFailed: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyBoxUID](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyboxuid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyBoxUID: Int { get } ``` |
| To | ``` var kAudioBoxPropertyBoxUID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyDeviceList](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertydevicelist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyDeviceList: Int { get } ``` |
| To | ``` var kAudioBoxPropertyDeviceList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyHasAudio](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyhasaudio)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyHasAudio: Int { get } ``` |
| To | ``` var kAudioBoxPropertyHasAudio: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyHasMIDI](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyhasmidi)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyHasMIDI: Int { get } ``` |
| To | ``` var kAudioBoxPropertyHasMIDI: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyHasVideo](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertyhasvideo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyHasVideo: Int { get } ``` |
| To | ``` var kAudioBoxPropertyHasVideo: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyIsProtected](https://developer.apple.com/documentation/coreaudio/kaudioboxpropertyisprotected)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyIsProtected: Int { get } ``` |
| To | ``` var kAudioBoxPropertyIsProtected: AudioObjectPropertySelector { get } ``` |

Modified [kAudioBoxPropertyTransportType](https://developer.apple.com/documentation/coreaudio/1494522-anonymous/kaudioboxpropertytransporttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioBoxPropertyTransportType: Int { get } ``` |
| To | ``` var kAudioBoxPropertyTransportType: AudioObjectPropertySelector { get } ``` |

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

Modified [kAudioClipLightControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiocliplightcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioClipLightControlClassID: Int { get } ``` |
| To | ``` var kAudioClipLightControlClassID: AudioClassID { get } ``` |

Modified [kAudioClockSourceControlClassID](https://developer.apple.com/documentation/coreaudio/1494554-anonymous/kaudioclocksourcecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioClockSourceControlClassID: Int { get } ``` |
| To | ``` var kAudioClockSourceControlClassID: AudioClassID { get } ``` |

Modified [kAudioClockSourceControlPropertyItemKind](https://developer.apple.com/documentation/coreaudio/1580736-anonymous/kaudioclocksourcecontrolpropertyitemkind)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioClockSourceControlPropertyItemKind: Int { get } ``` |
| To | ``` var kAudioClockSourceControlPropertyItemKind: AudioObjectPropertySelector { get } ``` |

Modified [kAudioClockSourceItemKindInternal](https://developer.apple.com/documentation/coreaudio/kaudioclocksourceitemkindinternal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioClockSourceItemKindInternal: Int { get } ``` |
| To | ``` var kAudioClockSourceItemKindInternal: UInt32 { get } ``` |

Modified [kAudioControlClassID](https://developer.apple.com/documentation/coreaudio/1494474-anonymous/kaudiocontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioControlClassID: Int { get } ``` |
| To | ``` var kAudioControlClassID: AudioClassID { get } ``` |

Modified [kAudioControlPropertyElement](https://developer.apple.com/documentation/coreaudio/1494571-anonymous/kaudiocontrolpropertyelement)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioControlPropertyElement: Int { get } ``` |
| To | ``` var kAudioControlPropertyElement: AudioObjectPropertySelector { get } ``` |

Modified [kAudioControlPropertyScope](https://developer.apple.com/documentation/coreaudio/1494571-anonymous/kaudiocontrolpropertyscope)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioControlPropertyScope: Int { get } ``` |
| To | ``` var kAudioControlPropertyScope: AudioObjectPropertySelector { get } ``` |

Modified [kAudioControlPropertyVariant](https://developer.apple.com/documentation/coreaudio/1580741-anonymous/kaudiocontrolpropertyvariant)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioControlPropertyVariant: Int { get } ``` |
| To | ``` var kAudioControlPropertyVariant: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDataDestinationControlClassID](https://developer.apple.com/documentation/coreaudio/1494554-anonymous/kaudiodatadestinationcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDataDestinationControlClassID: Int { get } ``` |
| To | ``` var kAudioDataDestinationControlClassID: AudioClassID { get } ``` |

Modified [kAudioDataSourceControlClassID](https://developer.apple.com/documentation/coreaudio/1494554-anonymous/kaudiodatasourcecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDataSourceControlClassID: Int { get } ``` |
| To | ``` var kAudioDataSourceControlClassID: AudioClassID { get } ``` |

Modified [kAudioDeviceClassID](https://developer.apple.com/documentation/coreaudio/kaudiodeviceclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceClassID: Int { get } ``` |
| To | ``` var kAudioDeviceClassID: AudioClassID { get } ``` |

Modified [kAudioDevicePermissionsError](https://developer.apple.com/documentation/coreaudio/kaudiodevicepermissionserror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePermissionsError: Int { get } ``` |
| To | ``` var kAudioDevicePermissionsError: OSStatus { get } ``` |

Modified [kAudioDeviceProcessorOverload](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodeviceprocessoroverload)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceProcessorOverload: Int { get } ``` |
| To | ``` var kAudioDeviceProcessorOverload: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyActualSampleRate](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyactualsamplerate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyActualSampleRate: Int { get } ``` |
| To | ``` var kAudioDevicePropertyActualSampleRate: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyAvailableNominalSampleRates](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyavailablenominalsamplerates)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyAvailableNominalSampleRates: Int { get } ``` |
| To | ``` var kAudioDevicePropertyAvailableNominalSampleRates: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyBufferFrameSize](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertybufferframesize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyBufferFrameSize: Int { get } ``` |
| To | ``` var kAudioDevicePropertyBufferFrameSize: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyBufferFrameSizeRange](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertybufferframesizerange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyBufferFrameSizeRange: Int { get } ``` |
| To | ``` var kAudioDevicePropertyBufferFrameSizeRange: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyBufferSize](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertybuffersize)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyBufferSize: Int { get } ``` |
| To | ``` var kAudioDevicePropertyBufferSize: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyBufferSizeRange](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertybuffersizerange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyBufferSizeRange: Int { get } ``` |
| To | ``` var kAudioDevicePropertyBufferSizeRange: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelCategoryName](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelcategoryname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelCategoryName: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelCategoryName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelCategoryNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelcategorynamecfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelCategoryNameCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelCategoryNameCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelName](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelName: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelnamecfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNameCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNameCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNominalLineLevel](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnominallinelevel)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNominalLineLevel: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNominalLineLevel: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNominalLineLevelNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnominallinelevelnameforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNominalLineLevelNameForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNominalLineLevelNameForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNominalLineLevelNameForIDCFString](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertychannelnominallinelevelnameforidcfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNominalLineLevelNameForIDCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNominalLineLevelNameForIDCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNominalLineLevels](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnominallinelevels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNominalLineLevels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNominalLineLevels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNumberName](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertychannelnumbername)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNumberName: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNumberName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyChannelNumberNameCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertychannelnumbernamecfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyChannelNumberNameCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyChannelNumberNameCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClipLight](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertycliplight)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClipLight: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClipLight: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockDomain](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyclockdomain)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockDomain: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockDomain: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockSource](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyclocksource)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockSource: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockSource: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockSourceKindForID](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyclocksourcekindforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockSourceKindForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockSourceKindForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockSourceNameForID](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertyclocksourcenameforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockSourceNameForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockSourceNameForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockSourceNameForIDCFString](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyclocksourcenameforidcfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockSourceNameForIDCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockSourceNameForIDCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyClockSources](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyclocksources)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyClockSources: Int { get } ``` |
| To | ``` var kAudioDevicePropertyClockSources: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyConfigurationApplication](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyconfigurationapplication)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyConfigurationApplication: Int { get } ``` |
| To | ``` var kAudioDevicePropertyConfigurationApplication: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDataSource](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydatasource)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDataSource: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDataSource: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDataSourceKindForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydatasourcekindforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDataSourceKindForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDataSourceKindForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDataSourceNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydatasourcenameforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDataSourceNameForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDataSourceNameForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDataSourceNameForIDCFString](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydatasourcenameforidcfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDataSourceNameForIDCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDataSourceNameForIDCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDataSources](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertydatasources)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDataSources: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDataSources: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceCanBeDefaultDevice](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicecanbedefaultdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceCanBeDefaultDevice: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceCanBeDefaultDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceCanBeDefaultSystemDevice](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicecanbedefaultsystemdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceCanBeDefaultSystemDevice: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceCanBeDefaultSystemDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceHasChanged](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertydevicehaschanged)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceHasChanged: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceHasChanged: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceIsAlive](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertydeviceisalive)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceIsAlive: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceIsAlive: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceIsRunning](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydeviceisrunning)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceIsRunning: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceIsRunning: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceIsRunningSomewhere](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydeviceisrunningsomewhere)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceIsRunningSomewhere: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceIsRunningSomewhere: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceManufacturer](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertydevicemanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceManufacturer: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceManufacturer: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceManufacturerCFString](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertydevicemanufacturercfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceManufacturerCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceManufacturerCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceName](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicename)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceName: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceNameCFString](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydevicenamecfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceNameCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceNameCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDeviceUID](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertydeviceuid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDeviceUID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDeviceUID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyDriverShouldOwniSub](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertydrivershouldownisub)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyDriverShouldOwniSub: Int { get } ``` |
| To | ``` var kAudioDevicePropertyDriverShouldOwniSub: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyHighPassFilterSetting](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyhighpassfiltersetting)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyHighPassFilterSetting: Int { get } ``` |
| To | ``` var kAudioDevicePropertyHighPassFilterSetting: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyHighPassFilterSettingNameForID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyhighpassfiltersettingnameforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyHighPassFilterSettingNameForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyHighPassFilterSettingNameForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyHighPassFilterSettingNameForIDCFString](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyhighpassfiltersettingnameforidcfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyHighPassFilterSettingNameForIDCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyHighPassFilterSettingNameForIDCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyHighPassFilterSettings](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyhighpassfiltersettings)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyHighPassFilterSettings: Int { get } ``` |
| To | ``` var kAudioDevicePropertyHighPassFilterSettings: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyHogMode](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyhogmode)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyHogMode: Int { get } ``` |
| To | ``` var kAudioDevicePropertyHogMode: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyIcon](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyicon)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyIcon: Int { get } ``` |
| To | ``` var kAudioDevicePropertyIcon: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyIOCycleUsage](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertyiocycleusage)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyIOCycleUsage: Int { get } ``` |
| To | ``` var kAudioDevicePropertyIOCycleUsage: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyIOProcStreamUsage](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyioprocstreamusage)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyIOProcStreamUsage: Int { get } ``` |
| To | ``` var kAudioDevicePropertyIOProcStreamUsage: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyIOStoppedAbnormally](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyiostoppedabnormally)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyIOStoppedAbnormally: Int { get } ``` |
| To | ``` var kAudioDevicePropertyIOStoppedAbnormally: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyIsHidden](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyishidden)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyIsHidden: Int { get } ``` |
| To | ``` var kAudioDevicePropertyIsHidden: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyJackIsConnected](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyjackisconnected)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyJackIsConnected: Int { get } ``` |
| To | ``` var kAudioDevicePropertyJackIsConnected: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyLatency](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertylatency)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyLatency: Int { get } ``` |
| To | ``` var kAudioDevicePropertyLatency: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyListenback](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertylistenback)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyListenback: Int { get } ``` |
| To | ``` var kAudioDevicePropertyListenback: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyModelUID](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertymodeluid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyModelUID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyModelUID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyMute](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertymute)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyMute: Int { get } ``` |
| To | ``` var kAudioDevicePropertyMute: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyNominalSampleRate](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertynominalsamplerate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyNominalSampleRate: Int { get } ``` |
| To | ``` var kAudioDevicePropertyNominalSampleRate: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPhantomPower](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyphantompower)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPhantomPower: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPhantomPower: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPhaseInvert](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyphaseinvert)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPhaseInvert: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPhaseInvert: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThru](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythru)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThru: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThru: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruDestination](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythrudestination)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruDestination: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruDestination: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruDestinationNameForID](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertyplaythrudestinationnameforid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruDestinationNameForID: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruDestinationNameForID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruDestinationNameForIDCFString](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythrudestinationnameforidcfstring)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruDestinationNameForIDCFString: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruDestinationNameForIDCFString: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruDestinations](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythrudestinations)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruDestinations: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruDestinations: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruSolo](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythrusolo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruSolo: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruSolo: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruStereoPan](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythrustereopan)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruStereoPan: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruStereoPan: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruStereoPanChannels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythrustereopanchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruStereoPanChannels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruStereoPanChannels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythruvolumedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythruvolumedecibelstoscalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeDecibelsToScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeDecibelsToScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythruvolumedecibelstoscalartransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeDecibelsToScalarTransferFunction: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeDecibelsToScalarTransferFunction: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeRangeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyplaythruvolumerangedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeRangeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeRangeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeScalar](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythruvolumescalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlayThruVolumeScalarToDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyplaythruvolumescalartodecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlayThruVolumeScalarToDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlayThruVolumeScalarToDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPlugIn](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertyplugin)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPlugIn: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPlugIn: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPreferredChannelLayout](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertypreferredchannellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPreferredChannelLayout: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPreferredChannelLayout: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyPreferredChannelsForStereo](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertypreferredchannelsforstereo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyPreferredChannelsForStereo: Int { get } ``` |
| To | ``` var kAudioDevicePropertyPreferredChannelsForStereo: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyRegisterBufferList](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyregisterbufferlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyRegisterBufferList: Int { get } ``` |
| To | ``` var kAudioDevicePropertyRegisterBufferList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyRelatedDevices](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertyrelateddevices)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyRelatedDevices: Int { get } ``` |
| To | ``` var kAudioDevicePropertyRelatedDevices: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySafetyOffset](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertysafetyoffset)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySafetyOffset: Int { get } ``` |
| To | ``` var kAudioDevicePropertySafetyOffset: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyScopeInput](https://developer.apple.com/documentation/coreaudio/1580726-anonymous/kaudiodevicepropertyscopeinput)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyScopeInput: Int { get } ``` |
| To | ``` var kAudioDevicePropertyScopeInput: AudioObjectPropertyScope { get } ``` |

Modified [kAudioDevicePropertyScopeOutput](https://developer.apple.com/documentation/coreaudio/1580726-anonymous/kaudiodevicepropertyscopeoutput)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyScopeOutput: Int { get } ``` |
| To | ``` var kAudioDevicePropertyScopeOutput: AudioObjectPropertyScope { get } ``` |

Modified [kAudioDevicePropertyScopePlayThrough](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyscopeplaythrough)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyScopePlayThrough: Int { get } ``` |
| To | ``` var kAudioDevicePropertyScopePlayThrough: AudioObjectPropertyScope { get } ``` |

Modified [kAudioDevicePropertySolo](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysolo)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySolo: Int { get } ``` |
| To | ``` var kAudioDevicePropertySolo: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStereoPan](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystereopan)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStereoPan: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStereoPan: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStereoPanChannels](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystereopanchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStereoPanChannels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStereoPanChannels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreamConfiguration](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreamConfiguration: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreamConfiguration: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreamFormat](https://developer.apple.com/documentation/coreaudio/1580731-anonymous/kaudiodevicepropertystreamformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreamFormat: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreamFormat: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreamFormatMatch](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamformatmatch)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreamFormatMatch: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreamFormatMatch: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreamFormats](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamformats)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreamFormats: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreamFormats: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreamFormatSupported](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreamformatsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreamFormatSupported: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreamFormatSupported: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyStreams](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertystreams)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyStreams: Int { get } ``` |
| To | ``` var kAudioDevicePropertyStreams: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubMute](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysubmute)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubMute: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubMute: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysubvolumedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysubvolumedecibelstoscalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeDecibelsToScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeDecibelsToScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/1580715-anonymous/kaudiodevicepropertysubvolumedecibelstoscalartransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeDecibelsToScalarTransferFunction: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeDecibelsToScalarTransferFunction: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeRangeDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertysubvolumerangedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeRangeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeRangeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeScalar](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertysubvolumescalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySubVolumeScalarToDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertysubvolumescalartodecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySubVolumeScalarToDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertySubVolumeScalarToDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertySupportsMixing](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertysupportsmixing)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertySupportsMixing: Int { get } ``` |
| To | ``` var kAudioDevicePropertySupportsMixing: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyTalkback](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertytalkback)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyTalkback: Int { get } ``` |
| To | ``` var kAudioDevicePropertyTalkback: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyTransportType](https://developer.apple.com/documentation/coreaudio/1494454-anonymous/kaudiodevicepropertytransporttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyTransportType: Int { get } ``` |
| To | ``` var kAudioDevicePropertyTransportType: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyUsesVariableBufferFrameSizes](https://developer.apple.com/documentation/coreaudio/1545866-anonymous/kaudiodevicepropertyusesvariablebufferframesizes)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyUsesVariableBufferFrameSizes: Int { get } ``` |
| To | ``` var kAudioDevicePropertyUsesVariableBufferFrameSizes: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyvolumedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyvolumedecibelstoscalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeDecibelsToScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeDecibelsToScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/1580715-anonymous/kaudiodevicepropertyvolumedecibelstoscalartransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeDecibelsToScalarTransferFunction: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeDecibelsToScalarTransferFunction: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeRangeDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyvolumerangedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeRangeDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeRangeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeScalar](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertyvolumescalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeScalar: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDevicePropertyVolumeScalarToDecibels](https://developer.apple.com/documentation/coreaudio/1545881-anonymous/kaudiodevicepropertyvolumescalartodecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDevicePropertyVolumeScalarToDecibels: Int { get } ``` |
| To | ``` var kAudioDevicePropertyVolumeScalarToDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioDeviceStartTimeDontConsultDeviceFlag](https://developer.apple.com/documentation/coreaudio/1545861-anonymous/kaudiodevicestarttimedontconsultdeviceflag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceStartTimeDontConsultDeviceFlag: Int { get } ``` |
| To | ``` var kAudioDeviceStartTimeDontConsultDeviceFlag: UInt32 { get } ``` |

Modified [kAudioDeviceStartTimeDontConsultHALFlag](https://developer.apple.com/documentation/coreaudio/kaudiodevicestarttimedontconsulthalflag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceStartTimeDontConsultHALFlag: Int { get } ``` |
| To | ``` var kAudioDeviceStartTimeDontConsultHALFlag: UInt32 { get } ``` |

Modified [kAudioDeviceStartTimeIsInputFlag](https://developer.apple.com/documentation/coreaudio/kaudiodevicestarttimeisinputflag)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceStartTimeIsInputFlag: Int { get } ``` |
| To | ``` var kAudioDeviceStartTimeIsInputFlag: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeAggregate](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeaggregate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeAggregate: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeAggregate: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeAirPlay](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeairplay)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeAirPlay: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeAirPlay: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeAutoAggregate](https://developer.apple.com/documentation/coreaudio/1580747-anonymous/kaudiodevicetransporttypeautoaggregate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeAutoAggregate: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeAutoAggregate: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeAVB](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypeavb)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeAVB: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeAVB: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeBluetooth](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypebluetooth)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeBluetooth: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeBluetooth: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeBluetoothLE](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypebluetoothle)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeBluetoothLE: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeBluetoothLE: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeBuiltIn](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypebuiltin)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeBuiltIn: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeBuiltIn: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypedisplayport)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeDisplayPort: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeDisplayPort: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeFireWire](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypefirewire)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeFireWire: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeFireWire: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeHDMI](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypehdmi)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeHDMI: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeHDMI: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypePCI](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypepci)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypePCI: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypePCI: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeThunderbolt](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypethunderbolt)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeThunderbolt: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeThunderbolt: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeUnknown](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeUnknown: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeUnknown: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeUSB](https://developer.apple.com/documentation/coreaudio/kaudiodevicetransporttypeusb)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeUSB: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeUSB: UInt32 { get } ``` |

Modified [kAudioDeviceTransportTypeVirtual](https://developer.apple.com/documentation/coreaudio/1494580-anonymous/kaudiodevicetransporttypevirtual)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceTransportTypeVirtual: Int { get } ``` |
| To | ``` var kAudioDeviceTransportTypeVirtual: UInt32 { get } ``` |

Modified [kAudioDeviceUnknown](https://developer.apple.com/documentation/coreaudio/1580746-anonymous/kaudiodeviceunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceUnknown: Int { get } ``` |
| To | ``` var kAudioDeviceUnknown: AudioObjectID { get } ``` |

Modified [kAudioDeviceUnsupportedFormatError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiodeviceunsupportedformaterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioDeviceUnsupportedFormatError: Int { get } ``` |
| To | ``` var kAudioDeviceUnsupportedFormatError: OSStatus { get } ``` |

Modified [kAudioEndPointClassID](https://developer.apple.com/documentation/coreaudio/kaudioendpointclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEndPointClassID: Int { get } ``` |
| To | ``` var kAudioEndPointClassID: AudioClassID { get } ``` |

Modified [kAudioEndPointDeviceClassID](https://developer.apple.com/documentation/coreaudio/kaudioendpointdeviceclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEndPointDeviceClassID: Int { get } ``` |
| To | ``` var kAudioEndPointDeviceClassID: AudioClassID { get } ``` |

Modified [kAudioEndPointDevicePropertyComposition](https://developer.apple.com/documentation/coreaudio/1494430-anonymous/kaudioendpointdevicepropertycomposition)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEndPointDevicePropertyComposition: Int { get } ``` |
| To | ``` var kAudioEndPointDevicePropertyComposition: AudioObjectPropertySelector { get } ``` |

Modified [kAudioEndPointDevicePropertyEndPointList](https://developer.apple.com/documentation/coreaudio/1494430-anonymous/kaudioendpointdevicepropertyendpointlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEndPointDevicePropertyEndPointList: Int { get } ``` |
| To | ``` var kAudioEndPointDevicePropertyEndPointList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioEndPointDevicePropertyIsPrivate](https://developer.apple.com/documentation/coreaudio/1494430-anonymous/kaudioendpointdevicepropertyisprivate)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioEndPointDevicePropertyIsPrivate: Int { get } ``` |
| To | ``` var kAudioEndPointDevicePropertyIsPrivate: AudioObjectPropertySelector { get } ``` |

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

Modified [kAudioHardwareBadDeviceError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwarebaddeviceerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareBadDeviceError: Int { get } ``` |
| To | ``` var kAudioHardwareBadDeviceError: OSStatus { get } ``` |

Modified [kAudioHardwareBadObjectError](https://developer.apple.com/documentation/coreaudio/1494531-anonymous/kaudiohardwarebadobjecterror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareBadObjectError: Int { get } ``` |
| To | ``` var kAudioHardwareBadObjectError: OSStatus { get } ``` |

Modified [kAudioHardwareBadPropertySizeError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarebadpropertysizeerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareBadPropertySizeError: Int { get } ``` |
| To | ``` var kAudioHardwareBadPropertySizeError: OSStatus { get } ``` |

Modified [kAudioHardwareBadStreamError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarebadstreamerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareBadStreamError: Int { get } ``` |
| To | ``` var kAudioHardwareBadStreamError: OSStatus { get } ``` |

Modified [kAudioHardwareIllegalOperationError](https://developer.apple.com/documentation/coreaudio/kaudiohardwareillegaloperationerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareIllegalOperationError: Int { get } ``` |
| To | ``` var kAudioHardwareIllegalOperationError: OSStatus { get } ``` |

Modified [kAudioHardwareNoError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarenoerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareNoError: Int { get } ``` |
| To | ``` var kAudioHardwareNoError: OSStatus { get } ``` |

Modified [kAudioHardwareNotRunningError](https://developer.apple.com/documentation/coreaudio/kaudiohardwarenotrunningerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareNotRunningError: Int { get } ``` |
| To | ``` var kAudioHardwareNotRunningError: OSStatus { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeDecibels: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumedecibelstoscalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeDecibelsToScalar: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeDecibelsToScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumedecibelstoscalartransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeDecibelsToScalarTransferFunction: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeDecibelsToScalarTransferFunction: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeRangeDecibels](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumerangedecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeRangeDecibels: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeRangeDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeScalar](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumescalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeScalar: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBootChimeVolumeScalarToDecibels](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertybootchimevolumescalartodecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBootChimeVolumeScalarToDecibels: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBootChimeVolumeScalarToDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyBoxList](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertyboxlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyBoxList: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyBoxList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyDefaultInputDevice](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertydefaultinputdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyDefaultInputDevice: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyDefaultInputDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyDefaultOutputDevice](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertydefaultoutputdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyDefaultOutputDevice: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyDefaultOutputDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyDefaultSystemOutputDevice](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertydefaultsystemoutputdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyDefaultSystemOutputDevice: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyDefaultSystemOutputDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyDeviceForUID](https://developer.apple.com/documentation/coreaudio/1580723-anonymous/kaudiohardwarepropertydeviceforuid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyDeviceForUID: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyDeviceForUID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyDevices](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertydevices)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyDevices: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyDevices: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyHogModeIsAllowed](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyhogmodeisallowed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyHogModeIsAllowed: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyHogModeIsAllowed: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyIsInitingOrExiting](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertyisinitingorexiting)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyIsInitingOrExiting: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyIsInitingOrExiting: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyMixStereoToMono](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertymixstereotomono)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyMixStereoToMono: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyMixStereoToMono: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyPlugInForBundleID](https://developer.apple.com/documentation/coreaudio/1580723-anonymous/kaudiohardwarepropertypluginforbundleid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyPlugInForBundleID: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyPlugInForBundleID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyPlugInList](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertypluginlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyPlugInList: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyPlugInList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyPowerHint](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertypowerhint)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyPowerHint: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyPowerHint: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyProcessIsAudible](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyprocessisaudible)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyProcessIsAudible: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyProcessIsAudible: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyProcessIsMaster](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertyprocessismaster)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyProcessIsMaster: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyProcessIsMaster: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyRunLoop](https://developer.apple.com/documentation/coreaudio/1580723-anonymous/kaudiohardwarepropertyrunloop)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyRunLoop: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyRunLoop: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyServiceRestarted](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyservicerestarted)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyServiceRestarted: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyServiceRestarted: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertySleepingIsAllowed](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertysleepingisallowed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertySleepingIsAllowed: Int { get } ``` |
| To | ``` var kAudioHardwarePropertySleepingIsAllowed: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyTranslateBundleIDToPlugIn](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertytranslatebundleidtoplugin)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyTranslateBundleIDToPlugIn: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyTranslateBundleIDToPlugIn: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyTranslateBundleIDToTransportManager](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertytranslatebundleidtotransportmanager)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyTranslateBundleIDToTransportManager: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyTranslateBundleIDToTransportManager: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyTranslateUIDToBox](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslateuidtobox)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyTranslateUIDToBox: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyTranslateUIDToBox: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyTranslateUIDToDevice](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertytranslateuidtodevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyTranslateUIDToDevice: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyTranslateUIDToDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyTransportManagerList](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertytransportmanagerlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyTransportManagerList: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyTransportManagerList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyUnloadingIsAllowed](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyunloadingisallowed)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyUnloadingIsAllowed: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyUnloadingIsAllowed: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyUserIDChanged](https://developer.apple.com/documentation/coreaudio/kaudiohardwarepropertyuseridchanged)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyUserIDChanged: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyUserIDChanged: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwarePropertyUserSessionIsActiveOrHeadless](https://developer.apple.com/documentation/coreaudio/1545886-anonymous/kaudiohardwarepropertyusersessionisactiveorheadless)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwarePropertyUserSessionIsActiveOrHeadless: Int { get } ``` |
| To | ``` var kAudioHardwarePropertyUserSessionIsActiveOrHeadless: AudioObjectPropertySelector { get } ``` |

Modified [kAudioHardwareUnknownPropertyError](https://developer.apple.com/documentation/coreaudio/kaudiohardwareunknownpropertyerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareUnknownPropertyError: Int { get } ``` |
| To | ``` var kAudioHardwareUnknownPropertyError: OSStatus { get } ``` |

Modified [kAudioHardwareUnspecifiedError](https://developer.apple.com/documentation/coreaudio/kaudiohardwareunspecifiederror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareUnspecifiedError: Int { get } ``` |
| To | ``` var kAudioHardwareUnspecifiedError: OSStatus { get } ``` |

Modified [kAudioHardwareUnsupportedOperationError](https://developer.apple.com/documentation/coreaudio/kaudiohardwareunsupportedoperationerror)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHardwareUnsupportedOperationError: Int { get } ``` |
| To | ``` var kAudioHardwareUnsupportedOperationError: OSStatus { get } ``` |

Modified [kAudioHighPassFilterControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiohighpassfiltercontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioHighPassFilterControlClassID: Int { get } ``` |
| To | ``` var kAudioHighPassFilterControlClassID: AudioClassID { get } ``` |

Modified [kAudioISubOwnerControlClassID](https://developer.apple.com/documentation/coreaudio/1580720-anonymous/kaudioisubownercontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioISubOwnerControlClassID: Int { get } ``` |
| To | ``` var kAudioISubOwnerControlClassID: AudioClassID { get } ``` |

Modified [kAudioJackControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiojackcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioJackControlClassID: Int { get } ``` |
| To | ``` var kAudioJackControlClassID: AudioClassID { get } ``` |

Modified [kAudioLevelControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlClassID: Int { get } ``` |
| To | ``` var kAudioLevelControlClassID: AudioClassID { get } ``` |

Modified [kAudioLevelControlPropertyConvertDecibelsToScalar](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertyconvertdecibelstoscalar)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyConvertDecibelsToScalar: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyConvertDecibelsToScalar: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLevelControlPropertyConvertScalarToDecibels](https://developer.apple.com/documentation/coreaudio/kaudiolevelcontrolpropertyconvertscalartodecibels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyConvertScalarToDecibels: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyConvertScalarToDecibels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLevelControlPropertyDecibelRange](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertydecibelrange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyDecibelRange: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyDecibelRange: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLevelControlPropertyDecibelsToScalarTransferFunction](https://developer.apple.com/documentation/coreaudio/1580728-anonymous/kaudiolevelcontrolpropertydecibelstoscalartransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyDecibelsToScalarTransferFunction: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyDecibelsToScalarTransferFunction: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLevelControlPropertyDecibelValue](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertydecibelvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyDecibelValue: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyDecibelValue: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLevelControlPropertyScalarValue](https://developer.apple.com/documentation/coreaudio/1494536-anonymous/kaudiolevelcontrolpropertyscalarvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLevelControlPropertyScalarValue: Int { get } ``` |
| To | ``` var kAudioLevelControlPropertyScalarValue: AudioObjectPropertySelector { get } ``` |

Modified [kAudioLFEMuteControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiolfemutecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLFEMuteControlClassID: Int { get } ``` |
| To | ``` var kAudioLFEMuteControlClassID: AudioClassID { get } ``` |

Modified [kAudioLFEVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/1494503-anonymous/kaudiolfevolumecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLFEVolumeControlClassID: Int { get } ``` |
| To | ``` var kAudioLFEVolumeControlClassID: AudioClassID { get } ``` |

Modified [kAudioLineLevelControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiolinelevelcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioLineLevelControlClassID: Int { get } ``` |
| To | ``` var kAudioLineLevelControlClassID: AudioClassID { get } ``` |

Modified [kAudioListenbackControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiolistenbackcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioListenbackControlClassID: Int { get } ``` |
| To | ``` var kAudioListenbackControlClassID: AudioClassID { get } ``` |

Modified [kAudioMuteControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiomutecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioMuteControlClassID: Int { get } ``` |
| To | ``` var kAudioMuteControlClassID: AudioClassID { get } ``` |

Modified [kAudioObjectClassID](https://developer.apple.com/documentation/coreaudio/1494439-anonymous/kaudioobjectclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectClassID: Int { get } ``` |
| To | ``` var kAudioObjectClassID: AudioClassID { get } ``` |

Modified [kAudioObjectClassIDWildcard](https://developer.apple.com/documentation/coreaudio/kaudioobjectclassidwildcard)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectClassIDWildcard: UInt32 { get } ``` |
| To | ``` var kAudioObjectClassIDWildcard: AudioClassID { get } ``` |

Modified [kAudioObjectPropertyBaseClass](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertybaseclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyBaseClass: Int { get } ``` |
| To | ``` var kAudioObjectPropertyBaseClass: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyClass](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyclass)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyClass: Int { get } ``` |
| To | ``` var kAudioObjectPropertyClass: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyControlList](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertycontrollist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyControlList: Int { get } ``` |
| To | ``` var kAudioObjectPropertyControlList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyCreator](https://developer.apple.com/documentation/coreaudio/1545874-anonymous/kaudioobjectpropertycreator)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyCreator: Int { get } ``` |
| To | ``` var kAudioObjectPropertyCreator: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyElementCategoryName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyelementcategoryname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyElementCategoryName: Int { get } ``` |
| To | ``` var kAudioObjectPropertyElementCategoryName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyElementMaster](https://developer.apple.com/documentation/coreaudio/1494464-anonymous/kaudioobjectpropertyelementmaster)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyElementMaster: Int { get } ``` |
| To | ``` var kAudioObjectPropertyElementMaster: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertyElementName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyelementname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyElementName: Int { get } ``` |
| To | ``` var kAudioObjectPropertyElementName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyElementNumberName](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyelementnumbername)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyElementNumberName: Int { get } ``` |
| To | ``` var kAudioObjectPropertyElementNumberName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyElementWildcard](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyelementwildcard)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyElementWildcard: UInt32 { get } ``` |
| To | ``` var kAudioObjectPropertyElementWildcard: AudioObjectPropertyElement { get } ``` |

Modified [kAudioObjectPropertyFirmwareVersion](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyfirmwareversion)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyFirmwareVersion: Int { get } ``` |
| To | ``` var kAudioObjectPropertyFirmwareVersion: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyIdentify](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyidentify)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyIdentify: Int { get } ``` |
| To | ``` var kAudioObjectPropertyIdentify: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyListenerAdded](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertylisteneradded)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyListenerAdded: Int { get } ``` |
| To | ``` var kAudioObjectPropertyListenerAdded: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyListenerRemoved](https://developer.apple.com/documentation/coreaudio/1545874-anonymous/kaudioobjectpropertylistenerremoved)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyListenerRemoved: Int { get } ``` |
| To | ``` var kAudioObjectPropertyListenerRemoved: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyManufacturer](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertymanufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyManufacturer: Int { get } ``` |
| To | ``` var kAudioObjectPropertyManufacturer: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyModelName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertymodelname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyModelName: Int { get } ``` |
| To | ``` var kAudioObjectPropertyModelName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyName](https://developer.apple.com/documentation/coreaudio/1494449-anonymous/kaudioobjectpropertyname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyName: Int { get } ``` |
| To | ``` var kAudioObjectPropertyName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyOwnedObjects](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyownedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyOwnedObjects: Int { get } ``` |
| To | ``` var kAudioObjectPropertyOwnedObjects: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyOwner](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyowner)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyOwner: Int { get } ``` |
| To | ``` var kAudioObjectPropertyOwner: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertyScopeGlobal](https://developer.apple.com/documentation/coreaudio/1494464-anonymous/kaudioobjectpropertyscopeglobal)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyScopeGlobal: Int { get } ``` |
| To | ``` var kAudioObjectPropertyScopeGlobal: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertyScopeInput](https://developer.apple.com/documentation/coreaudio/1494464-anonymous/kaudioobjectpropertyscopeinput)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyScopeInput: Int { get } ``` |
| To | ``` var kAudioObjectPropertyScopeInput: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertyScopeOutput](https://developer.apple.com/documentation/coreaudio/1494464-anonymous/kaudioobjectpropertyscopeoutput)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyScopeOutput: Int { get } ``` |
| To | ``` var kAudioObjectPropertyScopeOutput: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertyScopePlayThrough](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopeplaythrough)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyScopePlayThrough: Int { get } ``` |
| To | ``` var kAudioObjectPropertyScopePlayThrough: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertyScopeWildcard](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyscopewildcard)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertyScopeWildcard: UInt32 { get } ``` |
| To | ``` var kAudioObjectPropertyScopeWildcard: AudioObjectPropertyScope { get } ``` |

Modified [kAudioObjectPropertySelectorWildcard](https://developer.apple.com/documentation/coreaudio/1494591-anonymous/kaudioobjectpropertyselectorwildcard)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertySelectorWildcard: UInt32 { get } ``` |
| To | ``` var kAudioObjectPropertySelectorWildcard: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectPropertySerialNumber](https://developer.apple.com/documentation/coreaudio/kaudioobjectpropertyserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectPropertySerialNumber: Int { get } ``` |
| To | ``` var kAudioObjectPropertySerialNumber: AudioObjectPropertySelector { get } ``` |

Modified [kAudioObjectSystemObject](https://developer.apple.com/documentation/coreaudio/kaudioobjectsystemobject)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectSystemObject: Int { get } ``` |
| To | ``` var kAudioObjectSystemObject: Int32 { get } ``` |

Modified [kAudioObjectUnknown](https://developer.apple.com/documentation/coreaudio/kaudioobjectunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioObjectUnknown: Int { get } ``` |
| To | ``` var kAudioObjectUnknown: AudioObjectID { get } ``` |

Modified [kAudioPhantomPowerControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophantompowercontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPhantomPowerControlClassID: Int { get } ``` |
| To | ``` var kAudioPhantomPowerControlClassID: AudioClassID { get } ``` |

Modified [kAudioPhaseInvertControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiophaseinvertcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPhaseInvertControlClassID: Int { get } ``` |
| To | ``` var kAudioPhaseInvertControlClassID: AudioClassID { get } ``` |

Modified [kAudioPlugInClassID](https://developer.apple.com/documentation/coreaudio/kaudiopluginclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInClassID: Int { get } ``` |
| To | ``` var kAudioPlugInClassID: AudioClassID { get } ``` |

Modified [kAudioPlugInCreateAggregateDevice](https://developer.apple.com/documentation/coreaudio/kaudioplugincreateaggregatedevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInCreateAggregateDevice: Int { get } ``` |
| To | ``` var kAudioPlugInCreateAggregateDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInDestroyAggregateDevice](https://developer.apple.com/documentation/coreaudio/kaudioplugindestroyaggregatedevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInDestroyAggregateDevice: Int { get } ``` |
| To | ``` var kAudioPlugInDestroyAggregateDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInPropertyBoxList](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertyboxlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInPropertyBoxList: Int { get } ``` |
| To | ``` var kAudioPlugInPropertyBoxList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInPropertyBundleID](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertybundleid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInPropertyBundleID: Int { get } ``` |
| To | ``` var kAudioPlugInPropertyBundleID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInPropertyDeviceList](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertydevicelist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInPropertyDeviceList: Int { get } ``` |
| To | ``` var kAudioPlugInPropertyDeviceList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInPropertyTranslateUIDToBox](https://developer.apple.com/documentation/coreaudio/1494489-anonymous/kaudiopluginpropertytranslateuidtobox)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInPropertyTranslateUIDToBox: Int { get } ``` |
| To | ``` var kAudioPlugInPropertyTranslateUIDToBox: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPlugInPropertyTranslateUIDToDevice](https://developer.apple.com/documentation/coreaudio/kaudiopluginpropertytranslateuidtodevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPlugInPropertyTranslateUIDToDevice: Int { get } ``` |
| To | ``` var kAudioPlugInPropertyTranslateUIDToDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPropertyWildcardChannel](https://developer.apple.com/documentation/coreaudio/1580740-anonymous/kaudiopropertywildcardchannel)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPropertyWildcardChannel: UInt32 { get } ``` |
| To | ``` var kAudioPropertyWildcardChannel: AudioObjectPropertyElement { get } ``` |

Modified [kAudioPropertyWildcardPropertyID](https://developer.apple.com/documentation/coreaudio/1580722-anonymous/kaudiopropertywildcardpropertyid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPropertyWildcardPropertyID: UInt32 { get } ``` |
| To | ``` var kAudioPropertyWildcardPropertyID: AudioObjectPropertySelector { get } ``` |

Modified [kAudioPropertyWildcardSection](https://developer.apple.com/documentation/coreaudio/1580737-anonymous/kaudiopropertywildcardsection)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioPropertyWildcardSection: UInt32 { get } ``` |
| To | ``` var kAudioPropertyWildcardSection: UInt8 { get } ``` |

Modified [kAudioSelectorControlClassID](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlClassID: Int { get } ``` |
| To | ``` var kAudioSelectorControlClassID: AudioClassID { get } ``` |

Modified [kAudioSelectorControlItemKindSpacer](https://developer.apple.com/documentation/coreaudio/1494470-anonymous/kaudioselectorcontrolitemkindspacer)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlItemKindSpacer: Int { get } ``` |
| To | ``` var kAudioSelectorControlItemKindSpacer: UInt32 { get } ``` |

Modified [kAudioSelectorControlPropertyAvailableItems](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertyavailableitems)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlPropertyAvailableItems: Int { get } ``` |
| To | ``` var kAudioSelectorControlPropertyAvailableItems: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSelectorControlPropertyCurrentItem](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertycurrentitem)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlPropertyCurrentItem: Int { get } ``` |
| To | ``` var kAudioSelectorControlPropertyCurrentItem: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSelectorControlPropertyItemKind](https://developer.apple.com/documentation/coreaudio/kaudioselectorcontrolpropertyitemkind)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlPropertyItemKind: Int { get } ``` |
| To | ``` var kAudioSelectorControlPropertyItemKind: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSelectorControlPropertyItemName](https://developer.apple.com/documentation/coreaudio/1494594-anonymous/kaudioselectorcontrolpropertyitemname)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSelectorControlPropertyItemName: Int { get } ``` |
| To | ``` var kAudioSelectorControlPropertyItemName: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSliderControlClassID](https://developer.apple.com/documentation/coreaudio/1494533-anonymous/kaudioslidercontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSliderControlClassID: Int { get } ``` |
| To | ``` var kAudioSliderControlClassID: AudioClassID { get } ``` |

Modified [kAudioSliderControlPropertyRange](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyrange)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSliderControlPropertyRange: Int { get } ``` |
| To | ``` var kAudioSliderControlPropertyRange: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSliderControlPropertyValue](https://developer.apple.com/documentation/coreaudio/1494510-anonymous/kaudioslidercontrolpropertyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSliderControlPropertyValue: Int { get } ``` |
| To | ``` var kAudioSliderControlPropertyValue: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSoloControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiosolocontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSoloControlClassID: Int { get } ``` |
| To | ``` var kAudioSoloControlClassID: AudioClassID { get } ``` |

Modified [kAudioStereoPanControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiostereopancontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStereoPanControlClassID: Int { get } ``` |
| To | ``` var kAudioStereoPanControlClassID: AudioClassID { get } ``` |

Modified [kAudioStereoPanControlPropertyPanningChannels](https://developer.apple.com/documentation/coreaudio/1494557-anonymous/kaudiostereopancontrolpropertypanningchannels)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStereoPanControlPropertyPanningChannels: Int { get } ``` |
| To | ``` var kAudioStereoPanControlPropertyPanningChannels: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStereoPanControlPropertyValue](https://developer.apple.com/documentation/coreaudio/1494557-anonymous/kaudiostereopancontrolpropertyvalue)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStereoPanControlPropertyValue: Int { get } ``` |
| To | ``` var kAudioStereoPanControlPropertyValue: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamAnyRate](https://developer.apple.com/documentation/coreaudio/kaudiostreamanyrate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var kAudioStreamAnyRate: Int { get } ``` | OS X 10.10 |
| To | ``` let kAudioStreamAnyRate: Float64 ``` | OS X 10.11 |

Modified [kAudioStreamClassID](https://developer.apple.com/documentation/coreaudio/1494573-anonymous/kaudiostreamclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamClassID: Int { get } ``` |
| To | ``` var kAudioStreamClassID: AudioClassID { get } ``` |

Modified [kAudioStreamPropertyAvailablePhysicalFormats](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyavailablephysicalformats)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyAvailablePhysicalFormats: Int { get } ``` |
| To | ``` var kAudioStreamPropertyAvailablePhysicalFormats: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyAvailableVirtualFormats](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyavailablevirtualformats)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyAvailableVirtualFormats: Int { get } ``` |
| To | ``` var kAudioStreamPropertyAvailableVirtualFormats: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyDirection](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertydirection)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyDirection: Int { get } ``` |
| To | ``` var kAudioStreamPropertyDirection: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyIsActive](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyisactive)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyIsActive: Int { get } ``` |
| To | ``` var kAudioStreamPropertyIsActive: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyLatency](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertylatency)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyLatency: Int { get } ``` |
| To | ``` var kAudioStreamPropertyLatency: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyOwningDevice](https://developer.apple.com/documentation/coreaudio/1580748-anonymous/kaudiostreampropertyowningdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyOwningDevice: Int { get } ``` |
| To | ``` var kAudioStreamPropertyOwningDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyPhysicalFormat](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyphysicalformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyPhysicalFormat: Int { get } ``` |
| To | ``` var kAudioStreamPropertyPhysicalFormat: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyPhysicalFormatMatch](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyphysicalformatmatch)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyPhysicalFormatMatch: Int { get } ``` |
| To | ``` var kAudioStreamPropertyPhysicalFormatMatch: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyPhysicalFormats](https://developer.apple.com/documentation/coreaudio/1580748-anonymous/kaudiostreampropertyphysicalformats)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyPhysicalFormats: Int { get } ``` |
| To | ``` var kAudioStreamPropertyPhysicalFormats: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyPhysicalFormatSupported](https://developer.apple.com/documentation/coreaudio/1580748-anonymous/kaudiostreampropertyphysicalformatsupported)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyPhysicalFormatSupported: Int { get } ``` |
| To | ``` var kAudioStreamPropertyPhysicalFormatSupported: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyStartingChannel](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertystartingchannel)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyStartingChannel: Int { get } ``` |
| To | ``` var kAudioStreamPropertyStartingChannel: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyTerminalType](https://developer.apple.com/documentation/coreaudio/kaudiostreampropertyterminaltype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyTerminalType: Int { get } ``` |
| To | ``` var kAudioStreamPropertyTerminalType: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamPropertyVirtualFormat](https://developer.apple.com/documentation/coreaudio/1494541-anonymous/kaudiostreampropertyvirtualformat)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamPropertyVirtualFormat: Int { get } ``` |
| To | ``` var kAudioStreamPropertyVirtualFormat: AudioObjectPropertySelector { get } ``` |

Modified [kAudioStreamTerminalTypeDigitalAudioInterface](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypedigitalaudiointerface)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeDigitalAudioInterface: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeDigitalAudioInterface: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeDisplayPort](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypedisplayport)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeDisplayPort: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeDisplayPort: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeHDMI](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypehdmi)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeHDMI: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeHDMI: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeHeadphones](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypeheadphones)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeHeadphones: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeHeadphones: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeHeadsetMicrophone](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypeheadsetmicrophone)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeHeadsetMicrophone: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeHeadsetMicrophone: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeLFESpeaker](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypelfespeaker)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeLFESpeaker: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeLFESpeaker: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeLine](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypeline)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeLine: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeLine: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeMicrophone](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypemicrophone)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeMicrophone: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeMicrophone: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeReceiverMicrophone](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypereceivermicrophone)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeReceiverMicrophone: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeReceiverMicrophone: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeReceiverSpeaker](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypereceiverspeaker)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeReceiverSpeaker: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeReceiverSpeaker: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeSpeaker](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypespeaker)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeSpeaker: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeSpeaker: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeTTY](https://developer.apple.com/documentation/coreaudio/kaudiostreamterminaltypetty)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeTTY: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeTTY: UInt32 { get } ``` |

Modified [kAudioStreamTerminalTypeUnknown](https://developer.apple.com/documentation/coreaudio/1494543-anonymous/kaudiostreamterminaltypeunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamTerminalTypeUnknown: Int { get } ``` |
| To | ``` var kAudioStreamTerminalTypeUnknown: UInt32 { get } ``` |

Modified [kAudioStreamUnknown](https://developer.apple.com/documentation/coreaudio/kaudiostreamunknown)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioStreamUnknown: Int { get } ``` |
| To | ``` var kAudioStreamUnknown: AudioObjectID { get } ``` |

Modified [kAudioSubDeviceClassID](https://developer.apple.com/documentation/coreaudio/kaudiosubdeviceclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceClassID: Int { get } ``` |
| To | ``` var kAudioSubDeviceClassID: AudioClassID { get } ``` |

Modified [kAudioSubDeviceDriftCompensationHighQuality](https://developer.apple.com/documentation/coreaudio/1545878-anonymous/kaudiosubdevicedriftcompensationhighquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceDriftCompensationHighQuality: Int { get } ``` |
| To | ``` var kAudioSubDeviceDriftCompensationHighQuality: UInt32 { get } ``` |

Modified [kAudioSubDeviceDriftCompensationLowQuality](https://developer.apple.com/documentation/coreaudio/1545878-anonymous/kaudiosubdevicedriftcompensationlowquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceDriftCompensationLowQuality: Int { get } ``` |
| To | ``` var kAudioSubDeviceDriftCompensationLowQuality: UInt32 { get } ``` |

Modified [kAudioSubDeviceDriftCompensationMaxQuality](https://developer.apple.com/documentation/coreaudio/1545878-anonymous/kaudiosubdevicedriftcompensationmaxquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceDriftCompensationMaxQuality: Int { get } ``` |
| To | ``` var kAudioSubDeviceDriftCompensationMaxQuality: UInt32 { get } ``` |

Modified [kAudioSubDeviceDriftCompensationMediumQuality](https://developer.apple.com/documentation/coreaudio/1545878-anonymous/kaudiosubdevicedriftcompensationmediumquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceDriftCompensationMediumQuality: Int { get } ``` |
| To | ``` var kAudioSubDeviceDriftCompensationMediumQuality: UInt32 { get } ``` |

Modified [kAudioSubDeviceDriftCompensationMinQuality](https://developer.apple.com/documentation/coreaudio/kaudiosubdevicedriftcompensationminquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDeviceDriftCompensationMinQuality: Int { get } ``` |
| To | ``` var kAudioSubDeviceDriftCompensationMinQuality: UInt32 { get } ``` |

Modified [kAudioSubDevicePropertyDriftCompensation](https://developer.apple.com/documentation/coreaudio/1545880-anonymous/kaudiosubdevicepropertydriftcompensation)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDevicePropertyDriftCompensation: Int { get } ``` |
| To | ``` var kAudioSubDevicePropertyDriftCompensation: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSubDevicePropertyDriftCompensationQuality](https://developer.apple.com/documentation/coreaudio/1545880-anonymous/kaudiosubdevicepropertydriftcompensationquality)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDevicePropertyDriftCompensationQuality: Int { get } ``` |
| To | ``` var kAudioSubDevicePropertyDriftCompensationQuality: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSubDevicePropertyExtraLatency](https://developer.apple.com/documentation/coreaudio/1545880-anonymous/kaudiosubdevicepropertyextralatency)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSubDevicePropertyExtraLatency: Int { get } ``` |
| To | ``` var kAudioSubDevicePropertyExtraLatency: AudioObjectPropertySelector { get } ``` |

Modified [kAudioSystemObjectClassID](https://developer.apple.com/documentation/coreaudio/kaudiosystemobjectclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioSystemObjectClassID: Int { get } ``` |
| To | ``` var kAudioSystemObjectClassID: AudioClassID { get } ``` |

Modified [kAudioTalkbackControlClassID](https://developer.apple.com/documentation/coreaudio/1494512-anonymous/kaudiotalkbackcontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTalkbackControlClassID: Int { get } ``` |
| To | ``` var kAudioTalkbackControlClassID: AudioClassID { get } ``` |

Modified [kAudioTransportManagerClassID](https://developer.apple.com/documentation/coreaudio/1494472-anonymous/kaudiotransportmanagerclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerClassID: Int { get } ``` |
| To | ``` var kAudioTransportManagerClassID: AudioClassID { get } ``` |

Modified [kAudioTransportManagerCreateEndPointDevice](https://developer.apple.com/documentation/coreaudio/kaudiotransportmanagercreateendpointdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerCreateEndPointDevice: Int { get } ``` |
| To | ``` var kAudioTransportManagerCreateEndPointDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioTransportManagerDestroyEndPointDevice](https://developer.apple.com/documentation/coreaudio/1545857-anonymous/kaudiotransportmanagerdestroyendpointdevice)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerDestroyEndPointDevice: Int { get } ``` |
| To | ``` var kAudioTransportManagerDestroyEndPointDevice: AudioObjectPropertySelector { get } ``` |

Modified [kAudioTransportManagerPropertyEndPointList](https://developer.apple.com/documentation/coreaudio/1494466-anonymous/kaudiotransportmanagerpropertyendpointlist)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerPropertyEndPointList: Int { get } ``` |
| To | ``` var kAudioTransportManagerPropertyEndPointList: AudioObjectPropertySelector { get } ``` |

Modified [kAudioTransportManagerPropertyTranslateUIDToEndPoint](https://developer.apple.com/documentation/coreaudio/1494466-anonymous/kaudiotransportmanagerpropertytranslateuidtoendpoint)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerPropertyTranslateUIDToEndPoint: Int { get } ``` |
| To | ``` var kAudioTransportManagerPropertyTranslateUIDToEndPoint: AudioObjectPropertySelector { get } ``` |

Modified [kAudioTransportManagerPropertyTransportType](https://developer.apple.com/documentation/coreaudio/kaudiotransportmanagerpropertytransporttype)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioTransportManagerPropertyTransportType: Int { get } ``` |
| To | ``` var kAudioTransportManagerPropertyTransportType: AudioObjectPropertySelector { get } ``` |

Modified [kAudioVolumeControlClassID](https://developer.apple.com/documentation/coreaudio/kaudiovolumecontrolclassid)

|  | Declaration |
| --- | --- |
| From | ``` var kAudioVolumeControlClassID: Int { get } ``` |
| To | ``` var kAudioVolumeControlClassID: AudioClassID { get } ``` |

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
