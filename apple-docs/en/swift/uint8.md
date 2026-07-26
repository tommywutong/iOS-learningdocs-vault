---
title: UInt8
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint8
source_url: 'https://developer.apple.com/documentation/swift/uint8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8.json'
content_hash: 'sha256:5addada99444cee7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UInt8

<sub>Structure</sub>

An 8-bit unsigned integer value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UInt8
```

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryInteger](binaryinteger.md), [BitwiseCopyable](bitwisecopyable.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](cvararg.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FixedWidthInteger](fixedwidthinteger.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLTensorScalar](../coreml/mltensorscalar.md), [NetworkFixedWidthInteger](../network/networkfixedwidthinteger.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Strideable](strideable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md), [UnsignedInteger](unsignedinteger.md), [vDSP_IntegerConvertable](../accelerate/vdsp_integerconvertable.md)

## Topics

### Structures

- [Words](uint8/words-swift.struct.md) — A type that represents the words of this integer.

### Operators

- [!=(_:_:)](<uint8/!=(____).md>)
- [&=(_:_:)](<uint8/&=(____).md>) — Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [&\>\>=(_:_:)](<uint8/&__=(____)-172l7.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<uint8/&__=(____)-5wuaw.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [*=(_:_:)](<uint8/_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable.
- [+=(_:_:)](<uint8/+=(____).md>) — Adds two values and stores the result in the left-hand-side variable.
- [-=(_:_:)](<uint8/-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [==(_:_:)](<uint8/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<uint8/_(____)-140g8.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [%=(_:_:)](<uint8/_=(____)-12hmo.md>) — Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [^=(_:_:)](<uint8/_=(____)-23lmz.md>) — Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [|=(_:_:)](<uint8/_=(____)-56yu9.md>) — Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [/=(_:_:)](<uint8/_=(____)-7a5f0.md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable.

### Initializers

- [init(_:)](<uint8/init(__)-4e13y.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint8/init(__)-535b5.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint8/init(__)-8f7wu.md>)
- [init(_:)](<uint8/init(__)-8hqkq.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(_:)](<uint8/init(__)-ey6q.md>)
- [init(_:)](<uint8/init(__)-qdzq.md>) — Creates an integer from the given floating-point value, rounding toward zero.
- [init(ascii:)](<uint8/init(ascii_).md>) — Construct with value `v.value`.
- [init(bitPattern:)](<uint8/init(bitpattern_).md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<uint8/init(exactly_)-1ljfr.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint8/init(exactly_)-3la4a.md>)
- [init(exactly:)](<uint8/init(exactly_)-4mc0a.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint8/init(exactly_)-7wsjq.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<uint8/init(exactly_)-8rr3e.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating:)](<uint8/init(truncating_).md>)

### Instance Properties

- [byteSwapped](uint8/byteswapped.md) — A representation of this integer with the byte order swapped.
- [customPlaygroundQuickLook](uint8/customplaygroundquicklook.md) — A custom playground Quick Look for the `UInt8` instance. _(deprecated)_
- [leadingZeroBitCount](uint8/leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [nonzeroBitCount](uint8/nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.
- [trailingZeroBitCount](uint8/trailingzerobitcount.md) — The number of trailing zeros in this value’s binary representation.
- [words](uint8/words-swift.property.md) — A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

### Instance Methods

- [addingReportingOverflow(_:)](<uint8/addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<uint8/dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividingFullWidth(_:)](<uint8/dividingfullwidth(__).md>) — Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [multipliedFullWidth(by:)](<uint8/multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<uint8/multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<uint8/remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [signum()](<uint8/signum().md>) — Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [subtractingReportingOverflow(_:)](<uint8/subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Aliases

- [IntegerLiteralType](uint8/integerliteraltype.md) — A type that represents an integer literal.
- [Magnitude](uint8/magnitude.md) — A type that can represent the absolute value of any possible value of this type.
- [Stride](uint8/stride.md) — A type that represents the distance between two values.

### Type Properties

- [bitWidth](uint8/bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.

### Default Implementations

- [AdditiveArithmetic Implementations](uint8/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint8/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint8/binaryinteger-implementations.md)
- [Comparable Implementations](uint8/comparable-implementations.md)
- [CustomReflectable Implementations](uint8/customreflectable-implementations.md)
- [Decodable Implementations](uint8/decodable-implementations.md)
- [Encodable Implementations](uint8/encodable-implementations.md)
- [Equatable Implementations](uint8/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint8/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint8/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint8/hashable-implementations.md)
- [SIMDScalar Implementations](uint8/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint8/unsignedinteger-implementations.md)

## See Also

### Unsigned Integers

- [UInt](uint.md) — An unsigned integer value type.
- [UInt16](uint16.md) — A 16-bit unsigned integer value type.
- [UInt32](uint32.md) — A 32-bit unsigned integer value type.
- [UInt64](uint64.md) — A 64-bit unsigned integer value type.
- [UInt128](uint128.md) — A 128-bit unsigned integer value type.
