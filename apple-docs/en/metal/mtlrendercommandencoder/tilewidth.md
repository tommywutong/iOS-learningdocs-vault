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
doc_path: /documentation/metal/mtlrendercommandencoder/tilewidth
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/tilewidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/tilewidth.json'
content_hash: 'sha256:07d21a3847e608b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# tileWidth

<sub>Instance Property</sub>

The width of the tiles, in pixels, for the render command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileWidth: Int { get }
```

## Discussion

The value comes from the [tileWidth](../mtlrenderpassdescriptor/tilewidth.md) property of the [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) at the time you create the render command encoder.

## See Also

### Drawing with tile shaders

- [- dispatchThreadsPerTile:](<dispatchthreadspertile(__).md>) — Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.
- [tileHeight](tileheight.md) — The height of the tiles, in pixels, for the render command encoder.
