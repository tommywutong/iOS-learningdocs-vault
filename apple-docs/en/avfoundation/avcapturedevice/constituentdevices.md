---
title: constituentDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/constituentdevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/constituentdevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/constituentdevices.json'
content_hash: 'sha256:60beaad73b061543'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# constituentDevices

<sub>Instance Property</sub>

An array of physical devices that make up a virtual device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var constituentDevices: [AVCaptureDevice] { get }
```

## Discussion

The value of this property is an empty array when called on a device whose [virtualDevice](isvirtualdevice.md) property is [false](../../swift/false.md).

## See Also

### Inspecting device characteristics

- [virtualDevice](isvirtualdevice.md) — A Boolean value that indicates whether the device consists of two or more physical devices.
- [- hasMediaType:](<hasmediatype(__).md>) — Returns a Boolean value that indicates whether the device captures media of a particular type.
- [transportType](transporttype.md) — The transport type of the device.
- [- supportsAVCaptureSessionPreset:](<supportssessionpreset(__).md>) — Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.
