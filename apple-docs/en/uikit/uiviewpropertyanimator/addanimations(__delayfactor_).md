---
title: 'addAnimations(_:delayFactor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewpropertyanimator/addanimations(_:delayfactor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/addanimations(_:delayfactor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/addanimations%28_%3Adelayfactor%3A%29.json'
content_hash: 'sha256:40570a2040d72e25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# addAnimations(_:delayFactor:)

<sub>Instance Method</sub>

Adds the specified animation block with a delay.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAnimations(_ animation: @escaping () -> Void, delayFactor: CGFloat)
```

## Parameters

- `animation` — A block containing the animations you want to add to the animator object. This block has no return value and takes no parameters. This parameter must not be `nil`.

- `delayFactor` — The factor to use for delaying the start of the animations. The value you specify must be between `0.0` and `1.0`. This value is multiplied by the animator’s remaining duration to determine the actual delay in seconds. For example, specifying the value `0.5` when the duration is `2.0` results in a one second delay for the start of the animations.

## Discussion

Use this method to add new animation blocks to the animator. The animations in the new block run alongside any previously configured animations after the specified delay. Blocks added while the animator’s state is [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) are executed over the time specified by the [duration](duration.md) property minus any delay. Blocks added while the animator’s state is [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md) are executed over the remaining portion of the total run time minus the delay. For example, if the duration is `2.0` and you add an animation block with a delay factor of `0.25` to a running animator whose [fractionComplete](../uiviewanimating/fractioncomplete.md) property is `0.25`, the animations run for `1.0` second.

If the `animation` block modifies a property that is being modified by a different property animator, then the animators combine their changes in the most appropriate way. For many properties, the changes from each animator are added together to yield a new intermediate value. If a property cannot be modified in this additive manner, the new animations take over as if the [UIViewAnimationOptionBeginFromCurrentState](../uiview/animationoptions/beginfromcurrentstate.md) option had been specified for a view-based animation.

You can call this method multiple times to add multiple blocks to the animator. It is a programmer error to call this method when the animator’s [state](../uiviewanimating/state.md) property is set to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md).

## See Also

### Modifying animations

- [- addAnimations:](<addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addCompletion:](<addcompletion(__).md>) — Adds the specified completion block to the animator.
- [- continueAnimationWithTimingParameters:durationFactor:](<continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the timing and duration of a paused animation.
