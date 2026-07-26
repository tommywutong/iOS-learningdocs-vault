---
title: 'captionSceneChanges(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionrenderer/captionscenechanges(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captionscenechanges(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/captionscenechanges%28in%3A%29.json'
content_hash: 'sha256:3984c0d8289829ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# captionSceneChanges(in:)

<sub>Instance Method</sub>

Determine render time ranges within an enclosing time range to account for visual changes among captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func captionSceneChanges(in consideredTimeRange: CMTimeRange) -> [AVCaptionRenderer.Scene]
```

## Parameters

- `consideredTimeRange` — The time range to consider for rendering.

## Return Value

An array of render scenes for the time range, or an empty array if there are none.

## See Also

### Determining scene changes

- [Scene](scene.md) — An object that holds a time range and an associated state which indicates when the renderer draws output.
