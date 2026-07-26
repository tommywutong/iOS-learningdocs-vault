---
title: CodingKeyRepresentable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 15.4+, visionOS 1.0+, watchOS 8.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/codingkeyrepresentable
source_url: 'https://developer.apple.com/documentation/swift/codingkeyrepresentable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codingkeyrepresentable.json'
content_hash: 'sha256:38edd49e07100274'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CodingKeyRepresentable

<sub>Protocol</sub>

A type that can be converted to and from a coding key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CodingKeyRepresentable
```

## Overview

With a `CodingKeyRepresentable` type, you can losslessly convert between a custom type and a `CodingKey` type.

Conforming a type to `CodingKeyRepresentable` lets you opt in to encoding and decoding `Dictionary` values keyed by the conforming type to and from a keyed container, rather than encoding and decoding the dictionary as an unkeyed container of alternating key-value pairs.

## Relationships

- **Conforming Types**: [Int](int.md), [String](string.md)

## Topics

### Initializers

- [init(codingKey:)](<codingkeyrepresentable/init(codingkey_).md>)

### Instance Properties

- [codingKey](codingkeyrepresentable/codingkey.md)

## See Also

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Codable](codable.md) — A type that can convert itself into and out of an external representation.
- [Encodable](encodable.md) — A type that can encode itself to an external representation.
- [Decodable](decodable.md) — A type that can decode itself from an external representation.
- [CodingKey](codingkey.md) — A type that can be used as a key for encoding and decoding.
- [CodingUserInfoKey](codinguserinfokey.md) — A user-defined key for providing context during encoding and decoding.
