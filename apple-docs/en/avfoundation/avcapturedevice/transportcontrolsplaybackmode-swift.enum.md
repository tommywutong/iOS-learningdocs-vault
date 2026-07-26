---
title: AVCaptureDevice.TransportControlsPlaybackMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/transportcontrolsplaybackmode-swift.enum.json'
content_hash: 'sha256:3461fd56fd456c60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.TransportControlsPlaybackMode

<sub>Enumeration</sub>

Constants that indicate the transport control’s current mode of playback, if it has one.

<sub>macOS</sub>

```swift
enum TransportControlsPlaybackMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Playback modes

- [AVCaptureDeviceTransportControlsNotPlayingMode](transportcontrolsplaybackmode-swift.enum/notplaying.md) — A value that indicates that the tape transport isn’t threaded through the play head.
- [AVCaptureDeviceTransportControlsPlayingMode](transportcontrolsplaybackmode-swift.enum/playing.md) — A value that indicates that the tape transport is threaded through the play head.

### Initializers

- [init(rawValue:)](<transportcontrolsplaybackmode-swift.enum/init(rawvalue_).md>)

## See Also

### Controlling transport behavior

- [transportControlsSupported](transportcontrolssupported.md) — A Boolean value that indicates whether the device supports transport control commands.
- [transportControlsPlaybackMode](transportcontrolsplaybackmode-swift.property.md) — The current playback mode.
- [- setTransportControlsPlaybackMode:speed:](<settransportcontrolsplaybackmode(__speed_).md>) — Sets the transport control’s playback mode and speed.
- [transportControlsSpeed](transportcontrolsspeed-swift.property.md) — The current playback speed.
- [TransportControlsSpeed](transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.
