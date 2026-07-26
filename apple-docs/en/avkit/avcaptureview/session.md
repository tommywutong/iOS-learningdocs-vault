---
title: session
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureview/session
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview/session'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview/session.json'
content_hash: 'sha256:4d38acc3df627b13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureView](../avcaptureview.md)

# session

<sub>Instance Property</sub>

The view’s associated capture session.

<sub>macOS</sub>

```swift
var session: AVCaptureSession? { get }
```

## Discussion

This property’s default value is a capture session configured for movie file recordings of audio and video data. Use the [- setSession:showVideoPreview:showAudioPreview:](<setsession(__showvideopreview_showaudiopreview_).md>) method to provide a custom capture session. Modifying the capture session changes its visual representation in the view.

## See Also

### Configuring the Capture Session

- [- setSession:showVideoPreview:showAudioPreview:](<setsession(__showvideopreview_showaudiopreview_).md>) — Sets the view’s capture session.
