---
title: JSONEncoder.KeyEncodingStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum.json'
content_hash: 'sha256:e18e57ce4d2904b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# JSONEncoder.KeyEncodingStrategy

<sub>Enumeration</sub>

The values that determine how to encode a type’s coding keys as JSON keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeyEncodingStrategy
```

## Overview

> [!note] Note
> Key encoding strategies other than [JSONEncoder.KeyEncodingStrategy.useDefaultKeys](keyencodingstrategy-swift.enum/usedefaultkeys.md) may have a noticeable performance cost because those strategies may inspect and transform each key.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Built-in Encoding

- [JSONEncoder.KeyEncodingStrategy.convertToSnakeCase](keyencodingstrategy-swift.enum/converttosnakecase.md) — A key encoding strategy that converts camel-case keys to snake-case keys.
- [JSONEncoder.KeyEncodingStrategy.useDefaultKeys](keyencodingstrategy-swift.enum/usedefaultkeys.md) — A key encoding strategy that doesn’t change key names during encoding.

### Custom Encoding

- [JSONEncoder.KeyEncodingStrategy.custom(_:)](<keyencodingstrategy-swift.enum/custom(__).md>) — A key encoding strategy defined by the closure you supply.

## See Also

### Customizing Encoding

- [outputFormatting](outputformatting-swift.property.md) — A value that determines the readability, size, and element order of the encoded JSON object.
- [OutputFormatting](outputformatting-swift.struct.md) — The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [keyEncodingStrategy](keyencodingstrategy-swift.property.md) — A value that determines how to encode a  type’s coding keys as JSON keys.
- [userInfo](userinfo.md) — A dictionary you use to customize the encoding process by providing contextual information.
