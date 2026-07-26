---
title: macOS capture features
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/macos-capture-features
source_url: 'https://developer.apple.com/documentation/avfoundation/macos-capture-features'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/macos-capture-features.json'
content_hash: 'sha256:e9f92d7cecb46ff1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# macOS capture features

<sub>API Collection</sub>

Control the transport behavior and input sources of capture hardware in macOS.

## Topics

### Controlling transport behavior

- [transportControlsSupported](avcapturedevice/transportcontrolssupported.md) — A Boolean value that indicates whether the device supports transport control commands.
- [transportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.property.md) — The current playback mode.
- [- setTransportControlsPlaybackMode:speed:](<avcapturedevice/settransportcontrolsplaybackmode(__speed_).md>) — Sets the transport control’s playback mode and speed.
- [TransportControlsPlaybackMode](avcapturedevice/transportcontrolsplaybackmode-swift.enum.md) — Constants that indicate the transport control’s current mode of playback, if it has one.
- [transportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.property.md) — The current playback speed.
- [TransportControlsSpeed](avcapturedevice/transportcontrolsspeed-swift.typealias.md) — A constant that specifies speed of transport controls.

### Configuring input sources

- [inputSources](avcapturedevice/inputsources.md) — An array of input sources that the device supports.
- [activeInputSource](avcapturedevice/activeinputsource.md) — The currently active input source of the device.
- [InputSource](avcapturedevice/inputsource.md) — A distinct input source on a capture device.

### Accessing linked devices

- [linkedDevices](avcapturedevice/linkeddevices.md) — An array of capture devices that are physically linked to a device.
