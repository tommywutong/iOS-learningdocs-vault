---
title: UIView.KeyframeAnimationOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/keyframeanimationoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiview/keyframeanimationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/keyframeanimationoptions.json'
content_hash: 'sha256:659ddcd353966b24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.KeyframeAnimationOptions

<sub>Structure</sub>

Options for configuring keyframe-based animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct KeyframeAnimationOptions
```

## Overview

Use these options with the [+ animateKeyframesWithDuration:delay:options:animations:completion:](<animatekeyframes(withduration_delay_options_animations_completion_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIViewKeyframeAnimationOptionLayoutSubviews](keyframeanimationoptions/layoutsubviews.md) — The option to lay out subviews at commit time so that they’re animated along with their parent.
- [UIViewKeyframeAnimationOptionAllowUserInteraction](keyframeanimationoptions/allowuserinteraction.md) — The option that allows a person to interact with views while they’re being animated.
- [UIViewKeyframeAnimationOptionBeginFromCurrentState](keyframeanimationoptions/beginfromcurrentstate.md) — The option to start an animation from the current setting associated with an already in-flight animation.
- [UIViewKeyframeAnimationOptionRepeat](keyframeanimationoptions/repeat.md) — The option to repeat an animation indefinitely.
- [UIViewKeyframeAnimationOptionAutoreverse](keyframeanimationoptions/autoreverse.md) — The option to run an animation backwards and forwards.
- [UIViewKeyframeAnimationOptionOverrideInheritedDuration](keyframeanimationoptions/overrideinheritedduration.md) — The option to force an animation to use the original duration value specified when the animation was submitted.
- [UIViewKeyframeAnimationOptionOverrideInheritedOptions](keyframeanimationoptions/overrideinheritedoptions.md) — The option to not inherit the animation type or any options.
- [UIViewKeyframeAnimationOptionCalculationModeLinear](keyframeanimationoptions/calculationmodelinear.md) — The option to use a simple linear calculation when interpolating between keyframe values.
- [UIViewKeyframeAnimationOptionCalculationModeDiscrete](keyframeanimationoptions/calculationmodediscrete.md) — The option to not interpolate between keyframe values, but rather to jump directly to each new keyframe value.
- [UIViewKeyframeAnimationOptionCalculationModePaced](keyframeanimationoptions/calculationmodepaced.md) — The option to compute intermediate keyframe values using a simple pacing algorithm.
- [UIViewKeyframeAnimationOptionCalculationModeCubic](keyframeanimationoptions/calculationmodecubic.md) — The option to compute intermediate frames using a default Catmull-Rom spline that passes through the keyframe values.
- [UIViewKeyframeAnimationOptionCalculationModeCubicPaced](keyframeanimationoptions/calculationmodecubicpaced.md) — The option to compute intermediate frames using the cubic scheme while ignoring the timing properties of the animation.

### Initializers

- [init(rawValue:)](<keyframeanimationoptions/init(rawvalue_).md>) — Creates keyframe animation options with the specified raw value.

## See Also

### Constants

- [AnimationCurve](animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [Axis](../nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](autoresizingmask-swift.struct.md) — Options for automatic view resizing.
- [UISemanticContentAttribute](../uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
