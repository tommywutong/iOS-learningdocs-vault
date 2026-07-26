---
title: 'setAnimationDelegate(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/setanimationdelegate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationdelegate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationdelegate%28_%3A%29.json'
content_hash: 'sha256:31187bbb65d754d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationDelegate(_:)

<sub>Type Method</sub>

Sets the delegate for any animation messages.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func setAnimationDelegate(_ delegate: Any?)
```

## Parameters

- `delegate` — An object that defines the methods registered using the [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) and [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) methods.  The view maintains a strong reference to this object for the duration of the animation.

## Discussion

You can specify an animation delegate in cases where you want to receive messages when the animation starts or stops. After calling this method, you should call the [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) and [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) methods as needed to register appropriate selectors. By default, the animation delegate is set to `nil`.

You primarily use this method to set the delegate for animation blocks created using the begin/commit animation methods. Calling this method from outside an animation block does nothing.

Use of this method is discouraged in iOS 4.0 and later. If you are using the block-based animation methods, you can include your delegate’s start and end code directly inside your block.

## See Also

### Deprecated methods

- [+ beginAnimations:context:](<beginanimations(__context_).md>) — Marks the beginning of a begin/commit animation block. _(deprecated)_
- [+ commitAnimations](<commitanimations().md>) — Marks the end of a begin/commit animation block and schedules the animations for execution. _(deprecated)_
- [+ setAnimationStartDate:](<setanimationstart(__).md>) — Sets the start time for the current animation block. _(deprecated)_
- [+ setAnimationsEnabled:](<setanimationsenabled(__).md>) — Sets whether animations are enabled.
- [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) — Sets the message to send to the animation delegate when the animation starts. _(deprecated)_
- [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) — Sets the message to send to the animation delegate when animation stops. _(deprecated)_
- [+ setAnimationDuration:](<setanimationduration(__).md>) — Sets the duration (measured in seconds) of the animations in an animation block. _(deprecated)_
- [+ setAnimationDelay:](<setanimationdelay(__).md>) — Sets the amount of time (in seconds) to wait before animating property changes within an animation block. _(deprecated)_
- [+ setAnimationCurve:](<setanimationcurve(__).md>) — Sets the curve to use when animating property changes within an animation block. _(deprecated)_
- [+ setAnimationRepeatCount:](<setanimationrepeatcount(__).md>) — Sets the number of times animations within an animation block repeat. _(deprecated)_
- [+ setAnimationRepeatAutoreverses:](<setanimationrepeatautoreverses(__).md>) — Sets whether the animations within an animation block automatically reverse themselves. _(deprecated)_
- [+ setAnimationBeginsFromCurrentState:](<setanimationbeginsfromcurrentstate(__).md>) — Sets whether the animation should begin playing from the current state. _(deprecated)_
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
