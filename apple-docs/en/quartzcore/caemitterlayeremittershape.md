---
title: CAEmitterLayerEmitterShape
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayeremittershape
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayeremittershape.json'
content_hash: 'sha256:861e95148d95e80e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEmitterLayerEmitterShape

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAEmitterLayerEmitterShape
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<caemitterlayeremittershape/init(rawvalue_).md>)

### Type Properties

- [kCAEmitterLayerCircle](caemitterlayeremittershape/circle.md) — Particles are emitted from a circle centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
- [kCAEmitterLayerCuboid](caemitterlayeremittershape/cuboid.md) — Particles are emitted from a cuboid (3D rectangle) with opposite corners: [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition - emitterDepth/2], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition+emitterDepth/2].
- [kCAEmitterLayerLine](caemitterlayeremittershape/line.md) — Particles are emitted along a line from (`emitterPosition.x - emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`) to (`emitterPosition.x + emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`).
- [kCAEmitterLayerPoint](caemitterlayeremittershape/point.md) — Particles are emitted from a single point at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`)
- [kCAEmitterLayerRectangle](caemitterlayeremittershape/rectangle.md) — Particles are emitted from a rectangle with opposite corners [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition].
- [kCAEmitterLayerSphere](caemitterlayeremittershape/sphere.md) — Particles are emitted from a sphere centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.

## See Also

### Data Types

- [CAAnimationCalculationMode](caanimationcalculationmode.md)
- [CAAnimationRotationMode](caanimationrotationmode.md)
- [CAEmitterLayerEmitterMode](caemitterlayeremittermode.md)
- [CAEmitterLayerRenderMode](caemitterlayerrendermode.md)
- [CAGradientLayerType](cagradientlayertype.md)
- [CALayerContentsFilter](calayercontentsfilter.md)
- [CALayerContentsFormat](calayercontentsformat.md)
- [CALayerContentsGravity](calayercontentsgravity.md)
- [CALayerCornerCurve](calayercornercurve.md)
- [CAMediaTimingFillMode](camediatimingfillmode.md)
- [CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [CAShapeLayerFillRule](cashapelayerfillrule.md)
- [CAShapeLayerLineCap](cashapelayerlinecap.md)
- [CAShapeLayerLineJoin](cashapelayerlinejoin.md)
