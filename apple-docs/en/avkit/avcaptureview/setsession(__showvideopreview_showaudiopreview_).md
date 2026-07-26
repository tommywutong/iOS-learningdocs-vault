---
title: 'setSession(_:showVideoPreview:showAudioPreview:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcaptureview/setsession(_:showvideopreview:showaudiopreview:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview/setsession(_:showvideopreview:showaudiopreview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview/setsession%28_%3Ashowvideopreview%3Ashowaudiopreview%3A%29.json'
content_hash: 'sha256:541e8e2b4e6596fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureView](../avcaptureview.md)

# setSession(_:showVideoPreview:showAudioPreview:)

<sub>Instance Method</sub>

Sets the view’s capture session.

<sub>macOS</sub>

```swift
func setSession(_ session: AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)
```

## Parameters

- `session` — The capture session.

- `showVideoPreview` — A Boolean value that indicates whether the view displays a video preview. If `true`, the system adds, removes, or modifies capture inputs for video data based on device availability and user selection.

- `showAudioPreview` — A Boolean value that indicates whether the view shows an audio preview. If `true`, the system adds, removes, or modifies capture inputs for audio data based on device availability and user selection.

## Discussion

The view must show audio preview, video preview, or both. Furthermore, the view may modify the capture session, for example, to access media data for preview or when the user select a new capture source.

The capture view automatically starts and stops the default session. If you set a custom capture session on the view, you need to manually manage the session’s life cycle events.

## See Also

### Configuring the Capture Session

- [session](session.md) — The view’s associated capture session.
