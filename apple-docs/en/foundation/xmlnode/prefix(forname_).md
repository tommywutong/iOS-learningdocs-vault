---
title: 'prefix(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/prefix(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/prefix(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/prefix%28forname%3A%29.json'
content_hash: 'sha256:1e0861ab7eb3fc1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# prefix(forName:)

<sub>Type Method</sub>

Returns the prefix from the specified qualified name.

<sub>Mac Catalyst, macOS</sub>

```swift
class func prefix(forName name: String) -> String?
```

## Parameters

- `name` — A string that is a qualified name.

## Discussion

For example, if the qualified name is “bst:title”, this method returns “bst”.

## See Also

### Related Documentation

- [+ predefinedNamespaceForPrefix:](<predefinednamespace(forprefix_).md>) — Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.

### Managing Namespaces

- [localName](localname.md) — Returns the local name of the receiver.
- [+ localNameForName:](<localname(forname_).md>) — Returns the local name from the specified qualified name.
- [prefix](prefix.md) — Returns the prefix of the receiver’s name.
