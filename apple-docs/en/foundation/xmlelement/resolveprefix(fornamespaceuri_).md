---
title: 'resolvePrefix(forNamespaceURI:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/resolveprefix(fornamespaceuri:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/resolveprefix(fornamespaceuri:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/resolveprefix%28fornamespaceuri%3A%29.json'
content_hash: 'sha256:532fc2bd315c329f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# resolvePrefix(forNamespaceURI:)

<sub>Instance Method</sub>

Returns the prefix associated with the specified URI.

<sub>Mac Catalyst, macOS</sub>

```swift
func resolvePrefix(forNamespaceURI namespaceURI: String) -> String?
```

## Parameters

- `namespaceURI` — A string identifying the URI associated with the namespace.

## Return Value

A string that is the matching prefix or `nil` if it finds no matching prefix.

## Discussion

The method looks in the entire namespace chain for the URI.

## See Also

### Handling Namespaces

- [- addNamespace:](<addnamespace(__).md>) — Adds a namespace node to the receiver.
- [namespaces](namespaces.md) — Sets all of the namespace nodes of the receiver at once, replacing any existing namespace nodes.
- [- namespaceForPrefix:](<namespace(forprefix_).md>) — Returns the namespace node with a specified prefix.
- [- removeNamespaceForPrefix:](<removenamespace(forprefix_).md>) — Removes a namespace node that is identified by a given prefix.
- [- resolveNamespaceForName:](<resolvenamespace(forname_).md>) — Returns the namespace node with the prefix matching the given qualified name.
