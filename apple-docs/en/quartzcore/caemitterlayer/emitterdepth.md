---
title: emitterDepth
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/emitterdepth
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/emitterdepth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/emitterdepth.json'
content_hash: 'sha256:af3d088e37fb41dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# emitterDepth

<sub>Instance Property</sub>

Determines the depth of the emitter shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emitterDepth: CGFloat { get set }
```

## Discussion

How the emitter depth is applied depends on the emitter shape. See [Emitter Shape](../emitter-shape.md) for details. Depending on the value of [emitterShape](emittershape.md), this value may be ignored.

Default is `0.0`.

## See Also

### Emitter Geometry

- [renderMode](rendermode.md) — Defines how particle cells are rendered into the layer.
- [emitterPosition](emitterposition.md) — The position of the center of the particle emitter. Animatable.
- [emitterShape](emittershape.md) — Specifies the emitter shape.
- [emitterZPosition](emitterzposition.md) — Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [emitterSize](emittersize.md) — Determines the size of the particle emitter shape. Animatable.
