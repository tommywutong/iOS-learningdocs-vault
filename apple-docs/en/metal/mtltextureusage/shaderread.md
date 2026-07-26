---
title: shaderRead
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/shaderread
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/shaderread'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/shaderread.json'
content_hash: 'sha256:2ac443f35f479e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# shaderRead

<sub>Type Property</sub>

An option for reading or sampling from the texture in a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var shaderRead: MTLTextureUsage { get }
```

## Discussion

Set this option if you access the given texture with a `read()` or `sample()` function in any shader. This option enables the `access::read` and `access::sample` attributes for the texture. For more information about texture functions and access attributes, see [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364).

If the texture is a read-write texture that you also access with a `write()` function in the same shader, set the [MTLTextureUsageShaderWrite](shaderwrite.md) option to enable the `access::read_write` attribute.

## See Also

### Specifying texture usage options

- [MTLTextureUsageUnknown](unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderWrite](shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageShaderAtomic](shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsageRenderTarget](rendertarget.md) — An option for rendering to the texture in a render pass.
- [MTLTextureUsagePixelFormatView](pixelformatview.md) — An option to create texture views with a different component layout.
