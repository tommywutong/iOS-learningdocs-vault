---
title: Setting color properties for a specific resolution
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Video settings](video-settings.md)

# Setting color properties for a specific resolution

<sub>Article</sub>

Choose the proper color property keys for the desired color range.

## Overview

After specifying the [AVVideoColorPropertiesKey](avvideocolorpropertieskey.md), you must specify a color primary, transfer function, and Y’CbCr matrix.

For HD colorimetry, specify:

- [AVVideoColorPrimaries_ITU_R_709_2](avvideocolorprimaries_itu_r_709_2.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md)

For SD colorimetry, specify:

- [AVVideoColorPrimaries_SMPTE_C](avvideocolorprimaries_smpte_c.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_601_4](avvideoycbcrmatrix_itu_r_601_4.md)

For wide gamut HD colorimetry, specify:

- [AVVideoColorPrimaries_P3_D65](avvideocolorprimaries_p3_d65.md)
- [AVVideoTransferFunction_ITU_R_709_2](avvideotransferfunction_itu_r_709_2.md)
- [AVVideoYCbCrMatrix_ITU_R_709_2](avvideoycbcrmatrix_itu_r_709_2.md)

If the source and destination color properties differ, AVFoundation matches the color. You must tag the source.

## See Also

### Color properties

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
