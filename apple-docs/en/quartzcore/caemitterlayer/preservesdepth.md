---
title: preservesDepth
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/preservesdepth
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/preservesdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/preservesdepth.json'
content_hash: 'sha256:ffaf99d81e78cafc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# preservesDepth

<sub>Instance Property</sub>

Defines whether the layer flattens the particles into its plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preservesDepth: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the layer renders its particles as if they directly inhabit the three-dimensional coordinate space of the layer’s superlayer. When enabled, the effect of the layer’s `filters`, `backgroundFilters`, and shadow related properties is undefined.

Default is [false](../../swift/false.md).

## See Also

### Emitter Cell Attribute Multipliers

- [scale](scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [seed](seed.md) — Specifies the seed used to initialize the random number generator.
- [spin](spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [velocity](velocity.md) — Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [birthRate](birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [emitterMode](emittermode.md) — Specifies the emitter mode.
- [lifetime](lifetime.md) — Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
