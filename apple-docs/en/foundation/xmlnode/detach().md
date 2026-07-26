---
title: detach()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/detach()
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/detach()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/detach%28%29.json'
content_hash: 'sha256:1a06f87873659110'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# detach()

<sub>Instance Method</sub>

Detaches the receiver from its parent node.

<sub>Mac Catalyst, macOS</sub>

```swift
func detach()
```

## Discussion

This method is applicable to `NSXMLNode` objects representing elements, text, comments, processing instructions, attributes, and namespaces. Once the node object is detached, you can add it as a child node of another parent.

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
- [previousSibling](previoussibling.md) — Returns the previous `NSXMLNode` object that is a sibling node to the receiver.
