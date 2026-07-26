---
title: UnicodeCodec
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicodecodec
source_url: 'https://developer.apple.com/documentation/swift/unicodecodec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicodecodec.json'
content_hash: 'sha256:e63e4b76810ed4c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnicodeCodec

<sub>Protocol</sub>

A Unicode encoding form that translates between Unicode scalar values and form-specific code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UnicodeCodec : _UnicodeEncoding
```

## Overview

The `UnicodeCodec` protocol declares methods that decode code unit sequences into Unicode scalar values and encode Unicode scalar values into code unit sequences. The standard library implements codecs for the UTF-8, UTF-16, and UTF-32 encoding schemes as the `UTF8`, `UTF16`, and `UTF32` types, respectively. Use the `Unicode.Scalar` type to work with decoded Unicode scalar values.

## Relationships

- **Conforming Types**: [UTF16](unicode/utf16.md), [UTF32](unicode/utf32.md), [UTF8](unicode/utf8.md)

## Topics

### Initializers

- [init()](<unicodecodec/init().md>) — Creates an instance of the codec.

### Instance Methods

- [decode(_:)](<unicodecodec/decode(__).md>) — Starts or continues decoding a code unit sequence into Unicode scalar values.

### Type Methods

- [encode(_:into:)](<unicodecodec/encode(__into_).md>) — Encodes a Unicode scalar as a series of code units by calling the given closure on each code unit.

## See Also

### Unicode Codecs

- [ASCII](unicode/ascii.md)
- [UTF8](unicode/utf8.md)
- [UTF16](unicode/utf16.md)
- [UTF32](unicode/utf32.md)
- [UnicodeDecodingResult](unicodedecodingresult.md) — The result of one Unicode decoding step.
- [ParseResult](unicode/parseresult.md) — The result of attempting to parse a `T` from some input.
