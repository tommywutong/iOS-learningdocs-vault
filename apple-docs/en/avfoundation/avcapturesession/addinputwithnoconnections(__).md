---
title: 'addInputWithNoConnections(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addinputwithnoconnections(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addinputwithnoconnections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addinputwithnoconnections%28_%3A%29.json'
content_hash: 'sha256:b217465e4b9084e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addInputWithNoConnections(_:)

<sub>Instance Method</sub>

Adds a capture input to a session without forming any connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addInputWithNoConnections(_ input: AVCaptureInput)
```

## Parameters

- `input` — The capture input to add to the session.

## Discussion

You can call this method while the session is running.

In most cases, use the [- addInput:](<addinput(__).md>) method to add new inputs to a session. Call this method if you require fine-grained control over which inputs connect to which outputs.

## See Also

### Connecting inputs and outputs

- [connections](connections.md) — The connections between inputs and outputs that a capture session contains.
- [- addConnection:](<addconnection(__).md>) — Adds a connection to the capture session.
- [- canAddConnection:](<canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addOutputWithNoConnections:](<addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [- removeConnection:](<removeconnection(__).md>) — Removes a capture connection from the session.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
