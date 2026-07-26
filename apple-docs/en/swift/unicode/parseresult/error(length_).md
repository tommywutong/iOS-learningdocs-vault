---
title: 'Unicode.ParseResult.error(length:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/parseresult/error(length:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/parseresult/error(length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/parseresult/error%28length%3A%29.json'
content_hash: 'sha256:4d88dbc618177c66'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [ParseResult](../parseresult.md)

# Unicode.ParseResult.error(length:)

<sub>Case</sub>

An encoding error was detected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case error(length: Int)
```

## Discussion

`length` is the number of underlying code units consumed by this error, guaranteed to be greater than 0.
