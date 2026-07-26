---
title: 'init(duration:curve:animations:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/init(duration:curve:animations:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:curve:animations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/init%28duration%3Acurve%3Aanimations%3A%29.json'
content_hash: 'sha256:e6eb42a5a5cca381'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# init(duration:curve:animations:)

<sub>Initializer</sub>

Initializes the animator with a built-in UIKit timing curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(duration: TimeInterval, curve: UIView.AnimationCurve, animations: (() -> Void)? = nil)
```

## Parameters

- `duration` — The duration of the animation, in seconds.

- `curve` — The UIKit timing curve to apply to the animation.

- `animations` — The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable view properties. When you start the animations, those properties are animated from their current values to the new values using the specified animation parameters.

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

Use this method to create an animator object that uses the existing UIKit timing curves to control the animation behavior. Standard UIKit timing curves include [UIViewAnimationCurveLinear](../uiview/animationcurve/linear.md) and [UIViewAnimationCurveEaseInOut](../uiview/animationcurve/easeinout.md) among others.

The animator object returned by this method begins in the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [- startAnimation](<../uiviewanimating/startanimation().md>) method.

## See Also

### Initializing a property animator

- [- initWithDuration:controlPoint1:controlPoint2:animations:](<init(duration_controlpoint1_controlpoint2_animations_).md>) — Initializes the animator object with a cubic Bézier timing curve.
- [- initWithDuration:dampingRatio:animations:](<init(duration_dampingratio_animations_).md>) — Initializes the animator object with spring-based timing information.
- [- initWithDuration:timingParameters:](<init(duration_timingparameters_).md>) — Initializes the animator object with a custom timing curve object.
- [+ runningPropertyAnimatorWithDuration:delay:options:animations:completion:](<runningpropertyanimator(withduration_delay_options_animations_completion_).md>) — Creates and returns an animator object that begins running its animations immediately.
