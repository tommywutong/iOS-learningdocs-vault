---
title: 'addAnimationCompletion(criteria:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/transaction/addanimationcompletion(criteria:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/addanimationcompletion(criteria:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/addanimationcompletion%28criteria%3A_%3A%29.json'
content_hash: 'sha256:31804236c83f292a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# addAnimationCompletion(criteria:_:)

<sub>Instance Method</sub>

Adds a completion to run when the animations created with this transaction are all complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addAnimationCompletion(criteria: AnimationCompletionCriteria = .logicallyComplete, _ completion: @escaping () -> Void)
```

## Discussion

The completion callback will always be fired exactly one time. If no animations are created by the changes in `body`, then the callback will be called immediately after `body`.

## See Also

### Managing animations

- [animation](animation.md) — The animation, if any, associated with the current state change.
- [disablesAnimations](disablesanimations.md) — A Boolean value that indicates whether views should disable animations.
