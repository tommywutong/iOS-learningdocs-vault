---
title: inputPorts
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/inputports
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/inputports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/inputports.json'
content_hash: 'sha256:1b505f1ff3854d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# inputPorts

<sub>Instance Property</sub>

An array of the connection’s input ports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputPorts: [AVCaptureInput.Port] { get }
```

## Discussion

Input ports are instances of [Port](../avcaptureinput/port.md).

## See Also

### Inspecting a connection

- [output](output.md) — The connection’s output port, if applicable.
- [videoPreviewLayer](videopreviewlayer.md) — The video preview layer associated with the connection.
- [audioChannels](audiochannels.md) — An array of audio channels that the connection provides.
