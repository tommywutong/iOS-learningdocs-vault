---
title: columnNumber
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/columnnumber
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/columnnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/columnnumber.json'
content_hash: 'sha256:7997aa04723a8676'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# columnNumber

<sub>Instance Property</sub>

The column number of the XML document being processed by the parser.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var columnNumber: Int { get }
```

## Discussion

The column refers to the nesting level of the XML elements in the document. You may access this property once a parsing operation has begun or after an error occurs.

## See Also

### Obtaining Parser State

- [lineNumber](linenumber.md) — The line number of the XML document being processed by the parser.
- [publicID](publicid.md) — The public identifier of the external entity referenced in the XML document.
- [systemID](systemid.md) — The system identifier of the external entity referenced in the XML document.
