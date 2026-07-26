---
title: 'withAnimation(_:completionCriteria:_:completion:)'
framework: SwiftUI
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/withanimation(_:completioncriteria:_:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/withanimation(_:completioncriteria:_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/withanimation%28_%3Acompletioncriteria%3A_%3Acompletion%3A%29.json'
content_hash: 'sha256:844f8315f1f8928e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# withAnimation(_:completionCriteria:_:completion:)

<sub>Function</sub>

Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withAnimation<Result>(_ animation: Animation? = .default, completionCriteria: AnimationCompletionCriteria = .logicallyComplete, _ body: () throws -> Result, completion: @escaping () -> Void) rethrows -> Result
```

## Discussion

This function sets the given [Animation](animation.md) as the [animation](transaction/animation.md) property of the thread’s current [Transaction](transaction.md) as well as calling `Transaction/addAnimationCompletion` with the specified completion.

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

## See Also

### Adding state-based animation to an action

- [withAnimation(_:_:)](<withanimation(____).md>) — Returns the result of recomputing the view’s body with the provided animation.
- [AnimationCompletionCriteria](animationcompletioncriteria.md) — The criteria that determines when an animation is considered finished.
- [Animation](animation.md) — The way a view changes over time to create a smooth visual transition from one state to another.
