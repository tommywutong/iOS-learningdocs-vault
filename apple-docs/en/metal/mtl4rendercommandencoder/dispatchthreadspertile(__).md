---
title: 'dispatchThreadsPerTile(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/dispatchthreadspertile(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/dispatchthreadspertile(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/dispatchthreadspertile%28_%3A%29.json'
content_hash: 'sha256:0e06d44383b3a426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# dispatchThreadsPerTile(_:)

<sub>Instance Method</sub>

Encodes a command that invokes a tile shader function from the encoder’s current tile render pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreadsPerTile(_ threadsPerTile: MTLSize)
```

## Parameters

- `threadsPerTile` — A [MTLSize](../mtlsize.md) instance that represents the number of threads the render pass uses per tile. Set the size’s [width](../mtlsize/width.md) and [height](../mtlsize/height.md) properties to values that are less than or equal to [tileWidth](tilewidth.md) and [tileHeight](tileheight.md), respectively. Some GPU families only support square tile dispatches and require the same value for width and height. Set [depth](../mtlsize/depth.md) to `1`.

## See Also

### Drawing with tile shaders

- [tileWidth](tilewidth.md) — Sets the width of a tile for this render pass.
- [tileHeight](tileheight.md) — Sets the height of a tile for this render pass.
