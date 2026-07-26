---
title: 'removeNamespace(forPrefix:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/removenamespace(forprefix:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/removenamespace(forprefix:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/removenamespace%28forprefix%3A%29.json'
content_hash: 'sha256:42b0192e594eb8e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# removeNamespace(forPrefix:)

<sub>Instance Method</sub>

Removes a namespace node that is identified by a given prefix.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeNamespace(forPrefix name: String)
```

## Parameters

- `name` — A string that is the prefix for a namespace.

## Discussion

The removed XML node object is removed.

## See Also

### Handling Namespaces

- [- addNamespace:](<addnamespace(__).md>) — Adds a namespace node to the receiver.
- [namespaces](namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- namespaceForPrefix:](<namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- resolveNamespaceForName:](<resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
- [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>) — Returns the prefix associated with the specified URI.
