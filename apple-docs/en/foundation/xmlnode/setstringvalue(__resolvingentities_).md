---
title: 'setStringValue(_:resolvingEntities:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/setstringvalue(_:resolvingentities:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/setstringvalue(_:resolvingentities:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/setstringvalue%28_%3Aresolvingentities%3A%29.json'
content_hash: 'sha256:dd6b2b7c412e8bdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# setStringValue(_:resolvingEntities:)

<sub>Instance Method</sub>

Sets the content of the receiver as a string value and, optionally, resolves character references, predefined entities, and user-defined entities as declared in the associated DTD.

<sub>Mac Catalyst, macOS</sub>

```swift
func setStringValue(_ string: String, resolvingEntities resolve: Bool)
```

## Parameters

- `string` — A string to assign as the value of the receiver.

- `resolve` — [true](../../swift/true.md) to resolve character references, predefined entities, and user-defined entities as declared in the associated DTD; [false](../../swift/false.md) otherwise. Namespace and processing-instruction nodes have their entities resolved even if `resolve` is [false](../../swift/false.md).

## Discussion

User-defined entities not declared in the DTD remain in their unresolved form. This method can only be invoked on `NSXMLNode` objects that may have content, specifically elements, attributes, namespaces, processing instructions, text, and DTD-declaration nodes. Setting the string value of a node object removes all existing children, including processing instructions and comments. Setting the string value of an element -node object creates a text node as the sole child.

## See Also

### Managing XML Node Objects

- [index](index.md) — Returns the index of the receiver identifying its position relative to its sibling nodes.
- [kind](kind-swift.property.md) — Returns the kind of node the receiver is as a constant of type [Kind](kind-swift.enum.md).
- [level](level.md) — Returns the nesting level of the receiver within the tree hierarchy.
- [name](name.md) — Returns the name of the receiver.
- [objectValue](objectvalue.md) — Returns the object value of the receiver.
- [stringValue](stringvalue.md) — Returns the content of the receiver as a string value.
- [setURI:](../nsxmlnode-seturi.md) — Sets the URI of the receiver.
- [URI](uri.md) — Returns the URI associated with the receiver.
