---
title: 'init(unchecked:isKnownASCII:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/init(unchecked:isknownascii:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/init(unchecked:isknownascii:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/init%28unchecked%3Aisknownascii%3A%29.json'
content_hash: 'sha256:03cb2bbf519ea547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# init(unchecked:isKnownASCII:)

<sub>Initializer</sub>

Creates a UTF8Span, bypassing safety and security checks. The caller must guarantee that `codeUnits` contains validly-encoded UTF-8, or else undefined behavior may result upon use. If `isKnownASCII: true is passed`, the contents must be ASCII, or else undefined behavior may result upon use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(unchecked codeUnits: Span<UInt8>, isKnownASCII: Bool = false)
```
