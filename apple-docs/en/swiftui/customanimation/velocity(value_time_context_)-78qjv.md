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
doc_path: '/documentation/swiftui/customanimation/velocity(value:time:context:)-78qjv'
source_url: 'https://developer.apple.com/documentation/swiftui/customanimation/velocity(value:time:context:)-78qjv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customanimation/velocity%28value%3Atime%3Acontext%3A%29-78qjv.json'
content_hash: 'sha256:534fe4e8dc617657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomAnimation](../customanimation.md)

# velocity(value:time:context:)

<sub>Instance Method</sub>

Calculates the velocity of the animation at a specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func velocity<V>(value: V, time: TimeInterval, context: AnimationContext<V>) -> V? where V : VectorArithmetic
```

## Parameters

- `value` — The vector to animate towards.

- `time` — The amount of time since the start of the animation.

- `context` — An instance of [AnimationContext](../animationcontext.md) that provides access to state and the animation environment.

## Return Value

The current velocity of the animation, or `nil` if the animation has finished.

## Discussion

Implement this method to provide the velocity of the animation at a given time. Should subsequent animations merge with the animation, the system preserves continuity of the velocity between animations.

The default implementation of this method returns `nil`.

> [!note] Note
> State and environment data is available to this method via the `context` parameter, but `context` is read-only. This behavior is different than with [animate(value:time:context:)](<animate(value_time_context_).md>) and [shouldMerge(previous:value:time:context:)](<shouldmerge(previous_value_time_context_).md>) where `context` is an `inout` parameter, letting you change the context including state data of the animation. For more information about managing state data in a custom animation, see [AnimationContext](../animationcontext.md).
