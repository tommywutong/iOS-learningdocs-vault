---
title: 'copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationslice:destinationlevel:destinationorigin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/copy%28from%3Asourceslice%3Asourcelevel%3Asourceorigin%3Asourcesize%3Ato%3Adestinationslice%3Adestinationlevel%3Adestinationorigin%3A%29.json'
content_hash: 'sha256:be1670f7ca7c3e65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:)

<sub>Instance Method</sub>

Encodes a command that copies image data from a texture’s slice into another slice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(from sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)
```

## Parameters

- `sourceTexture` — A texture with an [framebufferOnly](../mtltexture/isframebufferonly.md) property value of [false](../../swift/false.md) that the command copies data from. For a texture that uses a compressed pixel format, align the copy region (`sourceOrigin` and `sourceSize`) to the pixel format’s block size.

- `sourceSlice` — A slice within `sourceTexture`.

- `sourceLevel` — A mipmap level within `sourceTexture`.

- `sourceOrigin` — A location within `sourceTexture` that the command begins copying data from. Assign `0` to each dimension that’s not relevant to `sourceTexture`. For example: - If the source texture is a 2D texture, set the origin’s [z](../mtlorigin/z.md) property to `0`. - If the source texture is a 1D texture, set the origin’s [y](../mtlorigin/y.md) and [z](../mtlorigin/z.md) properties to `0`.

- `sourceSize` — An [MTLSize](../mtlsize.md) instance, which can represent a 3D region, that instructs the command how many pixels to copy from `sourceTexture`, starting at `sourceOrigin`. Assign `1` to each dimension that’s not relevant to `sourceTexture`. For example: - If the source texture is a 2D texture, set the size’s [depth](../mtlsize/depth.md) property to `1`. - If the source texture is a 1D texture, set the size’s [height](../mtlsize/height.md) and [depth](../mtlsize/depth.md) properties to `1`. If `sourceTexture` uses a compressed pixel format, set `sourceSize` to a multiple of the pixel format’s block size. If the block extends outside the bounds of the texture, clamp `sourceSize` to the edge of the texture.

- `destinationTexture` — A texture the command copies data to that has the following configuration: - The [framebufferOnly](../mtltexture/isframebufferonly.md) property value is [false](../../swift/false.md). - The pixel format is the same as `sourceTexture`. - The sample count is the same as `sourceTexture`. For a texture that uses a compressed pixel format, align the copy region (`destinationOrigin`) to the pixel format’s block size.

- `destinationSlice` — A slice within `destinationTexture`.

- `destinationLevel` — A mipmap level within `destinationTexture`.

- `destinationOrigin` — A location within `destinationTexture` that the command begins copying data to. Assign `0` to each dimension that’s not relevant to `destinationTexture`. For example: - If the destination texture is a 2D texture, set the origin’s [z](../mtlorigin/z.md) property to `0`. - If the destination texture is a 1D texture, set the origin’s [y](../mtlorigin/y.md) and [z](../mtlorigin/z.md) properties to `0`.

## Discussion

For textures that use a PVRTC pixel format, you can use this method to copy the entire texture, but not a subregion of the texture.

> [!important] Important
> Copying data to overlapping regions within the same texture may result in unexpected behavior.

## See Also

### Copying texture data to another texture

- [- copyFromTexture:toTexture:](<copy(from_to_).md>) — Encodes a command that copies data from one texture to another.
- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<copy(from_sourceslice_sourcelevel_to_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to another texture’s slices.
- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<copy(from_sourceorigin_sourcedimensions_to_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
