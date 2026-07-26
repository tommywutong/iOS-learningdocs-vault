---
title: previousSibling
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/previoussibling
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/previoussibling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/previoussibling.json'
content_hash: 'sha256:c84505123ff2ebae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# previousSibling

<sub>Instance Property</sub>

Returns the previous `NSXMLNode` object that is a sibling node to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var previousSibling: XMLNode? { get }
```

## Discussion

This object will have an [index](index.md) value that is one less than the receiver’s. If there are no more previous siblings (that is, other child nodes of the receiver’s parent) the method returns `nil`

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [childCount](childcount.md) — Returns the number of child nodes the receiver has.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
