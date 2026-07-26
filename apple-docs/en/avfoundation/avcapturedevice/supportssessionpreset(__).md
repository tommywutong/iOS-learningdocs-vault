---
title: 'supportsSessionPreset(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/supportssessionpreset(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/supportssessionpreset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/supportssessionpreset%28_%3A%29.json'
content_hash: 'sha256:d7b9f1e042afa393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# supportsSessionPreset(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func supportsSessionPreset(_ preset: AVCaptureSession.Preset) -> Bool
```

## Parameters

- `preset` — A capture session preset.

## Return Value

[true](../../swift/true.md) if you can use the device; otherwise, [false](../../swift/false.md).

## See Also

### Inspecting device characteristics

- [virtualDevice](isvirtualdevice.md) — A Boolean value that indicates whether the device consists of two or more physical devices.
- [constituentDevices](constituentdevices.md) — An array of physical devices that make up a virtual device.
- [- hasMediaType:](<hasmediatype(__).md>) — Returns a Boolean value that indicates whether the device captures media of a particular type.
- [transportType](transporttype.md) — The transport type of the device.
