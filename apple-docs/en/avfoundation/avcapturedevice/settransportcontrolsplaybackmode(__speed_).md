---
title: 'setTransportControlsPlaybackMode(_:speed:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/settransportcontrolsplaybackmode(_:speed:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/settransportcontrolsplaybackmode(_:speed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/settransportcontrolsplaybackmode%28_%3Aspeed%3A%29.json'
content_hash: 'sha256:bfa3e90704bccc4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setTransportControlsPlaybackMode(_:speed:)

<sub>Instance Method</sub>

Sets the transport control’s playback mode and speed.

<sub>macOS</sub>

```swift
func setTransportControlsPlaybackMode(_ mode: AVCaptureDevice.TransportControlsPlaybackMode, speed: AVCaptureDevice.TransportControlsSpeed)
```

## Parameters

- `mode` — A playback mode constant that indicates whether to put the deck should into play mode.

- `speed` — The speed at which to wind or play the tape.

## Discussion

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, calling this method raises an exception. When you’re finished configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Controlling transport behavior

- [transportControlsSupported](transportcontrolssupported.md) — A Boolean value that indicates whether the device supports transport control commands.
- [transportControlsPlaybackMode](transportcontrolsplaybackmode-swift.property.md) — The current playback mode.
- [TransportControlsPlaybackMode](transportcontrolsplaybackmode-swift.enum.md) — Constants that indicate the transport control’s current mode of playback, if it has one.
- [transportControlsSpeed](transportcontrolsspeed-swift.property.md) — The current playback speed.
- [TransportControlsSpeed](transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.
