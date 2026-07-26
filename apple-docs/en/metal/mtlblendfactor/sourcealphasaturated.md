---
title: MTLBlendFactor.sourceAlphaSaturated
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendfactor/sourcealphasaturated
source_url: 'https://developer.apple.com/documentation/metal/mtlblendfactor/sourcealphasaturated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendfactor/sourcealphasaturated.json'
content_hash: 'sha256:2e70d73130302cdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendFactor](../mtlblendfactor.md)

# MTLBlendFactor.sourceAlphaSaturated

<sub>Case</sub>

Blend factor of the minimum of either source alpha or one minus destination alpha.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case sourceAlphaSaturated
```

## Discussion

`F(rgb) = min(Source.a, 1 - Dest.a)`

`F(a) = 1`

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
- [MTLBlendFactorBlendColor](blendcolor.md) — A blend factor that applies the blend color’s red, green, and blue components.
- [MTLBlendFactorOneMinusBlendColor](oneminusblendcolor.md) — A blend factor that applies one minus the blend color’s red, green, and blue components.
- [MTLBlendFactorBlendAlpha](blendalpha.md) — Blend factor of alpha value.
- [MTLBlendFactorOneMinusBlendAlpha](oneminusblendalpha.md) — Blend factor of one minus alpha value.
- [MTLBlendFactorSource1Color](source1color.md) — Blend factor of source values. This option supports dual-source blending and reads from the second color output of the fragment function.
