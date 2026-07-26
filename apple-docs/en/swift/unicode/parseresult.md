---
title: Unicode.ParseResult
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/parseresult
source_url: 'https://developer.apple.com/documentation/swift/unicode/parseresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/parseresult.json'
content_hash: 'sha256:607391bce8bb96ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.ParseResult

<sub>Enumeration</sub>

The result of attempting to parse a `T` from some input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ParseResult<T>
```

## Relationships

- **Conforms To**: [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Enumeration Cases

- [Unicode.ParseResult.emptyInput](parseresult/emptyinput.md) — The input was entirely consumed.
- [Unicode.ParseResult.error(length:)](<parseresult/error(length_).md>) — An encoding error was detected.
- [Unicode.ParseResult.valid(_:)](<parseresult/valid(__).md>) — A `T` was parsed successfully

## See Also

### Unicode Codecs

- [UnicodeCodec](../unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](ascii.md)
- [UTF8](utf8.md)
- [UTF16](utf16.md)
- [UTF32](utf32.md)
- [UnicodeDecodingResult](../unicodedecodingresult.md) — The result of one Unicode decoding step.
