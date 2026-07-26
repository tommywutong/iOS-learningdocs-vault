---
title: 'force(fromValue:toValue:position:velocity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/force(fromvalue:tovalue:position:velocity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/force(fromvalue:tovalue:position:velocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/force%28fromvalue%3Atovalue%3Aposition%3Avelocity%3A%29.json'
content_hash: 'sha256:a37c7b8af5150bab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# force(fromValue:toValue:position:velocity:)

<sub>Instance Method</sub>

Calculates the force upon the spring given a current position, velocity, and divisor from the starting and end values for the spring to travel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func force<V>(fromValue: V, toValue: V, position: V, velocity: V) -> V where V : Animatable
```

## Discussion

This value is in units of the vector type per second squared.

## See Also

### Calculating forces and durations

- [force(target:position:velocity:)](<force(target_position_velocity_).md>) — Calculates the force upon the spring given a current position, target, and velocity amount of change.
- [settlingDuration(target:initialVelocity:epsilon:)](<settlingduration(target_initialvelocity_epsilon_).md>) — The estimated duration required for the spring system to be considered at rest.
- [settlingDuration(fromValue:toValue:initialVelocity:epsilon:)](<settlingduration(fromvalue_tovalue_initialvelocity_epsilon_).md>) — The estimated duration required for the spring system to be considered at rest.
