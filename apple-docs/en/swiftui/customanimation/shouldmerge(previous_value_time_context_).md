---
title: 'shouldMerge(previous:value:time:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/customanimation/shouldmerge(previous:value:time:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/customanimation/shouldmerge(previous:value:time:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customanimation/shouldmerge%28previous%3Avalue%3Atime%3Acontext%3A%29.json'
content_hash: 'sha256:b8011d6ea85e15bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomAnimation](../customanimation.md)

# shouldMerge(previous:value:time:context:)

<sub>Instance Method</sub>

Determines whether an instance of the animation can merge with other running animations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func shouldMerge<V>(previous: Animation, value: V, time: TimeInterval, context: inout AnimationContext<V>) -> Bool where V : VectorArithmetic
```

## Parameters

- `previous` — The previous running animation.

- `value` — The vector to animate towards.

- `time` — The amount of time since the start of the previous animation.

- `context` — An instance of [AnimationContext](../animationcontext.md) that provides access to state and the animation environment.

## Return Value

A Boolean value of `true` if the animation should merge with the previous animation; otherwise, `false`.

## Discussion

When a view creates a new animation on an animatable value that already is running an animation, the system calls the `shouldMerge(previous:value:time:context:)` method on the new instance to determine whether it can merge the two instances. Implement this method if the animation can merge with other instances. The default implementation returns `false`.

If `shouldMerge(previous:value:time:context:)` returns `true`, the system merges the new animation instance with the previous animation. The system provides to the new instance the state and elapsed time from the previous one. Then it removes the previous animation.

If this method returns `false`, the system doesn’t merge the animation with the previous one. Instead, both animations run together and the system combines their results.

If your custom animation needs to maintain state between calls to the `shouldMerge(previous:value:time:context:)` method, store the state data in `context`. This makes the data available to the method next time the system calls it. To learn more, see [AnimationContext](../animationcontext.md).

## Default Implementations

### CustomAnimation Implementations

- [shouldMerge(previous:value:time:context:)](<shouldmerge(previous_value_time_context_)-9171c.md>) — Determines whether an instance of the animation can merge with other running animations.
