---
title: animation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/animation
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/animation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/animation.json'
content_hash: 'sha256:5fb6207766a2071e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# animation

<sub>Instance Property</sub>

The animation, if any, associated with the current state change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var animation: Animation? { get set }
```

## See Also

### Managing animations

- [disablesAnimations](disablesanimations.md) — A Boolean value that indicates whether views should disable animations.
- [addAnimationCompletion(criteria:_:)](<addanimationcompletion(criteria___).md>) — Adds a completion to run when the animations created with this transaction are all complete.
