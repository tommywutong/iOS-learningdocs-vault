---
title: 'init(_:id:editActions:selection:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:id:editactions:selection:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Aid%3Aeditactions%3Aselection%3Arowcontent%3A%29.json'
content_hash: 'sha256:9639da8f9f863d6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:id:editActions:selection:rowContent:)

<sub>Initializer</sub>

Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

<sub>macOS</sub>

```swift
nonisolated init<Data, ID, RowContent>(_ data: Binding<Data>, id: KeyPath<Data.Element, ID>, editActions: EditActions<Data>, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable
```

## Parameters

- `data` — The identifiable data for computing and to be edited by the list.

- `id` — The key path to the data model’s identifier.

- `editActions` — The edit actions that are synthesized on `data`.

- `selection` — A binding to a non optional selected value.

- `rowContent` — A content builder that creates the view for a single row of

## Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection, and selects a single row.

```swift
List(
    $foods,
    editActions: [.delete, .move],
    selection: $selectedFood
) { $food in
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
- [init(_:id:editActions:rowContent:)](<init(__id_editactions_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
