---
title: damping
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spring/damping
source_url: 'https://developer.apple.com/documentation/swiftui/spring/damping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/damping.json'
content_hash: 'sha256:3c36d9f77f7f5091'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# damping

<sub>Instance Property</sub>

Defines how the spring’s motion should be damped due to the forces of friction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var damping: Double { get }
```

## Discussion

Reducing this value reduces the energy loss with each oscillation: the spring will overshoot its destination. Increasing the value increases the energy loss with each duration: there will be fewer and smaller oscillations.

## See Also

### Getting spring characteristics

- [bounce](bounce.md) — How bouncy the spring is.
- [dampingRatio](dampingratio.md) — The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [duration](duration.md) — The perceptual duration, which defines the pace of the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [response](response.md) — The stiffness of the spring, defined as an approximate duration in seconds.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
