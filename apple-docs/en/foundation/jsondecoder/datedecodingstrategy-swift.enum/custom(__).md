---
title: 'JSONDecoder.DateDecodingStrategy.custom(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum/custom(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datedecodingstrategy-swift.enum/custom%28_%3A%29.json'
content_hash: 'sha256:27f2394f4f095c5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONDecoder](../../jsondecoder.md) · [DateDecodingStrategy](../datedecodingstrategy-swift.enum.md)

# JSONDecoder.DateDecodingStrategy.custom(_:)

<sub>Case</sub>

The strategy that formats custom dates by calling a user-defined function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(@Sendable (any Decoder) throws -> Date)
```

## See Also

### Custom Formats

- [JSONDecoder.DateDecodingStrategy.formatted(_:)](<formatted(__).md>) — The strategy that defers formatting settings to a supplied date formatter.
