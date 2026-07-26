---
title: 'addAnimations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/addanimations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addanimations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/addanimations%28_%3A%29.json'
content_hash: 'sha256:07c1db35c712806f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# addAnimations(_:)

<sub>Instance Method</sub>

Adds the specified animation block to the animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAnimations(_ animation: @escaping () -> Void)
```

## Parameters

- `animation` — A block containing the animations you want to add to the animator object. This block has no return value and takes no parameters. This parameter must not be `nil`.

## Discussion

Use this method to add new animation blocks to the animator. The animations in the new block run alongside any previously configured animations. Blocks added while the animator’s state is [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) are executed over the time specified by the [duration](duration.md) property. Blocks added while the animator’s state is [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md) are executed over the remaining portion of the total run time. For example, if the duration is `2.0` and you add an animation block to a running animator whose [fractionComplete](../uiviewanimating/fractioncomplete.md) property is `0.5`, the animations run for `1.0` second. Any blocks you add while the animator is running begin executing immediately.

If the `animation` block modifies a property that’s being modified by a different property animator, then the animators combine their changes in the most appropriate way. For many properties, the changes from each animator are added together to yield a new intermediate value. If a property can’t be modified in this additive manner, the new animations take over as if the [UIViewAnimationOptionBeginFromCurrentState](../uiview/animationoptions/beginfromcurrentstate.md) option had been specified for a view-based animation.

You can call this method multiple times to add multiple blocks to the animator. It’s a programmer error to call this method when the animator’s [state](../uiviewanimating/state.md) property is set to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md).

## See Also

### Modifying animations

- [- addAnimations:delayFactor:](<addanimations(__delayfactor_).md>) — Adds the specified animation block with a delay.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the timing and duration of a paused animation.
