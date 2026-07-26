---
title: velocity
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/velocity
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/velocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/velocity.json'
content_hash: 'sha256:d4b7fe45a825c224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# velocity

<sub>Instance Property</sub>

Defines a multiplier applied to the cell-defined particle velocity. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var velocity: Float { get set }
```

## Discussion

Default value is `1.0`.

## See Also

### Emitter Cell Attribute Multipliers

- [scale](scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [seed](seed.md) — Specifies the seed used to initialize the random number generator.
- [spin](spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [birthRate](birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [emitterMode](emittermode.md) — Specifies the emitter mode.
- [lifetime](lifetime.md) — Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [preservesDepth](preservesdepth.md) — Defines whether the layer flattens the particles into its plane.
