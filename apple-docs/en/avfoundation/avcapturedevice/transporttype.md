---
title: transportType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/transporttype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/transporttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/transporttype.json'
content_hash: 'sha256:9ae9e71f201c5d6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# transportType

<sub>Instance Property</sub>

The transport type of the device.

<sub>macOS</sub>

```swift
var transportType: Int32 { get }
```

## Discussion

The value of this property represents a capture device’s transport type, such as USB or PCI. The value is an IOKit framework transport type constant (`kIOAudioDeviceTransportType`).

## See Also

### Inspecting device characteristics

- [virtualDevice](isvirtualdevice.md) — A Boolean value that indicates whether the device consists of two or more physical devices.
- [constituentDevices](constituentdevices.md) — An array of physical devices that make up a virtual device.
- [- hasMediaType:](<hasmediatype(__).md>) — Returns a Boolean value that indicates whether the device captures media of a particular type.
- [- supportsAVCaptureSessionPreset:](<supportssessionpreset(__).md>) — Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.
