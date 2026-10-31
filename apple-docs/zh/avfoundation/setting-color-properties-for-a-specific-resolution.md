---
title: 为特定分辨率设置颜色属性
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/setting-color-properties-for-a-specific-resolution
source_url: 'https://developer.apple.com/documentation/avfoundation/setting-color-properties-for-a-specific-resolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/setting-color-properties-for-a-specific-resolution.json'
content_hash: 'sha256:a73e102561ff95b8'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [视频设置](video-settings.md)

# 为特定分辨率设置颜色属性

<sub>文章</sub>

为所需的色彩范围选择合适的颜色属性键。

## 概述

指定 [AVVideoColorPropertiesKey](avvideocolorpropertieskey.md) 之后，你必须指定颜色基色、传递函数和 Y’CbCr 矩阵。

对于 HD 色度，请指定：

- [AVVideoColorPrimaries_ITU_R_709_2](avvideocolorprimaries_itu_r_709_2.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md)

对于 SD 色度，请指定：

- [AVVideoColorPrimaries_SMPTE_C](avvideocolorprimaries_smpte_c.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_601_4](avvideoycbcrmatrix_itu_r_601_4.md)

对于广色域 HD 色度，请指定：

- [AVVideoColorPrimaries_P3_D65](avvideocolorprimaries_p3_d65.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md)

如果来源与目的地的颜色属性不同，AVFoundation 会进行颜色匹配。你必须为来源做标记。

## 另请参阅

### 颜色属性

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
