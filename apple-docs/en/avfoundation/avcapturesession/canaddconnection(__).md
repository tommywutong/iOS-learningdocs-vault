---
title: 'canAddConnection(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/canaddconnection(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddconnection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/canaddconnection%28_%3A%29.json'
content_hash: 'sha256:579de4f54c755623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# canAddConnection(_:)

<sub>Instance Method</sub>

Determines whether a you can add a connection to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAddConnection(_ connection: AVCaptureConnection) -> Bool
```

## Parameters

- `connection` — A connect object to test.

## Return Value

[true](../../swift/true.md) if you can add the connection; otherwise, [false](../../swift/false.md).

## See Also

### Connecting inputs and outputs

- [connections](connections.md) — The connections between inputs and outputs that a capture session contains.
- [- addConnection:](<addconnection(__).md>) — Adds a connection to the capture session.
- [- addInputWithNoConnections:](<addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- addOutputWithNoConnections:](<addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [- removeConnection:](<removeconnection(__).md>) — Removes a capture connection from the session.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
