---
title: String.StringInterpolation
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/stringinterpolation
source_url: 'https://developer.apple.com/documentation/swift/string/stringinterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/stringinterpolation.json'
content_hash: 'sha256:c5836639271fc84e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.StringInterpolation

<sub>Type Alias</sub>

The type each segment of a string literal containing interpolations should be appended to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias StringInterpolation = DefaultStringInterpolation
```

## Discussion

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.
