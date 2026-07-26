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
doc_path: '/documentation/foundation/xmlelement/setchildren(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/setchildren(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/setchildren%28_%3A%29.json'
content_hash: 'sha256:73bf501bf183b471'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# setChildren(_:)

<sub>Instance Method</sub>

Sets all child nodes of the receiver at once, replacing any existing children.

<sub>Mac Catalyst, macOS</sub>

```swift
func setChildren(_ children: [XMLNode]?)
```

## Parameters

- `children` — An array of `NSXMLElement` objects or [XMLNode](../xmlnode.md) objects of kinds [NSXMLElementKind](../xmlnode/kind-swift.enum/element.md), [NSXMLProcessingInstructionKind](../xmlnode/kind-swift.enum/processinginstruction.md), [NSXMLTextKind](../xmlnode/kind-swift.enum/text.md), or [NSXMLCommentKind](../xmlnode/kind-swift.enum/comment.md).

## Discussion

Send this message with `children` as `nil` to remove all child nodes.

## See Also

### Manipulating Child Elements

- [- addChild:](<addchild(__).md>) — Adds a child node at the end of the receiver’s current list of children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a new child node at a specified location in the receiver’s list of child nodes.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of child nodes at a specified location in the receiver’s list of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver identified by a given index.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces a child node at a specified location with another child node.
- [- normalizeAdjacentTextNodesPreservingCDATA:](<normalizeadjacenttextnodespreservingcdata(__).md>) — Coalesces adjacent text nodes of the receiver that you have explicitly added, optionally including CDATA sections.
