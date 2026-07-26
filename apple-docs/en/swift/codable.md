---
title: Codable
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/codable
source_url: 'https://developer.apple.com/documentation/swift/codable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codable.json'
content_hash: 'sha256:a1eab2067137e2d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Codable

<sub>Type Alias</sub>

A type that can convert itself into and out of an external representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Codable = Decodable & Encodable
```

## Discussion

`Codable` is a type alias for the `Encodable` and `Decodable` protocols. When you use `Codable` as a type or a generic constraint, it matches any type that conforms to both protocols.

## See Also

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Encodable](encodable.md) — A type that can encode itself to an external representation.
- [Decodable](decodable.md) — A type that can decode itself from an external representation.
- [CodingKey](codingkey.md) — A type that can be used as a key for encoding and decoding.
- [CodingKeyRepresentable](codingkeyrepresentable.md) — A type that can be converted to and from a coding key.
- [CodingUserInfoKey](codinguserinfokey.md) — A user-defined key for providing context during encoding and decoding.
