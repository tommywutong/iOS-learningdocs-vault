---
title: startAnimation()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/startanimation()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/startanimation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/startanimation%28%29.json'
content_hash: 'sha256:32ca7e070c97feb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# startAnimation()

<sub>Instance Method</sub>

Starts the animation from its current position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func startAnimation()
```

## Discussion

Call this method to start the animations or to resume the animation after they were paused. This method sets the state of the animator to [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md), if it isn’t already there. It’s a programmer error to call this method while the state of the animator is set to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md).

When implementing a custom animator, use this method to transition your animator to the active state and to run the animations. Run your animations from the progress point in the [fractionComplete](fractioncomplete.md) property. Update the [state](state.md) and [running](isrunning.md) properties, as well as any other relevant properties of your custom animator object.

## See Also

### Starting and stopping the animations

- [- startAnimationAfterDelay:](<startanimation(afterdelay_).md>) — Starts the animation after the specified delay.
- [- pauseAnimation](<pauseanimation().md>) — Pauses a running animation at its current position.
- [- stopAnimation:](<stopanimation(__).md>) — Stops the animations at their current positions.
- [- finishAnimationAtPosition:](<finishanimation(at_).md>) — Finishes the animations and returns the animator to the inactive state.
