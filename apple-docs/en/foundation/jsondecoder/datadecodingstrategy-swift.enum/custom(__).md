---
title: 'JSONDecoder.DataDecodingStrategy.custom(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum/custom(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum/custom%28_%3A%29.json'
content_hash: 'sha256:21cda3cc8d272629'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONDecoder](../../jsondecoder.md) · [DataDecodingStrategy](../datadecodingstrategy-swift.enum.md)

# JSONDecoder.DataDecodingStrategy.custom(_:)

<sub>Case</sub>

The strategy that decodes data using a user-defined function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(@Sendable (any Decoder) throws -> Data)
```
