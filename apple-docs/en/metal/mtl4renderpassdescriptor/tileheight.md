---
title: tileHeight
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/tileheight
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/tileheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/tileheight.json'
content_hash: 'sha256:55ad4e04e79b1dd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# tileHeight

<sub>Instance Property</sub>

The height of the tiles, in pixels, a render pass you create with this descriptor applies to its attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileHeight: Int { get set }
```

## Discussion

For tile-based rendering, Metal divides each render attachment into smaller regions, or _tiles_. The property’s default is `0`, which tells Metal to select a size that fits in tile memory.

See [Tailor your apps for Apple GPUs and tile-based deferred rendering](../tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md) for more information about tiles, tile memory, and deferred rendering.
