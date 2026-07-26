---
title: transportControlsSpeed
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/transportcontrolsspeed-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsspeed-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/transportcontrolsspeed-swift.property.json'
content_hash: 'sha256:a4b156389d6dd0f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# transportControlsSpeed

<sub>Instance Property</sub>

The current playback speed.

<sub>macOS</sub>

```swift
var transportControlsSpeed: AVCaptureDevice.TransportControlsSpeed { get }
```

## Discussion

For devices that support transport control, the value of this property indicates the current playback speed of the deck. The following table gives examples of the meaning of values:

| Value | Meaning |
|---|---|
| 0.0 | Stopped |
| 1.0 | Forward at normal speed. |
| -1.0 | Reverse at normal speed. |
| 2.0 | Forward at 2x normal speed. |

This property is key-value observable.

## See Also

### Controlling transport behavior

- [transportControlsSupported](transportcontrolssupported.md) — A Boolean value that indicates whether the device supports transport control commands.
- [transportControlsPlaybackMode](transportcontrolsplaybackmode-swift.property.md) — The current playback mode.
- [- setTransportControlsPlaybackMode:speed:](<settransportcontrolsplaybackmode(__speed_).md>) — Sets the transport control’s playback mode and speed.
- [TransportControlsPlaybackMode](transportcontrolsplaybackmode-swift.enum.md) — Constants that indicate the transport control’s current mode of playback, if it has one.
- [TransportControlsSpeed](transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.
