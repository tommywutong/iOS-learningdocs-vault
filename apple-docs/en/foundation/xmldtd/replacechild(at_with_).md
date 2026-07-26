---
title: 'replaceChild(at:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/replacechild(at:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/replacechild(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/replacechild%28at%3Awith%3A%29.json'
content_hash: 'sha256:e63c8a88b91c2249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# replaceChild(at:with:)

<sub>Instance Method</sub>

Replaces a child at a particular index with another child.

<sub>Mac Catalyst, macOS</sub>

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

## Parameters

- `index` — An integer identifying the position of a node in the receiver’s list of child nodes.

- `node` — An [XMLNode](../xmlnode.md) object to replace the object at `index`.

## Discussion

The replaced child node is released.

## See Also

### Manipulating Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- setChildren:](<setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.
