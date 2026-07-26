---
title: 'newTextureViewWithPixelFormat:textureType:levels:slices:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/newtextureviewwithpixelformat%3Atexturetype%3Alevels%3Aslices%3A.json'
content_hash: 'sha256:e4829ec8b9202ef4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# newTextureViewWithPixelFormat:textureType:levels:slices:

<sub>Instance Method</sub>

Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLTexture>) newTextureViewWithPixelFormat:(MTLPixelFormat) pixelFormat textureType:(MTLTextureType) textureType levels:(NSRange) levelRange slices:(NSRange) sliceRange;
```

## Parameters

- `pixelFormat` — A new pixel format, which needs to be compatible with the original pixel format.

- `textureType` — A new texture type, which can be cast according to the original texture type as listed in the table below.

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

## Default Implementations

### MTLTexture Implementations

- [makeTextureView(pixelFormat:textureType:levels:slices:)](<maketextureview(pixelformat_texturetype_levels_slices_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.

## See Also

### Related Documentation

- [parentRelativeLevel](parentrelativelevel.md) — The base level of the parent texture used to create this texture.
- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.

### Creating textures by reinterpreting existing texture data

- [- newTextureViewWithPixelFormat:](<maketextureview(pixelformat_).md>) — Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:](newtextureviewwithpixelformat_texturetype_levels_slices_swizzle_.md) — Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.
