---
title: 'modifyAnimations(withRepeatCount:autoreverses:animations:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/modifyanimations(withrepeatcount:autoreverses:animations:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/modifyanimations(withrepeatcount:autoreverses:animations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/modifyanimations%28withrepeatcount%3Aautoreverses%3Aanimations%3A%29.json'
content_hash: 'sha256:c21b35936b2c2e5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# modifyAnimations(withRepeatCount:autoreverses:animations:)

<sub>Type Method</sub>

Repeats the specified animations a specific number of times, optionally running the animation forward and backward.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func modifyAnimations(withRepeatCount count: CGFloat, autoreverses: Bool, animations: () -> Void)
```

## Parameters

- `count` — The number of times to repeat the animations.

- `autoreverses` — A Boolean value that indicates whether the animations run forward and backward.

- `animations` — The animations to perform.

## Discussion

You must call this method from within an enclosing animation block. The inverse nesting, calling [+ animateWithDuration:animations:](<animate(withduration_animations_).md>) from inside the [+ modifyAnimationsWithRepeatCount:autoreverses:animations:](<modifyanimations(withrepeatcount_autoreverses_animations_).md>) block, doesn’t work.

```swift
UIView.animate(withDuration: 1.0) {
    UIView.modifyAnimations(withRepeatCount: 2, autoreverses: true) {
        // Set view properties.
    }
}
```

## See Also

### Animating views

- [animate(_:changes:completion:)](<animate(__changes_completion_).md>)
- [animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)](<animate(springduration_bounce_initialspringvelocity_delay_options_animations_completion_).md>) — Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) — Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [+ animateWithDuration:animations:completion:](<animate(withduration_animations_completion_).md>) — Animate changes to one or more views using the specified duration and completion handler.
- [+ animateWithDuration:animations:](<animate(withduration_animations_).md>) — Animate changes to one or more views using the specified duration.
- [+ transitionWithView:duration:options:animations:completion:](<transition(with_duration_options_animations_completion_).md>) — Creates a transition animation for the specified container view.
- [+ transitionFromView:toView:duration:options:completion:](<transition(from_to_duration_options_completion_).md>) — Creates a transition animation between the specified views using the given parameters.
- [+ animateKeyframesWithDuration:delay:options:animations:completion:](<animatekeyframes(withduration_delay_options_animations_completion_).md>) — Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [+ addKeyframeWithRelativeStartTime:relativeDuration:animations:](<addkeyframe(withrelativestarttime_relativeduration_animations_).md>) — Specifies the timing and animation values for a single frame of a keyframe animation.
- [+ performSystemAnimation:onViews:options:animations:completion:](<perform(__on_options_animations_completion_).md>) — Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [+ animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:](<animate(withduration_delay_usingspringwithdamping_initialspringvelocity_options_animations_completion_).md>) — Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [+ performWithoutAnimation:](<performwithoutanimation(__).md>) — Disables a view transition animation.
