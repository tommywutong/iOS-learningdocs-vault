---
title: AnyView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anyview
source_url: 'https://developer.apple.com/documentation/swiftui/anyview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anyview.json'
content_hash: 'sha256:a5dc8c05932e1620'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyView

<sub>Structure</sub>

A type-erased view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct AnyView
```

## Overview

An `AnyView` allows changing the type of view used in a given view hierarchy. Whenever the type of view used with an `AnyView` changes, the old hierarchy is destroyed and a new hierarchy is created for the new type.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a view

- [init(_:)](<anyview/init(__).md>) — Create an instance that type-erases `view`.
- [init(erasing:)](<anyview/init(erasing_).md>)

## See Also

### Supporting view types

- [EmptyView](emptyview.md) — A view that doesn’t contain any content.
- [EquatableView](equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](subscriptionview.md) — A view that subscribes to a publisher with an action.
- [TupleView](tupleview.md) — A View created from a swift tuple of View values.
