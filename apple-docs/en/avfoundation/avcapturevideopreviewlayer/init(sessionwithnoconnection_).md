---
title: 'init(sessionWithNoConnection:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/init(sessionwithnoconnection:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/init(sessionwithnoconnection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/init%28sessionwithnoconnection%3A%29.json'
content_hash: 'sha256:626df5028e833562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# init(sessionWithNoConnection:)

<sub>Initializer</sub>

Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(sessionWithNoConnection session: AVCaptureSession)
```

## Parameters

- `session` — A capture session to preview.

## Discussion

Only use this initializer if you intend to manually connect the layer to a particular [Port](../avcaptureinput/port.md) by calling the session’s [- addConnection:](<../avcapturesession/addconnection(__).md>) method.

## See Also

### Creating a preview layer

- [- initWithSession:](<init(session_).md>) — Creates a layer to preview the visual output of a capture session.
