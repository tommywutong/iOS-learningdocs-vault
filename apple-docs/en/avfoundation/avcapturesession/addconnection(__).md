---
title: 'addConnection(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addconnection(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addconnection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addconnection%28_%3A%29.json'
content_hash: 'sha256:2add4bc4aa2212d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addConnection(_:)

<sub>Instance Method</sub>

Adds a connection to the capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addConnection(_ connection: AVCaptureConnection)
```

## Parameters

- `connection` — The capture connection to add to the session.

## Discussion

You can only add a capture connection to a session using this method if [- canAddConnection:](<canaddconnection(__).md>) returns [true](../../swift/true.md).

When using [- addInput:](<addinput(__).md>) or [- addOutput:](<addoutput(__).md>), the session automatically forms connections between all compatible inputs and outputs. Manually adding connections is only necessary when adding an input or output with no connections.

## See Also

### Connecting inputs and outputs

- [connections](connections.md) — The connections between inputs and outputs that a capture session contains.
- [- canAddConnection:](<canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addInputWithNoConnections:](<addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- addOutputWithNoConnections:](<addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [- removeConnection:](<removeconnection(__).md>) — Removes a capture connection from the session.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
