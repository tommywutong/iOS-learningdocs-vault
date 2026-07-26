---
title: 'init(configuration:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositioncoreanimationtool/init(configuration:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/init%28configuration%3A%29.json'
content_hash: 'sha256:5aff9761391d97df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../avvideocompositioncoreanimationtool.md)

# init(configuration:)

<sub>Initializer</sub>

Compose the composited video frames with the Core Animation layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)
```

## See Also

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:](<init(additionallayer_astrackid_).md>) — Adds a Core Animation layer to the video composition.
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:](<init(postprocessingasvideolayer_in_).md>) — Composes the composited video frame with a Core Animation layer. _(deprecated)_
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:](<init(postprocessingasvideolayers_in_).md>) — Composes the composited video frames with the Core Animation layer.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
