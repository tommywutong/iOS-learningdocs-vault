---
title: publicID
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/publicid
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/publicid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/publicid.json'
content_hash: 'sha256:0d78a274c0fca1fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# publicID

<sub>Instance Property</sub>

The public identifier of the external entity referenced in the XML document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var publicID: String? { get }
```

## Discussion

You may access this property once a parsing operation has begun or after an error occurs.

## See Also

### Obtaining Parser State

- [columnNumber](columnnumber.md) — The column number of the XML document being processed by the parser.
- [lineNumber](linenumber.md) — The line number of the XML document being processed by the parser.
- [systemID](systemid.md) — The system identifier of the external entity referenced in the XML document.
