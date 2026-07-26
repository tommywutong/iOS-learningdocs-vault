---
title: localName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/localname
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/localname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/localname.json'
content_hash: 'sha256:03fa13142eceaa75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# localName

<sub>Instance Property</sub>

Returns the local name of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var localName: String? { get }
```

## Return Value

A string containing the local name of the receiver.

## Discussion

The local name is the part of a node name that follows a namespace-qualifying colon or the full name if there is no colon. For example, “chapter” is the local name in the qualified name “acme:chapter”.

## See Also

### Managing Namespaces

- [+ localNameForName:](<localname(forname_).md>) — Returns the local name from the specified qualified name.
- [prefix](prefix.md) — Returns the prefix of the receiver’s name.
- [+ prefixForName:](<prefix(forname_).md>) — Returns the prefix from the specified qualified name.
