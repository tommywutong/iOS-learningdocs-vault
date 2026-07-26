---
title: 'settlingDuration(target:initialVelocity:epsilon:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/settlingduration(target:initialvelocity:epsilon:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/settlingduration(target:initialvelocity:epsilon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/settlingduration%28target%3Ainitialvelocity%3Aepsilon%3A%29.json'
content_hash: 'sha256:b04f2f754f20da33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# settlingDuration(target:initialVelocity:epsilon:)

<sub>Instance Method</sub>

The estimated duration required for the spring system to be considered at rest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func settlingDuration<V>(target: V, initialVelocity: V = .zero, epsilon: Double) -> TimeInterval where V : VectorArithmetic
```

## Discussion

The epsilon value specifies the threshold for how small all subsequent values need to be before the spring is considered to have settled.

## See Also

### Calculating forces and durations

- [force(target:position:velocity:)](<force(target_position_velocity_).md>) — Calculates the force upon the spring given a current position, target, and velocity amount of change.
- [force(fromValue:toValue:position:velocity:)](<force(fromvalue_tovalue_position_velocity_).md>) — Calculates the force upon the spring given a current position, velocity, and divisor from the starting and end values for the spring to travel.
- [settlingDuration(fromValue:toValue:initialVelocity:epsilon:)](<settlingduration(fromvalue_tovalue_initialvelocity_epsilon_).md>) — The estimated duration required for the spring system to be considered at rest.
