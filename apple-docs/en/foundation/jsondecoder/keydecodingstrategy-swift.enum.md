---
title: JSONDecoder.KeyDecodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum.json'
content_hash: 'sha256:685fa22e4926b9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# JSONDecoder.KeyDecodingStrategy

<sub>Enumeration</sub>

The values that determine how to decode a type’s coding keys from JSON keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeyDecodingStrategy
```

## Overview

> [!note] Note
> Key decoding strategies other than [JSONDecoder.KeyDecodingStrategy.useDefaultKeys](keydecodingstrategy-swift.enum/usedefaultkeys.md) may have a noticeable performance cost because those strategies may inspect and transform each key.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Built-in Decoding

- [JSONDecoder.KeyDecodingStrategy.convertFromSnakeCase](keydecodingstrategy-swift.enum/convertfromsnakecase.md) — A key decoding strategy that converts snake-case keys to camel-case keys.
- [JSONDecoder.KeyDecodingStrategy.useDefaultKeys](keydecodingstrategy-swift.enum/usedefaultkeys.md) — A key decoding strategy that doesn’t change key names during decoding.

### Custom Decoding

- [JSONDecoder.KeyDecodingStrategy.custom(_:)](<keydecodingstrategy-swift.enum/custom(__).md>) — A key decoding strategy defined by the closure you supply.

## See Also

### Customizing Decoding

- [keyDecodingStrategy](keydecodingstrategy-swift.property.md) — A value that determines how to decode a type’s coding keys from JSON keys.
- [userInfo](userinfo.md) — A dictionary you use to customize the decoding process by providing contextual information.
- [allowsJSON5](allowsjson5.md) — Specifies that decoding supports the JSON5 syntax.
- [assumesTopLevelDictionary](assumestopleveldictionary.md) — Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.
