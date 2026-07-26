---
title: 'finishAnimation(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewanimating/finishanimation(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/finishanimation(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/finishanimation%28at%3A%29.json'
content_hash: 'sha256:30a8fd4213b75e4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# finishAnimation(at:)

<sub>Instance Method</sub>

Finishes the animations and returns the animator to the inactive state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finishAnimation(at finalPosition: UIViewAnimatingPosition)
```

## Parameters

- `finalPosition` — The final position for any view properties. Specify [UIViewAnimatingPositionCurrent](../uiviewanimatingposition/current.md) to leave the view properties unchanged from their current values.

## Discussion

After putting the animator object into the [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md) state, call this method to perform any final cleanup tasks. It is a programmer error to call this method at any time except after a call to the [- stopAnimation:](<stopanimation(__).md>) method where you pass [false](../../swift/false.md) for the `withoutFinishing` parameter. Calling this method is not required, but is recommended in cases where you want to ensure that completion blocks or other final tasks are performed.

Implementations of this method are responsible for setting the state of the animator object to [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) and for performing any final cleanup tasks, such as executing completion blocks.

## See Also

### Starting and stopping the animations

- [- startAnimation](<startanimation().md>) — Starts the animation from its current position.
- [- startAnimationAfterDelay:](<startanimation(afterdelay_).md>) — Starts the animation after the specified delay.
- [- pauseAnimation](<pauseanimation().md>) — Pauses a running animation at its current position.
- [- stopAnimation:](<stopanimation(__).md>) — Stops the animations at their current positions.
