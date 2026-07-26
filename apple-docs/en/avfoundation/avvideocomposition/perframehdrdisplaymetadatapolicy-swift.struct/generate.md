---
title: generate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/generate
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/generate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct/generate.json'
content_hash: 'sha256:c0ff9cd5bd8549a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoComposition](../../avvideocomposition.md) · [PerFrameHDRDisplayMetadataPolicy](../perframehdrdisplaymetadatapolicy-swift.struct.md)

# generate

<sub>Type Property</sub>

A video composition may generate HDR metadata and attach it to the rendered frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let generate: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy
```

## Discussion

HDR metadata generation is influenced by the color space of the rendered frame, device, and HDR metadata format platform support. Any previously attached HDR metadata of the same metadata format is overwritten.

## See Also

### Policies

- [AVVideoCompositionPerFrameHDRDisplayMetadataPolicyPropagate](propagate.md) — A policy that passes HDR metadata through, if present on the composed frame.
