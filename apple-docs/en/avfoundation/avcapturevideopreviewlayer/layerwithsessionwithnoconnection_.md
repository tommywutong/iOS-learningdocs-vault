---
title: 'layerWithSessionWithNoConnection:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsessionwithnoconnection:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsessionwithnoconnection:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsessionwithnoconnection%3A.json'
content_hash: 'sha256:60a6a0db9f18a7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# layerWithSessionWithNoConnection:

<sub>Type Method</sub>

Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) layerWithSessionWithNoConnection:(AVCaptureSession *) session;
```

## Parameters

- `session` — A capture session to preview.

## Return Value

A preview layer with no connections to a session’s eligible video inputs

## Discussion

Only use this initializer if you intend to manually connect the layer to a particular [Port](../avcaptureinput/port.md) by calling the session’s [- addConnection:](<../avcapturesession/addconnection(__).md>) method.

## See Also

### Creating a preview layer

- [layerWithSession:](layerwithsession_.md) — Returns a new layer to preview the visual output of a capture session.
- [- initWithSession:](<init(session_).md>) — Creates a layer to preview the visual output of a capture session.
- [- initWithSessionWithNoConnection:](<init(sessionwithnoconnection_).md>) — Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.
