---
title: JSONEncoder.DataEncodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum.json'
content_hash: 'sha256:bc7c9b75d0788bd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# JSONEncoder.DataEncodingStrategy

<sub>Enumeration</sub>

The strategies for encoding raw data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DataEncodingStrategy
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Base64 Encoding

- [JSONEncoder.DataEncodingStrategy.base64](dataencodingstrategy-swift.enum/base64.md) — The strategy that encodes data using Base 64 encoding.

### Custom Encoding

- [JSONEncoder.DataEncodingStrategy.custom(_:)](<dataencodingstrategy-swift.enum/custom(__).md>) — The strategy that encodes data using a user-defined function.

### Data Encoding

- [JSONEncoder.DataEncodingStrategy.deferredToData](dataencodingstrategy-swift.enum/deferredtodata.md) — The strategy that encodes data using the encoding specified by the data instance itself.

## See Also

### Encoding Raw Data

- [dataEncodingStrategy](dataencodingstrategy-swift.property.md) — The strategy that an encoder uses to encode raw data.
