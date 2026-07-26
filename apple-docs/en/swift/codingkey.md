---
title: CodingKey
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/codingkey
source_url: 'https://developer.apple.com/documentation/swift/codingkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codingkey.json'
content_hash: 'sha256:a59f46242636f3a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CodingKey

<sub>Protocol</sub>

A type that can be used as a key for encoding and decoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CodingKey : CustomDebugStringConvertible, CustomStringConvertible, Sendable
```

## Relationships

- **Inherits From**: [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomStringConvertible](customstringconvertible.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(intValue:)](<codingkey/init(intvalue_).md>) — Creates a new instance from the specified integer.
- [init(stringValue:)](<codingkey/init(stringvalue_).md>) — Creates a new instance from the given string.

### Instance Properties

- [intValue](codingkey/intvalue.md) — The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [stringValue](codingkey/stringvalue.md) — The string to use in a named collection (e.g. a string-keyed dictionary).

## See Also

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Codable](codable.md) — A type that can convert itself into and out of an external representation.
- [Encodable](encodable.md) — A type that can encode itself to an external representation.
- [Decodable](decodable.md) — A type that can decode itself from an external representation.
- [CodingKeyRepresentable](codingkeyrepresentable.md) — A type that can be converted to and from a coding key.
- [CodingUserInfoKey](codinguserinfokey.md) — A user-defined key for providing context during encoding and decoding.
