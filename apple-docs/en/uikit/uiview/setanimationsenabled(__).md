---
title: 'setAnimationsEnabled(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/setanimationsenabled(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setanimationsenabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setanimationsenabled%28_%3A%29.json'
content_hash: 'sha256:564173491d889867'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setAnimationsEnabled(_:)

<sub>Type Method</sub>

Sets whether animations are enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func setAnimationsEnabled(_ enabled: Bool)
```

## Parameters

- `enabled` — Specify [true](../../swift/true.md) to enable animations or [false](../../swift/false.md) to disable them.

## Discussion

Animations are enabled by default. If you disable animations, code inside subsequent animation blocks is still executed but no animations actually occur. Thus, any changes you make inside an animation block are reflected immediately instead of being animated. This is true whether you use the block-based animation methods or the begin/commit animation methods.

This method affects only those animations that are submitted after it is called. If you call this method while existing animations are running, those animations continue running until they reach their natural end point.

## See Also

### Related Documentation

- [+ performWithoutAnimation:](<performwithoutanimation(__).md>) — Disables a view transition animation.

### Deprecated methods

- [+ beginAnimations:context:](<beginanimations(__context_).md>) — Marks the beginning of a begin/commit animation block. _(deprecated)_
- [+ commitAnimations](<commitanimations().md>) — Marks the end of a begin/commit animation block and schedules the animations for execution. _(deprecated)_
- [+ setAnimationStartDate:](<setanimationstart(__).md>) — Sets the start time for the current animation block. _(deprecated)_
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
