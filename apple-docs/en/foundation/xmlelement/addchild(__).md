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
doc_path: '/documentation/foundation/xmlelement/addchild(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/addchild(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/addchild%28_%3A%29.json'
content_hash: 'sha256:24627bbdab2a48d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# addChild(_:)

<sub>Instance Method</sub>

Adds a child node at the end of the receiver’s current list of children.

<sub>Mac Catalyst, macOS</sub>

```swift
func addChild(_ child: XMLNode)
```

## Parameters

- `child` — An XML node object to add to the receiver’s children.

## Discussion

The new node has an index value that is one greater than the last of the current children.

## See Also

### Manipulating Child Elements

- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- setChildren:](<setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
