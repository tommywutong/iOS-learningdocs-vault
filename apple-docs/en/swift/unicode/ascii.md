---
title: Unicode.ASCII
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/ascii
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii.json'
content_hash: 'sha256:05c82375b85c1852'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.ASCII

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ASCII
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Copyable](../copyable.md), [Escapable](../escapable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Structures

- [Parser](ascii/parser.md)

### Type Aliases

- [CodeUnit](ascii/codeunit.md) — The basic unit of encoding
- [EncodedScalar](ascii/encodedscalar.md) — A valid scalar value as represented in this encoding
- [ForwardParser](ascii/forwardparser.md) — A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [ReverseParser](ascii/reverseparser.md) — A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.

### Type Properties

- [encodedReplacementCharacter](ascii/encodedreplacementcharacter.md) — A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.

### Type Methods

- [decode(_:)](<ascii/decode(__).md>) — Converts from encoded to encoding-independent representation
- [encode(_:)](<ascii/encode(__).md>) — Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [isASCII(_:)](<ascii/isascii(__).md>) — Returns whether the given code unit represents an ASCII scalar
- [transcode(_:from:)](<ascii/transcode(__from_).md>) — Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.

## See Also

### Unicode Codecs

- [UnicodeCodec](../unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [UTF8](utf8.md)
- [UTF16](utf16.md)
- [UTF32](utf32.md)
- [UnicodeDecodingResult](../unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](parseresult.md) — The result of attempting to parse a `T` from some input.
