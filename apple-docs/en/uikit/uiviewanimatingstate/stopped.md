---
title: UIViewAnimatingState.stopped
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimatingstate/stopped
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimatingstate/stopped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimatingstate/stopped.json'
content_hash: 'sha256:3755af8cae59814e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewAnimatingState](../uiviewanimatingstate.md)

# UIViewAnimatingState.stopped

<sub>Case</sub>

The animation is stopped. Putting an animation into this state ends the animation and leaves any animatable properties at their current values, instead of updating them to their intended final values. An animation cannot be started while in this state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case stopped
```

## See Also

### Constants

- [UIViewAnimatingStateInactive](inactive.md) — The animations have not yet started executing. This is the initial state of the animator object.
- [UIViewAnimatingStateActive](active.md) — The animator object is active and animations are either running or paused. An animator moves to this state after the first call to [- startAnimation](<../uiviewanimating/startanimation().md>) or [- pauseAnimation](<../uiviewanimating/pauseanimation().md>). It stays in the active state until the animations finish naturally or until you call the [- stopAnimation:](<../uiviewanimating/stopanimation(__).md>) method.
