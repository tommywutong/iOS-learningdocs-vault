---
title: Unicode.UTF16
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf16
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf16'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf16.json'
content_hash: 'sha256:84222be4c7dc8b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.UTF16

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum UTF16
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Copyable](../copyable.md), [Escapable](../escapable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [UnicodeCodec](../unicodecodec.md)

## Topics

### Structures

- [ForwardParser](utf16/forwardparser.md) — A type that can be used to parse `CodeUnits` into `EncodedScalar`s.
- [ReverseParser](utf16/reverseparser.md) — A type that can be used to parse a reversed sequence of `CodeUnits` into `EncodedScalar`s.

### Type Aliases

- [CodeUnit](utf16/codeunit.md) — The basic unit of encoding
- [EncodedScalar](utf16/encodedscalar.md) — A valid scalar value as represented in this encoding

### Type Properties

- [encodedReplacementCharacter](utf16/encodedreplacementcharacter.md) — A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.

### Type Methods

- [decode(_:)](<utf16/decode(__)-swift.type.method.md>) — Converts from encoded to encoding-independent representation
- [encode(_:)](<utf16/encode(__).md>) — Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.
- [isASCII(_:)](<utf16/isascii(__).md>) — Returns whether the given code unit represents an ASCII scalar
- [isLeadSurrogate(_:)](<utf16/isleadsurrogate(__).md>) — Returns a Boolean value indicating whether the specified code unit is a high-surrogate code unit.
- [isSurrogate(_:)](<utf16/issurrogate(__).md>) — Returns a Boolean value indicating whether the specified code unit is a high or low surrogate code unit.
- [isTrailSurrogate(_:)](<utf16/istrailsurrogate(__).md>) — Returns a Boolean value indicating whether the specified code unit is a low-surrogate code unit.
- [leadSurrogate(_:)](<utf16/leadsurrogate(__).md>) — Returns the high-surrogate code unit of the surrogate pair representing the specified Unicode scalar.
- [trailSurrogate(_:)](<utf16/trailsurrogate(__).md>) — Returns the low-surrogate code unit of the surrogate pair representing the specified Unicode scalar.
- [transcode(_:from:)](<utf16/transcode(__from_).md>) — Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.
- [transcodedLength(of:decodedAs:repairingIllFormedSequences:)](<utf16/transcodedlength(of_decodedas_repairingillformedsequences_).md>) — Returns the number of UTF-16 code units required for the given code unit sequence when transcoded to UTF-16, and a Boolean value indicating whether the sequence was found to contain only ASCII characters.
- [width(_:)](<utf16/width(__).md>) — Returns the number of code units required to encode the given Unicode scalar.

### Default Implementations

- [UnicodeCodec Implementations](utf16/unicodecodec-implementations.md)

## See Also

### Unicode Codecs

- [UnicodeCodec](../unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](ascii.md)
- [UTF8](utf8.md)
- [UTF32](utf32.md)
- [UnicodeDecodingResult](../unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](parseresult.md) — The result of attempting to parse a `T` from some input.
