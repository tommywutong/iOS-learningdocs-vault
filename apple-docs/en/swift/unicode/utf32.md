---
title: Unicode.UTF32
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf32
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf32'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf32.json'
content_hash: 'sha256:6096ba4a87c7b8d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.UTF32

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum UTF32
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Copyable](../copyable.md), [Equatable](../equatable.md), [Escapable](../escapable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [UnicodeCodec](../unicodecodec.md)

## Topics

### Structures

- [Parser](utf32/parser.md)

### Operators

- [==(_:_:)](<utf32/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Instance Properties

- [hashValue](utf32/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<utf32/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Aliases

- [CodeUnit](utf32/codeunit.md) — The basic unit of encoding
- [EncodedScalar](utf32/encodedscalar.md) — A valid scalar value as represented in this encoding
- [ForwardParser](utf32/forwardparser.md) — A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [ReverseParser](utf32/reverseparser.md) — A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.

### Type Properties

- [encodedReplacementCharacter](utf32/encodedreplacementcharacter.md) — A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.

### Type Methods

- [decode(_:)](<utf32/decode(__)-swift.type.method.md>) — Converts from encoded to encoding-independent representation
- [encode(_:)](<utf32/encode(__).md>) — Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [isASCII(_:)](<utf32/isascii(__).md>) — Returns whether the given code unit represents an ASCII scalar

### Default Implementations

- [Equatable Implementations](utf32/equatable-implementations.md)
- [UnicodeCodec Implementations](utf32/unicodecodec-implementations.md)

## See Also

### Unicode Codecs

- [UnicodeCodec](../unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](ascii.md)
- [UTF8](utf8.md)
- [UTF16](utf16.md)
- [UnicodeDecodingResult](../unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](parseresult.md) — The result of attempting to parse a `T` from some input.
