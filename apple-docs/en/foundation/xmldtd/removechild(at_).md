---
title: 'removeChild(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/removechild(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/removechild(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/removechild%28at%3A%29.json'
content_hash: 'sha256:0eabd66907181c00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# removeChild(at:)

<sub>Instance Method</sub>

Removes the child node at a particular location in the receiver’s list of children.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeChild(at index: Int)
```

## Parameters

- `index` — An integer identifying the child node to remove. The indices of subsequent children in the list are decremented by one.

## Discussion

The removed child node is released.

## See Also

### Manipulating Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
- [- setChildren:](<setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.
