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
doc_path: '/documentation/foundation/xmldocument/replacechild(at:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/replacechild(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/replacechild%28at%3Awith%3A%29.json'
content_hash: 'sha256:fed1ea46bc172ff3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# replaceChild(at:with:)

<sub>Instance Method</sub>

Replaces the child node of the receiver located at a specified position in its array of children with another node.

<sub>Mac Catalyst, macOS</sub>

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

## Parameters

- `index` — An integer identifying a position in the receiver’s array of children. If `index` is less than zero or greater than the number of children minus one, an out-of-bounds exception is raised.

- `node` — An [XMLNode](../xmlnode.md) object to replace the one at `index`; it must represent a comment, a processing instruction, or the root element.

## Discussion

The removed `NSXMLNode` object is autoreleased.

## See Also

### Adding and Removing Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node after the last of the receiver’s existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of children at a specified position in the receiver’s array of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver located at a specified position in its array of children.
- [- setChildren:](<setchildren(__).md>) — Sets the child nodes of the receiver.
