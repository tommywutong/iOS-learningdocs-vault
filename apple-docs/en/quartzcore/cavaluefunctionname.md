---
title: CAValueFunctionName
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cavaluefunctionname
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunctionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunctionname.json'
content_hash: 'sha256:06f164da081273d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAValueFunctionName

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAValueFunctionName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<cavaluefunctionname/init(rawvalue_).md>)

### Type Properties

- [kCAValueFunctionRotateX](cavaluefunctionname/rotatex.md) — A value function that rotates by the input value, in radians, around the x-axis. This value function expects a single input value.
- [kCAValueFunctionRotateY](cavaluefunctionname/rotatey.md) — A value function that rotates by the input value, in radians, around the y-axis. This value function expects a single input value.
- [kCAValueFunctionRotateZ](cavaluefunctionname/rotatez.md) — A value function that rotates by the input value, in radians, around the z-axis. This value function expects a single input value.
- [kCAValueFunctionScale](cavaluefunctionname/scale.md) — A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [kCAValueFunctionScaleX](cavaluefunctionname/scalex.md) — A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.
- [kCAValueFunctionScaleY](cavaluefunctionname/scaley.md) — A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.
- [kCAValueFunctionScaleZ](cavaluefunctionname/scalez.md) — A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.
- [kCAValueFunctionTranslate](cavaluefunctionname/translate.md) — A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.
- [kCAValueFunctionTranslateX](cavaluefunctionname/translatex.md) — A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateY](cavaluefunctionname/translatey.md) — A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.
- [kCAValueFunctionTranslateZ](cavaluefunctionname/translatez.md) — A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.

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
- [CAShapeLayerFillRule](cashapelayerfillrule.md)
- [CAShapeLayerLineCap](cashapelayerlinecap.md)
