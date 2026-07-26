---
title: tileHeight
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrendercommandencoder/tileheight
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/tileheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/tileheight.json'
content_hash: 'sha256:9eb8959c4e7a0a8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# tileHeight

<sub>Instance Property</sub>

The height of the tiles, in pixels, for the render command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileHeight: Int { get }
```

## Discussion

The value comes from the [tileHeight](../mtlrenderpassdescriptor/tileheight.md) property of the [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md) at the time you create the render command encoder.

## See Also

### Drawing with tile shaders

- [- dispatchThreadsPerTile:](<dispatchthreadspertile(__).md>) — Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.
- [tileWidth](tilewidth.md) — The width of the tiles, in pixels, for the render command encoder.
