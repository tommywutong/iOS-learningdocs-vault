---
title: MTLBlendFactor.sourceColor
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendfactor/sourcecolor
source_url: 'https://developer.apple.com/documentation/metal/mtlblendfactor/sourcecolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendfactor/sourcecolor.json'
content_hash: 'sha256:2bee4de8b202f43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendFactor](../mtlblendfactor.md)

# MTLBlendFactor.sourceColor

<sub>Case</sub>

Blend factor of source values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case sourceColor
```

## Discussion

`F(rgb) = Source.rgb`

`F(a) = Source.a`

## See Also

### Blend factors

- [MTLBlendFactorZero](zero.md) — Blend factor of zero.
- [MTLBlendFactorOne](one.md) — Blend factor of one.
- [MTLBlendFactorOneMinusSourceColor](oneminussourcecolor.md) — Blend factor of one minus source values.
- [MTLBlendFactorSourceAlpha](sourcealpha.md) — Blend factor of source alpha.
- [MTLBlendFactorOneMinusSourceAlpha](oneminussourcealpha.md) — Blend factor of one minus source alpha.
- [MTLBlendFactorDestinationColor](destinationcolor.md) — Blend factor of destination values.
- [MTLBlendFactorOneMinusDestinationColor](oneminusdestinationcolor.md) — Blend factor of one minus destination values.
- [MTLBlendFactorDestinationAlpha](destinationalpha.md) — Blend factor of destination alpha.
- [MTLBlendFactorOneMinusDestinationAlpha](oneminusdestinationalpha.md) — Blend factor of one minus destination alpha.
- [MTLBlendFactorSourceAlphaSaturated](sourcealphasaturated.md) — Blend factor of the minimum of either source alpha or one minus destination alpha.
- [MTLBlendFactorBlendColor](blendcolor.md) — A blend factor that applies the blend color’s red, green, and blue components.
- [MTLBlendFactorOneMinusBlendColor](oneminusblendcolor.md) — A blend factor that applies one minus the blend color’s red, green, and blue components.
- [MTLBlendFactorBlendAlpha](blendalpha.md) — Blend factor of alpha value.
- [MTLBlendFactorOneMinusBlendAlpha](oneminusblendalpha.md) — Blend factor of one minus alpha value.
- [MTLBlendFactorSource1Color](source1color.md) — Blend factor of source values. This option supports dual-source blending and reads from the second color output of the fragment function.
