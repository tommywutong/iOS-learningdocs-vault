---
title: line
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayeremittershape/line
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/line'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayeremittershape/line.json'
content_hash: 'sha256:2bf803ef37d1618b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterLayerEmitterShape](../caemitterlayeremittershape.md)

# line

<sub>Type Property</sub>

Particles are emitted along a line from (`emitterPosition.x - emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`) to (`emitterPosition.x + emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let line: CAEmitterLayerEmitterShape
```

## See Also

### Constants

- [kCAEmitterLayerPoint](point.md) — Particles are emitted from a single point at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`)
- [kCAEmitterLayerRectangle](rectangle.md) — Particles are emitted from a rectangle with opposite corners [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition].
- [kCAEmitterLayerCuboid](cuboid.md) — Particles are emitted from a cuboid (3D rectangle) with opposite corners: [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition - emitterDepth/2], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition+emitterDepth/2].
- [kCAEmitterLayerCircle](circle.md) — Particles are emitted from a circle centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
- [kCAEmitterLayerSphere](sphere.md) — Particles are emitted from a sphere centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
