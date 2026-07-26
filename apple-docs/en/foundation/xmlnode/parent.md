---
title: parent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/parent
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/parent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/parent.json'
content_hash: 'sha256:908cb15c7e354337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# parent

<sub>Instance Property</sub>

Returns the parent node of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var parent: XMLNode? { get }
```

## Discussion

Document nodes and standalone nodes (that is, the root of a detached branch of a tree) have no parent, and sending this message to them returns `nil`. A one-to-one relationship does not always exists between a parent and its children; although a namespace or attribute node cannot be a child, it still has a parent element.

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
