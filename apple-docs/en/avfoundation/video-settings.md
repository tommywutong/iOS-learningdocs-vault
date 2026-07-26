---
title: Video settings
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/video-settings
source_url: 'https://developer.apple.com/documentation/avfoundation/video-settings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/video-settings.json'
content_hash: 'sha256:7975f99e6b370342'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Video settings

<sub>API Collection</sub>

Configure video processing settings using standard key and value constants.

## Topics

### Clean aperture

- [AVVideoCleanApertureKey](avvideocleanaperturekey.md) — A key that defines the region within the video dimension displayed during playback.
- [AVVideoCleanApertureWidthKey](avvideocleanaperturewidthkey.md) — A key to access the width of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureHeightKey](avvideocleanapertureheightkey.md) — A key to access the height of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureVerticalOffsetKey](avvideocleanapertureverticaloffsetkey.md) — A key to access the vertical offset of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureHorizontalOffsetKey](avvideocleanaperturehorizontaloffsetkey.md) — A key to access the horizontal offset of video that’s free from transition artifacts caused by signal encoding.

### Video codecs

- [AVVideoCodecKey](avvideocodeckey.md) — A key to access the name of the codec for compressing video.
- [AVVideoCodecType](avvideocodectype.md) — A set of constants that describe the codecs the system supports for video capture.

### Color properties

- [Setting color properties for a specific resolution](setting-color-properties-for-a-specific-resolution.md) — Choose the proper color property keys for the desired color range.
- [AVVideoAllowWideColorKey](avvideoallowwidecolorkey.md) — The key for a dictionary that indicates whether the client can process wide color.
- [AVVideoColorPrimariesKey](avvideocolorprimarieskey.md) — The key to identify color primaries in a color properties dictionary.
- [AVVideoColorPrimaries_EBU_3213](avvideocolorprimaries_ebu_3213.md) — The color primary is in the EBU Tech. 3213 color space.
- [AVVideoColorPrimaries_ITU_R_2020](avvideocolorprimaries_itu_r_2020.md) — The color primary is in the ITU_R BT.2020 color space for ultra high definition television.
- [AVVideoColorPrimaries_ITU_R_709_2](avvideocolorprimaries_itu_r_709_2.md) — The color primary is in the ITU_R BT.709 color space.
- [AVVideoColorPrimaries_P3_D65](avvideocolorprimaries_p3_d65.md) — The color primary uses the DCI-P3 D65 color space.
- [AVVideoColorPrimaries_SMPTE_C](avvideocolorprimaries_smpte_c.md) — The color primary uses the SMPTE C color space.
- [AVVideoColorPropertiesKey](avvideocolorpropertieskey.md) — The key for a dictionary that contains properties specifying video color.
- [AVVideoLogTransferFunctionKey](avvideologtransferfunctionkey.md) _(beta)_
- [AVVideoLogTransferFunction_AppleLog](avvideologtransferfunction_applelog.md) _(beta)_
- [AVVideoLogTransferFunction_AppleLog2](avvideologtransferfunction_applelog2.md) _(beta)_
- [AVVideoTransferFunctionKey](avvideotransferfunctionkey.md) — The key to identify the transfer function in a color properties dictionary.
- [AVVideoTransferFunction_IEC_sRGB](avvideotransferfunction_iec_srgb.md) — The transfer function for the IEC sRGB color space.
- [AVVideoTransferFunction_ITU_R_2100_HLG](avvideotransferfunction_itu_r_2100_hlg.md) — The transfer function for the ITU_R BT.2100 color space.
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md) — The transfer function for the ITU_R BT.709 color space.
- [AVVideoTransferFunction_Linear](avvideotransferfunction_linear.md) — The transfer function for the linear color space.
- [AVVideoTransferFunction_SMPTE_240M_1995](avvideotransferfunction_smpte_240m_1995.md) — The transfer function for the SMPTE 240M color space.
- [AVVideoTransferFunction_SMPTE_ST_2084_PQ](avvideotransferfunction_smpte_st_2084_pq.md) — The transfer function for the SMPTE 2084 color space.
- [AVVideoYCbCrMatrixKey](avvideoycbcrmatrixkey.md) — The key to identify the Y’CbCr matrix in a color properties dictionary.
- [AVVideoYCbCrMatrix_ITU_R_2020](avvideoycbcrmatrix_itu_r_2020.md) — The Y’CbCr color matrix for ITU-R BT.2020 conversion.
- [AVVideoYCbCrMatrix_ITU_R_601_4](avvideoycbcrmatrix_itu_r_601_4.md) — The Y’CbCr color matrix for ITU-R BT.601 conversion.
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md) — The Y’CbCr color matrix for ITU-R BT.709 conversion.
- [AVVideoYCbCrMatrix_SMPTE_240M_1995](avvideoycbcrmatrix_smpte_240m_1995.md) — The Y’CbCr color matrix for SMPTE 240M conversion.

