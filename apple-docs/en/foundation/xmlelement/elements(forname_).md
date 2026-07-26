---
title: 'elements(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/elements(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/elements(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/elements%28forname%3A%29.json'
content_hash: 'sha256:c9d3e5ac4b6da822'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# elements(forName:)

<sub>Instance Method</sub>

Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.

<sub>Mac Catalyst, macOS</sub>

```swift
func elements(forName name: String) -> [XMLElement]
```

## Parameters

- `name` — A string specifying the name of the child element nodes to find and return. If `name` is a qualified name, then this method invokes [- elementsForLocalName:URI:](<elements(forlocalname_uri_).md>) with the URI parameter set to the URI associated with the prefix. Otherwise comparison is based on string equality of the qualified or non-qualified name.

## Return Value

An array of of `NSXMLElement` objects or an empty array if no matching children can be found.

## See Also

### Obtaining Child Elements

- [- elementsForLocalName:URI:](<elements(forlocalname_uri_).md>) — Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.
