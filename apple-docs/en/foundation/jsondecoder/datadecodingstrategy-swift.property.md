---
title: dataDecodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/datadecodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datadecodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datadecodingstrategy-swift.property.json'
content_hash: 'sha256:016835d7a56c7fa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# dataDecodingStrategy

<sub>Instance Property</sub>

The strategy that a decoder uses to decode raw data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dataDecodingStrategy: JSONDecoder.DataDecodingStrategy { get set }
```

## Discussion

The default strategy is the [JSONDecoder.DataDecodingStrategy.base64](datadecodingstrategy-swift.enum/base64.md) strategy.

## See Also

### Decoding Raw Data

- [DataDecodingStrategy](datadecodingstrategy-swift.enum.md) — The strategies for decoding raw data.
