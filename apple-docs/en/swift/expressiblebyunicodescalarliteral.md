---
title: ExpressibleByUnicodeScalarLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyunicodescalarliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyunicodescalarliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyunicodescalarliteral.json'
content_hash: 'sha256:37396c6ea65a79a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByUnicodeScalarLiteral

<sub>Protocol</sub>

A type that can be initialized with a string literal containing a single Unicode scalar value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByUnicodeScalarLiteral
```

## Overview

The `String`, `StaticString`, `Character`, and `Unicode.Scalar` types all conform to the `ExpressibleByUnicodeScalarLiteral` protocol. You can initialize a variable of any of these types using a string literal that holds a single Unicode scalar.

```swift
let ñ: Unicode.Scalar = "ñ"
print(ñ)
// Prints "ñ"
```

## Conforming to ExpressibleByUnicodeScalarLiteral

To add `ExpressibleByUnicodeScalarLiteral` conformance to your custom type, implement the required initializer.

## Relationships

- **Inherited By**: [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](expressiblebystringliteral.md), [StringProtocol](stringprotocol.md)

- **Conforming Types**: [Character](character.md), [StaticString](staticstring.md), [String](string.md), [LocalizationValue](string/localizationvalue.md), [Substring](substring.md), [Scalar](unicode/scalar.md)

## Topics

### Associated Types

- [UnicodeScalarLiteralType](expressiblebyunicodescalarliteral/unicodescalarliteraltype.md) — A type that represents a Unicode scalar literal.

### Initializers

- [init(unicodeScalarLiteral:)](<expressiblebyunicodescalarliteral/init(unicodescalarliteral_).md>) — Creates an instance initialized to the given value.

## See Also

### String Literals

- [ExpressibleByStringLiteral](expressiblebystringliteral.md) — A type that can be initialized with a string literal.
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md) — A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — Represents the contents of a string literal with interpolations while it’s being built up.
- [DefaultStringInterpolation](defaultstringinterpolation.md) — Represents a string literal with interpolations while it’s being built up.
