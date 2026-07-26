---
title: 'update(value:velocity:target:deltaTime:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/update(value:velocity:target:deltatime:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/update(value:velocity:target:deltatime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/update%28value%3Avelocity%3Atarget%3Adeltatime%3A%29.json'
content_hash: 'sha256:294c80d9b58d946d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# update(value:velocity:target:deltaTime:)

<sub>Instance Method</sub>

Updates the current  value and velocity of a spring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func update<V>(value: inout V, velocity: inout V, target: V, deltaTime: TimeInterval) where V : VectorArithmetic
```

## Parameters

- `value` — The current value of the spring.

- `velocity` — The current velocity of the spring.

- `target` — The target that `value` is moving towards.

- `deltaTime` — The amount of time that has passed since the spring was at the position specified by `value`.
