---
title: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/perframehdrdisplaymetadatapolicy-swift.struct.json'
content_hash: 'sha256:6899ede0ec40c030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# AVVideoComposition.PerFrameHDRDisplayMetadataPolicy

<sub>Structure</sub>

A type that defines the policy for handling of per frame HDR metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PerFrameHDRDisplayMetadataPolicy
```

## Discussion

Use this type to specify what HDR display metadata to attach to the rendered frame.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Policies

- [AVVideoCompositionPerFrameHDRDisplayMetadataPolicyPropagate](perframehdrdisplaymetadatapolicy-swift.struct/propagate.md) — A policy that passes HDR metadata through, if present on the composed frame.
- [AVVideoCompositionPerFrameHDRDisplayMetadataPolicyGenerate](perframehdrdisplaymetadatapolicy-swift.struct/generate.md) — A video composition may generate HDR metadata and attach it to the rendered frame.

### Initializers

- [init(rawValue:)](<perframehdrdisplaymetadatapolicy-swift.struct/init(rawvalue_).md>) — Creates a policy with a string value.

## See Also

### Configuring HDR metadata

- [perFrameHDRDisplayMetadataPolicy](../avmutablevideocomposition/perframehdrdisplaymetadatapolicy.md) — Configures the policy for display of HDR display metadata on the rendered frame.
