---
title: Encoding, Decoding, and Serialization
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/encoding-decoding-and-serialization
source_url: 'https://developer.apple.com/documentation/swift/encoding-decoding-and-serialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encoding-decoding-and-serialization.json'
content_hash: 'sha256:e1a7f1eaf1d12e5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Encoding, Decoding, and Serialization

<sub>API Collection</sub>

Serialize and deserialize instances of your types with implicit or customized encoding.

## Topics

### Custom Encoding and Decoding

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [Codable](codable.md) — A type that can convert itself into and out of an external representation.
- [Encodable](encodable.md) — A type that can encode itself to an external representation.
- [Decodable](decodable.md) — A type that can decode itself from an external representation.
- [CodingKey](codingkey.md) — A type that can be used as a key for encoding and decoding.
- [CodingKeyRepresentable](codingkeyrepresentable.md) — A type that can be converted to and from a coding key.
- [CodingUserInfoKey](codinguserinfokey.md) — A user-defined key for providing context during encoding and decoding.

### Encoders and Decoders

- [Encoder](encoder.md) — A type that can encode values into a native format for external representation.
- [Decoder](decoder.md) — A type that can decode values from a native format into in-memory representations.
- [EncodingError](encodingerror.md) — An error that occurs during the encoding of a value.
- [DecodingError](decodingerror.md) — An error that occurs during the decoding of a value.

### Encoding Containers

- [SingleValueEncodingContainer](singlevalueencodingcontainer.md) — A container that can support the storage and direct encoding of a single non-keyed value.
- [KeyedEncodingContainer](keyedencodingcontainer.md) — A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [UnkeyedEncodingContainer](unkeyedencodingcontainer.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.

### Decoding Containers

- [KeyedDecodingContainer](keyeddecodingcontainer.md) — A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [SingleValueDecodingContainer](singlevaluedecodingcontainer.md) — A container that can support the storage and direct decoding of a single nonkeyed value.
- [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [UnkeyedDecodingContainer](unkeyeddecodingcontainer.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.

## See Also

### Tools for Your Types

- [Basic Behaviors](basic-behaviors.md) — Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Initialization with Literals](initialization-with-literals.md) — Allow values of your type to be expressed using different kinds of literals.
