---
title: kind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/kind-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/kind-swift.property.json'
content_hash: 'sha256:dd502084e7be8a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# kind

<sub>Instance Property</sub>

Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).

<sub>Mac Catalyst, macOS</sub>

```swift
var kind: XMLNode.Kind { get }
```

## Discussion

`NSXMLNode` objects can represent documents, elements, attributes, namespaces, text, processing instructions, comments, document type declarations, and specific declarations within DTDs. See Constants for a list of valid NSXMLNodeKind constants

## See Also

### Related Documentation

- [- initWithKind:](<init(kind_).md>) — Returns an `NSXMLNode` instance initialized with the constant indicating node kind.

### Managing XML Node Objects

- [index](index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [level](level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](name.md) — Returns the name of the receiver.
- [objectValue](objectvalue.md) — Returns the object value of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](uri.md) — Returns the URI associated with the receiver.
