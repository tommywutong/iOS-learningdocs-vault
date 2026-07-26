---
title: TupleView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tupleview
source_url: 'https://developer.apple.com/documentation/swiftui/tupleview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tupleview.json'
content_hash: 'sha256:3c44331e7d19b8cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TupleView

<sub>Structure</sub>

A View created from a swift tuple of View values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct TupleView<T>
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a tuple view

- [init(_:)](<tupleview/init(__).md>)
- [value](tupleview/value.md)

## See Also

### Supporting view types

- [AnyView](anyview.md) — A type-erased view.
- [EmptyView](emptyview.md) — A view that doesn’t contain any content.
- [EquatableView](equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](subscriptionview.md) — A view that subscribes to a publisher with an action.
