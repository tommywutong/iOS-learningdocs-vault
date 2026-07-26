---
title: UIViewAnimatingState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewanimatingstate
source_url: 'https://developer.apple.com/documentation/uikit/uiviewanimatingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewanimatingstate.json'
content_hash: 'sha256:e3fef44c48a41813'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewAnimatingState

<sub>Enumeration</sub>

Constants indicating the current state of the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIViewAnimatingState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIViewAnimatingStateInactive](uiviewanimatingstate/inactive.md) — The animations have not yet started executing. This is the initial state of the animator object.
- [UIViewAnimatingStateActive](uiviewanimatingstate/active.md) — The animator object is active and animations are either running or paused. An animator moves to this state after the first call to [- startAnimation](<uiviewanimating/startanimation().md>) or [- pauseAnimation](<uiviewanimating/pauseanimation().md>). It stays in the active state until the animations finish naturally or until you call the [- stopAnimation:](<uiviewanimating/stopanimation(__).md>) method.
- [UIViewAnimatingStateStopped](uiviewanimatingstate/stopped.md) — The animation is stopped. Putting an animation into this state ends the animation and leaves any animatable properties at their current values, instead of updating them to their intended final values. An animation cannot be started while in this state.

### Initializers

- [init(rawValue:)](<uiviewanimatingstate/init(rawvalue_).md>)

## See Also

### Constants

- [UIViewAnimatingPosition](uiviewanimatingposition.md) — Constants indicating positions within the animation.
