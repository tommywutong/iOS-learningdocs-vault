---
title: fadeOutDuration
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/fadeoutduration
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/fadeoutduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/fadeoutduration.json'
content_hash: 'sha256:00e6fc24cbd9f948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# fadeOutDuration

<sub>Instance Property</sub>

For animations attached to SceneKit objects, the duration for transitioning out of the animation’s effect as it ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fadeOutDuration: CGFloat { get set }
```

## Discussion

Use this property to create smooth transitions between the effects of multiple animations. These transitions are especially useful for geometry animations created with external 3D authoring tools.

For example, the geometry loaded from a scene file for a game character may have associated animations for player actions such as walking and jumping. When the player jumps, if the fade duration is zero, SceneKit abruptly switches from the current frame of the walk animation to the first frame of the jump animation. If the fade duration is greater than zero, SceneKit plays both animations at once during that duration and interpolates vertex positions from one animation to the other, creating a smooth transition.

To attach animations to SceneKit objects, see [SCNAnimatable](../../scenekit/scnanimatable.md).

## See Also

### Fading between SceneKit Animations

- [fadeInDuration](fadeinduration.md) — For animations attached to SceneKit objects, the duration for transitioning into the animation’s effect as it begins.
