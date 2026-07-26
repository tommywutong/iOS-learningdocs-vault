---
title: 'init(response:dampingRatio:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/init(response:dampingratio:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/init(response:dampingratio:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/init%28response%3Adampingratio%3A%29.json'
content_hash: 'sha256:40c9662982ea81b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# init(response:dampingRatio:)

<sub>Initializer</sub>

Creates a spring with the specified response and damping ratio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(response: Double, dampingRatio: Double)
```

## Parameters

- `response` — Defines the stiffness of the spring as an approximate duration in seconds.

- `dampingRatio` — Defines the amount of drag applied as a fraction the amount needed to produce critical damping.

## See Also

### Creating a spring

- [init(duration:bounce:)](<init(duration_bounce_).md>) — Creates a spring with the specified duration and bounce.
- [init(mass:stiffness:damping:allowOverDamping:)](<init(mass_stiffness_damping_allowoverdamping_).md>) — Creates a spring with the specified mass, stiffness, and damping.
- [init(settlingDuration:dampingRatio:epsilon:)](<init(settlingduration_dampingratio_epsilon_).md>) — Creates a spring with the specified duration and damping ratio.
