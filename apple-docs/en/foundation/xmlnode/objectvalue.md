---
title: objectValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/objectvalue
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/objectvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/objectvalue.json'
content_hash: 'sha256:de66029a2fe03352'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# objectValue

<sub>Instance Property</sub>

Returns the object value of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var objectValue: Any? { get set }
```

## Return Value

The object value of the receiver, which may be the same as the value returned by [stringValue](stringvalue.md). For nodes without content (for example, document nodes), this method returns the string value, or an empty string if there is no string value.

## See Also

### Managing XML Node Objects

- [index](index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [kind](kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).
- [level](level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](name.md) — Returns the name of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [- setStringValue:resolvingEntities:](<setstringvalue(__resolvingentities_).md>) — Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](uri.md) — Returns the URI associated with the receiver.
