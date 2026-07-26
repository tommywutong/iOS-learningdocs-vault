---
title: UnicodeScalarLiteralType
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyunicodescalarliteral/unicodescalarliteraltype
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyunicodescalarliteral/unicodescalarliteraltype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyunicodescalarliteral/unicodescalarliteraltype.json'
content_hash: 'sha256:5f2f73aabf6934b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByUnicodeScalarLiteral](../expressiblebyunicodescalarliteral.md)

# UnicodeScalarLiteralType

<sub>Associated Type</sub>

A type that represents a Unicode scalar literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype UnicodeScalarLiteralType : _ExpressibleByBuiltinUnicodeScalarLiteral
```

## Discussion

Valid types for `UnicodeScalarLiteralType` are `Unicode.Scalar`, `Character`, `String`, and `StaticString`.
