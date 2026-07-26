---
title: 'init(_:editActions:selection:rowContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/list/init(_:editactions:selection:rowcontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/list/init(_:editactions:selection:rowcontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/list/init%28_%3Aeditactions%3Aselection%3Arowcontent%3A%29.json'
content_hash: 'sha256:6ba26bba579856d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [List](../list.md)

# init(_:editActions:selection:rowContent:)

<sub>Initializer</sub>

Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.

<sub>macOS</sub>

```swift
nonisolated init<Data, RowContent>(_ data: Binding<Data>, editActions: EditActions<Data>, selection: Binding<SelectionValue>, @ContentBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable
```

## Parameters

- `data` — The identifiable data for computing the list.

- `editActions` — The edit actions that are synthesized on `data`.

- `selection` — A binding to a non optional selected value.

- `rowContent` — A content builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods allowing the user to delete or move elements from the collection, and select a single element.

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
- [init(_:id:editActions:rowContent:)](<init(__id_editactions_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data and enables editing the collection.
- [init(_:id:editActions:selection:rowContent:)](<init(__id_editactions_selection_rowcontent_).md>) — Creates a list that computes its rows on demand from an underlying collection of identifiable data, enables editing the collection, and requires a selection of a single row.
