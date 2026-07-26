---
title: rootDocument
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/rootdocument
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/rootdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/rootdocument.json'
content_hash: 'sha256:fb4df1e4d5a044db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# rootDocument

<sub>Instance Property</sub>

Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.

<sub>Mac Catalyst, macOS</sub>

```swift
var rootDocument: XMLDocument? { get }
```

## Discussion

If the receiver is a standalone node (that is, a node at the head of a detached branch of the tree), this method returns `nil`.

## See Also

### Navigating the Tree of Nodes

- [parent](parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
