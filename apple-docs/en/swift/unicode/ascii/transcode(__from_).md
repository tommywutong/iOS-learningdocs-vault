---
title: 'transcode(_:from:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/ascii/transcode(_:from:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii/transcode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii/transcode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:42f77c83b0ea65b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [ASCII](../ascii.md)

# transcode(_:from:)

<sub>Type Method</sub>

Converts a scalar from another encoding’s representation, returning `nil` if the scalar can’t be represented in this encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func transcode<FromEncoding>(_ content: FromEncoding.EncodedScalar, from _: FromEncoding.Type) -> Unicode.ASCII.EncodedScalar? where FromEncoding : _UnicodeEncoding
```

## Discussion

A default implementation of this method will be provided automatically for any conforming type that does not implement one.
