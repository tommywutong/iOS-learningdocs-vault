---
title: 'appendLiteral(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringinterpolationprotocol/appendliteral(_:)'
source_url: 'https://developer.apple.com/documentation/swift/stringinterpolationprotocol/appendliteral(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringinterpolationprotocol/appendliteral%28_%3A%29.json'
content_hash: 'sha256:132c2f8d1895471d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringInterpolationProtocol](../stringinterpolationprotocol.md)

# appendLiteral(_:)

<sub>Instance Method</sub>

Appends a literal segment to the interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendLiteral(_ literal: Self.StringLiteralType)
```

## Parameters

- `literal` — A string literal containing the characters that appear next in the string literal.

## Discussion

Don’t call this method directly. Instead, initialize a variable or constant using a string literal with interpolated expressions.

Interpolated expressions don’t pass through this method; instead, Swift selects an overload of `appendInterpolation`. For more information, see the top-level `StringInterpolationProtocol` documentation.
