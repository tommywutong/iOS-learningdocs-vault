---
title: dataEncodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/dataencodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/dataencodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/dataencodingstrategy-swift.property.json'
content_hash: 'sha256:a6918b0a9991068c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# dataEncodingStrategy

<sub>Instance Property</sub>

The strategy that an encoder uses to encode raw data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dataEncodingStrategy: JSONEncoder.DataEncodingStrategy { get set }
```

## Discussion

The default strategy is the [JSONEncoder.DataEncodingStrategy.base64](dataencodingstrategy-swift.enum/base64.md) strategy.

## See Also

### Encoding Raw Data

- [DataEncodingStrategy](dataencodingstrategy-swift.enum.md) — The strategies for encoding raw data.
