---
title: rasterSampleCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor/rastersamplecount
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/rastersamplecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor/rastersamplecount.json'
content_hash: 'sha256:a4db3c60fbea6dab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)

# rasterSampleCount

<sub>Instance Property</sub>

The number of samples the pipeline applies for each fragment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rasterSampleCount: Int { get set }
```

## Discussion

The render pipeline state honors this property only if the pipeline render targets support multisampling.

> [!important] Important
> This property needs to be `1` if the render targets don’t support multisampling.

When your create an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance, this property’s value needs to be equal to the number of render target textures. Furthermore, the texture type of all render target textures need to be [MTLTextureType2DMultisample](../mtltexturetype/type2dmultisample.md).

The number of samples a GPU supports varies by device. You can check whether an [MTLDevice](../mtldevice.md) instance supports a specific sample count by calling its [- supportsTextureSampleCount:](<../mtldevice/supportstexturesamplecount(__).md>) method.

The default value for this property is `1`.

## See Also

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [alphaToOneEnabled](isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [rasterizationEnabled](israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [inputPrimitiveTopology](inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_
