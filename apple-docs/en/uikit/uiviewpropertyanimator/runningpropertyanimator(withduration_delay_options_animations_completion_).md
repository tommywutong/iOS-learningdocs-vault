---
title: 'runningPropertyAnimator(withDuration:delay:options:animations:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/runningpropertyanimator(withduration:delay:options:animations:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/runningpropertyanimator(withduration:delay:options:animations:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/runningpropertyanimator%28withduration%3Adelay%3Aoptions%3Aanimations%3Acompletion%3A%29.json'
content_hash: 'sha256:751d336d1b4b323e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# runningPropertyAnimator(withDuration:delay:options:animations:completion:)

<sub>Type Method</sub>

Creates and returns an animator object that begins running its animations immediately.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func runningPropertyAnimator(withDuration duration: TimeInterval, delay: TimeInterval, options: UIView.AnimationOptions = [], animations: @escaping () -> Void, completion: ((UIViewAnimatingPosition) -> Void)? = nil) -> Self
```

## Parameters

- `duration` — The duration of the animation, in seconds.

- `delay` — The number of seconds to wait before starting the animations. Specify 0 to begin the animations immediately.

- `options` — The options to apply to the animations. You can specify most options, but transition-related options and options related to the animation direction are ignored. For a list of options, see [AnimationOptions](../uiview/animationoptions.md).

- `animations` — The block containing the animations. This block has no return value and takes no parameters. Use this block to modify any animatable properties of your view. Those properties are animated from their current values to the new values using the specified animation parameters.

- `completion` — The block to execute when the animations finish. You can use this block to perform any final actions. This block has no return value and takes the following parameter: - **finalPosition** — The ending position of the animations. Use this value to determine whether the animations stopped at the beginning, end, or somewhere in the middle.

## Return Value

An initialized animator object or `nil` if the object could not be created.

## Discussion

This method creates the property animator object, configures it, and calls its [- startAnimation](<../uiviewanimating/startanimation().md>) method after the specified delay. If you don’t specify an animation curve in the options parameter, this method uses the [UIViewAnimationOptionCurveEaseInOut](../uiview/animationoptions/curveeaseinout.md) option.

## See Also

### Initializing a property animator

- [- initWithDuration:curve:animations:](<init(duration_curve_animations_).md>) — Initializes the animator with a built-in UIKit timing curve.
- [- initWithDuration:controlPoint1:controlPoint2:animations:](<init(duration_controlpoint1_controlpoint2_animations_).md>) — Initializes the animator object with a cubic Bézier timing curve.
- [- initWithDuration:dampingRatio:animations:](<init(duration_dampingratio_animations_).md>) — Initializes the animator object with spring-based timing information.
- [- initWithDuration:timingParameters:](<init(duration_timingparameters_).md>) — Initializes the animator object with a custom timing curve object.
