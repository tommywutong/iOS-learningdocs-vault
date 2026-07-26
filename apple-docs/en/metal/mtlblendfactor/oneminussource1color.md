---
title: MTLBlendFactor.oneMinusSource1Color
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendfactor/oneminussource1color
source_url: 'https://developer.apple.com/documentation/metal/mtlblendfactor/oneminussource1color'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendfactor/oneminussource1color.json'
content_hash: 'sha256:b6303e56b67d935b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendFactor](../mtlblendfactor.md)

# MTLBlendFactor.oneMinusSource1Color

<sub>Case</sub>

Blend factor of one minus source values. This option supports dual-source blending and reads from the second color output of the fragment function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case oneMinusSource1Color
```

## Discussion

`F(rgb) = 1 - Source.rgb`

`F(a) = 1 - Source.a`

## See Also

### Blend factors

- [MTLBlendFactorZero](zero.md) — Blend factor of zero.
- [MTLBlendFactorOne](one.md) — Blend factor of one.
- [MTLBlendFactorSourceColor](sourcecolor.md) — Blend factor of source values.
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
