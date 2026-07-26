---
title: isAlphaToOneEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/isalphatooneenabled
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/isalphatooneenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/isalphatooneenabled.json'
content_hash: 'sha256:9dacb0a4597a9977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# isAlphaToOneEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isAlphaToOneEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

If enabled, alpha channel fragment values are only forced for `colorAttachments[0]`. Other attachments are unaffected.

You may use `alphaToOneEnabled` when you want to write an alpha value that represents partial coverage of the pixel, but also want to disable blending (by forcing alpha to one).

## See Also

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [rasterizationEnabled](israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [inputPrimitiveTopology](inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [rasterSampleCount](rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
