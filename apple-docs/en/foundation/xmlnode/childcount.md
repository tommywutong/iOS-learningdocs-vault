---
title: childCount
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/childcount
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/childcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/childcount.json'
content_hash: 'sha256:de3418e2799c3253'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# childCount

<sub>Instance Property</sub>

Returns the number of child nodes the receiver has.

<sub>Mac Catalyst, macOS</sub>

```swift
var childCount: Int { get }
```

## Discussion

This receiver should be an `NSXMLNode` object representing a document, element, or document type declaration. For performance reasons, use this method instead of getting the count from the array returned by [children](children.md) (for example, `[[thisNode children] count`]).

## See Also

### Navigating the Tree of Nodes

- [rootDocument](rootdocument.md) — Returns the [XMLDocument](../xmldocument.md) object containing the root element and representing the XML document as a whole.
- [parent](parent.md) — Returns the parent node of the receiver.
- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.
- [children](children.md) — Returns an immutable array containing the child nodes of the receiver (as `NSXMLNode` objects).
- [nextNode](next.md) — Returns the next `NSXMLNode` object in document order.
- [nextSibling](nextsibling.md) — Returns the next `NSXMLNode` object that is a sibling node to the receiver.
- [previousNode](previous.md) — Returns the previous `NSXMLNode` object in document order.
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
- [- detach](<detach().md>) — Detaches the receiver from its parent node.
