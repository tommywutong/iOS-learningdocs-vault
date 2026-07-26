---
title: JSONEncoder.KeyEncodingStrategy.useDefaultKeys
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/usedefaultkeys.json'
content_hash: 'sha256:8ad1591fb04bc8a5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONEncoder](../../jsonencoder.md) · [KeyEncodingStrategy](../keyencodingstrategy-swift.enum.md)

# JSONEncoder.KeyEncodingStrategy.useDefaultKeys

<sub>Case</sub>

A key encoding strategy that doesn’t change key names during encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case useDefaultKeys
```

## Discussion

The [JSONEncoder.KeyEncodingStrategy.useDefaultKeys](usedefaultkeys.md) strategy is the strategy used if you don’t specify one.

> [!note] Note
> If you use a nested `CodingKeys` enumeration to define custom key names, this strategy continues to use those names rather than reverting back to the original property names. Nested `CodingKeys` enumerations are described in [Encoding and Decoding Custom Types](../../encoding-and-decoding-custom-types.md).

## See Also

### Built-in Encoding

- [JSONEncoder.KeyEncodingStrategy.convertToSnakeCase](converttosnakecase.md) — A key encoding strategy that converts camel-case keys to snake-case keys.
