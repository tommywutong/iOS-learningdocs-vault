---
title: 'init(uuidString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuuid/init(uuidstring:)-8t9n3'
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid/init(uuidstring:)-8t9n3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid/init%28uuidstring%3A%29-8t9n3.json'
content_hash: 'sha256:ad187ac1022b584d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUUID](../nsuuid.md)

# init(uuidString:)

<sub>Initializer</sub>

Initializes a new UUID with the formatted string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(uuidString string: String)
```

## Parameters

- `string` — The source string containing the UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`.

## Return Value

A new UUID object. Returns `nil` for invalid strings.

## See Also

### Creating UUIDs

- [- init](<init().md>) — Initializes a new UUID with RFC 4122 version 4 random bytes.
- [- initWithUUIDBytes:](<init(uuidbytes_)-2p4d5.md>) — Initializes a new UUID with the given bytes.
