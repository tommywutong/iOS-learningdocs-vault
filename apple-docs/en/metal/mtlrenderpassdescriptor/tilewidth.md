---
title: tileWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/tilewidth
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/tilewidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/tilewidth.json'
content_hash: 'sha256:f0a9907cc6a15cf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# tileWidth

<sub>Instance Property</sub>

The tile width, in pixels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileWidth: Int { get set }
```

## Discussion

The valid tile sizes are `32 x 32`, `32 x 16`, and `16 x 16`. The Metal driver chooses a default size when your app doesn’t set a tile size.

## See Also

### Specifying tile shading parameters

- [imageblockSampleLength](imageblocksamplelength.md) — The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.
- [threadgroupMemoryLength](threadgroupmemorylength.md) — The per-tile size, in bytes, of the persistent threadgroup memory allocation.
- [tileHeight](tileheight.md) — The tile height, in pixels.
