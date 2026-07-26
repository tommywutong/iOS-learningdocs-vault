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
doc_path: '/documentation/foundation/xmlelement/insertchild(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/insertchild(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/insertchild%28_%3Aat%3A%29.json'
content_hash: 'sha256:48047d67246714b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# insertChild(_:at:)

<sub>Instance Method</sub>

Inserts a new child node at a specified location in the receiver’s list of child nodes.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertChild(_ child: XMLNode, at index: Int)
```

## Parameters

- `child` — An XML node object to be inserted as a child of the receiver.

- `index` — An integer identifying a position in the receiver’s list of children. An exception is raised if `index` is out of bounds.

## Discussion

Insertion of the node increments the indexes of sibling nodes after it.

## See Also

### Manipulating Child Elements

- [- addChild:](<addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- setChildren:](<setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
