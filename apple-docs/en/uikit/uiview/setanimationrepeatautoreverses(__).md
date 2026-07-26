---
title: 'setAnimationRepeatAutoreverses(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/setanimationrepeatautoreverses(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationrepeatautoreverses(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationrepeatautoreverses%28_%3A%29.json'
content_hash: 'sha256:abcf473660214481'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationRepeatAutoreverses(_:)

<sub>Type Method</sub>

Sets whether the animations within an animation block automatically reverse themselves.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)
```

## Parameters

- `repeatAutoreverses` — Specify [true](../../swift/true.md) to enable autoreversing or [false](../../swift/false.md) to disable it.

## Discussion

If you enable autoreversing, a single animation cycle changes the properties being animated to their new values and then back to their original values. At the end of the animations, the affected views are then updated immediately to reflect the new values. This method does nothing if called from outside of an animation block. By default, autoreversing is disabled.

If you combine autoreversing with a repeat count (settable using the [+ setAnimationRepeatCount:](<setanimationrepeatcount(__).md>) method), you can create animations that shift back and forth between the old and new values the specified number of times. However, remember that the repeat count indicates the number of complete cycles. If you specify an integral value such as `2.0`, the animation ends on the old value, which is followed by the view immediately updating itself to show the new value, which might be jarring. If you want the animation to end on the new value (instead of the old value), add `0.5` to the repeat count value. This adds an extra half cycle to the animation.

Use of this method is discouraged in iOS 4.0 and later. Instead, you should use the[+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) method to specify your animations and the animation options.

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
- [+ setAnimationBeginsFromCurrentState:](<setanimationbeginsfromcurrentstate(__).md>) — Sets whether the animation should begin playing from the current state. _(deprecated)_
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
