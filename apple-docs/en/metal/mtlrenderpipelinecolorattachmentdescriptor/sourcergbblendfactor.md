---
title: sourceRGBBlendFactor
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.json'
content_hash: 'sha256:4ea4cf91299a085a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md)

# sourceRGBBlendFactor

<sub>Instance Property</sub>

The source blend factor (SBF) used by the RGB blend operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceRGBBlendFactor: MTLBlendFactor { get set }
```

## Discussion

The default value is [MTLBlendFactorOne](../mtlblendfactor/one.md).

## See Also

### Configuring blend factors

- [destinationAlphaBlendFactor](destinationalphablendfactor.md) — The destination blend factor (DBF) used by the alpha blend operation.
- [destinationRGBBlendFactor](destinationrgbblendfactor.md) — The destination blend factor (DBF) used by the RGB blend operation.
- [sourceAlphaBlendFactor](sourcealphablendfactor.md) — The source blend factor (SBF) used by the alpha blend operation.
- [MTLBlendFactor](../mtlblendfactor.md) — The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values (_F(rgb)_) and alpha values (_F(a)_) are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [- setBlendColorRed:green:blue:alpha:](<../mtlrendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) method of `MTLRenderCommandEncoder`.
