---
title: xmlString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/xmlstring
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/xmlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/xmlstring.json'
content_hash: 'sha256:97b81da5878bdb9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# xmlString

<sub>Instance Property</sub>

Returns the string representation of the receiver as it would appear in an XML document.

<sub>Mac Catalyst, macOS</sub>

```swift
var xmlString: String { get }
```

## Discussion

The returned string includes the string representations of all children. This method invokes [- XMLStringWithOptions:](<xmlstring(options_).md>) with an `options` argument of `NSXMLNodeOptionsNone`.

## See Also

### Emitting Node Content

- [- XMLStringWithOptions:](<xmlstring(options_).md>) — Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [- canonicalXMLStringPreservingComments:](<canonicalxmlstringpreservingcomments(__).md>) — Returns a string object encapsulating the receiver’s XML in canonical form.
- [description](description.md)
