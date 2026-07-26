---
title: index
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/index
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/index.json'
content_hash: 'sha256:bf7ae41b71f4e388'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# index

<sub>Instance Property</sub>

Returns the index of the receiver identifying its position relative to its sibling nodes.

<sub>Mac Catalyst, macOS</sub>

```swift
var index: Int { get }
```

## Return Value

An integer that is the index of the receiver relative to its sibling nodes.

## Discussion

The first child node of a parent has an index of zero.

## See Also

### Related Documentation

- [- childAtIndex:](<child(at_).md>) — Returns the child node of the receiver at the specified location.

### Managing XML Node Objects

- [kind](kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).
- [level](level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](name.md) — Returns the name of the receiver.
- [objectValue](objectvalue.md) — Returns the object value of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](uri.md) — Returns the URI associated with the receiver.
