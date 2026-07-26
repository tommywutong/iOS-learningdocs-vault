---
title: 'beginAnimations(_:context:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/beginanimations(_:context:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/beginanimations(_:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/beginanimations%28_%3Acontext%3A%29.json'
content_hash: 'sha256:8cb1808446d35512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# beginAnimations(_:context:)

<sub>Type Method</sub>

Marks the beginning of a begin/commit animation block.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func beginAnimations(_ animationID: String?, context: UnsafeMutableRawPointer?)
```

## Parameters

- `animationID` — An application-supplied identifier for the animations.

- `context` — Custom data that you want to associate with this set of animations. information that is passed to the animation delegate messages—the selectors set using the [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) and [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) methods.

## Discussion

This method signals to the system that you want to specify one or more animations to perform. After calling this method, configure the animation options (using the `setAnimation…` class methods) and then change the desired animatable properties of your views. When you are done changing your view properties, call the [+ commitAnimations](<commitanimations().md>) method to close the set and schedule the animations.

You can nest sets of animations (by calling this method again before committing a previous set of animations) as needed. Nesting animations groups them together and allows you to set different animation options for the nested group.

If you install a start or stop selector using the [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) or [+ setAnimationDidStopSelector:](<setanimationdidstop(__).md>) method, the values you specify for the `animationID` and `context` parameters are passed to your selectors at runtime. You can use these parameters to pass additional information to those selectors.

Use of this method is discouraged in iOS 4.0 and later. You should use the block-based animation methods to specify your animations instead.

## See Also

### Deprecated methods

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
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
