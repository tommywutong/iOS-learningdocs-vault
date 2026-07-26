---
title: seed
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/seed
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/seed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/seed.json'
content_hash: 'sha256:017adba3376e6d9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# seed

<sub>Instance Property</sub>

Specifies the seed used to initialize the random number generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var seed: UInt32 { get set }
```

## Discussion

Each layer has its own random number generator state. Emitter cell properties that are defined as a mean and a range, such as a cell’s `speed`, the value of the properties are uniformly distributed in the interval [M - R/2, M + R/2].

## See Also

### Emitter Cell Attribute Multipliers

- [scale](scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [spin](spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [velocity](velocity.md) — Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [birthRate](birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [emitterMode](emittermode.md) — Specifies the emitter mode.
- [lifetime](lifetime.md) — Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [preservesDepth](preservesdepth.md) — Defines whether the layer flattens the particles into its plane.
