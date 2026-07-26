---
title: lifetime
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/lifetime
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/lifetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/lifetime.json'
content_hash: 'sha256:e46f86ae99d051d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# lifetime

<sub>Instance Property</sub>

Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lifetime: Float { get set }
```

## Discussion

Default value is `1.0`.

By setting an emitter’s [lifetime](lifetime.md) to `0`, you effectively stop particle emission: all new particles created have their [lifetime](../caemittercell/lifetime.md) set to `0` and are never rendered.

## See Also

### Emitter Cell Attribute Multipliers

- [scale](scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [seed](seed.md) — Specifies the seed used to initialize the random number generator.
- [spin](spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [velocity](velocity.md) — Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [birthRate](birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [emitterMode](emittermode.md) — Specifies the emitter mode.
- [preservesDepth](preservesdepth.md) — Defines whether the layer flattens the particles into its plane.
