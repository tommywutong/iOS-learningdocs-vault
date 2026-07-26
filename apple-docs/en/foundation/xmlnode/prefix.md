---
title: prefix
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/prefix
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/prefix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/prefix.json'
content_hash: 'sha256:e6028c722615cc52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# prefix

<sub>Instance Property</sub>

Returns the prefix of the receiver’s name.

<sub>Mac Catalyst, macOS</sub>

```swift
var prefix: String? { get }
```

## Return Value

A string containing the receiver’s prefix. This method returns an empty string if the receiver’s name is not qualified by a namespace.

## Discussion

The prefix is the part of a namespace-qualified name that precedes the colon. For example, “acme” is the prefix in the qualified name “acme:chapter”.

## See Also

### Managing Namespaces

- [localName](localname.md) — Returns the local name of the receiver.
- [+ localNameForName:](<localname(forname_).md>) — Returns the local name from the specified qualified name.
- [+ prefixForName:](<prefix(forname_).md>) — Returns the prefix from the specified qualified name.
