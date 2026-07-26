---
title: 'encode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/ascii/encode(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii/encode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii/encode%28_%3A%29.json'
content_hash: 'sha256:c7ce884408461a41'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [ASCII](../ascii.md)

# encode(_:)

<sub>Type Method</sub>

Converts from encoding-independent to encoded representation, returning `nil` if the scalar can’t be represented in this encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encode(_ source: Unicode.Scalar) -> Unicode.ASCII.EncodedScalar?
```
