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
doc_path: '/documentation/foundation/xmlelement/removechild(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/removechild(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/removechild%28at%3A%29.json'
content_hash: 'sha256:544fd43205b550ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# removeChild(at:)

<sub>Instance Method</sub>

Removes the child node of the receiver identified by a given index.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeChild(at index: Int)
```

## Parameters

- `index` — An integer identifying the node in the receiver’s list of children to remove. An exception is raised if `index` is out of bounds.

## Discussion

The XML node object is released upon removal. The indices of subsequent children are decremented by one.

## See Also

### Manipulating Child Elements

- [- addChild:](<addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- setChildren:](<setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
