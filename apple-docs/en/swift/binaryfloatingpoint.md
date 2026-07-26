---
title: BinaryFloatingPoint
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/binaryfloatingpoint
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint.json'
content_hash: 'sha256:4c8c4b9c3d55e7e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BinaryFloatingPoint

<sub>Protocol</sub>

A radix-2 (binary) floating-point type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol BinaryFloatingPoint : ExpressibleByFloatLiteral, FloatingPoint
```

## Overview

The `BinaryFloatingPoint` protocol extends the `FloatingPoint` protocol with operations specific to floating-point binary types, as defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933). `BinaryFloatingPoint` is implemented in the standard library by `Float`, `Double`, and `Float80` where available.

## Relationships

- **Inherits From**: [AdditiveArithmetic](additivearithmetic.md), [Comparable](comparable.md), [Equatable](equatable.md), [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FloatingPoint](floatingpoint.md), [Hashable](hashable.md), [Numeric](numeric.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md)

- **Conforming Types**: [Double](double.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md)

## Topics

### Converting Floating-Point Values

- [init(_:)](<binaryfloatingpoint/init(__)-57jx7.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<binaryfloatingpoint/init(__)-7ft14.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<binaryfloatingpoint/init(__)-1nijh.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<binaryfloatingpoint/init(__)-shau.md>) — Creates a new instance from the given value, rounded to the closest possible representation.

### Converting with No Loss of Precision

- [init(exactly:)](<binaryfloatingpoint/init(exactly_).md>) — Creates a new instance from the given value, if it can be represented exactly.

### Creating a Random Value

- [random(in:)](<binaryfloatingpoint/random(in_)-2j16p.md>) — Returns a random value within the specified range.
- [random(in:)](<binaryfloatingpoint/random(in_)-8jkjb.md>) — Returns a random value within the specified range.
- [random(in:using:)](<binaryfloatingpoint/random(in_using_)-6pf7f.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<binaryfloatingpoint/random(in_using_)-2awm8.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.

### Working with Binary Representation

- [binade](binaryfloatingpoint/binade.md) — The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
- [exponentBitPattern](binaryfloatingpoint/exponentbitpattern.md) — The raw encoding of the value’s exponent field.
- [significandBitPattern](binaryfloatingpoint/significandbitpattern.md) — The raw encoding of the value’s significand field.
- [significandWidth](binaryfloatingpoint/significandwidth.md) — The number of bits required to represent the value’s significand.
- [exponentBitCount](binaryfloatingpoint/exponentbitcount.md) — The number of bits used to represent the type’s exponent.
- [significandBitCount](binaryfloatingpoint/significandbitcount.md) — The available number of fractional significand bits.
- [init(sign:exponentBitPattern:significandBitPattern:)](<binaryfloatingpoint/init(sign_exponentbitpattern_significandbitpattern_).md>) — Creates a new instance from the specified sign and bit patterns.
- [RawExponent](binaryfloatingpoint/rawexponent.md) — A type that represents the encoded exponent of a value.
- [RawSignificand](binaryfloatingpoint/rawsignificand.md) — A type that represents the encoded significand of a value.

### Initializers

- [init(_:format:lenient:)](<binaryfloatingpoint/init(__format_lenient_)-166j0.md>)
- [init(_:format:lenient:)](<binaryfloatingpoint/init(__format_lenient_)-2b9qt.md>)
- [init(_:format:lenient:)](<binaryfloatingpoint/init(__format_lenient_)-2p118.md>) — Initialize an instance by parsing `value` with a `ParseStrategy` created with the given `format` and the `lenient` argument.
- [init(_:strategy:)](<binaryfloatingpoint/init(__strategy_)-4vta0.md>) — Initialize an instance by parsing `value` with the given `strategy`.

### Instance Methods

- [formatted()](<binaryfloatingpoint/formatted().md>) — Format `self` with `FloatingPointFormatStyle()`.
- [formatted(_:)](<binaryfloatingpoint/formatted(__)-4ksqj.md>) — Format `self` with the given format.
- [formatted(_:)](<binaryfloatingpoint/formatted(__)-83x4n.md>) — Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.

### Default Implementations

- [BinaryFloatingPoint Implementations](binaryfloatingpoint/binaryfloatingpoint-implementations.md)

## See Also

### Floating Point

- [FloatingPoint](floatingpoint.md) — A floating-point numeric type.
