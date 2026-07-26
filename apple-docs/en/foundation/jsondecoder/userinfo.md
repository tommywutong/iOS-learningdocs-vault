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
doc_path: /documentation/foundation/jsondecoder/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/userinfo.json'
content_hash: 'sha256:e4c16e5c0d38235c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# userInfo

<sub>Instance Property</sub>

A dictionary you use to customize the decoding process by providing contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency var userInfo: [CodingUserInfoKey : any Sendable] { get set }
```

## See Also

### Customizing Decoding

- [keyDecodingStrategy](keydecodingstrategy-swift.property.md) — A value that determines how to decode a type’s coding keys from JSON keys.
- [KeyDecodingStrategy](keydecodingstrategy-swift.enum.md) — The values that determine how to decode a type’s coding keys from JSON keys.
- [allowsJSON5](allowsjson5.md) — Specifies that decoding supports the JSON5 syntax.
- [assumesTopLevelDictionary](assumestopleveldictionary.md) — Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.
