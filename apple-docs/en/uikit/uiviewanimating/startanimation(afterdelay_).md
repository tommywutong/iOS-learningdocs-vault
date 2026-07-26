---
title: 'startAnimation(afterDelay:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewanimating/startanimation(afterdelay:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/startanimation(afterdelay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/startanimation%28afterdelay%3A%29.json'
content_hash: 'sha256:697e570e2c83896b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# startAnimation(afterDelay:)

<sub>Instance Method</sub>

Starts the animation after the specified delay.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startAnimation(afterDelay delay: TimeInterval)
```

## Parameters

- `delay` — The amount of time (in seconds) to wait before starting the animation.

## Discussion

Call this method to start the animations or to resume a set of paused animations after the specified time delay. This method sets the state of the animator to [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md), if it is not already there. It is a programmer error to call this method while the state of the animator is set to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md).

When implementing a custom animator, use this method to transition your animator to the active state and to run the animations after the specified delay. Run your animations from the progress point in the [fractionComplete](fractioncomplete.md) property. Update the [state](state.md) and [running](isrunning.md) properties, as well as any other relevant properties of your custom animator object.

## See Also

### Starting and stopping the animations

- [- startAnimation](<startanimation().md>) — Starts the animation from its current position.
- [- pauseAnimation](<pauseanimation().md>) — Pauses a running animation at its current position.
- [- stopAnimation:](<stopanimation(__).md>) — Stops the animations at their current positions.
- [- finishAnimationAtPosition:](<finishanimation(at_).md>) — Finishes the animations and returns the animator to the inactive state.
