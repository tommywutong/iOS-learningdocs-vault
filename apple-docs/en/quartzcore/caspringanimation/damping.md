---
title: damping
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation/damping
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation/damping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation/damping.json'
content_hash: 'sha256:f360a069a3b6afef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CASpringAnimation](../caspringanimation.md)

# damping

<sub>Instance Property</sub>

Defines how the spring’s motion should be damped due to the forces of friction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var damping: CGFloat { get set }
```

## Discussion

The default value of the [damping](damping.md) property is `10`. Reducing this value reduces the energy loss with each oscillation: the animated value will overshoot the [toValue](../cabasicanimation/tovalue.md) and the [settlingDuration](settlingduration.md) may be greater than the [duration](../camediatiming/duration.md). Increasing the value increases the energy loss with each duration: there will be fewer and smaller oscillations and the [settlingDuration](settlingduration.md) may be smaller than the duration.

## See Also

### Configuring Physical Attributes

- [initialVelocity](initialvelocity.md) — The initial velocity of the object attached to the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
