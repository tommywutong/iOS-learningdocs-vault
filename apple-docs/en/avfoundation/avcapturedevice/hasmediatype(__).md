---
title: 'hasMediaType(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/hasmediatype(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/hasmediatype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/hasmediatype%28_%3A%29.json'
content_hash: 'sha256:27e27342b87f4c5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# hasMediaType(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the device captures media of a particular type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func hasMediaType(_ mediaType: AVMediaType) -> Bool
```

## Parameters

- `mediaType` — A media type, such as [AVMediaTypeVideo](../avmediatype/video.md), [AVMediaTypeAudio](../avmediatype/audio.md), or [AVMediaTypeMuxed](../avmediatype/muxed.md).

## Return Value

[true](../../swift/true.md) if the device captures media of the specified type; otherwise, [false](../../swift/false.md).

## See Also

### Inspecting device characteristics

- [virtualDevice](isvirtualdevice.md) — A Boolean value that indicates whether the device consists of two or more physical devices.
- [constituentDevices](constituentdevices.md) — An array of physical devices that make up a virtual device.
- [transportType](transporttype.md) — The transport type of the device.
- [- supportsAVCaptureSessionPreset:](<supportssessionpreset(__).md>) — Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.
