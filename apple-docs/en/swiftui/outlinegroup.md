---
title: OutlineGroup
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/outlinegroup
source_url: 'https://developer.apple.com/documentation/swiftui/outlinegroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/outlinegroup.json'
content_hash: 'sha256:1498fad4ff6a720c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OutlineGroup

<sub>Structure</sub>

A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable
```

## Overview

Use an outline group when you need a view that can represent a hierarchy of data by using disclosure views. This allows the user to navigate the tree structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a simplified view of a file system. Passing the root of this tree and the key path of its children allows you to quickly create a visual representation of the file system.

```swift
struct FileItem: Hashable, Identifiable, CustomStringConvertible {
    var id: Self { self }
    var name: String
    var children: [FileItem]? = nil
    var description: String {
        switch children {
        case nil:
            return "📄 \(name)"
        case .some(let children):
            return children.isEmpty ? "📂 \(name)" : "📁 \(name)"
        }
    }
}

let data =
  FileItem(name: "users", children:
    [FileItem(name: "user1234", children:
      [FileItem(name: "Photos", children:
        [FileItem(name: "photo001.jpg"),
         FileItem(name: "photo002.jpg")]),
       FileItem(name: "Movies", children:
         [FileItem(name: "movie001.mp4")]),
          FileItem(name: "Documents", children: [])
      ]),
     FileItem(name: "newuser", children:
       [FileItem(name: "Documents", children: [])
       ])
    ])

OutlineGroup(data, children: \.children) { item in
    Text("\(item.description)")
}
```

### Type parameters

Five generic type constraints define a specific `OutlineGroup` instance:

- `Data`: The type of a collection containing the children of an element in the tree-shaped data.
- `ID`: The type of the identifier for an element.
- `Parent`: The type of the visual representation of an element whose children property is non-`nil`
- `Leaf`: The type of the visual representation of an element whose children property is `nil`.
- `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [TableRowContent](tablerowcontent.md), [View](view.md)

## Topics

### Creating an outline group

- [init(_:children:)](<outlinegroup/init(__children_).md>) — Creates an outline group from a collection of root data elements and a key path to element’s children.
- [init(_:children:content:)](<outlinegroup/init(__children_content_).md>) — Creates an outline group from a binding to a collection of root data elements and a key path to its children.
- [init(_:id:children:content:)](<outlinegroup/init(__id_children_content_).md>) — Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.

### Supporting types

- [OutlineSubgroupChildren](outlinesubgroupchildren.md) — A type-erased view representing the children in an outline subgroup.

## See Also

### Disclosing information progressively

- [DisclosureGroup](disclosuregroup.md) — A view that shows or hides another content view, based on the state of a disclosure control.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
