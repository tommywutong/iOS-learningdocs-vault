---
title: uri
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/uri
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/uri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/uri.json'
content_hash: 'sha256:5b8e1e14deaed780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# uri

<sub>Instance Property</sub>

Returns the URI associated with the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var uri: String? { get set }
```

## Discussion

A node’s URI is derived from its namespace or a document’s URI; for documents, the URI comes either from the parsed XML or is explicitly set. You cannot change the URI for a particular node other for than a namespace or document node.

## See Also

### Managing XML Node Objects

- [index](index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [kind](kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).
- [level](level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](name.md) — Returns the name of the receiver.
- [objectValue](objectvalue.md) — Returns the object value of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
