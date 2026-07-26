---
title: 'animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/animatewithspringduration:bounce:initialspringvelocity:delay:options:animations:completion:'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/animatewithspringduration:bounce:initialspringvelocity:delay:options:animations:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/animatewithspringduration%3Abounce%3Ainitialspringvelocity%3Adelay%3Aoptions%3Aanimations%3Acompletion%3A.json'
content_hash: 'sha256:381783b9ed1b74a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:

<sub>Type Method</sub>

Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (void) animateWithSpringDuration:(NSTimeInterval) duration bounce:(CGFloat) bounce initialSpringVelocity:(CGFloat) velocity delay:(NSTimeInterval) delay options:(UIViewAnimationOptions) options animations:(void (^)()) animations completion:(void (^)(BOOL finished)) completion;
```

## See Also

### Animating views

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
