---
title: UIView.AnimationOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/animationoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animationoptions.json'
content_hash: 'sha256:da832e358c5e5f07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.AnimationOptions

<sub>Structure</sub>

Options for animating views using block objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct AnimationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIViewAnimationOptionLayoutSubviews](animationoptions/layoutsubviews.md) — Lay out subviews at commit time so that they are animated along with their parent.
- [UIViewAnimationOptionAllowUserInteraction](animationoptions/allowuserinteraction.md) — Allow the user to interact with views while they are being animated.
- [UIViewAnimationOptionBeginFromCurrentState](animationoptions/beginfromcurrentstate.md) — Start the animation from the current setting associated with an already in-flight animation.
- [UIViewAnimationOptionRepeat](animationoptions/repeat.md) — Repeat the animation indefinitely.
- [UIViewAnimationOptionAutoreverse](animationoptions/autoreverse.md) — Run the animation backwards and forwards (must be combined with the repeat option).
- [UIViewAnimationOptionOverrideInheritedDuration](animationoptions/overrideinheritedduration.md) — Force the animation to use the original duration value specified when the animation was submitted.
- [UIViewAnimationOptionOverrideInheritedCurve](animationoptions/overrideinheritedcurve.md) — Force the animation to use the original curve value specified when the animation was submitted.
- [UIViewAnimationOptionAllowAnimatedContent](animationoptions/allowanimatedcontent.md) — Animate the views by changing the property values dynamically and redrawing the view.
- [UIViewAnimationOptionShowHideTransitionViews](animationoptions/showhidetransitionviews.md) — Hide or show views during a view transition.
- [UIViewAnimationOptionOverrideInheritedOptions](animationoptions/overrideinheritedoptions.md) — The option to not inherit the animation type or any options.
- [UIViewAnimationOptionCurveEaseInOut](animationoptions/curveeaseinout.md) — Specify an ease-in ease-out curve, which causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [UIViewAnimationOptionCurveEaseIn](animationoptions/curveeasein.md) — An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [UIViewAnimationOptionCurveEaseOut](animationoptions/curveeaseout.md) — An ease-out curve causes the animation to begin quickly, and then slow as it completes.
- [UIViewAnimationOptionCurveLinear](animationoptions/curvelinear.md) — A linear animation curve causes an animation to occur evenly over its duration.
- [UIViewAnimationOptionTransitionFlipFromLeft](animationoptions/transitionflipfromleft.md) — A transition that flips a view around its vertical axis from left to right (the left side of the view moves toward the front and right side toward the back).
- [UIViewAnimationOptionTransitionFlipFromRight](animationoptions/transitionflipfromright.md) — A transition that flips a view around its vertical axis from right to left (the right side of the view moves toward the front and left side toward the back).
- [UIViewAnimationOptionTransitionCurlUp](animationoptions/transitioncurlup.md) — A transition that curls a view up from the bottom.
- [UIViewAnimationOptionTransitionCurlDown](animationoptions/transitioncurldown.md) — A transition that curls a view down from the top.
- [UIViewAnimationOptionTransitionCrossDissolve](animationoptions/transitioncrossdissolve.md) — A transition that dissolves from one view to the next.
- [UIViewAnimationOptionTransitionFlipFromTop](animationoptions/transitionflipfromtop.md) — A transition that flips a view around its horizontal axis from top to bottom (the top side of the view moves toward the front and the bottom side toward the back).
- [UIViewAnimationOptionTransitionFlipFromBottom](animationoptions/transitionflipfrombottom.md) — A transition that flips a view around its horizontal axis from bottom to top (the bottom side of the view moves toward the front and the top side toward the back).
- [UIViewAnimationOptionPreferredFramesPerSecond30](animationoptions/preferredframespersecond30.md) — A frame rate of 30 frames per second.
- [UIViewAnimationOptionPreferredFramesPerSecond60](animationoptions/preferredframespersecond60.md) — A frame rate of 60 frames per second.

### Initializers

- [init(rawValue:)](<animationoptions/init(rawvalue_).md>) — Creates an animation options structure with the specified raw value.

### Type Properties

- [UIViewAnimationOptionFlushUpdates](animationoptions/flushupdates.md) — Flush all pending updates (including traits, properties, and layout) whenever the animation context changes. This includes flushing updates:

## See Also

### Constants

- [AnimationCurve](animationcurve.md) — Specifies the supported animation curves.
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
