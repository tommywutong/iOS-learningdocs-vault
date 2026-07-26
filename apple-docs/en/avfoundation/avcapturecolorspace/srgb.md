---
title: AVCaptureColorSpace.sRGB
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturecolorspace/srgb
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturecolorspace/srgb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturecolorspace/srgb.json'
content_hash: 'sha256:74d8f16cf1f9b753'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureColorSpace](../avcapturecolorspace.md)

# AVCaptureColorSpace.sRGB

<sub>Case</sub>

The standard RGB color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case sRGB
```

## Discussion

All devices support this color space.

## See Also

### Color spaces

- [AVCaptureColorSpace_P3_D65](p3_d65.md) — The P3 D65 wide color space that uses Illuminant D65 as the white point.
- [AVCaptureColorSpace_HLG_BT2020](hlg_bt2020.md) — The BT.2020 wide color space that uses Illuminant D65 as the white point and Hybrid Log-Gamma (HLG) as the transfer function.
- [AVCaptureColorSpace_AppleLog](applelog.md) — The Apple Log Color space, which uses BT2020 as the color primaries, and an Apple-defined Log curve as a transfer function.
- [AVCaptureColorSpace_AppleLog2](applelog2.md) — The Apple Log 2 Color space, which uses Apple Gamut as the color primaries, and an Apple defined Log curve as a transfer function. When you set this as the active color space on an [AVCaptureDevice](../avcapturedevice.md), any [AVCapturePhotoOutput](../avcapturephotooutput.md) or [AVCaptureStillImageOutput](../avcapturestillimageoutput.md) connected to the same [AVCaptureDevice](../avcapturedevice.md) is made inactive (its [active](../avcaptureconnection/isactive.md) property returns `false`).
