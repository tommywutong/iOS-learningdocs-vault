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
doc_path: /documentation/avfoundation/avassetexportsession/customvideocompositor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/customvideocompositor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/customvideocompositor.json'
content_hash: 'sha256:31e641fd39176b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# customVideoCompositor

<sub>Instance Property</sub>

An optional custom object to use when compositing video frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

## See Also

### Configuring video output

- [videoComposition](videocomposition.md) — An optional object that provides instructions for how to composite frames of video.
