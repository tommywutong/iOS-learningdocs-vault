---
title: CAEmitterLayerRenderMode
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayerrendermode
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayerrendermode.json'
content_hash: 'sha256:56197a00b232b4df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEmitterLayerRenderMode

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAEmitterLayerRenderMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<caemitterlayerrendermode/init(rawvalue_).md>)

### Type Properties

- [kCAEmitterLayerAdditive](caemitterlayerrendermode/additive.md) — The particles are rendered using source-additive compositing.
- [kCAEmitterLayerBackToFront](caemitterlayerrendermode/backtofront.md) — Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [kCAEmitterLayerOldestFirst](caemitterlayerrendermode/oldestfirst.md) — Particles are rendered oldest first. This mode uses source-over compositing.
- [kCAEmitterLayerOldestLast](caemitterlayerrendermode/oldestlast.md) — Particles are rendered oldest last. This mode uses source-over compositing.
- [kCAEmitterLayerUnordered](caemitterlayerrendermode/unordered.md) — Particles are rendered unordered. This mode uses source-over compositing.

## See Also

### Data Types

- [CAAnimationCalculationMode](caanimationcalculationmode.md)
- [CAAnimationRotationMode](caanimationrotationmode.md)
- [CAEmitterLayerEmitterMode](caemitterlayeremittermode.md)
- [CAEmitterLayerEmitterShape](caemitterlayeremittershape.md)
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
