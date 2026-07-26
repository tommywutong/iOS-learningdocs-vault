---
title: renderMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer/rendermode
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer/rendermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer/rendermode.json'
content_hash: 'sha256:3e608bd2ad8c6ebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayer](../caemitterlayer.md)

# renderMode

<sub>Instance Property</sub>

Defines how particle cells are rendered into the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderMode: CAEmitterLayerRenderMode { get set }
```

## Discussion

The possible values for render modes are shown in [Emitter Modes](../emitter-modes.md). The default value is [kCAEmitterLayerUnordered](../caemitterlayerrendermode/unordered.md).

## See Also

### Emitter Geometry

- [emitterPosition](emitterposition.md) — The position of the center of the particle emitter. Animatable.
- [emitterShape](emittershape.md) — Specifies the emitter shape.
- [emitterZPosition](emitterzposition.md) — Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [emitterDepth](emitterdepth.md) — Determines the depth of the emitter shape.
- [emitterSize](emittersize.md) — Determines the size of the particle emitter shape. Animatable.
