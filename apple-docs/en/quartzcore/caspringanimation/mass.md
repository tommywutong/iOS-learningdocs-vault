---
title: mass
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation/mass
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation/mass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation/mass.json'
content_hash: 'sha256:973206da8cff1952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CASpringAnimation](../caspringanimation.md)

# mass

<sub>Instance Property</sub>

The mass of the object attached to the end of the spring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mass: CGFloat { get set }
```

## Discussion

The default mass is `1`. Increasing this value will increase the spring effect: the attached object will be subject to more oscillations and greater overshoot, resulting in an increased [settlingDuration](settlingduration.md). Decreasing the mass will reduce the spring effect: there will be fewer oscillations and a reduced overshoot, resulting in a decreased [settlingDuration](settlingduration.md).

## See Also

### Configuring Physical Attributes

- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [initialVelocity](initialvelocity.md) — The initial velocity of the object attached to the spring.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
