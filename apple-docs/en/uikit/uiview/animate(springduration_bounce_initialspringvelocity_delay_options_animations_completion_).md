---
title: 'animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/animate(springduration:bounce:initialspringvelocity:delay:options:animations:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animate(springduration:bounce:initialspringvelocity:delay:options:animations:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animate%28springduration%3Abounce%3Ainitialspringvelocity%3Adelay%3Aoptions%3Aanimations%3Acompletion%3A%29.json'
content_hash: 'sha256:a0de8cdb7cbb3d07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)

<sub>Type Method</sub>

Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency class func animate(springDuration duration: TimeInterval = 0.5, bounce: CGFloat = 0.0, initialSpringVelocity: CGFloat = 0.0, delay: TimeInterval = 0.0, options: UIView.AnimationOptions = [], animations: () -> Void, completion: ((Bool) -> Void)? = nil)
```

## Discussion

> [!note] Related sessions from WWDC23
> Session 10055: [What’s new in UIKit](https://developer.apple.com/videos/play/wwdc2023/10055/)

## See Also

### Animating views

- [animate(_:changes:completion:)](<animate(__changes_completion_).md>)
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
- [+ modifyAnimationsWithRepeatCount:autoreverses:animations:](<modifyanimations(withrepeatcount_autoreverses_animations_).md>) — Repeats the specified animations a specific number of times, optionally running the animation forward and backward.
