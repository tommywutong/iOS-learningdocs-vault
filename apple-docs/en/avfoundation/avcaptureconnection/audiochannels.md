---
title: audioChannels
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/audiochannels
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/audiochannels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/audiochannels.json'
content_hash: 'sha256:b503debe50887429'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# audioChannels

<sub>Instance Property</sub>

An array of audio channels that the connection provides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var audioChannels: [AVCaptureAudioChannel] { get }
```

## Discussion

The property only applies to a video connection.

## See Also

### Inspecting a connection

- [inputPorts](inputports.md) — An array of the connection’s input ports.
- [output](output.md) — The connection’s output port, if applicable.
- [videoPreviewLayer](videopreviewlayer.md) — The video preview layer associated with the connection.
