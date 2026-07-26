---
title: initialVelocity
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation/initialvelocity
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation/initialvelocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation/initialvelocity.json'
content_hash: 'sha256:9f92df36a8e0a89e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CASpringAnimation](../caspringanimation.md)

# initialVelocity

<sub>Instance Property</sub>

The initial velocity of the object attached to the spring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var initialVelocity: CGFloat { get set }
```

## Discussion

Defaults to `0`, which represents an unmoving object. Negative values represent the object moving away from the spring attachment point, positive values represent the object moving towards the spring attachment point.

## See Also

### Configuring Physical Attributes

- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
