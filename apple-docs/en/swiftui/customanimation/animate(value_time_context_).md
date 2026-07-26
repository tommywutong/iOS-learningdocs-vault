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
doc_path: '/documentation/swiftui/customanimation/animate(value:time:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customanimation/animate(value:time:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customanimation/animate%28value%3Atime%3Acontext%3A%29.json'
content_hash: 'sha256:71a155d15579b36e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomAnimation](../customanimation.md)

# animate(value:time:context:)

<sub>Instance Method</sub>

Calculates the value of the animation at the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func animate<V>(value: V, time: TimeInterval, context: inout AnimationContext<V>) -> V? where V : VectorArithmetic
```

## Parameters

- `value` — The vector to animate towards.

- `time` — The elapsed time since the start of the animation.

- `context` — An instance of [AnimationContext](../animationcontext.md) that provides access to state and the animation environment.

## Return Value

The current value of the animation, or `nil` if the animation has finished.

## Discussion

Implement this method to calculate and return the value of the animation at a given point in time. If the animation has finished, return `nil` as the value. This signals to the system that it can remove the animation.

If your custom animation needs to maintain state between calls to the `animate(value:time:context:)` method, store the state data in `context`. This makes the data available to the method next time the system calls it. To learn more about managing state data in a custom animation, see [AnimationContext](../animationcontext.md).
