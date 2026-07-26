---
title: ExpressibleByFloatLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyfloatliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyfloatliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyfloatliteral.json'
content_hash: 'sha256:34cc0ec00e4bbd78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByFloatLiteral

<sub>Protocol</sub>

A type that can be initialized with a floating-point literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByFloatLiteral
```

## Overview

The standard library floating-point types—`Float`, `Double`, and `Float80` where available—all conform to the `ExpressibleByFloatLiteral` protocol. You can initialize a variable or constant of any of these types by assigning a floating-point literal.

```swift
// Type inferred as 'Double'
let threshold = 6.0

// An array of 'Double'
let measurements = [2.2, 4.1, 3.65, 4.2, 9.1]
```

## Conforming to ExpressibleByFloatLiteral

To add `ExpressibleByFloatLiteral` conformance to your custom type, implement the required initializer.

## Relationships

- **Inherited By**: [BinaryFloatingPoint](binaryfloatingpoint.md)

- **Conforming Types**: [Double](double.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md)

## Topics

### Associated Types

- [FloatLiteralType](expressiblebyfloatliteral/floatliteraltype.md) — A type that represents a floating-point literal.

### Initializers

- [init(floatLiteral:)](<expressiblebyfloatliteral/init(floatliteral_).md>) — Creates an instance initialized to the specified floating-point value.

## See Also

### Value Literals

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — A type that can be initialized with an integer literal.
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — A type that can be initialized with the Boolean literals `true` and `false`.
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — A type that can be initialized using the nil literal, `nil`.
- [StaticBigInt](staticbigint.md) — An immutable arbitrary-precision signed integer.
