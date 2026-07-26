---
title: videoComposition
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadervideocompositionoutput/videocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/videocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadervideocompositionoutput/videocomposition.json'
content_hash: 'sha256:a4f73c544e2d0718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderVideoCompositionOutput](../avassetreadervideocompositionoutput.md)

# videoComposition

<sub>Instance Property</sub>

The video composition to use for the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var videoComposition: AVVideoComposition? { get set }
```

## Discussion

The value is an [AVVideoComposition](../avvideocomposition.md) object that specifies the visual arrangement of video frames read from each source track over the timeline of the source asset.

## See Also

### Configuring video settings

- [customVideoCompositor](customvideocompositor.md) — A custom video compositor for the output.
