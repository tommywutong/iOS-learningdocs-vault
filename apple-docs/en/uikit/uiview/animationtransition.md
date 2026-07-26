---
title: UIView.AnimationTransition
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/animationtransition
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animationtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animationtransition.json'
content_hash: 'sha256:35d5aa8f5aa9dbbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.AnimationTransition

<sub>Enumeration</sub>

Animation transition options for use in an animation block object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum AnimationTransition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewAnimationTransitionNone](animationtransition/none.md) — The option for indicating that no transition is specified.
- [UIViewAnimationTransitionFlipFromLeft](animationtransition/flipfromleft.md) — A transition that flips a view around a vertical axis from left to right. The left side of the view moves towards the front and right side towards the back.
- [UIViewAnimationTransitionFlipFromRight](animationtransition/flipfromright.md) — A transition that flips a view around a vertical axis from right to left. The right side of the view moves towards the front and left side towards the back.
- [UIViewAnimationTransitionCurlUp](animationtransition/curlup.md) — A transition that curls a view up from the bottom.
- [UIViewAnimationTransitionCurlDown](animationtransition/curldown.md) — A transition that curls a view down from the top.

### Initializers

- [init(rawValue:)](<animationtransition/init(rawvalue_).md>)

## See Also

### Constants

- [AnimationCurve](animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](animationoptions.md) — Options for animating views using block objects.
- [SystemAnimation](systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](../nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](autoresizingmask-swift.struct.md) — Options for automatic view resizing.
- [UISemanticContentAttribute](../uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
