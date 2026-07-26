---
title: 'resolveNamespace(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/resolvenamespace(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/resolvenamespace(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/resolvenamespace%28forname%3A%29.json'
content_hash: 'sha256:731b3389bc55e044'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# resolveNamespace(forName:)

<sub>Instance Method</sub>

Returns the namespace node with the prefix matching the given qualified name.

<sub>Mac Catalyst, macOS</sub>

```swift
func resolveNamespace(forName name: String) -> XMLNode?
```

## Parameters

- `name` — A string that is the qualified name for a namespace (a qualified name is prefix plus local name).

## Return Value

An [XMLNode](../xmlnode.md) object of kind [NSXMLNamespaceKind](../xmlnode/kind-swift.enum/namespace.md) or `nil` if there is no matching namespace node.

## Discussion

The method looks in the entire namespace chain for the prefix.

## See Also

### Handling Namespaces

- [- addNamespace:](<addnamespace(__).md>) — Adds a namespace node to the receiver.
- [namespaces](namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- namespaceForPrefix:](<namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- removeNamespaceForPrefix:](<removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.
