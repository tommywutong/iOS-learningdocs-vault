---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreMedia.html
archived_at: '2026-07-18T02:56:45.873751Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreMedia Changes for Swift

### CoreMedia

Removed CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon: UnsafeMutablePointer<Void>)Removed CMBufferCallbacks.init()Removed CMBufferCallbacks.init(version: UInt32, refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration: CMBufferGetTimeCallback, isDataReady: CMBufferGetBooleanCallback, compare: CMBufferCompareCallback, dataBecameReadyNotification: Unmanaged<CFString>!, getSize: CMBufferGetSizeCallback)Removed CMTimeFlags.init(_: UInt32)Added CMBlockBufferCustomBlockSource.init(version: UInt32, AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?, FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?, refCon: UnsafeMutablePointer<Void>)Added CMTime.convertScale(_: Int32, method: CMTimeRoundingMethod) -> CMTimeAdded [CMTime.hasBeenRounded](https://developer.apple.com/documentation/coremedia/cmtime/1489548-hasbeenrounded)Added CMTime.init(seconds: Double, preferredTimescale: CMTimeScale)Added CMTime.init(value: CMTimeValue, timescale: CMTimeScale)Added [CMTime.isIndefinite](https://developer.apple.com/documentation/coremedia/cmtime/1489267-isindefinite)Added [CMTime.isNegativeInfinity](https://developer.apple.com/documentation/coremedia/cmtime/1489283-isnegativeinfinity)Added [CMTime.isNumeric](https://developer.apple.com/documentation/coremedia/cmtime/1489535-isnumeric)Added [CMTime.isPositiveInfinity](https://developer.apple.com/documentation/coremedia/cmtime/1489693-ispositiveinfinity)Added [CMTime.isValid](https://developer.apple.com/documentation/coremedia/cmtime/1489207-isvalid)Added [CMTime.seconds](https://developer.apple.com/documentation/coremedia/cmtime/1489443-seconds)Added CMTimeRange.containsTime(_: CMTime) -> BoolAdded CMTimeRange.containsTimeRange(_: CMTimeRange) -> BoolAdded CMTimeRange.endAdded CMTimeRange.init(start: CMTime, end: CMTime)Added CMTimeRange.intersection(_: CMTimeRange) -> CMTimeRangeAdded [CMTimeRange.isEmpty](https://developer.apple.com/documentation/coremedia/cmtimerange/1489139-isempty)Added [CMTimeRange.isIndefinite](https://developer.apple.com/documentation/coremedia/cmtimerange/1489366-isindefinite)Added [CMTimeRange.isValid](https://developer.apple.com/documentation/coremedia/cmtimerange/1489273-isvalid)Added CMTimeRange.union(_: CMTimeRange) -> CMTimeRangeAdded [CMTimeRoundingMethod.Default](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/kcmtimeroundingmethod_default)Added !=(_: CMTimeRange, _: CMTimeRange) -> BoolAdded !=(_: CMTime, _: CMTime) -> BoolAdded +(_: CMTime, _: CMTime) -> CMTimeAdded -(_: CMTime, _: CMTime) -> CMTimeAdded <(_: CMTime, _: CMTime) -> BoolAdded <=(_: CMTime, _: CMTime) -> BoolAdded ==(_: CMTimeRange, _: CMTimeRange) -> BoolAdded ==(_: CMTime, _: CMTime) -> BoolAdded >(_: CMTime, _: CMTime) -> BoolAdded >=(_: CMTime, _: CMTime) -> BoolAdded [CMTIME_HAS_BEEN_ROUNDED(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489530-cmtime_has_been_rounded)Added [CMTIME_IS_INDEFINITE(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489754-cmtime_is_indefinite)Added [CMTIME_IS_INVALID(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489272-cmtime_is_invalid)Added [CMTIME_IS_NEGATIVEINFINITY(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489459-cmtime_is_negativeinfinity)Added [CMTIME_IS_NUMERIC(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489401-cmtime_is_numeric)Added [CMTIME_IS_POSITIVEINFINITY(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489320-cmtime_is_positiveinfinity)Added [CMTIME_IS_VALID(_: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1489280-cmtime_is_valid)Added [CMTimebaseCopyMaster(_: CMTimebase) -> CMClockOrTimebase?](https://developer.apple.com/documentation/coremedia/1489679-cmtimebasecopymaster)Added [CMTimebaseCopyMasterClock(_: CMTimebase) -> CMClock?](https://developer.apple.com/documentation/coremedia/1489238-cmtimebasecopymasterclock)Added [CMTimebaseCopyMasterTimebase(_: CMTimebase) -> CMTimebase?](https://developer.apple.com/documentation/coremedia/1489341-cmtimebasecopymastertimebase)Added [CMTimebaseCopyUltimateMasterClock(_: CMTimebase) -> CMClock?](https://developer.apple.com/documentation/coremedia/1489262-cmtimebasecopyultimatemastercloc)Added [CMTimeMappingCopyAsDictionary(_: CMTimeMapping, _: CFAllocator?) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1462805-cmtimemappingcopyasdictionary)Added [CMTimeMappingCopyDescription(_: CFAllocator?, _: CMTimeMapping) -> CFString?](https://developer.apple.com/documentation/coremedia/1462811-cmtimemappingcopydescription)Added [CMTimeMappingMake(_: CMTimeRange, _: CMTimeRange) -> CMTimeMapping](https://developer.apple.com/documentation/coremedia/1462793-cmtimemappingmake)Added [CMTimeMappingMakeEmpty(_: CMTimeRange) -> CMTimeMapping](https://developer.apple.com/documentation/coremedia/1462828-cmtimemappingmakeempty)Added [CMTimeMappingMakeFromDictionary(_: CFDictionary) -> CMTimeMapping](https://developer.apple.com/documentation/coremedia/1462796-cmtimemappingmakefromdictionary)Added [CMTimeMappingShow(_: CMTimeMapping)](https://developer.apple.com/documentation/coremedia/1462835-cmtimemappingshow)Added [CMTIMERANGE_IS_EMPTY(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489251-cmtimerange_is_empty)Added [CMTIMERANGE_IS_INDEFINITE(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489261-cmtimerange_is_indefinite)Added [CMTIMERANGE_IS_INVALID(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489472-cmtimerange_is_invalid)Added [CMTIMERANGE_IS_VALID(_: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1489373-cmtimerange_is_valid)Added COREMEDIA_DECLARE_BRIDGED_TYPESAdded COREMEDIA_DECLARE_NULLABILITYAdded COREMEDIA_DECLARE_NULLABILITY_BEGIN_ENDAdded COREMEDIA_DECLARE_RETURNS_NOT_RETAINED_ON_PARAMETERSAdded COREMEDIA_DECLARE_RETURNS_RETAINEDAdded COREMEDIA_DECLARE_RETURNS_RETAINED_ON_PARAMETERSAdded [kCMFormatDescriptionChromaLocation_Bottom](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottom)Added [kCMFormatDescriptionChromaLocation_BottomLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottomleft)Added [kCMFormatDescriptionChromaLocation_Center](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_center)Added [kCMFormatDescriptionChromaLocation_DV420](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_dv420)Added [kCMFormatDescriptionChromaLocation_Left](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_left)Added [kCMFormatDescriptionChromaLocation_Top](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_top)Added [kCMFormatDescriptionChromaLocation_TopLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_topleft)Added [kCMFormatDescriptionColorPrimaries_DCI_P3](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_dci_p3)Added [kCMFormatDescriptionColorPrimaries_EBU_3213](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_ebu_3213)Added [kCMFormatDescriptionColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_2020)Added [kCMFormatDescriptionColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_709_2)Added [kCMFormatDescriptionColorPrimaries_P3_D65](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p3_d65)Added [kCMFormatDescriptionColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_smpte_c)Added [kCMFormatDescriptionExtension_ChromaLocationBottomField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationbottomfield)Added [kCMFormatDescriptionExtension_ChromaLocationTopField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationtopfield)Added [kCMFormatDescriptionExtension_CleanAperture](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_cleanaperture)Added [kCMFormatDescriptionExtension_ColorPrimaries](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_colorprimaries)Added [kCMFormatDescriptionExtension_FieldCount](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fieldcount)Added [kCMFormatDescriptionExtension_FieldDetail](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fielddetail)Added [kCMFormatDescriptionExtension_GammaLevel](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_gammalevel)Added [kCMFormatDescriptionExtension_PixelAspectRatio](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_pixelaspectratio)Added [kCMFormatDescriptionExtension_TransferFunction](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_transferfunction)Added [kCMFormatDescriptionExtension_VerbatimImageDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_verbatimimagedescription)Added [kCMFormatDescriptionExtension_YCbCrMatrix](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_ycbcrmatrix)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineEarly](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlineearly)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineLate](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlinelate)Added [kCMFormatDescriptionFieldDetail_TemporalBottomFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporalbottomfirst)Added [kCMFormatDescriptionFieldDetail_TemporalTopFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporaltopfirst)Added [kCMFormatDescriptionKey_CleanApertureHeight](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureheight)Added [kCMFormatDescriptionKey_CleanApertureHorizontalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturehorizontaloffset)Added [kCMFormatDescriptionKey_CleanApertureVerticalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureverticaloffset)Added [kCMFormatDescriptionKey_CleanApertureWidth](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturewidth)Added [kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratiohorizontalspacing)Added [kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratioverticalspacing)Added [kCMFormatDescriptionTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_2020)Added [kCMFormatDescriptionTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_709_2)Added [kCMFormatDescriptionTransferFunction_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_smpte_240m_1995)Added [kCMFormatDescriptionTransferFunction_UseGamma](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_usegamma)Added kCMFormatDescriptionYCbCrMatrix_DCI_P3Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_2020)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_601_4)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_709_2)Added kCMFormatDescriptionYCbCrMatrix_P3_D65Added [kCMFormatDescriptionYCbCrMatrix_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_smpte_240m_1995)Added [kCMMetadataBaseDataType_JSON](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_json)Added [kCMMetadataBaseDataType_PolygonF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polygonf32)Added [kCMMetadataBaseDataType_PolylineF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polylinef32)Added [kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescription_structuraldependencykey_dependencyisinvalidflag)Added [kCMMetadataFormatDescriptionKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_structuraldependency)Added [kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_structuraldependency)Added [kCMMetadataIdentifier_QuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatavideoorientation)Added [kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_stillimagelensstabilizationinfo)Added [kCMSampleBufferLensStabilizationInfo_Active](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_active)Added [kCMSampleBufferLensStabilizationInfo_Off](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_off)Added [kCMSampleBufferLensStabilizationInfo_OutOfRange](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_outofrange)Added [kCMSampleBufferLensStabilizationInfo_Unavailable](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_unavailable)Added [kCMTimeMappingInvalid](https://developer.apple.com/documentation/coremedia/cmtimemapping/1462795-invalid)Added [kCMTimeMappingSourceKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingsourcekey)Added [kCMTimeMappingTargetKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingtargetkey)Added [kCMVideoCodecType_HEVC](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_hevc)Modified [CMBlockBufferCustomBlockSource [struct]](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource)

|  | Declaration |
| --- | --- |
| From | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>     var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, AllocateBlock AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)>, FreeBlock FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)>, refCon refCon: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CMBlockBufferCustomBlockSource {     var version: UInt32     var AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?     var FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?     var refCon: UnsafeMutablePointer<Void>     init()     init(version version: UInt32, AllocateBlock AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)?, FreeBlock FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)?, refCon refCon: UnsafeMutablePointer<Void>) } ``` |

Modified [CMBlockBufferCustomBlockSource.AllocateBlock](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489804-allocateblock)

|  | Declaration |
| --- | --- |
| From | ``` var AllocateBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var AllocateBlock: ((UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>)? ``` |

Modified [CMBlockBufferCustomBlockSource.FreeBlock](https://developer.apple.com/documentation/coremedia/cmblockbuffercustomblocksource/1489467-freeblock)

|  | Declaration |
| --- | --- |
| From | ``` var FreeBlock: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)> ``` |
| To | ``` var FreeBlock: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Void)? ``` |

Modified [CMBufferCallbacks [struct]](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback     var getPresentationTimeStamp: CMBufferGetTimeCallback     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback     var compare: CMBufferCompareCallback     var dataBecameReadyNotification: Unmanaged<CFString>!     var getSize: CMBufferGetSizeCallback     init()     init(version version: UInt32, refcon refcon: UnsafeMutablePointer<Void>, getDecodeTimeStamp getDecodeTimeStamp: CMBufferGetTimeCallback, getPresentationTimeStamp getPresentationTimeStamp: CMBufferGetTimeCallback, getDuration getDuration: CMBufferGetTimeCallback, isDataReady isDataReady: CMBufferGetBooleanCallback, compare compare: CMBufferCompareCallback, dataBecameReadyNotification dataBecameReadyNotification: Unmanaged<CFString>!, getSize getSize: CMBufferGetSizeCallback) } ``` |
| To | ``` struct CMBufferCallbacks {     var version: UInt32     var refcon: UnsafeMutablePointer<Void>     var getDecodeTimeStamp: CMBufferGetTimeCallback?     var getPresentationTimeStamp: CMBufferGetTimeCallback?     var getDuration: CMBufferGetTimeCallback     var isDataReady: CMBufferGetBooleanCallback?     var compare: CMBufferCompareCallback?     var dataBecameReadyNotification: Unmanaged<CFString>?     var getSize: CMBufferGetSizeCallback? } ``` |

Modified [CMBufferCallbacks.compare](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489718-compare)

|  | Declaration |
| --- | --- |
| From | ``` var compare: CMBufferCompareCallback ``` |
| To | ``` var compare: CMBufferCompareCallback? ``` |

Modified [CMBufferCallbacks.dataBecameReadyNotification](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489416-databecamereadynotification)

|  | Declaration |
| --- | --- |
| From | ``` var dataBecameReadyNotification: Unmanaged<CFString>! ``` |
| To | ``` var dataBecameReadyNotification: Unmanaged<CFString>? ``` |

Modified [CMBufferCallbacks.getDecodeTimeStamp](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489805-getdecodetimestamp)

|  | Declaration |
| --- | --- |
| From | ``` var getDecodeTimeStamp: CMBufferGetTimeCallback ``` |
| To | ``` var getDecodeTimeStamp: CMBufferGetTimeCallback? ``` |

Modified [CMBufferCallbacks.getPresentationTimeStamp](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489600-getpresentationtimestamp)

|  | Declaration |
| --- | --- |
| From | ``` var getPresentationTimeStamp: CMBufferGetTimeCallback ``` |
| To | ``` var getPresentationTimeStamp: CMBufferGetTimeCallback? ``` |

Modified [CMBufferCallbacks.getSize](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489328-getsize)

|  | Declaration |
| --- | --- |
| From | ``` var getSize: CMBufferGetSizeCallback ``` |
| To | ``` var getSize: CMBufferGetSizeCallback? ``` |

Modified [CMBufferCallbacks.isDataReady](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/1489430-isdataready)

|  | Declaration |
| --- | --- |
| From | ``` var isDataReady: CMBufferGetBooleanCallback ``` |
| To | ``` var isDataReady: CMBufferGetBooleanCallback? ``` |

