---
title: bounce
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spring/bounce
source_url: 'https://developer.apple.com/documentation/swiftui/spring/bounce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/bounce.json'
content_hash: 'sha256:15d37573451ae4bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# bounce

<sub>Instance Property</sub>

How bouncy the spring is.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bounce: Double { get }
```

## Discussion

A value of 0 indicates no bounces (a critically damped spring), positive values indicate increasing amounts of bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and negative values indicate overdamped springs with a minimum value of -1.0.

## See Also

### Getting spring characteristics

- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [dampingRatio](dampingratio.md) — The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [duration](duration.md) — The perceptual duration, which defines the pace of the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [response](response.md) — The stiffness of the spring, defined as an approximate duration in seconds.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
