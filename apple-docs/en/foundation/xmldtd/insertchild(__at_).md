---
title: 'insertChild(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/insertchild(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/insertchild(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/insertchild%28_%3Aat%3A%29.json'
content_hash: 'sha256:5affd68b524bb3f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# insertChild(_:at:)

<sub>Instance Method</sub>

Inserts a child node in the receiver’s list of children at a specific location in the list.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

## Parameters

- `child` — An XML-node object that represents the child to insert.

- `index` — An integer identifying the location in the receiver’s list of children to insert `child`. The indices of subsequent children in the list are incremented by one.

## See Also

### Manipulating Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
- [- setChildren:](<setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.
