---
title: connections
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/connections
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/connections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/connections.json'
content_hash: 'sha256:e3c78937e990185a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# connections

<sub>Instance Property</sub>

The connections between inputs and outputs that a capture session contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var connections: [AVCaptureConnection] { get }
```

## Discussion

A capture session automatically forms connections between inputs and outputs when you call the [- addInput:](<addinput(__).md>) or [- addOutput:](<addoutput(__).md>) methods. You can explicitly add connections to a session by calling the [- addConnection:](<addconnection(__).md>) method.

## See Also

### Connecting inputs and outputs

- [- addConnection:](<addconnection(__).md>) — Adds a connection to the capture session.
- [- canAddConnection:](<canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addInputWithNoConnections:](<addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- addOutputWithNoConnections:](<addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [- removeConnection:](<removeconnection(__).md>) — Removes a capture connection from the session.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
