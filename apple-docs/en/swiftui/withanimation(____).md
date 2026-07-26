---
title: 'withAnimation(_:_:)'
framework: SwiftUI
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/withanimation(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/withanimation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/withanimation%28_%3A_%3A%29.json'
content_hash: 'sha256:3ae0460751917d61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# withAnimation(_:_:)

<sub>Function</sub>

Returns the result of recomputing the view’s body with the provided animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withAnimation<Result>(_ animation: Animation? = .default, _ body: () throws -> Result) rethrows -> Result
```

## Discussion

This function sets the given [Animation](animation.md) as the [animation](transaction/animation.md) property of the thread’s current [Transaction](transaction.md).

## See Also

### Adding state-based animation to an action

- [withAnimation(_:completionCriteria:_:completion:)](<withanimation(__completioncriteria___completion_).md>) — Returns the result of recomputing the view’s body with the provided animation, and runs the completion when all animations are complete.
- [AnimationCompletionCriteria](animationcompletioncriteria.md) — The criteria that determines when an animation is considered finished.
- [Animation](animation.md) — The way a view changes over time to create a smooth visual transition from one state to another.
