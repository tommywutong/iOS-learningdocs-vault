---
title: namespaces
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlelement/namespaces
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/namespaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/namespaces.json'
content_hash: 'sha256:e39ce4ad84b29237'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# namespaces

<sub>Instance Property</sub>

Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.

<sub>Mac Catalyst, macOS</sub>

```swift
var namespaces: [XMLNode]? { get set }
```

## Parameters

- `namespaces` — An array of [XMLNode](../xmlnode.md) objects of kind [NSXMLNamespaceKind](../xmlnode/kind-swift.enum/namespace.md).  If there are namespace nodes with the same prefix, the first attribute with that prefix is used. Send this message with `namespaces` as `nil` to remove all namespace nodes.

## See Also

### Handling Namespaces

- [- addNamespace:](<addnamespace(__).md>) — Adds a namespace node to the receiver.
- [- namespaceForPrefix:](<namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- removeNamespaceForPrefix:](<removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolveNamespaceForName:](<resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
- [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.
