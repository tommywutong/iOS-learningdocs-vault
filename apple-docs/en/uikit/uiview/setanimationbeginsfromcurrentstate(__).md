---
title: 'setAnimationBeginsFromCurrentState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/setanimationbeginsfromcurrentstate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationbeginsfromcurrentstate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationbeginsfromcurrentstate%28_%3A%29.json'
content_hash: 'sha256:d47c771823cc70df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationBeginsFromCurrentState(_:)

<sub>Type Method</sub>

Sets whether the animation should begin playing from the current state.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)
```

## Parameters

- `fromCurrentState` — Specify [true](../../swift/true.md) if animations should begin from their currently visible state; otherwise, [false](../../swift/false.md).

## Discussion

If set to [true](../../swift/true.md) when an animation is in flight, the current view position of the in-flight animation is used as the starting state for the new animation. If set to [false](../../swift/false.md), the in-flight animation ends before the new animation begins using the last view position as the starting state. This method does nothing if an animation is not in flight or invoked outside of an animation block. Use the [+ beginAnimations:context:](<beginanimations(__context_).md>) class method to start and the [+ commitAnimations](<commitanimations().md>) class method to end an animation block. The default value is [false](../../swift/false.md).

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
- [+ setAnimationRepeatAutoreverses:](<setanimationrepeatautoreverses(__).md>) — Sets whether the animations within an animation block automatically reverse themselves. _(deprecated)_
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
