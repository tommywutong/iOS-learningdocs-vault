---
title: showHideTransitionViews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/animationoptions/showhidetransitionviews
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animationoptions/showhidetransitionviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animationoptions/showhidetransitionviews.json'
content_hash: 'sha256:c18ee18b26664125'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [AnimationOptions](../animationoptions.md)

# showHideTransitionViews

<sub>Type Property</sub>

Hide or show views during a view transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var showHideTransitionViews: UIView.AnimationOptions { get }
```

## Discussion

When present, this key causes views to be hidden or shown (instead of removed or added) when performing a view transition. Both views must already be present in the parent view’s hierarchy when using this key. If this key is not present, the to-view in a transition is added to, and the from-view is removed from, the parent view’s list of subviews.

## See Also

### Constants

- [UIViewAnimationOptionLayoutSubviews](layoutsubviews.md) — Lay out subviews at commit time so that they are animated along with their parent.
- [UIViewAnimationOptionAllowUserInteraction](allowuserinteraction.md) — Allow the user to interact with views while they are being animated.
- [UIViewAnimationOptionBeginFromCurrentState](beginfromcurrentstate.md) — Start the animation from the current setting associated with an already in-flight animation.
- [UIViewAnimationOptionRepeat](repeat.md) — Repeat the animation indefinitely.
- [UIViewAnimationOptionAutoreverse](autoreverse.md) — Run the animation backwards and forwards (must be combined with the repeat option).
- [UIViewAnimationOptionOverrideInheritedDuration](overrideinheritedduration.md) — Force the animation to use the original duration value specified when the animation was submitted.
- [UIViewAnimationOptionOverrideInheritedCurve](overrideinheritedcurve.md) — Force the animation to use the original curve value specified when the animation was submitted.
- [UIViewAnimationOptionAllowAnimatedContent](allowanimatedcontent.md) — Animate the views by changing the property values dynamically and redrawing the view.
- [UIViewAnimationOptionOverrideInheritedOptions](overrideinheritedoptions.md) — The option to not inherit the animation type or any options.
- [UIViewAnimationOptionCurveEaseInOut](curveeaseinout.md) — Specify an ease-in ease-out curve, which causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [UIViewAnimationOptionCurveEaseIn](curveeasein.md) — An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [UIViewAnimationOptionCurveEaseOut](curveeaseout.md) — An ease-out curve causes the animation to begin quickly, and then slow as it completes.
- [UIViewAnimationOptionCurveLinear](curvelinear.md) — A linear animation curve causes an animation to occur evenly over its duration.
- [UIViewAnimationOptionTransitionFlipFromLeft](transitionflipfromleft.md) — A transition that flips a view around its vertical axis from left to right (the left side of the view moves toward the front and right side toward the back).
- [UIViewAnimationOptionTransitionFlipFromRight](transitionflipfromright.md) — A transition that flips a view around its vertical axis from right to left (the right side of the view moves toward the front and left side toward the back).
