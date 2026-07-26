---
title: Encoder
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/encoder
source_url: 'https://developer.apple.com/documentation/swift/encoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encoder.json'
content_hash: 'sha256:6309972afd622f78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Encoder

<sub>Protocol</sub>

A type that can encode values into a native format for external representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Encoder
```

## Topics

### Instance Properties

- [codingPath](encoder/codingpath.md) — The path of coding keys taken to get to this point in encoding.
- [userInfo](encoder/userinfo.md) — Any contextual information set by the user for encoding.

### Instance Methods

- [container(keyedBy:)](<encoder/container(keyedby_).md>) — Returns an encoding container appropriate for holding multiple values keyed by the given key type.
- [singleValueContainer()](<encoder/singlevaluecontainer().md>) — Returns an encoding container appropriate for holding a single primitive value.
- [unkeyedContainer()](<encoder/unkeyedcontainer().md>) — Returns an encoding container appropriate for holding multiple unkeyed values.

## See Also

### Encoders and Decoders

- [Decoder](decoder.md) — A type that can decode values from a native format into in-memory representations.
- [EncodingError](encodingerror.md) — An error that occurs during the encoding of a value.
- [DecodingError](decodingerror.md) — An error that occurs during the decoding of a value.
