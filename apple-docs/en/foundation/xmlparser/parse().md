---
title: parse()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/parse()
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/parse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/parse%28%29.json'
content_hash: 'sha256:ff2d0e14efdc9453'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# parse()

<sub>Instance Method</sub>

Starts the event-driven parsing operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse() -> Bool
```

## Return Value

[true](../../swift/true.md) if the parsing operation succeeds; [false](../../swift/false.md) if an error occurs or if the parsing operation aborts.

## See Also

### Parsing

- [- abortParsing](<abortparsing().md>) — Stops the parser object.
- [parserError](parsererror.md) — An [NSError](../nserror.md) object from which you can obtain information about a parsing error.
