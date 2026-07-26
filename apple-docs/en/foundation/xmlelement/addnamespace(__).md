---
title: 'addNamespace(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/addnamespace(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/addnamespace(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/addnamespace%28_%3A%29.json'
content_hash: 'sha256:1d123da6e58366bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# addNamespace(_:)

<sub>Instance Method</sub>

Adds a namespace node to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func addNamespace(_ aNamespace: XMLNode)
```

## Parameters

- `aNamespace` — An XML node object of kind [NSXMLNamespaceKind](../xmlnode/kind-swift.enum/namespace.md). If the receiver already has a namespace with the same name, `aNamespace` is not added.

## See Also

### Handling Namespaces

- [namespaces](namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- namespaceForPrefix:](<namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- removeNamespaceForPrefix:](<removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolveNamespaceForName:](<resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
- [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.
