---
title: AdditiveArithmetic
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/additivearithmetic
source_url: 'https://developer.apple.com/documentation/swift/additivearithmetic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/additivearithmetic.json'
content_hash: 'sha256:74fad1246bcbe6dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AdditiveArithmetic

<sub>Protocol</sub>

A type with values that support addition and subtraction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AdditiveArithmetic : Equatable
```

## Overview

The `AdditiveArithmetic` protocol provides a suitable basis for additive arithmetic on scalar values, such as integers and floating-point numbers, or vectors. You can write generic methods that operate on any numeric type in the standard library by using the `AdditiveArithmetic` protocol as a generic constraint.

The following code declares a method that calculates the total of any sequence with `AdditiveArithmetic` elements.

```swift
extension Sequence where Element: AdditiveArithmetic {
    func sum() -> Element {
        return reduce(.zero, +)
    }
}
```

The `sum()` method is now available on any sequence with values that conform to `AdditiveArithmetic`, whether it is an array of `Double` or a range of `Int`.

```swift
let arraySum = [1.1, 2.2, 3.3, 4.4, 5.5].sum()
// arraySum == 16.5

let rangeSum = (1..<10).sum()
// rangeSum == 45
```

## Conforming to the AdditiveArithmetic Protocol

To add `AdditiveArithmetic` protocol conformance to your own custom type, implement the required operators, and provide a static `zero` property.

## Relationships

- **Inherits From**: [Equatable](equatable.md)

- **Inherited By**: [BinaryFloatingPoint](binaryfloatingpoint.md), [BinaryInteger](binaryinteger.md), [DurationProtocol](durationprotocol.md), [FixedWidthInteger](fixedwidthinteger.md), [FloatingPoint](floatingpoint.md), [Numeric](numeric.md), [SignedInteger](signedinteger.md), [SignedNumeric](signednumeric.md), [UnsignedInteger](unsignedinteger.md)

- **Conforming Types**: [Double](double.md), [Duration](duration.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Operators

- [+(_:)](<additivearithmetic/+(__).md>) — Returns the given number unchanged.
- [+(_:_:)](<additivearithmetic/+(____).md>) — Adds two values and produces their sum.
- [+=(_:_:)](<additivearithmetic/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-(_:_:)](<additivearithmetic/-(____).md>) — Subtracts one value from another and produces their difference.
- [-=(_:_:)](<additivearithmetic/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.

### Type Properties

- [zero](additivearithmetic/zero.md) — The zero value.

## See Also

### Basic Arithmetic

- [Numeric](numeric.md) — A type with values that support multiplication.
- [SignedNumeric](signednumeric.md) — A numeric type with a negation operation.
- [Strideable](strideable.md) — A type representing continuous, one-dimensional values that can be offset and measured.
