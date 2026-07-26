---
title: 'namespace(forPrefix:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/namespace(forprefix:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/namespace(forprefix:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/namespace%28forprefix%3A%29.json'
content_hash: 'sha256:8144080330e72aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# namespace(forPrefix:)

<sub>Instance Method</sub>

Returns the namespace node with a specified prefix.

<sub>Mac Catalyst, macOS</sub>

```swift
func namespace(forPrefix name: String) -> XMLNode?
```

## Parameters

- `name` — A string specifying a namespace prefix.

## Return Value

An [XMLNode](../xmlnode.md) object of kind [NSXMLNamespaceKind](../xmlnode/kind-swift.enum/namespace.md) or `nil` if there is no namespace node with that prefix.

## See Also

### Handling Namespaces

- [- addNamespace:](<addnamespace(__).md>) — Adds a namespace node to the receiver.
- [namespaces](namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- removeNamespaceForPrefix:](<removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolveNamespaceForName:](<resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
- [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.
