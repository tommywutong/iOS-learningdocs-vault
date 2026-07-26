---
title: isRemovedOnCompletion
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/isremovedoncompletion
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/isremovedoncompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/isremovedoncompletion.json'
content_hash: 'sha256:cd8c9a93e412ed79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# isRemovedOnCompletion

<sub>Instance Property</sub>

Determines if the animation is removed from the target layer’s animations upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isRemovedOnCompletion: Bool { get set }
```

## Discussion

When [true](../../swift/true.md), the animation is removed from the target layer’s animations once its active duration has passed. Defaults to [true](../../swift/true.md).

## See Also

### Animation Attributes

- [timingFunction](timingfunction.md) — An optional timing function defining the pacing of the animation.
