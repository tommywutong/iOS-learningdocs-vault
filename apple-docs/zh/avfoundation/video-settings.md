---
title: 视频设置
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
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 视频设置

<sub>API 集合</sub>

使用标准的键和值常量来配置视频处理设置。

## 主题

### 净孔径

- [AVVideoCleanApertureKey](avvideocleanaperturekey.md) — 一个定义播放期间所显示视频尺寸内区域的键。
- [AVVideoCleanApertureWidthKey](avvideocleanaperturewidthkey.md) — 用于访问不受信号编码过渡伪影影响的视频宽度的键。
- [AVVideoCleanApertureHeightKey](avvideocleanapertureheightkey.md) — 用于访问不受信号编码过渡伪影影响的视频高度的键。
- [AVVideoCleanApertureVerticalOffsetKey](avvideocleanapertureverticaloffsetkey.md) — 用于访问不受信号编码过渡伪影影响的视频垂直偏移的键。
- [AVVideoCleanApertureHorizontalOffsetKey](avvideocleanaperturehorizontaloffsetkey.md) — 用于访问不受信号编码过渡伪影影响的视频水平偏移的键。

### 视频编解码器

- [AVVideoCodecKey](avvideocodeckey.md) — 用于访问压缩视频所用编解码器名称的键。
- [AVVideoCodecType](avvideocodectype.md) — 一组描述系统支持的用于视频捕捉的编解码器的常量。

### 颜色属性

- [为特定分辨率设置颜色属性](setting-color-properties-for-a-specific-resolution.md) — 为所需的色彩范围选择合适的颜色属性键。
- [AVVideoAllowWideColorKey](avvideoallowwidecolorkey.md) — 一个字典的键，指示客户端能否处理广色域。
- [AVVideoColorPrimariesKey](avvideocolorprimarieskey.md) — 在颜色属性字典中标识颜色基色的键。
- [AVVideoColorPrimaries_EBU_3213](avvideocolorprimaries_ebu_3213.md) — 颜色基色位于 EBU Tech. 3213 色彩空间。
- [AVVideoColorPrimaries_ITU_R_2020](avvideocolorprimaries_itu_r_2020.md) — 颜色基色位于用于超高清电视的 ITU_R BT.2020 色彩空间。
- [AVVideoColorPrimaries_ITU_R_709_2](avvideocolorprimaries_itu_r_709_2.md) — 颜色基色位于 ITU_R BT.709 色彩空间。
- [AVVideoColorPrimaries_P3_D65](avvideocolorprimaries_p3_d65.md) — 颜色基色使用 DCI-P3 D65 色彩空间。
- [AVVideoColorPrimaries_SMPTE_C](avvideocolorprimaries_smpte_c.md) — 颜色基色使用 SMPTE C 色彩空间。
- [AVVideoColorPropertiesKey](avvideocolorpropertieskey.md) — 一个字典的键，该字典包含指定视频颜色的属性。
- [AVVideoLogTransferFunctionKey](avvideologtransferfunctionkey.md) _(beta)_
- [AVVideoLogTransferFunction_AppleLog](avvideologtransferfunction_applelog.md) _(beta)_
- [AVVideoLogTransferFunction_AppleLog2](avvideologtransferfunction_applelog2.md) _(beta)_
- [AVVideoTransferFunctionKey](avvideotransferfunctionkey.md) — 在颜色属性字典中标识传递函数的键。
- [AVVideoTransferFunction_IEC_sRGB](avvideotransferfunction_iec_srgb.md) — IEC sRGB 色彩空间的传递函数。
- [AVVideoTransferFunction_ITU_R_2100_HLG](avvideotransferfunction_itu_r_2100_hlg.md) — ITU_R BT.2100 色彩空间的传递函数。
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md) — ITU_R BT.709 色彩空间的传递函数。
- [AVVideoTransferFunction_Linear](avvideotransferfunction_linear.md) — 线性色彩空间的传递函数。
- [AVVideoTransferFunction_SMPTE_240M_1995](avvideotransferfunction_smpte_240m_1995.md) — SMPTE 240M 色彩空间的传递函数。
- [AVVideoTransferFunction_SMPTE_ST_2084_PQ](avvideotransferfunction_smpte_st_2084_pq.md) — SMPTE 2084 色彩空间的传递函数。
- [AVVideoYCbCrMatrixKey](avvideoycbcrmatrixkey.md) — 在颜色属性字典中标识 Y’CbCr 矩阵的键。
- [AVVideoYCbCrMatrix_ITU_R_2020](avvideoycbcrmatrix_itu_r_2020.md) — 用于 ITU-R BT.2020 转换的 Y’CbCr 颜色矩阵。
- [AVVideoYCbCrMatrix_ITU_R_601_4](avvideoycbcrmatrix_itu_r_601_4.md) — 用于 ITU-R BT.601 转换的 Y’CbCr 颜色矩阵。
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md) — 用于 ITU-R BT.709 转换的 Y’CbCr 颜色矩阵。
- [AVVideoYCbCrMatrix_SMPTE_240M_1995](avvideoycbcrmatrix_smpte_240m_1995.md) — 用于 SMPTE 240M 转换的 Y’CbCr 颜色矩阵。

