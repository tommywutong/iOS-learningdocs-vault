---
title: 'makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/maketextureview%28pixelformat%3Atexturetype%3Alevels%3Aslices%3Aswizzle%3A%29.json'
content_hash: 'sha256:788e947949307f66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)

<sub>Instance Method</sub>

Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels levelRange: Range<Int>, slices sliceRange: Range<Int>, swizzle: MTLTextureSwizzleChannels) -> (any MTLTexture)?
```

## Parameters

- `pixelFormat` — A new pixel format, which needs to be compatible with the original pixel format.

- `textureType` — A new texture type.

- `levelRange` — A new base level range that restricts which mipmap levels are visible in the new texture.

- `sliceRange` — A new base slice range that restricts which array slices are visible in the new texture.

- `swizzle` — The swizzle pattern the GPU uses to reorder the data when sampling or reading the texture.

## Discussion

For more information on texture views, see [makeTextureView(pixelFormat:textureType:levels:slices:)](<maketextureview(pixelformat_texturetype_levels_slices_).md>)

The swizzle pattern of the view is combined with that of the parent texture to generate the final swizzle pattern. For example: An `[R,G,A,B]` swizzle of a texture with a `[R,1,1,G]` swizzle pattern is `[R,1,G,1]`.

## See Also

### Creating textures by reinterpreting existing texture data

- [- newTextureViewWithPixelFormat:](<maketextureview(pixelformat_).md>) — Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [makeTextureView(pixelFormat:textureType:levels:slices:)](<maketextureview(pixelformat_texturetype_levels_slices_).md>) — Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.
