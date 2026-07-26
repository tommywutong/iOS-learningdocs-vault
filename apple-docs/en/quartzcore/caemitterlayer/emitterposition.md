---
title: emitterPosition
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/emitterposition
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/emitterposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/emitterposition.json'
content_hash: 'sha256:95acbccae5ad673c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# emitterPosition

<sub>Instance Property</sub>

The position of the center of the particle emitter. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emitterPosition: CGPoint { get set }
```

## Discussion

See [Emitter Shape](../emitter-shape.md) for details of how the `emitterPosition` relates to the possible emitter shapes.

Default is `(0.0,0.0)`.

## See Also

### Emitter Geometry

- [renderMode](rendermode.md) — Defines how particle cells are rendered into the layer.
- [emitterShape](emittershape.md) — Specifies the emitter shape.
- [emitterZPosition](emitterzposition.md) — Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [emitterDepth](emitterdepth.md) — Determines the depth of the emitter shape.
- [emitterSize](emittersize.md) — Determines the size of the particle emitter shape. Animatable.
