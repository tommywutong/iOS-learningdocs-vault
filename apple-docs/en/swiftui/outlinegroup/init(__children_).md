---
title: 'init(_:children:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/outlinegroup/init(_:children:)'
source_url: 'https://developer.apple.com/documentation/swiftui/outlinegroup/init(_:children:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/outlinegroup/init%28_%3Achildren%3A%29.json'
content_hash: 'sha256:1d68a1b9f8483ff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OutlineGroup](../outlinegroup.md)

# init(_:children:)

<sub>Initializer</sub>

Creates an outline group from a collection of root data elements and a key path to element’s children.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init<DataElement>(_ data: Data, children: KeyPath<DataElement, Data?>) where ID == DataElement.ID, Parent == TableRow<DataElement>, Leaf == TableRow<DataElement>, Subgroup == TableRow<DataElement>, DataElement : Identifiable, DataElement == Data.Element
```

## Parameters

- `data` — A collection of tree-structured, identified data.

- `children` — A key path to a property whose non-`nil` value gives the children of `data`. A non-`nil` but empty value denotes an element capable of having children that’s currently childless, such as an empty directory in a file system. On the other hand, if the property at the key path is `nil`, then the outline group treats `data` as a leaf in the tree, like a regular file in a file system.

## Discussion

This initializer provides a default `TableRowBuilder` using `TableRow` for each data element.

This initializer creates an instance that uniquely identifies table rows across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

## See Also

### Creating an outline group

- [init(_:children:content:)](<init(__children_content_).md>) — Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](<init(__id_children_content_).md>) — Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.
