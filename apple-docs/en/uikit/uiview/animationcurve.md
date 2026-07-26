---
title: UIView.AnimationCurve
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/animationcurve
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animationcurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animationcurve.json'
content_hash: 'sha256:78e230d9c9f7877c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.AnimationCurve

<sub>Enumeration</sub>

Specifies the supported animation curves.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum AnimationCurve
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewAnimationCurveEaseInOut](animationcurve/easeinout.md) — An ease-in ease-out curve causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing. This is the default curve for most animations.
- [UIViewAnimationCurveEaseIn](animationcurve/easein.md) — An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [UIViewAnimationCurveEaseOut](animationcurve/easeout.md) — An ease-out curve causes the animation to begin quickly, and then slow down as it completes.
- [UIViewAnimationCurveLinear](animationcurve/linear.md) — A linear animation curve causes an animation to occur evenly over its duration.

### Initializers

- [init(rawValue:)](<animationcurve/init(rawvalue_).md>)

## See Also

### Constants

- [AnimationOptions](animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](../nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](autoresizingmask-swift.struct.md) — Options for automatic view resizing.
- [UISemanticContentAttribute](../uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
