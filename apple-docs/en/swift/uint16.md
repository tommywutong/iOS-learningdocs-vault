---
title: UInt16
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint16
source_url: 'https://developer.apple.com/documentation/swift/uint16'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16.json'
content_hash: 'sha256:6dee768defca722b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UInt16

<sub>Structure</sub>

A 16-bit unsigned integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UInt16
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLTensorScalar](../coreml/mltensorscalar.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Strideable](strideable.md), [UnsignedInteger](unsignedinteger.md), [vDSP_IntegerConvertable](../accelerate/vdsp_integerconvertable.md)

## Topics

### Structures

- [Words](uint16/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<uint16/!=(____).md>)
- [&=(_:_:)](<uint16/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\<\<=(_:_:)](<uint16/&__=(____)-4uh81.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<uint16/&__=(____)-54gew.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<uint16/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<uint16/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<uint16/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<uint16/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<uint16/_(____)-9tmro.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [|=(_:_:)](<uint16/_=(____)-2tboh.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [%=(_:_:)](<uint16/_=(____)-5c5xh.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [/=(_:_:)](<uint16/_=(____)-7gmk4.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [^=(_:_:)](<uint16/_=(____)-7q4om.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.

### Initializers

- [init(_:)](<uint16/init(__)-1x3ws.md>)
- [init(_:)](<uint16/init(__)-2gsqf.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint16/init(__)-5vkwt.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint16/init(__)-67c9u.md>)
- [init(_:)](<uint16/init(__)-754ls.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint16/init(__)-8jre.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern:)](<uint16/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<uint16/init(exactly_)-1l0o7.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint16/init(exactly_)-1n42w.md>)
- [init(exactly:)](<uint16/init(exactly_)-3qv86.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint16/init(exactly_)-4ljt.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint16/init(exactly_)-8jto3.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<uint16/init(truncating_).md>)

### Instance Properties

- [byteSwapped](uint16/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](uint16/customplaygroundquicklook.md) — A custom playground Quick Look for the `UInt16` instance. _(deprecated)_
- [leadingZeroBitCount](uint16/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [nonzeroBitCount](uint16/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](uint16/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](uint16/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<uint16/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<uint16/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<uint16/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<uint16/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<uint16/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<uint16/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<uint16/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<uint16/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](uint16/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](uint16/magnitude.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](uint16/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](uint16/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](uint16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint16/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint16/binaryinteger-implementations.md)
- [Comparable Implementations](uint16/comparable-implementations.md)
- [CustomReflectable Implementations](uint16/customreflectable-implementations.md)
- [Decodable Implementations](uint16/decodable-implementations.md)
- [Encodable Implementations](uint16/encodable-implementations.md)
- [Equatable Implementations](uint16/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint16/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint16/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint16/hashable-implementations.md)
- [SIMDScalar Implementations](uint16/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint16/unsignedinteger-implementations.md)

## See Also

### Unsigned Integers

- [UInt](uint.md) — An unsigned integer value type.
- [UInt8](uint8.md) — An 8-bit unsigned integer value type.
- [UInt32](uint32.md) — A 32-bit unsigned integer value type.
- [UInt64](uint64.md) — A 64-bit unsigned integer value type.
- [UInt128](uint128.md) — A 128-bit unsigned integer value type.
