---
title: shaderWrite
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/shaderwrite
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/shaderwrite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/shaderwrite.json'
content_hash: 'sha256:78d71ddcbdfc2f76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# shaderWrite

<sub>Type Property</sub>

An option for writing to the texture in a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var shaderWrite: MTLTextureUsage { get }
```

## Discussion

Set this option if you access the given texture with a `write()` function in any shader. This option enables the `access::write` attribute for the texture. For more information about texture functions and access attributes, see [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364).

If the texture is a read-write texture that you also access with a `read()` function in the same shader, set the [MTLTextureUsageShaderRead](shaderread.md) option to enable the `access::read_write` attribute.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to the given texture if you set this option.

> [!important] Important
> Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [MTLTextureUsageRenderTarget](rendertarget.md) option if you render to a given texture, but don’t set the [MTLTextureUsageShaderWrite](shaderwrite.md) option if you don’t write to the texture. The [MTLTextureUsageRenderTarget](rendertarget.md) and [MTLTextureUsageShaderWrite](shaderwrite.md) options aren’t equivalent, and setting [MTLTextureUsageRenderTarget](rendertarget.md) doesn’t require you to also set [MTLTextureUsageShaderWrite](shaderwrite.md).

## See Also

### Specifying texture usage options

- [MTLTextureUsageUnknown](unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderRead](shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderAtomic](shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsageRenderTarget](rendertarget.md) — An option for rendering to the texture in a render pass.
- [MTLTextureUsagePixelFormatView](pixelformatview.md) — An option to create texture views with a different component layout.
