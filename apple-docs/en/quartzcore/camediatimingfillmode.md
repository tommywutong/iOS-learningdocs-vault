---
title: CAMediaTimingFillMode
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfillmode
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfillmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfillmode.json'
content_hash: 'sha256:32ae86f4edb98987'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMediaTimingFillMode

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAMediaTimingFillMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<camediatimingfillmode/init(rawvalue_).md>)

### Type Properties

- [kCAFillModeBackwards](camediatimingfillmode/backwards.md) — The receiver clamps values before zero to zero when the animation is completed.
- [kCAFillModeBoth](camediatimingfillmode/both.md) — The receiver clamps values at both ends of the object’s time space
- [kCAFillModeForwards](camediatimingfillmode/forwards.md) — The receiver remains visible in its final state when the animation is completed.
- [kCAFillModeRemoved](camediatimingfillmode/removed.md) — The receiver is removed from the presentation when the animation is completed.

## See Also

### Data Types

- [CAAnimationCalculationMode](caanimationcalculationmode.md)
- [CAAnimationRotationMode](caanimationrotationmode.md)
- [CAEmitterLayerEmitterMode](caemitterlayeremittermode.md)
- [CAEmitterLayerEmitterShape](caemitterlayeremittershape.md)
- [CAEmitterLayerRenderMode](caemitterlayerrendermode.md)
- [CAGradientLayerType](cagradientlayertype.md)
- [CALayerContentsFilter](calayercontentsfilter.md)
- [CALayerContentsFormat](calayercontentsformat.md)
- [CALayerContentsGravity](calayercontentsgravity.md)
- [CALayerCornerCurve](calayercornercurve.md)
- [CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [CAShapeLayerFillRule](cashapelayerfillrule.md)
- [CAShapeLayerLineCap](cashapelayerlinecap.md)
- [CAShapeLayerLineJoin](cashapelayerlinejoin.md)
