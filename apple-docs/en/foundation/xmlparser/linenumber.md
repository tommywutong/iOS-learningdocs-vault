---
title: lineNumber
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/linenumber
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/linenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/linenumber.json'
content_hash: 'sha256:16f57f7f53a632ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# lineNumber

<sub>Instance Property</sub>

The line number of the XML document being processed by the parser.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lineNumber: Int { get }
```

## Discussion

You may access this property once a parsing operation has begun or after an error occurs.

## See Also

### Obtaining Parser State

- [columnNumber](columnnumber.md) — The column number of the XML document being processed by the parser.
- [publicID](publicid.md) — The public identifier of the external entity referenced in the XML document.
- [systemID](systemid.md) — The system identifier of the external entity referenced in the XML document.
