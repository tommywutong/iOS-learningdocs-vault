---
title: 'addChild(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/addchild(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/addchild(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/addchild%28_%3A%29.json'
content_hash: 'sha256:57644b3a08b9dda3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# addChild(_:)

<sub>Instance Method</sub>

Adds a child node to the end of the list of existing children.

<sub>Mac Catalyst, macOS</sub>

```swift
func addChild(_ child: XMLNode)
```

## Parameters

- `child` — The node object to add to the existing children.

## See Also

### Manipulating Child Nodes

- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
- [- setChildren:](<setchildren(__).md>) — Removes all existing children of the receiver and replaces them with an array of new child nodes.
