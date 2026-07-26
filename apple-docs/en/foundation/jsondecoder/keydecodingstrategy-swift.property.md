---
title: keyDecodingStrategy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/keydecodingstrategy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/keydecodingstrategy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/keydecodingstrategy-swift.property.json'
content_hash: 'sha256:4032f1d6ca017fd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# keyDecodingStrategy

<sub>Instance Property</sub>

A value that determines how to decode a type’s coding keys from JSON keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keyDecodingStrategy: JSONDecoder.KeyDecodingStrategy { get set }
```

## See Also

### Customizing Decoding

- [KeyDecodingStrategy](keydecodingstrategy-swift.enum.md) — The values that determine how to decode a type’s coding keys from JSON keys.
- [userInfo](userinfo.md) — A dictionary you use to customize the decoding process by providing contextual information.
- [allowsJSON5](allowsjson5.md) — Specifies that decoding supports the JSON5 syntax.
- [assumesTopLevelDictionary](assumestopleveldictionary.md) — Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.
