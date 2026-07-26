---
title: 'supportsTextureSampleCount(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/supportstexturesamplecount(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportstexturesamplecount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportstexturesamplecount%28_%3A%29.json'
content_hash: 'sha256:83302ece59922ac4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsTextureSampleCount(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsTextureSampleCount(_ sampleCount: Int) -> Bool
```

## Parameters

- `sampleCount` — The number of points a GPU can sample from a texture.

## Discussion

The number of points the GPU can sample a texture varies by device:

| Sample count | Devices |
|---|---|
| 1 | All devices |
| 2 | All iOS devices ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) All tvOS devices ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Some macOS devices |
| 4 | All devices |
| 8 | Some macOS devices |

Consider a GPU device’s limitations for sample count by checking [MTLTexture](../mtltexture.md)`.`[sampleCount](../mtltexture/samplecount.md) when configuring these properties:

- [MTLTextureDescriptor](../mtltexturedescriptor.md)`.`[sampleCount](../mtltexturedescriptor/samplecount.md)
- [MTLRenderPipelineDescriptor](../mtlrenderpipelinedescriptor.md)`.`[rasterSampleCount](../mtlrenderpipelinedescriptor/rastersamplecount.md)
- [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)`.`[rasterSampleCount](../mtltilerenderpipelinedescriptor/rastersamplecount.md)
- [MTLMeshRenderPipelineDescriptor](../mtlmeshrenderpipelinedescriptor.md)`.`[rasterSampleCount](../mtlmeshrenderpipelinedescriptor/rastersamplecount.md)
- [MTKView](../../metalkit/mtkview.md)`.`[sampleCount](../../metalkit/mtkview/samplecount.md)

## See Also

### Creating samplers

- [- newSamplerStateWithDescriptor:](<makesamplerstate(descriptor_).md>) — Creates a sampler state instance.
- [getDefaultSamplePositions(sampleCount:)](<getdefaultsamplepositions(samplecount_).md>) — Returns the default sample locations based on the number of samples.
