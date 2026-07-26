---
title: imageblockSampleLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/imageblocksamplelength
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/imageblocksamplelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/imageblocksamplelength.json'
content_hash: 'sha256:fabcdf77464242e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# imageblockSampleLength

<sub>Instance Property</sub>

The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var imageblockSampleLength: Int { get set }
```

## Discussion

If `imageBlockSampleLength` isn’t specified, Metal determines the imageblock sample length from the render pass attachment formats.  If any render pipelines bound to the encoder reference imageblocks with explicit layout, you need to set this property.

## See Also

### Specifying tile shading parameters

- [threadgroupMemoryLength](threadgroupmemorylength.md) — The per-tile size, in bytes, of the persistent threadgroup memory allocation.
- [tileWidth](tilewidth.md) — The tile width, in pixels.
- [tileHeight](tileheight.md) — The tile height, in pixels.
