---
title: videoPreviewLayer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/videopreviewlayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videopreviewlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videopreviewlayer.json'
content_hash: 'sha256:7aa129a8332ea6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoPreviewLayer

<sub>Instance Property</sub>

The video preview layer associated with the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoPreviewLayer: AVCaptureVideoPreviewLayer? { get }
```

## Discussion

The connection sets the property in its [- initWithInputPort:videoPreviewLayer:](<init(inputport_videopreviewlayer_).md>) initializer.

## See Also

### Inspecting a connection

- [inputPorts](inputports.md) — An array of the connection’s input ports.
- [output](output.md) — The connection’s output port, if applicable.
- [audioChannels](audiochannels.md) — An array of audio channels that the connection provides.
