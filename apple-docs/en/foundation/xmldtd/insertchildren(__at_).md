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
doc_path: '/documentation/foundation/xmldtd/insertchildren(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/insertchildren(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/insertchildren%28_%3Aat%3A%29.json'
content_hash: 'sha256:c1465651a42cb6bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# insertChildren(_:at:)

<sub>Instance Method</sub>

Inserts an array of child nodes at a specified location in the receiver’s list of children.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertChildren(_ children: [XMLNode], at index: Int)
```

## Parameters

- `children` — An array of [XMLNode](../xmlnode.md) objects to insert as children of the receiver.

- `index` — An integer identifying the location in the list of current children to make the insertion. The indices of subsequent children in the list are incremented by the number of inserted children.

## See Also

### Manipulating Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
- [- setChildren:](<setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.
