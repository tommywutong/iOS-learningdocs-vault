---
title: ExpressibleByExtendedGraphemeClusterLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyextendedgraphemeclusterliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyextendedgraphemeclusterliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyextendedgraphemeclusterliteral.json'
content_hash: 'sha256:11970d088ed71ee5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByExtendedGraphemeClusterLiteral

<sub>Protocol</sub>

A type that can be initialized with a string literal containing a single extended grapheme cluster.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByExtendedGraphemeClusterLiteral : ExpressibleByUnicodeScalarLiteral
```

## Overview

An _extended grapheme cluster_ is a group of one or more Unicode scalar values that approximates a single user-perceived character.  Many individual characters, such as “é”, “김”, and “🇮🇳”, can be made up of multiple Unicode scalar values. These code points are combined by Unicode’s boundary algorithms into extended grapheme clusters.

The `String`, `StaticString`, and `Character` types conform to the `ExpressibleByExtendedGraphemeClusterLiteral` protocol. You can initialize a variable or constant of any of these types using a string literal that holds a single character.

```swift
let snowflake: Character = "❄︎"
print(snowflake)
// Prints "❄︎"
```

## Conforming to ExpressibleByExtendedGraphemeClusterLiteral

To add `ExpressibleByExtendedGraphemeClusterLiteral` conformance to your custom type, implement the required initializer.

## Relationships

- **Inherits From**: [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)

- **Inherited By**: [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](expressiblebystringliteral.md), [StringProtocol](stringprotocol.md)

- **Conforming Types**: [Character](character.md), [StaticString](staticstring.md), [String](string.md), [LocalizationValue](string/localizationvalue.md), [Substring](substring.md)

## Topics

### Associated Types

- [ExtendedGraphemeClusterLiteralType](expressiblebyextendedgraphemeclusterliteral/extendedgraphemeclusterliteraltype.md) — A type that represents an extended grapheme cluster literal.

### Initializers

- [init(extendedGraphemeClusterLiteral:)](<expressiblebyextendedgraphemeclusterliteral/init(extendedgraphemeclusterliteral_).md>) — Creates an instance initialized to the given value.

## See Also

### String Literals

- [ExpressibleByStringLiteral](expressiblebystringliteral.md) — A type that can be initialized with a string literal.
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md) — A type that can be initialized with a string literal containing a single Unicode scalar value.
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — Represents the contents of a string literal with interpolations while it’s being built up.
- [DefaultStringInterpolation](defaultstringinterpolation.md) — Represents a string literal with interpolations while it’s being built up.
