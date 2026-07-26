---
title: Emitter Render Order
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/emitter-render-order
source_url: 'https://developer.apple.com/documentation/quartzcore/emitter-render-order'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/emitter-render-order.json'
content_hash: 'sha256:3ee4abca2f4e6982'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CAEmitterLayer](caemitterlayer.md)

# Emitter Render Order

<sub>API Collection</sub>

These constants specify the order that emitter cells are composited. They are used by the [renderMode](caemitterlayer/rendermode.md) property.

## Topics

### Constants

- [kCAEmitterLayerUnordered](caemitterlayerrendermode/unordered.md) — Particles are rendered unordered. This mode uses source-over compositing.
- [kCAEmitterLayerOldestFirst](caemitterlayerrendermode/oldestfirst.md) — Particles are rendered oldest first. This mode uses source-over compositing.
- [kCAEmitterLayerOldestLast](caemitterlayerrendermode/oldestlast.md) — Particles are rendered oldest last. This mode uses source-over compositing.
- [kCAEmitterLayerBackToFront](caemitterlayerrendermode/backtofront.md) — Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [kCAEmitterLayerAdditive](caemitterlayerrendermode/additive.md) — The particles are rendered using source-additive compositing.

## See Also

### Constants

- [Emitter Shape](emitter-shape.md) — The emission shape is a one, two or three dimensional shape that defines where the emitted particles originate. The shapes are defined by a subset of [emitterPosition](caemitterlayer/emitterposition.md), [emitterZPosition](caemitterlayer/emitterzposition.md), [emitterSize](caemitterlayer/emittersize.md) and [emitterDepth](caemitterlayer/emitterdepth.md) properties.
- [Emitter Modes](emitter-modes.md) — These constants specify the possible emitter modes. They are used by the [emitterMode](caemitterlayer/emittermode.md) property.
