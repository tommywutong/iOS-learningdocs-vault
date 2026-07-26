---
title: perFrameHDRDisplayMetadataPolicy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.property.json'
content_hash: 'sha256:ec7ae148a72f7a2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# perFrameHDRDisplayMetadataPolicy

<sub>Instance Property</sub>

The policy for display of HDR display metadata on the rendered frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy { get }
```

## Discussion

Allows the system to identify situations where it can generate HDR metadata and attach it to the rendered video frame.

The default value is [AVVideoCompositionPerFrameHDRDisplayMetadataPolicyPropagate](perframehdrdisplaymetadatapolicy-swift.struct/propagate.md), which indicates the system propagates any HDR metadata attached to the composed frame to the rendered video frames.

## See Also

### Configuring HDR metadata

- [PerFrameHDRDisplayMetadataPolicy](perframehdrdisplaymetadatapolicy-swift.struct.md) — A type that defines the policy for handling of per frame HDR metadata.
