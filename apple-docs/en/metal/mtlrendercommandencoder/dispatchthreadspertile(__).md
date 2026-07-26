---
title: 'dispatchThreadsPerTile(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/dispatchthreadspertile(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/dispatchthreadspertile(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/dispatchthreadspertile%28_%3A%29.json'
content_hash: 'sha256:8fa2d35b9cb9cea6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# dispatchThreadsPerTile(_:)

<sub>Instance Method</sub>

Encodes a command that invokes GPU functions from the encoder’s current tile render pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchThreadsPerTile(_ threadsPerTile: MTLSize)
```

## Parameters

- `threadsPerTile` — An [MTLSize](../mtlsize.md) instance that represents the number of threads the render pass uses per tile. Set the size’s [width](../mtlsize/width.md) and [height](../mtlsize/height.md) properties to values that are less than or equal to [tileWidth](tilewidth.md) and [tileHeight](tileheight.md), respectively. Some GPU families only support square tile dispatches and require the same value for [width](../mtlsize/width.md) and [height](../mtlsize/height.md). See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check which GPU families support nonsquare dispatches. Set the [depth](../mtlsize/depth.md) property to `1`.

## Discussion

The command invokes the GPU function that’s in the encoder’s current tile render pipeline state. You can configure that state with the following steps:

1. Configure an [MTLTileRenderPipelineDescriptor](../mtltilerenderpipelinedescriptor.md) instance.
2. Create a tile render pipeline state by calling one of the applicable methods of an [MTLDevice](../mtldevice.md) instance, including [- newRenderPipelineStateWithTileDescriptor:options:reflection:error:](<../mtldevice/makerenderpipelinestate(tiledescriptor_options_reflection_).md>).
3. Apply that tile render pipeline state by calling the [- setRenderPipelineState:](<setrenderpipelinestate(__).md>) method.

The method records the encoder’s current rendering state and resources the command needs as it runs. You can safely change the encoder’s render pipeline state to encode other commands after calling this method. Subsequent changes to the state don’t affect the commands already in the encoder’s [MTLCommandBuffer](../mtlcommandbuffer.md).

## See Also

### Drawing with tile shaders

- [tileWidth](tilewidth.md) — The width of the tiles, in pixels, for the render command encoder.
- [tileHeight](tileheight.md) — The height of the tiles, in pixels, for the render command encoder.
