---
title: MTLBlendFactor
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendfactor
source_url: 'https://developer.apple.com/documentation/metal/mtlblendfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendfactor.json'
content_hash: 'sha256:bb1512a51337097b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBlendFactor

<sub>Enumeration</sub>

The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values (_F(rgb)_) and alpha values (_F(a)_) are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [- setBlendColorRed:green:blue:alpha:](<mtlrendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) method of `MTLRenderCommandEncoder`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLBlendFactor
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Blend factors

- [MTLBlendFactorZero](mtlblendfactor/zero.md) — Blend factor of zero.
- [MTLBlendFactorOne](mtlblendfactor/one.md) — Blend factor of one.
- [MTLBlendFactorSourceColor](mtlblendfactor/sourcecolor.md) — Blend factor of source values.
- [MTLBlendFactorOneMinusSourceColor](mtlblendfactor/oneminussourcecolor.md) — Blend factor of one minus source values.
- [MTLBlendFactorSourceAlpha](mtlblendfactor/sourcealpha.md) — Blend factor of source alpha.
- [MTLBlendFactorOneMinusSourceAlpha](mtlblendfactor/oneminussourcealpha.md) — Blend factor of one minus source alpha.
- [MTLBlendFactorDestinationColor](mtlblendfactor/destinationcolor.md) — Blend factor of destination values.
- [MTLBlendFactorOneMinusDestinationColor](mtlblendfactor/oneminusdestinationcolor.md) — Blend factor of one minus destination values.
- [MTLBlendFactorDestinationAlpha](mtlblendfactor/destinationalpha.md) — Blend factor of destination alpha.
- [MTLBlendFactorOneMinusDestinationAlpha](mtlblendfactor/oneminusdestinationalpha.md) — Blend factor of one minus destination alpha.
- [MTLBlendFactorSourceAlphaSaturated](mtlblendfactor/sourcealphasaturated.md) — Blend factor of the minimum of either source alpha or one minus destination alpha.
- [MTLBlendFactorBlendColor](mtlblendfactor/blendcolor.md) — A blend factor that applies the blend color’s red, green, and blue components.
- [MTLBlendFactorOneMinusBlendColor](mtlblendfactor/oneminusblendcolor.md) — A blend factor that applies one minus the blend color’s red, green, and blue components.
- [MTLBlendFactorBlendAlpha](mtlblendfactor/blendalpha.md) — Blend factor of alpha value.
- [MTLBlendFactorOneMinusBlendAlpha](mtlblendfactor/oneminusblendalpha.md) — Blend factor of one minus alpha value.
- [MTLBlendFactorSource1Color](mtlblendfactor/source1color.md) — Blend factor of source values. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactorOneMinusSource1Color](mtlblendfactor/oneminussource1color.md) — Blend factor of one minus source values. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactorSource1Alpha](mtlblendfactor/source1alpha.md) — Blend factor of source alpha. This option supports dual-source blending and reads from the second color output of the fragment function.
- [MTLBlendFactorOneMinusSource1Alpha](mtlblendfactor/oneminussource1alpha.md) — Blend factor of one minus source alpha. This option supports dual-source blending and reads from the second color output of the fragment function.

### Enumeration Cases

- [MTLBlendFactorUnspecialized](mtlblendfactor/unspecialized.md) — Defers assigning the blend factor.

### Initializers

- [init(rawValue:)](<mtlblendfactor/init(rawvalue_).md>)

## See Also

### Configuring blend factors

- [destinationAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationalphablendfactor.md) — The destination blend factor (DBF) used by the alpha blend operation.
- [destinationRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/destinationrgbblendfactor.md) — The destination blend factor (DBF) used by the RGB blend operation.
- [sourceAlphaBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcealphablendfactor.md) — The source blend factor (SBF) used by the alpha blend operation.
- [sourceRGBBlendFactor](mtlrenderpipelinecolorattachmentdescriptor/sourcergbblendfactor.md) — The source blend factor (SBF) used by the RGB blend operation.
