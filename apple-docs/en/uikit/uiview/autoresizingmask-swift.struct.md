---
title: UIView.AutoresizingMask
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/autoresizingmask-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiview/autoresizingmask-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/autoresizingmask-swift.struct.json'
content_hash: 'sha256:4e0e32ad5442d4a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.AutoresizingMask

<sub>Structure</sub>

Options for automatic view resizing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct AutoresizingMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIViewAutoresizingFlexibleLeftMargin](autoresizingmask-swift.struct/flexibleleftmargin.md) — Resizing performed by expanding or shrinking a view in the direction of the left margin.
- [UIViewAutoresizingFlexibleWidth](autoresizingmask-swift.struct/flexiblewidth.md) — Resizing performed by expanding or shrinking a view’s width.
- [UIViewAutoresizingFlexibleRightMargin](autoresizingmask-swift.struct/flexiblerightmargin.md) — Resizing performed by expanding or shrinking a view in the direction of the right margin.
- [UIViewAutoresizingFlexibleTopMargin](autoresizingmask-swift.struct/flexibletopmargin.md) — Resizing performed by expanding or shrinking a view in the direction of the top margin.
- [UIViewAutoresizingFlexibleHeight](autoresizingmask-swift.struct/flexibleheight.md) — Resizing performed by expanding or shrinking a view’s height.
- [UIViewAutoresizingFlexibleBottomMargin](autoresizingmask-swift.struct/flexiblebottommargin.md) — Resizing performed by expanding or shrinking a view in the direction of the bottom margin.

### Initializers

- [init(rawValue:)](<autoresizingmask-swift.struct/init(rawvalue_).md>) — Creates an autoresizing mask structure with the specified raw value.

## See Also

### Constants

- [AnimationCurve](animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](../nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [UISemanticContentAttribute](../uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
