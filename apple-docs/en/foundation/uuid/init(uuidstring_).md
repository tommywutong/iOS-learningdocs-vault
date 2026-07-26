---
title: 'init(uuidString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 6.0+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/uuid/init(uuidstring:)'
source_url: 'https://developer.apple.com/documentation/foundation/uuid/init(uuidstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/uuid/init%28uuidstring%3A%29.json'
content_hash: 'sha256:785c9b4466f81d81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UUID](../uuid.md)

# init(uuidString:)

<sub>Initializer</sub>

Creates a UUID from a string representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(uuidString string: String)
```

## Parameters

- `string` — The string representation of a UUID, such as `E621E1F8-C36C-495A-93FC-0C247A3E6E5F`.

## Discussion

Returns `nil` if the string isn’t a valid UUID representation.

## See Also

### Creating UUIDs

- [init()](<init().md>) — Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuid:)](<init(uuid_).md>) — Creates a UUID from the uuid C-language structure.
