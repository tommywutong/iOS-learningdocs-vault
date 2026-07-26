---
title: 'normalizeAdjacentTextNodesPreservingCDATA(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/normalizeadjacenttextnodespreservingcdata(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/normalizeadjacenttextnodespreservingcdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/normalizeadjacenttextnodespreservingcdata%28_%3A%29.json'
content_hash: 'sha256:37f56425b532a780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# normalizeAdjacentTextNodesPreservingCDATA(_:)

<sub>Instance Method</sub>

Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.

<sub>Mac Catalyst, macOS</sub>

```swift
func normalizeAdjacentTextNodesPreservingCDATA(_ preserve: Bool)
```

## Parameters

- `preserve` — [true](../../swift/true.md) if CDATA sections are left alone as text nodes, [false](../../swift/false.md) otherwise.

## Discussion

A text node with a value of an empty string is removed. When you process an input source of XML, adjacent text nodes are automatically normalized. You should invoke this method (with `preserve` as [false](../../swift/false.md)) before using the [XMLNode](../xmlnode.md) methods [- objectsForXQuery:constants:error:](<../xmlnode/objects(forxquery_constants_).md>) or [- nodesForXPath:error:](<../xmlnode/nodes(forxpath_).md>).

## See Also

### Manipulating Child Elements

- [- addChild:](<addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- setChildren:](<setchildren(__).md>) — Sets all child nodes of the receiver at once, replacing any existing children.
