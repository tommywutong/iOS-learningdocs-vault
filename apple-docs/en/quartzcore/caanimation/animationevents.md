---
title: animationEvents
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/animationevents
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/animationevents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/animationevents.json'
content_hash: 'sha256:4155c15076f4eae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# animationEvents

<sub>Instance Property</sub>

For animations attached to SceneKit objects, a list of events attached to an animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var animationEvents: [SCNAnimationEvent]? { get set }
```

## Discussion

An array of [SCNAnimationEvent](../../scenekit/scnanimationevent.md) objects, each of which adds a timed action to the animation.

For example, you can create animation events that play sound effects timed to match the footsteps of an animated game character or that add new nodes to the scene when an animation completes.

To attach animations to SceneKit objects, see [SCNAnimatable](../../scenekit/scnanimatable.md).
