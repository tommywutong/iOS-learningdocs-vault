---
title: FullyInhabited
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/fullyinhabited
source_url: 'https://developer.apple.com/documentation/swift/fullyinhabited'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fullyinhabited.json'
content_hash: 'sha256:737b9916c41469fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# FullyInhabited

<sub>Type Alias</sub>

A protocol for types whose memory can safely be written as or read from raw bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias FullyInhabited = ConvertibleFromBytes & ConvertibleToBytes
```

## See Also

### Safe Access to Raw Bytes

- [ConvertibleFromBytes](convertiblefrombytes.md) — A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [ConvertibleToBytes](convertibletobytes.md) — A protocol for types whose memory can safely be read as individual raw bytes.
- [ByteOrder](byteorder.md) — A byte ordering in memory. _(beta)_
- [bitCast(_:to:)](<bitcast(__to_).md>) — Returns the bits of the given instance, interpreted as having the specified type.
