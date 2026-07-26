---
title: transportControlsSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/transportcontrolssupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolssupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/transportcontrolssupported.json'
content_hash: 'sha256:7fcd446acdcfd3c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# transportControlsSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports transport control commands.

<sub>macOS</sub>

```swift
var transportControlsSupported: Bool { get }
```

## Discussion

For devices with transport controls, such as AVC tape-based camcorders or pro capture devices with RS422 deck control, the value of this property is [true](../../swift/true.md). If transport controls aren’t supported, none of the associated transport control methods and properties are available to the device.

This property is key-value observable.

## See Also

### Controlling transport behavior

- [transportControlsPlaybackMode](transportcontrolsplaybackmode-swift.property.md) — The current playback mode.
- [- setTransportControlsPlaybackMode:speed:](<settransportcontrolsplaybackmode(__speed_).md>) — Sets the transport control’s playback mode and speed.
- [TransportControlsPlaybackMode](transportcontrolsplaybackmode-swift.enum.md) — Constants that indicate the transport control’s current mode of playback, if it has one.
- [transportControlsSpeed](transportcontrolsspeed-swift.property.md) — The current playback speed.
- [TransportControlsSpeed](transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.
