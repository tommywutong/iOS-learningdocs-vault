---
title: 'setChildren(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/setchildren(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/setchildren(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/setchildren%28_%3A%29.json'
content_hash: 'sha256:8371a2a6376ba939'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# setChildren(_:)

<sub>Instance Method</sub>

Removes all existing children of the receiver and replaces them with an array of new child nodes.

<sub>Mac Catalyst, macOS</sub>

```swift
func setChildren(_ children: [XMLNode]?)
```

## Parameters

- `children` — An array of [XMLNode](../xmlnode.md) objects. To remove all existing children, pass in `nil`.

## Discussion

Replaced or removed child nodes are released.

## See Also

### Manipulating Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node to the end of the list of existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a child node in the receiver’s list of children at a specific location in the list.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node at a particular location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child at a particular index with another child.
