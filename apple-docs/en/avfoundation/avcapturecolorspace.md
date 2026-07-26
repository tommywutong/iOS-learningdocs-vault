---
title: AVCaptureColorSpace
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturecolorspace
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturecolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturecolorspace.json'
content_hash: 'sha256:609ec6ce6c2a0618'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureColorSpace

<sub>Enumeration</sub>

An enumeration of color spaces a device can support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum AVCaptureColorSpace
```

## Overview

By default, a capture session automatically enables wide-gamut capture for supported devices and capture workflows.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Color spaces

- [AVCaptureColorSpace_sRGB](avcapturecolorspace/srgb.md) — The standard RGB color space.
- [AVCaptureColorSpace_P3_D65](avcapturecolorspace/p3_d65.md) — The P3 D65 wide color space that uses Illuminant D65 as the white point.
- [AVCaptureColorSpace_HLG_BT2020](avcapturecolorspace/hlg_bt2020.md) — The BT.2020 wide color space that uses Illuminant D65 as the white point and Hybrid Log-Gamma (HLG) as the transfer function.
- [AVCaptureColorSpace_AppleLog](avcapturecolorspace/applelog.md) — The Apple Log Color space, which uses BT2020 as the color primaries, and an Apple-defined Log curve as a transfer function.
- [AVCaptureColorSpace_AppleLog2](avcapturecolorspace/applelog2.md) — The Apple Log 2 Color space, which uses Apple Gamut as the color primaries, and an Apple defined Log curve as a transfer function. When you set this as the active color space on an [AVCaptureDevice](avcapturedevice.md), any [AVCapturePhotoOutput](avcapturephotooutput.md) or [AVCaptureStillImageOutput](avcapturestillimageoutput.md) connected to the same [AVCaptureDevice](avcapturedevice.md) is made inactive (its [active](avcaptureconnection/isactive.md) property returns `false`).

### Initializers

- [init(rawValue:)](<avcapturecolorspace/init(rawvalue_).md>)

## See Also

### Configuring color space settings

- [activeColorSpace](avcapturedevice/activecolorspace.md) — The currently active color space for capture.
