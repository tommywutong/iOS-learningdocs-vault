---
title: UIView.TintAdjustmentMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/tintadjustmentmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiview/tintadjustmentmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/tintadjustmentmode-swift.enum.json'
content_hash: 'sha256:93b29abdeaf82504'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.TintAdjustmentMode

<sub>Enumeration</sub>

The tint adjustment mode for the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum TintAdjustmentMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewTintAdjustmentModeAutomatic](tintadjustmentmode-swift.enum/automatic.md) — The tint adjustment mode of the view is the same as its superview’s tint adjustment mode (or `UIViewTintAdjustmentModeNormal` if the view has no superview).
- [UIViewTintAdjustmentModeNormal](tintadjustmentmode-swift.enum/normal.md) — The view’s tint color property returns the completely unmodified tint color of the view.
- [UIViewTintAdjustmentModeDimmed](tintadjustmentmode-swift.enum/dimmed.md) — The view’s tint color property returns a desaturated, dimmed version of the view’s original tint color.

### Initializers

- [init(rawValue:)](<tintadjustmentmode-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [AnimationCurve](animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](../nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](autoresizingmask-swift.struct.md) — Options for automatic view resizing.
- [UISemanticContentAttribute](../uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
