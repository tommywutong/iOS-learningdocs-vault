---
title: Decoder
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decoder
source_url: 'https://developer.apple.com/documentation/swift/decoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decoder.json'
content_hash: 'sha256:e606727643143c71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Decoder

<sub>Protocol</sub>

A type that can decode values from a native format into in-memory representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Decoder
```

## Topics

### Instance Properties

- [codingPath](decoder/codingpath.md) — The path of coding keys taken to get to this point in decoding.
- [userInfo](decoder/userinfo.md) — Any contextual information set by the user for decoding.

### Instance Methods

- [container(keyedBy:)](<decoder/container(keyedby_).md>) — Returns the data stored in this decoder as represented in a container keyed by the given key type.
- [singleValueContainer()](<decoder/singlevaluecontainer().md>) — Returns the data stored in this decoder as represented in a container appropriate for holding a single primitive value.
- [unkeyedContainer()](<decoder/unkeyedcontainer().md>) — Returns the data stored in this decoder as represented in a container appropriate for holding values with no keys.

## See Also

### Encoders and Decoders

- [Encoder](encoder.md) — A type that can encode values into a native format for external representation.
- [EncodingError](encodingerror.md) — An error that occurs during the encoding of a value.
- [DecodingError](decodingerror.md) — An error that occurs during the decoding of a value.
