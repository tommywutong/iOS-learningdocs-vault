---
title: oldestFirst
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayerrendermode/oldestfirst
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/oldestfirst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayerrendermode/oldestfirst.json'
content_hash: 'sha256:07a2092613938ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayerRenderMode](../caemitterlayerrendermode.md)

# oldestFirst

<sub>Type Property</sub>

Particles are rendered oldest first. This mode uses source-over compositing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let oldestFirst: CAEmitterLayerRenderMode
```

## See Also

### Constants

- [kCAEmitterLayerUnordered](unordered.md) — Particles are rendered unordered. This mode uses source-over compositing.
- [kCAEmitterLayerOldestLast](oldestlast.md) — Particles are rendered oldest last. This mode uses source-over compositing.
- [kCAEmitterLayerBackToFront](backtofront.md) — Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [kCAEmitterLayerAdditive](additive.md) — The particles are rendered using source-additive compositing.
