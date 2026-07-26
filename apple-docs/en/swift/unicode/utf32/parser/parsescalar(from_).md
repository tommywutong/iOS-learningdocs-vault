---
title: 'parseScalar(from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf32/parser/parsescalar(from:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf32/parser/parsescalar(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf32/parser/parsescalar%28from%3A%29.json'
content_hash: 'sha256:1be06f2b9afea7d6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [UTF32](../../utf32.md) · [Parser](../parser.md)

# parseScalar(from:)

<sub>Instance Method</sub>

Parses a single Unicode scalar value from `input`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func parseScalar<I>(from input: inout I) -> Unicode.ParseResult<Unicode.UTF32.Parser.Encoding.EncodedScalar> where I : IteratorProtocol, I.Element == UInt32
```
