---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreMedia.html
archived_at: '2026-07-18T02:56:32.295951Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreMedia Changes for Objective-C

### CoreMedia

#### CMBase.h

Added #def CM_ASSUME_NONNULL_BEGINAdded #def CM_ASSUME_NONNULL_ENDAdded #def CM_BRIDGED_TYPEAdded #def CM_NONNULLAdded #def CM_NULLABLEAdded #def CM_RETURNS_NOT_RETAINED_PARAMETERAdded #def CM_RETURNS_RETAINEDAdded #def CM_RETURNS_RETAINED_PARAMETERAdded #def COREMEDIA_DECLARE_BRIDGED_TYPESAdded #def COREMEDIA_DECLARE_NULLABILITYAdded #def COREMEDIA_DECLARE_NULLABILITY_BEGIN_ENDAdded #def COREMEDIA_DECLARE_RETURNS_NOT_RETAINED_ON_PARAMETERSAdded #def COREMEDIA_DECLARE_RETURNS_RETAINEDAdded #def COREMEDIA_DECLARE_RETURNS_RETAINED_ON_PARAMETERSAdded #def COREMEDIA_USE_DERIVED_ENUMS_FOR_CONSTANTS

#### CMFormatDescription.h

Added [kCMFormatDescriptionChromaLocation_Bottom](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottom)Added [kCMFormatDescriptionChromaLocation_BottomLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_bottomleft)Added [kCMFormatDescriptionChromaLocation_Center](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_center)Added [kCMFormatDescriptionChromaLocation_DV420](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_dv420)Added [kCMFormatDescriptionChromaLocation_Left](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_left)Added [kCMFormatDescriptionChromaLocation_Top](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_top)Added [kCMFormatDescriptionChromaLocation_TopLeft](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionchromalocation_topleft)Added [kCMFormatDescriptionColorPrimaries_DCI_P3](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_dci_p3)Added [kCMFormatDescriptionColorPrimaries_EBU_3213](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_ebu_3213)Added [kCMFormatDescriptionColorPrimaries_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_2020)Added [kCMFormatDescriptionColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_itu_r_709_2)Added [kCMFormatDescriptionColorPrimaries_P3_D65](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p3_d65)Added [kCMFormatDescriptionColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_smpte_c)Added [kCMFormatDescriptionExtension_ChromaLocationBottomField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationbottomfield)Added [kCMFormatDescriptionExtension_ChromaLocationTopField](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_chromalocationtopfield)Added [kCMFormatDescriptionExtension_CleanAperture](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_cleanaperture)Added [kCMFormatDescriptionExtension_ColorPrimaries](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_colorprimaries)Added [kCMFormatDescriptionExtension_FieldCount](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fieldcount)Added [kCMFormatDescriptionExtension_FieldDetail](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_fielddetail)Added [kCMFormatDescriptionExtension_GammaLevel](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_gammalevel)Added [kCMFormatDescriptionExtension_PixelAspectRatio](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_pixelaspectratio)Added [kCMFormatDescriptionExtension_TransferFunction](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_transferfunction)Added [kCMFormatDescriptionExtension_VerbatimImageDescription](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_verbatimimagedescription)Added [kCMFormatDescriptionExtension_YCbCrMatrix](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionextension_ycbcrmatrix)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineEarly](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlineearly)Added [kCMFormatDescriptionFieldDetail_SpatialFirstLineLate](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_spatialfirstlinelate)Added [kCMFormatDescriptionFieldDetail_TemporalBottomFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporalbottomfirst)Added [kCMFormatDescriptionFieldDetail_TemporalTopFirst](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionfielddetail_temporaltopfirst)Added [kCMFormatDescriptionKey_CleanApertureHeight](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureheight)Added [kCMFormatDescriptionKey_CleanApertureHorizontalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturehorizontaloffset)Added [kCMFormatDescriptionKey_CleanApertureVerticalOffset](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanapertureverticaloffset)Added [kCMFormatDescriptionKey_CleanApertureWidth](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_cleanaperturewidth)Added [kCMFormatDescriptionKey_PixelAspectRatioHorizontalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratiohorizontalspacing)Added [kCMFormatDescriptionKey_PixelAspectRatioVerticalSpacing](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionkey_pixelaspectratioverticalspacing)Added [kCMFormatDescriptionTransferFunction_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_2020)Added [kCMFormatDescriptionTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_itu_r_709_2)Added [kCMFormatDescriptionTransferFunction_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_smpte_240m_1995)Added [kCMFormatDescriptionTransferFunction_UseGamma](https://developer.apple.com/documentation/coremedia/kcmformatdescriptiontransferfunction_usegamma)Added kCMFormatDescriptionYCbCrMatrix_DCI_P3Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_2020](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_2020)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_601_4)Added [kCMFormatDescriptionYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_itu_r_709_2)Added kCMFormatDescriptionYCbCrMatrix_P3_D65Added [kCMFormatDescriptionYCbCrMatrix_SMPTE_240M_1995](https://developer.apple.com/documentation/coremedia/kcmformatdescriptionycbcrmatrix_smpte_240m_1995)Added [kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescription_structuraldependencykey_dependencyisinvalidflag)Added [kCMMetadataFormatDescriptionKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionkey_structuraldependency)Added [kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency](https://developer.apple.com/documentation/coremedia/kcmmetadataformatdescriptionmetadataspecificationkey_structuraldependency)Added [kCMVideoCodecType_HEVC](https://developer.apple.com/documentation/coremedia/1564239-video_codec_constants/kcmvideocodectype_hevc)

#### CMMetadata.h

Added [kCMMetadataBaseDataType_JSON](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_json)Added [kCMMetadataBaseDataType_PolygonF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polygonf32)Added [kCMMetadataBaseDataType_PolylineF32](https://developer.apple.com/documentation/coremedia/kcmmetadatabasedatatype_polylinef32)Added [kCMMetadataIdentifier_QuickTimeMetadataVideoOrientation](https://developer.apple.com/documentation/coremedia/kcmmetadataidentifier_quicktimemetadatavideoorientation)

#### CMSampleBuffer.h

Added [kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_stillimagelensstabilizationinfo)Added [kCMSampleBufferLensStabilizationInfo_Active](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_active)Added [kCMSampleBufferLensStabilizationInfo_Off](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_off)Added [kCMSampleBufferLensStabilizationInfo_OutOfRange](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_outofrange)Added [kCMSampleBufferLensStabilizationInfo_Unavailable](https://developer.apple.com/documentation/coremedia/kcmsamplebufferlensstabilizationinfo_unavailable)

#### CMSync.h

Added [CMTimebaseCopyMaster()](https://developer.apple.com/documentation/coremedia/1489679-cmtimebasecopymaster)Added [CMTimebaseCopyMasterClock()](https://developer.apple.com/documentation/coremedia/1489238-cmtimebasecopymasterclock)Added [CMTimebaseCopyMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489341-cmtimebasecopymastertimebase)Added [CMTimebaseCopyUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489262-cmtimebasecopyultimatemastercloc)Modified [CMTimebaseGetMaster()](https://developer.apple.com/documentation/coremedia/1489764-cmtimebasegetmaster)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [CMTimebaseGetMasterClock()](https://developer.apple.com/documentation/coremedia/1489691-cmtimebasegetmasterclock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [CMTimebaseGetMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489484-cmtimebasegetmastertimebase)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [CMTimebaseGetUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489671-cmtimebasegetultimatemasterclock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### CMTimeRange.h

Added #def CMTIMEMAPPING_IS_EMPTYAdded #def CMTIMEMAPPING_IS_INVALIDAdded #def CMTIMEMAPPING_IS_VALIDAdded [CMTimeMappingCopyAsDictionary()](https://developer.apple.com/documentation/coremedia/1462805-cmtimemappingcopyasdictionary)Added [CMTimeMappingCopyDescription()](https://developer.apple.com/documentation/coremedia/1462811-cmtimemappingcopydescription)Added [CMTimeMappingMake()](https://developer.apple.com/documentation/coremedia/1462793-cmtimemappingmake)Added [CMTimeMappingMakeEmpty()](https://developer.apple.com/documentation/coremedia/1462828-cmtimemappingmakeempty)Added [CMTimeMappingMakeFromDictionary()](https://developer.apple.com/documentation/coremedia/1462796-cmtimemappingmakefromdictionary)Added [CMTimeMappingShow()](https://developer.apple.com/documentation/coremedia/1462835-cmtimemappingshow)Added [kCMTimeMappingInvalid](https://developer.apple.com/documentation/coremedia/cmtimemapping/1462795-invalid)Added [kCMTimeMappingSourceKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingsourcekey)Added [kCMTimeMappingTargetKey](https://developer.apple.com/documentation/coremedia/kcmtimemappingtargetkey)

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
