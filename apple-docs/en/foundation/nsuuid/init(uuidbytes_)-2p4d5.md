---
title: 'init(uuidBytes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuuid/init(uuidbytes:)-2p4d5'
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid/init(uuidbytes:)-2p4d5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid/init%28uuidbytes%3A%29-2p4d5.json'
content_hash: 'sha256:c195a60c0c3ca161'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUUID](../nsuuid.md)

# init(uuidBytes:)

<sub>Initializer</sub>

Initializes a new UUID with the given bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(uuidBytes bytes: UnsafePointer<UInt8>?)
```

## Parameters

- `bytes` — Raw UUID bytes to use to create the UUID.

## Return Value

A new UUID object.

## See Also

### Creating UUIDs

- [- init](<init().md>) — Initializes a new UUID with RFC 4122 version 4 random bytes.
- [- initWithUUIDString:](<init(uuidstring_)-8t9n3.md>) — Initializes a new UUID with the formatted string.
