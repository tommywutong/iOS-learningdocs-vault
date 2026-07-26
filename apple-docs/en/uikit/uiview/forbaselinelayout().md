---
title: forBaselineLayout()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（9.0 起废弃）, iPadOS 6.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiview/forbaselinelayout()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/forbaselinelayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/forbaselinelayout%28%29.json'
content_hash: 'sha256:702abdefbf7b7b91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# forBaselineLayout()

<sub>Instance Method</sub>

Returns a view used to satisfy baseline constraints.

> [!warning] Deprecated
> Use the [viewForFirstBaselineLayout](forfirstbaselinelayout.md) or [viewForLastBaselineLayout](forlastbaselinelayout.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func forBaselineLayout() -> UIView
```

## Return Value

The view the constraint system should use to satisfy baseline constraints

## Discussion

When you make a constraint to a view’s [NSLayoutAttributeBaseline](../nslayoutattribute/nslayoutattributebaseline.md) attribute, Auto Layout uses the baseline of the view returned by this method. If that view does not have a baseline, Auto Layout uses the view’s bottom edge.

Override this method to return a text-based subview (for example, [UILabel](../uilabel.md) or a nonscrolling [UITextView](../uitextview.md)). If you override this method, the returned view must be a subview of the receiver. The default implementation returns the receiving view.

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
- [areAnimationsEnabled](areanimationsenabled.md) — Returns a Boolean value indicating whether animations are enabled.
