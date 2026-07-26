---
title: 'init(_:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Arowcontent%3A%29.json'
content_hash: 'sha256:d3a1466315bbbe5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:rowContent:)

<sub>Initializer</sub>

Creates a list that computes its rows on demand from an underlying collection of identifiable data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<Data, RowContent>(_ data: Binding<Data>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

## Parameters

- `data` — A collection of identifiable data for computing the list.

- `rowContent` — A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from enumerated data

- [init(_:selection:rowContent:)](<init(__selection_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.
- [init(_:id:rowContent:)](<init(__id_rowcontent_).md>) — Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](<init(__id_selection_rowcontent_).md>) — Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.
