---
title: UIViewAnimationOptionPreferredFramesPerSecondDefault
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimationoptions/uiviewanimationoptionpreferredframesperseconddefault
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionpreferredframesperseconddefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionpreferredframesperseconddefault.json'
content_hash: 'sha256:f934de7b3c1e5eb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [AnimationOptions](../uiview/animationoptions.md)

# UIViewAnimationOptionPreferredFramesPerSecondDefault

<sub>Enumeration Case</sub>

The default number of frames per second.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UIViewAnimationOptionPreferredFramesPerSecondDefault
```

## Discussion

It’s recommended that you use the default value unless you have identified a specific need for an explicit rate.

## See Also

### Constants

- [UIViewAnimationOptionLayoutSubviews](../uiview/animationoptions/layoutsubviews.md) — Lay out subviews at commit time so that they are animated along with their parent.
- [UIViewAnimationOptionAllowUserInteraction](../uiview/animationoptions/allowuserinteraction.md) — Allow the user to interact with views while they are being animated.
- [UIViewAnimationOptionBeginFromCurrentState](../uiview/animationoptions/beginfromcurrentstate.md) — Start the animation from the current setting associated with an already in-flight animation.
- [UIViewAnimationOptionRepeat](../uiview/animationoptions/repeat.md) — Repeat the animation indefinitely.
- [UIViewAnimationOptionAutoreverse](../uiview/animationoptions/autoreverse.md) — Run the animation backwards and forwards (must be combined with the repeat option).
- [UIViewAnimationOptionOverrideInheritedDuration](../uiview/animationoptions/overrideinheritedduration.md) — Force the animation to use the original duration value specified when the animation was submitted.
- [UIViewAnimationOptionOverrideInheritedCurve](../uiview/animationoptions/overrideinheritedcurve.md) — Force the animation to use the original curve value specified when the animation was submitted.
- [UIViewAnimationOptionAllowAnimatedContent](../uiview/animationoptions/allowanimatedcontent.md) — Animate the views by changing the property values dynamically and redrawing the view.
- [UIViewAnimationOptionShowHideTransitionViews](../uiview/animationoptions/showhidetransitionviews.md) — Hide or show views during a view transition.
- [UIViewAnimationOptionOverrideInheritedOptions](../uiview/animationoptions/overrideinheritedoptions.md) — The option to not inherit the animation type or any options.
- [UIViewAnimationOptionCurveEaseInOut](../uiview/animationoptions/curveeaseinout.md) — Specify an ease-in ease-out curve, which causes the animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [UIViewAnimationOptionCurveEaseIn](../uiview/animationoptions/curveeasein.md) — An ease-in curve causes the animation to begin slowly, and then speed up as it progresses.
- [UIViewAnimationOptionCurveEaseOut](../uiview/animationoptions/curveeaseout.md) — An ease-out curve causes the animation to begin quickly, and then slow as it completes.
- [UIViewAnimationOptionCurveLinear](../uiview/animationoptions/curvelinear.md) — A linear animation curve causes an animation to occur evenly over its duration.
- [UIViewAnimationOptionTransitionNone](uiviewanimationoptiontransitionnone.md) — No transition is specified.
