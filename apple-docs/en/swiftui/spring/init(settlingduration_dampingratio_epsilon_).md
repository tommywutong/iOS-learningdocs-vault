---
title: 'init(settlingDuration:dampingRatio:epsilon:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/init(settlingduration:dampingratio:epsilon:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/init(settlingduration:dampingratio:epsilon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/init%28settlingduration%3Adampingratio%3Aepsilon%3A%29.json'
content_hash: 'sha256:8d6a2c01006dd907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# init(settlingDuration:dampingRatio:epsilon:)

<sub>Initializer</sub>

Creates a spring with the specified duration and damping ratio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(settlingDuration: TimeInterval, dampingRatio: Double, epsilon: Double = 0.001)
```

## Parameters

- `settlingDuration` — The approximate time it will take for the spring to come to rest.

- `dampingRatio` — The amount of drag applied as a fraction of the amount needed to produce critical damping.

- `epsilon` — The threshhold for how small all subsequent values need to be before the spring is considered to have settled.

## See Also

### Creating a spring

- [init(duration:bounce:)](<init(duration_bounce_).md>) — Creates a spring with the specified duration and bounce.
- [init(mass:stiffness:damping:allowOverDamping:)](<init(mass_stiffness_damping_allowoverdamping_).md>) — Creates a spring with the specified mass, stiffness, and damping.
- [init(response:dampingRatio:)](<init(response_dampingratio_).md>) — Creates a spring with the specified response and damping ratio.
