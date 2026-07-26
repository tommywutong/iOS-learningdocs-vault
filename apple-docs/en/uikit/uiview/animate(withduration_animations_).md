---
title: 'animate(withDuration:animations:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/animate(withduration:animations:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animate(withduration:animations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animate%28withduration%3Aanimations%3A%29.json'
content_hash: 'sha256:2f3e7ec493a2bad2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# animate(withDuration:animations:)

<sub>Type Method</sub>

Animate changes to one or more views using the specified duration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func animate(withDuration duration: TimeInterval, animations: @escaping () -> Void)
```

## Parameters

- `duration` — The total duration of the animations, measured in seconds. If you specify a negative value or `0`, the changes are made without animating them.

- `animations` — A block object containing the changes to commit to the views. This is where you programmatically change any animatable properties of the views in your view hierarchy. This block takes no parameters and has no return value. This parameter must not be `NULL`.

## Discussion

This method performs the specified animations immediately using the [UIViewAnimationOptionCurveEaseInOut](animationoptions/curveeaseinout.md) and [UIViewAnimationOptionTransitionNone](../uiviewanimationoptions/uiviewanimationoptiontransitionnone.md) animation options.

During an animation, user interactions are temporarily disabled for the views being animated. (Prior to iOS 5, user interactions are disabled for the entire application.)

## See Also

### Animating views

- [animate(_:changes:completion:)](<animate(__changes_completion_).md>)
- [animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)](<animate(springduration_bounce_initialspringvelocity_delay_options_animations_completion_).md>) — Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) — Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [+ animateWithDuration:animations:completion:](<animate(withduration_animations_completion_).md>) — Animate changes to one or more views using the specified duration and completion handler.
- [+ transitionWithView:duration:options:animations:completion:](<transition(with_duration_options_animations_completion_).md>) — Creates a transition animation for the specified container view.
- [+ transitionFromView:toView:duration:options:completion:](<transition(from_to_duration_options_completion_).md>) — Creates a transition animation between the specified views using the given parameters.
- [+ animateKeyframesWithDuration:delay:options:animations:completion:](<animatekeyframes(withduration_delay_options_animations_completion_).md>) — Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [+ addKeyframeWithRelativeStartTime:relativeDuration:animations:](<addkeyframe(withrelativestarttime_relativeduration_animations_).md>) — Specifies the timing and animation values for a single frame of a keyframe animation.
- [+ performSystemAnimation:onViews:options:animations:completion:](<perform(__on_options_animations_completion_).md>) — Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [+ animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:](<animate(withduration_delay_usingspringwithdamping_initialspringvelocity_options_animations_completion_).md>) — Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [+ performWithoutAnimation:](<performwithoutanimation(__).md>) — Disables a view transition animation.
- [+ modifyAnimationsWithRepeatCount:autoreverses:animations:](<modifyanimations(withrepeatcount_autoreverses_animations_).md>) — Repeats the specified animations a specific number of times, optionally running the animation forward and backward.
