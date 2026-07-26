---
title: ExpressibleByNilLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebynilliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebynilliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebynilliteral.json'
content_hash: 'sha256:0b13fb22f096c088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByNilLiteral

<sub>Protocol</sub>

A type that can be initialized using the nil literal, `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByNilLiteral : ~Copyable, ~Escapable
```

## Overview

`nil` has a specific meaning in Swift—the absence of a value. Only the `Optional` type conforms to `ExpressibleByNilLiteral`. `ExpressibleByNilLiteral` conformance for types that use `nil` for other purposes is discouraged.

## Relationships

- **Conforming Types**: [Optional](optional.md)

## Topics

### Initializers

- [init(nilLiteral:)](<expressiblebynilliteral/init(nilliteral_).md>) — Creates an instance initialized with `nil`.

## See Also

### Value Literals

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — A type that can be initialized with an integer literal.
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — A type that can be initialized with a floating-point literal.
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — A type that can be initialized with the Boolean literals `true` and `false`.
- [StaticBigInt](staticbigint.md) — An immutable arbitrary-precision signed integer.
