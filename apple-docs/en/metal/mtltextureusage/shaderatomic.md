---
title: shaderAtomic
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/shaderatomic
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/shaderatomic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/shaderatomic.json'
content_hash: 'sha256:01b57f6431ecde14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# shaderAtomic

<sub>Type Property</sub>

An option that enables atomic memory operations on texture elements in shader code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var shaderAtomic: MTLTextureUsage { get }
```

## Discussion

Shaders can run atomic memory operations on textures with specific element type and pixel format combinations:

| Shader element type | Pixel format |
|---|---|
| `int` | [MTLPixelFormatR32Sint](../mtlpixelformat/r32sint.md) |
| `uint` | [MTLPixelFormatR32Uint](../mtlpixelformat/r32uint.md) |
| `ulong` | [MTLPixelFormatRG32Uint](../mtlpixelformat/rg32uint.md) |

> [!note] Note
> Applying this usage option to a texture disables lossless compression.

## See Also

### Specifying texture usage options

- [MTLTextureUsageUnknown](unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderRead](shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderWrite](shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageRenderTarget](rendertarget.md) — An option for rendering to the texture in a render pass.
- [MTLTextureUsagePixelFormatView](pixelformatview.md) — An option to create texture views with a different component layout.
