---
title: isRasterizationEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/israsterizationenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/israsterizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/israsterizationenabled.json'
content_hash: 'sha256:b3cad89776959b57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# isRasterizationEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether the pipeline rasterizes primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isRasterizationEnabled: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), indicating that primitives are rasterized. If the value is [false](../../swift/false.md), then primitives are dropped prior to rasterization (i.e. rasterization is disabled). Disabling rasterization may be useful to gather data from vertex-only transformations.

When this value is [false](../../swift/false.md), no fragments are processed and the vertex shader function needs to return `void`.

## See Also

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [alphaToOneEnabled](isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [inputPrimitiveTopology](inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [rasterSampleCount](rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
