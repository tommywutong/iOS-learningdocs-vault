---
title: 'transition(with:duration:options:animations:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/transition(with:duration:options:animations:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/transition(with:duration:options:animations:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/transition%28with%3Aduration%3Aoptions%3Aanimations%3Acompletion%3A%29.json'
content_hash: 'sha256:d4814818cb5c60e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# transition(with:duration:options:animations:completion:)

<sub>Type Method</sub>

Creates a transition animation for the specified container view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func transition(with view: UIView, duration: TimeInterval, options: UIView.AnimationOptions = [], animations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

## Parameters

- `view` — The container view that performs the transition.

- `duration` — The duration of the transition animation, measured in seconds. If you specify a negative value or `0`, the transition is made without animations.

- `options` — A mask of options indicating how you want to perform the animations. For a list of valid constants, see [AnimationOptions](animationoptions.md).

- `animations` — A block object that contains the changes you want to make to the specified view. This block takes no parameters and has no return value. This parameter must not be `NULL`.

- `completion` — A block object to be executed when the animation sequence ends. This block has no return value and takes a single Boolean argument that indicates whether or not the animations actually finished before the completion handler was called. If the duration of the animation is 0, this block is performed at the beginning of the next run loop cycle. This parameter may be `NULL`.

## Discussion

This method applies a transition to the specified view so that you can make state changes to it. The block you specify in the `animations` parameter contains whatever state changes you want to make. You can use this block to add, remove, show, or hide subviews of the specified view. If you want to incorporate other animatable changes, you must include the [UIViewAnimationOptionAllowAnimatedContent](animationoptions/allowanimatedcontent.md) key in the `options` parameter.

The following code creates a flip transition for the specified container view. At the appropriate point in the transition, one subview is removed and another is added to the container view. This makes it look as if a new view was flipped into place with the new subview, but really it is just the same view animated back into place with a new configuration.

```objc
[UIView transitionWithView:containerView
           duration:0.2
           options:UIViewAnimationOptionTransitionFlipFromLeft
           animations:^{ [fromView removeFromSuperview]; [containerView addSubview:toView]; }
           completion:NULL];
```

During an animation, user interactions are temporarily disabled for the views being animated. (Prior to iOS 5, user interactions are disabled for the entire application.) If you want users to be able to interact with the views, include the [UIViewAnimationOptionAllowUserInteraction](animationoptions/allowuserinteraction.md) constant in the `options` parameter.

## See Also

### Animating views

- [animate(_:changes:completion:)](<animate(__changes_completion_).md>)
- [animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)](<animate(springduration_bounce_initialspringvelocity_delay_options_animations_completion_).md>) — Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) — Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [+ animateWithDuration:animations:completion:](<animate(withduration_animations_completion_).md>) — Animate changes to one or more views using the specified duration and completion handler.
- [+ animateWithDuration:animations:](<animate(withduration_animations_).md>) — Animate changes to one or more views using the specified duration.
- [+ transitionFromView:toView:duration:options:completion:](<transition(from_to_duration_options_completion_).md>) — Creates a transition animation between the specified views using the given parameters.
- [+ animateKeyframesWithDuration:delay:options:animations:completion:](<animatekeyframes(withduration_delay_options_animations_completion_).md>) — Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [+ addKeyframeWithRelativeStartTime:relativeDuration:animations:](<addkeyframe(withrelativestarttime_relativeduration_animations_).md>) — Specifies the timing and animation values for a single frame of a keyframe animation.
- [+ performSystemAnimation:onViews:options:animations:completion:](<perform(__on_options_animations_completion_).md>) — Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [+ animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:](<animate(withduration_delay_usingspringwithdamping_initialspringvelocity_options_animations_completion_).md>) — Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [+ performWithoutAnimation:](<performwithoutanimation(__).md>) — Disables a view transition animation.
- [+ modifyAnimationsWithRepeatCount:autoreverses:animations:](<modifyanimations(withrepeatcount_autoreverses_animations_).md>) — Repeats the specified animations a specific number of times, optionally running the animation forward and backward.
