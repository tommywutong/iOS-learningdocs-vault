---
title: 'xmlString(options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/xmlstring(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/xmlstring(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/xmlstring%28options%3A%29.json'
content_hash: 'sha256:d997f7aec7635c45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# xmlString(options:)

<sub>Instance Method</sub>

Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.

<sub>Mac Catalyst, macOS</sub>

```swift
func xmlString(options: XMLNode.Options = []) -> String
```

## Parameters

- `options` — One or more `enum` constants identifying an output option; bit-OR multiple constants together.  See Constants for a list of valid constants for specifying output options.

## Discussion

The returned string includes the string representations of all children.

## See Also

### Emitting Node Content

- [XMLString](xmlstring.md) — Returns the string representation of the receiver as it would appear in an XML document.
- [- canonicalXMLStringPreservingComments:](<canonicalxmlstringpreservingcomments(__).md>) — Returns a string object encapsulating the receiver’s XML in canonical form.
- [description](description.md)
