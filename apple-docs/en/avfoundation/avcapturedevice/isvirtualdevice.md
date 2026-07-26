---
title: isVirtualDevice
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isvirtualdevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isvirtualdevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isvirtualdevice.json'
content_hash: 'sha256:076c4d89275e484d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isVirtualDevice

<sub>Instance Property</sub>

A Boolean value that indicates whether the device consists of two or more physical devices.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVirtualDevice: Bool { get }
```

## Discussion

Examples of virtual devices are:

- The dual camera, which supports seamless switching between wide-angle and telephoto cameras while zooming and generating depth data from the disparities between the points of view of the physical cameras.
- The TrueDepth camera, which generates depth data from disparities between YUV and infrared cameras pointed in the same direction.

## See Also

### Inspecting device characteristics

- [constituentDevices](constituentdevices.md) — An array of physical devices that make up a virtual device.
- [- hasMediaType:](<hasmediatype(__).md>) — Returns a Boolean value that indicates whether the device captures media of a particular type.
- [transportType](transporttype.md) — The transport type of the device.
- [- supportsAVCaptureSessionPreset:](<supportssessionpreset(__).md>) — Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.
