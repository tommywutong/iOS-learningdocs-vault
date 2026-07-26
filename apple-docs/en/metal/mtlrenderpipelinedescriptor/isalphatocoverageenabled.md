---
title: isAlphaToCoverageEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/isalphatocoverageenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/isalphatocoverageenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/isalphatocoverageenabled.json'
content_hash: 'sha256:487c3f35f0f38a2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# isAlphaToCoverageEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isAlphaToCoverageEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

## See Also

### Specifying rasterization and visibility state

- [alphaToOneEnabled](isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [rasterizationEnabled](israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [inputPrimitiveTopology](inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [rasterSampleCount](rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
