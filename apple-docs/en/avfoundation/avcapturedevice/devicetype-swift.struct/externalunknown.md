---
title: externalUnknown
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/externalunknown
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/externalunknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/externalunknown.json'
content_hash: 'sha256:59d3c6de535d8902'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# externalUnknown

<sub>Type Property</sub>

An unknown external device type.

> [!warning] Deprecated
> Use [AVCaptureDeviceTypeExternal](external.md) instead.

<sub>macOS</sub>

```swift
static let externalUnknown: AVCaptureDevice.DeviceType
```

## Discussion

In macOS, use this type to specify external devices, such as an iPhone camera.

> [!important] Important
> In [Mac Catalyst](../../../uikit/mac-catalyst.md) apps, use [AVCaptureDeviceTypeBuiltInWideAngleCamera](builtinwideanglecamera.md) instead.

## See Also

### External devices

- [AVCaptureDeviceTypeExternal](external.md) — An external device type.
