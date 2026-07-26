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
doc_path: '/documentation/foundation/xmlelement/replacechild(at:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/replacechild(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/replacechild%28at%3Awith%3A%29.json'
content_hash: 'sha256:ea2681d69ef17ea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# replaceChild(at:with:)

<sub>Instance Method</sub>

Replaces a child node at a specified location with another child node.

<sub>Mac Catalyst, macOS</sub>

```swift
func replaceChild(at index: Int, with node: XMLNode)
```

## Parameters

- `index` — An integer identifying a position in the receiver’s list of children. An exception is raised if `index` is out of bounds.

- `node` — An XML node object that will replace the current child.

## Discussion

The replaced XML node object is released upon removal.

## See Also

### Manipulating Child Elements

- [- addChild:](<addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- setChildren:](<setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
