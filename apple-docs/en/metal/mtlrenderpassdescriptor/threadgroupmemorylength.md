---
title: threadgroupMemoryLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdescriptor/threadgroupmemorylength
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/threadgroupmemorylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/threadgroupmemorylength.json'
content_hash: 'sha256:4d7e1b9edcc2967e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# threadgroupMemoryLength

<sub>Instance Property</sub>

The per-tile size, in bytes, of the persistent threadgroup memory allocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var threadgroupMemoryLength: Int { get set }
```

## See Also

### Specifying tile shading parameters

- [imageblockSampleLength](imageblocksamplelength.md) — The per-sample size, in bytes, of the largest explicit imageblock layout in the render pass.
- [tileWidth](tilewidth.md) — The tile width, in pixels.
- [tileHeight](tileheight.md) — The tile height, in pixels.
