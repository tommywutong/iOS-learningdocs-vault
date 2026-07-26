---
title: parserError
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/parsererror
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/parsererror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/parsererror.json'
content_hash: 'sha256:d32261d668f85cbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# parserError

<sub>Instance Property</sub>

An [NSError](../nserror.md) object from which you can obtain information about a parsing error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var parserError: (any Error)? { get }
```

## Discussion

You may access this property after a parsing operation abnormally terminates to determine the cause of error.

## See Also

### Parsing

- [- parse](<parse().md>) — Starts the event-driven parsing operation.
- [- abortParsing](<abortparsing().md>) — Stops the parser object.
