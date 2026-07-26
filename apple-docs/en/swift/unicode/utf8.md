---
title: Unicode.UTF8
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf8
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8.json'
content_hash: 'sha256:b3d614c17fe78964'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.UTF8

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum UTF8
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Copyable](../copyable.md), [Escapable](../escapable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [UnicodeCodec](../unicodecodec.md)

## Topics

### Structures

- [ForwardParser](utf8/forwardparser.md) — A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [ReverseParser](utf8/reverseparser.md) — A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.
- [ValidationError](utf8/validationerror.md) — The kind and location of a UTF-8 encoding error.

### Type Aliases

- [CodeUnit](utf8/codeunit.md) — The basic unit of encoding
- [EncodedScalar](utf8/encodedscalar.md) — A valid scalar value as represented in this encoding

### Type Properties

- [encodedReplacementCharacter](utf8/encodedreplacementcharacter.md) — A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.

### Type Methods

- [decode(_:)](<utf8/decode(__)-swift.type.method.md>) — Converts from encoded to encoding-independent representation
- [encode(_:)](<utf8/encode(__).md>) — Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [isASCII(_:)](<utf8/isascii(__).md>) — Returns whether the given code unit represents an ASCII scalar
- [isContinuation(_:)](<utf8/iscontinuation(__).md>) — Returns a Boolean value indicating whether the specified code unit is a UTF-8 continuation byte.
- [transcode(_:from:)](<utf8/transcode(__from_).md>) — Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.
- [width(_:)](<utf8/width(__).md>) — Returns the number of code units required to encode the given Unicode scalar.

### Default Implementations

- [UnicodeCodec Implementations](utf8/unicodecodec-implementations.md)

## See Also

### Unicode Codecs

- [UnicodeCodec](../unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](ascii.md)
- [UTF16](utf16.md)
- [UTF32](utf32.md)
- [UnicodeDecodingResult](../unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](parseresult.md) — The result of attempting to parse a `T` from some input.
