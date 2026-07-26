---
title: nonConformingFloatEncodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/nonconformingfloatencodingstrategy-swift.property.json'
content_hash: 'sha256:54e4dda13c75f1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# nonConformingFloatEncodingStrategy

<sub>Instance Property</sub>

The strategy used by an encoder when it encounters exceptional floating-point values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonConformingFloatEncodingStrategy: JSONEncoder.NonConformingFloatEncodingStrategy { get set }
```

## Discussion

The default strategy is the [JSONEncoder.NonConformingFloatEncodingStrategy.throw](nonconformingfloatencodingstrategy-swift.enum/throw.md) strategy.

## See Also

### Encoding Exceptional Numbers

- [NonConformingFloatEncodingStrategy](nonconformingfloatencodingstrategy-swift.enum.md) — The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.
