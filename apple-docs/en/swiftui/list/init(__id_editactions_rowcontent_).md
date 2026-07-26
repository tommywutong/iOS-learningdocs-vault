---
title: 'init(_:id:editActions:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:id:editactions:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:id:editactions:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Aid%3Aeditactions%3Arowcontent%3A%29.json'
content_hash: 'sha256:11c78c549b874df9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:id:editActions:rowContent:)

<sub>Initializer</sub>

Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

## Parameters

- `data` — A collection of identifiable data for computing the list.

- `id` — The key path to the data model’s identifier.

- `editActions` — The edit actions that are synthesized on `data`.

- `rowContent` — A content builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection.

```swift
List($foods, editActions: [.delete, .move]) { $food in
   HStack {
       Text(food.name)
       Toggle("Favorite", isOn: $food.isFavorite)
   }
}
```

Use [deleteDisabled(_:)](<../view/deletedisabled(__).md>) and [moveDisabled(_:)](<../view/movedisabled(__).md>) to disable respectively delete or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`, `DynamicViewContent.onMove(perform:)`, or `View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any synthesized action

## See Also

### Creating a list from editable data

- [init(_:editActions:rowContent:)](<init(__editactions_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:editActions:selection:rowContent:)](<init(__editactions_selection_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
- [init(_:id:editActions:selection:rowContent:)](<init(__id_editactions_selection_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
