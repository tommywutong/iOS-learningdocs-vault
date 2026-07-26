---
title: areAnimationsEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/areanimationsenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiview/areanimationsenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/areanimationsenabled.json'
content_hash: 'sha256:6ebcd58c47ec5968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# areAnimationsEnabled

<sub>Type Property</sub>

Returns a Boolean value indicating whether animations are enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var areAnimationsEnabled: Bool { get }
```

## Return Value

[true](../../swift/true.md) if animations are enabled; otherwise, [false](../../swift/false.md).

## Discussion

The value of this property is [true](../../swift/true.md) if animations are enabled; otherwise, it is [false](../../swift/false.md).

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
- [+ setAnimationTransition:forView:cache:](<setanimationtransition(__for_cache_).md>) — Sets a transition to apply to a view during an animation block. _(deprecated)_
- [- viewForBaselineLayout](<forbaselinelayout().md>) — Returns a view used to satisfy baseline constraints. _(deprecated)_
