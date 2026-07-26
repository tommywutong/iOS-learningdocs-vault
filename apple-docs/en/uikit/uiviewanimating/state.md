---
title: state
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/state
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/state.json'
content_hash: 'sha256:d0cb5df340f6ec6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# state

<sub>Instance Property</sub>

The current state of the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var state: UIViewAnimatingState { get }
```

## Discussion

This property reflects the current state of the animation. An animator object starts in the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state. Calling the [- startAnimation](<startanimation().md>) or [- pauseAnimation](<pauseanimation().md>) method changes the state to [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md). Changing the [fractionComplete](fractioncomplete.md) property also moves the animator to the active state. The animator remains in the active state until its animations finish, at which point it moves back to the inactive state.

Calling the [- stopAnimation:](<stopanimation(__).md>) method changes the state of the animator to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md). When in this state, the animations are stopped and cannot be restarted until you call the [- finishAnimationAtPosition:](<finishanimation(at_).md>) method, which returns the animator to the inactive state.

## See Also

### Getting the animator’s state

- [fractionComplete](fractioncomplete.md) — The completion percentage of the animation.
- [reversed](isreversed.md) — A Boolean value indicating whether the animation is running in the reverse direction.
- [running](isrunning.md) — A Boolean value indicating whether the animation is currently running.
