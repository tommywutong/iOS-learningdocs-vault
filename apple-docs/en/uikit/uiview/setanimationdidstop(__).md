---
title: 'setAnimationDidStop(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiview/setanimationdidstop(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationdidstop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationdidstop%28_%3A%29.json'
content_hash: 'sha256:1566b16ced35ac75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationDidStop(_:)

<sub>Type Method</sub>

Sets the message to send to the animation delegate when animation stops.

> [!warning] Deprecated
> Use [+ animateWithDuration:delay:options:animations:completion:](<animate(withduration_delay_options_animations_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func setAnimationDidStop(_ selector: Selector?)
```

## Parameters

- `selector` — The message sent to the animation delegate after animations end. The default value is `NULL`. The selector should be of the form: `- (void)animationDidStop:(NSString *)animationID finished:(NSNumber *)finished context:(void *)context`. Your method must take the following arguments: - `animationID` An [NSString](../../foundation/nsstring.md) containing an optional application-supplied identifier. This is the identifier that is passed to the [+ beginAnimations:context:](<beginanimations(__context_).md>) method. This argument can be `nil`. - `finished` An [NSNumber](../../foundation/nsnumber.md) object containing a Boolean value. The value is [true](../../swift/true.md) if the animation ran to completion before it stopped or [false](../../swift/false.md) if it did not. - `context` An optional application-supplied context. This is the context data passed to the [+ beginAnimations:context:](<beginanimations(__context_).md>) method. This argument can be `nil`.

## Discussion

If you specify an animation delegate for a begin/commit set of animations, you use this method to specify the selector to call after the animations end. This method does nothing if called from outside of an animation block. It must be called between calls to the [+ beginAnimations:context:](<beginanimations(__context_).md>) and [+ commitAnimations](<commitanimations().md>) methods. This selector is set to `NULL` by default.

> [!note] Note
> Your stop selector is still called even if animations are disabled.

Use of this method is discouraged in iOS 4.0 and later. If you are using the block-based animation methods, you can include your delegate’s end code directly inside your block.

## See Also

### Deprecated methods

- [+ beginAnimations:context:](<beginanimations(__context_).md>) — Marks the beginning of a begin/commit animation block. _(deprecated)_
- [+ commitAnimations](<commitanimations().md>) — Marks the end of a begin/commit animation block and schedules the animations for execution. _(deprecated)_
- [+ setAnimationStartDate:](<setanimationstart(__).md>) — Sets the start time for the current animation block. _(deprecated)_
- [+ setAnimationsEnabled:](<setanimationsenabled(__).md>) — Sets whether animations are enabled.
- [+ setAnimationDelegate:](<setanimationdelegate(__).md>) — Sets the delegate for any animation messages. _(deprecated)_
- [+ setAnimationWillStartSelector:](<setanimationwillstart(__).md>) — Sets the message to send to the animation delegate when the animation starts. _(deprecated)_
- [+ setAnimationDuration:](<setanimationduration(__).md>) — Sets the duration (measured in seconds) of the animations in an animation block. _(deprecated)_
- [+ setAnimationDelay:](<setanimationdelay(__).md>) — Sets the amount of time (in seconds) to wait before animating property changes within an animation block. _(deprecated)_
- [+ setAnimationCurve:](<setanimationcurve(__).md>) — Sets the curve to use when animating property changes within an animation block. _(deprecated)_
- [+ setAnimationRepeatCount:](<setanimationrepeatcount(__).md>) — Sets the number of times animations within an animation block repeat. _(deprecated)_
- [+ setAnimationRepeatAutoreverses:](<setanimationrepeatautoreverses(__).md>) — Sets whether the animations within an animation block automatically reverse themselves. _(deprecated)_
- [+ setAnimationBeginsFromCurrentState:](<setanimationbeginsfromcurrentstate(__).md>) — Sets whether the animation should begin playing from the current state. _(deprecated)_
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
