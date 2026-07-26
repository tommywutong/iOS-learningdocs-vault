---
title: nextSibling
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/nextsibling
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/nextsibling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/nextsibling.json'
content_hash: 'sha256:199f473993aabfe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# nextSibling

<sub>Instance Property</sub>

Returns the next `NSXMLNode` object that is a sibling node to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var nextSibling: XMLNode? { get }
```

## Discussion

This object will have an [index](index.md) value that is one more than the receiver’s. If there are no more subsequent siblings (that is, other child nodes of the receiver’s parent) the method returns `nil`.

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
