---
title: settlingDuration
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation/settlingduration
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation/settlingduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation/settlingduration.json'
content_hash: 'sha256:ed78940b5eed0e1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CASpringAnimation](../caspringanimation.md)

# settlingDuration

<sub>Instance Property</sub>

The estimated duration required for the spring system to be considered at rest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var settlingDuration: CFTimeInterval { get }
```

## Discussion

The duration is evaluated for the current animation parameters and may not the same as the [duration](../camediatiming/duration.md).

The following code creates a spring animation with a [duration](../camediatiming/duration.md) of 2 seconds.

```swift
let spring = CASpringAnimation()

spring.keyPath = "position.x"
spring.fromValue = 0
spring.toValue = 640
spring.damping = 5
spring.duration = 2
```

With a damping coefficient of `5`, the settling duration is approximately 2.85 seconds: the animated layer bounces around the target position several times before settling. However, changing the [damping](damping.md) property to `15` reduces the settling duration to just over 1 second: the animated layer quickly comes to a stop as it reaches the target position.

All of the spring animation’s physical attributes: [damping](damping.md), [initialVelocity](initialvelocity.md), [mass](mass.md) and [stiffness](stiffness.md), can affect the settling duration.

## See Also

### Configuring Physical Attributes

- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [initialVelocity](initialvelocity.md) — The initial velocity of the object attached to the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
