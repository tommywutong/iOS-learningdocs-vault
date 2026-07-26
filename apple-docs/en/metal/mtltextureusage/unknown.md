---
title: unknown
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/unknown
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/unknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/unknown.json'
content_hash: 'sha256:7ce1082f201c5059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# unknown

<sub>Type Property</sub>

An option for a texture whose usage is unknown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var unknown: MTLTextureUsage { get }
```

## Discussion

Set this option if you’re not sure how your app uses the given texture, but you want to be able to use it in many ways. This might be the case if you have multiple code paths and it’s unclear how your app specifically uses the texture at runtime.

This is the most flexible usage option for a texture, but it incurs a significant performance cost. Metal can’t optimize operations for the texture if you don’t set specific usage options.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to the given texture if you set this option.

## See Also

### Specifying texture usage options

- [MTLTextureUsageShaderRead](shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderWrite](shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageShaderAtomic](shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsageRenderTarget](rendertarget.md) — An option for rendering to the texture in a render pass.
- [MTLTextureUsagePixelFormatView](pixelformatview.md) — An option to create texture views with a different component layout.
