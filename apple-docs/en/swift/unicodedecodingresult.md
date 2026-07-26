---
title: UnicodeDecodingResult
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicodedecodingresult
source_url: 'https://developer.apple.com/documentation/swift/unicodedecodingresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicodedecodingresult.json'
content_hash: 'sha256:d221b7f853e63091'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnicodeDecodingResult

<sub>Enumeration</sub>

The result of one Unicode decoding step.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum UnicodeDecodingResult
```

## Overview

Each `UnicodeDecodingResult` instance can represent a Unicode scalar value, an indication that no more Unicode scalars are available, or an indication of a decoding error.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<unicodedecodingresult/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [UnicodeDecodingResult.emptyInput](unicodedecodingresult/emptyinput.md) — An indication that no more Unicode scalars are available in the input.
- [UnicodeDecodingResult.error](unicodedecodingresult/error.md) — An indication of a decoding error.
- [UnicodeDecodingResult.scalarValue(_:)](<unicodedecodingresult/scalarvalue(__).md>) — A decoded Unicode scalar value.

### Default Implementations

- [Equatable Implementations](unicodedecodingresult/equatable-implementations.md)

## See Also

### Unicode Codecs

- [UnicodeCodec](unicodecodec.md) — A Unicode encoding form that translates between Unicode scalar values and form-specific code units.
- [ASCII](unicode/ascii.md)
- [UTF8](unicode/utf8.md)
- [UTF16](unicode/utf16.md)
- [UTF32](unicode/utf32.md)
- [ParseResult](unicode/parseresult.md) — The result of attempting to parse a `T` from some input.
