---
title: UUID
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuuid/uuid
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid/uuid.json'
content_hash: 'sha256:58107362674ee541'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUUID](../nsuuid.md)

# UUID

<sub>Type Method</sub>

Create and returns a new UUID with RFC 4122 version 4 random bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) UUID;
```

## Return Value

A new UUID object.

## See Also

### Creating UUIDs

- [- init](<init().md>) — Initializes a new UUID with RFC 4122 version 4 random bytes.
- [- initWithUUIDString:](<init(uuidstring_)-8t9n3.md>) — Initializes a new UUID with the formatted string.
- [- initWithUUIDBytes:](<init(uuidbytes_)-2p4d5.md>) — Initializes a new UUID with the given bytes.
