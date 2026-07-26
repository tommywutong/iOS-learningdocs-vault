---
title: 'init(_:children:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:children:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:children:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Achildren%3Arowcontent%3A%29.json'
content_hash: 'sha256:91cea73cd983b663'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:children:rowContent:)

<sub>Initializer</sub>

Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data, RowContent>(_ data: Binding<Data>, children: WritableKeyPath<Data.Element, Data?>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable
```

## Parameters

- `data` — A collection of identifiable data for computing the list.

- `children` — A key path to a property whose non-`nil` value gives the children of `data`. A non-`nil` but empty value denotes a node capable of having children that is currently childless, such as an empty directory in a file system. On the other hand, if the property at the key path is `nil`, then `data` is treated as a leaf node in the tree, like a regular file in a file system.

- `rowContent` — A content builder that creates the view for a single row of the list.

## See Also

### Creating a list from hierarchical data

- [init(_:children:selection:rowContent:)](<init(__children_selection_rowcontent_).md>) — Creates a hierarchical list that computes its rows on demand from a binding to an underlying collection of identifiable data and allowing users to have exactly one row always selected.
- [init(_:id:children:rowContent:)](<init(__id_children_rowcontent_).md>) — Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data.
- [init(_:id:children:selection:rowContent:)](<init(__id_children_selection_rowcontent_).md>) — Creates a hierarchical list that identifies its rows based on a key path to the identifier of the underlying data and allowing users to have exactly one row always selected.
