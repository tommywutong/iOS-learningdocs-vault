---
title: dampingRatio
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spring/dampingratio
source_url: 'https://developer.apple.com/documentation/swiftui/spring/dampingratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/dampingratio.json'
content_hash: 'sha256:af8e577232811b08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# dampingRatio

<sub>Instance Property</sub>

The amount of drag applied, as a fraction of the amount needed to produce critical damping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dampingRatio: Double { get }
```

## Discussion

When `dampingRatio` is 1, the spring will smoothly decelerate to its final position without oscillating. Damping ratios less than 1 will oscillate more and more before coming to a complete stop.

## See Also

### Getting spring characteristics

- [bounce](bounce.md) — How bouncy the spring is.
- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [duration](duration.md) — The perceptual duration, which defines the pace of the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [response](response.md) — The stiffness of the spring, defined as an approximate duration in seconds.
- [settlingDuration](settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
