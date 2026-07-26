---
title: 'init(duration:dampingRatio:animations:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/init(duration:dampingratio:animations:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:dampingratio:animations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/init%28duration%3Adampingratio%3Aanimations%3A%29.json'
content_hash: 'sha256:393661e54d539976'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# init(duration:dampingRatio:animations:)

<sub>Initializer</sub>

Initializes the animator object with spring-based timing information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(duration: TimeInterval, dampingRatio ratio: CGFloat, animations: (() -> Void)? = nil)
```

## Parameters

- `duration` — The duration of the animation, in seconds.

- `ratio` — The damping ratio to apply to the initial acceleration and oscillation. To smoothly decelerate the animation without oscillation, specify a value of `1`. Specify values closer to `0` to create less damping and more oscillation.

- `animations` — The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable view properties. When you start the animations, those properties are animated from their current values to the new values using the specified animation parameters.

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

Spring-based animations cause the value of a property to accelerate initially toward its new value and then oscillate around that value until before finally coming to rest on the value. The initial amount of acceleration is proportional to the difference between the start and end values of the property. In other words, the greater the difference between the start and end values, the greater the initial acceleration. The `ratio` parameter determines the amount of damping applied to the initial acceleration. Lower damping values correspond to less resistance to the acceleration and more oscillation before coming to rest. Higher damping values correspond to more resistance and less oscillation.

The animator object returned by this method begins in the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [- startAnimation](<../uiviewanimating/startanimation().md>) method.

## See Also

### Initializing a property animator

- [- initWithDuration:curve:animations:](<init(duration_curve_animations_).md>) — Initializes the animator with a built-in UIKit timing curve.
- [- initWithDuration:controlPoint1:controlPoint2:animations:](<init(duration_controlpoint1_controlpoint2_animations_).md>) — Initializes the animator object with a cubic Bézier timing curve.
- [- initWithDuration:timingParameters:](<init(duration_timingparameters_).md>) — Initializes the animator object with a custom timing curve object.
- [+ runningPropertyAnimatorWithDuration:delay:options:animations:completion:](<runningpropertyanimator(withduration_delay_options_animations_completion_).md>) — Creates and returns an animator object that begins running its animations immediately.