### Compression

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — A key to access the dictionary of compression properties for a video asset.
- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — The key that indicates the video decompression properties to pass to the video decoder.
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — A key to access the average bit rate—as bits per second—used in compressing video.
- [AVVideoQualityKey](avvideoqualitykey.md) — A key to set the JPEG compression quality of the video.
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — A key to access the maximum interval between keyframes.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.

### Entropy mode

- [AVVideoH264EntropyModeKey](avvideoh264entropymodekey.md) — The entropy encoding mode for H.264 compression.
- [AVVideoH264EntropyModeCABAC](avvideoh264entropymodecabac.md) — The encoder uses Context-based Adaptive Binary Arithmetic Coding.
- [AVVideoH264EntropyModeCAVLC](avvideoh264entropymodecavlc.md) — The encoder uses Context-based Adaptive Variable Length Coding.

### FairPlay

- [AVStreamingKeyDeliveryContentKeyType](avstreamingkeydeliverycontentkeytype.md) — A URL for a content key.
- [AVStreamingKeyDeliveryPersistentContentKeyType](avstreamingkeydeliverypersistentcontentkeytype.md) — A URL for a persistent content key.

### Frame rate

- [AVVideoExpectedSourceFrameRateKey](avvideoexpectedsourceframeratekey.md) — The expected source frame rate.
- [AVVideoAverageNonDroppableFrameRateKey](avvideoaveragenondroppableframeratekey.md) — The desired average number of non-droppable frames to be encoded for each second of video.

### Geometry

- [AVVideoWidthKey](avvideowidthkey.md) — A key to access the width of the video in pixels.
- [AVVideoHeightKey](avvideoheightkey.md) — A key to access the height of the video in pixels.
- [AVVideoPixelAspectRatioKey](avvideopixelaspectratiokey.md) — A key to access the video’s pixel aspect ratio.
- [AVVideoPixelAspectRatioVerticalSpacingKey](avvideopixelaspectratioverticalspacingkey.md) — A key to access the pixel aspect ratio vertical spacing.
- [AVVideoPixelAspectRatioHorizontalSpacingKey](avvideopixelaspectratiohorizontalspacingkey.md) — A key to access the pixel aspect ratio horizontal spacing.

### Profile level

- [AVVideoProfileLevelKey](avvideoprofilelevelkey.md) — A key to access the video profile.
- [AVVideoProfileLevelH264High40](avvideoprofilelevelh264high40.md) — A high-level 4.0 profile.
- [AVVideoProfileLevelH264High41](avvideoprofilelevelh264high41.md) — A high-level 4.1 profile.
- [AVVideoProfileLevelH264Main30](avvideoprofilelevelh264main30.md) — A main-level 3.0 profile.
- [AVVideoProfileLevelH264Main31](avvideoprofilelevelh264main31.md) — A main-level 3.1 profile.
- [AVVideoProfileLevelH264Main32](avvideoprofilelevelh264main32.md) — A main-level 3.2 profile.
- [AVVideoProfileLevelH264Main41](avvideoprofilelevelh264main41.md) — A main-level 4.1 profile.
- [AVVideoProfileLevelH264Baseline30](avvideoprofilelevelh264baseline30.md) — A baseline-level 3.0 profile.
- [AVVideoProfileLevelH264Baseline31](avvideoprofilelevelh264baseline31.md) — A baseline-level 3.1 profile.
- [AVVideoProfileLevelH264Baseline41](avvideoprofilelevelh264baseline41.md) — A baseline-level 4.1 profile.
- [AVVideoProfileLevelH264HighAutoLevel](avvideoprofilelevelh264highautolevel.md) — A high profile auto level profile.
- [AVVideoProfileLevelH264MainAutoLevel](avvideoprofilelevelh264mainautolevel.md) — A main profile auto level profile.
- [AVVideoProfileLevelH264BaselineAutoLevel](avvideoprofilelevelh264baselineautolevel.md) — A baseline auto level profile.

### Scaling mode

- [AVVideoScalingModeFit](avvideoscalingmodefit.md) — The string identifier for scaling a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeKey](avvideoscalingmodekey.md) — A key to retrieve the video scaling mode from a dictionary.
- [AVVideoScalingModeResize](avvideoscalingmoderesize.md) — The string identifier for resizing a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeResizeAspect](avvideoscalingmoderesizeaspect.md) — The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.
- [AVVideoScalingModeResizeAspectFill](avvideoscalingmoderesizeaspectfill.md) — The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.

### VideoToolbox options

- [AVVideoEncoderSpecificationKey](avvideoencoderspecificationkey.md) — The video encoder specification includes options for choosing a specific video encoder.

## See Also

### Common

- [Media assets](media-assets.md) — Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- [Media reading and writing](media-reading-and-writing.md) — Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](media-types-and-utilities.md) — Identify the types of content and file formats that AVFoundation supports.
- [Audio settings](audio-settings.md) — Configure audio processing settings using standard key and value constants.
