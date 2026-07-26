---
title: abortParsing()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/abortparsing()
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/abortparsing()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/abortparsing%28%29.json'
content_hash: 'sha256:8863751e23ab82ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# abortParsing()

<sub>Instance Method</sub>

Stops the parser object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func abortParsing()
```

## Discussion

If you invoke this method, the delegate, if it implements [- parser:parseErrorOccurred:](<../xmlparserdelegate/parser(__parseerroroccurred_).md>), is informed of the cancelled parsing operation.

## See Also

### Parsing

- [- parse](<parse().md>) — Starts the event-driven parsing operation.
- [parserError](parsererror.md) — An [NSError](../nserror.md) object from which you can obtain information about a parsing error.
