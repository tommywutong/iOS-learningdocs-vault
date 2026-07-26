---
title: tileWidth
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderpassdescriptor/tilewidth
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/tilewidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/tilewidth.json'
content_hash: 'sha256:2818b9edb74305f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# tileWidth

<sub>Instance Property</sub>

The width of the tiles, in pixels, a render pass you create with this descriptor applies to its attachments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileWidth: Int { get set }
```

## Discussion

For tile-based rendering, Metal divides each render attachment into smaller regions, or _tiles_. The property’s default is `0`, which tells Metal to select a size that fits in tile memory.

See [Tailor your apps for Apple GPUs and tile-based deferred rendering](../tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering.md) for more information about tiles, tile memory, and deferred rendering.
