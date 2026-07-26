---
title: stiffness
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation/stiffness
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation/stiffness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation/stiffness.json'
content_hash: 'sha256:d772b996760eb210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CASpringAnimation](../caspringanimation.md)

# stiffness

<sub>Instance Property</sub>

The spring stiffness coefficient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stiffness: CGFloat { get set }
```

## Discussion

The default stiffness coefficient is `100`. Increasing the [stiffness](stiffness.md) reduces the number of oscillations and will reduce the settling duration. Decreasing the [stiffness](stiffness.md) increases the the number of oscillations and will increase the settling duration.

## See Also

### Configuring Physical Attributes

- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [initialVelocity](initialvelocity.md) — The initial velocity of the object attached to the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
