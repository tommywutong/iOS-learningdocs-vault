---
title: SubscriptionView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subscriptionview
source_url: 'https://developer.apple.com/documentation/swiftui/subscriptionview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subscriptionview.json'
content_hash: 'sha256:8dfc0f0e9f38b308'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SubscriptionView

<sub>Structure</sub>

A view that subscribes to a publisher with an action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct SubscriptionView<PublisherType, Content> where PublisherType : Publisher, Content : View, PublisherType.Failure == Never
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a subscription view

- [init(content:publisher:action:)](<subscriptionview/init(content_publisher_action_).md>)

### Managing the subscription

- [publisher](subscriptionview/publisher.md) — The `Publisher` that is being subscribed.
- [action](subscriptionview/action.md) — The `Action` executed when `publisher` emits an event.
- [content](subscriptionview/content.md) — The content view.

## See Also

### Supporting view types

- [AnyView](anyview.md) — A type-erased view.
- [EmptyView](emptyview.md) — A view that doesn’t contain any content.
- [EquatableView](equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [TupleView](tupleview.md) — A View created from a swift tuple of View values.
