---
title: MTLPrimitiveTopologyClass
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlprimitivetopologyclass
source_url: 'https://developer.apple.com/documentation/metal/mtlprimitivetopologyclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlprimitivetopologyclass.json'
content_hash: 'sha256:1362f79145607b0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPrimitiveTopologyClass

<sub>Enumeration</sub>

The primitive topologies available for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLPrimitiveTopologyClass
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Topology classes

- [MTLPrimitiveTopologyClassUnspecified](mtlprimitivetopologyclass/unspecified.md) — An unspecified primitive.
- [MTLPrimitiveTopologyClassPoint](mtlprimitivetopologyclass/point.md) — A point primitive.
- [MTLPrimitiveTopologyClassLine](mtlprimitivetopologyclass/line.md) — A line primitive.
- [MTLPrimitiveTopologyClassTriangle](mtlprimitivetopologyclass/triangle.md) — A triangle primitive.

### Initializers

- [init(rawValue:)](<mtlprimitivetopologyclass/init(rawvalue_).md>)

## See Also

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [alphaToOneEnabled](mtlrenderpipelinedescriptor/isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [rasterizationEnabled](mtlrenderpipelinedescriptor/israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [inputPrimitiveTopology](mtlrenderpipelinedescriptor/inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [rasterSampleCount](mtlrenderpipelinedescriptor/rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [sampleCount](mtlrenderpipelinedescriptor/samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
