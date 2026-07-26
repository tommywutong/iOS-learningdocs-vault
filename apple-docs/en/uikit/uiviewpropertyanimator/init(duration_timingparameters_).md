---
title: 'init(duration:timingParameters:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/init(duration:timingparameters:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/init(duration:timingparameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/init%28duration%3Atimingparameters%3A%29.json'
content_hash: 'sha256:49708731576e9d7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# init(duration:timingParameters:)

<sub>Initializer</sub>

Initializes the animator object with a custom timing curve object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(duration: TimeInterval, timingParameters parameters: any UITimingCurveProvider)
```

## Parameters

- `duration` — The duration of the animation, in seconds.

- `parameters` — The object providing the timing information. This object must adopt the [UITimingCurveProvider](../uitimingcurveprovider.md) protocol.

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

Use this method to initialize the animator with a custom timing curve. After initializing the animator, you must add one or more animation blocks before calling starting the animations.

The animator object returned by this method begins in the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state. You must explicitly start the animations by calling the [- startAnimation](<../uiviewanimating/startanimation().md>) method.

## See Also

### Initializing a property animator

- [- initWithDuration:curve:animations:](<init(duration_curve_animations_).md>) — Initializes the animator with a built-in UIKit timing curve.
- [- initWithDuration:controlPoint1:controlPoint2:animations:](<init(duration_controlpoint1_controlpoint2_animations_).md>) — Initializes the animator object with a cubic Bézier timing curve.
- [- initWithDuration:dampingRatio:animations:](<init(duration_dampingratio_animations_).md>) — Initializes the animator object with spring-based timing information.
- [+ runningPropertyAnimatorWithDuration:delay:options:animations:completion:](<runningpropertyanimator(withduration_delay_options_animations_completion_).md>) — Creates and returns an animator object that begins running its animations immediately.
