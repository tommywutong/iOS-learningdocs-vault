---
title: 'child(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/child(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/child(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/child%28at%3A%29.json'
content_hash: 'sha256:ac4630e9891e9150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# child(at:)

<sub>Instance Method</sub>

Returns the child node of the receiver at the specified location.

<sub>Mac Catalyst, macOS</sub>

```swift
func child(at index: Int) -> XMLNode?
```

## Parameters

- `index` — An integer specifying a node position in the receiver’s array of children. If `index` is out of bounds, an exception is raised.

## Return Value

An NSXMLNode object or `nil` f the receiver has no children.

## Discussion

The receiver should be an `NSXMLNode` object representing a document, element, or document type declaration. The returned node object can represent an element, comment, text, or processing instruction.

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](parent.md) — Returns the parent node of the receiver.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
