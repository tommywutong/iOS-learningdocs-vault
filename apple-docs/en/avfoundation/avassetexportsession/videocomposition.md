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
doc_path: /documentation/avfoundation/avassetexportsession/videocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/videocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/videocomposition.json'
content_hash: 'sha256:6806977b8e70f22d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# videoComposition

<sub>Instance Property</sub>

An optional object that provides instructions for how to composite frames of video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var videoComposition: AVVideoComposition? { get set }
```

## Discussion

The default value is `nil`.

This property is key-value observable.

## See Also

### Configuring video output

- [customVideoCompositor](customvideocompositor.md) — An optional custom object to use when compositing video frames.
