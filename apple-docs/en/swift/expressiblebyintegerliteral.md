---
title: ExpressibleByIntegerLiteral
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/expressiblebyintegerliteral
source_url: 'https://developer.apple.com/documentation/swift/expressiblebyintegerliteral'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/expressiblebyintegerliteral.json'
content_hash: 'sha256:fafe765c8eb41799'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ExpressibleByIntegerLiteral

<sub>Protocol</sub>

A type that can be initialized with an integer literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ExpressibleByIntegerLiteral
```

## Overview

The standard library integer and floating-point types, such as `Int` and `Double`, conform to the `ExpressibleByIntegerLiteral` protocol. You can initialize a variable or constant of any of these types by assigning an integer literal.

```swift
// Type inferred as 'Int'
let cookieCount = 12

// An array of 'Int'
let chipsPerCookie = [21, 22, 25, 23, 24, 19]

// A floating-point value initialized using an integer literal
let redPercentage: Double = 1
// redPercentage == 1.0
```

## Conforming to ExpressibleByIntegerLiteral

To add `ExpressibleByIntegerLiteral` conformance to your custom type, implement the required initializer.

## Relationships

- **Inherited By**: [BinaryFloatingPoint](binaryfloatingpoint.md), [BinaryInteger](binaryinteger.md), [FixedWidthInteger](fixedwidthinteger.md), [FloatingPoint](floatingpoint.md), [Numeric](numeric.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [UnsignedInteger](unsignedinteger.md)

- **Conforming Types**: [Double](double.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [StaticBigInt](staticbigint.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Associated Types

- [IntegerLiteralType](expressiblebyintegerliteral/integerliteraltype.md) — A type that represents an integer literal.

### Initializers

- [init(integerLiteral:)](<expressiblebyintegerliteral/init(integerliteral_).md>) — Creates an instance initialized to the specified integer value.

## See Also

### Value Literals

- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — A type that can be initialized with a floating-point literal.
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — A type that can be initialized with the Boolean literals `true` and `false`.
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — A type that can be initialized using the nil literal, `nil`.
- [StaticBigInt](staticbigint.md) — An immutable arbitrary-precision signed integer.
