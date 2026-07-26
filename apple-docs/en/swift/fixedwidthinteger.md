---
title: FixedWidthInteger
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/fixedwidthinteger
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger.json'
content_hash: 'sha256:0aa0273eda3afb33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# FixedWidthInteger

<sub>Protocol</sub>

An integer type that uses a fixed size for every instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol FixedWidthInteger : BinaryInteger, LosslessStringConvertible where Self.Magnitude : FixedWidthInteger, Self.Magnitude : UnsignedInteger, Self.Stride : FixedWidthInteger, Self.Stride : SignedInteger
```

## Overview

The `FixedWidthInteger` protocol adds binary bitwise operations, bit shifts, and overflow handling to the operations supported by the `BinaryInteger` protocol.

Use the `FixedWidthInteger` protocol as a constraint or extension point when writing operations that depend on bit shifting, performing bitwise operations, catching overflows, or having access to the maximum or minimum representable value of a type. For example, the following code provides a `binaryString` property on every fixed-width integer that represents the number’s binary representation, split into 8-bit chunks.

```swift
extension FixedWidthInteger {
    var binaryString: String {
        var result: [String] = []
        for i in 0..<(Self.bitWidth / 8) {
            let byte = UInt8(truncatingIfNeeded: self >> (i * 8))
            let byteString = String(byte, radix: 2)
            let padding = String(repeating: "0",
                                 count: 8 - byteString.count)
            result.append(padding + byteString)
        }
        return "0b" + result.reversed().joined(separator: "_")
    }
}

print(Int16.max.binaryString)
// Prints "0b01111111_11111111"
print((101 as UInt8).binaryString)
// Prints "0b01100101"
```

The `binaryString` implementation uses the static `bitWidth` property and the right shift operator (`>>`), both of which are available to any type that conforms to the `FixedWidthInteger` protocol.

The next example declares a generic `squared` function, which accepts an instance `x` of any fixed-width integer type. The function uses the `multipliedReportingOverflow(by:)` method to multiply `x` by itself and check whether the result is too large to represent in the same type.

```swift
func squared<T: FixedWidthInteger>(_ x: T) -> T? {
    let (result, overflow) = x.multipliedReportingOverflow(by: x)
    if overflow {
        return nil
    }
    return result
}

let (x, y): (Int8, Int8) = (9, 123)
print(squared(x))
// Prints "Optional(81)"
print(squared(y))
// Prints "nil"
```

## Conforming to the FixedWidthInteger Protocol

To make your own custom type conform to the `FixedWidthInteger` protocol, declare the required initializers, properties, and methods. The required methods that are suffixed with `ReportingOverflow` serve as the customization points for arithmetic operations. When you provide just those methods, the standard library provides default implementations for all other arithmetic methods and operators.

## Relationships

- **Inherits From**: [AdditiveArithmetic](additivearithmetic.md), [BinaryInteger](binaryinteger.md), [Comparable](comparable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [Numeric](numeric.md), [Strideable](strideable.md)

- **Conforming Types**: [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md)

## Topics

### Operators

- [&*(_:_:)](<fixedwidthinteger/&_(____).md>) — Returns the product of the two given values, wrapping the result in case of any overflow.
- [&*=(_:_:)](<fixedwidthinteger/&_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&+(_:_:)](<fixedwidthinteger/&+(____).md>) — Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](<fixedwidthinteger/&+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-(_:_:)](<fixedwidthinteger/&-(____).md>) — Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&-=(_:_:)](<fixedwidthinteger/&-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&\>\>(_:_:)](<fixedwidthinteger/&__(____)-1sn91.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\<\<(_:_:)](<fixedwidthinteger/&__(____)-4j1s7.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\>\>=(_:_:)](<fixedwidthinteger/&__=(____)-2ffyd.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<fixedwidthinteger/&__=(____)-q186.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

### Initializers

- [init(_:radix:)](<fixedwidthinteger/init(__radix_).md>) — Creates a new integer value from the given string and radix.
- [init(bigEndian:)](<fixedwidthinteger/init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init(littleEndian:)](<fixedwidthinteger/init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.

### Instance Properties

- [bigEndian](fixedwidthinteger/bigendian.md) — The big-endian representation of this integer.
- [byteSwapped](fixedwidthinteger/byteswapped.md) — A representation of this integer with the byte order swapped.
- [leadingZeroBitCount](fixedwidthinteger/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [littleEndian](fixedwidthinteger/littleendian.md) — The little-endian representation of this integer.
- [nonzeroBitCount](fixedwidthinteger/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.

### Instance Methods

- [addingReportingOverflow(_:)](<fixedwidthinteger/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<fixedwidthinteger/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<fixedwidthinteger/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder obtained by dividing the given value by this value.
- [multipliedFullWidth(by:)](<fixedwidthinteger/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<fixedwidthinteger/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<fixedwidthinteger/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [subtractingReportingOverflow(_:)](<fixedwidthinteger/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Properties

- [bitWidth](fixedwidthinteger/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [max](fixedwidthinteger/max.md) — The maximum representable integer in this type.
- [min](fixedwidthinteger/min.md) — The minimum representable integer in this type.

### Type Methods

- [random(in:)](<fixedwidthinteger/random(in_)-3uaq4.md>) — Returns a random value within the specified range.
- [random(in:)](<fixedwidthinteger/random(in_)-467fr.md>) — Returns a random value within the specified range.
- [random(in:using:)](<fixedwidthinteger/random(in_using_)-33n1n.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<fixedwidthinteger/random(in_using_)-4byak.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.

## See Also

### Integer

- [BinaryInteger](binaryinteger.md) — An integer type with a binary representation.
- [SignedInteger](signedinteger.md) — An integer type that can represent both positive and negative values.
- [UnsignedInteger](unsignedinteger.md) — An integer type that can represent only nonnegative values.