Modified [CMTime [struct]](https://developer.apple.com/documentation/coremedia/cmtime)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch) } ``` | -- |
| To | ``` struct CMTime {     var value: CMTimeValue     var timescale: CMTimeScale     var flags: CMTimeFlags     var epoch: CMTimeEpoch     init()     init(value value: CMTimeValue, timescale timescale: CMTimeScale, flags flags: CMTimeFlags, epoch epoch: CMTimeEpoch) } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } extension CMTime {     init(seconds seconds: Double, preferredTimescale preferredTimescale: CMTimeScale)     init(value value: CMTimeValue, timescale timescale: CMTimeScale) } extension CMTime {     var isValid: Bool { get }     var isPositiveInfinity: Bool { get }     var isNegativeInfinity: Bool { get }     var isIndefinite: Bool { get }     var isNumeric: Bool { get }     var hasBeenRounded: Bool { get }     var seconds: Double { get }     func convertScale(_ newTimescale: Int32, method method: CMTimeRoundingMethod) -> CMTime } extension CMTime : Equatable, Comparable { } ``` | Comparable, Equatable |

Modified [CMTimeFlags [struct]](https://developer.apple.com/documentation/coremedia/cmtimeflags)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMTimeFlags : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` | RawOptionSetType |
| To | ``` struct CMTimeFlags : OptionSetType {     init(rawValue rawValue: UInt32)     static var Valid: CMTimeFlags { get }     static var HasBeenRounded: CMTimeFlags { get }     static var PositiveInfinity: CMTimeFlags { get }     static var NegativeInfinity: CMTimeFlags { get }     static var Indefinite: CMTimeFlags { get }     static var ImpliedValueFlagsMask: CMTimeFlags { get } } ``` | OptionSetType |

Modified [CMTimeRange [struct]](https://developer.apple.com/documentation/coremedia/cmtimerange)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime) } ``` | -- |
| To | ``` struct CMTimeRange {     var start: CMTime     var duration: CMTime     init()     init(start start: CMTime, duration duration: CMTime) } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     @warn_unused_result     func union(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func containsTime(_ time: CMTime) -> Bool     @warn_unused_result     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } extension CMTimeRange {     init(start start: CMTime, end end: CMTime)     var isValid: Bool { get }     var isIndefinite: Bool { get }     var isEmpty: Bool { get }     var end: CMTime { get }     @warn_unused_result     func union(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func intersection(_ otherRange: CMTimeRange) -> CMTimeRange     @warn_unused_result     func containsTime(_ time: CMTime) -> Bool     @warn_unused_result     func containsTimeRange(_ range: CMTimeRange) -> Bool } extension CMTimeRange : Equatable { } ``` | Equatable |

Modified [CMTimeRoundingMethod [enum]](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum CMTimeRoundingMethod : UInt32 {     case RoundHalfAwayFromZero     case RoundTowardZero     case RoundAwayFromZero     case QuickTime     case RoundTowardPositiveInfinity     case RoundTowardNegativeInfinity } ``` | -- |
| To | ``` enum CMTimeRoundingMethod : UInt32 {     case RoundHalfAwayFromZero     case RoundTowardZero     case RoundAwayFromZero     case QuickTime     case RoundTowardPositiveInfinity     case RoundTowardNegativeInfinity     static var Default: CMTimeRoundingMethod { get } } ``` | UInt32 |

Modified [CMAudioClockCreate(_: CFAllocator?, _: UnsafeMutablePointer<CMClock?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1618913-cmaudioclockcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioClockCreate(_ allocator: CFAllocator!, _ clockOut: UnsafeMutablePointer<Unmanaged<CMClock>?>) -> OSStatus ``` |
| To | ``` func CMAudioClockCreate(_ allocator: CFAllocator?, _ clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(_: CFAllocator?, _: CMAudioFormatDescription, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416293-cmaudioformatdescriptioncopyasbi)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ audioFormatDescription: CMAudioFormatDescription!, _ soundDescriptionFlavor: CFString!, _ soundDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator?, _ audioFormatDescription: CMAudioFormatDescription, _ soundDescriptionFlavor: CFString?, _ soundDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionCreate(_: CFAllocator?, _: UnsafePointer<AudioStreamBasicDescription>, _: Int, _: UnsafePointer<AudioChannelLayout>, _: Int, _: UnsafePointer<Void>, _: CFDictionary?, _: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489522-cmaudioformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator!, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: Int, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreate(_ allocator: CFAllocator?, _ asbd: UnsafePointer<AudioStreamBasicDescription>, _ layoutSize: Int, _ layout: UnsafePointer<AudioChannelLayout>, _ magicCookieSize: Int, _ magicCookie: UnsafePointer<Void>, _ extensions: CFDictionary?, _ outDesc: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFString?, _: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416264-cmaudioformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator!, _ soundDescriptionBlockBuffer: CMBlockBuffer!, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer(_ allocator: CFAllocator?, _ soundDescriptionBlockBuffer: CMBlockBuffer, _ soundDescriptionFlavor: CFString?, _ audioFormatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFString?, _: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416299-cmaudioformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator!, _ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: Int, _ soundDescriptionFlavor: CFString!, _ audioFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData(_ allocator: CFAllocator?, _ soundDescriptionData: UnsafePointer<UInt8>, _ soundDescriptionSize: Int, _ soundDescriptionFlavor: CFString?, _ audioFormatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionCreateSummary(_: CFAllocator?, _: CFArray, _: UInt32, _: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489608-cmaudioformatdescriptioncreatesu)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionCreateSummary(_ allocator: CFAllocator!, _ formatDescriptionArray: CFArray!, _ flags: UInt32, _ summaryFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMAudioFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMAudioFormatDescriptionCreateSummary(_ allocator: CFAllocator?, _ formatDescriptionArray: CFArray, _ flags: UInt32, _ summaryFormatDescriptionOut: UnsafeMutablePointer<CMAudioFormatDescription?>) -> OSStatus ``` |

Modified [CMAudioFormatDescriptionEqual(_: CMAudioFormatDescription, _: CMAudioFormatDescription, _: CMAudioFormatDescriptionMask, _: UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Bool](https://developer.apple.com/documentation/coremedia/1489582-cmaudioformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription!, _ desc2: CMAudioFormatDescription!, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Boolean ``` |
| To | ``` func CMAudioFormatDescriptionEqual(_ desc1: CMAudioFormatDescription, _ desc2: CMAudioFormatDescription, _ equalityMask: CMAudioFormatDescriptionMask, _ equalityMaskOut: UnsafeMutablePointer<CMAudioFormatDescriptionMask>) -> Bool ``` |

Modified [CMAudioFormatDescriptionGetChannelLayout(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout>](https://developer.apple.com/documentation/coremedia/1489137-cmaudioformatdescriptiongetchann)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription!, _ layoutSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout> ``` |
| To | ``` func CMAudioFormatDescriptionGetChannelLayout(_ desc: CMAudioFormatDescription, _ layoutSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioChannelLayout> ``` |

Modified [CMAudioFormatDescriptionGetFormatList(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem>](https://developer.apple.com/documentation/coremedia/1489782-cmaudioformatdescriptiongetforma)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription!, _ formatListSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetFormatList(_ desc: CMAudioFormatDescription, _ formatListSize: UnsafeMutablePointer<Int>) -> UnsafePointer<AudioFormatListItem> ``` |

Modified [CMAudioFormatDescriptionGetMagicCookie(_: CMAudioFormatDescription, _: UnsafeMutablePointer<Int>) -> UnsafePointer<Void>](https://developer.apple.com/documentation/coremedia/1489508-cmaudioformatdescriptiongetmagic)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription!, _ cookieSizeOut: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |
| To | ``` func CMAudioFormatDescriptionGetMagicCookie(_ desc: CMAudioFormatDescription, _ cookieSizeOut: UnsafeMutablePointer<Int>) -> UnsafePointer<Void> ``` |

Modified [CMAudioFormatDescriptionGetMostCompatibleFormat(_: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>](https://developer.apple.com/documentation/coremedia/1489474-cmaudioformatdescriptiongetmostc)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetMostCompatibleFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem> ``` |

Modified [CMAudioFormatDescriptionGetRichestDecodableFormat(_: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem>](https://developer.apple.com/documentation/coremedia/1489575-cmaudioformatdescriptiongetriche)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioFormatListItem> ``` |
| To | ``` func CMAudioFormatDescriptionGetRichestDecodableFormat(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioFormatListItem> ``` |

Modified [CMAudioFormatDescriptionGetStreamBasicDescription(_: CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription>](https://developer.apple.com/documentation/coremedia/1489226-cmaudioformatdescriptiongetstrea)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription!) -> UnsafePointer<AudioStreamBasicDescription> ``` |
| To | ``` func CMAudioFormatDescriptionGetStreamBasicDescription(_ desc: CMAudioFormatDescription) -> UnsafePointer<AudioStreamBasicDescription> ``` |

Modified [CMAudioSampleBufferCreateReadyWithPacketDescriptions(_: CFAllocator?, _: CMBlockBuffer?, _: CMFormatDescription, _: CMItemCount, _: CMTime, _: UnsafePointer<AudioStreamPacketDescription>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489500-cmaudiosamplebuffercreatereadywi)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioSampleBufferCreateReadyWithPacketDescriptions(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMAudioSampleBufferCreateReadyWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMAudioSampleBufferCreateWithPacketDescriptions(_: CFAllocator?, _: CMBlockBuffer?, _: Bool, _: CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutablePointer<Void>, _: CMFormatDescription, _: CMItemCount, _: CMTime, _: UnsafePointer<AudioStreamPacketDescription>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489466-cmaudiosamplebuffercreatewithpac)

|  | Declaration |
| --- | --- |
| From | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMAudioSampleBufferCreateWithPacketDescriptions(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ sbufPTS: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferAccessDataBytes(_: CMBlockBuffer, _: Int, _: Int, _: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489228-cmblockbufferaccessdatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferAccessDataBytes(_ theBuffer: CMBlockBuffer, _ offset: Int, _ length: Int, _ temporaryBlock: UnsafeMutablePointer<Void>, _ returnedPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |

Modified [CMBlockBufferAppendBufferReference(_: CMBlockBuffer, _: CMBlockBuffer, _: Int, _: Int, _: CMBlockBufferFlags) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489160-cmblockbufferappendbufferreferen)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer!, _ targetBBuf: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |
| To | ``` func CMBlockBufferAppendBufferReference(_ theBuffer: CMBlockBuffer, _ targetBBuf: CMBlockBuffer, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |

Modified [CMBlockBufferAppendMemoryBlock(_: CMBlockBuffer, _: UnsafeMutablePointer<Void>, _: Int, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>, _: Int, _: Int, _: CMBlockBufferFlags) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489394-cmblockbufferappendmemoryblock)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |
| To | ``` func CMBlockBufferAppendMemoryBlock(_ theBuffer: CMBlockBuffer, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags) -> OSStatus ``` |

Modified [CMBlockBufferAssureBlockMemory(_: CMBlockBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489560-cmblockbufferassureblockmemory)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferAssureBlockMemory(_ theBuffer: CMBlockBuffer!) -> OSStatus ``` |
| To | ``` func CMBlockBufferAssureBlockMemory(_ theBuffer: CMBlockBuffer) -> OSStatus ``` |

Modified [CMBlockBufferCopyDataBytes(_: CMBlockBuffer, _: Int, _: Int, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489155-cmblockbuffercopydatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCopyDataBytes(_ theSourceBuffer: CMBlockBuffer, _ offsetToData: Int, _ dataLength: Int, _ destination: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMBlockBufferCreateContiguous(_: CFAllocator?, _: CMBlockBuffer, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>, _: Int, _: Int, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489220-cmblockbuffercreatecontiguous)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator!, _ sourceBuffer: CMBlockBuffer!, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateContiguous(_ structureAllocator: CFAllocator?, _ sourceBuffer: CMBlockBuffer, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferCreateEmpty(_: CFAllocator?, _: UInt32, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489149-cmblockbuffercreateempty)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateEmpty(_ structureAllocator: CFAllocator!, _ subBlockCapacity: UInt32, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateEmpty(_ structureAllocator: CFAllocator?, _ subBlockCapacity: UInt32, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferCreateWithBufferReference(_: CFAllocator?, _: CMBlockBuffer, _: Int, _: Int, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489279-cmblockbuffercreatewithbufferref)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator!, _ targetBuffer: CMBlockBuffer!, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateWithBufferReference(_ structureAllocator: CFAllocator?, _ targetBuffer: CMBlockBuffer, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferCreateWithMemoryBlock(_: CFAllocator?, _: UnsafeMutablePointer<Void>, _: Int, _: CFAllocator?, _: UnsafePointer<CMBlockBufferCustomBlockSource>, _: Int, _: Int, _: CMBlockBufferFlags, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489501-cmblockbuffercreatewithmemoryblo)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator!, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator!, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMBlockBufferCreateWithMemoryBlock(_ structureAllocator: CFAllocator?, _ memoryBlock: UnsafeMutablePointer<Void>, _ blockLength: Int, _ blockAllocator: CFAllocator?, _ customBlockSource: UnsafePointer<CMBlockBufferCustomBlockSource>, _ offsetToData: Int, _ dataLength: Int, _ flags: CMBlockBufferFlags, _ newBBufOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMBlockBufferFillDataBytes(_: Int8, _: CMBlockBuffer, _: Int, _: Int) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489550-cmblockbufferfilldatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |
| To | ``` func CMBlockBufferFillDataBytes(_ fillByte: Int8, _ destinationBuffer: CMBlockBuffer, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |

Modified [CMBlockBufferGetDataLength(_: CMBlockBuffer) -> Int](https://developer.apple.com/documentation/coremedia/1489292-cmblockbuffergetdatalength)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer!) -> Int ``` |
| To | ``` func CMBlockBufferGetDataLength(_ theBuffer: CMBlockBuffer) -> Int ``` |

Modified [CMBlockBufferGetDataPointer(_: CMBlockBuffer, _: Int, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489264-cmblockbuffergetdatapointer)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>, _ totalLength: UnsafeMutablePointer<Int>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |
| To | ``` func CMBlockBufferGetDataPointer(_ theBuffer: CMBlockBuffer, _ offset: Int, _ lengthAtOffset: UnsafeMutablePointer<Int>, _ totalLength: UnsafeMutablePointer<Int>, _ dataPointer: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` |

Modified [CMBlockBufferIsEmpty(_: CMBlockBuffer) -> Bool](https://developer.apple.com/documentation/coremedia/1489813-cmblockbufferisempty)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferIsEmpty(_ theBuffer: CMBlockBuffer!) -> Boolean ``` |
| To | ``` func CMBlockBufferIsEmpty(_ theBuffer: CMBlockBuffer) -> Bool ``` |

Modified [CMBlockBufferIsRangeContiguous(_: CMBlockBuffer, _: Int, _: Int) -> Bool](https://developer.apple.com/documentation/coremedia/1489609-cmblockbufferisrangecontiguous)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer!, _ offset: Int, _ length: Int) -> Boolean ``` |
| To | ``` func CMBlockBufferIsRangeContiguous(_ theBuffer: CMBlockBuffer, _ offset: Int, _ length: Int) -> Bool ``` |

Modified [CMBlockBufferReplaceDataBytes(_: UnsafePointer<Void>, _: CMBlockBuffer, _: Int, _: Int) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489222-cmblockbufferreplacedatabytes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer!, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |
| To | ``` func CMBlockBufferReplaceDataBytes(_ sourceBytes: UnsafePointer<Void>, _ destinationBuffer: CMBlockBuffer, _ offsetIntoDestination: Int, _ dataLength: Int) -> OSStatus ``` |

Modified [CMBufferCompareCallback](https://developer.apple.com/documentation/coremedia/cmbuffercomparecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferCompareCallback = CFunctionPointer<((CMBuffer!, CMBuffer!, UnsafeMutablePointer<Void>) -> CFComparisonResult)> ``` |
| To | ``` typealias CMBufferCompareCallback = (CMBuffer, CMBuffer, UnsafeMutablePointer<Void>) -> CFComparisonResult ``` |

Modified [CMBufferGetBooleanCallback](https://developer.apple.com/documentation/coremedia/cmbuffergetbooleancallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetBooleanCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Boolean)> ``` |
| To | ``` typealias CMBufferGetBooleanCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> DarwinBoolean ``` |

Modified [CMBufferGetSizeCallback](https://developer.apple.com/documentation/coremedia/cmbuffergetsizecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetSizeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Int)> ``` |
| To | ``` typealias CMBufferGetSizeCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> Int ``` |

Modified [CMBufferGetTimeCallback](https://developer.apple.com/documentation/coremedia/cmbuffergettimecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferGetTimeCallback = CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> CMTime)> ``` |
| To | ``` typealias CMBufferGetTimeCallback = (CMBuffer, UnsafeMutablePointer<Void>) -> CMTime ``` |

Modified [CMBufferQueueCallForEachBuffer(_: CMBufferQueue, _: (CMBuffer, UnsafeMutablePointer<Void>) -> OSStatus, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489798-cmbufferqueuecallforeachbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueCallForEachBuffer(_ queue: CMBufferQueue, _ callback: (CMBuffer, UnsafeMutablePointer<Void>) -> OSStatus, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMBufferQueueContainsEndOfData(_: CMBufferQueue) -> Bool](https://developer.apple.com/documentation/coremedia/1489480-cmbufferqueuecontainsendofdata)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueContainsEndOfData(_ queue: CMBufferQueue!) -> Boolean ``` |
| To | ``` func CMBufferQueueContainsEndOfData(_ queue: CMBufferQueue) -> Bool ``` |

Modified [CMBufferQueueCreate(_: CFAllocator?, _: CMItemCount, _: UnsafePointer<CMBufferCallbacks>, _: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489604-cmbufferqueuecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueCreate(_ allocator: CFAllocator!, _ capacity: CMItemCount, _ callbacks: UnsafePointer<CMBufferCallbacks>, _ queueOut: UnsafeMutablePointer<Unmanaged<CMBufferQueue>?>) -> OSStatus ``` |
| To | ``` func CMBufferQueueCreate(_ allocator: CFAllocator?, _ capacity: CMItemCount, _ callbacks: UnsafePointer<CMBufferCallbacks>, _ queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus ``` |

Modified [CMBufferQueueEnqueue(_: CMBufferQueue, _: CMBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489422-cmbufferqueueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueEnqueue(_ queue: CMBufferQueue!, _ buf: CMBuffer!) -> OSStatus ``` |
| To | ``` func CMBufferQueueEnqueue(_ queue: CMBufferQueue, _ buf: CMBuffer) -> OSStatus ``` |

Modified [CMBufferQueueGetBufferCount(_: CMBufferQueue) -> CMItemCount](https://developer.apple.com/documentation/coremedia/1489589-cmbufferqueuegetbuffercount)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetBufferCount(_ queue: CMBufferQueue!) -> CMItemCount ``` |
| To | ``` func CMBufferQueueGetBufferCount(_ queue: CMBufferQueue) -> CMItemCount ``` |

Modified [CMBufferQueueGetDuration(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489766-cmbufferqueuegetduration)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetDuration(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetDuration(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetEndPresentationTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489229-cmbufferqueuegetendpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetEndPresentationTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetEndPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetFirstDecodeTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489487-cmbufferqueuegetfirstdecodetimes)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetFirstDecodeTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetFirstDecodeTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetFirstPresentationTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489143-cmbufferqueuegetfirstpresentatio)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetFirstPresentationTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetFirstPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetHead(_: CMBufferQueue) -> CMBuffer?](https://developer.apple.com/documentation/coremedia/1489558-cmbufferqueuegethead)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetHead(_ queue: CMBufferQueue!) -> Unmanaged<CMBuffer>! ``` |
| To | ``` func CMBufferQueueGetHead(_ queue: CMBufferQueue) -> CMBuffer? ``` |

Modified [CMBufferQueueGetMaxPresentationTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489685-cmbufferqueuegetmaxpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetMaxPresentationTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetMaxPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetMinDecodeTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489486-cmbufferqueuegetmindecodetimesta)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetMinDecodeTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetMinDecodeTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetMinPresentationTimeStamp(_: CMBufferQueue) -> CMTime](https://developer.apple.com/documentation/coremedia/1489317-cmbufferqueuegetminpresentationt)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetMinPresentationTimeStamp(_ queue: CMBufferQueue!) -> CMTime ``` |
| To | ``` func CMBufferQueueGetMinPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime ``` |

Modified [CMBufferQueueGetTotalSize(_: CMBufferQueue) -> Int](https://developer.apple.com/documentation/coremedia/1489793-cmbufferqueuegettotalsize)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue!) -> Int ``` |
| To | ``` func CMBufferQueueGetTotalSize(_ queue: CMBufferQueue) -> Int ``` |

Modified [CMBufferQueueInstallTrigger(_: CMBufferQueue, _: CMBufferQueueTriggerCallback?, _: UnsafeMutablePointer<Void>, _: CMBufferQueueTriggerCondition, _: CMTime, _: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489822-cmbufferqueueinstalltrigger)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |
| To | ``` func CMBufferQueueInstallTrigger(_ queue: CMBufferQueue, _ triggerCallback: CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerTime: CMTime, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |

Modified [CMBufferQueueInstallTriggerWithIntegerThreshold(_: CMBufferQueue, _: CMBufferQueueTriggerCallback?, _: UnsafeMutablePointer<Void>, _: CMBufferQueueTriggerCondition, _: CMItemCount, _: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489140-cmbufferqueueinstalltriggerwithi)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue!, _ triggerCallback: CMBufferQueueTriggerCallback, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |
| To | ``` func CMBufferQueueInstallTriggerWithIntegerThreshold(_ queue: CMBufferQueue, _ triggerCallback: CMBufferQueueTriggerCallback?, _ triggerRefcon: UnsafeMutablePointer<Void>, _ triggerCondition: CMBufferQueueTriggerCondition, _ triggerThreshold: CMItemCount, _ triggerTokenOut: UnsafeMutablePointer<CMBufferQueueTriggerToken>) -> OSStatus ``` |

Modified [CMBufferQueueIsAtEndOfData(_: CMBufferQueue) -> Bool](https://developer.apple.com/documentation/coremedia/1489131-cmbufferqueueisatendofdata)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueIsAtEndOfData(_ queue: CMBufferQueue!) -> Boolean ``` |
| To | ``` func CMBufferQueueIsAtEndOfData(_ queue: CMBufferQueue) -> Bool ``` |

Modified [CMBufferQueueIsEmpty(_: CMBufferQueue) -> Bool](https://developer.apple.com/documentation/coremedia/1489479-cmbufferqueueisempty)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueIsEmpty(_ queue: CMBufferQueue!) -> Boolean ``` |
| To | ``` func CMBufferQueueIsEmpty(_ queue: CMBufferQueue) -> Bool ``` |

Modified [CMBufferQueueMarkEndOfData(_: CMBufferQueue) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489584-cmbufferqueuemarkendofdata)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueMarkEndOfData(_ queue: CMBufferQueue!) -> OSStatus ``` |
| To | ``` func CMBufferQueueMarkEndOfData(_ queue: CMBufferQueue) -> OSStatus ``` |

Modified [CMBufferQueueRemoveTrigger(_: CMBufferQueue, _: CMBufferQueueTriggerToken) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489445-cmbufferqueueremovetrigger)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueRemoveTrigger(_ queue: CMBufferQueue!, _ triggerToken: CMBufferQueueTriggerToken) -> OSStatus ``` |
| To | ``` func CMBufferQueueRemoveTrigger(_ queue: CMBufferQueue, _ triggerToken: CMBufferQueueTriggerToken) -> OSStatus ``` |

Modified [CMBufferQueueReset(_: CMBufferQueue) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489291-cmbufferqueuereset)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueReset(_ queue: CMBufferQueue!) -> OSStatus ``` |
| To | ``` func CMBufferQueueReset(_ queue: CMBufferQueue) -> OSStatus ``` |

Modified [CMBufferQueueResetWithCallback(_: CMBufferQueue, _: (CMBuffer, UnsafeMutablePointer<Void>) -> Void, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489361-cmbufferqueueresetwithcallback)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue!, _ callback: CFunctionPointer<((CMBuffer!, UnsafeMutablePointer<Void>) -> Void)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueResetWithCallback(_ queue: CMBufferQueue, _ callback: (CMBuffer, UnsafeMutablePointer<Void>) -> Void, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMBufferQueueSetValidationCallback(_: CMBufferQueue, _: CMBufferValidationCallback, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489350-cmbufferqueuesetvalidationcallba)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue!, _ validationCallback: CMBufferValidationCallback, _ validationRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, _ validationCallback: CMBufferValidationCallback, _ validationRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMBufferQueueTestTrigger(_: CMBufferQueue, _: CMBufferQueueTriggerToken) -> Bool](https://developer.apple.com/documentation/coremedia/1489135-cmbufferqueuetesttrigger)

|  | Declaration |
| --- | --- |
| From | ``` func CMBufferQueueTestTrigger(_ queue: CMBufferQueue!, _ triggerToken: CMBufferQueueTriggerToken) -> Boolean ``` |
| To | ``` func CMBufferQueueTestTrigger(_ queue: CMBufferQueue, _ triggerToken: CMBufferQueueTriggerToken) -> Bool ``` |

Modified [CMBufferQueueTriggerCallback](https://developer.apple.com/documentation/coremedia/cmbufferqueuetriggercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferQueueTriggerCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CMBufferQueueTriggerToken) -> Void)> ``` |
| To | ``` typealias CMBufferQueueTriggerCallback = (UnsafeMutablePointer<Void>, CMBufferQueueTriggerToken) -> Void ``` |

Modified [CMBufferValidationCallback](https://developer.apple.com/documentation/coremedia/cmbuffervalidationcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMBufferValidationCallback = CFunctionPointer<((CMBufferQueue!, CMBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias CMBufferValidationCallback = (CMBufferQueue, CMBuffer, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMClockGetAnchorTime(_: CMClock, _: UnsafeMutablePointer<CMTime>, _: UnsafeMutablePointer<CMTime>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489299-cmclockgetanchortime)

|  | Declaration |
| --- | --- |
| From | ``` func CMClockGetAnchorTime(_ clock: CMClock!, _ outClockTime: UnsafeMutablePointer<CMTime>, _ outReferenceClockTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` |
| To | ``` func CMClockGetAnchorTime(_ clock: CMClock, _ outClockTime: UnsafeMutablePointer<CMTime>, _ outReferenceClockTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` |

Modified [CMClockGetHostTimeClock() -> CMClock](https://developer.apple.com/documentation/coremedia/1489402-cmclockgethosttimeclock)

|  | Declaration |
| --- | --- |
| From | ``` func CMClockGetHostTimeClock() -> CMClock! ``` |
| To | ``` func CMClockGetHostTimeClock() -> CMClock ``` |

Modified [CMClockGetTime(_: CMClock) -> CMTime](https://developer.apple.com/documentation/coremedia/1489382-cmclockgettime)

|  | Declaration |
| --- | --- |
| From | ``` func CMClockGetTime(_ clock: CMClock!) -> CMTime ``` |
| To | ``` func CMClockGetTime(_ clock: CMClock) -> CMTime ``` |

Modified [CMClockInvalidate(_: CMClock)](https://developer.apple.com/documentation/coremedia/1489202-cmclockinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func CMClockInvalidate(_ clock: CMClock!) ``` |
| To | ``` func CMClockInvalidate(_ clock: CMClock) ``` |

Modified [CMClockMightDrift(_: CMClock, _: CMClock) -> Bool](https://developer.apple.com/documentation/coremedia/1489494-cmclockmightdrift)

|  | Declaration |
| --- | --- |
| From | ``` func CMClockMightDrift(_ clock: CMClock!, _ otherClock: CMClock!) -> Boolean ``` |
| To | ``` func CMClockMightDrift(_ clock: CMClock, _ otherClock: CMClock) -> Bool ``` |

Modified [CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(_: CFAllocator?, _: CMClosedCaptionFormatDescription, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416313-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionFormatDescription: CMClosedCaptionFormatDescription!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator?, _ closedCaptionFormatDescription: CMClosedCaptionFormatDescription, _ closedCaptionDescriptionFlavor: CFString?, _ closedCaptionDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFString?, _: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416291-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator!, _ closedCaptionDescriptionBlockBuffer: CMBlockBuffer!, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer(_ allocator: CFAllocator?, _ closedCaptionDescriptionBlockBuffer: CMBlockBuffer, _ closedCaptionDescriptionFlavor: CFString?, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus ``` |

Modified [CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFString?, _: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416295-cmclosedcaptionformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator!, _ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: Int, _ closedCaptionDescriptionFlavor: CFString!, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMClosedCaptionFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData(_ allocator: CFAllocator?, _ closedCaptionDescriptionData: UnsafePointer<UInt8>, _ closedCaptionDescriptionSize: Int, _ closedCaptionDescriptionFlavor: CFString?, _ closedCaptionFormatDescriptionOut: UnsafeMutablePointer<CMClosedCaptionFormatDescription?>) -> OSStatus ``` |

Modified [CMCopyDictionaryOfAttachments(_: CFAllocator?, _: CMAttachmentBearer, _: CMAttachmentMode) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1470699-cmcopydictionaryofattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CMCopyDictionaryOfAttachments(_ allocator: CFAllocator!, _ target: CMAttachmentBearer!, _ attachmentMode: CMAttachmentMode) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CMCopyDictionaryOfAttachments(_ allocator: CFAllocator?, _ target: CMAttachmentBearer, _ attachmentMode: CMAttachmentMode) -> CFDictionary? ``` |

Modified [CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout(_: CMBlockBuffer, _: CFString?) -> Bool](https://developer.apple.com/documentation/coremedia/1416317-cmdoesbigendiansounddescriptionr)

|  | Declaration |
| --- | --- |
| From | ``` func CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout(_ soundDescriptionBlockBuffer: CMBlockBuffer!, _ soundDescriptionFlavor: CFString!) -> Boolean ``` |
| To | ``` func CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout(_ soundDescriptionBlockBuffer: CMBlockBuffer, _ soundDescriptionFlavor: CFString?) -> Bool ``` |

Modified [CMFormatDescriptionCreate(_: CFAllocator?, _: CMMediaType, _: FourCharCode, _: CFDictionary?, _: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489182-cmformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionCreate(_ allocator: CFAllocator!, _ mediaType: CMMediaType, _ mediaSubtype: FourCharCode, _ extensions: CFDictionary!, _ descOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMFormatDescriptionCreate(_ allocator: CFAllocator?, _ mediaType: CMMediaType, _ mediaSubtype: FourCharCode, _ extensions: CFDictionary?, _ descOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus ``` |

Modified [CMFormatDescriptionEqual(_: CMFormatDescription?, _: CMFormatDescription?) -> Bool](https://developer.apple.com/documentation/coremedia/1489825-cmformatdescriptionequal)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionEqual(_ desc1: CMFormatDescription!, _ desc2: CMFormatDescription!) -> Boolean ``` |
| To | ``` func CMFormatDescriptionEqual(_ desc1: CMFormatDescription?, _ desc2: CMFormatDescription?) -> Bool ``` |

Modified [CMFormatDescriptionEqualIgnoringExtensionKeys(_: CMFormatDescription?, _: CMFormatDescription?, _: AnyObject?, _: AnyObject?) -> Bool](https://developer.apple.com/documentation/coremedia/1489465-cmformatdescriptionequalignoring)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionEqualIgnoringExtensionKeys(_ desc1: CMFormatDescription!, _ desc2: CMFormatDescription!, _ formatDescriptionExtensionKeysToIgnore: AnyObject!, _ sampleDescriptionExtensionAtomKeysToIgnore: AnyObject!) -> Boolean ``` |
| To | ``` func CMFormatDescriptionEqualIgnoringExtensionKeys(_ desc1: CMFormatDescription?, _ desc2: CMFormatDescription?, _ formatDescriptionExtensionKeysToIgnore: AnyObject?, _ sampleDescriptionExtensionAtomKeysToIgnore: AnyObject?) -> Bool ``` |

Modified [CMFormatDescriptionGetExtension(_: CMFormatDescription, _: CFString) -> CFPropertyList?](https://developer.apple.com/documentation/coremedia/1489750-cmformatdescriptiongetextension)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionGetExtension(_ desc: CMFormatDescription!, _ extensionKey: CFString!) -> Unmanaged<CFPropertyList>! ``` |
| To | ``` func CMFormatDescriptionGetExtension(_ desc: CMFormatDescription, _ extensionKey: CFString) -> CFPropertyList? ``` |

Modified [CMFormatDescriptionGetExtensions(_: CMFormatDescription) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1489170-cmformatdescriptiongetextensions)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionGetExtensions(_ desc: CMFormatDescription!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CMFormatDescriptionGetExtensions(_ desc: CMFormatDescription) -> CFDictionary? ``` |

Modified [CMFormatDescriptionGetMediaSubType(_: CMFormatDescription) -> FourCharCode](https://developer.apple.com/documentation/coremedia/1489255-cmformatdescriptiongetmediasubty)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionGetMediaSubType(_ desc: CMFormatDescription!) -> FourCharCode ``` |
| To | ``` func CMFormatDescriptionGetMediaSubType(_ desc: CMFormatDescription) -> FourCharCode ``` |

Modified [CMFormatDescriptionGetMediaType(_: CMFormatDescription) -> CMMediaType](https://developer.apple.com/documentation/coremedia/1489174-cmformatdescriptiongetmediatype)

|  | Declaration |
| --- | --- |
| From | ``` func CMFormatDescriptionGetMediaType(_ desc: CMFormatDescription!) -> CMMediaType ``` |
| To | ``` func CMFormatDescriptionGetMediaType(_ desc: CMFormatDescription) -> CMMediaType ``` |

Modified [CMGetAttachment(_: CMAttachmentBearer, _: CFString, _: UnsafeMutablePointer<CMAttachmentMode>) -> AnyObject?](https://developer.apple.com/documentation/coremedia/1470707-cmgetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CMGetAttachment(_ target: CMAttachmentBearer!, _ key: CFString!, _ attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>) -> Unmanaged<AnyObject>! ``` |
| To | ``` func CMGetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>) -> AnyObject? ``` |

Modified [CMMemoryPoolCreate(_: CFDictionary?) -> CMMemoryPool](https://developer.apple.com/documentation/coremedia/1489395-cmmemorypoolcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMMemoryPoolCreate(_ options: CFDictionary!) -> Unmanaged<CMMemoryPool>! ``` |
| To | ``` func CMMemoryPoolCreate(_ options: CFDictionary?) -> CMMemoryPool ``` |

Modified [CMMemoryPoolFlush(_: CMMemoryPool)](https://developer.apple.com/documentation/coremedia/1489661-cmmemorypoolflush)

|  | Declaration |
| --- | --- |
| From | ``` func CMMemoryPoolFlush(_ pool: CMMemoryPool!) ``` |
| To | ``` func CMMemoryPoolFlush(_ pool: CMMemoryPool) ``` |

Modified [CMMemoryPoolGetAllocator(_: CMMemoryPool) -> CFAllocator](https://developer.apple.com/documentation/coremedia/1489675-cmmemorypoolgetallocator)

|  | Declaration |
| --- | --- |
| From | ``` func CMMemoryPoolGetAllocator(_ pool: CMMemoryPool!) -> Unmanaged<CFAllocator>! ``` |
| To | ``` func CMMemoryPoolGetAllocator(_ pool: CMMemoryPool) -> CFAllocator ``` |

Modified [CMMemoryPoolInvalidate(_: CMMemoryPool)](https://developer.apple.com/documentation/coremedia/1489674-cmmemorypoolinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func CMMemoryPoolInvalidate(_ pool: CMMemoryPool!) ``` |
| To | ``` func CMMemoryPoolInvalidate(_ pool: CMMemoryPool) ``` |

Modified [CMMetadataCreateIdentifierForKeyAndKeySpace(_: CFAllocator?, _: AnyObject, _: CFString, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1474037-cmmetadatacreateidentifierforkey)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator!, _ key: AnyObject!, _ keySpace: CFString!, _ identifierOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateIdentifierForKeyAndKeySpace(_ allocator: CFAllocator?, _ key: AnyObject, _ keySpace: CFString, _ identifierOut: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [CMMetadataCreateKeyFromIdentifier(_: CFAllocator?, _: CFString, _: UnsafeMutablePointer<AnyObject?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1474086-cmmetadatacreatekeyfromidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafeMutablePointer<Unmanaged<AnyObject>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeyFromIdentifier(_ allocator: CFAllocator?, _ identifier: CFString, _ keyOut: UnsafeMutablePointer<AnyObject?>) -> OSStatus ``` |

Modified [CMMetadataCreateKeyFromIdentifierAsCFData(_: CFAllocator?, _: CFString, _: UnsafeMutablePointer<CFData?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1473974-cmmetadatacreatekeyfromidentifie)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeyFromIdentifierAsCFData(_ allocator: CFAllocator!, _ identifier: CFString!, _ keyOut: UnsafeMutablePointer<Unmanaged<CFData>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeyFromIdentifierAsCFData(_ allocator: CFAllocator?, _ identifier: CFString, _ keyOut: UnsafeMutablePointer<CFData?>) -> OSStatus ``` |

Modified [CMMetadataCreateKeySpaceFromIdentifier(_: CFAllocator?, _: CFString, _: UnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1474002-cmmetadatacreatekeyspacefromiden)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataCreateKeySpaceFromIdentifier(_ allocator: CFAllocator!, _ identifier: CFString!, _ keySpaceOut: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMMetadataCreateKeySpaceFromIdentifier(_ allocator: CFAllocator?, _ identifier: CFString, _ keySpaceOut: UnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [CMMetadataDataTypeRegistryDataTypeConformsToDataType(_: CFString, _: CFString) -> Bool](https://developer.apple.com/documentation/coremedia/1474024-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryDataTypeConformsToDataType(_ dataType: CFString!, _ conformsToDataType: CFString!) -> Boolean ``` |
| To | ``` func CMMetadataDataTypeRegistryDataTypeConformsToDataType(_ dataType: CFString, _ conformsToDataType: CFString) -> Bool ``` |

Modified [CMMetadataDataTypeRegistryDataTypeIsBaseDataType(_: CFString) -> Bool](https://developer.apple.com/documentation/coremedia/1473980-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(_ dataType: CFString!) -> Boolean ``` |
| To | ``` func CMMetadataDataTypeRegistryDataTypeIsBaseDataType(_ dataType: CFString) -> Bool ``` |

Modified [CMMetadataDataTypeRegistryDataTypeIsRegistered(_: CFString) -> Bool](https://developer.apple.com/documentation/coremedia/1473986-cmmetadatadatatyperegistrydataty)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryDataTypeIsRegistered(_ dataType: CFString!) -> Boolean ``` |
| To | ``` func CMMetadataDataTypeRegistryDataTypeIsRegistered(_ dataType: CFString) -> Bool ``` |

Modified [CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(_: CFString) -> CFString](https://developer.apple.com/documentation/coremedia/1474035-cmmetadatadatatyperegistrygetbas)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(_ dataType: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func CMMetadataDataTypeRegistryGetBaseDataTypeForConformingDataType(_ dataType: CFString) -> CFString ``` |

Modified [CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray?](https://developer.apple.com/documentation/coremedia/1473994-cmmetadatadatatyperegistrygetbas)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryGetBaseDataTypes() -> Unmanaged<CFArray>! ``` |
| To | ``` func CMMetadataDataTypeRegistryGetBaseDataTypes() -> CFArray? ``` |

Modified [CMMetadataDataTypeRegistryGetConformingDataTypes(_: CFString) -> CFArray](https://developer.apple.com/documentation/coremedia/1473964-cmmetadatadatatyperegistrygetcon)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryGetConformingDataTypes(_ dataType: CFString!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CMMetadataDataTypeRegistryGetConformingDataTypes(_ dataType: CFString) -> CFArray ``` |

Modified [CMMetadataDataTypeRegistryGetDataTypeDescription(_: CFString) -> CFString](https://developer.apple.com/documentation/coremedia/1474041-cmmetadatadatatyperegistrygetdat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryGetDataTypeDescription(_ dataType: CFString!) -> Unmanaged<CFString>! ``` |
| To | ``` func CMMetadataDataTypeRegistryGetDataTypeDescription(_ dataType: CFString) -> CFString ``` |

Modified [CMMetadataDataTypeRegistryRegisterDataType(_: CFString, _: CFString, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/coremedia/1473992-cmmetadatadatatyperegistryregist)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataDataTypeRegistryRegisterDataType(_ dataType: CFString!, _ description: CFString!, _ conformingDataTypes: CFArray!) -> OSStatus ``` |
| To | ``` func CMMetadataDataTypeRegistryRegisterDataType(_ dataType: CFString, _ description: CFString, _ conformingDataTypes: CFArray) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(_: CFAllocator?, _: CMMetadataFormatDescription, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416249-cmmetadataformatdescriptioncopya)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataFormatDescription: CMMetadataFormatDescription!, _ metadataDescriptionFlavor: CFString!, _ metadataDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator?, _ metadataFormatDescription: CMMetadataFormatDescription, _ metadataDescriptionFlavor: CFString?, _ metadataDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(_: CFAllocator?, _: CMMetadataFormatDescription, _: CMMetadataFormatDescription, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489346-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(_ allocator: CFAllocator!, _ srcDesc1: CMMetadataFormatDescription!, _ srcDesc2: CMMetadataFormatDescription!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateByMergingMetadataFormatDescriptions(_ allocator: CFAllocator?, _ srcDesc1: CMMetadataFormatDescription, _ srcDesc2: CMMetadataFormatDescription, _ outDesc: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFString?, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416301-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator!, _ metadataDescriptionBlockBuffer: CMBlockBuffer!, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer(_ allocator: CFAllocator?, _ metadataDescriptionBlockBuffer: CMBlockBuffer, _ metadataDescriptionFlavor: CFString?, _ metadataFormatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFString?, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416265-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator!, _ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: Int, _ metadataDescriptionFlavor: CFString!, _ metadataFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData(_ allocator: CFAllocator?, _ metadataDescriptionData: UnsafePointer<UInt8>, _ metadataDescriptionSize: Int, _ metadataDescriptionFlavor: CFString?, _ metadataFormatDescriptionOut: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateWithKeys(_: CFAllocator?, _: CMMetadataFormatType, _: CFArray?, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489719-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithKeys(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ keys: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateWithKeys(_ allocator: CFAllocator?, _ metadataType: CMMetadataFormatType, _ keys: CFArray?, _ outDesc: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(_: CFAllocator?, _: CMMetadataFormatDescription, _: CFArray, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489454-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(_ allocator: CFAllocator!, _ srcDesc: CMMetadataFormatDescription!, _ metadataSpecifications: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications(_ allocator: CFAllocator?, _ srcDesc: CMMetadataFormatDescription, _ metadataSpecifications: CFArray, _ outDesc: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionCreateWithMetadataSpecifications(_: CFAllocator?, _: CMMetadataFormatType, _: CFArray, _: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489368-cmmetadataformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(_ allocator: CFAllocator!, _ metadataType: CMMetadataFormatType, _ metadataSpecifications: CFArray!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMetadataFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMetadataFormatDescriptionCreateWithMetadataSpecifications(_ allocator: CFAllocator?, _ metadataType: CMMetadataFormatType, _ metadataSpecifications: CFArray, _ outDesc: UnsafeMutablePointer<CMMetadataFormatDescription?>) -> OSStatus ``` |

Modified [CMMetadataFormatDescriptionGetIdentifiers(_: CMMetadataFormatDescription) -> CFArray?](https://developer.apple.com/documentation/coremedia/1489457-cmmetadataformatdescriptiongetid)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionGetIdentifiers(_ desc: CMMetadataFormatDescription!) -> Unmanaged<CFArray>! ``` |
| To | ``` func CMMetadataFormatDescriptionGetIdentifiers(_ desc: CMMetadataFormatDescription) -> CFArray? ``` |

Modified [CMMetadataFormatDescriptionGetKeyWithLocalID(_: CMMetadataFormatDescription, _: OSType) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1489196-cmmetadataformatdescriptiongetke)

|  | Declaration |
| --- | --- |
| From | ``` func CMMetadataFormatDescriptionGetKeyWithLocalID(_ desc: CMMetadataFormatDescription!, _ localKeyID: OSType) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func CMMetadataFormatDescriptionGetKeyWithLocalID(_ desc: CMMetadataFormatDescription, _ localKeyID: OSType) -> CFDictionary? ``` |

Modified [CMMuxedFormatDescriptionCreate(_: CFAllocator?, _: CMMuxedStreamType, _: CFDictionary?, _: UnsafeMutablePointer<CMMuxedFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489271-cmmuxedformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMMuxedFormatDescriptionCreate(_ allocator: CFAllocator!, _ muxType: CMMuxedStreamType, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMMuxedFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMMuxedFormatDescriptionCreate(_ allocator: CFAllocator?, _ muxType: CMMuxedStreamType, _ extensions: CFDictionary?, _ outDesc: UnsafeMutablePointer<CMMuxedFormatDescription?>) -> OSStatus ``` |

Modified [CMPropagateAttachments(_: CMAttachmentBearer, _: CMAttachmentBearer)](https://developer.apple.com/documentation/coremedia/1470701-cmpropagateattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CMPropagateAttachments(_ source: CMAttachmentBearer!, _ destination: CMAttachmentBearer!) ``` |
| To | ``` func CMPropagateAttachments(_ source: CMAttachmentBearer, _ destination: CMAttachmentBearer) ``` |

Modified [CMRemoveAllAttachments(_: CMAttachmentBearer)](https://developer.apple.com/documentation/coremedia/1470705-cmremoveallattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CMRemoveAllAttachments(_ target: CMAttachmentBearer!) ``` |
| To | ``` func CMRemoveAllAttachments(_ target: CMAttachmentBearer) ``` |

Modified [CMRemoveAttachment(_: CMAttachmentBearer, _: CFString)](https://developer.apple.com/documentation/coremedia/1470692-cmremoveattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CMRemoveAttachment(_ target: CMAttachmentBearer!, _ key: CFString!) ``` |
| To | ``` func CMRemoveAttachment(_ target: CMAttachmentBearer, _ key: CFString) ``` |

Modified [CMSampleBufferCallBlockForEachSample(_: CMSampleBuffer, _: (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489374-cmsamplebuffercallblockforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCallBlockForEachSample(_ sbuf: CMSampleBuffer!, _ handler: ((CMSampleBuffer!, CMItemCount) -> OSStatus)!) -> OSStatus ``` |
| To | ``` func CMSampleBufferCallBlockForEachSample(_ sbuf: CMSampleBuffer, _ handler: (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus ``` |

Modified [CMSampleBufferCallForEachSample(_: CMSampleBuffer, _: (CMSampleBuffer, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus, _: UnsafeMutablePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489563-cmsamplebuffercallforeachsample)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer!, _ callback: CFunctionPointer<((CMSampleBuffer!, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus)>, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCallForEachSample(_ sbuf: CMSampleBuffer, _ callback: (CMSampleBuffer, CMItemCount, UnsafeMutablePointer<Void>) -> OSStatus, _ refcon: UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMSampleBufferCopyPCMDataIntoAudioBufferList(_: CMSampleBuffer, _: Int32, _: Int32, _: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489200-cmsamplebuffercopypcmdataintoaud)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCopyPCMDataIntoAudioBufferList(_ sbuf: CMSampleBuffer!, _ frameOffset: Int32, _ numFrames: Int32, _ bufferList: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCopyPCMDataIntoAudioBufferList(_ sbuf: CMSampleBuffer, _ frameOffset: Int32, _ numFrames: Int32, _ bufferList: UnsafeMutablePointer<AudioBufferList>) -> OSStatus ``` |

Modified [CMSampleBufferCopySampleBufferForRange(_: CFAllocator?, _: CMSampleBuffer, _: CFRange, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489461-cmsamplebuffercopysamplebufferfo)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCopySampleBufferForRange(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sampleRange: CFRange, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCopySampleBufferForRange(_ allocator: CFAllocator?, _ sbuf: CMSampleBuffer, _ sampleRange: CFRange, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreate(_: CFAllocator?, _: CMBlockBuffer?, _: Bool, _: CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutablePointer<Void>, _: CMFormatDescription?, _: CMItemCount, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>, _: CMItemCount, _: UnsafePointer<Int>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489723-cmsamplebuffercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreate(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreate(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateCopy(_: CFAllocator?, _: CMSampleBuffer, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489543-cmsamplebuffercreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateCopy(_ allocator: CFAllocator!, _ sbuf: CMSampleBuffer!, _ sbufCopyOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateCopy(_ allocator: CFAllocator?, _ sbuf: CMSampleBuffer, _ sbufCopyOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateCopyWithNewTiming(_: CFAllocator?, _: CMSampleBuffer, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489645-cmsamplebuffercreatecopywithnewt)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator!, _ originalSBuf: CMSampleBuffer!, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ sBufCopyOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateCopyWithNewTiming(_ allocator: CFAllocator?, _ originalSBuf: CMSampleBuffer, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ sBufCopyOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateForImageBuffer(_: CFAllocator?, _: CVImageBuffer, _: Bool, _: CMSampleBufferMakeDataReadyCallback?, _: UnsafeMutablePointer<Void>, _: CMVideoFormatDescription, _: UnsafePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489414-cmsamplebuffercreateforimagebuff)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ dataReady: Boolean, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMVideoFormatDescription!, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateForImageBuffer(_ allocator: CFAllocator?, _ imageBuffer: CVImageBuffer, _ dataReady: Bool, _ makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, _ makeDataReadyRefcon: UnsafeMutablePointer<Void>, _ formatDescription: CMVideoFormatDescription, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateReady(_: CFAllocator?, _: CMBlockBuffer?, _: CMFormatDescription?, _: CMItemCount, _: CMItemCount, _: UnsafePointer<CMSampleTimingInfo>, _: CMItemCount, _: UnsafePointer<Int>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489513-cmsamplebuffercreateready)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator!, _ dataBuffer: CMBlockBuffer!, _ formatDescription: CMFormatDescription!, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateReady(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ formatDescription: CMFormatDescription?, _ numSamples: CMItemCount, _ numSampleTimingEntries: CMItemCount, _ sampleTimingArray: UnsafePointer<CMSampleTimingInfo>, _ numSampleSizeEntries: CMItemCount, _ sampleSizeArray: UnsafePointer<Int>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferCreateReadyWithImageBuffer(_: CFAllocator?, _: CVImageBuffer, _: CMVideoFormatDescription, _: UnsafePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489745-cmsamplebuffercreatereadywithima)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferCreateReadyWithImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ formatDescription: CMVideoFormatDescription!, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<Unmanaged<CMSampleBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferCreateReadyWithImageBuffer(_ allocator: CFAllocator?, _ imageBuffer: CVImageBuffer, _ formatDescription: CMVideoFormatDescription, _ sampleTiming: UnsafePointer<CMSampleTimingInfo>, _ sBufOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferDataIsReady(_: CMSampleBuffer) -> Bool](https://developer.apple.com/documentation/coremedia/1489694-cmsamplebufferdataisready)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferDataIsReady(_ sbuf: CMSampleBuffer!) -> Boolean ``` |
| To | ``` func CMSampleBufferDataIsReady(_ sbuf: CMSampleBuffer) -> Bool ``` |

Modified [CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_: CMSampleBuffer, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<AudioBufferList>, _: Int, _: CFAllocator?, _: CFAllocator?, _: UInt32, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489191-cmsamplebuffergetaudiobufferlist)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer!, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(_ sbuf: CMSampleBuffer, _ bufferListSizeNeededOut: UnsafeMutablePointer<Int>, _ bufferListOut: UnsafeMutablePointer<AudioBufferList>, _ bufferListSize: Int, _ bbufStructAllocator: CFAllocator?, _ bbufMemoryAllocator: CFAllocator?, _ flags: UInt32, _ blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptions(_: CMSampleBuffer, _: Int, _: UnsafeMutablePointer<AudioStreamPacketDescription>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489190-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer!, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptions(_ sbuf: CMSampleBuffer, _ packetDescriptionsSize: Int, _ packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>, _ packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_: CMSampleBuffer, _: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _: UnsafeMutablePointer<Int>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489564-cmsamplebuffergetaudiostreampack)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer!, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(_ sbuf: CMSampleBuffer, _ packetDescriptionsPtrOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>>, _ packetDescriptionsSizeOut: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified [CMSampleBufferGetDataBuffer(_: CMSampleBuffer) -> CMBlockBuffer?](https://developer.apple.com/documentation/coremedia/1489629-cmsamplebuffergetdatabuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetDataBuffer(_ sbuf: CMSampleBuffer!) -> CMBlockBuffer! ``` |
| To | ``` func CMSampleBufferGetDataBuffer(_ sbuf: CMSampleBuffer) -> CMBlockBuffer? ``` |

Modified [CMSampleBufferGetDecodeTimeStamp(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489404-cmsamplebuffergetdecodetimestamp)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetDecodeTimeStamp(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetDecodeTimeStamp(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetDuration(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489562-cmsamplebuffergetduration)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetDuration(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetDuration(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetFormatDescription(_: CMSampleBuffer) -> CMFormatDescription?](https://developer.apple.com/documentation/coremedia/1489185-cmsamplebuffergetformatdescripti)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetFormatDescription(_ sbuf: CMSampleBuffer!) -> CMFormatDescription! ``` |
| To | ``` func CMSampleBufferGetFormatDescription(_ sbuf: CMSampleBuffer) -> CMFormatDescription? ``` |

Modified [CMSampleBufferGetImageBuffer(_: CMSampleBuffer) -> CVImageBuffer?](https://developer.apple.com/documentation/coremedia/1489236-cmsamplebuffergetimagebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetImageBuffer(_ sbuf: CMSampleBuffer!) -> CVImageBuffer! ``` |
| To | ``` func CMSampleBufferGetImageBuffer(_ sbuf: CMSampleBuffer) -> CVImageBuffer? ``` |

Modified [CMSampleBufferGetNumSamples(_: CMSampleBuffer) -> CMItemCount](https://developer.apple.com/documentation/coremedia/1489399-cmsamplebuffergetnumsamples)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetNumSamples(_ sbuf: CMSampleBuffer!) -> CMItemCount ``` |
| To | ``` func CMSampleBufferGetNumSamples(_ sbuf: CMSampleBuffer) -> CMItemCount ``` |

Modified [CMSampleBufferGetOutputDecodeTimeStamp(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489742-cmsamplebuffergetoutputdecodetim)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetOutputDecodeTimeStamp(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetOutputDecodeTimeStamp(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetOutputDuration(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489237-cmsamplebuffergetoutputduration)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetOutputDuration(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetOutputDuration(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetOutputPresentationTimeStamp(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489655-cmsamplebuffergetoutputpresentat)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetOutputSampleTimingInfoArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMItemCount>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489380-cmsamplebuffergetoutputsampletim)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |

Modified [CMSampleBufferGetPresentationTimeStamp(_: CMSampleBuffer) -> CMTime](https://developer.apple.com/documentation/coremedia/1489252-cmsamplebuffergetpresentationtim)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetPresentationTimeStamp(_ sbuf: CMSampleBuffer!) -> CMTime ``` |
| To | ``` func CMSampleBufferGetPresentationTimeStamp(_ sbuf: CMSampleBuffer) -> CMTime ``` |

Modified [CMSampleBufferGetSampleAttachmentsArray(_: CMSampleBuffer, _: Bool) -> CFArray?](https://developer.apple.com/documentation/coremedia/1489189-cmsamplebuffergetsampleattachmen)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleAttachmentsArray(_ sbuf: CMSampleBuffer!, _ createIfNecessary: Boolean) -> CFArray! ``` |
| To | ``` func CMSampleBufferGetSampleAttachmentsArray(_ sbuf: CMSampleBuffer, _ createIfNecessary: Bool) -> CFArray? ``` |

Modified [CMSampleBufferGetSampleSize(_: CMSampleBuffer, _: CMItemIndex) -> Int](https://developer.apple.com/documentation/coremedia/1489210-cmsamplebuffergetsamplesize)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex) -> Int ``` |
| To | ``` func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer, _ sampleIndex: CMItemIndex) -> Int ``` |

Modified [CMSampleBufferGetSampleSizeArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<CMItemCount>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489295-cmsamplebuffergetsamplesizearray)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer!, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer, _ sizeArrayEntries: CMItemCount, _ sizeArrayOut: UnsafeMutablePointer<Int>, _ sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |

Modified [CMSampleBufferGetSampleTimingInfo(_: CMSampleBuffer, _: CMItemIndex, _: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489670-cmsamplebuffergetsampletiminginf)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleTimingInfo(_ sbuf: CMSampleBuffer!, _ sampleIndex: CMItemIndex, _ timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleTimingInfo(_ sbuf: CMSampleBuffer, _ sampleIndex: CMItemIndex, _ timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus ``` |

Modified [CMSampleBufferGetSampleTimingInfoArray(_: CMSampleBuffer, _: CMItemCount, _: UnsafeMutablePointer<CMSampleTimingInfo>, _: UnsafeMutablePointer<CMItemCount>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489652-cmsamplebuffergetsampletiminginf)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer!, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |
| To | ``` func CMSampleBufferGetSampleTimingInfoArray(_ sbuf: CMSampleBuffer, _ timingArrayEntries: CMItemCount, _ timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>, _ timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>) -> OSStatus ``` |

Modified [CMSampleBufferGetTotalSampleSize(_: CMSampleBuffer) -> Int](https://developer.apple.com/documentation/coremedia/1489481-cmsamplebuffergettotalsamplesize)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer!) -> Int ``` |
| To | ``` func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer) -> Int ``` |

Modified [CMSampleBufferHasDataFailed(_: CMSampleBuffer, _: UnsafeMutablePointer<OSStatus>) -> Bool](https://developer.apple.com/documentation/coremedia/1489503-cmsamplebufferhasdatafailed)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferHasDataFailed(_ sbuf: CMSampleBuffer!, _ statusOut: UnsafeMutablePointer<OSStatus>) -> Boolean ``` |
| To | ``` func CMSampleBufferHasDataFailed(_ sbuf: CMSampleBuffer, _ statusOut: UnsafeMutablePointer<OSStatus>) -> Bool ``` |

Modified [CMSampleBufferInvalidate(_: CMSampleBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489640-cmsamplebufferinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferInvalidate(_ sbuf: CMSampleBuffer!) -> OSStatus ``` |
| To | ``` func CMSampleBufferInvalidate(_ sbuf: CMSampleBuffer) -> OSStatus ``` |

Modified [CMSampleBufferInvalidateCallback](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferInvalidateCallback = CFunctionPointer<((CMSampleBuffer!, UInt64) -> Void)> ``` |
| To | ``` typealias CMSampleBufferInvalidateCallback = (CMSampleBuffer, UInt64) -> Void ``` |

Modified [CMSampleBufferInvalidateHandler](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferInvalidateHandler = (CMSampleBuffer!) -> Void ``` |
| To | ``` typealias CMSampleBufferInvalidateHandler = (CMSampleBuffer) -> Void ``` |

Modified [CMSampleBufferIsValid(_: CMSampleBuffer) -> Bool](https://developer.apple.com/documentation/coremedia/1489151-cmsamplebufferisvalid)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferIsValid(_ sbuf: CMSampleBuffer!) -> Boolean ``` |
| To | ``` func CMSampleBufferIsValid(_ sbuf: CMSampleBuffer) -> Bool ``` |

Modified [CMSampleBufferMakeDataReady(_: CMSampleBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489314-cmsamplebuffermakedataready)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferMakeDataReady(_ sbuf: CMSampleBuffer!) -> OSStatus ``` |
| To | ``` func CMSampleBufferMakeDataReady(_ sbuf: CMSampleBuffer) -> OSStatus ``` |

Modified [CMSampleBufferMakeDataReadyCallback](https://developer.apple.com/documentation/coremedia/cmsamplebuffermakedatareadycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMSampleBufferMakeDataReadyCallback = CFunctionPointer<((CMSampleBuffer!, UnsafeMutablePointer<Void>) -> OSStatus)> ``` |
| To | ``` typealias CMSampleBufferMakeDataReadyCallback = (CMSampleBuffer, UnsafeMutablePointer<Void>) -> OSStatus ``` |

Modified [CMSampleBufferSetDataBuffer(_: CMSampleBuffer, _: CMBlockBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489381-cmsamplebuffersetdatabuffer)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetDataBuffer(_ sbuf: CMSampleBuffer!, _ dataBuffer: CMBlockBuffer!) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetDataBuffer(_ sbuf: CMSampleBuffer, _ dataBuffer: CMBlockBuffer) -> OSStatus ``` |

Modified [CMSampleBufferSetDataBufferFromAudioBufferList(_: CMSampleBuffer, _: CFAllocator?, _: CFAllocator?, _: UInt32, _: UnsafePointer<AudioBufferList>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489725-cmsamplebuffersetdatabufferfroma)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetDataBufferFromAudioBufferList(_ sbuf: CMSampleBuffer!, _ bbufStructAllocator: CFAllocator!, _ bbufMemoryAllocator: CFAllocator!, _ flags: UInt32, _ bufferList: UnsafePointer<AudioBufferList>) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetDataBufferFromAudioBufferList(_ sbuf: CMSampleBuffer, _ bbufStructAllocator: CFAllocator?, _ bbufMemoryAllocator: CFAllocator?, _ flags: UInt32, _ bufferList: UnsafePointer<AudioBufferList>) -> OSStatus ``` |

Modified [CMSampleBufferSetDataFailed(_: CMSampleBuffer, _: OSStatus) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489697-cmsamplebuffersetdatafailed)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetDataFailed(_ sbuf: CMSampleBuffer!, _ status: OSStatus) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetDataFailed(_ sbuf: CMSampleBuffer, _ status: OSStatus) -> OSStatus ``` |

Modified [CMSampleBufferSetDataReady(_: CMSampleBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489482-cmsamplebuffersetdataready)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetDataReady(_ sbuf: CMSampleBuffer!) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetDataReady(_ sbuf: CMSampleBuffer) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateCallback(_: CMSampleBuffer, _: CMSampleBufferInvalidateCallback, _: UInt64) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489773-cmsamplebuffersetinvalidatecallb)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer!, _ invalidateCallback: CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, _ invalidateCallback: CMSampleBufferInvalidateCallback, _ invalidateRefCon: UInt64) -> OSStatus ``` |

Modified [CMSampleBufferSetInvalidateHandler(_: CMSampleBuffer, _: CMSampleBufferInvalidateHandler) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489256-cmsamplebuffersetinvalidatehandl)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer!, _ invalidateHandler: CMSampleBufferInvalidateHandler!) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, _ invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus ``` |

Modified [CMSampleBufferSetOutputPresentationTimeStamp(_: CMSampleBuffer, _: CMTime) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489442-cmsamplebuffersetoutputpresentat)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferSetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer!, _ outputPresentationTimeStamp: CMTime) -> OSStatus ``` |
| To | ``` func CMSampleBufferSetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer, _ outputPresentationTimeStamp: CMTime) -> OSStatus ``` |

Modified [CMSampleBufferTrackDataReadiness(_: CMSampleBuffer, _: CMSampleBuffer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489667-cmsamplebuffertrackdatareadiness)

|  | Declaration |
| --- | --- |
| From | ``` func CMSampleBufferTrackDataReadiness(_ sbuf: CMSampleBuffer!, _ sbufToTrack: CMSampleBuffer!) -> OSStatus ``` |
| To | ``` func CMSampleBufferTrackDataReadiness(_ sbuf: CMSampleBuffer, _ sbufToTrack: CMSampleBuffer) -> OSStatus ``` |

Modified [CMSetAttachment(_: CMAttachmentBearer, _: CFString, _: AnyObject?, _: CMAttachmentMode)](https://developer.apple.com/documentation/coremedia/1470696-cmsetattachment)

|  | Declaration |
| --- | --- |
| From | ``` func CMSetAttachment(_ target: CMAttachmentBearer!, _ key: CFString!, _ value: AnyObject!, _ attachmentMode: CMAttachmentMode) ``` |
| To | ``` func CMSetAttachment(_ target: CMAttachmentBearer, _ key: CFString, _ value: AnyObject?, _ attachmentMode: CMAttachmentMode) ``` |

Modified [CMSetAttachments(_: CMAttachmentBearer, _: CFDictionary, _: CMAttachmentMode)](https://developer.apple.com/documentation/coremedia/1470690-cmsetattachments)

|  | Declaration |
| --- | --- |
| From | ``` func CMSetAttachments(_ target: CMAttachmentBearer!, _ theAttachments: CFDictionary!, _ attachmentMode: CMAttachmentMode) ``` |
| To | ``` func CMSetAttachments(_ target: CMAttachmentBearer, _ theAttachments: CFDictionary, _ attachmentMode: CMAttachmentMode) ``` |

Modified [CMSimpleQueueCreate(_: CFAllocator?, _: Int32, _: UnsafeMutablePointer<CMSimpleQueue?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489641-cmsimplequeuecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueCreate(_ allocator: CFAllocator!, _ capacity: Int32, _ queueOut: UnsafeMutablePointer<Unmanaged<CMSimpleQueue>?>) -> OSStatus ``` |
| To | ``` func CMSimpleQueueCreate(_ allocator: CFAllocator?, _ capacity: Int32, _ queueOut: UnsafeMutablePointer<CMSimpleQueue?>) -> OSStatus ``` |

Modified [CMSimpleQueueDequeue(_: CMSimpleQueue) -> UnsafePointer<Void>](https://developer.apple.com/documentation/coremedia/1489820-cmsimplequeuedequeue)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue!) -> UnsafePointer<Void> ``` |
| To | ``` func CMSimpleQueueDequeue(_ queue: CMSimpleQueue) -> UnsafePointer<Void> ``` |

Modified [CMSimpleQueueEnqueue(_: CMSimpleQueue, _: UnsafePointer<Void>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489315-cmsimplequeueenqueue)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue!, _ element: UnsafePointer<Void>) -> OSStatus ``` |
| To | ``` func CMSimpleQueueEnqueue(_ queue: CMSimpleQueue, _ element: UnsafePointer<Void>) -> OSStatus ``` |

Modified [CMSimpleQueueGetCapacity(_: CMSimpleQueue) -> Int32](https://developer.apple.com/documentation/coremedia/1489168-cmsimplequeuegetcapacity)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueGetCapacity(_ queue: CMSimpleQueue!) -> Int32 ``` |
| To | ``` func CMSimpleQueueGetCapacity(_ queue: CMSimpleQueue) -> Int32 ``` |

Modified [CMSimpleQueueGetCount(_: CMSimpleQueue) -> Int32](https://developer.apple.com/documentation/coremedia/1489223-cmsimplequeuegetcount)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueGetCount(_ queue: CMSimpleQueue!) -> Int32 ``` |
| To | ``` func CMSimpleQueueGetCount(_ queue: CMSimpleQueue) -> Int32 ``` |

Modified [CMSimpleQueueGetHead(_: CMSimpleQueue) -> UnsafePointer<Void>](https://developer.apple.com/documentation/coremedia/1489410-cmsimplequeuegethead)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue!) -> UnsafePointer<Void> ``` |
| To | ``` func CMSimpleQueueGetHead(_ queue: CMSimpleQueue) -> UnsafePointer<Void> ``` |

Modified [CMSimpleQueueReset(_: CMSimpleQueue) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489224-cmsimplequeuereset)

|  | Declaration |
| --- | --- |
| From | ``` func CMSimpleQueueReset(_ queue: CMSimpleQueue!) -> OSStatus ``` |
| To | ``` func CMSimpleQueueReset(_ queue: CMSimpleQueue) -> OSStatus ``` |

Modified [CMSyncConvertTime(_: CMTime, _: CMClockOrTimebase, _: CMClockOrTimebase) -> CMTime](https://developer.apple.com/documentation/coremedia/1489632-cmsyncconverttime)

|  | Declaration |
| --- | --- |
| From | ``` func CMSyncConvertTime(_ time: CMTime, _ fromClockOrTimebase: CMClockOrTimebase!, _ toClockOrTimebase: CMClockOrTimebase!) -> CMTime ``` |
| To | ``` func CMSyncConvertTime(_ time: CMTime, _ fromClockOrTimebase: CMClockOrTimebase, _ toClockOrTimebase: CMClockOrTimebase) -> CMTime ``` |

Modified [CMSyncGetRelativeRate(_: CMClockOrTimebase, _: CMClockOrTimebase) -> Float64](https://developer.apple.com/documentation/coremedia/1489528-cmsyncgetrelativerate)

|  | Declaration |
| --- | --- |
| From | ``` func CMSyncGetRelativeRate(_ ofClockOrTimebase: CMClockOrTimebase!, _ relativeToClockOrTimebase: CMClockOrTimebase!) -> Float64 ``` |
| To | ``` func CMSyncGetRelativeRate(_ ofClockOrTimebase: CMClockOrTimebase, _ relativeToClockOrTimebase: CMClockOrTimebase) -> Float64 ``` |

Modified [CMSyncGetRelativeRateAndAnchorTime(_: CMClockOrTimebase, _: CMClockOrTimebase, _: UnsafeMutablePointer<Float64>, _: UnsafeMutablePointer<CMTime>, _: UnsafeMutablePointer<CMTime>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489570-cmsyncgetrelativerateandanchorti)

|  | Declaration |
| --- | --- |
| From | ``` func CMSyncGetRelativeRateAndAnchorTime(_ ofClockOrTimebase: CMClockOrTimebase!, _ relativeToClockOrTimebase: CMClockOrTimebase!, _ outRelativeRate: UnsafeMutablePointer<Float64>, _ outOfClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>, _ outRelativeToClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` |
| To | ``` func CMSyncGetRelativeRateAndAnchorTime(_ ofClockOrTimebase: CMClockOrTimebase, _ relativeToClockOrTimebase: CMClockOrTimebase, _ outRelativeRate: UnsafeMutablePointer<Float64>, _ outOfClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>, _ outRelativeToClockOrTimebaseAnchorTime: UnsafeMutablePointer<CMTime>) -> OSStatus ``` |

Modified [CMSyncGetTime(_: CMClockOrTimebase) -> CMTime](https://developer.apple.com/documentation/coremedia/1489233-cmsyncgettime)

|  | Declaration |
| --- | --- |
| From | ``` func CMSyncGetTime(_ clockOrTimebase: CMClockOrTimebase!) -> CMTime ``` |
| To | ``` func CMSyncGetTime(_ clockOrTimebase: CMClockOrTimebase) -> CMTime ``` |

Modified [CMSyncMightDrift(_: CMClockOrTimebase, _: CMClockOrTimebase) -> Bool](https://developer.apple.com/documentation/coremedia/1489610-cmsyncmightdrift)

|  | Declaration |
| --- | --- |
| From | ``` func CMSyncMightDrift(_ clockOrTimebase1: CMClockOrTimebase!, _ clockOrTimebase2: CMClockOrTimebase!) -> Boolean ``` |
| To | ``` func CMSyncMightDrift(_ clockOrTimebase1: CMClockOrTimebase, _ clockOrTimebase2: CMClockOrTimebase) -> Bool ``` |

Modified [CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(_: CFAllocator?, _: CMTextFormatDescription, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416246-cmtextformatdescriptioncopyasbig)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textFormatDescription: CMTextFormatDescription!, _ textDescriptionFlavor: CFString!, _ textDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator?, _ textFormatDescription: CMTextFormatDescription, _ textDescriptionFlavor: CFString?, _ textDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFString?, _: CMMediaType, _: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416283-cmtextformatdescriptioncreatefro)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator!, _ textDescriptionBlockBuffer: CMBlockBuffer!, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer(_ allocator: CFAllocator?, _ textDescriptionBlockBuffer: CMBlockBuffer, _ textDescriptionFlavor: CFString?, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFString?, _: CMMediaType, _: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416260-cmtextformatdescriptioncreatefro)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator!, _ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: Int, _ textDescriptionFlavor: CFString!, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTextFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData(_ allocator: CFAllocator?, _ textDescriptionData: UnsafePointer<UInt8>, _ textDescriptionSize: Int, _ textDescriptionFlavor: CFString?, _ mediaType: CMMediaType, _ textFormatDescriptionOut: UnsafeMutablePointer<CMTextFormatDescription?>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetDefaultStyle(_: CMFormatDescription, _: UnsafeMutablePointer<UInt16>, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<CGFloat>, _: UnsafeMutablePointer<CGFloat>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489145-cmtextformatdescriptiongetdefaul)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription!, _ outLocalFontID: UnsafeMutablePointer<UInt16>, _ outBold: UnsafeMutablePointer<Boolean>, _ outItalic: UnsafeMutablePointer<Boolean>, _ outUnderline: UnsafeMutablePointer<Boolean>, _ outFontSize: UnsafeMutablePointer<CGFloat>, _ outColorComponents: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetDefaultStyle(_ desc: CMFormatDescription, _ outLocalFontID: UnsafeMutablePointer<UInt16>, _ outBold: UnsafeMutablePointer<DarwinBoolean>, _ outItalic: UnsafeMutablePointer<DarwinBoolean>, _ outUnderline: UnsafeMutablePointer<DarwinBoolean>, _ outFontSize: UnsafeMutablePointer<CGFloat>, _ outColorComponents: UnsafeMutablePointer<CGFloat>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetDefaultTextBox(_: CMFormatDescription, _: Bool, _: CGFloat, _: UnsafeMutablePointer<CGRect>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489452-cmtextformatdescriptiongetdefaul)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetDefaultTextBox(_ desc: CMFormatDescription!, _ originIsAtTopLeft: Boolean, _ heightOfTextTrack: CGFloat, _ outDefaultTextBox: UnsafeMutablePointer<CGRect>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetDefaultTextBox(_ desc: CMFormatDescription, _ originIsAtTopLeft: Bool, _ heightOfTextTrack: CGFloat, _ outDefaultTextBox: UnsafeMutablePointer<CGRect>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetDisplayFlags(_: CMFormatDescription, _: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489707-cmtextformatdescriptiongetdispla)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetDisplayFlags(_ desc: CMFormatDescription!, _ outDisplayFlags: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetDisplayFlags(_ desc: CMFormatDescription, _ outDisplayFlags: UnsafeMutablePointer<CMTextDisplayFlags>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetFontName(_: CMFormatDescription, _: UInt16, _: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489704-cmtextformatdescriptiongetfontna)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetFontName(_ desc: CMFormatDescription!, _ localFontID: UInt16, _ outFontName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetFontName(_ desc: CMFormatDescription, _ localFontID: UInt16, _ outFontName: AutoreleasingUnsafeMutablePointer<CFString?>) -> OSStatus ``` |

Modified [CMTextFormatDescriptionGetJustification(_: CMFormatDescription, _: UnsafeMutablePointer<CMTextJustificationValue>, _: UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489232-cmtextformatdescriptiongetjustif)

|  | Declaration |
| --- | --- |
| From | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription!, _ outHorizontalJust: UnsafeMutablePointer<CMTextJustificationValue>, _ outVerticalJust: UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus ``` |
| To | ``` func CMTextFormatDescriptionGetJustification(_ desc: CMFormatDescription, _ outHorizontalJust: UnsafeMutablePointer<CMTextJustificationValue>, _ outVerticalJust: UnsafeMutablePointer<CMTextJustificationValue>) -> OSStatus ``` |

Modified [CMTimebaseAddTimer(_: CMTimebase, _: CFRunLoopTimer, _: CFRunLoop) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489654-cmtimebaseaddtimer)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseAddTimer(_ timebase: CMTimebase!, _ timer: CFRunLoopTimer!, _ runloop: CFRunLoop!) -> OSStatus ``` |
| To | ``` func CMTimebaseAddTimer(_ timebase: CMTimebase, _ timer: CFRunLoopTimer, _ runloop: CFRunLoop) -> OSStatus ``` |

Modified [CMTimebaseAddTimerDispatchSource(_: CMTimebase, _: dispatch_source_t) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489429-cmtimebaseaddtimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseAddTimerDispatchSource(_ timebase: CMTimebase!, _ timerSource: dispatch_source_t!) -> OSStatus ``` |
| To | ``` func CMTimebaseAddTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |

Modified [CMTimebaseCreateWithMasterClock(_: CFAllocator?, _: CMClock, _: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489367-cmtimebasecreatewithmasterclock)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseCreateWithMasterClock(_ allocator: CFAllocator!, _ masterClock: CMClock!, _ timebaseOut: UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` |
| To | ``` func CMTimebaseCreateWithMasterClock(_ allocator: CFAllocator?, _ masterClock: CMClock, _ timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus ``` |

Modified [CMTimebaseCreateWithMasterTimebase(_: CFAllocator?, _: CMTimebase, _: UnsafeMutablePointer<CMTimebase?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489132-cmtimebasecreatewithmastertimeba)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseCreateWithMasterTimebase(_ allocator: CFAllocator!, _ masterTimebase: CMTimebase!, _ timebaseOut: UnsafeMutablePointer<Unmanaged<CMTimebase>?>) -> OSStatus ``` |
| To | ``` func CMTimebaseCreateWithMasterTimebase(_ allocator: CFAllocator?, _ masterTimebase: CMTimebase, _ timebaseOut: UnsafeMutablePointer<CMTimebase?>) -> OSStatus ``` |

Modified [CMTimebaseGetEffectiveRate(_: CMTimebase) -> Float64](https://developer.apple.com/documentation/coremedia/1489313-cmtimebasegeteffectiverate)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseGetEffectiveRate(_ timebase: CMTimebase!) -> Float64 ``` |
| To | ``` func CMTimebaseGetEffectiveRate(_ timebase: CMTimebase) -> Float64 ``` |

Modified [CMTimebaseGetMaster(_: CMTimebase) -> CMClockOrTimebase?](https://developer.apple.com/documentation/coremedia/1489764-cmtimebasegetmaster)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMaster(_ timebase: CMTimebase!) -> CMClockOrTimebase! ``` | -- |
| To | ``` func CMTimebaseGetMaster(_ timebase: CMTimebase) -> CMClockOrTimebase? ``` | iOS 9.0 |

Modified [CMTimebaseGetMasterClock(_: CMTimebase) -> CMClock?](https://developer.apple.com/documentation/coremedia/1489691-cmtimebasegetmasterclock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMasterClock(_ timebase: CMTimebase!) -> CMClock! ``` | -- |
| To | ``` func CMTimebaseGetMasterClock(_ timebase: CMTimebase) -> CMClock? ``` | iOS 9.0 |

Modified [CMTimebaseGetMasterTimebase(_: CMTimebase) -> CMTimebase?](https://developer.apple.com/documentation/coremedia/1489484-cmtimebasegetmastertimebase)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CMTimebaseGetMasterTimebase(_ timebase: CMTimebase!) -> CMTimebase! ``` | -- |
| To | ``` func CMTimebaseGetMasterTimebase(_ timebase: CMTimebase) -> CMTimebase? ``` | iOS 9.0 |

Modified [CMTimebaseGetRate(_: CMTimebase) -> Float64](https://developer.apple.com/documentation/coremedia/1489302-cmtimebasegetrate)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseGetRate(_ timebase: CMTimebase!) -> Float64 ``` |
| To | ``` func CMTimebaseGetRate(_ timebase: CMTimebase) -> Float64 ``` |

Modified [CMTimebaseGetTime(_: CMTimebase) -> CMTime](https://developer.apple.com/documentation/coremedia/1489812-cmtimebasegettime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseGetTime(_ timebase: CMTimebase!) -> CMTime ``` |
| To | ``` func CMTimebaseGetTime(_ timebase: CMTimebase) -> CMTime ``` |

Modified [CMTimebaseGetTimeAndRate(_: CMTimebase, _: UnsafeMutablePointer<CMTime>, _: UnsafeMutablePointer<Float64>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489415-cmtimebasegettimeandrate)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseGetTimeAndRate(_ timebase: CMTimebase!, _ outTime: UnsafeMutablePointer<CMTime>, _ outRate: UnsafeMutablePointer<Float64>) -> OSStatus ``` |
| To | ``` func CMTimebaseGetTimeAndRate(_ timebase: CMTimebase, _ outTime: UnsafeMutablePointer<CMTime>, _ outRate: UnsafeMutablePointer<Float64>) -> OSStatus ``` |

Modified [CMTimebaseGetTimeWithTimeScale(_: CMTimebase, _: CMTimeScale, _: CMTimeRoundingMethod) -> CMTime](https://developer.apple.com/documentation/coremedia/1489700-cmtimebasegettimewithtimescale)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseGetTimeWithTimeScale(_ timebase: CMTimebase!, _ timescale: CMTimeScale, _ method: CMTimeRoundingMethod) -> CMTime ``` |
| To | ``` func CMTimebaseGetTimeWithTimeScale(_ timebase: CMTimebase, _ timescale: CMTimeScale, _ method: CMTimeRoundingMethod) -> CMTime ``` |

Modified [CMTimebaseGetUltimateMasterClock(_: CMTimebase) -> CMClock?](https://developer.apple.com/documentation/coremedia/1489671-cmtimebasegetultimatemasterclock)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func CMTimebaseGetUltimateMasterClock(_ timebase: CMTimebase!) -> CMClock! ``` | -- |
| To | ``` func CMTimebaseGetUltimateMasterClock(_ timebase: CMTimebase) -> CMClock? ``` | iOS 9.0 |

Modified [CMTimebaseNotificationBarrier(_: CMTimebase) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489171-cmtimebasenotificationbarrier)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseNotificationBarrier(_ timebase: CMTimebase!) -> OSStatus ``` |
| To | ``` func CMTimebaseNotificationBarrier(_ timebase: CMTimebase) -> OSStatus ``` |

Modified [CMTimebaseRemoveTimer(_: CMTimebase, _: CFRunLoopTimer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489746-cmtimebaseremovetimer)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseRemoveTimer(_ timebase: CMTimebase!, _ timer: CFRunLoopTimer!) -> OSStatus ``` |
| To | ``` func CMTimebaseRemoveTimer(_ timebase: CMTimebase, _ timer: CFRunLoopTimer) -> OSStatus ``` |

Modified [CMTimebaseRemoveTimerDispatchSource(_: CMTimebase, _: dispatch_source_t) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489198-cmtimebaseremovetimerdispatchsou)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseRemoveTimerDispatchSource(_ timebase: CMTimebase!, _ timerSource: dispatch_source_t!) -> OSStatus ``` |
| To | ``` func CMTimebaseRemoveTimerDispatchSource(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |

Modified [CMTimebaseSetAnchorTime(_: CMTimebase, _: CMTime, _: CMTime) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489504-cmtimebasesetanchortime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetAnchorTime(_ timebase: CMTimebase!, _ timebaseTime: CMTime, _ immediateMasterTime: CMTime) -> OSStatus ``` |
| To | ``` func CMTimebaseSetAnchorTime(_ timebase: CMTimebase, _ timebaseTime: CMTime, _ immediateMasterTime: CMTime) -> OSStatus ``` |

Modified [CMTimebaseSetRate(_: CMTimebase, _: Float64) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489590-cmtimebasesetrate)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetRate(_ timebase: CMTimebase!, _ rate: Float64) -> OSStatus ``` |
| To | ``` func CMTimebaseSetRate(_ timebase: CMTimebase, _ rate: Float64) -> OSStatus ``` |

Modified [CMTimebaseSetRateAndAnchorTime(_: CMTimebase, _: Float64, _: CMTime, _: CMTime) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489332-cmtimebasesetrateandanchortime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetRateAndAnchorTime(_ timebase: CMTimebase!, _ rate: Float64, _ timebaseTime: CMTime, _ immediateMasterTime: CMTime) -> OSStatus ``` |
| To | ``` func CMTimebaseSetRateAndAnchorTime(_ timebase: CMTimebase, _ rate: Float64, _ timebaseTime: CMTime, _ immediateMasterTime: CMTime) -> OSStatus ``` |

Modified [CMTimebaseSetTime(_: CMTimebase, _: CMTime) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489372-cmtimebasesettime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTime(_ timebase: CMTimebase!, _ time: CMTime) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTime(_ timebase: CMTimebase, _ time: CMTime) -> OSStatus ``` |

Modified [CMTimebaseSetTimerDispatchSourceNextFireTime(_: CMTimebase, _: dispatch_source_t, _: CMTime, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489489-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerDispatchSourceNextFireTime(_ timebase: CMTimebase!, _ timerSource: dispatch_source_t!, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerDispatchSourceNextFireTime(_ timebase: CMTimebase, _ timerSource: dispatch_source_t, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |

Modified [CMTimebaseSetTimerDispatchSourceToFireImmediately(_: CMTimebase, _: dispatch_source_t) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489552-cmtimebasesettimerdispatchsource)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerDispatchSourceToFireImmediately(_ timebase: CMTimebase!, _ timerSource: dispatch_source_t!) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerDispatchSourceToFireImmediately(_ timebase: CMTimebase, _ timerSource: dispatch_source_t) -> OSStatus ``` |

Modified [CMTimebaseSetTimerNextFireTime(_: CMTimebase, _: CFRunLoopTimer, _: CMTime, _: UInt32) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489692-cmtimebasesettimernextfiretime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerNextFireTime(_ timebase: CMTimebase!, _ timer: CFRunLoopTimer!, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerNextFireTime(_ timebase: CMTimebase, _ timer: CFRunLoopTimer, _ fireTime: CMTime, _ flags: UInt32) -> OSStatus ``` |

Modified [CMTimebaseSetTimerToFireImmediately(_: CMTimebase, _: CFRunLoopTimer) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489213-cmtimebasesettimertofireimmediat)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimebaseSetTimerToFireImmediately(_ timebase: CMTimebase!, _ timer: CFRunLoopTimer!) -> OSStatus ``` |
| To | ``` func CMTimebaseSetTimerToFireImmediately(_ timebase: CMTimebase, _ timer: CFRunLoopTimer) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(_: CFAllocator?, _: CMTimeCodeFormatDescription, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416287-cmtimecodeformatdescriptioncopya)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeFormatDescription: CMTimeCodeFormatDescription!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator?, _ timeCodeFormatDescription: CMTimeCodeFormatDescription, _ timeCodeDescriptionFlavor: CFString?, _ timeCodeDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescriptionCreate(_: CFAllocator?, _: CMTimeCodeFormatType, _: CMTime, _: UInt32, _: UInt32, _: CFDictionary?, _: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489250-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreate(_ allocator: CFAllocator!, _ timeCodeFormatType: CMTimeCodeFormatType, _ frameDuration: CMTime, _ frameQuanta: UInt32, _ tcFlags: UInt32, _ extensions: CFDictionary!, _ descOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreate(_ allocator: CFAllocator?, _ timeCodeFormatType: CMTimeCodeFormatType, _ frameDuration: CMTime, _ frameQuanta: UInt32, _ tcFlags: UInt32, _ extensions: CFDictionary?, _ descOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFString?, _: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416315-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator!, _ timeCodeDescriptionBlockBuffer: CMBlockBuffer!, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer(_ allocator: CFAllocator?, _ timeCodeDescriptionBlockBuffer: CMBlockBuffer, _ timeCodeDescriptionFlavor: CFString?, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFString?, _: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416256-cmtimecodeformatdescriptioncreat)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator!, _ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: Int, _ timeCodeDescriptionFlavor: CFString!, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMTimeCodeFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData(_ allocator: CFAllocator?, _ timeCodeDescriptionData: UnsafePointer<UInt8>, _ timeCodeDescriptionSize: Int, _ timeCodeDescriptionFlavor: CFString?, _ timeCodeFormatDescriptionOut: UnsafeMutablePointer<CMTimeCodeFormatDescription?>) -> OSStatus ``` |

Modified [CMTimeCodeFormatDescriptionGetFrameDuration(_: CMTimeCodeFormatDescription) -> CMTime](https://developer.apple.com/documentation/coremedia/1489815-cmtimecodeformatdescriptiongetfr)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionGetFrameDuration(_ timeCodeFormatDescription: CMTimeCodeFormatDescription!) -> CMTime ``` |
| To | ``` func CMTimeCodeFormatDescriptionGetFrameDuration(_ timeCodeFormatDescription: CMTimeCodeFormatDescription) -> CMTime ``` |

Modified [CMTimeCodeFormatDescriptionGetFrameQuanta(_: CMTimeCodeFormatDescription) -> UInt32](https://developer.apple.com/documentation/coremedia/1489418-cmtimecodeformatdescriptiongetfr)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionGetFrameQuanta(_ timeCodeFormatDescription: CMTimeCodeFormatDescription!) -> UInt32 ``` |
| To | ``` func CMTimeCodeFormatDescriptionGetFrameQuanta(_ timeCodeFormatDescription: CMTimeCodeFormatDescription) -> UInt32 ``` |

Modified [CMTimeCodeFormatDescriptionGetTimeCodeFlags(_: CMTimeCodeFormatDescription) -> UInt32](https://developer.apple.com/documentation/coremedia/1489390-cmtimecodeformatdescriptiongetti)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCodeFormatDescriptionGetTimeCodeFlags(_ desc: CMTimeCodeFormatDescription!) -> UInt32 ``` |
| To | ``` func CMTimeCodeFormatDescriptionGetTimeCodeFlags(_ desc: CMTimeCodeFormatDescription) -> UInt32 ``` |

Modified [CMTimeCopyAsDictionary(_: CMTime, _: CFAllocator?) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1400845-cmtimecopyasdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCopyAsDictionary(_ time: CMTime, _ allocator: CFAllocator!) -> CFDictionary! ``` |
| To | ``` func CMTimeCopyAsDictionary(_ time: CMTime, _ allocator: CFAllocator?) -> CFDictionary? ``` |

Modified [CMTimeCopyDescription(_: CFAllocator?, _: CMTime) -> CFString?](https://developer.apple.com/documentation/coremedia/1400791-cmtimecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeCopyDescription(_ allocator: CFAllocator!, _ time: CMTime) -> CFString! ``` |
| To | ``` func CMTimeCopyDescription(_ allocator: CFAllocator?, _ time: CMTime) -> CFString? ``` |

Modified [CMTimeMakeFromDictionary(_: CFDictionary?) -> CMTime](https://developer.apple.com/documentation/coremedia/1400819-cmtimemakefromdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeMakeFromDictionary(_ dict: CFDictionary!) -> CMTime ``` |
| To | ``` func CMTimeMakeFromDictionary(_ dict: CFDictionary?) -> CMTime ``` |

Modified [CMTimeRangeContainsTime(_: CMTimeRange, _: CMTime) -> Bool](https://developer.apple.com/documentation/coremedia/1462775-cmtimerangecontainstime)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeContainsTime(_ range: CMTimeRange, _ time: CMTime) -> Boolean ``` |
| To | ``` func CMTimeRangeContainsTime(_ range: CMTimeRange, _ time: CMTime) -> Bool ``` |

Modified [CMTimeRangeContainsTimeRange(_: CMTimeRange, _: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1462830-cmtimerangecontainstimerange)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeContainsTimeRange(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Boolean ``` |
| To | ``` func CMTimeRangeContainsTimeRange(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |

Modified [CMTimeRangeCopyAsDictionary(_: CMTimeRange, _: CFAllocator?) -> CFDictionary?](https://developer.apple.com/documentation/coremedia/1462781-cmtimerangecopyasdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeCopyAsDictionary(_ range: CMTimeRange, _ allocator: CFAllocator!) -> CFDictionary! ``` |
| To | ``` func CMTimeRangeCopyAsDictionary(_ range: CMTimeRange, _ allocator: CFAllocator?) -> CFDictionary? ``` |

Modified [CMTimeRangeCopyDescription(_: CFAllocator?, _: CMTimeRange) -> CFString?](https://developer.apple.com/documentation/coremedia/1462823-cmtimerangecopydescription)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeCopyDescription(_ allocator: CFAllocator!, _ range: CMTimeRange) -> CFString! ``` |
| To | ``` func CMTimeRangeCopyDescription(_ allocator: CFAllocator?, _ range: CMTimeRange) -> CFString? ``` |

Modified [CMTimeRangeEqual(_: CMTimeRange, _: CMTimeRange) -> Bool](https://developer.apple.com/documentation/coremedia/1462841-cmtimerangeequal)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeEqual(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Boolean ``` |
| To | ``` func CMTimeRangeEqual(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool ``` |

Modified [CMTimeRangeMakeFromDictionary(_: CFDictionary) -> CMTimeRange](https://developer.apple.com/documentation/coremedia/1462777-cmtimerangemakefromdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CMTimeRangeMakeFromDictionary(_ dict: CFDictionary!) -> CMTimeRange ``` |
| To | ``` func CMTimeRangeMakeFromDictionary(_ dict: CFDictionary) -> CMTimeRange ``` |

Modified [CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(_: CFAllocator?, _: CMVideoFormatDescription, _: CFStringEncoding, _: CFString?, _: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416273-cmvideoformatdescriptioncopyasbi)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ videoFormatDescription: CMVideoFormatDescription!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ imageDescriptionBlockBufferOut: UnsafeMutablePointer<Unmanaged<CMBlockBuffer>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator?, _ videoFormatDescription: CMVideoFormatDescription, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString?, _ imageDescriptionBlockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionCreate(_: CFAllocator?, _: CMVideoCodecType, _: Int32, _: Int32, _: CFDictionary?, _: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489743-cmvideoformatdescriptioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreate(_ allocator: CFAllocator!, _ codecType: CMVideoCodecType, _ width: Int32, _ height: Int32, _ extensions: CFDictionary!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreate(_ allocator: CFAllocator?, _ codecType: CMVideoCodecType, _ width: Int32, _ height: Int32, _ extensions: CFDictionary?, _ outDesc: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionCreateForImageBuffer(_: CFAllocator?, _: CVImageBuffer, _: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489730-cmvideoformatdescriptioncreatefo)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateForImageBuffer(_ allocator: CFAllocator!, _ imageBuffer: CVImageBuffer!, _ outDesc: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateForImageBuffer(_ allocator: CFAllocator?, _ imageBuffer: CVImageBuffer, _ outDesc: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(_: CFAllocator?, _: CMBlockBuffer, _: CFStringEncoding, _: CFString?, _: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416242-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator!, _ imageDescriptionBlockBuffer: CMBlockBuffer!, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer(_ allocator: CFAllocator?, _ imageDescriptionBlockBuffer: CMBlockBuffer, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString?, _ videoFormatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_: CFAllocator?, _: UnsafePointer<UInt8>, _: Int, _: CFStringEncoding, _: CFString?, _: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1416297-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator!, _ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: Int, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString!, _ videoFormatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMVideoFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData(_ allocator: CFAllocator?, _ imageDescriptionData: UnsafePointer<UInt8>, _ imageDescriptionSize: Int, _ imageDescriptionStringEncoding: CFStringEncoding, _ imageDescriptionFlavor: CFString?, _ videoFormatDescriptionOut: UnsafeMutablePointer<CMVideoFormatDescription?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionCreateFromH264ParameterSets(_: CFAllocator?, _: Int, _: UnsafePointer<UnsafePointer<UInt8>>, _: UnsafePointer<Int>, _: Int32, _: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489818-cmvideoformatdescriptioncreatefr)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator!, _ parameterSetCount: Int, _ parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, _ parameterSetSizes: UnsafePointer<Int>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafeMutablePointer<Unmanaged<CMFormatDescription>?>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionCreateFromH264ParameterSets(_ allocator: CFAllocator?, _ parameterSetCount: Int, _ parameterSetPointers: UnsafePointer<UnsafePointer<UInt8>>, _ parameterSetSizes: UnsafePointer<Int>, _ NALUnitHeaderLength: Int32, _ formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionGetCleanAperture(_: CMVideoFormatDescription, _: Bool) -> CGRect](https://developer.apple.com/documentation/coremedia/1489235-cmvideoformatdescriptiongetclean)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetCleanAperture(_ videoDesc: CMVideoFormatDescription!, _ originIsAtTopLeft: Boolean) -> CGRect ``` |
| To | ``` func CMVideoFormatDescriptionGetCleanAperture(_ videoDesc: CMVideoFormatDescription, _ originIsAtTopLeft: Bool) -> CGRect ``` |

Modified [CMVideoFormatDescriptionGetDimensions(_: CMVideoFormatDescription) -> CMVideoDimensions](https://developer.apple.com/documentation/coremedia/1489287-cmvideoformatdescriptiongetdimen)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetDimensions(_ videoDesc: CMVideoFormatDescription!) -> CMVideoDimensions ``` |
| To | ``` func CMVideoFormatDescriptionGetDimensions(_ videoDesc: CMVideoFormatDescription) -> CMVideoDimensions ``` |

Modified [CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> CFArray](https://developer.apple.com/documentation/coremedia/1489296-cmvideoformatdescriptiongetexten)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> Unmanaged<CFArray>! ``` |
| To | ``` func CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers() -> CFArray ``` |

Modified [CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_: CMFormatDescription, _: Int, _: UnsafeMutablePointer<UnsafePointer<UInt8>>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int>, _: UnsafeMutablePointer<Int32>) -> OSStatus](https://developer.apple.com/documentation/coremedia/1489529-cmvideoformatdescriptiongeth264p)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription!, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<Int>, _ parameterSetCountOut: UnsafeMutablePointer<Int>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` |
| To | ``` func CMVideoFormatDescriptionGetH264ParameterSetAtIndex(_ videoDesc: CMFormatDescription, _ parameterSetIndex: Int, _ parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ parameterSetSizeOut: UnsafeMutablePointer<Int>, _ parameterSetCountOut: UnsafeMutablePointer<Int>, _ NALUnitHeaderLengthOut: UnsafeMutablePointer<Int32>) -> OSStatus ``` |

Modified [CMVideoFormatDescriptionGetPresentationDimensions(_: CMVideoFormatDescription, _: Bool, _: Bool) -> CGSize](https://developer.apple.com/documentation/coremedia/1489218-cmvideoformatdescriptiongetprese)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionGetPresentationDimensions(_ videoDesc: CMVideoFormatDescription!, _ usePixelAspectRatio: Boolean, _ useCleanAperture: Boolean) -> CGSize ``` |
| To | ``` func CMVideoFormatDescriptionGetPresentationDimensions(_ videoDesc: CMVideoFormatDescription, _ usePixelAspectRatio: Bool, _ useCleanAperture: Bool) -> CGSize ``` |

Modified [CMVideoFormatDescriptionMatchesImageBuffer(_: CMVideoFormatDescription, _: CVImageBuffer) -> Bool](https://developer.apple.com/documentation/coremedia/1489579-cmvideoformatdescriptionmatchesi)

|  | Declaration |
| --- | --- |
| From | ``` func CMVideoFormatDescriptionMatchesImageBuffer(_ desc: CMVideoFormatDescription!, _ imageBuffer: CVImageBuffer!) -> Boolean ``` |
| To | ``` func CMVideoFormatDescriptionMatchesImageBuffer(_ desc: CMVideoFormatDescription, _ imageBuffer: CVImageBuffer) -> Bool ``` |

Modified [kCMAttachmentMode_ShouldNotPropagate](https://developer.apple.com/documentation/coremedia/1470711-attachment_modes/kcmattachmentmode_shouldnotpropagate)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAttachmentMode_ShouldNotPropagate: Int { get } ``` |
| To | ``` var kCMAttachmentMode_ShouldNotPropagate: CMAttachmentMode { get } ``` |

Modified [kCMAttachmentMode_ShouldPropagate](https://developer.apple.com/documentation/coremedia/1470711-attachment_modes/kcmattachmentmode_shouldpropagate)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAttachmentMode_ShouldPropagate: Int { get } ``` |
| To | ``` var kCMAttachmentMode_ShouldPropagate: CMAttachmentMode { get } ``` |

Modified [kCMAudioCodecType_AAC_AudibleProtected](https://developer.apple.com/documentation/coremedia/kcmaudiocodectype_aac_audibleprotected)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioCodecType_AAC_AudibleProtected: Int { get } ``` |
| To | ``` var kCMAudioCodecType_AAC_AudibleProtected: CMAudioCodecType { get } ``` |

Modified [kCMAudioCodecType_AAC_LCProtected](https://developer.apple.com/documentation/coremedia/1564221-cmaudiocodectype/kcmaudiocodectype_aac_lcprotected)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioCodecType_AAC_LCProtected: Int { get } ``` |
| To | ``` var kCMAudioCodecType_AAC_LCProtected: CMAudioCodecType { get } ``` |

Modified [kCMAudioFormatDescriptionMask_All](https://developer.apple.com/documentation/coremedia/kcmaudioformatdescriptionmask_all)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioFormatDescriptionMask_All: Int { get } ``` |
| To | ``` var kCMAudioFormatDescriptionMask_All: CMAudioFormatDescriptionMask { get } ``` |

Modified [kCMAudioFormatDescriptionMask_ChannelLayout](https://developer.apple.com/documentation/coremedia/1564202-format_description_mask_codes/kcmaudioformatdescriptionmask_channellayout)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioFormatDescriptionMask_ChannelLayout: Int { get } ``` |
| To | ``` var kCMAudioFormatDescriptionMask_ChannelLayout: CMAudioFormatDescriptionMask { get } ``` |

Modified [kCMAudioFormatDescriptionMask_Extensions](https://developer.apple.com/documentation/coremedia/kcmaudioformatdescriptionmask_extensions)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioFormatDescriptionMask_Extensions: Int { get } ``` |
| To | ``` var kCMAudioFormatDescriptionMask_Extensions: CMAudioFormatDescriptionMask { get } ``` |

Modified [kCMAudioFormatDescriptionMask_MagicCookie](https://developer.apple.com/documentation/coremedia/1564202-format_description_mask_codes/kcmaudioformatdescriptionmask_magiccookie)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioFormatDescriptionMask_MagicCookie: Int { get } ``` |
| To | ``` var kCMAudioFormatDescriptionMask_MagicCookie: CMAudioFormatDescriptionMask { get } ``` |

Modified [kCMAudioFormatDescriptionMask_StreamBasicDescription](https://developer.apple.com/documentation/coremedia/kcmaudioformatdescriptionmask_streambasicdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kCMAudioFormatDescriptionMask_StreamBasicDescription: Int { get } ``` |
| To | ``` var kCMAudioFormatDescriptionMask_StreamBasicDescription: CMAudioFormatDescriptionMask { get } ``` |

Modified [kCMBlockBufferAlwaysCopyDataFlag](https://developer.apple.com/documentation/coremedia/1575286-cmblockbuffer_flags/kcmblockbufferalwayscopydataflag)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferAlwaysCopyDataFlag: Int { get } ``` |
| To | ``` var kCMBlockBufferAlwaysCopyDataFlag: CMBlockBufferFlags { get } ``` |

Modified [kCMBlockBufferAssureMemoryNowFlag](https://developer.apple.com/documentation/coremedia/1575286-cmblockbuffer_flags/kcmblockbufferassurememorynowflag)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferAssureMemoryNowFlag: Int { get } ``` |
| To | ``` var kCMBlockBufferAssureMemoryNowFlag: CMBlockBufferFlags { get } ``` |

Modified [kCMBlockBufferBadCustomBlockSourceErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferbadcustomblocksourceerr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferBadCustomBlockSourceErr: Int { get } ``` |
| To | ``` var kCMBlockBufferBadCustomBlockSourceErr: OSStatus { get } ``` |

Modified [kCMBlockBufferBadLengthParameterErr](https://developer.apple.com/documentation/coremedia/kcmblockbufferbadlengthparametererr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferBadLengthParameterErr: Int { get } ``` |
| To | ``` var kCMBlockBufferBadLengthParameterErr: OSStatus { get } ``` |

Modified [kCMBlockBufferBadOffsetParameterErr](https://developer.apple.com/documentation/coremedia/kcmblockbufferbadoffsetparametererr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferBadOffsetParameterErr: Int { get } ``` |
| To | ``` var kCMBlockBufferBadOffsetParameterErr: OSStatus { get } ``` |

Modified [kCMBlockBufferBadPointerParameterErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferbadpointerparametererr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferBadPointerParameterErr: Int { get } ``` |
| To | ``` var kCMBlockBufferBadPointerParameterErr: OSStatus { get } ``` |

Modified [kCMBlockBufferBlockAllocationFailedErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferblockallocationfailederr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferBlockAllocationFailedErr: Int { get } ``` |
| To | ``` var kCMBlockBufferBlockAllocationFailedErr: OSStatus { get } ``` |

Modified [kCMBlockBufferCustomBlockSourceVersion](https://developer.apple.com/documentation/coremedia/1575287-custom_block_source_version/kcmblockbuffercustomblocksourceversion)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferCustomBlockSourceVersion: Int { get } ``` |
| To | ``` var kCMBlockBufferCustomBlockSourceVersion: UInt32 { get } ``` |

Modified [kCMBlockBufferDontOptimizeDepthFlag](https://developer.apple.com/documentation/coremedia/kcmblockbufferdontoptimizedepthflag)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferDontOptimizeDepthFlag: Int { get } ``` |
| To | ``` var kCMBlockBufferDontOptimizeDepthFlag: CMBlockBufferFlags { get } ``` |

Modified [kCMBlockBufferEmptyBBufErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferemptybbuferr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferEmptyBBufErr: Int { get } ``` |
| To | ``` var kCMBlockBufferEmptyBBufErr: OSStatus { get } ``` |

Modified [kCMBlockBufferInsufficientSpaceErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferinsufficientspaceerr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferInsufficientSpaceErr: Int { get } ``` |
| To | ``` var kCMBlockBufferInsufficientSpaceErr: OSStatus { get } ``` |

Modified [kCMBlockBufferNoErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbuffernoerr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferNoErr: Int { get } ``` |
| To | ``` var kCMBlockBufferNoErr: OSStatus { get } ``` |

Modified [kCMBlockBufferPermitEmptyReferenceFlag](https://developer.apple.com/documentation/coremedia/kcmblockbufferpermitemptyreferenceflag)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferPermitEmptyReferenceFlag: Int { get } ``` |
| To | ``` var kCMBlockBufferPermitEmptyReferenceFlag: CMBlockBufferFlags { get } ``` |

Modified [kCMBlockBufferStructureAllocationFailedErr](https://developer.apple.com/documentation/coremedia/1575288-block_buffer_error_codes/kcmblockbufferstructureallocationfailederr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferStructureAllocationFailedErr: Int { get } ``` |
| To | ``` var kCMBlockBufferStructureAllocationFailedErr: OSStatus { get } ``` |

Modified [kCMBlockBufferUnallocatedBlockErr](https://developer.apple.com/documentation/coremedia/kcmblockbufferunallocatedblockerr)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBlockBufferUnallocatedBlockErr: Int { get } ``` |
| To | ``` var kCMBlockBufferUnallocatedBlockErr: OSStatus { get } ``` |

Modified [kCMBufferQueueError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMBufferQueueError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMBufferQueueError_BadTriggerDuration](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_badtriggerduration)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_BadTriggerDuration: Int { get } ``` |
| To | ``` var kCMBufferQueueError_BadTriggerDuration: OSStatus { get } ``` |

Modified [kCMBufferQueueError_CannotModifyQueueFromTriggerCallback](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_cannotmodifyqueuefromtriggercallback)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_CannotModifyQueueFromTriggerCallback: Int { get } ``` |
| To | ``` var kCMBufferQueueError_CannotModifyQueueFromTriggerCallback: OSStatus { get } ``` |

Modified [kCMBufferQueueError_EnqueueAfterEndOfData](https://developer.apple.com/documentation/coremedia/kcmbufferqueueerror_enqueueafterendofdata)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_EnqueueAfterEndOfData: Int { get } ``` |
| To | ``` var kCMBufferQueueError_EnqueueAfterEndOfData: OSStatus { get } ``` |

Modified [kCMBufferQueueError_InvalidBuffer](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_invalidbuffer)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_InvalidBuffer: Int { get } ``` |
| To | ``` var kCMBufferQueueError_InvalidBuffer: OSStatus { get } ``` |

Modified [kCMBufferQueueError_InvalidCMBufferCallbacksStruct](https://developer.apple.com/documentation/coremedia/kcmbufferqueueerror_invalidcmbuffercallbacksstruct)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_InvalidCMBufferCallbacksStruct: Int { get } ``` |
| To | ``` var kCMBufferQueueError_InvalidCMBufferCallbacksStruct: OSStatus { get } ``` |

Modified [kCMBufferQueueError_InvalidTriggerCondition](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_invalidtriggercondition)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_InvalidTriggerCondition: Int { get } ``` |
| To | ``` var kCMBufferQueueError_InvalidTriggerCondition: OSStatus { get } ``` |

Modified [kCMBufferQueueError_InvalidTriggerToken](https://developer.apple.com/documentation/coremedia/1564485-buffer_queue_error_codes/kcmbufferqueueerror_invalidtriggertoken)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_InvalidTriggerToken: Int { get } ``` |
| To | ``` var kCMBufferQueueError_InvalidTriggerToken: OSStatus { get } ``` |

Modified [kCMBufferQueueError_QueueIsFull](https://developer.apple.com/documentation/coremedia/kcmbufferqueueerror_queueisfull)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_QueueIsFull: Int { get } ``` |
| To | ``` var kCMBufferQueueError_QueueIsFull: OSStatus { get } ``` |

Modified [kCMBufferQueueError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/kcmbufferqueueerror_requiredparametermissing)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueError_RequiredParameterMissing: Int { get } ``` |
| To | ``` var kCMBufferQueueError_RequiredParameterMissing: OSStatus { get } ``` |

Modified [kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whenbuffercountbecomesgreaterthan)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenBufferCountBecomesGreaterThan: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whenbuffercountbecomeslessthan)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenBufferCountBecomesLessThan: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenDataBecomesReady](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whendatabecomesready)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenDataBecomesReady: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenDataBecomesReady: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whendurationbecomesgreaterthan)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThan: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whendurationbecomesgreaterthanorequalto)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualTo: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenDurationBecomesLessThan](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whendurationbecomeslessthan)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenDurationBecomesLessThan: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenDurationBecomesLessThan: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whendurationbecomeslessthanorequalto)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenDurationBecomesLessThanOrEqualTo: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenEndOfDataReached](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whenendofdatareached)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenEndOfDataReached: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenEndOfDataReached: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whenmaxpresentationtimestampchanges)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenMaxPresentationTimeStampChanges: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges](https://developer.apple.com/documentation/coremedia/1564484-trigger_conditions/kcmbufferqueuetrigger_whenminpresentationtimestampchanges)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenMinPresentationTimeStampChanges: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMBufferQueueTrigger_WhenReset](https://developer.apple.com/documentation/coremedia/kcmbufferqueuetrigger_whenreset)

|  | Declaration |
| --- | --- |
| From | ``` var kCMBufferQueueTrigger_WhenReset: Int { get } ``` |
| To | ``` var kCMBufferQueueTrigger_WhenReset: CMBufferQueueTriggerCondition { get } ``` |

Modified [kCMClockError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmclockerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClockError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMClockError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMClockError_InvalidParameter](https://developer.apple.com/documentation/coremedia/kcmclockerror_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClockError_InvalidParameter: Int { get } ``` |
| To | ``` var kCMClockError_InvalidParameter: OSStatus { get } ``` |

Modified [kCMClockError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_missingrequiredparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClockError_MissingRequiredParameter: Int { get } ``` |
| To | ``` var kCMClockError_MissingRequiredParameter: OSStatus { get } ``` |

Modified [kCMClockError_UnsupportedOperation](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_unsupportedoperation)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClockError_UnsupportedOperation: Int { get } ``` |
| To | ``` var kCMClockError_UnsupportedOperation: OSStatus { get } ``` |

Modified [kCMClosedCaptionFormatType_ATSC](https://developer.apple.com/documentation/coremedia/kcmclosedcaptionformattype_atsc)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClosedCaptionFormatType_ATSC: Int { get } ``` |
| To | ``` var kCMClosedCaptionFormatType_ATSC: CMClosedCaptionFormatType { get } ``` |

Modified [kCMClosedCaptionFormatType_CEA608](https://developer.apple.com/documentation/coremedia/1564218-closed_capture_format_type_const/kcmclosedcaptionformattype_cea608)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClosedCaptionFormatType_CEA608: Int { get } ``` |
| To | ``` var kCMClosedCaptionFormatType_CEA608: CMClosedCaptionFormatType { get } ``` |

Modified [kCMClosedCaptionFormatType_CEA708](https://developer.apple.com/documentation/coremedia/1564218-closed_capture_format_type_const/kcmclosedcaptionformattype_cea708)

|  | Declaration |
| --- | --- |
| From | ``` var kCMClosedCaptionFormatType_CEA708: Int { get } ``` |
| To | ``` var kCMClosedCaptionFormatType_CEA708: CMClosedCaptionFormatType { get } ``` |

Modified [kCMFormatDescriptionBridgeError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionbridgeerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_IncompatibleFormatDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionbridgeerror_incompatibleformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_IncompatibleFormatDescription: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_IncompatibleFormatDescription: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_InvalidFormatDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionbridgeerror_invalidformatdescription)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_InvalidFormatDescription: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_InvalidFormatDescription: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1416276-format_description_bridge_error_/kcmformatdescriptionbridgeerror_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_InvalidParameter: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_InvalidParameter: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_InvalidSerializedSampleDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionbridgeerror_invalidserializedsampledescription)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_InvalidSerializedSampleDescription: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_InvalidSerializedSampleDescription: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_InvalidSlice](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionbridgeerror_invalidslice)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_InvalidSlice: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_InvalidSlice: OSStatus { get } ``` |

Modified [kCMFormatDescriptionBridgeError_UnsupportedSampleDescriptionFlavor](https://developer.apple.com/documentation/coremedia/1416276-format_description_bridge_error_/kcmformatdescriptionbridgeerror_unsupportedsampledescriptionflavor)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionBridgeError_UnsupportedSampleDescriptionFlavor: Int { get } ``` |
| To | ``` var kCMFormatDescriptionBridgeError_UnsupportedSampleDescriptionFlavor: OSStatus { get } ``` |

Modified [kCMFormatDescriptionColorPrimaries_P22](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p22)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionColorPrimaries_P22: CFString! ``` |
| To | ``` let kCMFormatDescriptionColorPrimaries_P22: CFString ``` |

Modified [kCMFormatDescriptionConformsToMPEG2VideoProfile](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionconformstompeg2videoprofile)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionConformsToMPEG2VideoProfile: CFString! ``` |
| To | ``` let kCMFormatDescriptionConformsToMPEG2VideoProfile: CFString ``` |

Modified [kCMFormatDescriptionError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1564245-error_codes/kcmformatdescriptionerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMFormatDescriptionError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMFormatDescriptionError_InvalidParameter](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionerror_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionError_InvalidParameter: Int { get } ``` |
| To | ``` var kCMFormatDescriptionError_InvalidParameter: OSStatus { get } ``` |

Modified [kCMFormatDescriptionError_ValueNotAvailable](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionerror_valuenotavailable)

|  | Declaration |
| --- | --- |
| From | ``` var kCMFormatDescriptionError_ValueNotAvailable: Int { get } ``` |
| To | ``` var kCMFormatDescriptionError_ValueNotAvailable: OSStatus { get } ``` |

Modified [kCMFormatDescriptionExtension_BytesPerRow](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_bytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_BytesPerRow: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_BytesPerRow: CFString ``` |

Modified [kCMFormatDescriptionExtension_Depth](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_depth)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_Depth: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_Depth: CFString ``` |

Modified [kCMFormatDescriptionExtension_FormatName](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_formatname)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_FormatName: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_FormatName: CFString ``` |

Modified [kCMFormatDescriptionExtension_FullRangeVideo](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fullrangevideo)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_FullRangeVideo: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_FullRangeVideo: CFString ``` |

Modified [kCMFormatDescriptionExtension_ICCProfile](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_iccprofile)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_ICCProfile: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_ICCProfile: CFString ``` |

Modified [kCMFormatDescriptionExtension_OriginalCompressionSettings](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_originalcompressionsettings)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_OriginalCompressionSettings: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_OriginalCompressionSettings: CFString ``` |

Modified [kCMFormatDescriptionExtension_RevisionLevel](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_revisionlevel)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_RevisionLevel: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_RevisionLevel: CFString ``` |

Modified [kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_sampledescriptionextensionatoms)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_SampleDescriptionExtensionAtoms: CFString ``` |

Modified [kCMFormatDescriptionExtension_SpatialQuality](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_spatialquality)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_SpatialQuality: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_SpatialQuality: CFString ``` |

Modified [kCMFormatDescriptionExtension_TemporalQuality](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_temporalquality)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_TemporalQuality: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_TemporalQuality: CFString ``` |

Modified [kCMFormatDescriptionExtension_Vendor](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_vendor)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_Vendor: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_Vendor: CFString ``` |

Modified [kCMFormatDescriptionExtension_VerbatimISOSampleEntry](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_verbatimisosampleentry)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_VerbatimISOSampleEntry: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_VerbatimISOSampleEntry: CFString ``` |

Modified [kCMFormatDescriptionExtension_VerbatimSampleDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_verbatimsampledescription)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_VerbatimSampleDescription: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_VerbatimSampleDescription: CFString ``` |

Modified [kCMFormatDescriptionExtension_Version](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_version)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtension_Version: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtension_Version: CFString ``` |

Modified [kCMFormatDescriptionExtensionKey_MetadataKeyTable](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextensionkey_metadatakeytable)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionExtensionKey_MetadataKeyTable: CFString! ``` |
| To | ``` let kCMFormatDescriptionExtensionKey_MetadataKeyTable: CFString ``` |

Modified [kCMFormatDescriptionKey_CleanApertureHeightRational](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureheightrational)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionKey_CleanApertureHeightRational: CFString! ``` |
| To | ``` let kCMFormatDescriptionKey_CleanApertureHeightRational: CFString ``` |

Modified [kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturehorizontaloffsetrational)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational: CFString! ``` |
| To | ``` let kCMFormatDescriptionKey_CleanApertureHorizontalOffsetRational: CFString ``` |

Modified [kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureverticaloffsetrational)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational: CFString! ``` |
| To | ``` let kCMFormatDescriptionKey_CleanApertureVerticalOffsetRational: CFString ``` |

Modified [kCMFormatDescriptionKey_CleanApertureWidthRational](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturewidthrational)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionKey_CleanApertureWidthRational: CFString! ``` |
| To | ``` let kCMFormatDescriptionKey_CleanApertureWidthRational: CFString ``` |

Modified [kCMFormatDescriptionVendor_Apple](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionvendor_apple)

|  | Declaration |
| --- | --- |
| From | ``` let kCMFormatDescriptionVendor_Apple: CFString! ``` |
| To | ``` let kCMFormatDescriptionVendor_Apple: CFString ``` |

Modified [kCMImageDescriptionFlavor_3GPFamily](https://developer.apple.com/documentation/coremedia/kcmimagedescriptionflavor_3gpfamily)

|  | Declaration |
| --- | --- |
| From | ``` let kCMImageDescriptionFlavor_3GPFamily: CFString! ``` |
| To | ``` let kCMImageDescriptionFlavor_3GPFamily: CFString ``` |

Modified [kCMImageDescriptionFlavor_ISOFamily](https://developer.apple.com/documentation/coremedia/cmimagedescriptionflavor/1416253-isofamily)

|  | Declaration |
| --- | --- |
| From | ``` let kCMImageDescriptionFlavor_ISOFamily: CFString! ``` |
| To | ``` let kCMImageDescriptionFlavor_ISOFamily: CFString ``` |

Modified [kCMImageDescriptionFlavor_QuickTimeMovie](https://developer.apple.com/documentation/coremedia/cmimagedescriptionflavor/1416282-quicktimemovie)

|  | Declaration |
| --- | --- |
| From | ``` let kCMImageDescriptionFlavor_QuickTimeMovie: CFString! ``` |
| To | ``` let kCMImageDescriptionFlavor_QuickTimeMovie: CFString ``` |

Modified [kCMMediaType_Audio](https://developer.apple.com/documentation/coremedia/1564193-cmmediatype/kcmmediatype_audio)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Audio: Int { get } ``` |
| To | ``` var kCMMediaType_Audio: CMMediaType { get } ``` |

Modified [kCMMediaType_ClosedCaption](https://developer.apple.com/documentation/coremedia/kcmmediatype_closedcaption)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_ClosedCaption: Int { get } ``` |
| To | ``` var kCMMediaType_ClosedCaption: CMMediaType { get } ``` |

Modified [kCMMediaType_Metadata](https://developer.apple.com/documentation/coremedia/kcmmediatype_metadata)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Metadata: Int { get } ``` |
| To | ``` var kCMMediaType_Metadata: CMMediaType { get } ``` |

Modified [kCMMediaType_Muxed](https://developer.apple.com/documentation/coremedia/kcmmediatype_muxed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Muxed: Int { get } ``` |
| To | ``` var kCMMediaType_Muxed: CMMediaType { get } ``` |

Modified [kCMMediaType_Subtitle](https://developer.apple.com/documentation/coremedia/kcmmediatype_subtitle)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Subtitle: Int { get } ``` |
| To | ``` var kCMMediaType_Subtitle: CMMediaType { get } ``` |

Modified [kCMMediaType_Text](https://developer.apple.com/documentation/coremedia/1564193-cmmediatype/kcmmediatype_text)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Text: Int { get } ``` |
| To | ``` var kCMMediaType_Text: CMMediaType { get } ``` |

Modified [kCMMediaType_TimeCode](https://developer.apple.com/documentation/coremedia/1564193-cmmediatype/kcmmediatype_timecode)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_TimeCode: Int { get } ``` |
| To | ``` var kCMMediaType_TimeCode: CMMediaType { get } ``` |

Modified [kCMMediaType_Video](https://developer.apple.com/documentation/coremedia/kcmmediatype_video)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMediaType_Video: Int { get } ``` |
| To | ``` var kCMMediaType_Video: CMMediaType { get } ``` |

Modified [kCMMemoryPoolOption_AgeOutPeriod](https://developer.apple.com/documentation/coremedia/kcmmemorypooloption_ageoutperiod)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMemoryPoolOption_AgeOutPeriod: CFString! ``` |
| To | ``` let kCMMemoryPoolOption_AgeOutPeriod: CFString ``` |

Modified [kCMMetadataBaseDataType_AffineTransformF64](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_affinetransformf64)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_AffineTransformF64: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_AffineTransformF64: CFString ``` |

Modified [kCMMetadataBaseDataType_BMP](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_bmp)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_BMP: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_BMP: CFString ``` |

Modified [kCMMetadataBaseDataType_DimensionsF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_dimensionsf32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_DimensionsF32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_DimensionsF32: CFString ``` |

Modified [kCMMetadataBaseDataType_Float32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_float32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_Float32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_Float32: CFString ``` |

Modified [kCMMetadataBaseDataType_Float64](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_float64)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_Float64: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_Float64: CFString ``` |

Modified [kCMMetadataBaseDataType_GIF](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_gif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_GIF: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_GIF: CFString ``` |

Modified [kCMMetadataBaseDataType_JPEG](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_jpeg)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_JPEG: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_JPEG: CFString ``` |

Modified [kCMMetadataBaseDataType_PNG](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_png)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_PNG: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_PNG: CFString ``` |

Modified [kCMMetadataBaseDataType_PointF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_pointf32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_PointF32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_PointF32: CFString ``` |

Modified [kCMMetadataBaseDataType_RawData](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_rawdata)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_RawData: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_RawData: CFString ``` |

Modified [kCMMetadataBaseDataType_RectF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_rectf32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_RectF32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_RectF32: CFString ``` |

Modified [kCMMetadataBaseDataType_SInt16](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_sint16)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_SInt16: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_SInt16: CFString ``` |

Modified [kCMMetadataBaseDataType_SInt32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_sint32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_SInt32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_SInt32: CFString ``` |

Modified [kCMMetadataBaseDataType_SInt64](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_sint64)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_SInt64: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_SInt64: CFString ``` |

Modified [kCMMetadataBaseDataType_SInt8](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_sint8)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_SInt8: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_SInt8: CFString ``` |

Modified [kCMMetadataBaseDataType_UInt16](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_uint16)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UInt16: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UInt16: CFString ``` |

Modified [kCMMetadataBaseDataType_UInt32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_uint32)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UInt32: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UInt32: CFString ``` |

Modified [kCMMetadataBaseDataType_UInt64](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_uint64)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UInt64: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UInt64: CFString ``` |

Modified [kCMMetadataBaseDataType_UInt8](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_uint8)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UInt8: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UInt8: CFString ``` |

Modified [kCMMetadataBaseDataType_UTF16](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_utf16)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UTF16: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UTF16: CFString ``` |

Modified [kCMMetadataBaseDataType_UTF8](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_utf8)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataBaseDataType_UTF8: CFString! ``` |
| To | ``` let kCMMetadataBaseDataType_UTF8: CFString ``` |

Modified [kCMMetadataDataType_QuickTimeMetadataDirection](https://developer.apple.com/documentation/coremedia/kcmmetadatadatatype_quicktimemetadatadirection)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataDataType_QuickTimeMetadataDirection: CFString! ``` |
| To | ``` let kCMMetadataDataType_QuickTimeMetadataDirection: CFString ``` |

Modified [kCMMetadataDataType_QuickTimeMetadataLocation_ISO6709](https://developer.apple.com/documentation/coremedia/kcmmetadatadatatype_quicktimemetadatalocation_iso6709)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataDataType_QuickTimeMetadataLocation_ISO6709: CFString! ``` |
| To | ``` let kCMMetadataDataType_QuickTimeMetadataLocation_ISO6709: CFString ``` |

Modified [kCMMetadataDataTypeRegistryError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1473968-metadata_registry_error_codes/kcmmetadatadatatyperegistryerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMMetadataDataTypeRegistryError_BadDataTypeIdentifier](https://developer.apple.com/documentation/coremedia/1473968-metadata_registry_error_codes/kcmmetadatadatatyperegistryerror_baddatatypeidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_BadDataTypeIdentifier: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_BadDataTypeIdentifier: OSStatus { get } ``` |

Modified [kCMMetadataDataTypeRegistryError_DataTypeAlreadyRegistered](https://developer.apple.com/documentation/coremedia/1473968-metadata_registry_error_codes/kcmmetadatadatatyperegistryerror_datatypealreadyregistered)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_DataTypeAlreadyRegistered: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_DataTypeAlreadyRegistered: OSStatus { get } ``` |

Modified [kCMMetadataDataTypeRegistryError_MultipleConformingBaseTypes](https://developer.apple.com/documentation/coremedia/1473968-metadata_registry_error_codes/kcmmetadatadatatyperegistryerror_multipleconformingbasetypes)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_MultipleConformingBaseTypes: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_MultipleConformingBaseTypes: OSStatus { get } ``` |

Modified [kCMMetadataDataTypeRegistryError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/1473968-metadata_registry_error_codes/kcmmetadatadatatyperegistryerror_requiredparametermissing)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_RequiredParameterMissing: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_RequiredParameterMissing: OSStatus { get } ``` |

Modified [kCMMetadataDataTypeRegistryError_RequiresConformingBaseType](https://developer.apple.com/documentation/coremedia/kcmmetadatadatatyperegistryerror_requiresconformingbasetype)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataDataTypeRegistryError_RequiresConformingBaseType: Int { get } ``` |
| To | ``` var kCMMetadataDataTypeRegistryError_RequiresConformingBaseType: OSStatus { get } ``` |

Modified [kCMMetadataFormatDescriptionKey_ConformingDataTypes](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_conformingdatatypes)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_ConformingDataTypes: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_ConformingDataTypes: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_DataType](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_datatype)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_DataType: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_DataType: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_DataTypeNamespace](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_datatypenamespace)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_DataTypeNamespace: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_DataTypeNamespace: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_LanguageTag](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_languagetag)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_LanguageTag: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_LanguageTag: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_LocalID](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_localid)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_LocalID: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_LocalID: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_Namespace](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_namespace)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_Namespace: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_Namespace: CFString ``` |

Modified [kCMMetadataFormatDescriptionKey_Value](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_value)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionKey_Value: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionKey_Value: CFString ``` |

Modified [kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_datatype)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_DataType: CFString ``` |

Modified [kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_extendedlanguagetag)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag: CFString ``` |

Modified [kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_identifier)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier: CFString! ``` |
| To | ``` let kCMMetadataFormatDescriptionMetadataSpecificationKey_Identifier: CFString ``` |

Modified [kCMMetadataFormatType_Boxed](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_boxed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataFormatType_Boxed: Int { get } ``` |
| To | ``` var kCMMetadataFormatType_Boxed: CMMetadataFormatType { get } ``` |

Modified [kCMMetadataFormatType_ICY](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_icy)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataFormatType_ICY: Int { get } ``` |
| To | ``` var kCMMetadataFormatType_ICY: CMMetadataFormatType { get } ``` |

Modified [kCMMetadataFormatType_ID3](https://developer.apple.com/documentation/coremedia/1564222-cmmetadataformattype/kcmmetadataformattype_id3)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataFormatType_ID3: Int { get } ``` |
| To | ``` var kCMMetadataFormatType_ID3: CMMetadataFormatType { get } ``` |

Modified [kCMMetadataIdentifier_QuickTimeMetadataDirection_Facing](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatadirection_facing)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataIdentifier_QuickTimeMetadataDirection_Facing: CFString! ``` |
| To | ``` let kCMMetadataIdentifier_QuickTimeMetadataDirection_Facing: CFString ``` |

Modified [kCMMetadataIdentifier_QuickTimeMetadataLocation_ISO6709](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatalocation_iso6709)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataIdentifier_QuickTimeMetadataLocation_ISO6709: CFString! ``` |
| To | ``` let kCMMetadataIdentifier_QuickTimeMetadataLocation_ISO6709: CFString ``` |

Modified [kCMMetadataIdentifier_QuickTimeMetadataPreferredAffineTransform](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatapreferredaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataIdentifier_QuickTimeMetadataPreferredAffineTransform: CFString! ``` |
| To | ``` let kCMMetadataIdentifier_QuickTimeMetadataPreferredAffineTransform: CFString ``` |

Modified [kCMMetadataIdentifierError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadIdentifier](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifiererror_badidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadIdentifier: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadIdentifier: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadKey](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_badkey)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadKey: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadKey: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadKeyLength](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_badkeylength)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadKeyLength: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadKeyLength: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadKeySpace](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifiererror_badkeyspace)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadKeySpace: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadKeySpace: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadKeyType](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifiererror_badkeytype)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadKeyType: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadKeyType: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_BadNumberKey](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_badnumberkey)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_BadNumberKey: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_BadNumberKey: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_NoKeyValueAvailable](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_nokeyvalueavailable)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_NoKeyValueAvailable: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_NoKeyValueAvailable: OSStatus { get } ``` |

Modified [kCMMetadataIdentifierError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/1474082-metadata_identifier_error_codes/kcmmetadataidentifiererror_requiredparametermissing)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMetadataIdentifierError_RequiredParameterMissing: Int { get } ``` |
| To | ``` var kCMMetadataIdentifierError_RequiredParameterMissing: OSStatus { get } ``` |

Modified [kCMMetadataKeySpace_Icy](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_icy)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_Icy: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_Icy: CFString ``` |

Modified [kCMMetadataKeySpace_ID3](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_id3)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_ID3: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_ID3: CFString ``` |

Modified [kCMMetadataKeySpace_ISOUserData](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_isouserdata)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_ISOUserData: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_ISOUserData: CFString ``` |

Modified [kCMMetadataKeySpace_iTunes](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_itunes)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_iTunes: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_iTunes: CFString ``` |

Modified [kCMMetadataKeySpace_QuickTimeMetadata](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_quicktimemetadata)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_QuickTimeMetadata: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_QuickTimeMetadata: CFString ``` |

Modified [kCMMetadataKeySpace_QuickTimeUserData](https://developer.apple.com/documentation/coremedia/kcmmetadatakeyspace_quicktimeuserdata)

|  | Declaration |
| --- | --- |
| From | ``` let kCMMetadataKeySpace_QuickTimeUserData: CFString! ``` |
| To | ``` let kCMMetadataKeySpace_QuickTimeUserData: CFString ``` |

Modified [kCMMPEG2VideoProfile_HDV_1080i50](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_hdv_1080i50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_1080i50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_1080i50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_1080i60](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_hdv_1080i60)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_1080i60: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_1080i60: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_1080p24](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_hdv_1080p24)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_1080p24: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_1080p24: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_1080p25](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_hdv_1080p25)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_1080p25: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_1080p25: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_1080p30](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_hdv_1080p30)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_1080p30: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_1080p30: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_720p24](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_hdv_720p24)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_720p24: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_720p24: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_720p25](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_hdv_720p25)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_720p25: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_720p25: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_720p30](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_hdv_720p30)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_720p30: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_720p30: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_720p50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_hdv_720p50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_720p50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_720p50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_HDV_720p60](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_hdv_720p60)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_HDV_720p60: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_HDV_720p60: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_1080i50_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_ex_1080i50_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080i50_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080i50_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_1080i60_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_ex_1080i60_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080i60_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080i60_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_1080p24_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_ex_1080p24_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p24_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p24_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_1080p25_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_1080p25_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p25_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p25_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_1080p30_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_ex_1080p30_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p30_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_1080p30_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_720p24_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_720p24_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p24_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p24_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_720p25_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_720p25_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p25_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p25_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_720p30_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_720p30_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p30_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p30_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_720p50_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_720p50_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p50_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p50_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_EX_720p60_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_ex_720p60_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p60_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_EX_720p60_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_1080i50_CBR50](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd422_1080i50_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080i50_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080i50_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_1080i60_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_1080i60_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080i60_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080i60_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_1080p24_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_1080p24_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p24_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p24_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_1080p25_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_1080p25_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p25_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p25_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_1080p30_CBR50](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd422_1080p30_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p30_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_1080p30_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_540p](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_540p)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_540p: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_540p: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p24_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p24_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p25_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p25_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p30_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p30_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_720p50_CBR50](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd422_720p50_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p50_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p50_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD422_720p60_CBR50](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd422_720p60_cbr50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p60_CBR50: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD422_720p60_CBR50: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_1080i50_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd_1080i50_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080i50_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080i50_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_1080i60_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd_1080i60_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080i60_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080i60_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_1080p24_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd_1080p24_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p24_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p24_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_1080p25_VBR35](https://developer.apple.com/documentation/coremedia/kcmmpeg2videoprofile_xdcam_hd_1080p25_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p25_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p25_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_1080p30_VBR35](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd_1080p30_vbr35)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p30_VBR35: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_1080p30_VBR35: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XDCAM_HD_540p](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xdcam_hd_540p)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XDCAM_HD_540p: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XDCAM_HD_540p: Int32 { get } ``` |

Modified [kCMMPEG2VideoProfile_XF](https://developer.apple.com/documentation/coremedia/1564241-video_profile_constants/kcmmpeg2videoprofile_xf)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMPEG2VideoProfile_XF: Int { get } ``` |
| To | ``` var kCMMPEG2VideoProfile_XF: Int32 { get } ``` |

Modified [kCMMuxedStreamType_DV](https://developer.apple.com/documentation/coremedia/1564230-cmmuxedstreamtype/kcmmuxedstreamtype_dv)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMuxedStreamType_DV: Int { get } ``` |
| To | ``` var kCMMuxedStreamType_DV: CMMuxedStreamType { get } ``` |

Modified [kCMMuxedStreamType_MPEG1System](https://developer.apple.com/documentation/coremedia/1564230-cmmuxedstreamtype/kcmmuxedstreamtype_mpeg1system)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMuxedStreamType_MPEG1System: Int { get } ``` |
| To | ``` var kCMMuxedStreamType_MPEG1System: CMMuxedStreamType { get } ``` |

Modified [kCMMuxedStreamType_MPEG2Program](https://developer.apple.com/documentation/coremedia/1564230-cmmuxedstreamtype/kcmmuxedstreamtype_mpeg2program)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMuxedStreamType_MPEG2Program: Int { get } ``` |
| To | ``` var kCMMuxedStreamType_MPEG2Program: CMMuxedStreamType { get } ``` |

Modified [kCMMuxedStreamType_MPEG2Transport](https://developer.apple.com/documentation/coremedia/1564230-cmmuxedstreamtype/kcmmuxedstreamtype_mpeg2transport)

|  | Declaration |
| --- | --- |
| From | ``` var kCMMuxedStreamType_MPEG2Transport: Int { get } ``` |
| To | ``` var kCMMuxedStreamType_MPEG2Transport: CMMuxedStreamType { get } ``` |

Modified [kCMPersistentTrackID_Invalid](https://developer.apple.com/documentation/coremedia/kcmpersistenttrackid_invalid)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPersistentTrackID_Invalid: Int { get } ``` |
| To | ``` var kCMPersistentTrackID_Invalid: CMPersistentTrackID { get } ``` |

Modified [kCMPixelFormat_16BE555](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_16be555)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_16BE555: Int { get } ``` |
| To | ``` var kCMPixelFormat_16BE555: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_16BE565](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_16be565)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_16BE565: Int { get } ``` |
| To | ``` var kCMPixelFormat_16BE565: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_16LE555](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_16le555)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_16LE555: Int { get } ``` |
| To | ``` var kCMPixelFormat_16LE555: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_16LE5551](https://developer.apple.com/documentation/coremedia/kcmpixelformat_16le5551)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_16LE5551: Int { get } ``` |
| To | ``` var kCMPixelFormat_16LE5551: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_16LE565](https://developer.apple.com/documentation/coremedia/kcmpixelformat_16le565)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_16LE565: Int { get } ``` |
| To | ``` var kCMPixelFormat_16LE565: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_24RGB](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_24rgb)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_24RGB: Int { get } ``` |
| To | ``` var kCMPixelFormat_24RGB: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_32ARGB](https://developer.apple.com/documentation/coremedia/kcmpixelformat_32argb)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_32ARGB: Int { get } ``` |
| To | ``` var kCMPixelFormat_32ARGB: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_32BGRA](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_32bgra)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_32BGRA: Int { get } ``` |
| To | ``` var kCMPixelFormat_32BGRA: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_422YpCbCr10](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_422ypcbcr10)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_422YpCbCr10: Int { get } ``` |
| To | ``` var kCMPixelFormat_422YpCbCr10: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_422YpCbCr16](https://developer.apple.com/documentation/coremedia/kcmpixelformat_422ypcbcr16)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_422YpCbCr16: Int { get } ``` |
| To | ``` var kCMPixelFormat_422YpCbCr16: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_422YpCbCr8](https://developer.apple.com/documentation/coremedia/kcmpixelformat_422ypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_422YpCbCr8: Int { get } ``` |
| To | ``` var kCMPixelFormat_422YpCbCr8: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_422YpCbCr8_yuvs](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_422ypcbcr8_yuvs)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_422YpCbCr8_yuvs: Int { get } ``` |
| To | ``` var kCMPixelFormat_422YpCbCr8_yuvs: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_4444YpCbCrA8](https://developer.apple.com/documentation/coremedia/kcmpixelformat_4444ypcbcra8)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_4444YpCbCrA8: Int { get } ``` |
| To | ``` var kCMPixelFormat_4444YpCbCrA8: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_444YpCbCr10](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_444ypcbcr10)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_444YpCbCr10: Int { get } ``` |
| To | ``` var kCMPixelFormat_444YpCbCr10: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_444YpCbCr8](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_444ypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_444YpCbCr8: Int { get } ``` |
| To | ``` var kCMPixelFormat_444YpCbCr8: CMPixelFormatType { get } ``` |

Modified [kCMPixelFormat_8IndexedGray_WhiteIsZero](https://developer.apple.com/documentation/coremedia/1564244-video_pixel_format_constants/kcmpixelformat_8indexedgray_whiteiszero)

|  | Declaration |
| --- | --- |
| From | ``` var kCMPixelFormat_8IndexedGray_WhiteIsZero: Int { get } ``` |
| To | ``` var kCMPixelFormat_8IndexedGray_WhiteIsZero: CMPixelFormatType { get } ``` |

Modified [kCMSampleAttachmentKey_DependsOnOthers](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_dependsonothers)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_DependsOnOthers: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_DependsOnOthers: CFString ``` |

Modified [kCMSampleAttachmentKey_DisplayImmediately](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_displayimmediately)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_DisplayImmediately: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_DisplayImmediately: CFString ``` |

Modified [kCMSampleAttachmentKey_DoNotDisplay](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_donotdisplay)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_DoNotDisplay: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_DoNotDisplay: CFString ``` |

Modified [kCMSampleAttachmentKey_EarlierDisplayTimesAllowed](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_earlierdisplaytimesallowed)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_EarlierDisplayTimesAllowed: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_EarlierDisplayTimesAllowed: CFString ``` |

Modified [kCMSampleAttachmentKey_HasRedundantCoding](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_hasredundantcoding)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_HasRedundantCoding: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_HasRedundantCoding: CFString ``` |

Modified [kCMSampleAttachmentKey_IsDependedOnByOthers](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_isdependedonbyothers)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_IsDependedOnByOthers: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_IsDependedOnByOthers: CFString ``` |

Modified [kCMSampleAttachmentKey_NotSync](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_notsync)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_NotSync: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_NotSync: CFString ``` |

Modified [kCMSampleAttachmentKey_PartialSync](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_partialsync)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleAttachmentKey_PartialSync: CFString! ``` |
| To | ``` let kCMSampleAttachmentKey_PartialSync: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_displayemptymediaimmediately)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_DrainAfterDecoding](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_drainafterdecoding)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_DrainAfterDecoding: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_DrainAfterDecoding: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_DroppedFrameReason](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_droppedframereason)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_DroppedFrameReason: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_DroppedFrameReason: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_droppedframereasoninfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_EmptyMedia](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_emptymedia)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_EmptyMedia: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_EmptyMedia: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_endsprevioussampleduration)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_filldiscontinuitieswithsilence)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_ForceKeyFrame](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_forcekeyframe)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_ForceKeyFrame: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_ForceKeyFrame: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_GradualDecoderRefresh](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_gradualdecoderrefresh)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_GradualDecoderRefresh: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_GradualDecoderRefresh: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_PermanentEmptyMedia](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_permanentemptymedia)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_PermanentEmptyMedia: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_PermanentEmptyMedia: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_postnotificationwhenconsumed)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_resetdecoderbeforedecoding)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_ResumeOutput](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_resumeoutput)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_ResumeOutput: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_ResumeOutput: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_Reverse](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_reverse)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_Reverse: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_Reverse: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_SampleReferenceByteOffset](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_samplereferencebyteoffset)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_SampleReferenceByteOffset: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_SampleReferenceByteOffset: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_SampleReferenceURL](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_samplereferenceurl)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_SampleReferenceURL: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_SampleReferenceURL: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_SpeedMultiplier](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_speedmultiplier)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_SpeedMultiplier: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_SpeedMultiplier: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_TransitionID](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_transitionid)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_TransitionID: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_TransitionID: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_TrimDurationAtEnd](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_trimdurationatend)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_TrimDurationAtEnd: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_TrimDurationAtEnd: CFString ``` |

Modified [kCMSampleBufferAttachmentKey_TrimDurationAtStart](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_trimdurationatstart)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferAttachmentKey_TrimDurationAtStart: CFString! ``` |
| To | ``` let kCMSampleBufferAttachmentKey_TrimDurationAtStart: CFString ``` |

Modified [kCMSampleBufferConduitNotification_InhibitOutputUntil](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotification_inhibitoutputuntil)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotification_InhibitOutputUntil: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotification_InhibitOutputUntil: CFString ``` |

Modified [kCMSampleBufferConduitNotification_ResetOutput](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotification_resetoutput)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotification_ResetOutput: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotification_ResetOutput: CFString ``` |

Modified [kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged: CFString ``` |

Modified [kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS: CFString ``` |

Modified [kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS: CFString ``` |

Modified [kCMSampleBufferConduitNotificationParameter_ResumeTag](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_resumetag)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString ``` |

Modified [kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange: CFString! ``` |
| To | ``` let kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange: CFString ``` |

Modified [kCMSampleBufferConsumerNotification_BufferConsumed](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconsumernotification_bufferconsumed)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferConsumerNotification_BufferConsumed: CFString! ``` |
| To | ``` let kCMSampleBufferConsumerNotification_BufferConsumed: CFString ``` |

Modified [kCMSampleBufferDroppedFrameReason_Discontinuity](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_discontinuity)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferDroppedFrameReason_Discontinuity: CFString! ``` |
| To | ``` let kCMSampleBufferDroppedFrameReason_Discontinuity: CFString ``` |

Modified [kCMSampleBufferDroppedFrameReason_FrameWasLate](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_framewaslate)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferDroppedFrameReason_FrameWasLate: CFString! ``` |
| To | ``` let kCMSampleBufferDroppedFrameReason_FrameWasLate: CFString ``` |

Modified [kCMSampleBufferDroppedFrameReason_OutOfBuffers](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_outofbuffers)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferDroppedFrameReason_OutOfBuffers: CFString! ``` |
| To | ``` let kCMSampleBufferDroppedFrameReason_OutOfBuffers: CFString ``` |

Modified [kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereasoninfo_cameramodeswitch)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch: CFString! ``` |
| To | ``` let kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch: CFString ``` |

Modified [kCMSampleBufferError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMSampleBufferError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMSampleBufferError_AlreadyHasDataBuffer](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_alreadyhasdatabuffer)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_AlreadyHasDataBuffer: Int { get } ``` |
| To | ``` var kCMSampleBufferError_AlreadyHasDataBuffer: OSStatus { get } ``` |

Modified [kCMSampleBufferError_ArrayTooSmall](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_arraytoosmall)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_ArrayTooSmall: Int { get } ``` |
| To | ``` var kCMSampleBufferError_ArrayTooSmall: OSStatus { get } ``` |

Modified [kCMSampleBufferError_BufferHasNoSampleSizes](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_bufferhasnosamplesizes)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_BufferHasNoSampleSizes: Int { get } ``` |
| To | ``` var kCMSampleBufferError_BufferHasNoSampleSizes: OSStatus { get } ``` |

Modified [kCMSampleBufferError_BufferHasNoSampleTimingInfo](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_bufferhasnosampletiminginfo)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_BufferHasNoSampleTimingInfo: Int { get } ``` |
| To | ``` var kCMSampleBufferError_BufferHasNoSampleTimingInfo: OSStatus { get } ``` |

Modified [kCMSampleBufferError_BufferNotReady](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_buffernotready)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_BufferNotReady: Int { get } ``` |
| To | ``` var kCMSampleBufferError_BufferNotReady: OSStatus { get } ``` |

Modified [kCMSampleBufferError_CannotSubdivide](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_cannotsubdivide)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_CannotSubdivide: Int { get } ``` |
| To | ``` var kCMSampleBufferError_CannotSubdivide: OSStatus { get } ``` |

Modified [kCMSampleBufferError_DataCanceled](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_datacanceled)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_DataCanceled: Int { get } ``` |
| To | ``` var kCMSampleBufferError_DataCanceled: OSStatus { get } ``` |

Modified [kCMSampleBufferError_DataFailed](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_datafailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_DataFailed: Int { get } ``` |
| To | ``` var kCMSampleBufferError_DataFailed: OSStatus { get } ``` |

Modified [kCMSampleBufferError_Invalidated](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_invalidated)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_Invalidated: Int { get } ``` |
| To | ``` var kCMSampleBufferError_Invalidated: OSStatus { get } ``` |

Modified [kCMSampleBufferError_InvalidEntryCount](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_invalidentrycount)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_InvalidEntryCount: Int { get } ``` |
| To | ``` var kCMSampleBufferError_InvalidEntryCount: OSStatus { get } ``` |

Modified [kCMSampleBufferError_InvalidMediaFormat](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_invalidmediaformat)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_InvalidMediaFormat: Int { get } ``` |
| To | ``` var kCMSampleBufferError_InvalidMediaFormat: OSStatus { get } ``` |

Modified [kCMSampleBufferError_InvalidMediaTypeForOperation](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_invalidmediatypeforoperation)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_InvalidMediaTypeForOperation: Int { get } ``` |
| To | ``` var kCMSampleBufferError_InvalidMediaTypeForOperation: OSStatus { get } ``` |

Modified [kCMSampleBufferError_InvalidSampleData](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_invalidsampledata)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_InvalidSampleData: Int { get } ``` |
| To | ``` var kCMSampleBufferError_InvalidSampleData: OSStatus { get } ``` |

Modified [kCMSampleBufferError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_requiredparametermissing)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_RequiredParameterMissing: Int { get } ``` |
| To | ``` var kCMSampleBufferError_RequiredParameterMissing: OSStatus { get } ``` |

Modified [kCMSampleBufferError_SampleIndexOutOfRange](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_sampleindexoutofrange)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_SampleIndexOutOfRange: Int { get } ``` |
| To | ``` var kCMSampleBufferError_SampleIndexOutOfRange: OSStatus { get } ``` |

Modified [kCMSampleBufferError_SampleTimingInfoInvalid](https://developer.apple.com/documentation/coremedia/1495039-sample_buffer_error_codes/kcmsamplebuffererror_sampletiminginfoinvalid)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferError_SampleTimingInfoInvalid: Int { get } ``` |
| To | ``` var kCMSampleBufferError_SampleTimingInfoInvalid: OSStatus { get } ``` |

Modified [kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment](https://developer.apple.com/documentation/coremedia/kcmsamplebufferflag_audiobufferlist_assure16bytealignment)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment: Int { get } ``` |
| To | ``` var kCMSampleBufferFlag_AudioBufferList_Assure16ByteAlignment: UInt32 { get } ``` |

Modified [kCMSampleBufferNotification_DataBecameReady](https://developer.apple.com/documentation/coremedia/kcmsamplebuffernotification_databecameready)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferNotification_DataBecameReady: CFString! ``` |
| To | ``` let kCMSampleBufferNotification_DataBecameReady: CFString ``` |

Modified [kCMSampleBufferNotification_DataFailed](https://developer.apple.com/documentation/coremedia/kcmsamplebuffernotification_datafailed)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferNotification_DataFailed: CFString! ``` |
| To | ``` let kCMSampleBufferNotification_DataFailed: CFString ``` |

Modified [kCMSampleBufferNotificationParameter_OSStatus](https://developer.apple.com/documentation/coremedia/kcmsamplebuffernotificationparameter_osstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSampleBufferNotificationParameter_OSStatus: CFString! ``` |
| To | ``` let kCMSampleBufferNotificationParameter_OSStatus: CFString ``` |

Modified [kCMSimpleQueueError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmsimplequeueerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSimpleQueueError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMSimpleQueueError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMSimpleQueueError_ParameterOutOfRange](https://developer.apple.com/documentation/coremedia/kcmsimplequeueerror_parameteroutofrange)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSimpleQueueError_ParameterOutOfRange: Int { get } ``` |
| To | ``` var kCMSimpleQueueError_ParameterOutOfRange: OSStatus { get } ``` |

Modified [kCMSimpleQueueError_QueueIsFull](https://developer.apple.com/documentation/coremedia/1584369-simple_queue_error_codes/kcmsimplequeueerror_queueisfull)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSimpleQueueError_QueueIsFull: Int { get } ``` |
| To | ``` var kCMSimpleQueueError_QueueIsFull: OSStatus { get } ``` |

Modified [kCMSimpleQueueError_RequiredParameterMissing](https://developer.apple.com/documentation/coremedia/kcmsimplequeueerror_requiredparametermissing)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSimpleQueueError_RequiredParameterMissing: Int { get } ``` |
| To | ``` var kCMSimpleQueueError_RequiredParameterMissing: OSStatus { get } ``` |

Modified [kCMSoundDescriptionFlavor_3GPFamily](https://developer.apple.com/documentation/coremedia/cmsounddescriptionflavor/1416248-mobile3gpfamily)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSoundDescriptionFlavor_3GPFamily: CFString! ``` |
| To | ``` let kCMSoundDescriptionFlavor_3GPFamily: CFString ``` |

Modified [kCMSoundDescriptionFlavor_ISOFamily](https://developer.apple.com/documentation/coremedia/cmsounddescriptionflavor/1416311-isofamily)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSoundDescriptionFlavor_ISOFamily: CFString! ``` |
| To | ``` let kCMSoundDescriptionFlavor_ISOFamily: CFString ``` |

Modified [kCMSoundDescriptionFlavor_QuickTimeMovie](https://developer.apple.com/documentation/coremedia/cmsounddescriptionflavor/1416274-quicktimemovie)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSoundDescriptionFlavor_QuickTimeMovie: CFString! ``` |
| To | ``` let kCMSoundDescriptionFlavor_QuickTimeMovie: CFString ``` |

Modified [kCMSoundDescriptionFlavor_QuickTimeMovieV2](https://developer.apple.com/documentation/coremedia/kcmsounddescriptionflavor_quicktimemoviev2)

|  | Declaration |
| --- | --- |
| From | ``` let kCMSoundDescriptionFlavor_QuickTimeMovieV2: CFString! ``` |
| To | ``` let kCMSoundDescriptionFlavor_QuickTimeMovieV2: CFString ``` |

Modified [kCMSubtitleFormatType_3GText](https://developer.apple.com/documentation/coremedia/1564237-cmsubtitleformattype/kcmsubtitleformattype_3gtext)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSubtitleFormatType_3GText: Int { get } ``` |
| To | ``` var kCMSubtitleFormatType_3GText: CMSubtitleFormatType { get } ``` |

Modified [kCMSubtitleFormatType_WebVTT](https://developer.apple.com/documentation/coremedia/1564237-cmsubtitleformattype/kcmsubtitleformattype_webvtt)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSubtitleFormatType_WebVTT: Int { get } ``` |
| To | ``` var kCMSubtitleFormatType_WebVTT: CMSubtitleFormatType { get } ``` |

Modified [kCMSyncError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1509590-cmsync_error_codes/kcmsyncerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSyncError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMSyncError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMSyncError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1509590-cmsync_error_codes/kcmsyncerror_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSyncError_InvalidParameter: Int { get } ``` |
| To | ``` var kCMSyncError_InvalidParameter: OSStatus { get } ``` |

Modified [kCMSyncError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/1509590-cmsync_error_codes/kcmsyncerror_missingrequiredparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSyncError_MissingRequiredParameter: Int { get } ``` |
| To | ``` var kCMSyncError_MissingRequiredParameter: OSStatus { get } ``` |

Modified [kCMSyncError_RateMustBeNonZero](https://developer.apple.com/documentation/coremedia/kcmsyncerror_ratemustbenonzero)

|  | Declaration |
| --- | --- |
| From | ``` var kCMSyncError_RateMustBeNonZero: Int { get } ``` |
| To | ``` var kCMSyncError_RateMustBeNonZero: OSStatus { get } ``` |

Modified [kCMTextDisplayFlag_allSubtitlesForced](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_allsubtitlesforced)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_allSubtitlesForced: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_allSubtitlesForced: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_continuousKaraoke](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_continuouskaraoke)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_continuousKaraoke: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_continuousKaraoke: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_fillTextRegion](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_filltextregion)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_fillTextRegion: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_fillTextRegion: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_forcedSubtitlesPresent](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_forcedsubtitlespresent)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_forcedSubtitlesPresent: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_forcedSubtitlesPresent: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_obeySubtitleFormatting](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_obeysubtitleformatting)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_obeySubtitleFormatting: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_obeySubtitleFormatting: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollDirection_bottomToTop](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_scrolldirection_bottomtotop)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollDirection_bottomToTop: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollDirection_bottomToTop: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollDirection_leftToRight](https://developer.apple.com/documentation/coremedia/1564197-text_display_flags/kcmtextdisplayflag_scrolldirection_lefttoright)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollDirection_leftToRight: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollDirection_leftToRight: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollDirection_rightToLeft](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_scrolldirection_righttoleft)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollDirection_rightToLeft: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollDirection_rightToLeft: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollDirection_topToBottom](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_scrolldirection_toptobottom)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollDirection_topToBottom: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollDirection_topToBottom: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollDirectionMask](https://developer.apple.com/documentation/coremedia/1564197-text_display_flags/kcmtextdisplayflag_scrolldirectionmask)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollDirectionMask: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollDirectionMask: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollIn](https://developer.apple.com/documentation/coremedia/1564197-text_display_flags/kcmtextdisplayflag_scrollin)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollIn: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollIn: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_scrollOut](https://developer.apple.com/documentation/coremedia/1564197-text_display_flags/kcmtextdisplayflag_scrollout)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_scrollOut: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_scrollOut: CMTextDisplayFlags { get } ``` |

Modified [kCMTextDisplayFlag_writeTextVertically](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_writetextvertically)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextDisplayFlag_writeTextVertically: UInt32 { get } ``` |
| To | ``` var kCMTextDisplayFlag_writeTextVertically: CMTextDisplayFlags { get } ``` |

Modified [kCMTextFormatDescriptionColor_Alpha](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptioncolor_alpha)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionColor_Alpha: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionColor_Alpha: CFString ``` |

Modified [kCMTextFormatDescriptionColor_Blue](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptioncolor_blue)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionColor_Blue: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionColor_Blue: CFString ``` |

Modified [kCMTextFormatDescriptionColor_Green](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptioncolor_green)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionColor_Green: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionColor_Green: CFString ``` |

Modified [kCMTextFormatDescriptionColor_Red](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptioncolor_red)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionColor_Red: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionColor_Red: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_BackgroundColor](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_BackgroundColor: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_BackgroundColor: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_DefaultFontName](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_defaultfontname)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_DefaultFontName: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_DefaultFontName: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_DefaultStyle](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_defaultstyle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_DefaultStyle: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_DefaultStyle: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_DefaultTextBox](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_defaulttextbox)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_DefaultTextBox: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_DefaultTextBox: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_DisplayFlags](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_displayflags)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_DisplayFlags: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_DisplayFlags: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_FontTable](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_fonttable)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_FontTable: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_FontTable: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_HorizontalJustification](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_horizontaljustification)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_HorizontalJustification: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_HorizontalJustification: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_TextJustification](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_textjustification)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_TextJustification: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_TextJustification: CFString ``` |

Modified [kCMTextFormatDescriptionExtension_VerticalJustification](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionextension_verticaljustification)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionExtension_VerticalJustification: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionExtension_VerticalJustification: CFString ``` |

Modified [kCMTextFormatDescriptionRect_Bottom](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionrect_bottom)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionRect_Bottom: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionRect_Bottom: CFString ``` |

Modified [kCMTextFormatDescriptionRect_Left](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionrect_left)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionRect_Left: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionRect_Left: CFString ``` |

Modified [kCMTextFormatDescriptionRect_Right](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionrect_right)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionRect_Right: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionRect_Right: CFString ``` |

Modified [kCMTextFormatDescriptionRect_Top](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionrect_top)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionRect_Top: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionRect_Top: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_Ascent](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_ascent)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_Ascent: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_Ascent: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_EndChar](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_endchar)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_EndChar: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_EndChar: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_Font](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_font)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_Font: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_Font: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_FontFace](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_fontface)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_FontFace: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_FontFace: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_FontSize](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_fontsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_FontSize: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_FontSize: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_ForegroundColor](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_foregroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_ForegroundColor: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_ForegroundColor: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_Height](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_height)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_Height: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_Height: CFString ``` |

Modified [kCMTextFormatDescriptionStyle_StartChar](https://developer.apple.com/documentation/coremedia/kcmtextformatdescriptionstyle_startchar)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextFormatDescriptionStyle_StartChar: CFString! ``` |
| To | ``` let kCMTextFormatDescriptionStyle_StartChar: CFString ``` |

Modified [kCMTextFormatType_3GText](https://developer.apple.com/documentation/coremedia/kcmtextformattype_3gtext)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextFormatType_3GText: Int { get } ``` |
| To | ``` var kCMTextFormatType_3GText: CMTextFormatType { get } ``` |

Modified [kCMTextFormatType_QTText](https://developer.apple.com/documentation/coremedia/kcmtextformattype_qttext)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextFormatType_QTText: Int { get } ``` |
| To | ``` var kCMTextFormatType_QTText: CMTextFormatType { get } ``` |

Modified [kCMTextJustification_bottom_right](https://developer.apple.com/documentation/coremedia/kcmtextjustification_bottom_right)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextJustification_bottom_right: Int { get } ``` |
| To | ``` var kCMTextJustification_bottom_right: CMTextJustificationValue { get } ``` |

Modified [kCMTextJustification_centered](https://developer.apple.com/documentation/coremedia/1564228-text_justification_constants/kcmtextjustification_centered)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextJustification_centered: Int { get } ``` |
| To | ``` var kCMTextJustification_centered: CMTextJustificationValue { get } ``` |

Modified [kCMTextJustification_left_top](https://developer.apple.com/documentation/coremedia/1564228-text_justification_constants/kcmtextjustification_left_top)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTextJustification_left_top: Int { get } ``` |
| To | ``` var kCMTextJustification_left_top: CMTextJustificationValue { get } ``` |

Modified [kCMTextMarkupAlignmentType_End](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_end)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAlignmentType_End: CFString! ``` |
| To | ``` let kCMTextMarkupAlignmentType_End: CFString ``` |

Modified [kCMTextMarkupAlignmentType_Left](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_left)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAlignmentType_Left: CFString! ``` |
| To | ``` let kCMTextMarkupAlignmentType_Left: CFString ``` |

Modified [kCMTextMarkupAlignmentType_Middle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_middle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAlignmentType_Middle: CFString! ``` |
| To | ``` let kCMTextMarkupAlignmentType_Middle: CFString ``` |

Modified [kCMTextMarkupAlignmentType_Right](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_right)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAlignmentType_Right: CFString! ``` |
| To | ``` let kCMTextMarkupAlignmentType_Right: CFString ``` |

Modified [kCMTextMarkupAlignmentType_Start](https://developer.apple.com/documentation/coremedia/kcmtextmarkupalignmenttype_start)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAlignmentType_Start: CFString! ``` |
| To | ``` let kCMTextMarkupAlignmentType_Start: CFString ``` |

Modified [kCMTextMarkupAttribute_Alignment](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_alignment)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_Alignment: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_Alignment: CFString ``` |

Modified [kCMTextMarkupAttribute_BackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_backgroundcolorargb)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_BackgroundColorARGB: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_BackgroundColorARGB: CFString ``` |

Modified [kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_basefontsizepercentagerelativetovideoheight)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_BaseFontSizePercentageRelativeToVideoHeight: CFString ``` |

Modified [kCMTextMarkupAttribute_BoldStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_boldstyle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_BoldStyle: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_BoldStyle: CFString ``` |

Modified [kCMTextMarkupAttribute_CharacterBackgroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characterbackgroundcolorargb)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_CharacterBackgroundColorARGB: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_CharacterBackgroundColorARGB: CFString ``` |

Modified [kCMTextMarkupAttribute_CharacterEdgeStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_characteredgestyle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_CharacterEdgeStyle: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_CharacterEdgeStyle: CFString ``` |

Modified [kCMTextMarkupAttribute_FontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_fontfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_FontFamilyName: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_FontFamilyName: CFString ``` |

Modified [kCMTextMarkupAttribute_ForegroundColorARGB](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_foregroundcolorargb)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_ForegroundColorARGB: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_ForegroundColorARGB: CFString ``` |

Modified [kCMTextMarkupAttribute_GenericFontFamilyName](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_genericfontfamilyname)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_GenericFontFamilyName: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_GenericFontFamilyName: CFString ``` |

Modified [kCMTextMarkupAttribute_ItalicStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_italicstyle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_ItalicStyle: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_ItalicStyle: CFString ``` |

Modified [kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString ``` |

Modified [kCMTextMarkupAttribute_RelativeFontSize](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_relativefontsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_RelativeFontSize: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_RelativeFontSize: CFString ``` |

Modified [kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString ``` |

Modified [kCMTextMarkupAttribute_UnderlineStyle](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_underlinestyle)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_UnderlineStyle: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_UnderlineStyle: CFString ``` |

Modified [kCMTextMarkupAttribute_VerticalLayout](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_verticallayout)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_VerticalLayout: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_VerticalLayout: CFString ``` |

Modified [kCMTextMarkupAttribute_WritingDirectionSizePercentage](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_writingdirectionsizepercentage)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString! ``` |
| To | ``` let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString ``` |

Modified [kCMTextMarkupCharacterEdgeStyle_Depressed](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_depressed)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupCharacterEdgeStyle_Depressed: CFString! ``` |
| To | ``` let kCMTextMarkupCharacterEdgeStyle_Depressed: CFString ``` |

Modified [kCMTextMarkupCharacterEdgeStyle_DropShadow](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_dropshadow)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupCharacterEdgeStyle_DropShadow: CFString! ``` |
| To | ``` let kCMTextMarkupCharacterEdgeStyle_DropShadow: CFString ``` |

Modified [kCMTextMarkupCharacterEdgeStyle_None](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_none)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupCharacterEdgeStyle_None: CFString! ``` |
| To | ``` let kCMTextMarkupCharacterEdgeStyle_None: CFString ``` |

Modified [kCMTextMarkupCharacterEdgeStyle_Raised](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_raised)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupCharacterEdgeStyle_Raised: CFString! ``` |
| To | ``` let kCMTextMarkupCharacterEdgeStyle_Raised: CFString ``` |

Modified [kCMTextMarkupCharacterEdgeStyle_Uniform](https://developer.apple.com/documentation/coremedia/kcmtextmarkupcharacteredgestyle_uniform)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupCharacterEdgeStyle_Uniform: CFString! ``` |
| To | ``` let kCMTextMarkupCharacterEdgeStyle_Uniform: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Casual](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_casual)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Casual: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Casual: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Cursive](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_cursive)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Cursive: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Cursive: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Default](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_default)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Default: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Default: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Fantasy](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_fantasy)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Fantasy: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Fantasy: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Monospace](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospace)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Monospace: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Monospace: CFString ``` |

Modified [kCMTextMarkupGenericFontName_MonospaceSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospacesansserif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_MonospaceSansSerif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_MonospaceSansSerif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_MonospaceSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_monospaceserif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_MonospaceSerif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_MonospaceSerif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_ProportionalSansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalsansserif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_ProportionalSansSerif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_ProportionalSansSerif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_ProportionalSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_proportionalserif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_ProportionalSerif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_ProportionalSerif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_SansSerif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_sansserif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_SansSerif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_SansSerif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_Serif](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_serif)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_Serif: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_Serif: CFString ``` |

Modified [kCMTextMarkupGenericFontName_SmallCapital](https://developer.apple.com/documentation/coremedia/kcmtextmarkupgenericfontname_smallcapital)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextMarkupGenericFontName_SmallCapital: CFString! ``` |
| To | ``` let kCMTextMarkupGenericFontName_SmallCapital: CFString ``` |

Modified [kCMTextVerticalLayout_LeftToRight](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_lefttoright)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextVerticalLayout_LeftToRight: CFString! ``` |
| To | ``` let kCMTextVerticalLayout_LeftToRight: CFString ``` |

Modified [kCMTextVerticalLayout_RightToLeft](https://developer.apple.com/documentation/coremedia/kcmtextverticallayout_righttoleft)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTextVerticalLayout_RightToLeft: CFString! ``` |
| To | ``` let kCMTextVerticalLayout_RightToLeft: CFString ``` |

Modified [kCMTimebaseError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_allocationfailed)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimebaseError_AllocationFailed: Int { get } ``` |
| To | ``` var kCMTimebaseError_AllocationFailed: OSStatus { get } ``` |

Modified [kCMTimebaseError_InvalidParameter](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimebaseError_InvalidParameter: Int { get } ``` |
| To | ``` var kCMTimebaseError_InvalidParameter: OSStatus { get } ``` |

Modified [kCMTimebaseError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_missingrequiredparameter)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimebaseError_MissingRequiredParameter: Int { get } ``` |
| To | ``` var kCMTimebaseError_MissingRequiredParameter: OSStatus { get } ``` |

Modified [kCMTimebaseError_ReadOnly](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_readonly)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimebaseError_ReadOnly: Int { get } ``` |
| To | ``` var kCMTimebaseError_ReadOnly: OSStatus { get } ``` |

Modified [kCMTimebaseError_TimerIntervalTooShort](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_timerintervaltooshort)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimebaseError_TimerIntervalTooShort: Int { get } ``` |
| To | ``` var kCMTimebaseError_TimerIntervalTooShort: OSStatus { get } ``` |

Modified [kCMTimebaseNotification_EffectiveRateChanged](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_effectiveratechanged)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimebaseNotification_EffectiveRateChanged: CFString! ``` |
| To | ``` let kCMTimebaseNotification_EffectiveRateChanged: CFString ``` |

Modified [kCMTimebaseNotification_TimeJumped](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_timejumped)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimebaseNotification_TimeJumped: CFString! ``` |
| To | ``` let kCMTimebaseNotification_TimeJumped: CFString ``` |

Modified [kCMTimebaseNotificationKey_EventTime](https://developer.apple.com/documentation/coremedia/kcmtimebasenotificationkey_eventtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimebaseNotificationKey_EventTime: CFString! ``` |
| To | ``` let kCMTimebaseNotificationKey_EventTime: CFString ``` |

Modified [kCMTimeCodeFlag_24HourMax](https://developer.apple.com/documentation/coremedia/1564243-time_code_flags/kcmtimecodeflag_24hourmax)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFlag_24HourMax: Int { get } ``` |
| To | ``` var kCMTimeCodeFlag_24HourMax: UInt32 { get } ``` |

Modified [kCMTimeCodeFlag_DropFrame](https://developer.apple.com/documentation/coremedia/kcmtimecodeflag_dropframe)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFlag_DropFrame: Int { get } ``` |
| To | ``` var kCMTimeCodeFlag_DropFrame: UInt32 { get } ``` |

Modified [kCMTimeCodeFlag_NegTimesOK](https://developer.apple.com/documentation/coremedia/kcmtimecodeflag_negtimesok)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFlag_NegTimesOK: Int { get } ``` |
| To | ``` var kCMTimeCodeFlag_NegTimesOK: UInt32 { get } ``` |

Modified [kCMTimeCodeFormatDescriptionExtension_SourceReferenceName](https://developer.apple.com/documentation/coremedia/kcmtimecodeformatdescriptionextension_sourcereferencename)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeCodeFormatDescriptionExtension_SourceReferenceName: CFString! ``` |
| To | ``` let kCMTimeCodeFormatDescriptionExtension_SourceReferenceName: CFString ``` |

Modified [kCMTimeCodeFormatDescriptionKey_LangCode](https://developer.apple.com/documentation/coremedia/kcmtimecodeformatdescriptionkey_langcode)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeCodeFormatDescriptionKey_LangCode: CFString! ``` |
| To | ``` let kCMTimeCodeFormatDescriptionKey_LangCode: CFString ``` |

Modified [kCMTimeCodeFormatDescriptionKey_Value](https://developer.apple.com/documentation/coremedia/kcmtimecodeformatdescriptionkey_value)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeCodeFormatDescriptionKey_Value: CFString! ``` |
| To | ``` let kCMTimeCodeFormatDescriptionKey_Value: CFString ``` |

Modified [kCMTimeCodeFormatType_Counter32](https://developer.apple.com/documentation/coremedia/kcmtimecodeformattype_counter32)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFormatType_Counter32: Int { get } ``` |
| To | ``` var kCMTimeCodeFormatType_Counter32: CMTimeCodeFormatType { get } ``` |

Modified [kCMTimeCodeFormatType_Counter64](https://developer.apple.com/documentation/coremedia/kcmtimecodeformattype_counter64)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFormatType_Counter64: Int { get } ``` |
| To | ``` var kCMTimeCodeFormatType_Counter64: CMTimeCodeFormatType { get } ``` |

Modified [kCMTimeCodeFormatType_TimeCode32](https://developer.apple.com/documentation/coremedia/1564226-cmtimecodeformattype/kcmtimecodeformattype_timecode32)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFormatType_TimeCode32: Int { get } ``` |
| To | ``` var kCMTimeCodeFormatType_TimeCode32: CMTimeCodeFormatType { get } ``` |

Modified [kCMTimeCodeFormatType_TimeCode64](https://developer.apple.com/documentation/coremedia/1564226-cmtimecodeformattype/kcmtimecodeformattype_timecode64)

|  | Declaration |
| --- | --- |
| From | ``` var kCMTimeCodeFormatType_TimeCode64: Int { get } ``` |
| To | ``` var kCMTimeCodeFormatType_TimeCode64: CMTimeCodeFormatType { get } ``` |

Modified [kCMTimeEpochKey](https://developer.apple.com/documentation/coremedia/kcmtimeepochkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeEpochKey: CFString! ``` |
| To | ``` let kCMTimeEpochKey: CFString ``` |

Modified [kCMTimeFlagsKey](https://developer.apple.com/documentation/coremedia/kcmtimeflagskey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeFlagsKey: CFString! ``` |
| To | ``` let kCMTimeFlagsKey: CFString ``` |

Modified [kCMTimeRangeDurationKey](https://developer.apple.com/documentation/coremedia/kcmtimerangedurationkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeRangeDurationKey: CFString! ``` |
| To | ``` let kCMTimeRangeDurationKey: CFString ``` |

Modified [kCMTimeRangeStartKey](https://developer.apple.com/documentation/coremedia/kcmtimerangestartkey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeRangeStartKey: CFString! ``` |
| To | ``` let kCMTimeRangeStartKey: CFString ``` |

Modified [kCMTimeScaleKey](https://developer.apple.com/documentation/coremedia/kcmtimescalekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeScaleKey: CFString! ``` |
| To | ``` let kCMTimeScaleKey: CFString ``` |

Modified [kCMTimeValueKey](https://developer.apple.com/documentation/coremedia/kcmtimevaluekey)

|  | Declaration |
| --- | --- |
| From | ``` let kCMTimeValueKey: CFString! ``` |
| To | ``` let kCMTimeValueKey: CFString ``` |

Modified [kCMVideoCodecType_422YpCbCr8](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_422ypcbcr8)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_422YpCbCr8: Int { get } ``` |
| To | ``` var kCMVideoCodecType_422YpCbCr8: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_Animation](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_animation)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_Animation: Int { get } ``` |
| To | ``` var kCMVideoCodecType_Animation: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_AppleProRes422](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores422)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_AppleProRes422: Int { get } ``` |
| To | ``` var kCMVideoCodecType_AppleProRes422: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_AppleProRes422HQ](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_appleprores422hq)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_AppleProRes422HQ: Int { get } ``` |
| To | ``` var kCMVideoCodecType_AppleProRes422HQ: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_AppleProRes422LT](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores422lt)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_AppleProRes422LT: Int { get } ``` |
| To | ``` var kCMVideoCodecType_AppleProRes422LT: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_AppleProRes422Proxy](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores422proxy)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_AppleProRes422Proxy: Int { get } ``` |
| To | ``` var kCMVideoCodecType_AppleProRes422Proxy: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_AppleProRes4444](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_appleprores4444)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_AppleProRes4444: Int { get } ``` |
| To | ``` var kCMVideoCodecType_AppleProRes4444: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_Cinepak](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_cinepak)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_Cinepak: Int { get } ``` |
| To | ``` var kCMVideoCodecType_Cinepak: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCNTSC](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcntsc)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCNTSC: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCNTSC: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPAL](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_dvcpal)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPAL: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPAL: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPro50NTSC](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_dvcpro50ntsc)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPro50NTSC: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPro50NTSC: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPro50PAL](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcpro50pal)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPro50PAL: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPro50PAL: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD1080i50](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_dvcprohd1080i50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD1080i50: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD1080i50: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD1080i60](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcprohd1080i60)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD1080i60: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD1080i60: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD1080p25](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_dvcprohd1080p25)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD1080p25: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD1080p25: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD1080p30](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcprohd1080p30)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD1080p30: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD1080p30: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD720p50](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcprohd720p50)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD720p50: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD720p50: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCPROHD720p60](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcprohd720p60)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCPROHD720p60: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCPROHD720p60: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_DVCProPAL](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_dvcpropal)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_DVCProPAL: Int { get } ``` |
| To | ``` var kCMVideoCodecType_DVCProPAL: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_H263](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_h263)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_H263: Int { get } ``` |
| To | ``` var kCMVideoCodecType_H263: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_H264](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_h264)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_H264: Int { get } ``` |
| To | ``` var kCMVideoCodecType_H264: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_JPEG](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_jpeg)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_JPEG: Int { get } ``` |
| To | ``` var kCMVideoCodecType_JPEG: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_JPEG_OpenDML](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_jpeg_opendml)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_JPEG_OpenDML: Int { get } ``` |
| To | ``` var kCMVideoCodecType_JPEG_OpenDML: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_MPEG1Video](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_mpeg1video)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_MPEG1Video: Int { get } ``` |
| To | ``` var kCMVideoCodecType_MPEG1Video: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_MPEG2Video](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_mpeg2video)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_MPEG2Video: Int { get } ``` |
| To | ``` var kCMVideoCodecType_MPEG2Video: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_MPEG4Video](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_mpeg4video)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_MPEG4Video: Int { get } ``` |
| To | ``` var kCMVideoCodecType_MPEG4Video: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_SorensonVideo](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_sorensonvideo)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_SorensonVideo: Int { get } ``` |
| To | ``` var kCMVideoCodecType_SorensonVideo: CMVideoCodecType { get } ``` |

Modified [kCMVideoCodecType_SorensonVideo3](https://developer.apple.com/documentation/coremedia/kcmvideocodectype_sorensonvideo3)

|  | Declaration |
| --- | --- |
| From | ``` var kCMVideoCodecType_SorensonVideo3: Int { get } ``` |
| To | ``` var kCMVideoCodecType_SorensonVideo3: CMVideoCodecType { get } ``` |

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
