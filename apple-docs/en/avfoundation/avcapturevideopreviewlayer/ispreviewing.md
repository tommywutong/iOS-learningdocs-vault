---
title: isPreviewing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/ispreviewing
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/ispreviewing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/ispreviewing.json'
content_hash: 'sha256:77cfafd6a15bc106'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# isPreviewing

<sub>Instance Property</sub>

A Boolean value that indicates whether the layer is rendering video frames from its source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isPreviewing: Bool { get }
```

## Discussion

A preview layer begins displaying content when you call the capture session’s [- startRunning](<../avcapturesession/startrunning().md>) method. If you associate the layer with an instance of [AVCaptureMultiCamSession](../avcapturemulticamsession.md), the system guarantees that all video preview layers display content by the time the blocking call to [- startRunning](<../avcapturesession/startrunning().md>) or [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) returns.

While a session is running, you may enable or disable a video preview layer’s connection to start or stop the flow of video to the layer. You may key-value observe the connection’s [enabled](../avcaptureconnection/isenabled.md) property to observe this property changing, and synchronize any user interface changes to take place precisely when the video resumes rendering to the video preview layer.

## See Also

### Layer configuration

- [videoGravity](videogravity.md) — A value that indicates how the layer displays video content within its bounds.
