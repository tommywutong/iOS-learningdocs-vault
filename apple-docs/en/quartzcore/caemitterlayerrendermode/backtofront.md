---
title: backToFront
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayerrendermode/backtofront
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode/backtofront'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayerrendermode/backtofront.json'
content_hash: 'sha256:1661f7e7d5c71055'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayerRenderMode](../caemitterlayerrendermode.md)

# backToFront

<sub>Type Property</sub>

Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let backToFront: CAEmitterLayerRenderMode
```

## See Also

### Constants

- [kCAEmitterLayerUnordered](unordered.md) — Particles are rendered unordered. This mode uses source-over compositing.
- [kCAEmitterLayerOldestFirst](oldestfirst.md) — Particles are rendered oldest first. This mode uses source-over compositing.
- [kCAEmitterLayerOldestLast](oldestlast.md) — Particles are rendered oldest last. This mode uses source-over compositing.
- [kCAEmitterLayerAdditive](additive.md) — The particles are rendered using source-additive compositing.
