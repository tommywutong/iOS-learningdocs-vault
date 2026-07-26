---
title: 'removeConnection(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/removeconnection(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/removeconnection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/removeconnection%28_%3A%29.json'
content_hash: 'sha256:2930c70f222c2d63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# removeConnection(_:)

<sub>Instance Method</sub>

Removes a capture connection from the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeConnection(_ connection: AVCaptureConnection)
```

## Parameters

- `connection` — The capture connection to remove from the session.

## Discussion

You can call this method while the session is running.

## See Also

### Connecting inputs and outputs

- [connections](connections.md) — The connections between inputs and outputs that a capture session contains.
- [- addConnection:](<addconnection(__).md>) — Adds a connection to the capture session.
- [- canAddConnection:](<canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addInputWithNoConnections:](<addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- addOutputWithNoConnections:](<addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
