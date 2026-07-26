---
title: 'init(uuid:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 6.0+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/uuid/init(uuid:)'
source_url: 'https://developer.apple.com/documentation/foundation/uuid/init(uuid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/uuid/init%28uuid%3A%29.json'
content_hash: 'sha256:b77d95ceda499ce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UUID](../uuid.md)

# init(uuid:)

<sub>Initializer</sub>

Creates a UUID from the uuid C-language structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uuid: uuid_t)
```

## Parameters

- `uuid` — The C-language structure of a UUID.

## See Also

### Creating UUIDs

- [init()](<init().md>) — Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuidString:)](<init(uuidstring_).md>) — Creates a UUID from a string representation.
