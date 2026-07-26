---
title: 'init(duration:bounce:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/init(duration:bounce:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/init(duration:bounce:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/init%28duration%3Abounce%3A%29.json'
content_hash: 'sha256:cbf1b0dc487db9ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# init(duration:bounce:)

<sub>Initializer</sub>

Creates a spring with the specified duration and bounce.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(duration: TimeInterval = 0.5, bounce: Double = 0.0)
```

## Parameters

- `duration` — Defines the pace of the spring. This is approximately equal to the settling duration, but for springs with very large bounce values, will be the duration of the period of oscillation for the spring.

- `bounce` — How bouncy the spring should be. A value of 0 indicates no bounces (a critically damped spring), positive values indicate increasing amounts of bounciness up to a maximum of 1.0 (corresponding to undamped oscillation), and negative values indicate overdamped springs with a minimum value of -1.0.

## See Also

### Creating a spring

- [init(mass:stiffness:damping:allowOverDamping:)](<init(mass_stiffness_damping_allowoverdamping_).md>) — Creates a spring with the specified mass, stiffness, and damping.
- [init(response:dampingRatio:)](<init(response_dampingratio_).md>) — Creates a spring with the specified response and damping ratio.
- [init(settlingDuration:dampingRatio:epsilon:)](<init(settlingduration_dampingratio_epsilon_).md>) — Creates a spring with the specified duration and damping ratio.
