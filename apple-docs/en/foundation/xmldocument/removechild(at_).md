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
doc_path: '/documentation/foundation/xmldocument/removechild(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/removechild(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/removechild%28at%3A%29.json'
content_hash: 'sha256:e530b5f7f26c0c14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# removeChild(at:)

<sub>Instance Method</sub>

Removes the child node of the receiver located at a specified position in its array of children.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeChild(at index: Int)
```

## Parameters

- `index` — An integer identifying the position of an child in the receiver’s array. If `index` is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.

## Discussion

Subsequent children have their indexes decreased by one. The removed [XMLNode](../xmlnode.md) object is autoreleased.

## See Also

### Adding and Removing Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node after the last of the receiver’s existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of children at a specified position in the receiver’s array of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [- setChildren:](<setchildren(__).md>) — Sets the child nodes of the receiver.
