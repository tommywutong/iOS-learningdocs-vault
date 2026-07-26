---
title: xmlData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/xmldata
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/xmldata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/xmldata.json'
content_hash: 'sha256:68934571b4433fdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# xmlData

<sub>Instance Property</sub>

Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

<sub>Mac Catalyst, macOS</sub>

```swift
var xmlData: Data { get }
```

## Discussion

This method invokes [- XMLDataWithOptions:](<xmldata(options_).md>) with an option of `NSXMLNodeOptionsNone`. The encoding used is based on the value returned from [characterEncoding](characterencoding.md) or UTF-8 if no valid encoding is returned by that method.

## See Also

### Writing a Document as XML Data

- [- XMLDataWithOptions:](<xmldata(options_).md>) — Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.
