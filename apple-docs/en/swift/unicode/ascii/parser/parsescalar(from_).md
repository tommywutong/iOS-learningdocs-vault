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
doc_path: '/documentation/swift/unicode/ascii/parser/parsescalar(from:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii/parser/parsescalar(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii/parser/parsescalar%28from%3A%29.json'
content_hash: 'sha256:330d4d2d2ee8d996'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [ASCII](../../ascii.md) · [Parser](../parser.md)

# parseScalar(from:)

<sub>Instance Method</sub>

Parses a single Unicode scalar value from `input`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func parseScalar<I>(from input: inout I) -> Unicode.ParseResult<Unicode.ASCII.Parser.Encoding.EncodedScalar> where I : IteratorProtocol, I.Element == UInt8
```
