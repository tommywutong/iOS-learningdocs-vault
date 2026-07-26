---
title: SignedInteger
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/signedinteger
source_url: 'https://developer.apple.com/documentation/swift/signedinteger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/signedinteger.json'
content_hash: 'sha256:8d4afb035036494d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SignedInteger

<sub>Protocol</sub>

An integer type that can represent both positive and negative values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SignedInteger : BinaryInteger, SignedNumeric
```

## Relationships

- **Inherits From**: [AdditiveArithmetic](additivearithmetic.md), [BinaryInteger](binaryinteger.md), [Comparable](comparable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [Hashable](hashable.md), [Numeric](numeric.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md)

- **Conforming Types**: [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md)

## Topics

### Instance Methods

- [dividingFullWidth(_:)](<signedinteger/dividingfullwidth(__).md>)

### Type Properties

- [max](signedinteger/max.md) — The maximum representable integer in this type.
- [min](signedinteger/min.md) — The minimum representable integer in this type.

## See Also

### Integer

- [BinaryInteger](binaryinteger.md) — An integer type with a binary representation.
- [FixedWidthInteger](fixedwidthinteger.md) — An integer type that uses a fixed size for every instance.
- [UnsignedInteger](unsignedinteger.md) — An integer type that can represent only nonnegative values.
