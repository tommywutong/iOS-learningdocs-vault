---
title: customVideoCompositor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/customvideocompositor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/customvideocompositor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/customvideocompositor.json'
content_hash: 'sha256:9993abea181ccc7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# customVideoCompositor

<sub>Instance Property</sub>

A custom video compositor to use when extracting images from assets with multiple video tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

## See Also

### Configuring compositing

- [videoComposition](videocomposition.md) — A video composition to use when extracting images from assets with multiple video tracks.
