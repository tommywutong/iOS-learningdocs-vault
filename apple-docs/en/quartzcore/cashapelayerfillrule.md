---
title: CAShapeLayerFillRule
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayerfillrule
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayerfillrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayerfillrule.json'
content_hash: 'sha256:64f0f5052c12e10d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAShapeLayerFillRule

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAShapeLayerFillRule
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<cashapelayerfillrule/init(rawvalue_).md>)

### Type Properties

- [kCAFillRuleEvenOdd](cashapelayerfillrule/evenodd.md) — Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.
- [kCAFillRuleNonZero](cashapelayerfillrule/nonzero.md) — Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.

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
- [CAMediaTimingFillMode](camediatimingfillmode.md)
- [CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [CAShapeLayerLineCap](cashapelayerlinecap.md)
- [CAShapeLayerLineJoin](cashapelayerlinejoin.md)
