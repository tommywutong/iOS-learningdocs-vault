---
title: rasterSampleCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltilerenderpipelinedescriptor/rastersamplecount
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/rastersamplecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinedescriptor/rastersamplecount.json'
content_hash: 'sha256:1e89f832bd08d0ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md)

# rasterSampleCount

<sub>Instance Property</sub>

The number of samples in each fragment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rasterSampleCount: Int { get set }
```

## Discussion

The default value is `1`. This value is used only if the pipeline render targets support multisampling. If the render targets don’t support multisampling, then this value needs to be `1`.

When you create a  [MTLRenderCommandEncoder](../mtlrendercommandencoder.md), the [sampleCount](../mtltexture/samplecount.md) value of all attachments need to match this `sampleCount` value. Furthermore, the texture type of all attachments need to be [MTLTextureType2DMultisample](../mtltexturetype/type2dmultisample.md).

Support for different sample count values varies by device instance. Call the [- supportsTextureSampleCount:](<../mtldevice/supportstexturesamplecount(__).md>) method on an [MTLDevice](../mtldevice.md) instance to determine whether it supports a specific sample count.

## See Also

### Specifying rasterization and visibility state

- [threadgroupSizeMatchesTileSize](threadgroupsizematchestilesize.md) — A Boolean value that indicates whether all threadgroups for this pipeline completely cover tiles.
