---
title: AVCaptureViewDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureviewdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureviewdelegate.json'
content_hash: 'sha256:2e6bad2a3b919309'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureViewDelegate

<sub>Protocol</sub>

The protocol that defines the methods you can implement to respond to capture view events.

<sub>macOS</sub>

```swift
protocol AVCaptureViewDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Starting a New Recording

- [- captureView:startRecordingToFileOutput:](<avcaptureviewdelegate/captureview(__startrecordingto_).md>) — Tells the delegate that the user has made a request to start a new recording.

## See Also

### Configuring the Delegate

- [delegate](avcaptureview/delegate.md) — The capture view’s delegate object.
