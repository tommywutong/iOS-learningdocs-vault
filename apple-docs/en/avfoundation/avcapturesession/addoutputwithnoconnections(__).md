---
title: 'addOutputWithNoConnections(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/addoutputwithnoconnections(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/addoutputwithnoconnections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/addoutputwithnoconnections%28_%3A%29.json'
content_hash: 'sha256:3f4dbaa4832eaba5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# addOutputWithNoConnections(_:)

<sub>Instance Method</sub>

Adds a capture output to the session without forming any connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addOutputWithNoConnections(_ output: AVCaptureOutput)
```

## Parameters

- `output` — The capture output to add to the session.

## Discussion

You can call this method while the session is running.

In most cases, use the [- addOutput:](<addoutput(__).md>) method to add new outputs to a session. Call this method if you require fine-grained control over which inputs connect to which outputs.

## See Also

### Connecting inputs and outputs

- [connections](connections.md) — The connections between inputs and outputs that a capture session contains.
- [- addConnection:](<addconnection(__).md>) — Adds a connection to the capture session.
- [- canAddConnection:](<canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addInputWithNoConnections:](<addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- removeConnection:](<removeconnection(__).md>) — Removes a capture connection from the session.
- [AVCaptureAudioChannel](../avcaptureaudiochannel.md) — An object that monitors average and peak power levels for an audio channel in a capture connection.
