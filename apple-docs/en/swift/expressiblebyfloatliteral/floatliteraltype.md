---
title: FloatLiteralType
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyfloatliteral/floatliteraltype
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyfloatliteral/floatliteraltype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyfloatliteral/floatliteraltype.json'
content_hash: 'sha256:a1cd974767c23540'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ExpressibleByFloatLiteral](../expressiblebyfloatliteral.md)

# FloatLiteralType

<sub>Associated Type</sub>

A type that represents a floating-point literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype FloatLiteralType : _ExpressibleByBuiltinFloatLiteral
```

## Discussion

Valid types for `FloatLiteralType` are `Float`, `Double`, and `Float80` where available.
