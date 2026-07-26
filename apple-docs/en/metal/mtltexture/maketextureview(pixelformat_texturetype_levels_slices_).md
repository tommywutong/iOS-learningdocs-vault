---
title: 'makeTextureView(pixelFormat:textureType:levels:slices:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 9.0+, macOS 10.11+, tvOS 9.0+, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/maketextureview%28pixelformat%3Atexturetype%3Alevels%3Aslices%3A%29.json'
content_hash: 'sha256:3b252af4012bb068'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# makeTextureView(pixelFormat:textureType:levels:slices:)

<sub>Instance Method</sub>

Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels levelRange: Range<Int>, slices sliceRange: Range<Int>) -> (any MTLTexture)?
```

## Parameters

- `pixelFormat` — A new pixel format, which needs to be compatible with the original pixel format.

- `textureType` — A new texture type, which can be cast according to the original texture type as listed the table below.

- `levelRange` — A new base level range that restricts which mipmap levels are visible in the new texture.

- `sliceRange` — A new base slice range that restricts which array slices are visible in the new texture.

## Return Value

A new texture object that shares the same storage allocation of the calling texture object.

## Discussion

The texture type can be cast between the targets listed in the following table.

| Original texture type | New texture type |
|---|---|
| [MTLTextureType1D](../mtltexturetype/type1d.md) | [MTLTextureType1D](../mtltexturetype/type1d.md) |
| [MTLTextureType2D](../mtltexturetype/type2d.md) | [MTLTextureType2D](../mtltexturetype/type2d.md) or [MTLTextureType2DArray](../mtltexturetype/type2darray.md) |
| [MTLTextureType2DArray](../mtltexturetype/type2darray.md), [MTLTextureTypeCube](../mtltexturetype/typecube.md), or [MTLTextureTypeCubeArray](../mtltexturetype/typecubearray.md) | [MTLTextureType2D](../mtltexturetype/type2d.md), [MTLTextureType2DArray](../mtltexturetype/type2darray.md), [MTLTextureTypeCube](../mtltexturetype/typecube.md), or [MTLTextureTypeCubeArray](../mtltexturetype/typecubearray.md) |
| [MTLTextureType3D](../mtltexturetype/type3d.md) | [MTLTextureType3D](../mtltexturetype/type3d.md) |

The `length` value of the `sliceRange` parameter needs to be `6` if the new texture type value is [MTLTextureTypeCube](../mtltexturetype/typecube.md), or a multiple of `6` if the new texture type value is [MTLTextureTypeCubeArray](../mtltexturetype/typecubearray.md).

For more information on pixel format restrictions, see [- newTextureViewWithPixelFormat:](<maketextureview(pixelformat_).md>)

## See Also

### Related Documentation

- [parentRelativeLevel](parentrelativelevel.md) — The base level of the parent texture used to create this texture.
- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.

### Creating textures by reinterpreting existing texture data

- [- newTextureViewWithPixelFormat:](<maketextureview(pixelformat_).md>) — Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)](<maketextureview(pixelformat_texturetype_levels_slices_swizzle_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.
