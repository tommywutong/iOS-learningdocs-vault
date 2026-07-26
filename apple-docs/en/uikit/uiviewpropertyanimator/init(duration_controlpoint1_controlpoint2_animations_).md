---
title: 'init(duration:controlPoint1:controlPoint2:animations:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/init(duration:controlpoint1:controlpoint2:animations:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:controlpoint1:controlpoint2:animations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/init%28duration%3Acontrolpoint1%3Acontrolpoint2%3Aanimations%3A%29.json'
content_hash: 'sha256:2ca1eb44f184e7e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# init(duration:controlPoint1:controlPoint2:animations:)

<sub>Initializer</sub>

Initializes the animator object with a cubic Bézier timing curve.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(duration: TimeInterval, controlPoint1 point1: CGPoint, controlPoint2 point2: CGPoint, animations: (() -> Void)? = nil)
```

## Parameters

- `duration` — The duration of the animation, in seconds.

- `point1` — The first control point for the cubic Bézier timing curve.

- `point2` — The second control point for the cubic Bézier timing curve.

- `animations` — The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable view properties. When you start the animations, those properties are animated from their current values to the new values using the specified animation parameters.

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

Use this method to create an animator object using a cubic timing curve whose starting point is (0, 0) and whose end point is (1, 1). The `point1` and `point2` parameters are the control points that define the shape of the resulting Bezier curve. The slope of the curve defines the speed of the animation at different times. Steep slopes cause animations to appear to run faster and shallower slopes cause them to appear to run slower. The following image shows a timing curve where the animations start fast and finish fast but run more slowly through the middle section.

![](../../../../attachments/0054ab7fbcfb5dc1810282e7c7d2a202/media-1965739@2x.png)

The animator object returned by this method begins in the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [- startAnimation](<../uiviewanimating/startanimation().md>) method.

## See Also

### Initializing a property animator

- [- initWithDuration:curve:animations:](<init(duration_curve_animations_).md>) — Initializes the animator with a built-in UIKit timing curve.
- [- initWithDuration:dampingRatio:animations:](<init(duration_dampingratio_animations_).md>) — Initializes the animator object with spring-based timing information.
- [- initWithDuration:timingParameters:](<init(duration_timingparameters_).md>) — Initializes the animator object with a custom timing curve object.
- [+ runningPropertyAnimatorWithDuration:delay:options:animations:completion:](<runningpropertyanimator(withduration_delay_options_animations_completion_).md>) — Creates and returns an animator object that begins running its animations immediately.
