---
title: isContinuous
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/iscontinuous
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/iscontinuous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/iscontinuous.json'
content_hash: 'sha256:dcb92432ade4ddab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# isContinuous

<sub>Instance Property</sub>

A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isContinuous: Bool { get set }
```

## Discussion

This value is `true` if a continuous action created the transaction, and is `false` otherwise. Continuous actions include things like dragging a slider or pressing and holding a stepper, as opposed to tapping a button.

## See Also

### Getting information about a transaction

- [scrollTargetAnchor](scrolltargetanchor.md) — The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [tracksVelocity](tracksvelocity.md) — Whether this transaction will track the velocity of any animatable properties that change.
- [subscript(_:)](<subscript(__).md>) — Accesses the transaction value associated with a custom key.
