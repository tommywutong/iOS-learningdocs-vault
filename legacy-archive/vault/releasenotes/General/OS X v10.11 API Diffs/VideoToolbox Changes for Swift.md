---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/VideoToolbox.html
archived_at: '2026-07-18T02:53:47.340227Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# VideoToolbox Changes for Swift

### VideoToolbox

Removed VTCompressionSessionOptionFlags.init(_: UInt32)Removed VTDecompressionOutputCallbackRecord.init(decompressionOutputCallback: VTDecompressionOutputCallback, decompressionOutputRefCon: UnsafeMutablePointer<Void>)Removed kVTDecodeFrame_1xRealTimePlaybackRemoved kVTDecodeFrame_DoNotOutputFrameRemoved kVTDecodeFrame_EnableAsynchronousDecompressionRemoved kVTDecodeFrame_EnableTemporalProcessingRemoved kVTDecodeInfo_AsynchronousRemoved kVTDecodeInfo_FrameDroppedRemoved kVTDecodeInfo_ImageBufferModifiableRemoved kVTEncodeInfo_AsynchronousRemoved kVTEncodeInfo_FrameDroppedRemoved VTDecodeFrameFlagsRemoved VTDecodeInfoFlagsRemoved VTEncodeInfoFlagsAdded [VTDecodeFrameFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags)Added VTDecodeFrameFlags.init(rawValue: UInt32)Added [VTDecodeInfoFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags)Added [VTDecodeInfoFlags.Asynchronous](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/kvtdecodeinfo_asynchronous)Added [VTDecodeInfoFlags.FrameDropped](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/1490385-framedropped)Added [VTDecodeInfoFlags.ImageBufferModifiable](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/1490384-imagebuffermodifiable)Added VTDecodeInfoFlags.init(rawValue: UInt32)Added VTDecompressionOutputCallbackRecord.init(decompressionOutputCallback: VTDecompressionOutputCallback?, decompressionOutputRefCon: UnsafeMutablePointer<Void>)Added [VTEncodeInfoFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags)Added [VTEncodeInfoFlags.Asynchronous](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags/1490349-asynchronous)Added [VTEncodeInfoFlags.FrameDropped](https://developer.apple.com/documentation/videotoolbox/vtencodeinfoflags/1490388-framedropped)Added VTEncodeInfoFlags.init(rawValue: UInt32)Added [VTCompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputhandler)Added [VTCompressionSessionEncodeFrameWithOutputHandler(_: VTCompressionSession, _: CVImageBuffer, _: CMTime, _: CMTime, _: CFDictionary?, _: UnsafeMutablePointer<VTEncodeInfoFlags>, _: VTCompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428281-vtcompressionsessionencodeframew)Added [VTCreateCGImageFromCVPixelBuffer(_: CVPixelBuffer, _: CFDictionary?, _: UnsafeMutablePointer<CGImage?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536089-vtcreatecgimagefromcvpixelbuffer)Added [VTDecompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputhandler)Added [VTDecompressionSessionDecodeFrameWithOutputHandler(_: VTDecompressionSession, _: CMSampleBuffer, _: VTDecodeFrameFlags, _: UnsafeMutablePointer<VTDecodeInfoFlags>, _: VTDecompressionOutputHandler) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536067-vtdecompressionsessiondecodefram)Added [VTRegisterProfessionalVideoWorkflowVideoDecoders()](https://developer.apple.com/documentation/videotoolbox/1437860-vtregisterprofessionalvideoworkf)Added [VTRegisterProfessionalVideoWorkflowVideoEncoders()](https://developer.apple.com/documentation/videotoolbox/1437858-vtregisterprofessionalvideoworkf)Modified [VTCompressionSessionOptionFlags [struct]](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VTCompressionSessionOptionFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` | RawOptionSetType |
| To | ``` struct VTCompressionSessionOptionFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var BeginFinalPass: VTCompressionSessionOptionFlags { get } } ``` | OptionSetType |

Modified [VTDecompressionOutputCallbackRecord [struct]](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord)

|  | Declaration |
| --- | --- |
| From | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VTDecompressionOutputCallback     var decompressionOutputRefCon: UnsafeMutablePointer<Void>     init()     init(decompressionOutputCallback decompressionOutputCallback: VTDecompressionOutputCallback, decompressionOutputRefCon decompressionOutputRefCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct VTDecompressionOutputCallbackRecord {     var decompressionOutputCallback: VTDecompressionOutputCallback?     var decompressionOutputRefCon: UnsafeMutablePointer<Void>     init()     init(decompressionOutputCallback decompressionOutputCallback: VTDecompressionOutputCallback?, decompressionOutputRefCon decompressionOutputRefCon: UnsafeMutablePointer<Void>) } ``` |

Modified [VTDecompressionOutputCallbackRecord.decompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord/1536141-decompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` var decompressionOutputCallback: VTDecompressionOutputCallback ``` |
| To | ``` var decompressionOutputCallback: VTDecompressionOutputCallback? ``` |

Modified [kVTAllocationFailedErr](https://developer.apple.com/documentation/videotoolbox/kvtallocationfailederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTAllocationFailedErr: Int { get } ``` |
| To | ``` var kVTAllocationFailedErr: OSStatus { get } ``` |

Modified [kVTColorCorrectionPixelTransferFailedErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcolorcorrectionpixeltransferfailederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTColorCorrectionPixelTransferFailedErr: Int { get } ``` |
| To | ``` var kVTColorCorrectionPixelTransferFailedErr: OSStatus { get } ``` |

Modified [kVTColorSyncTransformConvertFailedErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcolorsynctransformconvertfailederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTColorSyncTransformConvertFailedErr: Int { get } ``` |
| To | ``` var kVTColorSyncTransformConvertFailedErr: OSStatus { get } ``` |

Modified [kVTCompressionPropertyKey_AllowFrameReordering](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_allowframereordering)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_AllowFrameReordering: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_AllowFrameReordering: CFString ``` |

Modified [kVTCompressionPropertyKey_AllowTemporalCompression](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_allowtemporalcompression)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_AllowTemporalCompression: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_AllowTemporalCompression: CFString ``` |

Modified [kVTCompressionPropertyKey_AspectRatio16x9](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_aspectratio16x9)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_AspectRatio16x9: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_AspectRatio16x9: CFString ``` |

Modified [kVTCompressionPropertyKey_AverageBitRate](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_averagebitrate)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_AverageBitRate: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_AverageBitRate: CFString ``` |

Modified [kVTCompressionPropertyKey_CleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_cleanaperture)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_CleanAperture: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_CleanAperture: CFString ``` |

Modified [kVTCompressionPropertyKey_ColorPrimaries](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_colorprimaries)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ColorPrimaries: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ColorPrimaries: CFString ``` |

Modified [kVTCompressionPropertyKey_DataRateLimits](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_dataratelimits)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_DataRateLimits: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_DataRateLimits: CFString ``` |

Modified [kVTCompressionPropertyKey_Depth](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_depth)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_Depth: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_Depth: CFString ``` |

Modified [kVTCompressionPropertyKey_ExpectedDuration](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_expectedduration)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ExpectedDuration: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ExpectedDuration: CFString ``` |

Modified [kVTCompressionPropertyKey_ExpectedFrameRate](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_expectedframerate)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ExpectedFrameRate: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ExpectedFrameRate: CFString ``` |

Modified [kVTCompressionPropertyKey_FieldCount](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_fieldcount)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_FieldCount: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_FieldCount: CFString ``` |

Modified [kVTCompressionPropertyKey_FieldDetail](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_fielddetail)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_FieldDetail: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_FieldDetail: CFString ``` |

Modified [kVTCompressionPropertyKey_H264EntropyMode](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_h264entropymode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_H264EntropyMode: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_H264EntropyMode: CFString ``` |

Modified [kVTCompressionPropertyKey_ICCProfile](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_iccprofile)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ICCProfile: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ICCProfile: CFString ``` |

Modified [kVTCompressionPropertyKey_MaxFrameDelayCount](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxframedelaycount)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MaxFrameDelayCount: CFString ``` |

Modified [kVTCompressionPropertyKey_MaxH264SliceBytes](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxh264slicebytes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MaxH264SliceBytes: CFString ``` |

Modified [kVTCompressionPropertyKey_MaxKeyFrameInterval](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxkeyframeinterval)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MaxKeyFrameInterval: CFString ``` |

Modified [kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_maxkeyframeintervalduration)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MaxKeyFrameIntervalDuration: CFString ``` |

Modified [kVTCompressionPropertyKey_MoreFramesAfterEnd](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_moreframesafterend)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MoreFramesAfterEnd: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MoreFramesAfterEnd: CFString ``` |

Modified [kVTCompressionPropertyKey_MoreFramesBeforeStart](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_moreframesbeforestart)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MoreFramesBeforeStart: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MoreFramesBeforeStart: CFString ``` |

Modified [kVTCompressionPropertyKey_MultiPassStorage](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_multipassstorage)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_MultiPassStorage: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_MultiPassStorage: CFString ``` |

Modified [kVTCompressionPropertyKey_NumberOfPendingFrames](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_numberofpendingframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_NumberOfPendingFrames: CFString ``` |

Modified [kVTCompressionPropertyKey_PixelAspectRatio](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_pixelaspectratio)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_PixelAspectRatio: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_PixelAspectRatio: CFString ``` |

Modified [kVTCompressionPropertyKey_PixelBufferPoolIsShared](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_pixelbufferpoolisshared)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_PixelBufferPoolIsShared: CFString ``` |

Modified [kVTCompressionPropertyKey_PixelTransferProperties](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_pixeltransferproperties)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_PixelTransferProperties: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_PixelTransferProperties: CFString ``` |

Modified [kVTCompressionPropertyKey_ProfileLevel](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_profilelevel)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ProfileLevel: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ProfileLevel: CFString ``` |

Modified [kVTCompressionPropertyKey_ProgressiveScan](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_progressivescan)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_ProgressiveScan: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_ProgressiveScan: CFString ``` |

Modified [kVTCompressionPropertyKey_Quality](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_quality)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_Quality: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_Quality: CFString ``` |

Modified [kVTCompressionPropertyKey_RealTime](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_realtime)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_RealTime: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_RealTime: CFString ``` |

Modified [kVTCompressionPropertyKey_SourceFrameCount](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_sourceframecount)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_SourceFrameCount: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_SourceFrameCount: CFString ``` |

Modified [kVTCompressionPropertyKey_TransferFunction](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_transferfunction)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_TransferFunction: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_TransferFunction: CFString ``` |

Modified [kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_usinghardwareacceleratedvideoencoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_UsingHardwareAcceleratedVideoEncoder: CFString ``` |

Modified [kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_videoencoderpixelbufferattributes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_VideoEncoderPixelBufferAttributes: CFString ``` |

Modified [kVTCompressionPropertyKey_YCbCrMatrix](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_ycbcrmatrix)

|  | Declaration |
| --- | --- |
| From | ``` let kVTCompressionPropertyKey_YCbCrMatrix: CFString! ``` |
| To | ``` let kVTCompressionPropertyKey_YCbCrMatrix: CFString ``` |

Modified [kVTCouldNotCreateColorCorrectionDataErr](https://developer.apple.com/documentation/videotoolbox/kvtcouldnotcreatecolorcorrectiondataerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTCouldNotCreateColorCorrectionDataErr: Int { get } ``` |
| To | ``` var kVTCouldNotCreateColorCorrectionDataErr: OSStatus { get } ``` |

Modified [kVTCouldNotCreateInstanceErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcouldnotcreateinstanceerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTCouldNotCreateInstanceErr: Int { get } ``` |
| To | ``` var kVTCouldNotCreateInstanceErr: OSStatus { get } ``` |

Modified [kVTCouldNotFindTemporalFilterErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcouldnotfindtemporalfiltererr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTCouldNotFindTemporalFilterErr: Int { get } ``` |
| To | ``` var kVTCouldNotFindTemporalFilterErr: OSStatus { get } ``` |

Modified [kVTCouldNotFindVideoDecoderErr](https://developer.apple.com/documentation/videotoolbox/kvtcouldnotfindvideodecodererr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTCouldNotFindVideoDecoderErr: Int { get } ``` |
| To | ``` var kVTCouldNotFindVideoDecoderErr: OSStatus { get } ``` |

Modified [kVTCouldNotFindVideoEncoderErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtcouldnotfindvideoencodererr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTCouldNotFindVideoEncoderErr: Int { get } ``` |
| To | ``` var kVTCouldNotFindVideoEncoderErr: OSStatus { get } ``` |

Modified [kVTDecompressionProperty_DeinterlaceMode_Temporal](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_deinterlacemode_temporal)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_DeinterlaceMode_Temporal: CFString! ``` |
| To | ``` let kVTDecompressionProperty_DeinterlaceMode_Temporal: CFString ``` |

Modified [kVTDecompressionProperty_DeinterlaceMode_VerticalFilter](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_deinterlacemode_verticalfilter)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_DeinterlaceMode_VerticalFilter: CFString! ``` |
| To | ``` let kVTDecompressionProperty_DeinterlaceMode_VerticalFilter: CFString ``` |

Modified [kVTDecompressionProperty_FieldMode_BothFields](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_fieldmode_bothfields)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_FieldMode_BothFields: CFString! ``` |
| To | ``` let kVTDecompressionProperty_FieldMode_BothFields: CFString ``` |

Modified [kVTDecompressionProperty_FieldMode_BottomFieldOnly](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_fieldmode_bottomfieldonly)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_FieldMode_BottomFieldOnly: CFString! ``` |
| To | ``` let kVTDecompressionProperty_FieldMode_BottomFieldOnly: CFString ``` |

Modified [kVTDecompressionProperty_FieldMode_DeinterlaceFields](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_fieldmode_deinterlacefields)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_FieldMode_DeinterlaceFields: CFString! ``` |
| To | ``` let kVTDecompressionProperty_FieldMode_DeinterlaceFields: CFString ``` |

Modified [kVTDecompressionProperty_FieldMode_SingleField](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_fieldmode_singlefield)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_FieldMode_SingleField: CFString! ``` |
| To | ``` let kVTDecompressionProperty_FieldMode_SingleField: CFString ``` |

Modified [kVTDecompressionProperty_FieldMode_TopFieldOnly](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_fieldmode_topfieldonly)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_FieldMode_TopFieldOnly: CFString! ``` |
| To | ``` let kVTDecompressionProperty_FieldMode_TopFieldOnly: CFString ``` |

Modified [kVTDecompressionProperty_OnlyTheseFrames_AllFrames](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_onlytheseframes_allframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_OnlyTheseFrames_AllFrames: CFString! ``` |
| To | ``` let kVTDecompressionProperty_OnlyTheseFrames_AllFrames: CFString ``` |

Modified [kVTDecompressionProperty_OnlyTheseFrames_IFrames](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_onlytheseframes_iframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_OnlyTheseFrames_IFrames: CFString! ``` |
| To | ``` let kVTDecompressionProperty_OnlyTheseFrames_IFrames: CFString ``` |

Modified [kVTDecompressionProperty_OnlyTheseFrames_KeyFrames](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_onlytheseframes_keyframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_OnlyTheseFrames_KeyFrames: CFString! ``` |
| To | ``` let kVTDecompressionProperty_OnlyTheseFrames_KeyFrames: CFString ``` |

Modified [kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionproperty_onlytheseframes_nondroppableframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames: CFString! ``` |
| To | ``` let kVTDecompressionProperty_OnlyTheseFrames_NonDroppableFrames: CFString ``` |

Modified [kVTDecompressionPropertyKey_ContentHasInterframeDependencies](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_contenthasinterframedependencies)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_ContentHasInterframeDependencies: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_ContentHasInterframeDependencies: CFString ``` |

Modified [kVTDecompressionPropertyKey_DeinterlaceMode](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_deinterlacemode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_DeinterlaceMode: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_DeinterlaceMode: CFString ``` |

Modified [kVTDecompressionPropertyKey_FieldMode](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_fieldmode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_FieldMode: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_FieldMode: CFString ``` |

Modified [kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_maxoutputpresentationtimestampofframesbeingdecoded)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded: CFString ``` |

Modified [kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_minoutputpresentationtimestampofframesbeingdecoded)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded: CFString ``` |

Modified [kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_numberofframesbeingdecoded)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_NumberOfFramesBeingDecoded: CFString ``` |

Modified [kVTDecompressionPropertyKey_OnlyTheseFrames](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_onlytheseframes)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_OnlyTheseFrames: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_OnlyTheseFrames: CFString ``` |

Modified [kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_outputpoolrequestedminimumbuffercount)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_OutputPoolRequestedMinimumBufferCount: CFString ``` |

Modified [kVTDecompressionPropertyKey_PixelBufferPool](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixelbufferpool)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_PixelBufferPool: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_PixelBufferPool: CFString ``` |

Modified [kVTDecompressionPropertyKey_PixelBufferPoolIsShared](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixelbufferpoolisshared)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_PixelBufferPoolIsShared: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_PixelBufferPoolIsShared: CFString ``` |

Modified [kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixelformatswithreducedresolutionsupport)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport: CFString ``` |

Modified [kVTDecompressionPropertyKey_PixelTransferProperties](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_pixeltransferproperties)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_PixelTransferProperties: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_PixelTransferProperties: CFString ``` |

Modified [kVTDecompressionPropertyKey_RealTime](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_realtime)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_RealTime: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_RealTime: CFString ``` |

Modified [kVTDecompressionPropertyKey_ReducedCoefficientDecode](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_reducedcoefficientdecode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_ReducedCoefficientDecode: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_ReducedCoefficientDecode: CFString ``` |

Modified [kVTDecompressionPropertyKey_ReducedFrameDelivery](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_reducedframedelivery)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_ReducedFrameDelivery: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_ReducedFrameDelivery: CFString ``` |

Modified [kVTDecompressionPropertyKey_ReducedResolutionDecode](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_reducedresolutiondecode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_ReducedResolutionDecode: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_ReducedResolutionDecode: CFString ``` |

Modified [kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_suggestedqualityofservicetiers)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_SuggestedQualityOfServiceTiers: CFString ``` |

Modified [kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_supportedpixelformatsorderedbyperformance)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance: CFString ``` |

Modified [kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_supportedpixelformatsorderedbyquality)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByQuality: CFString ``` |

Modified [kVTDecompressionPropertyKey_ThreadCount](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_threadcount)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_ThreadCount: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_ThreadCount: CFString ``` |

Modified [kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_usinghardwareacceleratedvideodecoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString! ``` |
| To | ``` let kVTDecompressionPropertyKey_UsingHardwareAcceleratedVideoDecoder: CFString ``` |

Modified [kVTDecompressionResolutionKey_Height](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionresolutionkey_height)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionResolutionKey_Height: CFString! ``` |
| To | ``` let kVTDecompressionResolutionKey_Height: CFString ``` |

Modified [kVTDecompressionResolutionKey_Width](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionresolutionkey_width)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDecompressionResolutionKey_Width: CFString! ``` |
| To | ``` let kVTDecompressionResolutionKey_Width: CFString ``` |

Modified [kVTDownsamplingMode_Average](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_average)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDownsamplingMode_Average: CFString! ``` |
| To | ``` let kVTDownsamplingMode_Average: CFString ``` |

Modified [kVTDownsamplingMode_Decimate](https://developer.apple.com/documentation/videotoolbox/kvtdownsamplingmode_decimate)

|  | Declaration |
| --- | --- |
| From | ``` let kVTDownsamplingMode_Decimate: CFString! ``` |
| To | ``` let kVTDownsamplingMode_Decimate: CFString ``` |

Modified [kVTEncodeFrameOptionKey_ForceKeyFrame](https://developer.apple.com/documentation/videotoolbox/kvtencodeframeoptionkey_forcekeyframe)

|  | Declaration |
| --- | --- |
| From | ``` let kVTEncodeFrameOptionKey_ForceKeyFrame: CFString! ``` |
| To | ``` let kVTEncodeFrameOptionKey_ForceKeyFrame: CFString ``` |

Modified [kVTFormatDescriptionChangeNotSupportedErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtformatdescriptionchangenotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTFormatDescriptionChangeNotSupportedErr: Int { get } ``` |
| To | ``` var kVTFormatDescriptionChangeNotSupportedErr: OSStatus { get } ``` |

Modified [kVTFrameSiloInvalidTimeRangeErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtframesiloinvalidtimerangeerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTFrameSiloInvalidTimeRangeErr: Int { get } ``` |
| To | ``` var kVTFrameSiloInvalidTimeRangeErr: OSStatus { get } ``` |

Modified [kVTFrameSiloInvalidTimeStampErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtframesiloinvalidtimestamperr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTFrameSiloInvalidTimeStampErr: Int { get } ``` |
| To | ``` var kVTFrameSiloInvalidTimeStampErr: OSStatus { get } ``` |

Modified [kVTH264EntropyMode_CABAC](https://developer.apple.com/documentation/videotoolbox/kvth264entropymode_cabac)

|  | Declaration |
| --- | --- |
| From | ``` let kVTH264EntropyMode_CABAC: CFString! ``` |
| To | ``` let kVTH264EntropyMode_CABAC: CFString ``` |

Modified [kVTH264EntropyMode_CAVLC](https://developer.apple.com/documentation/videotoolbox/kvth264entropymode_cavlc)

|  | Declaration |
| --- | --- |
| From | ``` let kVTH264EntropyMode_CAVLC: CFString! ``` |
| To | ``` let kVTH264EntropyMode_CAVLC: CFString ``` |

Modified [kVTImageRotationNotSupportedErr](https://developer.apple.com/documentation/videotoolbox/kvtimagerotationnotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTImageRotationNotSupportedErr: Int { get } ``` |
| To | ``` var kVTImageRotationNotSupportedErr: OSStatus { get } ``` |

Modified [kVTInsufficientSourceColorDataErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtinsufficientsourcecolordataerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTInsufficientSourceColorDataErr: Int { get } ``` |
| To | ``` var kVTInsufficientSourceColorDataErr: OSStatus { get } ``` |

Modified [kVTInvalidSessionErr](https://developer.apple.com/documentation/videotoolbox/kvtinvalidsessionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTInvalidSessionErr: Int { get } ``` |
| To | ``` var kVTInvalidSessionErr: OSStatus { get } ``` |

Modified [kVTMultiPassStorageCreationOption_DoNotDelete](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstoragecreationoption_donotdelete)

|  | Declaration |
| --- | --- |
| From | ``` let kVTMultiPassStorageCreationOption_DoNotDelete: CFString! ``` |
| To | ``` let kVTMultiPassStorageCreationOption_DoNotDelete: CFString ``` |

Modified [kVTMultiPassStorageIdentifierMismatchErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtmultipassstorageidentifiermismatcherr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTMultiPassStorageIdentifierMismatchErr: Int { get } ``` |
| To | ``` var kVTMultiPassStorageIdentifierMismatchErr: OSStatus { get } ``` |

Modified [kVTMultiPassStorageInvalidErr](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstorageinvaliderr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTMultiPassStorageInvalidErr: Int { get } ``` |
| To | ``` var kVTMultiPassStorageInvalidErr: OSStatus { get } ``` |

Modified [kVTParameterErr](https://developer.apple.com/documentation/videotoolbox/kvtparametererr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTParameterErr: Int { get } ``` |
| To | ``` var kVTParameterErr: OSStatus { get } ``` |

Modified [kVTPixelTransferNotPermittedErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtpixeltransfernotpermittederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTPixelTransferNotPermittedErr: Int { get } ``` |
| To | ``` var kVTPixelTransferNotPermittedErr: OSStatus { get } ``` |

Modified [kVTPixelTransferNotSupportedErr](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransfernotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTPixelTransferNotSupportedErr: Int { get } ``` |
| To | ``` var kVTPixelTransferNotSupportedErr: OSStatus { get } ``` |

Modified [kVTPixelTransferPropertyKey_DestinationCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationcleanaperture)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationCleanAperture: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationCleanAperture: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DestinationColorPrimaries](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationcolorprimaries)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationColorPrimaries: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationColorPrimaries: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DestinationICCProfile](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationiccprofile)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationICCProfile: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationICCProfile: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DestinationPixelAspectRatio](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationpixelaspectratio)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationPixelAspectRatio: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationPixelAspectRatio: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DestinationTransferFunction](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationtransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationTransferFunction: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationTransferFunction: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DestinationYCbCrMatrix](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_destinationycbcrmatrix)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DestinationYCbCrMatrix: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DestinationYCbCrMatrix: CFString ``` |

Modified [kVTPixelTransferPropertyKey_DownsamplingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_downsamplingmode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_DownsamplingMode: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_DownsamplingMode: CFString ``` |

Modified [kVTPixelTransferPropertyKey_ScalingMode](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransferpropertykey_scalingmode)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPixelTransferPropertyKey_ScalingMode: CFString! ``` |
| To | ``` let kVTPixelTransferPropertyKey_ScalingMode: CFString ``` |

Modified [kVTProfileLevel_H263_Profile0_Level10](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h263_profile0_level10)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H263_Profile0_Level10: CFString! ``` |
| To | ``` let kVTProfileLevel_H263_Profile0_Level10: CFString ``` |

Modified [kVTProfileLevel_H263_Profile0_Level45](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h263_profile0_level45)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H263_Profile0_Level45: CFString! ``` |
| To | ``` let kVTProfileLevel_H263_Profile0_Level45: CFString ``` |

Modified [kVTProfileLevel_H263_Profile3_Level45](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h263_profile3_level45)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H263_Profile3_Level45: CFString! ``` |
| To | ``` let kVTProfileLevel_H263_Profile3_Level45: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_1_3](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_1_3)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_1_3: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_1_3: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_3_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_3_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_3_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_3_0: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_3_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_3_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_3_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_3_1: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_3_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_3_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_3_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_3_2: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_4_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_4_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_4_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_4_0: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_4_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_4_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_4_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_4_1: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_4_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_4_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_4_2: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_5_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_5_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_5_0: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_5_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_5_1: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_5_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_5_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_5_2: CFString ``` |

Modified [kVTProfileLevel_H264_Baseline_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_baseline_autolevel)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Baseline_AutoLevel: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Baseline_AutoLevel: CFString ``` |

Modified [kVTProfileLevel_H264_Extended_5_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_extended_5_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Extended_5_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Extended_5_0: CFString ``` |

Modified [kVTProfileLevel_H264_Extended_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_extended_autolevel)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Extended_AutoLevel: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Extended_AutoLevel: CFString ``` |

Modified [kVTProfileLevel_H264_High_3_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_3_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_3_0: CFString ``` |

Modified [kVTProfileLevel_H264_High_3_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_3_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_3_1: CFString ``` |

Modified [kVTProfileLevel_H264_High_3_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_3_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_3_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_3_2: CFString ``` |

Modified [kVTProfileLevel_H264_High_4_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_4_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_4_0: CFString ``` |

Modified [kVTProfileLevel_H264_High_4_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_4_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_4_1: CFString ``` |

Modified [kVTProfileLevel_H264_High_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_4_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_4_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_4_2: CFString ``` |

Modified [kVTProfileLevel_H264_High_5_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_5_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_5_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_5_0: CFString ``` |

Modified [kVTProfileLevel_H264_High_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_5_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_5_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_5_1: CFString ``` |

Modified [kVTProfileLevel_H264_High_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_5_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_5_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_5_2: CFString ``` |

Modified [kVTProfileLevel_H264_High_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_high_autolevel)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_High_AutoLevel: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_High_AutoLevel: CFString ``` |

Modified [kVTProfileLevel_H264_Main_3_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_3_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_3_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_3_0: CFString ``` |

Modified [kVTProfileLevel_H264_Main_3_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_3_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_3_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_3_1: CFString ``` |

Modified [kVTProfileLevel_H264_Main_3_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_3_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_3_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_3_2: CFString ``` |

Modified [kVTProfileLevel_H264_Main_4_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_4_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_4_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_4_0: CFString ``` |

Modified [kVTProfileLevel_H264_Main_4_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_4_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_4_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_4_1: CFString ``` |

Modified [kVTProfileLevel_H264_Main_4_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_4_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_4_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_4_2: CFString ``` |

Modified [kVTProfileLevel_H264_Main_5_0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_5_0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_5_0: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_5_0: CFString ``` |

Modified [kVTProfileLevel_H264_Main_5_1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_5_1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_5_1: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_5_1: CFString ``` |

Modified [kVTProfileLevel_H264_Main_5_2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_5_2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_5_2: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_5_2: CFString ``` |

Modified [kVTProfileLevel_H264_Main_AutoLevel](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_h264_main_autolevel)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_H264_Main_AutoLevel: CFString! ``` |
| To | ``` let kVTProfileLevel_H264_Main_AutoLevel: CFString ``` |

Modified [kVTProfileLevel_MP4V_AdvancedSimple_L0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_advancedsimple_l0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L0: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L0: CFString ``` |

Modified [kVTProfileLevel_MP4V_AdvancedSimple_L1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_advancedsimple_l1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L1: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L1: CFString ``` |

Modified [kVTProfileLevel_MP4V_AdvancedSimple_L2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_advancedsimple_l2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L2: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L2: CFString ``` |

Modified [kVTProfileLevel_MP4V_AdvancedSimple_L3](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_advancedsimple_l3)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L3: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L3: CFString ``` |

Modified [kVTProfileLevel_MP4V_AdvancedSimple_L4](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_advancedsimple_l4)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L4: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_AdvancedSimple_L4: CFString ``` |

Modified [kVTProfileLevel_MP4V_Main_L2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_main_l2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Main_L2: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Main_L2: CFString ``` |

Modified [kVTProfileLevel_MP4V_Main_L3](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_main_l3)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Main_L3: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Main_L3: CFString ``` |

Modified [kVTProfileLevel_MP4V_Main_L4](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_main_l4)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Main_L4: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Main_L4: CFString ``` |

Modified [kVTProfileLevel_MP4V_Simple_L0](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_simple_l0)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Simple_L0: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Simple_L0: CFString ``` |

Modified [kVTProfileLevel_MP4V_Simple_L1](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_simple_l1)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Simple_L1: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Simple_L1: CFString ``` |

Modified [kVTProfileLevel_MP4V_Simple_L2](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_simple_l2)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Simple_L2: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Simple_L2: CFString ``` |

Modified [kVTProfileLevel_MP4V_Simple_L3](https://developer.apple.com/documentation/videotoolbox/kvtprofilelevel_mp4v_simple_l3)

|  | Declaration |
| --- | --- |
| From | ``` let kVTProfileLevel_MP4V_Simple_L3: CFString! ``` |
| To | ``` let kVTProfileLevel_MP4V_Simple_L3: CFString ``` |

Modified [kVTPropertyDocumentationKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertydocumentationkey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyDocumentationKey: CFString! ``` |
| To | ``` let kVTPropertyDocumentationKey: CFString ``` |

Modified [kVTPropertyNotSupportedErr](https://developer.apple.com/documentation/videotoolbox/kvtpropertynotsupportederr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTPropertyNotSupportedErr: Int { get } ``` |
| To | ``` var kVTPropertyNotSupportedErr: OSStatus { get } ``` |

Modified [kVTPropertyReadOnlyErr](https://developer.apple.com/documentation/videotoolbox/kvtpropertyreadonlyerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTPropertyReadOnlyErr: Int { get } ``` |
| To | ``` var kVTPropertyReadOnlyErr: OSStatus { get } ``` |

Modified [kVTPropertyReadWriteStatus_ReadOnly](https://developer.apple.com/documentation/videotoolbox/kvtpropertyreadwritestatus_readonly)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyReadWriteStatus_ReadOnly: CFString! ``` |
| To | ``` let kVTPropertyReadWriteStatus_ReadOnly: CFString ``` |

Modified [kVTPropertyReadWriteStatus_ReadWrite](https://developer.apple.com/documentation/videotoolbox/kvtpropertyreadwritestatus_readwrite)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyReadWriteStatus_ReadWrite: CFString! ``` |
| To | ``` let kVTPropertyReadWriteStatus_ReadWrite: CFString ``` |

Modified [kVTPropertyReadWriteStatusKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertyreadwritestatuskey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyReadWriteStatusKey: CFString! ``` |
| To | ``` let kVTPropertyReadWriteStatusKey: CFString ``` |

Modified [kVTPropertyShouldBeSerializedKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertyshouldbeserializedkey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyShouldBeSerializedKey: CFString! ``` |
| To | ``` let kVTPropertyShouldBeSerializedKey: CFString ``` |

Modified [kVTPropertySupportedValueListKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertysupportedvaluelistkey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertySupportedValueListKey: CFString! ``` |
| To | ``` let kVTPropertySupportedValueListKey: CFString ``` |

Modified [kVTPropertySupportedValueMaximumKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertysupportedvaluemaximumkey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertySupportedValueMaximumKey: CFString! ``` |
| To | ``` let kVTPropertySupportedValueMaximumKey: CFString ``` |

Modified [kVTPropertySupportedValueMinimumKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertysupportedvalueminimumkey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertySupportedValueMinimumKey: CFString! ``` |
| To | ``` let kVTPropertySupportedValueMinimumKey: CFString ``` |

Modified [kVTPropertyType_Boolean](https://developer.apple.com/documentation/videotoolbox/kvtpropertytype_boolean)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyType_Boolean: CFString! ``` |
| To | ``` let kVTPropertyType_Boolean: CFString ``` |

Modified [kVTPropertyType_Enumeration](https://developer.apple.com/documentation/videotoolbox/kvtpropertytype_enumeration)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyType_Enumeration: CFString! ``` |
| To | ``` let kVTPropertyType_Enumeration: CFString ``` |

Modified [kVTPropertyType_Number](https://developer.apple.com/documentation/videotoolbox/kvtpropertytype_number)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyType_Number: CFString! ``` |
| To | ``` let kVTPropertyType_Number: CFString ``` |

Modified [kVTPropertyTypeKey](https://developer.apple.com/documentation/videotoolbox/kvtpropertytypekey)

|  | Declaration |
| --- | --- |
| From | ``` let kVTPropertyTypeKey: CFString! ``` |
| To | ``` let kVTPropertyTypeKey: CFString ``` |

Modified [kVTScalingMode_CropSourceToCleanAperture](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_cropsourcetocleanaperture)

|  | Declaration |
| --- | --- |
| From | ``` let kVTScalingMode_CropSourceToCleanAperture: CFString! ``` |
| To | ``` let kVTScalingMode_CropSourceToCleanAperture: CFString ``` |

Modified [kVTScalingMode_Letterbox](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_letterbox)

|  | Declaration |
| --- | --- |
| From | ``` let kVTScalingMode_Letterbox: CFString! ``` |
| To | ``` let kVTScalingMode_Letterbox: CFString ``` |

Modified [kVTScalingMode_Normal](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_normal)

|  | Declaration |
| --- | --- |
| From | ``` let kVTScalingMode_Normal: CFString! ``` |
| To | ``` let kVTScalingMode_Normal: CFString ``` |

Modified [kVTScalingMode_Trim](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_trim)

|  | Declaration |
| --- | --- |
| From | ``` let kVTScalingMode_Trim: CFString! ``` |
| To | ``` let kVTScalingMode_Trim: CFString ``` |

Modified [kVTVideoDecoderAuthorizationErr](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderauthorizationerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoDecoderAuthorizationErr: Int { get } ``` |
| To | ``` var kVTVideoDecoderAuthorizationErr: OSStatus { get } ``` |

Modified [kVTVideoDecoderBadDataErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtvideodecoderbaddataerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoDecoderBadDataErr: Int { get } ``` |
| To | ``` var kVTVideoDecoderBadDataErr: OSStatus { get } ``` |

Modified [kVTVideoDecoderMalfunctionErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtvideodecodermalfunctionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoDecoderMalfunctionErr: Int { get } ``` |
| To | ``` var kVTVideoDecoderMalfunctionErr: OSStatus { get } ``` |

Modified [kVTVideoDecoderNotAvailableNowErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtvideodecodernotavailablenowerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoDecoderNotAvailableNowErr: Int { get } ``` |
| To | ``` var kVTVideoDecoderNotAvailableNowErr: OSStatus { get } ``` |

Modified [kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_enablehardwareacceleratedvideodecoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder: CFString! ``` |
| To | ``` let kVTVideoDecoderSpecification_EnableHardwareAcceleratedVideoDecoder: CFString ``` |

Modified [kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderspecification_requirehardwareacceleratedvideodecoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString! ``` |
| To | ``` let kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder: CFString ``` |

Modified [kVTVideoDecoderUnsupportedDataFormatErr](https://developer.apple.com/documentation/videotoolbox/kvtvideodecoderunsupporteddataformaterr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoDecoderUnsupportedDataFormatErr: Int { get } ``` |
| To | ``` var kVTVideoDecoderUnsupportedDataFormatErr: OSStatus { get } ``` |

Modified [kVTVideoEncoderAuthorizationErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtvideoencoderauthorizationerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoEncoderAuthorizationErr: Int { get } ``` |
| To | ``` var kVTVideoEncoderAuthorizationErr: OSStatus { get } ``` |

Modified [kVTVideoEncoderList_CodecName](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_codecname)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderList_CodecName: CFString! ``` |
| To | ``` let kVTVideoEncoderList_CodecName: CFString ``` |

Modified [kVTVideoEncoderList_CodecType](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_codectype)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderList_CodecType: CFString! ``` |
| To | ``` let kVTVideoEncoderList_CodecType: CFString ``` |

Modified [kVTVideoEncoderList_DisplayName](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_displayname)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderList_DisplayName: CFString! ``` |
| To | ``` let kVTVideoEncoderList_DisplayName: CFString ``` |

Modified [kVTVideoEncoderList_EncoderID](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_encoderid)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderList_EncoderID: CFString! ``` |
| To | ``` let kVTVideoEncoderList_EncoderID: CFString ``` |

Modified [kVTVideoEncoderList_EncoderName](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderlist_encodername)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderList_EncoderName: CFString! ``` |
| To | ``` let kVTVideoEncoderList_EncoderName: CFString ``` |

Modified [kVTVideoEncoderMalfunctionErr](https://developer.apple.com/documentation/videotoolbox/kvtvideoencodermalfunctionerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoEncoderMalfunctionErr: Int { get } ``` |
| To | ``` var kVTVideoEncoderMalfunctionErr: OSStatus { get } ``` |

Modified [kVTVideoEncoderNotAvailableNowErr](https://developer.apple.com/documentation/videotoolbox/kvtvideoencodernotavailablenowerr)

|  | Declaration |
| --- | --- |
| From | ``` var kVTVideoEncoderNotAvailableNowErr: Int { get } ``` |
| To | ``` var kVTVideoEncoderNotAvailableNowErr: OSStatus { get } ``` |

Modified [kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_enablehardwareacceleratedvideoencoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString! ``` |
| To | ``` let kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder: CFString ``` |

Modified [kVTVideoEncoderSpecification_EncoderID](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_encoderid)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderSpecification_EncoderID: CFString! ``` |
| To | ``` let kVTVideoEncoderSpecification_EncoderID: CFString ``` |

Modified [kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder](https://developer.apple.com/documentation/videotoolbox/kvtvideoencoderspecification_requirehardwareacceleratedvideoencoder)

|  | Declaration |
| --- | --- |
| From | ``` let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString! ``` |
| To | ``` let kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder: CFString ``` |

Modified [VTCompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTCompressionOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTEncodeInfoFlags, CMSampleBuffer!) -> Void)> ``` |
| To | ``` typealias VTCompressionOutputCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void ``` |

Modified [VTCompressionSessionBeginPass(_: VTCompressionSession, _: VTCompressionSessionOptionFlags, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428289-vtcompressionsessionbeginpass)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession!, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionBeginPass(_ session: VTCompressionSession, _ beginPassFlags: VTCompressionSessionOptionFlags, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [VTCompressionSessionCompleteFrames(_: VTCompressionSession, _: CMTime) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428303-vtcompressionsessioncompletefram)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionCompleteFrames(_ session: VTCompressionSession!, _ completeUntilPresentationTimeStamp: CMTime) -> OSStatus ``` |
| To | ``` func VTCompressionSessionCompleteFrames(_ session: VTCompressionSession, _ completeUntilPresentationTimeStamp: CMTime) -> OSStatus ``` |

Modified [VTCompressionSessionCreate(_: CFAllocator?, _: Int32, _: Int32, _: CMVideoCodecType, _: CFDictionary?, _: CFDictionary?, _: CFAllocator?, _: VTCompressionOutputCallback?, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428285-vtcompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator!, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary!, _ sourceImageBufferAttributes: CFDictionary!, _ compressedDataAllocator: CFAllocator!, _ outputCallback: VTCompressionOutputCallback, _ outputCallbackRefCon: UnsafeMutablePointer<Void>, _ compressionSessionOut: UnsafeMutablePointer<Unmanaged<VTCompressionSession>?>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionCreate(_ allocator: CFAllocator?, _ width: Int32, _ height: Int32, _ codecType: CMVideoCodecType, _ encoderSpecification: CFDictionary?, _ sourceImageBufferAttributes: CFDictionary?, _ compressedDataAllocator: CFAllocator?, _ outputCallback: VTCompressionOutputCallback?, _ outputCallbackRefCon: UnsafeMutablePointer<Void>, _ compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus ``` |

Modified [VTCompressionSessionEncodeFrame(_: VTCompressionSession, _: CVImageBuffer, _: CMTime, _: CMTime, _: CFDictionary?, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428287-vtcompressionsessionencodeframe)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession!, _ imageBuffer: CVImageBuffer!, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary!, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEncodeFrame(_ session: VTCompressionSession, _ imageBuffer: CVImageBuffer, _ presentationTimeStamp: CMTime, _ duration: CMTime, _ frameProperties: CFDictionary?, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTEncodeInfoFlags>) -> OSStatus ``` |

Modified [VTCompressionSessionEndPass(_: VTCompressionSession, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<UInt32>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428313-vtcompressionsessionendpass)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession!, _ furtherPassesRequestedOut: UnsafeMutablePointer<Boolean>, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionEndPass(_ session: VTCompressionSession, _ furtherPassesRequestedOut: UnsafeMutablePointer<DarwinBoolean>, _ reserved: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified [VTCompressionSessionGetPixelBufferPool(_: VTCompressionSession) -> CVPixelBufferPool?](https://developer.apple.com/documentation/videotoolbox/1428293-vtcompressionsessiongetpixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionGetPixelBufferPool(_ session: VTCompressionSession!) -> CVPixelBufferPool! ``` |
| To | ``` func VTCompressionSessionGetPixelBufferPool(_ session: VTCompressionSession) -> CVPixelBufferPool? ``` |

Modified [VTCompressionSessionGetTimeRangesForNextPass(_: VTCompressionSession, _: UnsafeMutablePointer<CMItemCount>, _: UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428311-vtcompressionsessiongettimerange)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession!, _ timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, _ timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus ``` |
| To | ``` func VTCompressionSessionGetTimeRangesForNextPass(_ session: VTCompressionSession, _ timeRangeCountOut: UnsafeMutablePointer<CMItemCount>, _ timeRangeArrayOut: UnsafeMutablePointer<UnsafePointer<CMTimeRange>>) -> OSStatus ``` |

Modified [VTCompressionSessionInvalidate(_: VTCompressionSession)](https://developer.apple.com/documentation/videotoolbox/1428295-vtcompressionsessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionInvalidate(_ session: VTCompressionSession!) ``` |
| To | ``` func VTCompressionSessionInvalidate(_ session: VTCompressionSession) ``` |

Modified [VTCompressionSessionPrepareToEncodeFrames(_: VTCompressionSession) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1428283-vtcompressionsessionpreparetoenc)

|  | Declaration |
| --- | --- |
| From | ``` func VTCompressionSessionPrepareToEncodeFrames(_ session: VTCompressionSession!) -> OSStatus ``` |
| To | ``` func VTCompressionSessionPrepareToEncodeFrames(_ session: VTCompressionSession) -> OSStatus ``` |

Modified [VTCopyVideoEncoderList(_: CFDictionary?, _: UnsafeMutablePointer<CFArray?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1522108-vtcopyvideoencoderlist)

|  | Declaration |
| --- | --- |
| From | ``` func VTCopyVideoEncoderList(_ options: CFDictionary!, _ listOfVideoEncodersOut: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus ``` |
| To | ``` func VTCopyVideoEncoderList(_ options: CFDictionary?, _ listOfVideoEncodersOut: UnsafeMutablePointer<CFArray?>) -> OSStatus ``` |

Modified [VTDecompressionOutputCallback](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias VTDecompressionOutputCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTDecodeInfoFlags, CVImageBuffer!, CMTime, CMTime) -> Void)> ``` |
| To | ``` typealias VTDecompressionOutputCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, OSStatus, VTDecodeInfoFlags, CVImageBuffer?, CMTime, CMTime) -> Void ``` |

Modified [VTDecompressionSessionCanAcceptFormatDescription(_: VTDecompressionSession, _: CMFormatDescription) -> Bool](https://developer.apple.com/documentation/videotoolbox/1536112-vtdecompressionsessioncanacceptf)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionCanAcceptFormatDescription(_ session: VTDecompressionSession!, _ newFormatDesc: CMFormatDescription!) -> Boolean ``` |
| To | ``` func VTDecompressionSessionCanAcceptFormatDescription(_ session: VTDecompressionSession, _ newFormatDesc: CMFormatDescription) -> Bool ``` |

Modified [VTDecompressionSessionCopyBlackPixelBuffer(_: VTDecompressionSession, _: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536140-vtdecompressionsessioncopyblackp)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionCopyBlackPixelBuffer(_ session: VTDecompressionSession!, _ pixelBufferOut: UnsafeMutablePointer<Unmanaged<CVPixelBuffer>?>) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionCopyBlackPixelBuffer(_ session: VTDecompressionSession, _ pixelBufferOut: UnsafeMutablePointer<CVPixelBuffer?>) -> OSStatus ``` |

Modified [VTDecompressionSessionCreate(_: CFAllocator?, _: CMVideoFormatDescription, _: CFDictionary?, _: CFDictionary?, _: UnsafePointer<VTDecompressionOutputCallbackRecord>, _: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536134-vtdecompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ videoDecoderSpecification: CFDictionary!, _ destinationImageBufferAttributes: CFDictionary!, _ outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>, _ decompressionSessionOut: UnsafeMutablePointer<Unmanaged<VTDecompressionSession>?>) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionCreate(_ allocator: CFAllocator?, _ videoFormatDescription: CMVideoFormatDescription, _ videoDecoderSpecification: CFDictionary?, _ destinationImageBufferAttributes: CFDictionary?, _ outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>, _ decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus ``` |

Modified [VTDecompressionSessionDecodeFrame(_: VTDecompressionSession, _: CMSampleBuffer, _: VTDecodeFrameFlags, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536071-vtdecompressionsessiondecodefram)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession!, _ sampleBuffer: CMSampleBuffer!, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionDecodeFrame(_ session: VTDecompressionSession, _ sampleBuffer: CMSampleBuffer, _ decodeFlags: VTDecodeFrameFlags, _ sourceFrameRefCon: UnsafeMutablePointer<Void>, _ infoFlagsOut: UnsafeMutablePointer<VTDecodeInfoFlags>) -> OSStatus ``` |

Modified [VTDecompressionSessionFinishDelayedFrames(_: VTDecompressionSession) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536101-vtdecompressionsessionfinishdela)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionFinishDelayedFrames(_ session: VTDecompressionSession!) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionFinishDelayedFrames(_ session: VTDecompressionSession) -> OSStatus ``` |

Modified [VTDecompressionSessionInvalidate(_: VTDecompressionSession)](https://developer.apple.com/documentation/videotoolbox/1536093-vtdecompressionsessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionInvalidate(_ session: VTDecompressionSession!) ``` |
| To | ``` func VTDecompressionSessionInvalidate(_ session: VTDecompressionSession) ``` |

Modified [VTDecompressionSessionWaitForAsynchronousFrames(_: VTDecompressionSession) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536066-vtdecompressionsessionwaitforasy)

|  | Declaration |
| --- | --- |
| From | ``` func VTDecompressionSessionWaitForAsynchronousFrames(_ session: VTDecompressionSession!) -> OSStatus ``` |
| To | ``` func VTDecompressionSessionWaitForAsynchronousFrames(_ session: VTDecompressionSession) -> OSStatus ``` |

Modified [VTFrameSiloAddSampleBuffer(_: VTFrameSilo, _: CMSampleBuffer) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474240-vtframesiloaddsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloAddSampleBuffer(_ silo: VTFrameSilo!, _ sampleBuffer: CMSampleBuffer!) -> OSStatus ``` |
| To | ``` func VTFrameSiloAddSampleBuffer(_ silo: VTFrameSilo, _ sampleBuffer: CMSampleBuffer) -> OSStatus ``` |

Modified [VTFrameSiloCallBlockForEachSampleBuffer(_: VTFrameSilo, _: CMTimeRange, _: (CMSampleBuffer) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474252-vtframesilocallblockforeachsampl)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCallBlockForEachSampleBuffer(_ silo: VTFrameSilo!, _ timeRange: CMTimeRange, _ handler: ((CMSampleBuffer!) -> OSStatus)!) -> OSStatus ``` |
| To | ``` func VTFrameSiloCallBlockForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ handler: (CMSampleBuffer) -> OSStatus) -> OSStatus ``` |

Modified [VTFrameSiloCallFunctionForEachSampleBuffer(_: VTFrameSilo, _: CMTimeRange, _: UnsafeMutablePointer<Void>, _: (UnsafeMutablePointer<Void>, CMSampleBuffer) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474246-vtframesilocallfunctionforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo!, _ timeRange: CMTimeRange, _ callbackInfo: UnsafeMutablePointer<Void>, _ callback: CFunctionPointer<((UnsafeMutablePointer<Void>, CMSampleBuffer!) -> OSStatus)>) -> OSStatus ``` |
| To | ``` func VTFrameSiloCallFunctionForEachSampleBuffer(_ silo: VTFrameSilo, _ timeRange: CMTimeRange, _ callbackInfo: UnsafeMutablePointer<Void>, _ callback: (UnsafeMutablePointer<Void>, CMSampleBuffer) -> OSStatus) -> OSStatus ``` |

Modified [VTFrameSiloCreate(_: CFAllocator?, _: CFURL?, _: CMTimeRange, _: CFDictionary?, _: UnsafeMutablePointer<VTFrameSilo?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474250-vtframesilocreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ siloOut: UnsafeMutablePointer<Unmanaged<VTFrameSilo>?>) -> OSStatus ``` |
| To | ``` func VTFrameSiloCreate(_ allocator: CFAllocator?, _ fileURL: CFURL?, _ timeRange: CMTimeRange, _ options: CFDictionary?, _ siloOut: UnsafeMutablePointer<VTFrameSilo?>) -> OSStatus ``` |

Modified [VTFrameSiloGetProgressOfCurrentPass(_: VTFrameSilo, _: UnsafeMutablePointer<Float32>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474248-vtframesilogetprogressofcurrentp)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloGetProgressOfCurrentPass(_ silo: VTFrameSilo!, _ progressOut: UnsafeMutablePointer<Float32>) -> OSStatus ``` |
| To | ``` func VTFrameSiloGetProgressOfCurrentPass(_ silo: VTFrameSilo, _ progressOut: UnsafeMutablePointer<Float32>) -> OSStatus ``` |

Modified [VTFrameSiloSetTimeRangesForNextPass(_: VTFrameSilo, _: CMItemCount, _: UnsafePointer<CMTimeRange>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1474238-vtframesilosettimerangesfornextp)

|  | Declaration |
| --- | --- |
| From | ``` func VTFrameSiloSetTimeRangesForNextPass(_ silo: VTFrameSilo!, _ timeRangeCount: CMItemCount, _ timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus ``` |
| To | ``` func VTFrameSiloSetTimeRangesForNextPass(_ silo: VTFrameSilo, _ timeRangeCount: CMItemCount, _ timeRangeArray: UnsafePointer<CMTimeRange>) -> OSStatus ``` |

Modified [VTMultiPassStorageClose(_: VTMultiPassStorage) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536110-vtmultipassstorageclose)

|  | Declaration |
| --- | --- |
| From | ``` func VTMultiPassStorageClose(_ multiPassStorage: VTMultiPassStorage!) -> OSStatus ``` |
| To | ``` func VTMultiPassStorageClose(_ multiPassStorage: VTMultiPassStorage) -> OSStatus ``` |

Modified [VTMultiPassStorageCreate(_: CFAllocator?, _: CFURL?, _: CMTimeRange, _: CFDictionary?, _: UnsafeMutablePointer<VTMultiPassStorage?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536088-vtmultipassstoragecreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTMultiPassStorageCreate(_ allocator: CFAllocator!, _ fileURL: CFURL!, _ timeRange: CMTimeRange, _ options: CFDictionary!, _ multiPassStorageOut: UnsafeMutablePointer<Unmanaged<VTMultiPassStorage>?>) -> OSStatus ``` |
| To | ``` func VTMultiPassStorageCreate(_ allocator: CFAllocator?, _ fileURL: CFURL?, _ timeRange: CMTimeRange, _ options: CFDictionary?, _ multiPassStorageOut: UnsafeMutablePointer<VTMultiPassStorage?>) -> OSStatus ``` |

Modified [VTPixelTransferSessionCreate(_: CFAllocator?, _: UnsafeMutablePointer<VTPixelTransferSession?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1503546-vtpixeltransfersessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func VTPixelTransferSessionCreate(_ allocator: CFAllocator!, _ pixelTransferSessionOut: UnsafeMutablePointer<Unmanaged<VTPixelTransferSession>?>) -> OSStatus ``` |
| To | ``` func VTPixelTransferSessionCreate(_ allocator: CFAllocator?, _ pixelTransferSessionOut: UnsafeMutablePointer<VTPixelTransferSession?>) -> OSStatus ``` |

Modified [VTPixelTransferSessionInvalidate(_: VTPixelTransferSession)](https://developer.apple.com/documentation/videotoolbox/1503544-vtpixeltransfersessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func VTPixelTransferSessionInvalidate(_ session: VTPixelTransferSession!) ``` |
| To | ``` func VTPixelTransferSessionInvalidate(_ session: VTPixelTransferSession) ``` |

Modified [VTPixelTransferSessionTransferImage(_: VTPixelTransferSession, _: CVPixelBuffer, _: CVPixelBuffer) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1503548-vtpixeltransfersessiontransferim)

|  | Declaration |
| --- | --- |
| From | ``` func VTPixelTransferSessionTransferImage(_ session: VTPixelTransferSession!, _ sourceBuffer: CVPixelBuffer!, _ destinationBuffer: CVPixelBuffer!) -> OSStatus ``` |
| To | ``` func VTPixelTransferSessionTransferImage(_ session: VTPixelTransferSession, _ sourceBuffer: CVPixelBuffer, _ destinationBuffer: CVPixelBuffer) -> OSStatus ``` |

Modified [VTSessionCopyProperty(_: VTSession, _: CFString, _: CFAllocator?, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536169-vtsessioncopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionCopyProperty(_ session: VTSession!, _ propertyKey: CFString!, _ allocator: CFAllocator!, _ propertyValueOut: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func VTSessionCopyProperty(_ session: VTSession, _ propertyKey: CFString, _ allocator: CFAllocator?, _ propertyValueOut: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [VTSessionCopySerializableProperties(_: VTSession, _: CFAllocator?, _: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536142-vtsessioncopyserializablepropert)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionCopySerializableProperties(_ session: VTSession!, _ allocator: CFAllocator!, _ dictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func VTSessionCopySerializableProperties(_ session: VTSession, _ allocator: CFAllocator?, _ dictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus ``` |

Modified [VTSessionCopySupportedPropertyDictionary(_: VTSession, _: UnsafeMutablePointer<CFDictionary?>) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536080-vtsessioncopysupportedpropertydi)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionCopySupportedPropertyDictionary(_ session: VTSession!, _ supportedPropertyDictionaryOut: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus ``` |
| To | ``` func VTSessionCopySupportedPropertyDictionary(_ session: VTSession, _ supportedPropertyDictionaryOut: UnsafeMutablePointer<CFDictionary?>) -> OSStatus ``` |

Modified [VTSessionSetProperties(_: VTSession, _: CFDictionary) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536153-vtsessionsetproperties)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionSetProperties(_ session: VTSession!, _ propertyDictionary: CFDictionary!) -> OSStatus ``` |
| To | ``` func VTSessionSetProperties(_ session: VTSession, _ propertyDictionary: CFDictionary) -> OSStatus ``` |

Modified [VTSessionSetProperty(_: VTSession, _: CFString, _: AnyObject) -> OSStatus](https://developer.apple.com/documentation/videotoolbox/1536144-vtsessionsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` func VTSessionSetProperty(_ session: VTSession!, _ propertyKey: CFString!, _ propertyValue: AnyObject!) -> OSStatus ``` |
| To | ``` func VTSessionSetProperty(_ session: VTSession, _ propertyKey: CFString, _ propertyValue: AnyObject) -> OSStatus ``` |

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
