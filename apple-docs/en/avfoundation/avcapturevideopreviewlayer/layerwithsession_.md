---
title: 'layerWithSession:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsession:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsession:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/layerwithsession%3A.json'
content_hash: 'sha256:3ddc61c474c50424'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# layerWithSession:

<sub>Type Method</sub>

Returns a new layer to preview the visual output of a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) layerWithSession:(AVCaptureSession *) session;
```

## Parameters

- `session` — The capture session from which to source the preview.

## Return Value

A preview layer.

## See Also

### Creating a preview layer

- [- initWithSession:](<init(session_).md>) — Creates a layer to preview the visual output of a capture session.
- [layerWithSessionWithNoConnection:](layerwithsessionwithnoconnection_.md) — Returns a new layer to preview the visual output of a capture session, without making connections to eligible video inputs.
- [- initWithSessionWithNoConnection:](<init(sessionwithnoconnection_).md>) — Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.
