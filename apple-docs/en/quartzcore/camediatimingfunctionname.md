---
title: CAMediaTimingFunctionName
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/camediatimingfunctionname
source_url: 'https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/camediatimingfunctionname.json'
content_hash: 'sha256:236bd8fdec727f32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAMediaTimingFunctionName

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAMediaTimingFunctionName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<camediatimingfunctionname/init(rawvalue_).md>)

### Type Properties

- [kCAMediaTimingFunctionDefault](camediatimingfunctionname/default.md) — The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.
- [kCAMediaTimingFunctionEaseIn](camediatimingfunctionname/easein.md) — Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [kCAMediaTimingFunctionEaseInEaseOut](camediatimingfunctionname/easeineaseout.md) — Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [kCAMediaTimingFunctionEaseOut](camediatimingfunctionname/easeout.md) — Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [kCAMediaTimingFunctionLinear](camediatimingfunctionname/linear.md) — Linear pacing, which causes an animation to occur evenly over its duration.

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
- [CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [CAShapeLayerFillRule](cashapelayerfillrule.md)
- [CAShapeLayerLineCap](cashapelayerlinecap.md)
- [CAShapeLayerLineJoin](cashapelayerlinejoin.md)
