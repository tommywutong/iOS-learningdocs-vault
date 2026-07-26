---
title: next
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/next
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/next'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/next.json'
content_hash: 'sha256:0adddc5aa74593e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# next

<sub>Instance Property</sub>

Returns the next `NSXMLNode` object in document order.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var next: XMLNode? { get }
```

## Discussion

You use this method to “walk” forward through the tree structure representing an XML document or document section. (Use [previousNode](previous.md) to traverse the tree in the opposite direction.) Document order is the natural order that XML constructs appear in markup text. If you send this message to the last node in the tree, `nil` is returned. `NSXMLNode` bypasses namespace and attribute nodes when it traverses a tree in document order.

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
