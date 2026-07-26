---
title: renderTarget
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureusage/rendertarget
source_url: 'https://developer.apple.com/documentation/metal/mtltextureusage/rendertarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureusage/rendertarget.json'
content_hash: 'sha256:3a0d2f0f68beed9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureUsage](../mtltextureusage.md)

# renderTarget

<sub>Type Property</sub>

An option for rendering to the texture in a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var renderTarget: MTLTextureUsage { get }
```

## Discussion

Set this option if you use the given texture as a color, depth, or stencil render target in any render pass. This option allows you to assign the texture to the [texture](../mtlrenderpassattachmentdescriptor/texture.md) property of an [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md).

> [!important] Important
> Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [MTLTextureUsageRenderTarget](rendertarget.md) option if you render to a given texture, but don’t set the [MTLTextureUsageShaderWrite](shaderwrite.md) option if you don’t write to the texture. The [MTLTextureUsageRenderTarget](rendertarget.md) and [MTLTextureUsageShaderWrite](shaderwrite.md) options aren’t equivalent, and setting [MTLTextureUsageRenderTarget](rendertarget.md) doesn’t require you to also set [MTLTextureUsageShaderWrite](shaderwrite.md).

## See Also

### Specifying texture usage options

- [MTLTextureUsageUnknown](unknown.md) — An option for a texture whose usage is unknown.
- [MTLTextureUsageShaderRead](shaderread.md) — An option for reading or sampling from the texture in a shader.
- [MTLTextureUsageShaderWrite](shaderwrite.md) — An option for writing to the texture in a shader.
- [MTLTextureUsageShaderAtomic](shaderatomic.md) — An option that enables atomic memory operations on texture elements in shader code.
- [MTLTextureUsagePixelFormatView](pixelformatview.md) — An option to create texture views with a different component layout.
