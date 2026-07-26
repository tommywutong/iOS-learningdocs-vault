---
title: 'localName(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/localname(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/localname(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/localname%28forname%3A%29.json'
content_hash: 'sha256:0b7abfece653481e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# localName(forName:)

<sub>Type Method</sub>

Returns the local name from the specified qualified name.

<sub>Mac Catalyst, macOS</sub>

```swift
class func localName(forName name: String) -> String
```

## Parameters

- `name` — A string that is a qualified name.

## Discussion

For example, if the qualified name is “bst:title”, this method returns “title”.

## See Also

### Related Documentation

- [+ predefinedNamespaceForPrefix:](<predefinednamespace(forprefix_).md>) — Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.

### Managing Namespaces

- [localName](localname.md) — Returns the local name of the receiver.
- [prefix](prefix.md) — Returns the prefix of the receiver’s name.
- [+ prefixForName:](<prefix(forname_).md>) — Returns the prefix from the specified qualified name.
