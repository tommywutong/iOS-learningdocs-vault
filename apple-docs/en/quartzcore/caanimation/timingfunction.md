---
title: timingFunction
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/timingfunction
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/timingfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/timingfunction.json'
content_hash: 'sha256:4fde5b3ad553e815'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# timingFunction

<sub>Instance Property</sub>

An optional timing function defining the pacing of the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timingFunction: CAMediaTimingFunction? { get set }
```

## Discussion

Defaults to `nil`, indicating linear pacing.

## See Also

### Animation Attributes

- [removedOnCompletion](isremovedoncompletion.md) — Determines if the animation is removed from the target layer’s animations upon completion.
