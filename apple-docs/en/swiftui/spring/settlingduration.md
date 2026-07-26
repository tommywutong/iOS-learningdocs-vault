---
title: settlingDuration
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spring/settlingduration
source_url: 'https://developer.apple.com/documentation/swiftui/spring/settlingduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/settlingduration.json'
content_hash: 'sha256:f7614d06fef5f38f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# settlingDuration

<sub>Instance Property</sub>

The estimated duration required for the spring system to be considered at rest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var settlingDuration: TimeInterval { get }
```

## Discussion

This uses a `target` of 1.0, an `initialVelocity` of 0, and an `epsilon` of 0.001.

## See Also

### Getting spring characteristics

- [bounce](bounce.md) — How bouncy the spring is.
- [damping](damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [dampingRatio](dampingratio.md) — The amount of drag applied, as a fraction of the amount needed to produce critical damping.
- [duration](duration.md) — The perceptual duration, which defines the pace of the spring.
- [mass](mass.md) — The mass of the object attached to the end of the spring.
- [response](response.md) — The stiffness of the spring, defined as an approximate duration in seconds.
- [stiffness](stiffness.md) — The spring stiffness coefficient.
