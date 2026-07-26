---
title: 'setSessionWithNoConnection(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/setsessionwithnoconnection(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/setsessionwithnoconnection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/setsessionwithnoconnection%28_%3A%29.json'
content_hash: 'sha256:4f5e0cb822bb44b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# setSessionWithNoConnection(_:)

<sub>Instance Method</sub>

Associates a session with the layer without automatically forming a connection to an eligible input port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setSessionWithNoConnection(_ session: AVCaptureSession)
```

## Parameters

- `session` — A capture session.

## Discussion

Only use this method if you intend to manually create a connection between the layer and a particular [Port](../avcaptureinput/port.md), and add it to the session using its [- addConnection:](<../avcapturesession/addconnection(__).md>) method.

## See Also

### Session configuration

- [session](session.md) — A capture session with visual output to preview.
- [connection](connection.md) — An object that describes the connection from the layer to a particular input port.
