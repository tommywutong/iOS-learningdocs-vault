---
title: connection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/connection
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/connection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/connection.json'
content_hash: 'sha256:875b9b848c87e3b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# connection

<sub>Instance Property</sub>

An object that describes the connection from the layer to a particular input port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var connection: AVCaptureConnection? { get }
```

## Discussion

When you associate a preview layer with a capture session, the session automatically creates a connection to the first eligible video [Port](../avcaptureinput/port.md) object. If you detach a preview layer from a session, the connection property becomes `nil`.

## See Also

### Session configuration

- [session](session.md) — A capture session with visual output to preview.
- [- setSessionWithNoConnection:](<setsessionwithnoconnection(__).md>) — Associates a session with the layer without automatically forming a connection to an eligible input port.
