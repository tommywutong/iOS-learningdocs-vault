---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/userinfo.json'
content_hash: 'sha256:51ed0a84fb6d8d92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# userInfo

<sub>Instance Property</sub>

A dictionary you use to customize the encoding process by providing contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency var userInfo: [CodingUserInfoKey : any Sendable] { get set }
```

## See Also

### Customizing Encoding

- [outputFormatting](outputformatting-swift.property.md) — A value that determines the readability, size, and element order of the encoded JSON object.
- [OutputFormatting](outputformatting-swift.struct.md) — The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [keyEncodingStrategy](keyencodingstrategy-swift.property.md) — A value that determines how to encode a  type’s coding keys as JSON keys.
- [KeyEncodingStrategy](keyencodingstrategy-swift.enum.md) — The values that determine how to encode a type’s coding keys as JSON keys.
