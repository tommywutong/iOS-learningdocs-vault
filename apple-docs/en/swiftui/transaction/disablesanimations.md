---
title: disablesAnimations
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/disablesanimations
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/disablesanimations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/disablesanimations.json'
content_hash: 'sha256:be9b5da3748f808d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# disablesAnimations

<sub>Instance Property</sub>

A Boolean value that indicates whether views should disable animations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var disablesAnimations: Bool { get set }
```

## Discussion

This value is `true` during the initial phase of a two-part transition update, to prevent [animation(_:)](<../view/animation(__).md>) from inserting new animations into the transaction.

## See Also

### Managing animations

- [animation](animation.md) — The animation, if any, associated with the current state change.
- [addAnimationCompletion(criteria:_:)](<addanimationcompletion(criteria___).md>) — Adds a completion to run when the animations created with this transaction are all complete.
