---
title: 'velocity(value:time:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/velocity(value:time:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/velocity(value:time:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/velocity%28value%3Atime%3Acontext%3A%29.json'
content_hash: 'sha256:d3bec22d4028aafa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# velocity(value:time:context:)

<sub>Instance Method</sub>

Calculates the current velocity of the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>) -> V? where V : VectorArithmetic
```

## Return Value

The current velocity of the animation, or `nil` if the velocity isn’t available.
