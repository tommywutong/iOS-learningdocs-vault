---
title: 'init(_:selection:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:selection:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:selection:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Aselection%3Arowcontent%3A%29.json'
content_hash: 'sha256:a785922321667662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:selection:rowContent:)

<sub>Initializer</sub>

Creates a list that computes its rows on demand from an underlying collection of identifiable data, optionally allowing users to select a single row.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<Data, RowContent>(_ data: Binding<Data>, selection: Binding<SelectionValue?>?, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

## Parameters

- `data` — The identifiable data for computing the list.

- `selection` — A binding to a selected value.

- `rowContent` — A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from enumerated data

- [init(_:rowContent:)](<init(__rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data.
- [init(_:id:rowContent:)](<init(__id_rowcontent_).md>) — Creates a list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:selection:rowContent:)](<init(__id_selection_rowcontent_).md>) — Creates a list that identifies its rows based on a key path to the identifier of the underlying data, optionally allowing users to select a single row.
