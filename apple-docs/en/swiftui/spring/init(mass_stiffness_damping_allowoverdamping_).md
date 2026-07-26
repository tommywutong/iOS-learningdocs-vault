---
title: 'init(mass:stiffness:damping:allowOverDamping:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/init(mass:stiffness:damping:allowoverdamping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/init(mass:stiffness:damping:allowoverdamping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/init%28mass%3Astiffness%3Adamping%3Aallowoverdamping%3A%29.json'
content_hash: 'sha256:855c9a88151eae97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# init(mass:stiffness:damping:allowOverDamping:)

<sub>Initializer</sub>

Creates a spring with the specified mass, stiffness, and damping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mass: Double = 1.0, stiffness: Double, damping: Double, allowOverDamping: Bool = false)
```

## Parameters

- `mass` — Specifies that property of the object attached to the end of the spring.

- `stiffness` — The corresponding spring coefficient.

- `damping` — Defines how the spring’s motion should be damped due to the forces of friction.

## See Also

### Creating a spring

- [init(duration:bounce:)](<init(duration_bounce_).md>) — Creates a spring with the specified duration and bounce.
- [init(response:dampingRatio:)](<init(response_dampingratio_).md>) — Creates a spring with the specified response and damping ratio.
- [init(settlingDuration:dampingRatio:epsilon:)](<init(settlingduration_dampingratio_epsilon_).md>) — Creates a spring with the specified duration and damping ratio.
