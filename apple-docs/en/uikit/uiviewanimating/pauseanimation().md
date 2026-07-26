---
title: pauseAnimation()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimating/pauseanimation()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimating/pauseanimation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimating/pauseanimation%28%29.json'
content_hash: 'sha256:f8ea21a56dbac887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimating](../uiviewanimating.md)

# pauseAnimation()

<sub>Instance Method</sub>

Pauses a running animation at its current position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pauseAnimation()
```

## Discussion

This method pauses running animations at their current values. Calling this method on an inactive animator moves its state to [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md) and puts its animations in a paused state right away. To resume the animations, call the [- startAnimation](<startanimation().md>) method. If the animation is already paused, this method should do nothing. It is a programmer error to call this method while the state of the animator is set to [UIViewAnimatingStateStopped](../uiviewanimatingstate/stopped.md).

## See Also

### Starting and stopping the animations

- [- startAnimation](<startanimation().md>) — Starts the animation from its current position.
- [- startAnimationAfterDelay:](<startanimation(afterdelay_).md>) — Starts the animation after the specified delay.
- [- stopAnimation:](<stopanimation(__).md>) — Stops the animations at their current positions.
- [- finishAnimationAtPosition:](<finishanimation(at_).md>) — Finishes the animations and returns the animator to the inactive state.
