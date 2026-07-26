---
title: 'newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:swizzle:'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/newtextureviewwithpixelformat:texturetype:levels:slices:swizzle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/newtextureviewwithpixelformat%3Atexturetype%3Alevels%3Aslices%3Aswizzle%3A.json'
content_hash: 'sha256:04c733a4ee50bc49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:

<sub>Instance Method</sub>

Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (id<MTLTexture>) newTextureViewWithPixelFormat:(MTLPixelFormat) pixelFormat textureType:(MTLTextureType) textureType levels:(NSRange) levelRange slices:(NSRange) sliceRange swizzle:(MTLTextureSwizzleChannels) swizzle;
```

## Parameters

- `pixelFormat` — A new pixel format, which needs to be compatible with the original pixel format.

- `textureType` — A new texture type.

- `levelRange` — A new base level range that restricts which mipmap levels are visible in the new texture.

- `sliceRange` — A new base slice range that restricts which array slices are visible in the new texture.

- `swizzle` — The swizzle pattern the GPU uses to reorder the data when sampling or reading the texture.

## Return Value

A new texture view.

## Discussion

For more information on texture views, see [newTextureViewWithPixelFormat:textureType:levels:slices:](newtextureviewwithpixelformat_texturetype_levels_slices_.md).

The swizzle pattern of the view is combined with that of the parent texture to generate the final swizzle pattern. For example: An `[R,G,A,B]` swizzle of a texture with a `[R,1,1,G]` swizzle pattern is `[R,1,G,1]`.

## Default Implementations

### MTLTexture Implementations

- [makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)](<maketextureview(pixelformat_texturetype_levels_slices_swizzle_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.

## See Also

### Creating textures by reinterpreting existing texture data

- [- newTextureViewWithPixelFormat:](<maketextureview(pixelformat_).md>) — Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [newTextureViewWithPixelFormat:textureType:levels:slices:](newtextureviewwithpixelformat_texturetype_levels_slices_.md) — Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.
