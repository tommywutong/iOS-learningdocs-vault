---
title: emitterMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/emittermode
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/emittermode.json'
content_hash: 'sha256:5d286eb287b5044c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# emitterMode

<sub>Instance Property</sub>

Specifies the emitter mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emitterMode: CAEmitterLayerEmitterMode { get set }
```

## Discussion

The possible values for emitterMode are shown in [Emitter Modes](../emitter-modes.md). The default value is [kCAEmitterLayerVolume](../caemitterlayeremittermode/volume.md).

## See Also

### Emitter Cell Attribute Multipliers

- [scale](scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [seed](seed.md) — Specifies the seed used to initialize the random number generator.
- [spin](spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [velocity](velocity.md) — Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [birthRate](birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [lifetime](lifetime.md) — Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [preservesDepth](preservesdepth.md) — Defines whether the layer flattens the particles into its plane.
