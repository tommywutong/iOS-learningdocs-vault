---
title: 'JSONEncoder.DateEncodingStrategy.custom(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum/custom(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/dateencodingstrategy-swift.enum/custom%28_%3A%29.json'
content_hash: 'sha256:275ec72202969dba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONEncoder](../../jsonencoder.md) · [DateEncodingStrategy](../dateencodingstrategy-swift.enum.md)

# JSONEncoder.DateEncodingStrategy.custom(_:)

<sub>Case</sub>

The strategy that formats custom dates by calling a user-defined function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(@Sendable (Date, any Encoder) throws -> Void)
```

## Parameters

- `custom` — A closure that receives the data to encode and the encoder instance to encode to.

## Discussion

If the user-defined function throws, the error propagates upward.

If the user-defined function doesn’t perform any encoding at all, the encoder produces an empty JSON object instead.

## See Also

### Custom Formats

- [JSONEncoder.DateEncodingStrategy.formatted(_:)](<formatted(__).md>) — The strategy that defers formatting settings to a supplied date formatter.
