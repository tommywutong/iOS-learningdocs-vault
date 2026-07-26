---
title: 'stopAnimation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewanimating/stopanimation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/stopanimation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/stopanimation%28_%3A%29.json'
content_hash: 'sha256:22cae2c26fd52988'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# stopAnimation(_:)

<sub>Instance Method</sub>

Stops the animations at their current positions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func stopAnimation(_ withoutFinishing: Bool)
```

## Parameters

- `withoutFinishing` — A Boolean indicating whether any final actions should be performed. Specify [true](../../swift/true.md) to clear any animations and move the animator directly to the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state without performing any final actions. Specify [false](../../swift/false.md) to put the animator into the [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md) state.

## Discussion

Call this method when you want to end the animations at their current position. This method removes all of the associated animations from the execution stack and sets the values of any animatable properties to their current values. This method also updates the state of the animator object based on the value of the `withoutFinishing` parameter.

If you specify [false](../../swift/false.md) for the `withoutFinishing` parameter, you can subsequently call the [- finishAnimationAtPosition:](<finishanimation(at_).md>) method to perform the animator’s final actions. For example, a [UIViewPropertyAnimator](../uiviewpropertyanimator.md) object executes its completion blocks when you call this method. You do not have to call the [- finishAnimationAtPosition:](<finishanimation(at_).md>) method right away, or at all, and you can perform other animations before calling that method.

## See Also

### Starting and stopping the animations

- [- startAnimation](<startanimation().md>) — Starts the animation from its current position.
- [- startAnimationAfterDelay:](<startanimation(afterdelay_).md>) — Starts the animation after the specified delay.
- [- pauseAnimation](<pauseanimation().md>) — Pauses a running animation at its current position.
- [- finishAnimationAtPosition:](<finishanimation(at_).md>) — Finishes the animations and returns the animator to the inactive state.
