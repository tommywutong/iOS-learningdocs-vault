---
title: ExpressibleByStringLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebystringliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebystringliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebystringliteral.json'
content_hash: 'sha256:b73514cf6c563600'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByStringLiteral

<sub>Protocol</sub>

A type that can be initialized with a string literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByStringLiteral : ExpressibleByExtendedGraphemeClusterLiteral
```

## Overview

The `String` and `StaticString` types conform to the `ExpressibleByStringLiteral` protocol. You can initialize a variable or constant of either of these types using a string literal of any length.

```swift
let picnicGuest = "Deserving porcupine"
```

## Conforming to ExpressibleByStringLiteral

To add `ExpressibleByStringLiteral` conformance to your custom type, implement the required initializer.

## Relationships

- **Inherits From**: [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)

- **Inherited By**: [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md), [StringProtocol](stringprotocol.md)

- **Conforming Types**: [StaticString](staticstring.md), [String](string.md), [LocalizationValue](string/localizationvalue.md), [Substring](substring.md)

## Topics

### Associated Types

- [StringLiteralType](expressiblebystringliteral/stringliteraltype.md) — A type that represents a string literal.

### Initializers

- [init(stringLiteral:)](<expressiblebystringliteral/init(stringliteral_).md>) — Creates an instance initialized to the given string value.

## See Also

### String Literals

- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md) — A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md) — A type that can be initialized with a string literal containing a single Unicode scalar value.
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — Represents the contents of a string literal with interpolations while it’s being built up.
- [DefaultStringInterpolation](defaultstringinterpolation.md) — Represents a string literal with interpolations while it’s being built up.
