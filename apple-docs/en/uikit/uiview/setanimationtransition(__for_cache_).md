---
title: 'setAnimationTransition(_:for:cache:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/setanimationtransition(_:for:cache:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationtransition(_:for:cache:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationtransition%28_%3Afor%3Acache%3A%29.json'
content_hash: 'sha256:443e4f220c675443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationTransition(_:for:cache:)

<sub>Type Method</sub>

Sets a transition to apply to a view during an animation block.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func setAnimationTransition(_ transition: UIView.AnimationTransition, for view: UIView, cache: Bool)
```

## Parameters

- `transition` — A transition to apply to `view`. Possible values are described in [AnimationTransition](animationtransition.md).

- `view` — The view to apply the transition to.

- `cache` — If [true](../../swift/true.md), the before and after images of `view` are rendered once and used to create the frames in the animation. Caching can improve performance but if you set this parameter to [true](../../swift/true.md), you must not update the view or its subviews during the transition. Updating the view and its subviews may interfere with the caching behaviors and cause the view contents to be rendered incorrectly (or in the wrong location) during the animation. You must wait until the transition ends to update the view. If [false](../../swift/false.md), the view and its contents must be updated for each frame of the transition animation, which may noticeably affect the frame rate.

## Discussion

If you want to change the appearance of a view during a transition—for example, flip from one view to another—then use a container view, an instance of [UIView](../uiview.md), as follows:

1. Begin an animation block.
2. Set the transition on the container view.
3. Remove the subview from the container view.
4. Add the new subview to the container view.
5. Commit the animation block.

Use of this method is discouraged in iOS 4.0 and later. You should use the [+ transitionWithView:duration:options:animations:completion:](<transition(with_duration_options_animations_completion_).md>) method to perform transitions instead.

## See Also

### Deprecated methods

- [+ beginAnimations:context:](<beginanimations(__context_).md>) — Marks the beginning of a begin/commit animation block. _(deprecated)_
- [+ commitAnimations](<commitanimations().md>) — Marks the end of a begin/commit animation block and schedules the animations for execution. _(deprecated)_
- [+ setAnimationStartDate:](<setanimationstart(__).md>) — Sets the start time for the current animation block. _(deprecated)_
- [+ setAnimationsEnabled:](<setanimationsenabled(__).md>) — Sets whether animations are enabled.
- [+ setAnimationDelegate:](<setanimationdelegate(__).md>) — Sets the delegate for any animation messages. _(deprecated)_
- [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) — Sets the message to send to the animation delegate when the animation starts. _(deprecated)_
- [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) — Sets the message to send to the animation delegate when animation stops. _(deprecated)_
- [+ setAnimationDuration:](<setanimationduration(__).md>) — Sets the duration (measured in seconds) of the animations in an animation block. _(deprecated)_
- [+ setAnimationDelay:](<setanimationdelay(__).md>) — Sets the amount of time (in seconds) to wait before animating property changes within an animation block. _(deprecated)_
- [+ setAnimationCurve:](<setanimationcurve(__).md>) — Sets the curve to use when animating property changes within an animation block. _(deprecated)_
- [+ setAnimationRepeatCount:](<setanimationrepeatcount(__).md>) — Sets the number of times animations within an animation block repeat. _(deprecated)_
- [+ setAnimationRepeatAutoreverses:](<setanimationrepeatautoreverses(__).md>) — Sets whether the animations within an animation block automatically reverse themselves. _(deprecated)_
- [+ setAnimationBeginsFromCurrentState:](<setanimationbeginsfromcurrentstate(__).md>) — Sets whether the animation should begin playing from the current state. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