### 压缩

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — 用于访问视频资产压缩属性字典的键。
- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — 指示要传给视频解码器的视频解压属性的键。
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — 用于访问压缩视频时所用平均比特率（以比特每秒计）的键。
- [AVVideoQualityKey](avvideoqualitykey.md) — 设置视频 JPEG 压缩质量的键。
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — 用于访问关键帧之间最大间隔的键。
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — 用于访问关键帧之间最大间隔时长的键。
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — 用于访问帧重排许可的键。
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — 用于访问 Apple ProRAW 位深度的键。

### 熵模式

- [AVVideoH264EntropyModeKey](avvideoh264entropymodekey.md) — H.264 压缩的熵编码模式。
- [AVVideoH264EntropyModeCABAC](avvideoh264entropymodecabac.md) — 编码器使用基于上下文的自适应二进制算术编码。
- [AVVideoH264EntropyModeCAVLC](avvideoh264entropymodecavlc.md) — 编码器使用基于上下文的自适应可变长度编码。

### FairPlay

- [AVStreamingKeyDeliveryContentKeyType](avstreamingkeydeliverycontentkeytype.md) — 内容密钥的 URL。
- [AVStreamingKeyDeliveryPersistentContentKeyType](avstreamingkeydeliverypersistentcontentkeytype.md) — 持久化内容密钥的 URL。

### 帧率

- [AVVideoExpectedSourceFrameRateKey](avvideoexpectedsourceframeratekey.md) — 预期的来源帧率。
- [AVVideoAverageNonDroppableFrameRateKey](avvideoaveragenondroppableframeratekey.md) — 视频每秒编码所需的不可丢弃帧的平均数量。

### 几何形状

- [AVVideoWidthKey](avvideowidthkey.md) — 用于访问视频宽度（以像素计）的键。
- [AVVideoHeightKey](avvideoheightkey.md) — 用于访问视频高度（以像素计）的键。
- [AVVideoPixelAspectRatioKey](avvideopixelaspectratiokey.md) — 用于访问视频像素宽高比的键。
- [AVVideoPixelAspectRatioVerticalSpacingKey](avvideopixelaspectratioverticalspacingkey.md) — 用于访问像素宽高比垂直间距的键。
- [AVVideoPixelAspectRatioHorizontalSpacingKey](avvideopixelaspectratiohorizontalspacingkey.md) — 用于访问像素宽高比水平间距的键。

### 档次级别

- [AVVideoProfileLevelKey](avvideoprofilelevelkey.md) — 用于访问视频档次的键。
- [AVVideoProfileLevelH264High40](avvideoprofilelevelh264high40.md) — High 4.0 档次。
- [AVVideoProfileLevelH264High41](avvideoprofilelevelh264high41.md) — High 4.1 档次。
- [AVVideoProfileLevelH264Main30](avvideoprofilelevelh264main30.md) — Main 3.0 档次。
- [AVVideoProfileLevelH264Main31](avvideoprofilelevelh264main31.md) — Main 3.1 档次。
- [AVVideoProfileLevelH264Main32](avvideoprofilelevelh264main32.md) — Main 3.2 档次。
- [AVVideoProfileLevelH264Main41](avvideoprofilelevelh264main41.md) — Main 4.1 档次。
- [AVVideoProfileLevelH264Baseline30](avvideoprofilelevelh264baseline30.md) — Baseline 3.0 档次。
- [AVVideoProfileLevelH264Baseline31](avvideoprofilelevelh264baseline31.md) — Baseline 3.1 档次。
- [AVVideoProfileLevelH264Baseline41](avvideoprofilelevelh264baseline41.md) — Baseline 4.1 档次。
- [AVVideoProfileLevelH264HighAutoLevel](avvideoprofilelevelh264highautolevel.md) — High 档次自动级别。
- [AVVideoProfileLevelH264MainAutoLevel](avvideoprofilelevelh264mainautolevel.md) — Main 档次自动级别。
- [AVVideoProfileLevelH264BaselineAutoLevel](avvideoprofilelevelh264baselineautolevel.md) — Baseline 档次自动级别。

### 缩放模式

- [AVVideoScalingModeFit](avvideoscalingmodefit.md) — 将视频缩放至适应周围视图尺寸的字符串标识符。
- [AVVideoScalingModeKey](avvideoscalingmodekey.md) — 从字典中取回视频缩放模式的键。
- [AVVideoScalingModeResize](avvideoscalingmoderesize.md) — 将视频重新调整大小以适应周围视图尺寸的字符串标识符。
- [AVVideoScalingModeResizeAspect](avvideoscalingmoderesizeaspect.md) — 在保持宽高比的同时，将视频重新调整大小以适应周围视图较短尺寸的字符串标识符。
- [AVVideoScalingModeResizeAspectFill](avvideoscalingmoderesizeaspectfill.md) — 在保持宽高比的同时，将视频重新调整大小以填满周围视图较长尺寸的字符串标识符。

### VideoToolbox 选项

- [AVVideoEncoderSpecificationKey](avvideoencoderspecificationkey.md) — 视频编码器规范，包含用于选择特定视频编码器的选项。

## 另请参阅

### 通用

- [媒体资产](media-assets.md) — 从文件和流加载媒体资产，以检查其属性、轨道和内嵌元数据。
- [媒体读取与写入](media-reading-and-writing.md) — 从视频中读取图像、导出为其他格式，以及对媒体数据执行样本级读取和写入。
- [媒体类型与实用工具](media-types-and-utilities.md) — 识别 AVFoundation 支持的内容类型和文件格式。
- [音频设置](audio-settings.md) — 使用标准的键和值常量来配置音频处理设置。
