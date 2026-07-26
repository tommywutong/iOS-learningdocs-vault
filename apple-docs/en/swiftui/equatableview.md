---
title: EquatableView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/equatableview
source_url: 'https://developer.apple.com/documentation/swiftui/equatableview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/equatableview.json'
content_hash: 'sha256:51ae14a68ba281fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EquatableView

<sub>Structure</sub>

A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct EquatableView<Content> where Content : Equatable, Content : View
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating an equatable view

- [init(content:)](<equatableview/init(content_).md>)
- [content](equatableview/content.md)

## See Also

### Supporting view types

- [AnyView](anyview.md) — A type-erased view.
- [EmptyView](emptyview.md) — A view that doesn’t contain any content.
- [SubscriptionView](subscriptionview.md) — A view that subscribes to a publisher with an action.
- [TupleView](tupleview.md) — A View created from a swift tuple of View values.
