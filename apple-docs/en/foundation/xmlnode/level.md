---
title: level
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/level
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/level.json'
content_hash: 'sha256:4940944cc77ea3b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# level

<sub>Instance Property</sub>

Returns the nesting level of the receiver within the tree hierarchy.

<sub>Mac Catalyst, macOS</sub>

```swift
var level: Int { get }
```

## Return Value

An integer indicating a nesting level.

## Discussion

The root element of a document has a nesting level of one.

## See Also

### Managing XML Node Objects

- [index](index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [kind](kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).
- [name](name.md) — Returns the name of the receiver.
- [objectValue](objectvalue.md) — Returns the object value of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](uri.md) — Returns the URI associated with the receiver.
