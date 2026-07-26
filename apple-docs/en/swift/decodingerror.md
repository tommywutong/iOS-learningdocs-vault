---
title: DecodingError
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decodingerror
source_url: 'https://developer.apple.com/documentation/swift/decodingerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror.json'
content_hash: 'sha256:1f5d57d4779c16b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# DecodingError

<sub>Enumeration</sub>

An error that occurs during the decoding of a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DecodingError
```

## Relationships

- **Conforms To**: [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Error](error.md), [Escapable](escapable.md), [LocalizedError](../foundation/localizederror.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Context](decodingerror/context.md) — The context in which the error occurred.

### Enumeration Cases

- [DecodingError.dataCorrupted(_:)](<decodingerror/datacorrupted(__).md>) — An indication that the data is corrupted or otherwise invalid.
- [DecodingError.keyNotFound(_:_:)](<decodingerror/keynotfound(____).md>) — An indication that a keyed decoding container was asked for an entry for the given key, but did not contain one.
- [DecodingError.typeMismatch(_:_:)](<decodingerror/typemismatch(____).md>) — An indication that a value of the given type could not be decoded because it did not match the type of what was found in the encoded payload.
- [DecodingError.valueNotFound(_:_:)](<decodingerror/valuenotfound(____).md>) — An indication that a non-optional value of the given type was expected, but a null value was found.

### Type Methods

- [dataCorruptedError(forKey:in:debugDescription:)](<decodingerror/datacorruptederror(forkey_in_debugdescription_).md>) — Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.
- [dataCorruptedError(in:debugDescription:)](<decodingerror/datacorruptederror(in_debugdescription_)-4ruvu.md>) — Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.
- [dataCorruptedError(in:debugDescription:)](<decodingerror/datacorruptederror(in_debugdescription_)-5on9z.md>) — Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

### Default Implementations

- [CustomDebugStringConvertible Implementations](decodingerror/customdebugstringconvertible-implementations.md)

## See Also

### Encoders and Decoders

- [Encoder](encoder.md) — A type that can encode values into a native format for external representation.
- [Decoder](decoder.md) — A type that can decode values from a native format into in-memory representations.
- [EncodingError](encodingerror.md) — An error that occurs during the encoding of a value.
