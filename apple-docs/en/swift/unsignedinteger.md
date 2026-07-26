---
title: UnsignedInteger
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsignedinteger
source_url: 'https://developer.apple.com/documentation/swift/unsignedinteger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsignedinteger.json'
content_hash: 'sha256:304187ebb2b5e71e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsignedInteger

<sub>Protocol</sub>

An integer type that can represent only nonnegative values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UnsignedInteger : BinaryInteger
```

## Relationships

- **Inherits From**: [AdditiveArithmetic](additivearithmetic.md), [BinaryInteger](binaryinteger.md), [Comparable](comparable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [Hashable](hashable.md), [Numeric](numeric.md), [Strideable](strideable.md)

- **Conforming Types**: [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Instance Methods

- [dividingFullWidth(_:)](<unsignedinteger/dividingfullwidth(__).md>)

### Type Properties

- [max](unsignedinteger/max.md) — The maximum representable integer in this type.
- [min](unsignedinteger/min.md) — The minimum representable integer in this type.

## See Also

### Integer

- [BinaryInteger](binaryinteger.md) — An integer type with a binary representation.
- [FixedWidthInteger](fixedwidthinteger.md) — An integer type that uses a fixed size for every instance.
- [SignedInteger](signedinteger.md) — An integer type that can represent both positive and negative values.
