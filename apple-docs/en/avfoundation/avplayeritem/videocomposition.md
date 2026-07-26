---
title: videoComposition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/videocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/videocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/videocomposition.json'
content_hash: 'sha256:81395343867ad6da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# videoComposition

<sub>Instance Property</sub>

The video composition settings to be applied during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying nonisolated var videoComposition: AVVideoComposition? { get set }
```

## Discussion

A video composition can only be used with file-based media and is not supported for use with media served using HTTP Live Streaming.

## See Also

### Configuring video compositing

- [customVideoCompositor](customvideocompositor.md) — The custom video compositor.
- [seekingWaitsForVideoCompositionRendering](seekingwaitsforvideocompositionrendering.md) — A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.
