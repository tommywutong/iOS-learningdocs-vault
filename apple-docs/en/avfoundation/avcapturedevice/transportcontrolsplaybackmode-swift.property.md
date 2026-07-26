---
title: transportControlsPlaybackMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.property.json'
content_hash: 'sha256:14128ad5145c657f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# transportControlsPlaybackMode

<sub>Instance Property</sub>

The current playback mode.

<sub>macOS</sub>

```swift
var transportControlsPlaybackMode: AVCaptureDevice.TransportControlsPlaybackMode { get }
```

## Discussion

For devices that support transport control, query this property to discover the current playback mode.

## See Also

### Controlling transport behavior

- [transportControlsSupported](transportcontrolssupported.md) — A Boolean value that indicates whether the device supports transport control commands.
- [- setTransportControlsPlaybackMode:speed:](<settransportcontrolsplaybackmode(__speed_).md>) — Sets the transport control’s playback mode and speed.
- [TransportControlsPlaybackMode](transportcontrolsplaybackmode-swift.enum.md) — Constants that indicate the transport control’s current mode of playback, if it has one.
- [transportControlsSpeed](transportcontrolsspeed-swift.property.md) — The current playback speed.
- [TransportControlsSpeed](transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.
