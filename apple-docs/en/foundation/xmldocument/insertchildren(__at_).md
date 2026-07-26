---
title: 'insertChildren(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/insertchildren(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/insertchildren(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/insertchildren%28_%3Aat%3A%29.json'
content_hash: 'sha256:b7e4c6816746674a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# insertChildren(_:at:)

<sub>Instance Method</sub>

Inserts an array of children at a specified position in the receiver’s array of children.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertChildren(_ children: [XMLNode], at index: Int)
```

## Parameters

- `children` — An array of [XMLNode](../xmlnode.md) objects representing comments, processing instructions, or the root element.

- `index` — An integer identifying the location in the receiver’s children array for insertion. The indexes of children after the new child are increased by `[children count`]. If `index` is less than zero or greater than the number of children, an out-of-bounds exception is raised.

## See Also

### Adding and Removing Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node after the last of the receiver’s existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver located at a specified position in its array of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [- setChildren:](<setchildren(__).md>) — Sets the child nodes of the receiver.
