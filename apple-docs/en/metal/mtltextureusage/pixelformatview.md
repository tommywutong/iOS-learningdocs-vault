---
title: pixelFormatView
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/pixelformatview
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/pixelformatview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/pixelformatview.json'
content_hash: 'sha256:afd56e8f1869c132'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# pixelFormatView

<sub>Type Property</sub>

An option to create texture views with a different component layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var pixelFormatView: MTLTextureUsage { get }
```

## Discussion

Set this option if you need to call any of these methods of the texture to create a texture view with a different component layout:

- [- newTextureViewWithPixelFormat:](<../mtltexture/maketextureview(pixelformat_).md>)
- [makeTextureView(pixelFormat:textureType:levels:slices:)](<../mtltexture/maketextureview(pixelformat_texturetype_levels_slices_).md>)
- [newTextureViewWithPixelFormat:textureType:levels:slices:](../mtltexture/newtextureviewwithpixelformat_texturetype_levels_slices_.md)
- [makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)](<../mtltexture/maketextureview(pixelformat_texturetype_levels_slices_swizzle_).md>)
- [newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:](../mtltexture/newtextureviewwithpixelformat_texturetype_levels_slices_swizzle_.md)

For example, if your texture uses the [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md) pixel format, you can reinterpret the data as [MTLPixelFormatR32Uint](../mtlpixelformat/r32uint.md). The pixel layout is considered different if the number of components differs, or if their size or order is different from the components in the original pixel format.

Don’t set this option if your texture view needs to read the component values in a different order. Instead, create a texture view with a swizzle pattern that specifies the new order.

Don’t set this option if your texture view only converts between linear space and sRGB. For example, if your texture uses the [MTLPixelFormatRGBA8Unorm](../mtlpixelformat/rgba8unorm.md) pixel format and your texture view uses [MTLPixelFormatBGRA8Unorm_sRGB](../mtlpixelformat/bgra8unorm_srgb.md).

In iOS devices with GPU family 5 and later, Metal doesn’t apply lossless compression to the given texture if you set this option.

## See Also

### Specifying texture usage options

- [MTLTextureUsageUnknown](unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderRead](shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderWrite](shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageShaderAtomic](shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsageRenderTarget](rendertarget.md) — An option for rendering to the texture in a render pass.
