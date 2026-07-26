---
title: mass
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spring/mass
source_url: 'https://developer.apple.com/documentation/swiftui/spring/mass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/mass.json'
content_hash: 'sha256:f031675a4660b5f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# mass

<sub>Instance Property</sub>

The mass of the object attached to the end of the spring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mass: Double { get }
```

## Discussion

The default mass is 1. Increasing this value will increase the spring’s effect: the attached object will be subject to more oscillations and greater overshoot, resulting in an increased settling duration. Decreasing the mass will reduce the spring effect: there will be fewer oscillations and a reduced overshoot, resulting in a decreased settling duration.

## See Also

### Getting spring characteristics

- [bounce](bounce.md) — How bouncy the spring is.
- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [dampingRatio](dampingratio.md) — The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [duration](duration.md) — The perceptual duration, which defines the pace of the spring.
- [response](response.md) — The stiffness of the spring, defined as an approximate duration in seconds.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
