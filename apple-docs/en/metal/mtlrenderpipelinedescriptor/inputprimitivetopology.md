---
title: inputPrimitiveTopology
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/inputprimitivetopology
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/inputprimitivetopology'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/inputprimitivetopology.json'
content_hash: 'sha256:c88c03416492fc0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# inputPrimitiveTopology

<sub>Instance Property</sub>

The type of primitive topology the pipeline renders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputPrimitiveTopology: MTLPrimitiveTopologyClass { get set }
```

## Discussion

Your app needs to specify this value when layered rendering is enabled.

The default value is `MTLPrimitiveTopologyClassUnspecified`.

## See Also

### Related Documentation

- [renderTargetArrayLength](../mtlrenderpassdescriptor/rendertargetarraylength.md) — The number of active layers that all attachments need to have for layered rendering.

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [alphaToOneEnabled](isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [rasterizationEnabled](israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [rasterSampleCount](rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
