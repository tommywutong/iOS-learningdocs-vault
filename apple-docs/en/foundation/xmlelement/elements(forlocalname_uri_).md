---
title: 'elements(forLocalName:uri:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/elements(forlocalname:uri:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/elements(forlocalname:uri:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/elements%28forlocalname%3Auri%3A%29.json'
content_hash: 'sha256:e829f154536e71f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# elements(forLocalName:uri:)

<sub>Instance Method</sub>

Returns the child element nodes (as `NSXMLElement` objects) of the receiver that are matched with the specified local name and URI.

<sub>Mac Catalyst, macOS</sub>

```swift
func elements(forLocalName localName: String, uri URI: String?) -> [XMLElement]
```

## Parameters

- `localName` — A string specifying a local name of an element.

- `URI` — A string specifying a URI associated with an element.

## Return Value

An array of `NSXMLElement` objects or an empty array if no matching children could be found.

## See Also

### Obtaining Child Elements

- [- elementsForName:](<elements(forname_).md>) — Returns the child element nodes (as `NSXMLElement` objects) of the receiver that have a specified name.
