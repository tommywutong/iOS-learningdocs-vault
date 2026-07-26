---
title: 'animate(value:time:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/animate(value:time:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/animate(value:time:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/animate%28value%3Atime%3Acontext%3A%29.json'
content_hash: 'sha256:163aa536eb510f2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# animate(value:time:context:)

<sub>Instance Method</sub>

Calculates the current value of the animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic
```

## Return Value

The current value of the animation, or `nil` if the animation has finished.
