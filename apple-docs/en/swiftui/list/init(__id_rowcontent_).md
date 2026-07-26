---
title: 'init(_:id:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:id:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:id:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Aid%3Arowcontent%3A%29.json'
content_hash: 'sha256:ffde78c1167a1a1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:id:rowContent:)

<sub>Initializer</sub>

Creates a list that identifies its rows based on a key path to the identifier of the underlying data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

## Parameters

- `data` — The data for populating the list.

- `id` — The key path to the data model’s identifier.

- `rowContent` — A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from enumerated data

- [init(_:rowContent:)](<init(__rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:selection:rowContent:)](<init(__selection_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:selection:rowContent:)](<init(__id_selection_rowcontent_).md>) — Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.
