---
title: 'init(_:children:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/outlinegroup/init(_:children:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/outlinegroup/init(_:children:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/outlinegroup/init%28_%3Achildren%3Acontent%3A%29.json'
content_hash: 'sha256:57a45353770ed3a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OutlineGroup](../outlinegroup.md)

# init(_:children:content:)

<sub>Initializer</sub>

Creates an outline group from a binding to a collection of root data elements and a key path to its children.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init<C, E>(_ data: Binding<C>, children: WritableKeyPath<E, C?>, @ContentBuilder content: @escaping (Binding<E>) -> Leaf) where Data == Binding<C>, ID == E.ID, C : MutableCollection, C : RandomAccessCollection, E : Identifiable, E == C.Element
```

## Parameters

- `data` — A collection of tree-structured, identified data.

- `children` — A key path to a property whose non-`nil` value gives the children of `data`. A non-`nil` but empty value denotes an element capable of having children that’s currently childless, such as an empty directory in a file system. On the other hand, if the property at the key path is `nil`, then the outline group treats `data` as a leaf in the tree, like a regular file in a file system.

- `content` — A content builder that produces a content view based on an element in `data`.

## Discussion

This initializer creates an instance that uniquely identifies views across updates based on the identity of the underlying data element.

All generated disclosure groups begin in the collapsed state.

Make sure that the identifier of a data element only changes if you mean to replace that element with a new element, one with a new identity. If the ID of an element changes, then the content view generated from that element will lose any current state and animations.

## See Also

### Creating an outline group

- [init(_:children:)](<init(__children_).md>) — Creates an outline group from a collection of root data elements and a key path to element’s children.
- [init(_:id:children:content:)](<init(__id_children_content_).md>) — Creates an outline group from a binding to a collection of root data elements, the key path to a data element’s identifier, and a key path to its children.
