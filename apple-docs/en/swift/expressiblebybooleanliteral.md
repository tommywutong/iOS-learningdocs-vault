---
title: ExpressibleByBooleanLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebybooleanliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebybooleanliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebybooleanliteral.json'
content_hash: 'sha256:9754ae2fc01e9f9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByBooleanLiteral

<sub>Protocol</sub>

A type that can be initialized with the Boolean literals `true` and `false`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByBooleanLiteral
```

## Overview

`Bool`, `DarwinBoolean`, `ObjCBool`, and `WindowsBool` are treated as Boolean values. Expanding this set to include types that represent more than simple Boolean values is discouraged.

To add `ExpressibleByBooleanLiteral` conformance to your custom type, implement the `init(booleanLiteral:)` initializer that creates an instance of your type with the given Boolean value.

## Relationships

- **Conforming Types**: [Bool](bool.md)

## Topics

### Associated Types

- [BooleanLiteralType](expressiblebybooleanliteral/booleanliteraltype.md) — A type that represents a Boolean literal, such as `Bool`.

### Initializers

- [init(booleanLiteral:)](<expressiblebybooleanliteral/init(booleanliteral_).md>) — Creates an instance initialized to the given Boolean value.

## See Also

### Value Literals

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — A type that can be initialized with an integer literal.
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — A type that can be initialized with a floating-point literal.
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — A type that can be initialized using the nil literal, `nil`.
- [StaticBigInt](staticbigint.md) — An immutable arbitrary-precision signed integer.
