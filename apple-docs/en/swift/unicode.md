---
title: Unicode
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode
source_url: 'https://developer.apple.com/documentation/swift/unicode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode.json'
content_hash: 'sha256:87d41d8d03f8923c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Unicode

<sub>Enumeration</sub>

A namespace for Unicode utilities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Unicode
```

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Individual Unicode Scalar Values

- [Scalar](unicode/scalar.md) — A Unicode scalar value.

### Unicode Scalar Classifications

- [GeneralCategory](unicode/generalcategory.md) — The most general classification of a Unicode scalar.
- [CanonicalCombiningClass](unicode/canonicalcombiningclass.md) — The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.
- [NumericType](unicode/numerictype.md) — The numeric type of a scalar.

### Unicode Codecs

- [UnicodeCodec](unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](unicode/ascii.md)
- [UTF8](unicode/utf8.md)
- [UTF16](unicode/utf16.md)
- [UTF32](unicode/utf32.md)
- [UnicodeDecodingResult](unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](unicode/parseresult.md) — The result of attempting to parse a `T` from some input.

### Translation Between Unicode Encodings

- [transcode(_:from:to:stoppingOnError:into:)](<transcode(__from_to_stoppingonerror_into_).md>) — Translates the given input from one Unicode encoding to another by calling the given closure.

### Deprecated

- [UnicodeScalar](unicodescalar.md)
- [UTF8](utf8.md)
- [UTF16](utf16.md)
- [UTF32](utf32.md)

### Type Aliases

- [Encoding](unicode/encoding.md)
- [Parser](unicode/parser.md)
- [Version](unicode/version.md) — A version of the Unicode Standard represented by its major and minor components.
