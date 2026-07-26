---
title: BooleanLiteralType
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/booleanliteraltype
source_url: 'https://developer.apple.com/documentation/swift/booleanliteraltype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/booleanliteraltype.json'
content_hash: 'sha256:9c3c20fc4c49782a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BooleanLiteralType

<sub>Type Alias</sub>

The default type for an otherwise-unconstrained Boolean literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias BooleanLiteralType = Bool
```

## Discussion

When you create a constant or variable using one of the Boolean literals `true` or `false`, the resulting type is determined by the `BooleanLiteralType` alias. For example:

```swift
let isBool = true
print("isBool is a '\(type(of: isBool))'")
// Prints "isBool is a 'Bool'"
```

The type aliased by `BooleanLiteralType` must conform to the `ExpressibleByBooleanLiteral` protocol.

## See Also

### Basic Values

- [IntegerLiteralType](integerliteraltype.md) — The default type for an otherwise-unconstrained integer literal.
- [FloatLiteralType](floatliteraltype.md) — The default type for an otherwise-unconstrained floating-point literal.
