---
title: emitterShape
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/emittershape
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittershape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/emittershape.json'
content_hash: 'sha256:5405964565434da6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# emitterShape

<sub>Instance Property</sub>

Specifies the emitter shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emitterShape: CAEmitterLayerEmitterShape { get set }
```

## Discussion

The possible values for emitterMode are shown in [Emitter Shape](../emitter-shape.md). The default value is [kCAEmitterLayerPoint](../caemitterlayeremittershape/point.md).

## See Also

### Emitter Geometry

- [renderMode](rendermode.md) — Defines how particle cells are rendered into the layer.
- [emitterPosition](emitterposition.md) — The position of the center of the particle emitter. Animatable.
- [emitterZPosition](emitterzposition.md) — Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [emitterDepth](emitterdepth.md) — Determines the depth of the emitter shape.
- [emitterSize](emittersize.md) — Determines the size of the particle emitter shape. Animatable.
