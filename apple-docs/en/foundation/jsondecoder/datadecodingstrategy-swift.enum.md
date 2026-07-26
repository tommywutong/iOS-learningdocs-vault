---
title: JSONDecoder.DataDecodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/datadecodingstrategy-swift.enum.json'
content_hash: 'sha256:eaf2fe581bc9f8bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# JSONDecoder.DataDecodingStrategy

<sub>Enumeration</sub>

The strategies for decoding raw data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DataDecodingStrategy
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Base64 Decoding

- [JSONDecoder.DataDecodingStrategy.base64](datadecodingstrategy-swift.enum/base64.md) — The strategy that decodes data using Base 64 decoding.

### Custom Decoding

- [JSONDecoder.DataDecodingStrategy.custom(_:)](<datadecodingstrategy-swift.enum/custom(__).md>) — The strategy that decodes data using a user-defined function.

### Data Decoding

- [JSONDecoder.DataDecodingStrategy.deferredToData](datadecodingstrategy-swift.enum/deferredtodata.md) — The strategy that encodes data using the encoding specified by the data instance itself.

## See Also

### Decoding Raw Data

- [dataDecodingStrategy](datadecodingstrategy-swift.property.md) — The strategy that a decoder uses to decode raw data.
