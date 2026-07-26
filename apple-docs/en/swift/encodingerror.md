---
title: EncodingError
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/encodingerror
source_url: 'https://developer.apple.com/documentation/swift/encodingerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encodingerror.json'
content_hash: 'sha256:83d2a4daad13d532'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# EncodingError

<sub>Enumeration</sub>

An error that occurs during the encoding of a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum EncodingError
```

## Relationships

- **Conforms To**: [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Error](error.md), [Escapable](escapable.md), [LocalizedError](../foundation/localizederror.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Structures

- [Context](encodingerror/context.md) — The context in which the error occurred.

### Enumeration Cases

- [EncodingError.invalidValue(_:_:)](<encodingerror/invalidvalue(____).md>) — An indication that an encoder or its containers could not encode the given value.

### Default Implementations

- [CustomDebugStringConvertible Implementations](encodingerror/customdebugstringconvertible-implementations.md)

## See Also

### Encoders and Decoders

- [Encoder](encoder.md) — A type that can encode values into a native format for external representation.
- [Decoder](decoder.md) — A type that can decode values from a native format into in-memory representations.
- [DecodingError](decodingerror.md) — An error that occurs during the decoding of a value.
